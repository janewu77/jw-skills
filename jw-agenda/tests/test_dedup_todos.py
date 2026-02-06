"""Unit tests for dedup_todos.py: normalize, extract_items, and dedup result (main)."""
import os
import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

from dedup_todos import extract_items, main, normalize


class TestNormalize:
    """Tests for normalize(text)."""

    def test_strips_checkbox_unchecked(self):
        assert normalize("- [ ] 任务内容") == "任务内容"

    def test_strips_checkbox_checked(self):
        assert normalize("- [x] 已完成") == "已完成"

    def test_strips_source_mark(self):
        assert normalize("- [ ] 任务 *(来自规划)*") == "任务"
        assert normalize("- [ ] 项 *(从昨天转移)*") == "项"

    def test_strips_parenthesis_remark(self):
        assert normalize("- [ ] 事项（取消）") == "事项"
        assert normalize("- [x] 完成（取消）") == "完成"

    def test_lowercase(self):
        assert normalize("- [ ]  ABC ") == "abc"

    def test_strips_trailing_punctuation(self):
        assert normalize("- [ ] 任务。") == "任务"
        assert normalize("- [ ] 任务，、；") == "任务"

    def test_combined(self):
        assert normalize("- [x] 投递简历 *(来自规划)*（推迟）") == "投递简历"


class TestExtractItems:
    """Tests for extract_items(filepath)."""

    def test_extracts_checkbox_lines(self, tmp_path):
        f = tmp_path / "t.md"
        f.write_text("- [ ] 任务一\n- [x] 任务二\n")
        assert set(extract_items(str(f))) == {"任务一", "任务二"}

    def test_ignores_non_checkbox_lines(self, tmp_path):
        f = tmp_path / "t.md"
        f.write_text("# 标题\n- [ ] 唯一\n## 小节\n")
        assert extract_items(str(f)) == ["唯一"]

    def test_returns_empty_for_missing_file(self, tmp_path):
        assert extract_items(str(tmp_path / "nonexistent.md")) == []

    def test_returns_empty_for_empty_file(self, tmp_path):
        f = tmp_path / "empty.md"
        f.write_text("")
        assert extract_items(str(f)) == []

    def test_normalizes_extracted_items(self, tmp_path):
        f = tmp_path / "t.md"
        f.write_text("- [ ] 任务 *(来自规划)*\n")
        assert extract_items(str(f)) == ["任务"]


class TestMainDedupResult:
    """Tests for main() dedup output (paths under WORKSPACE_ROOT)."""

    def _run_main(self, existing_path: str, new_path: str, workspace_root: str) -> str:
        buf = StringIO()
        with patch.object(sys, "argv", ["dedup_todos.py", existing_path, new_path]):
            with patch.object(sys, "stdout", buf):
                with patch.dict(os.environ, {"WORKSPACE_ROOT": workspace_root}, clear=False):
                    main()
        return buf.getvalue()

    def test_outputs_only_new_items(self, tmp_path):
        """Lines already present (after normalize) in existing are not printed."""
        root = str(tmp_path)
        (tmp_path / "existing.md").write_text("- [ ] 任务A\n- [x] 任务B\n")
        (tmp_path / "new.txt").write_text(
            "- [ ] 任务A *(来自规划)*\n"  # duplicate
            "- [ ] 任务C\n"  # new
        )
        out = self._run_main(
            str(tmp_path / "existing.md"),
            str(tmp_path / "new.txt"),
            root,
        )
        lines = [l for l in out.strip().split("\n") if l.strip()]
        assert len(lines) == 1
        assert "任务C" in lines[0]
        assert "任务A" not in out or lines[0].strip() != "- [ ] 任务A *(来自规划)*"

    def test_outputs_nothing_when_all_duplicate(self, tmp_path):
        root = str(tmp_path)
        (tmp_path / "existing.md").write_text("- [ ] 任务A\n")
        (tmp_path / "new.txt").write_text("- [ ] 任务A *(来自规划)*\n")
        out = self._run_main(
            str(tmp_path / "existing.md"),
            str(tmp_path / "new.txt"),
            root,
        )
        assert out.strip() == ""

    def test_existing_file_missing_treated_as_empty(self, tmp_path):
        root = str(tmp_path)
        (tmp_path / "new.txt").write_text("- [ ] 任务X\n")
        out = self._run_main(
            str(tmp_path / "nonexistent.md"),
            str(tmp_path / "new.txt"),
            root,
        )
        assert "任务X" in out

    def test_rejects_path_outside_workspace(self, tmp_path):
        root = str(tmp_path)
        (tmp_path / "existing.md").write_text("")
        (tmp_path / "new.txt").write_text("- [ ] x\n")
        with patch.object(sys, "argv", ["dedup_todos.py", "/etc/passwd", str(tmp_path / "new.txt")]):
            with patch.object(sys, "stderr", StringIO()):
                with patch.dict(os.environ, {"WORKSPACE_ROOT": root}, clear=False):
                    with pytest.raises(SystemExit) as exc:
                        main()
        assert exc.value.code == 1
