# 维护说明

## 运行测试

### 测试前需要安装

- **Python 3.9+**（脚本使用 `list[str]` 等类型提示）
- **pytest**：`pip install pytest`

### 如何运行测试

在仓库根目录或本目录（jw-agenda）下执行：

```bash
# 从仓库根
pytest jw-agenda/tests/ -v

# 或进入 jw-agenda 后
cd jw-agenda
pytest tests/ -v
```

测试位于 `jw-agenda/tests/`，当前包含 `test_date_utils.py`（对 `_common/scripts/date_utils.py` 的单元测试）。`conftest.py` 会将 `_common/scripts` 加入 Python 路径，无需额外配置即可导入脚本。

## 修改约定或脚本后保持 5 个 Skill 一致

约定（conventions）、作息模板（schedule-config.example）和脚本（date_utils.py、dedup_todos.py）的**唯一来源**是 `_common/`。修改 `_common/` 下任何文件后，请执行：

```bash
./scripts/sync-common-to-skills.sh
```

脚本会把 `_common/` 的内容同步到每个 skill 的 `assets/`（conventions.md、schedule-config.example.md、scripts/）。提交时请同时包含 `_common/` 与各 skill 的 `assets/` 变更。

## 版本与维护

- **命名与路径**：以各 Skill 的 `assets/conventions.md`（或本仓库 `_common/conventions.md`）为准：月规划 `YYYY-MM-plan.md`，周规划 `Week{N}-plan.md`，周总结 `Week{N}-review.md`。若某 Skill 内路径描述与 conventions 不一致，以 conventions 为准。
- **Skill 版本**：各 Skill 的 SKILL.md 中含 `author: Jing Wu`、`version`、`updated`。版本号格式 `0.M.P`：单 skill 更新时第三位 +0.0.1（如 0.0.1→0.0.2）；**配合版本升级**时，所有 skill 的第二位（0.X）对齐升级（如统一升为 0.1.0），便于整组协同发布。
