# Cascade Update Conventions

> Loaded on demand: daily-log, weekly-review, monthly-review, weekly-plan, add-or-move, and planning-sync modes read this file before starting.

## Cascade Update Mechanism

The planning system has five levels, from top to bottom: tasks/TODO (master backlog) → yearly plan (optional) → monthly plan → weekly plan → daily plan. Each Skill mode must check and sync layer by layer in the appropriate direction to ensure consistency across all levels.

**Top-down (planning operations)**: When adjusting tasks or generating plans, check from tasks/TODO downward to the daily plan, ensuring tasks are properly broken down to each level. Applies to daily-todo (add/move task) and weekly-plan.

**Bottom-up (review operations)**: When recording logs or generating reviews, check from daily plan/log upward to the yearly plan, syncing completion status. Applies to daily-log and weekly-review. Only make **lightweight marks** on upper-level planning files (`[x]`, in progress, etc.) — do not alter the planning content itself.

**Shared rules**: Each level is only modified when actually affected, but every level must be checked — none may be skipped. After completing the operation, all modified file paths must be reported to the user.

| Skill | Direction | Cascade Path |
|-------|-----------|-------------|
| daily-todo (add/move) | Top-down | tasks/TODO → monthly → weekly → daily |
| weekly-plan | Top-down | tasks/TODO → monthly (read-only) → weekly → existing daily plans |
| daily-log | Bottom-up | daily → weekly → monthly → yearly (lightweight marks) |
| weekly-review | Bottom-up | logs (source of truth) → weekly → monthly → yearly (lightweight marks) |
| planning-sync | Bidirectional | Full-level post-hoc consistency check |

## Bottom-up Cascade Sync Standard Steps

For **each upper-level planning file** within the check scope, execute in order:

1. Find the corresponding entry in that level's file for each completed/in-progress task from this operation (use normalized keyword matching, allowing slight wording differences)
2. Update status marks: completed → `[x]`; in progress → append `(in progress)`; cancelled → `[x] (cancelled)`
3. **Only update status marks — do not alter the planning content itself** (preserve structure, wording, and order as-is)
4. Each level is only modified when **actually affected**, but **every level must be checked — none may be skipped**
5. Yearly plan is an optional level; if the file does not exist, skip it without notifying the user

## Top-down Cascade Sync Standard Steps

Check and update layer by layer in the following order:

1. **tasks/TODO.md (master backlog)**: Tasks assigned to specific dates are marked "planned" or removed; newly added tasks with no specific date are written to this file
2. **Monthly plan (monthly/YYYY-MM-plan.md)**: If the task involves monthly goals, cross-week changes, or new items for the current month, reflect it in the monthly plan; if a task is cancelled or postponed to next month, update the status (specific read/write permissions per mode are defined in mode files)
3. **Weekly plan (weekly/Week{W}-plan.md)**: Update the corresponding day's tasks in the target week; if cross-week, update both the source and target week plan files
4. **Daily plan (daily/YYYY-MM-DD-todo.md)**: Idempotent append, skip existing entries (specific handling per mode is defined in mode files)
5. Each level is only modified when **actually affected**, but **every level must be checked — none may be skipped**

## Conflict Resolution Strategy (When Multiple Sources Disagree)

When daily todo / daily log and weekly plan / monthly plan show inconsistent descriptions or status for the same task, resolve by the following priority (used by planning-sync and routine sync):

| Priority | Data Source | Explanation |
|----------|-------------|-------------|
| 1 (highest) | Daily todo / daily log | The **daily execution record** is authoritative. E.g., if daily todo is checked complete, the weekly plan's corresponding item should sync to completed; if the daily log records "incomplete" or "cancelled", the weekly plan follows the daily record. |
| 2 | Weekly plan | When the daily level has no record, the weekly plan is authoritative; when weekly and monthly conflict, weekly takes precedence (closer to execution). |
| 3 | Monthly plan | Only authoritative when weekly and daily have no record. |
| 4 | Yearly plan | Only authoritative when monthly, weekly, and daily have no record. Yearly plan is optional. |

Principle: **Whoever is closer to "what actually happened" takes priority**. Daily execution is the factual record; weekly/monthly/yearly are planning layers. Sync flows from daily → weekly → monthly → yearly upward.
