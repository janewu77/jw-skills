# Template Variable Naming Conventions

> Developer reference document; not loaded at runtime.

Template files (`templates/*.md`) use `{{UPPER_SNAKE_CASE}}` placeholders:

| Category | Examples | Description |
|----------|----------|-------------|
| Date | `{{DATE}}`, `{{START_DATE}}`, `{{END_DATE}}` | Date-related |
| Week/Month | `{{WEEK_NUM}}`, `{{YEAR_MONTH}}` | Week number or year-month |
| Task lists | `{{COMPLETED_TASKS}}`, `{{INCOMPLETE_TASKS}}`, `{{CARRY_OVER_ITEMS}}` | Task lists (plural) |
| Single task | `{{TASK}}` | Placeholder for a specific task |
| Time | `{{TIMESTAMP}}`, `{{TIME_ALLOCATION}}`, `{{ACTUAL_WORK_TIME}}` | Timestamps or time allocation |
| Count stats | `{{COMPLETED_COUNT}}`, `{{TOTAL_COUNT}}`, `{{ACTION_COUNT}}` | Quantity statistics (suffix `_COUNT`) |
| Rate stats | `{{COMPLETION_RATE}}` | Rate statistics (suffix `_RATE`) |

**Naming rules**:
- All uppercase, words separated by underscores
- Use full words, not abbreviations (e.g., `{{WEEK_NUM}}` not `{{W}}`)
- Lists use `_ITEMS` suffix (e.g., `{{COMPLETED_TASKS}}`)
- Counts use `_COUNT` suffix; rates use `_RATE` suffix
