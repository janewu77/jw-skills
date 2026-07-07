# Mode: Add/Move Task

Handle user adding new tasks or moving existing tasks to a target date.

> **Additional loading**: `assets/conventions-marks.md` + `assets/conventions-cascade.md`.

## Triggers

`加一项 XXX`、`add a task XXX`、`明天要 XXX`、`tomorrow need XXX`、`把 X 移到周三`、`move X to Wednesday`、`推迟到 2.10`、`postpone to 2.10`、`记一下 XXX`、`note down XXX`、`本周三要 XXX`、`本月要 XXX`、`以后要 XXX` etc.

## Step 1: Identify Task and Target Date

Extract from user input: **task content** and **target date** (today/tomorrow/this week X/this month/next week/specific date/someday). If no date is specified, default to today. If ambiguous, calculate the specific date first and confirm with the user if necessary.

Based on the target date, determine which files to write (write sequentially from coarser to finer granularity):

| Time Scope | Files to Write |
|------------|---------------|
| **Cannot determine date** / **Not something to do this month** | `{agendaRoot}/tasks/TODO.md` |
| Today / tomorrow / a specific day this week | ① `{agendaRoot}/monthly/YYYY-MM-plan.md` → ② `{agendaRoot}/weekly/Week{W}-plan.md` → ③ `{agendaRoot}/daily/YYYY-MM-DD-todo.md` |
| This week (no specific day) / next week / a specific week | ① `{agendaRoot}/monthly/YYYY-MM-plan.md` → ② `{agendaRoot}/weekly/Week{W}-plan.md` |
| This month / later (further out) | `{agendaRoot}/monthly/YYYY-MM-plan.md` |

## Step 2: Determine Move vs. Add

Check if the same or similar task exists in today's todo (normalized comparison, ignoring marks and whitespace):
- **Exists**: Treat as a move, record the original date (today)
- **Does not exist**: Treat as a new addition

## Step 3: Update Source Date (Move Only)

If this is a move, delete the entry from today's todo.

## Step 4: Update Target Date

- If the target day's todo exists: Idempotency check then append
- If it does not exist: Create a file containing only this item (recommended to create immediately for consistency)
- **Marks** (see `assets/conventions-marks.md`; mark only exceptions):
  - Move: `*(moved from M.D)*` (M.D is the original date, e.g., `2.5` for February 5)
  - New addition: no mark by default; add one only if clarity truly requires it

## Step 5: Top-down Cascade Sync Planning Files

**Core principle**: After each task adjustment, **every level must be checked top-down** to ensure all planning levels remain consistent. Do not modify only the daily plan while ignoring upper-level planning files.

Follow the "Top-down Cascade Sync Standard Steps" in conventions-cascade.md. Mode-specific behavior:

- **5a tasks/TODO.md**: If the task came from the master backlog and is now assigned to a specific date → mark as planned or remove; new tasks with no specific date → write to the master backlog; cancelled tasks → mark accordingly
- **5d Daily plan**: Already handled in Steps 3–4 (updated source and target date todos), skip here

## Step 6: Report

State the operation type (move/add), target date, and synced files. **Must list all modified file paths** (e.g., `{agendaRoot}/tasks/TODO.md`, `{agendaRoot}/monthly/...`, `{agendaRoot}/weekly/...`, `{agendaRoot}/daily/{date}-todo.md`) so the user knows where changes landed.

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Target file does not exist | Automatically create a new file containing only this item, inform user of the created path |
| Source task not found (during move) | Inform user the task was not found in today's todo, ask whether to add as new instead, or provide a different source date |
| Cross-month boundary (target date is in the next month) | Handle normally, update the target month's monthly plan (`YYYY-MM-plan.md`) instead of the current month |
| Cross-year boundary (target date is in the next year) | Handle normally, also update the target year's weekly and monthly plans; if a yearly plan (`YYYY-plan.md`) is involved, check it as well |
