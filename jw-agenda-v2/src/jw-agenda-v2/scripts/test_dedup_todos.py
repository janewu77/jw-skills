#!/usr/bin/env python3
"""dedup_todos.py 测试用例"""

import os
import sys
import tempfile
import unittest

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dedup_todos import normalize, extract_items, _path_under_root


class TestNormalize(unittest.TestCase):
    """测试归一化函数"""

    def test_basic_checkbox_removal(self):
        """测试移除 checkbox 标记"""
        self.assertEqual(normalize("- [ ] 写报告"), "写报告")
        self.assertEqual(normalize("- [x] 写报告"), "写报告")

    def test_source_mark_removal(self):
        """测试移除来源标记"""
        self.assertEqual(normalize("- [ ] 写报告 *(从昨天转移)*"), "写报告")
        self.assertEqual(normalize("- [ ] 写报告 *(来自规划)*"), "写报告")
        self.assertEqual(normalize("- [ ] 写报告 *(从 3.15 移入)*"), "写报告")
        self.assertEqual(normalize("- [ ] 写报告 *(临时追加)*"), "写报告")

    def test_chinese_note_removal(self):
        """测试移除中文备注"""
        self.assertEqual(normalize("- [ ] 写报告（进行中）"), "写报告")
        self.assertEqual(normalize("- [ ] 写报告（取消）"), "写报告")
        self.assertEqual(normalize("- [ ] 写报告（推迟）"), "写报告")

    def test_whitespace_handling(self):
        """测试空格处理"""
        self.assertEqual(normalize("  - [ ] 写报告  "), "写报告")
        self.assertEqual(normalize("- [ ]  写报告"), "写报告")

    def test_punctuation_removal(self):
        """测试标点移除"""
        self.assertEqual(normalize("- [ ] 写报告。"), "写报告")
        self.assertEqual(normalize("- [ ] 写报告，"), "写报告")

    def test_case_insensitive(self):
        """测试大小写不敏感"""
        self.assertEqual(normalize("- [ ] Write Report"), "write report")
        self.assertEqual(normalize("- [ ] WRITE REPORT"), "write report")

    def test_combined_marks(self):
        """测试组合标记"""
        result = normalize("- [x] 写报告 *(从昨天转移)*（进行中）")
        self.assertEqual(result, "写报告")

    def test_plain_text(self):
        """测试纯文本（无 checkbox）"""
        self.assertEqual(normalize("写报告"), "写报告")
        self.assertEqual(normalize("写报告 *(来自规划)*"), "写报告")


class TestExtractItems(unittest.TestCase):
    """测试条目提取"""

    def setUp(self):
        """创建临时目录"""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """清理临时文件"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_extract_from_file(self):
        """测试从文件提取条目"""
        filepath = os.path.join(self.temp_dir, "test.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("# Todo\n")
            f.write("- [ ] 任务一\n")
            f.write("- [x] 任务二\n")
            f.write("普通文本\n")
            f.write("- [ ] 任务三 *(来自规划)*\n")

        items = extract_items(filepath)
        self.assertEqual(len(items), 3)
        self.assertIn("任务一", items)
        self.assertIn("任务二", items)
        self.assertIn("任务三", items)

    def test_extract_nonexistent_file(self):
        """测试提取不存在的文件"""
        items = extract_items("/nonexistent/path/file.md")
        self.assertEqual(items, [])

    def test_extract_empty_file(self):
        """测试提取空文件"""
        filepath = os.path.join(self.temp_dir, "empty.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("")
        items = extract_items(filepath)
        self.assertEqual(items, [])


class TestPathSecurity(unittest.TestCase):
    """测试路径安全检查"""

    def test_path_under_root(self):
        """测试路径在根目录下"""
        root = "/home/user/workspace"
        self.assertTrue(_path_under_root("/home/user/workspace/file.md", root))
        self.assertTrue(_path_under_root("/home/user/workspace/sub/file.md", root))

    def test_path_outside_root(self):
        """测试路径不在根目录下"""
        root = "/home/user/workspace"
        self.assertFalse(_path_under_root("/home/user/other/file.md", root))
        self.assertFalse(_path_under_root("/etc/passwd", root))

    def test_path_traversal_attempt(self):
        """测试路径遍历攻击"""
        root = "/home/user/workspace"
        # 相对路径会被转换为绝对路径进行比较
        # 这个测试取决于当前工作目录，所以我们测试绝对路径
        self.assertFalse(_path_under_root("/home/user/workspace/../other/file.md", root))


class TestDeduplication(unittest.TestCase):
    """测试去重逻辑"""

    def setUp(self):
        """创建临时目录"""
        self.temp_dir = tempfile.mkdtemp()
        # 设置 WORKSPACE_ROOT 为临时目录
        os.environ["WORKSPACE_ROOT"] = self.temp_dir

    def tearDown(self):
        """清理"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        if "WORKSPACE_ROOT" in os.environ:
            del os.environ["WORKSPACE_ROOT"]

    def test_dedup_same_content(self):
        """测试相同内容去重"""
        existing = os.path.join(self.temp_dir, "existing.md")
        new_items = os.path.join(self.temp_dir, "new.txt")

        with open(existing, "w", encoding="utf-8") as f:
            f.write("- [ ] 写报告\n")
            f.write("- [x] 开会\n")

        with open(new_items, "w", encoding="utf-8") as f:
            f.write("- [ ] 写报告\n")  # 重复
            f.write("- [ ] 新任务\n")  # 新

        # 使用 extract_items 模拟去重逻辑
        existing_items = set(extract_items(existing))

        # 读取新条目
        with open(new_items, "r", encoding="utf-8") as f:
            new_lines = [line.strip() for line in f if line.strip()]

        # 过滤出新条目
        unique_new = [line for line in new_lines if normalize(line) not in existing_items]

        self.assertEqual(len(unique_new), 1)
        self.assertIn("新任务", unique_new[0])

    def test_dedup_with_different_marks(self):
        """测试不同标记但相同内容的去重"""
        existing = os.path.join(self.temp_dir, "existing.md")
        new_items = os.path.join(self.temp_dir, "new.txt")

        with open(existing, "w", encoding="utf-8") as f:
            f.write("- [ ] 写报告 *(来自规划)*\n")

        with open(new_items, "w", encoding="utf-8") as f:
            f.write("- [ ] 写报告 *(从昨天转移)*\n")  # 内容相同，标记不同

        existing_items = set(extract_items(existing))

        with open(new_items, "r", encoding="utf-8") as f:
            new_lines = [line.strip() for line in f if line.strip()]

        unique_new = [line for line in new_lines if normalize(line) not in existing_items]

        # 应该被去重（内容相同）
        self.assertEqual(len(unique_new), 0)


if __name__ == "__main__":
    unittest.main()
