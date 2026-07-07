# Tests

单元测试覆盖 `skills/jw-agenda-v2/scripts/` 下的两个工具脚本。

## 测试文件

| 文件 | 覆盖模块 |
|------|---------|
| `test_date_utils.py` | `scripts/date_utils.py`：日期计算、周数、跨年、闰年 |
| `test_dedup_todos.py` | `scripts/dedup_todos.py`：去重、归一化、路径安全 |

## 运行方式

从 `tests/` 目录运行：

```bash
cd jw-agenda-v2/tests

# 运行所有测试
python3 -m unittest -v

# 只运行某个文件
python3 -m unittest test_date_utils -v
python3 -m unittest test_dedup_todos -v
```

也可以从项目根目录运行：

```bash
cd jw-agenda-v2
python3 -m unittest discover -s tests -v
```
