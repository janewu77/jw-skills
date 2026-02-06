#!/usr/bin/env python3
"""Todo 去重工具 - 归一化比较 todo 条目，输出去重后的列表。

用法：
    python3 dedup_todos.py existing.md new_items.txt

    existing.md  - 已有的 todo 文件（不存在时视为空，不报错）
    new_items.txt - 待追加的条目（每行一条，可带来源标记）

路径安全：两个路径必须位于 workspace 根目录之下（或环境变量 WORKSPACE_ROOT 指定
的目录之下），否则拒绝执行，避免路径遍历。仅传入约定目录（如 personal/agenda 下）
内的路径。

输出：仅输出不在 existing.md 中的新条目（已去重），每行一条。

文件缺失：若 existing.md 不存在，视为无已有条目；若 new_items.txt 不存在，
则向 stderr 输出错误信息并 exit(1)。
"""

import os
import re
import sys


def _allowed_root() -> str:
    """Workspace 根目录：环境变量 WORKSPACE_ROOT 或当前工作目录。"""
    return os.path.abspath(os.environ.get("WORKSPACE_ROOT", os.getcwd()))


def _path_under_root(path: str, root: str) -> bool:
    """判定 path 的绝对路径是否在 root 之下（防止路径遍历）。"""
    abs_path = os.path.abspath(path)
    try:
        return os.path.commonpath([root, abs_path]) == root
    except ValueError:
        return False  # 不同盘符（Windows）等


def normalize(text: str) -> str:
    """归一化：去掉勾选状态、来源标记、前后空格、列表符号。"""
    text = text.strip()
    # 去掉 markdown checkbox
    text = re.sub(r"^-\s*\[[ x]\]\s*", "", text)
    # 去掉来源标记
    text = re.sub(r"\*\(.*?\)\*", "", text)
    # 去掉备注标记
    text = re.sub(r"（.*?）", "", text)
    # 去掉前后空格和标点
    text = text.strip().strip("。，、；")
    return text.lower()


def extract_items(filepath: str) -> list[str]:
    """从 markdown 文件中提取 todo 条目的归一化文本。"""
    items = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if re.match(r"^-\s*\[[ x]\]", line):
                    items.append(normalize(line))
    except FileNotFoundError:
        pass
    return items


def main():
    if len(sys.argv) < 3:
        print("用法: python3 dedup_todos.py existing.md new_items.txt", file=sys.stderr)
        sys.exit(1)

    existing_file = sys.argv[1]
    new_file = sys.argv[2]

    root = _allowed_root()
    for name, path in [("existing", existing_file), ("new", new_file)]:
        if not _path_under_root(path, root):
            print(
                f"dedup_todos: 路径不允许（必须在 workspace 内）: {path}",
                file=sys.stderr,
            )
            sys.exit(1)

    existing_normalized = set(extract_items(existing_file))

    try:
        with open(new_file, "r", encoding="utf-8") as f:
            new_lines = f.readlines()
    except FileNotFoundError:
        print(f"dedup_todos: 文件不存在: {new_file}", file=sys.stderr)
        sys.exit(1)

    for line in new_lines:
        line = line.strip()
        if not line:
            continue
        if normalize(line) not in existing_normalized:
            print(line)


if __name__ == "__main__":
    main()
