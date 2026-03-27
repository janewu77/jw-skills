# Mode 2: Daily Log (daily-log)

Summarize yesterday's work and generate a log, or organize today's conversational progress report into a log; carry over incomplete items to today's todo.

> **Additional loading**: `assets/conventions-cascade.md`.

**Division of responsibility with Mode 1**: Adjustments to incomplete or unstarted tasks are handled by Mode 1 (Daily Todo).

**Conversational reporting**: Users may report progress casually with thoughts mixed in. Parse from the report: completed items, incomplete items, time allocation; thoughts, feelings, and casual remarks go into the log's "Today's Thoughts / Quick Notes" section, preserving original meaning without discarding.

## Two Usage Patterns

| User Intent | Handling |
|-------------|----------|
| Summarize yesterday / organize yesterday's log | Read yesterday's todo and existing data → generate yesterday's log → carry over incomplete to today |
| Report today / log today (including casual, thoughts) | Parse user's conversational report for today → generate today's log → sync-update today's todo checkmarks → keep or carry over incomplete |

---

## Step 1: Determine Date and Data Sources

- **If user wants to "summarize yesterday"**: Calculate yesterday's date (recommended: use this Skill's `scripts/date_utils.py`); read `{yesterday's date}-todo.md`, `{yesterday's date}-log.md` (if exists); identify completed / incomplete / time allocation / learning output by summary categories from the data.
- **If user "reports today" (conversational)**: Calculate today's date; parse completed items, incomplete items, time/sequence, thoughts/feelings/casual remarks from user input.
- **Read summary categories config**: Read `{agendaRoot}/summary-categories.md` (if absent, use this Skill's `assets/summary-categories.example.md`), obtain category list for Step 2's "Learning/Output" section.

## Step 2: Generate Log File

Use `templates/log-template.md` template, fill variables and write:

**Path**: `{agendaRoot}/daily/{target date}-log.md`

**Template variables**: `{{DATE}}`, `{{COMPLETED_TASKS}}`, `{{TIME_ALLOCATION}}`, `{{ACTUAL_WORK_TIME}}` (total actual work/study time, e.g., "approx. 6h50 (German ~50min + jw-agenda skills ~6h)"), `{{SUMMARY_CATEGORIES}}` (generated per summary categories config, see below), `{{INCOMPLETE_TASKS}}`, `{{SUMMARY}}`, `{{NOTES_AND_THOUGHTS}}` (thoughts/quick notes; write "None" if empty), `{{TIMESTAMP}}`.

**Summary categories**: Before generating the log, read `{agendaRoot}/summary-categories.md` (if absent, use this Skill's `assets/summary-categories.example.md`), parse the category list under `## Categories`. In the "Learning/Output" section, summarize the day's activities and output for each category in order. Format: `- **Category Name**: content summary`. If a category has no content for the day, omit or write "None" (see empty category handling rules in conventions).

If the `daily/` directory under the jw-agenda root does not exist, create it.

## Step 3: Bottom-up Cascade Status Sync

Check and update layer by layer in the following order:

### 3a: Daily Plan (daily/YYYY-MM-DD-todo.md)

- **If this is "report today"**: In `{today's date}-todo.md`, check `[x]` for completed items, mark `(in progress)` for in-progress items; if today's todo does not exist, only write the log.
- **If this is "summarize yesterday"**: In `{yesterday's date}-todo.md`, check completed items; if there are incomplete items, append them to `{today's date}-todo.md` marked `*(carried over from yesterday)*`, skipping existing entries.

### 3b–3d: Weekly Plan → Monthly Plan → Yearly Plan

Follow the "Bottom-up Cascade Sync Standard Steps" in conventions-cascade.md. Check scope: weekly plan → monthly plan → yearly plan (if exists). Modifications to upper-level files are limited to status marks; detailed content stays in the log file.

## Step 4: Report

Inform user of: log file path written, completion overview, carry-over count, **all file paths where status was synced**.

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Yesterday's todo does not exist | Infer activities from available files only; if no content at all, generate empty template log |
| Yesterday's log already exists | Ask user whether to overwrite or append; default is no overwrite |
