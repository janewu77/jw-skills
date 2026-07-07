# Mark Conventions (Source / Status / Priority)

> Loaded on demand: daily-todo and add-or-move modes read this file before starting.

## Source Marks (Daily Todo Output)

**Default: no mark.** Tasks from monthly/weekly plan, tasks lists, or reading lists do **not** need source marks in the daily todo file — plan context is implicit. Keep entries scannable.

**Only mark exceptions:**

| Situation | Mark |
|-----------|------|
| Deferrable task carried forward from a prior day/week | `*(结转)*` |
| Explicitly moved in from another date | `*(moved from M.D)*` |
| Ad-hoc addition in the current conversation | optional; omit unless clarity needed |

**Do not write in daily todo output:**
- `*(from plan)*` — default origin; redundant
- `*(from tasks list)*` / `*(from reading list)*` — default origin; redundant
- `*(carried over from yesterday)*` — use `*(结转)*` instead (shorter)

### Internal dedup (not shown in output)

When merging sources internally, track origin for dedup and priority resolution:

| Source | Internal use |
|--------|-------------|
| Yesterday's incomplete (deferrable only) | Output as `*(结转)*` |
| Monthly/weekly plan | No output mark |
| Moved from another date | `*(moved from M.D)*` |
| Tasks / reading lists | No output mark |
| Ad-hoc addition | No mark unless needed |

**Principle**: Mark only **exceptions** — facts that change how the reader should interpret the item (结转, 移入). Do not stack multiple marks.

## Daily Todo Writing Style

- **No catch-up framing**: Never write "遗留", "补做", "补 X/X 的 …". Non-deferrable missed tasks are dropped; deferrable tasks are assigned to this week with `*(结转)*` only.
- **Low priority — no hedging**: Do not add "有空档再看", "弹性", "有时间再做" etc. The 🟢 heading already signals optional.
- **Schedule — keep lean**: Time slots match the current week plan for that day; do not invent extra slots to "补" prior days.
- **Footer**: Omit source legend and verbose generation notes unless the user asks for them.

## Status Marks

Different planning levels use different status mark formats:

### Daily Todo / Day-by-Day Sections in Weekly Plan — Checkbox Format

| Status | Format |
|--------|--------|
| Completed | `- [x] task content` |
| In progress | `- [ ] task content (in progress)` |
| Cancelled | `- [x] task content (cancelled)` |
| Postponed (no target date) | `- [ ] task content (postponed)` or noted in remarks |
| Postponed (with target date) | Move to target date, marked `*(moved from M.D)*` |

### Weekly Task Overview Table — Emoji Format

The overview table at the top of the weekly plan uses emoji status icons for visual scanning:

| Status | Emoji |
|--------|-------|
| Completed | ✅ Completed |
| In progress | 🔄 In progress |
| Not started | ⬜ Not started |
| Cancelled | ❌ Cancelled |

**Rule of thumb**: Checkbox (`- [x]`/`- [ ]`) is the standard format for all actionable task lists (daily todo, weekly day-by-day sections). Emoji status is only used in the weekly overview summary table, which is a read-oriented dashboard — not directly checked off.

## Priority Labels

| Level | Heading Format |
|-------|---------------|
| High (must finish today) | `## 🔴 High Priority` |
| Medium | `## 🟡 Medium Priority` |
| Low (optional) | `## 🟢 Low Priority` |
