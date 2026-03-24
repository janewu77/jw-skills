# 模板变量命名约定

> 开发参考文档，运行时无需加载。

模板文件（`templates/*.md`）中的占位符统一使用 `{{UPPER_SNAKE_CASE}}` 格式：

| 类别 | 示例 | 说明 |
|------|------|------|
| 日期 | `{{DATE}}`、`{{START_DATE}}`、`{{END_DATE}}` | 日期相关 |
| 周/月 | `{{WEEK_NUM}}`、`{{YEAR_MONTH}}` | 周号或年月 |
| 任务列表 | `{{COMPLETED_TASKS}}`、`{{INCOMPLETE_TASKS}}`、`{{CARRY_OVER_ITEMS}}` | 任务列表（复数） |
| 单个任务 | `{{TASK}}` | 占位符，表示此处填入具体任务 |
| 时间 | `{{TIMESTAMP}}`、`{{TIME_ALLOCATION}}`、`{{ACTUAL_WORK_TIME}}` | 时间戳或时间分配 |
| 统计计数 | `{{COMPLETED_COUNT}}`、`{{TOTAL_COUNT}}`、`{{ACTION_COUNT}}` | 数量统计（以 `_COUNT` 结尾） |
| 统计比率 | `{{COMPLETION_RATE}}` | 比率统计（以 `_RATE` 结尾） |

**命名规则**：
- 全大写，单词间用下划线分隔
- 使用完整单词而非缩写（如 `{{WEEK_NUM}}` 而非 `{{W}}`）
- 列表用 `_ITEMS` 后缀（如 `{{COMPLETED_TASKS}}`）
- 数量用 `_COUNT` 后缀；比率用 `_RATE` 后缀
