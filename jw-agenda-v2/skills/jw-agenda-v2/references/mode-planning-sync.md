# Mode 6: Planning Sync (planning-sync)

Check consistency among tasks/TODO master backlog, yearly plan, monthly plan, weekly plan, and daily plan. After discovering discrepancies, generate sync suggestions and **only execute batch updates after user confirmation**.

> **Additional loading**: `assets/conventions-cascade.md`.
> **Recommended timing**: Mid-week (e.g., Wednesday) to check for deviations; once before generating the weekly review at the end of each week; after making large schedule adjustments.

This mode serves as a **post-hoc global consistency check**, catching discrepancies that other modes' cascade updates may have missed.

## Core Principles

1. **Read-only analysis**: Steps 1–4 only read and compare — no files are modified
2. **User confirmation**: Step 5 must obtain explicit user consent before executing updates
3. **Minimal changes**: Only modify parts that have discrepancies — no unnecessary changes
4. **Preview first**: Default to dry-run mode showing a change preview; execute only after user confirms

## Step 1: Determine Check Scope

Use this Skill's `scripts/date_utils.py` to calculate dates and week numbers, then read layer by layer from top to bottom:

- **Tasks master backlog**: `{agendaRoot}/tasks/TODO.md` and other `todo-*.md` files
- **Yearly plan** (if exists): `{agendaRoot}/yearly/YYYY-plan.md` or similar path
- **Monthly**: `{agendaRoot}/monthly/YYYY-MM-plan.md` (current month)
- **Weekly**: `{agendaRoot}/weekly/Week{W}-plan.md`
- **Daily**: `{agendaRoot}/daily/{today's date}-todo.md` (optional: todos and logs from the last 3–7 days)

Missing levels are skipped, with an explanation to the user (see error handling).

## Step 2: Comparative Analysis

Check consistency across all available levels along three dimensions:

**Dimension 1 — Task Content Alignment (top-down)**:
- Are tasks marked "planned" in tasks/TODO actually present in monthly/weekly/daily plans?
- Are tasks for this week/today from the monthly plan present in the weekly plan and daily todo?
- Are tasks for today from the weekly plan present in the daily todo?
- Reverse: Do tasks in daily todo / weekly plan have a source in upper-level plans, or have they been backfilled?

**Dimension 2 — Completion Status Sync (bottom-up)**:
- Are tasks completed (`[x]`) in daily todo / logs also marked complete in the weekly plan?
- Are tasks completed in the weekly plan also marked in the monthly plan?
- Are completed goals in the monthly plan reflected in the yearly plan (if exists)?
- Use **daily execution as authoritative** and sync upward (see conflict resolution strategy in conventions)

**Dimension 3 — Addition/Change Tracking**: Do newly added tasks in daily execution need to be backfilled into weekly/monthly plans? Are cancelled/postponed tasks synced across all levels?

**Content alignment comparison strategy** (for Dimensions 1 and 2):
- **Task content alignment**: Uses **normalized keyword matching**. Extract the entry body (strip `- [ ]` / `- [x]`, source marks like `*(from plan)*`, etc.), then normalize whitespace and line breaks. If two entries' core descriptions match (post-stripping text is identical, or one contains the other's key substring), they are considered the "same task". Exact character-by-character match is not required, to tolerate user wording tweaks.
- **Completion status sync**: Given the "same task", compare checkmark status (`[x]` vs `[ ]`) between daily todo and weekly/monthly plans. If daily is checked but weekly is not, or vice versa, it's recorded as a discrepancy; the recommendation is to sync using **daily execution as authoritative** (see conflict resolution strategy in conventions).

## Step 3: Discrepancy Classification

| Level | Meaning | Examples |
|-------|---------|----------|
| ⚠️ Action needed | Affects plan execution, recommend immediate sync | Daily completed but weekly not checked; weekly has today's task but daily todo doesn't include it |
| ℹ️ Informational | Does not affect execution, for reference | Daily todo has extra ad-hoc tasks not in plans; items in daily/weekly sourced from tasks directory todo-prefixed lists (a legitimate source) |

Each discrepancy includes: affected file paths, specific location, recommended action.

## Step 4: Generate Sync Suggestions

Output a structured suggestion list (using the `templates/sync-report-template.md` format).

## Step 5: User Confirmation and Execution

1. Present the suggestion list to the user
2. Ask "Execute the above suggestions?" with options:
   - **Execute all** — execute all suggestions
   - **Only ⚠️ Action needed** — shortcut to execute only "⚠️ Action needed" level suggestions, skip "ℹ️ Informational"
   - **Specify by number** — user inputs specific numbers (e.g., 1,3,5)
   - **Skip** — do not execute any modifications
3. **Only execute file modifications for items the user agreed to**
4. Report: which files were updated, what was changed

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Only one level exists | Cannot do cross-level comparison; inform user and suggest generating the missing plans first |
| No discrepancies | Report "All planning levels are consistent, no sync needed" |
| User doesn't confirm any suggestions | Report "No modifications made", do not execute any write operations |
