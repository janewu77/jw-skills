# 维护说明

## 修改约定或脚本后保持 5 个 Skill 一致

约定（conventions）、作息模板（schedule-config.example）和脚本（date_utils.py、dedup_todos.py）的**唯一来源**是 `_common/`。修改 `_common/` 下任何文件后，请执行：

```bash
./scripts/sync-common-to-skills.sh
```

脚本会把 `_common/` 的内容同步到每个 skill 的 `assets/`（conventions.md、schedule-config.example.md、scripts/）。提交时请同时包含 `_common/` 与各 skill 的 `assets/` 变更。
