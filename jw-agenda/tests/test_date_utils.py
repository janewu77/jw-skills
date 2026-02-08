"""Unit tests for date_utils.py: get_date_info and CLI (--yesterday, --week-range)."""
import json
import os
import sys
from datetime import date
from unittest.mock import patch

import pytest

from date_utils import get_date_info, main


def _capture_stdout(argv, today_iso=None):
    from io import StringIO
    buf = StringIO()
    env = {k: v for k, v in os.environ.items()}
    if today_iso is not None:
        env["DATE_UTILS_TODAY"] = today_iso
    with patch.object(sys, "argv", ["date_utils.py"] + argv), patch.object(sys, "stdout", buf):
        with patch.dict(os.environ, env, clear=False):
            main()
    return buf.getvalue()


class TestGetDateInfo:
    """Tests for get_date_info(d)."""

    def test_structure_and_keys(self):
        """Output has all expected keys."""
        d = date(2026, 2, 5)
        info = get_date_info(d)
        want = {
            "date", "date_cn", "weekday", "month", "day",
            "year_week", "year_week_label", "week_plan_file", "week_review_file",
            "month_plan_file", "todo_file", "log_file",
            "week_monday", "week_sunday",
        }
        assert set(info.keys()) == want

    def test_fixed_date_2026_02_05(self):
        """2026-02-05 is Thursday, year week 6, week Mon 02-02 to Sun 02-08."""
        info = get_date_info(date(2026, 2, 5))
        assert info["date"] == "2026-02-05"
        assert info["date_cn"] == "2026年2月5日"
        assert info["weekday"] == "周四"
        assert info["month"] == 2
        assert info["day"] == 5
        assert info["year_week"] == 6
        assert info["year_week_label"] == "Week6"
        assert info["week_plan_file"] == "Week6-plan.md"
        assert info["week_review_file"] == "Week6-review.md"
        assert info["month_plan_file"] == "2026-02-plan.md"
        assert info["todo_file"] == "2026-02-05-todo.md"
        assert info["log_file"] == "2026-02-05-log.md"
        assert info["week_monday"] == "2026-02-02"
        assert info["week_sunday"] == "2026-02-08"

    def test_year_week_range(self):
        """year_week is ISO week of year, typically 1–52, sometimes 53."""
        info = get_date_info(date(2026, 2, 5))
        assert 1 <= info["year_week"] <= 53
        info_jan = get_date_info(date(2026, 1, 5))
        assert 1 <= info_jan["year_week"] <= 53

    def test_year_week_feb_29_leap_year(self):
        """2024-02-29 (leap year) has a valid year_week (ISO week 9)."""
        info = get_date_info(date(2024, 2, 29))
        assert info["year_week"] == 9
        assert info["year_week_label"] == "Week9"
        assert info["week_review_file"] == "Week9-review.md"

    def test_week_monday_sunday(self):
        """week_monday/week_sunday are Mon–Sun of the ISO week."""
        # 2026-02-05 Thursday → Mon 2026-02-02, Sun 2026-02-08
        info = get_date_info(date(2026, 2, 5))
        assert info["week_monday"] == "2026-02-02"
        assert info["week_sunday"] == "2026-02-08"


class TestMainCLI:
    """Tests for main() (CLI). Uses DATE_UTILS_TODAY env for deterministic --yesterday/--week-range."""

    def test_main_with_iso_date(self):
        """python3 date_utils.py 2026-02-05 → JSON with date and yesterday."""
        out = _capture_stdout(["2026-02-05"])
        data = json.loads(out)
        assert data["date"] == "2026-02-05"
        assert "yesterday" in data
        assert data["yesterday"]["date"] == "2026-02-04"

    def test_main_yesterday(self):
        """--yesterday with DATE_UTILS_TODAY=2026-02-06 → target 2026-02-05."""
        out = _capture_stdout(["--yesterday"], today_iso="2026-02-06")
        data = json.loads(out)
        assert data["date"] == "2026-02-05"
        assert data["yesterday"]["date"] == "2026-02-04"

    def test_main_week_range(self):
        """--week-range with DATE_UTILS_TODAY=2026-02-05 → 7 days Mon–Sun."""
        out = _capture_stdout(["--week-range"], today_iso="2026-02-05")
        data = json.loads(out)
        assert "week_range" in data
        days = data["week_range"]
        assert len(days) == 7
        assert days[0]["date"] == "2026-02-02"  # Monday
        assert days[0]["weekday"] == "周一"
        assert days[6]["date"] == "2026-02-08"  # Sunday
        assert days[6]["weekday"] == "周日"

    def test_main_invalid_date_exits_nonzero(self):
        """Invalid date string → stderr message and exit(1)."""
        from io import StringIO
        err = StringIO()
        with patch.object(sys, "argv", ["date_utils.py", "2026/02/05"]):
            with patch.object(sys, "stderr", err):
                with pytest.raises(SystemExit) as exc:
                    main()
        assert exc.value.code == 1
        assert "无效日期" in err.getvalue() or "invalid" in err.getvalue().lower()
