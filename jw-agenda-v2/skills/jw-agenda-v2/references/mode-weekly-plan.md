# Mode 3: Weekly Plan (weekly-plan)

Generate this week's day-by-day plan based on monthly plan goals and tasks carried over from last week.

> **Additional loading**: `assets/conventions-cascade.md`.

**Note**: This mode generates a draft plan. Users may adjust daily assignments after generation. Mode 1 (Daily Todo) reads this file as one source for the daily plan.

## Step 1: Determine Current Week

Use this Skill's `scripts/date_utils.py` to calculate: ISO week number (1–52), this week's date range (Monday through Sunday), and last week's date range.

## Step 2: Read Monthly Plan

- **Path**: `{agendaRoot}/monthly/YYYY-MM-plan.md` (current month, e.g., 2026-02-plan.md; use date_utils to compute)
- **Extract**: Focus areas, core tasks, and output targets from the `Week {W}` subsection in the monthly plan
- If the monthly plan does not exist, see error handling

## Step 3: Read Carry-over Tasks from Last Week

Read in priority order:
1. **Last week's review** (if exists): `{agendaRoot}/weekly/Week{W-1}-review.md`, the "Carry Over to Next Week" section
2. **Last week's logs**: Logs from `{agendaRoot}/daily/` within last week's date range, extract "Incomplete" sections
3. **Last week's todos**: Unchecked items from `{agendaRoot}/daily/{last week dates}-todo.md`
4. **Todo-prefixed files in tasks directory** (optional): e.g., `{agendaRoot}/tasks/TODO.md`, `todo-readinglist.md`, `todo-*.md`. Unchecked items serve as "candidates for this week", selectively assigned to specific days (grouped on certain days or distributed by priority)

Compile into a carry-over task list.

## Step 4: Generate Weekly Plan

Use the `templates/week-template.md` template structure.

**Assignment principles** (by priority and dependencies):
- **Priority**: 🔴 High → early week (Mon–Wed); 🟡 Medium → mid-week (Tue–Thu); 🟢 Low → late week or weekend. High-priority/urgent carry-over tasks take precedence over new tasks, scheduled for Monday or Tuesday.
- **Dependencies**: Identify dependency chains (e.g., research → prepare → submit); prerequisite tasks come first, dependent tasks after, with possible 1-day gap.
- **Splitting and balancing**: Large tasks are split into 2–3 day sub-tasks; daily recurring tasks are marked "Daily" in the overview table's "Scheduled Day" column; target 2–4 items per day; time-sensitive items placed near their deadlines.

**Operation**: Extract tasks from the monthly plan and carry-over list, identify priorities and dependencies → assign to days per above principles → fill the "📋 Weekly Task Overview" table and daily sections (`- [ ] ...`), with source marks: `*(from plan)*` / `*(carried over from last week)*`.

**If `Week{W}-plan.md` already exists**: Incremental update. Preserve completed items (`- [x]`), user additions, and manual adjustments; only append new tasks that are non-duplicate after normalization; do not overwrite the user's modifications to dates, priorities, or status.

## Step 5: Write File

**Path**: `{agendaRoot}/weekly/Week{W}-plan.md`

Create the directory if it does not exist.

## Step 6: Top-down Cascade Sync

Follow the "Top-down Cascade Sync Standard Steps" in conventions-cascade.md. Mode-specific behavior:

- **tasks/TODO.md**: Tasks included in this week's plan are marked as planned or removed from the master backlog, preventing the same task from being repeatedly pulled into future weekly plans
- **Monthly plan (read-only)**: Maintained by the user; this mode does not modify it, only reads it in Step 2
- **Existing daily plans**: If a day's plan already exists, idempotent append (marked `*(from plan)*`); if it does not exist, do not create it (leave for Mode 1 to handle)

## Step 7: Report

State: file path, this week's focus, carry-over task count, **all synced file paths**. Suggest using Mode 1 to generate daily plans.

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Monthly plan does not exist | Inform user, ask whether to generate a skeleton based solely on carry-over tasks |
| Monthly plan has no subsection for current week | Use the monthly plan's overall goals as reference |
| Cross-month boundary (e.g., 1.29–2.4) | Attribute to the month containing the week's end date; see conventions.md |
