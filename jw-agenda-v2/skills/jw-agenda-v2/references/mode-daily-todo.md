# Mode 1: Daily Todo (daily-todo)

Manage the full lifecycle of today's todo: generation and adjustment.

> **Additional loading**: `assets/conventions-marks.md`; Sub-mode C also requires `assets/conventions-cascade.md`.

**Schedule configuration**: Preferentially reads `{agendaRoot}/schedule-config.md`; if absent, uses `assets/schedule-config.example.md`. Fixed activities are not overwritten; only empty time slots are filled with tasks.

## Sub-mode Selection

Automatically selected based on user intent:

| Trigger Scenario | Sub-mode |
|-----------------|----------|
| `生成今天的计划`、`today plan` | Sub-mode A: Generate (see below) |
| `今天完成得怎么样`、`还剩哪些`、`how's it going`、`what's left` | Sub-mode B1: Query Progress (see below) |
| `Y 不做了`、`取消`、`推迟`、`cancel`、`postpone` etc. | Sub-mode B2: Update Status (see below) |
| `把 X 移到周三`、`move X to Wednesday`、`推迟到下周`、`加一项`、`add a task`、`明天要`、`本月要` etc. | Sub-mode C: Add/Move Task (see below) |

---

## Sub-mode A: Generate Daily Todo

### Step 1: Determine Date

Calculate today's date (YYYY-MM-DD), current month, and ISO week number (recommended: use this Skill's `scripts/date_utils.py`).

### Step 2: Read Sources

Read in order (skip if missing):

1. **Current month plan**: `{agendaRoot}/monthly/YYYY-MM-plan.md` (current year-month, e.g., 2026-02-plan.md; use date_utils to compute), extract this month's goals and this week's focus
2. **Current week plan**: `{agendaRoot}/weekly/Week{W}-plan.md`, extract suggested tasks for "today"
3. **Yesterday's incomplete**: From `{agendaRoot}/daily/{yesterday's date}-log.md` or `{yesterday's date}-todo.md`, unchecked items — **deferrable only** (see `assets/conventions.md` "Deferrable vs Non-Deferrable Tasks"). Drop non-deferrable items (daily v2, missed 投递日 batches, fixed events, etc.). For deferrable items still relevant in this week's plan, mark `*(结转)*`.
4. **Todo-prefixed files in tasks directory** (optional): e.g., `{agendaRoot}/tasks/TODO.md`, `todo-readinglist.md`, `todo-*.md`. Read unchecked items, selectively include in today's plan (e.g., 1–2 low-priority items). No source mark in output.

### Step 3: Merge, Deduplicate, Prioritize

**Idempotency check**: If today's todo already exists, read existing entries, normalize for comparison (ignoring checkmarks, source marks, leading/trailing whitespace); existing entries are not re-appended.

**Dedup rules**: Items with identical or highly similar content across sources (monthly plan, weekly plan, yesterday's incomplete, tasks lists) are kept only once. If a deferrable item appears in both yesterday's incomplete and this week's plan, keep once and mark `*(结转)*`.

**Non-deferrable filter**: Do not carry forward daily discipline, missed 投递 batches, or fixed events from yesterday. Today's plan defines only what belongs today.

**Source marks and priority**: Follow `assets/conventions-marks.md` — default no mark; only `*(结转)*` / `*(moved from M.D)*` when applicable. Follow writing-style rules (no 遗留/补做, no low-priority hedging).

### Step 4: Write File

**Path**: `{agendaRoot}/daily/{today's date}-todo.md`

Use the `templates/daily-todo-template.md` template. **Must include**:

0. **Theme line** (`{{THEME}}`, optional): A one-line focus for the day, drawn from this week's plan focus (e.g., "v2 收尾 + 投递"). Omit the line entirely if there is no clear theme.
1. **Today's schedule**: Preferentially read time slot config from `{agendaRoot}/schedule-config.md`; if absent, from this Skill's `assets/schedule-config.example.md`. Fill each time slot into one `| Time | Activity |` row (`{{SCHEDULE_ROWS}}`), taking today's tasks for the "Activity" column. Preferentially extract from the weekly plan's "today" time slots; if unavailable, allocate by priority. Each time slot should have a specific task.
2. **High/Medium/Low priority**: Task lists consistent with the schedule, for checking off. Source marks only for exceptions (`*(结转)*`, `*(moved from M.D)*`).

If the file already exists, only append non-duplicate new entries; if the schedule already exists, preserve it without overwriting.

### Step 5: Report

**Must first state**: The file path written/updated. Then describe the item count per priority level and source distribution.

---

## Sub-mode B: Track Daily Completion

### B1: Query Progress

Read today's todo, count completed (`[x]`) / incomplete (`[ ]`), summarize by priority. Do not modify the file.

### B2: Update Status

Identify the target entry and new status, update in today's todo: completed → `[x]`; in progress → `[ ]` with `(in progress)`; cancelled → `[x]` with `(cancelled)`; postponed without target date → add `(postponed)`; postponed with target date → transfer to Sub-mode C (Add/Move Task). Confirm and report the updated file path.

---

## Sub-mode C: Add/Move Task

Handle user adding new tasks or moving existing tasks to a target date.

**Triggers**: `加一项 XXX`、`add a task XXX`、`明天要 XXX`、`tomorrow need XXX`、`把 X 移到周三`、`move X to Wednesday`、`推迟到 2.10`、`postpone to 2.10`、`记一下 XXX`、`note down XXX`、`本周三要 XXX`、`本月要 XXX`、`以后要 XXX` etc.

**Detailed execution steps**: Read `references/mode-add-or-move.md` and follow its instructions.

---

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Target file does not exist (add/move task) | Create a minimal scaffold then append, or inform user |
