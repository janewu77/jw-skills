# Conventions (Shared Across All Skill Modes)

## Path Discovery

This file is located at **`assets/conventions.md` within this Skill**. All Skill modes should read this file (relative to the Skill's installation directory) before execution to obtain the conventions below. The user workspace only stores **data** and **optional user configurations** (schedule config, summary categories config) — see "jw-agenda Root Directory", "Directory Paths", and "File Naming Rules".

## jw-agenda Root Directory (Configurable)

All agenda data resides under the "jw-agenda root directory" (i.e., the user data root). **jw-agenda** is the skill group name; by default, user data is stored under **`jw-agenda-data`** in the user's workspace. The root directory is **preferentially** read from the `agendaRoot` field in `.jw-agenda.json` (or `jw-agenda.json`) at the workspace root; if the file does not exist or `agendaRoot` is not set, the default `jw-agenda-data` is used.

**Convention**: Before any read/write operation, the Agent first determines the workspace root, then reads the config to obtain the jw-agenda root directory (default `jw-agenda-data`). All subsequent paths are relative to this root. Paths should use forward slashes and be relative to the workspace root; normalize as needed (e.g., strip trailing `/`, avoid `..`).

## Directory Paths (User Workspace)

`{agendaRoot}` is derived from the configuration or default above. Agenda plans and completion records are stored under `{agendaRoot}` in the workspace, organized by time granularity:

| Purpose | Path |
|---------|------|
| Yearly plan (optional) | `{agendaRoot}/yearly/` |
| Monthly plan, monthly review | `{agendaRoot}/monthly/` |
| Weekly plan, weekly review | `{agendaRoot}/weekly/` |
| Daily todo, daily log | `{agendaRoot}/daily/` |
| Other tasks and lists (reading list, shopping list, etc.) | `{agendaRoot}/tasks/` |
| User schedule config (optional) | `{agendaRoot}/schedule-config.md` |
| Summary categories config (optional) | `{agendaRoot}/summary-categories.md` |

**Daily directory archival rule**: Current and recent todo/log files stay in the `daily/` root. Files older than the archival threshold are moved into year-month subdirectories (e.g., `202601/`, `202602/`, format `YYYYMM`).

**Archival threshold configuration**: Default is 14 days (2 weeks). Customizable via the `archiveAfterDays` field in `.jw-agenda.json`:

```json
{
  "agendaRoot": "jw-agenda-data",
  "archiveAfterDays": 14
}
```

Set to `0` or negative to disable automatic archival.

## File Naming Rules

| File Type | Naming Format | Example |
|-----------|---------------|---------|
| Yearly plan (optional) | `YYYY-plan.md` | `2026-plan.md` |
| Monthly plan | `YYYY-MM-plan.md` (e.g., `2026-02-plan.md` for February) | `2026-02-plan.md` |
| Weekly plan | `Week{N}-plan.md` (N = ISO week number, 1–52) | `Week6-plan.md` |
| Daily todo | `YYYY-MM-DD-todo.md` | `2026-02-05-todo.md` |
| Daily log | `YYYY-MM-DD-log.md` | `2026-02-05-log.md` |
| Weekly review | `Week{N}-review.md` (N = ISO week number, matching weekly plan) | `Week6-review.md` |
| Monthly review | `YYYY-MM-review.md` | `2026-02-review.md` |
| Reading list | `todo-readinglist.md` | `{agendaRoot}/tasks/todo-readinglist.md` |
| Unscheduled / backlog | `TODO.md` | `{agendaRoot}/tasks/TODO.md` |
| Schedule config (optional) | `schedule-config.md` | `{agendaRoot}/schedule-config.md` (if absent, daily-todo uses this Skill's `assets/schedule-config.example.md`) |
| Summary categories config (optional) | `summary-categories.md` | `{agendaRoot}/summary-categories.md` (if absent, uses this Skill's `assets/summary-categories.example.md`) |

All example paths above are relative to the jw-agenda root directory; the default `agendaRoot` is `jw-agenda-data`, but the actual value depends on the resolved configuration.

**Files starting with `todo` in the tasks directory** (e.g., `TODO.md`, `todo-readinglist.md`, `todo-xxx.md`) are all treated as backlog/lists. When generating weekly plans or daily plans, unchecked items from these files should be considered as optional sources.

**"Today's thoughts / quick notes" in logs**: When users report progress conversationally, thoughts, feelings, and casual remarks are recorded in this section, preserving the original meaning for future review.

## Summary Categories Configuration

The "Learning/Output" section in daily-log and weekly-review summarizes content along **configurable category dimensions**.

**Config source**: Preferentially reads `{agendaRoot}/summary-categories.md`; if absent, uses this Skill's `assets/summary-categories.example.md`.

**Config format**: Each line starting with `- ` under `## Categories` is a category. When generating logs or weekly reviews, the Agent parses the category list from this file and generates a sub-paragraph for each category under the "Learning/Output" section (`- **Category Name**: content`).

**Empty category handling**: If a category has no relevant content for the day/week, the category line shows "None" or is omitted entirely — the Agent decides based on data richness: if most categories have content, keep "None" for structural consistency; if only a few categories have content, omit empty ones to reduce noise.

## Week Number Calculation Rules

**Week boundaries**: Monday through Sunday.

**Week number**: The ISO week number within the year, typically 1–52, occasionally 53. Use Python `date.isocalendar()` to get `iso_week` (1–52 or 53).

**Example**: 2026-02-05 (Thursday) falls in Week 6 of 2026 → weekly plan `Week6-plan.md`, weekly review `Week6-review.md`.

**Cross-year week note**: ISO weeks are determined by the year containing Thursday. For example, 2025-12-29 (Monday) through 2026-01-04 (Sunday) — Thursday is 2026-01-01, so this is **2026 Week 1**. Similarly, if December 31 of a year falls on Monday–Wednesday, that day belongs to the next year's Week 1; if it falls on Thursday–Sunday, it belongs to the current year's last week.

**Recommended**: Use **this Skill's** `scripts/date_utils.py` to calculate dates and week numbers, avoiding manual calculation errors. `scripts/dedup_todos.py` is available for deduplication when merging todos (e.g., daily-todo mode A idempotent merge); optional, the Skill may also deduplicate in its own logic. **When calling dedup_todos.py, only pass paths under the jw-agenda root directory** (i.e., paths resolved per user configuration); the script validates that paths are within the workspace to prevent path traversal.

## Deduplication

When merging tasks from multiple sources (e.g., daily-todo idempotent merge, planning-sync comparison), use the following standard deduplication flow:

1. **Strip marks**: Remove checkbox prefix (`- [ ]` / `- [x]`), source marks (`*(结转)*`, `*(from plan)*`, `*(carried over from yesterday)*`, etc.), and parenthesized annotations (both `（…）` and `(…)`)
2. **Trim**: Strip leading/trailing whitespace and trailing punctuation (`。，、；`)
3. **Case-insensitive compare**: Lowercase the normalized text
4. **Exact match**: Two entries are duplicates if and only if their normalized text is **identical**

Substring matching is intentionally **not** used — it produces false positives (e.g., "Review PR" matching "Review PR feedback"). If an entry looks similar but is not an exact normalized match, treat it as a distinct task.

This algorithm is implemented in `scripts/dedup_todos.py` and should be used (or replicated) by any mode that needs deduplication.

## Ad-hoc Task Attribution

See the write-rule table in `references/mode-add-or-move.md` Step 1. After completing the operation, **always report to the user which files were written**.

## Mark Conventions (Source / Status / Priority)

See `assets/conventions-marks.md` (loaded before starting daily-todo and add-or-move modes).

## Cascade Updates and Conflict Resolution

See `assets/conventions-cascade.md` (loaded before starting daily-log, weekly-review, monthly-review, weekly-plan, add-or-move, and planning-sync modes).

## Deferrable vs Non-Deferrable Tasks

When merging yesterday's incomplete (or prior-period leftovers) into a new plan, distinguish two categories:

### Non-deferrable (time-bound)

**Cannot be carried over or "made up" later.** If missed, it is simply missed; only execute **today's instance** per the current plan. Do not add entries like "补 7/3 遗留" or "补昨天的 v2".

Examples:
- Daily discipline: v2 最小闭环, daily 录音/出声, daily 卡点
- 投递 batches scheduled on a specific 投递日
- Fixed events: weekly swimming, Build Friday, interviews
- **Analogy**: yesterday's lunch cannot be eaten next Wednesday

**Rule**: When reading yesterday's incomplete, **drop** non-deferrable items — do not append them to today's todo. The current week plan already defines what to do today (e.g., today's v2); that replaces any missed instance.

### Deferrable (flexible)

**Can be rescheduled** within the current week or month. This is what **结转** is for.

Examples:
- Elastic tasks: blog drafts, GSC sitemap, visa research, learning materials, backlog reading
- Must still appear in the **current week's plan** (or be explicitly assigned to a slot this week)
- Mark with `*(结转)*` when carrying forward — no "遗留 / 补做" framing

**Rule**: Only carry deferrable items that remain relevant in the current week plan. Assign them to an appropriate day in **this week**, not as catch-up for a missed daily discipline.

See also: source mark and writing-style rules in `assets/conventions-marks.md`.

## General Execution Rules

- **Reporting obligation**: After every operation, the user must be informed of all modified file paths.
- **Cascade direction**: Each mode's cascade direction and paths are defined in `assets/conventions-cascade.md`'s direction table; mode files do not repeat these.

## Default Error Handling Strategy

| Situation | Handling |
|-----------|----------|
| File does not exist | Skip that source, continue with available data, inform user which file is missing |
| Format does not match expectations | Best-effort parsing; if unparseable, show file content to user and request confirmation |
| All sources are missing | Generate a minimal scaffold (title and empty sections only), annotated "No data source, please fill in manually" |
| File already exists (idempotency) | Read existing content first, only append non-duplicate new entries, preserve user's existing checkmarks and notes |
| Date ambiguity (e.g., "next week") | Calculate the specific date and confirm with user |
