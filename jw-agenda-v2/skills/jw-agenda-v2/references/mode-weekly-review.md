# Mode 4: Weekly Review (weekly-review)

Aggregate this week's logs and todos, calculate completion rates and time allocation, generate a weekly review report, and identify items to carry over to next week.

> **Additional loading**: `assets/conventions-cascade.md`.

## Step 1: Determine Review Scope

Use this Skill's `scripts/date_utils.py` to calculate this/last week's date range and ISO week number (1–52).

- **Default**: This week (Monday through Sunday)
- If user says "last week review", use last week's date range

## Step 2: Aggregate Data

Read all files within this week's date range:

**Primary sources**:
- `{agendaRoot}/daily/{date}-log.md`: Read day by day, extract completed, incomplete, time allocation, learning/output
- `{agendaRoot}/daily/{date}-todo.md`: Read day by day for checkmark status, cross-validate with logs

**Optional sources**:
- `{agendaRoot}/weekly/Week{W}-plan.md`: Compare planned vs. actual

**Summary categories config**: Read `{agendaRoot}/summary-categories.md` (if absent, use this Skill's `assets/summary-categories.example.md`), obtain category list for Steps 3 and 4 to summarize output by category dimension.

Record which days have data and which are missing.

## Step 3: Statistical Analysis

**Completion rate**: `total checked items / total items × 100%`; days without a todo file are excluded. Break down by high/medium/low priority.

**Time allocation**: Extract from each daily log's "Time Allocation" section, aggregate by category.

**Output summary**: From each daily log's "Learning/Output" section, aggregate by the category dimensions defined in the summary categories config. Generate a sub-section (`### Category Name`) for each category, summarizing all activities and output for that dimension this week. If a category has no content this week, omit or write "None" (see empty category handling rules in conventions).

## Step 4: Generate Weekly Review

Use `templates/review-template.md` template, fill and write:

**Path**: `{agendaRoot}/weekly/Week{W}-review.md` (W = ISO week number, 1–52, matching weekly plan naming)

**Content**: Overall overview (completion rate, key achievements), category statistics, incomplete/pending items, **carry over to next week** list.

## Step 5: Bottom-up Cascade Status Sync

Follow the "Bottom-up Cascade Sync Standard Steps" in conventions-cascade.md, using the actual completion data from Steps 2–3 as basis. Check scope: weekly plan → monthly plan → yearly plan (if exists).

## Step 6: Archive Daily Directory

> **Can be triggered independently**: When user inputs `archive daily`, `archive logs`, etc., this step can be executed alone without completing the full weekly review flow. See the trigger phrase mapping table in `SKILL.md`.

Follow the **daily directory archival rule** in `conventions.md`:

- Read the `archiveAfterDays` config from `.jw-agenda.json` (default 14 days)
- If the config value ≤ 0, skip archival
- Scan `{agendaRoot}/daily/` root for `YYYY-MM-DD-todo.md` and `YYYY-MM-DD-log.md` files
- If a file's date is earlier than "today − archiveAfterDays", move it to the `{agendaRoot}/daily/YYYYMM/` subdirectory
- Create the subdirectory if it does not exist; files from the same month go into the same subdirectory
- After archival, inform user how many files were moved and the target subdirectory

## Step 7: Report

State: weekly review file path, completion rate, time allocation highlights, carry-over item count, archived file count (if any), **all file paths where status was synced**.

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Some dates missing logs | Use available logs for statistics, note missing dates in the report |
| All dates have no logs | Ask user whether to generate an empty scaffold |
| Logs lack time allocation data | Skip time statistics, note this in the report |
| Weekly review already exists | Ask user whether to overwrite; default is no overwrite |
| No todo files | Only count completed/incomplete items from logs |
