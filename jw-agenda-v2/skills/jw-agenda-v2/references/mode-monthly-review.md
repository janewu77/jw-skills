# Mode 5: Monthly Review (monthly-review)

Aggregate this month's weekly reviews and logs, calculate completion rates and time allocation, generate a monthly review report, and identify items to carry over to next month.

> **Additional loading**: `assets/conventions-cascade.md`.

## Step 1: Determine Review Scope

Use this Skill's `scripts/date_utils.py` to calculate date ranges.

- **Default**: Current month (1st through month-end)
- If user says "last month review", use last month's date range (`--prev-month`)
- If user specifies a **quarter** (e.g., `Q1`, `Q2`, third quarter), map to the corresponding month range: Q1=Jan–Mar, Q2=Apr–Jun, Q3=Jul–Sep, Q4=Oct–Dec → enter the "Quarter/Multi-month Summary" flow (see below)
- If user specifies a **custom range** (e.g., `2026-01 to 2026-03`, `January to March`), parse start and end months → also enter the "Quarter/Multi-month Summary" flow

### Quarter/Multi-month Summary Flow

When the review scope spans multiple months, execute the following steps instead of Steps 2–6:

1. **Check monthly reviews for each month**: For each month in the range, check if `{agendaRoot}/monthly/YYYY-MM-review.md` exists
   - If exists: Read the monthly review, extract completion rate, time allocation, output summary
   - If absent: Ask user whether to generate the monthly review first; if user chooses to skip, aggregate that month's data from raw weekly reviews/logs
2. **Cross-month statistics**: Merge data from all months, calculate completion rate trends (month-over-month comparison), total time allocation, cumulative output
3. **Generate summary report**:
   - **Path**: `{agendaRoot}/monthly/YYYY-Q{N}-review.md` (quarterly) or `YYYY-MM-to-MM-review.md` (custom range)
   - **Content**: Month-over-month completion rate comparison, total time allocation, cumulative output, cross-month carry-over item tracking
4. **No cascade sync**: The summary report is a read-only overview; do not modify monthly or yearly plan status (individual monthly reviews have already synced separately)
5. Report: Report path, per-month completion rates, total time, key outputs

## Step 2: Aggregate Data

Read files within this month's range, by priority:

**Primary sources**:
- `{agendaRoot}/weekly/Week{W}-review.md`: All weekly reviews for this month, extract completion data, time allocation, carry-over items
- `{agendaRoot}/monthly/YYYY-MM-plan.md`: Compare planned vs. actual

**Supplementary sources** (if weekly reviews are missing):
- `{agendaRoot}/daily/{date}-log.md`: Read day by day, extract completed, incomplete, time allocation
- `{agendaRoot}/daily/{date}-todo.md`: Read day by day for checkmark status, cross-validate

**Summary categories config**: Read `{agendaRoot}/summary-categories.md` (if absent, use `assets/summary-categories.example.md`), aggregate output by category dimension.

Record which weeks have data and which are missing.

## Step 3: Statistical Analysis

**Completion rate**: Aggregate weekly completion rates, calculate the monthly overall rate. Break down by high/medium/low priority.

**Time allocation**: Extract from each weekly review's "Time Allocation" section, aggregate by category for total monthly hours.

**Output summary**: From each weekly review's "Learning/Output" section, aggregate by the category dimensions in the summary categories config.

**Goal achievement**: Compare against goals in the monthly plan, checking each item's completion status.

## Step 4: Generate Monthly Review

Use `templates/monthly-review-template.md` template, fill and write:

**Path**: `{agendaRoot}/monthly/YYYY-MM-review.md`

**Content**:
- Overall overview (completion rate, key achievements)
- Goal achievement status
- Time allocation analysis
- Learning and output summary
- Incomplete/pending items
- **Carry over to next month** list

## Step 5: Bottom-up Cascade Status Sync

Follow the "Bottom-up Cascade Sync Standard Steps" in conventions-cascade.md. Check scope: monthly plan → yearly plan (if exists). Using aggregated actual completion data, mark each goal's status in the monthly plan (completed `[x]`, incomplete stays `[ ]`, in progress marked `(in progress)`).

## Step 6: Report

State: monthly review file path, overall completion rate, time allocation highlights, carry-over item count, **all file paths where status was synced**.

## Error Handling

Default strategy: see `assets/conventions.md` "Default Error Handling Strategy". Mode-specific cases below:

| Situation | Handling |
|-----------|----------|
| Some weeks missing weekly reviews | Attempt to aggregate from logs, note missing weeks in the report |
| All weeks have no weekly reviews | Ask user whether to generate from logs, or generate an empty scaffold |
| Monthly plan does not exist | Skip goal achievement analysis, only report execution data |
| Monthly review already exists | Ask user whether to overwrite; default is no overwrite |
