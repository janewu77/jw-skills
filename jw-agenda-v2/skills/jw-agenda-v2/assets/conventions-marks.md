# Mark Conventions (Source / Status / Priority)

> Loaded on demand: daily-todo and add-or-move modes read this file before starting.

## Source Marks

| Source | Mark Format |
|--------|-------------|
| Yesterday's incomplete | `*(carried over from yesterday)*` |
| Monthly/weekly plan | `*(from plan)*` |
| Yesterday's incomplete + also in plan | `*(carried over from yesterday)*` |
| Moved in from another date | `*(moved from M.D)*` |
| From reading list | `*(from reading list)*` |
| From tasks lists (including above and other todo-prefixed files) | `*(from tasks list)*` |
| Ad-hoc addition (added via daily-todo add/move task mode) | `*(ad-hoc addition)*` |

**Source mark priority**: When a task meets multiple source conditions, select the first matching mark in the following order (no stacking):
1. `*(carried over from yesterday)*` — yesterday's incomplete has highest priority, even if the task is also in a plan
2. `*(moved from M.D)*` — explicitly moved in from another date
3. `*(from plan)*` — purely from weekly/monthly plan
4. `*(from reading list)*` / `*(from tasks list)*` — from a list
5. `*(ad-hoc addition)*` — newly added in the current conversation

**Principle**: Prioritize marking "facts that have occurred" (yesterday's leftovers), then "explicit actions" (moved in), and finally "origin" (plan/list).

## Status Marks (Used When Updating Status in daily-todo)

| Status | Format in Todo Entry |
|--------|----------------------|
| Completed | `- [x] task content` |
| In progress | `- [ ] task content (in progress)` |
| Cancelled | `- [x] task content (cancelled)` |
| Postponed (no target date) | `- [ ] task content (postponed)` or noted in remarks |
| Postponed (with target date) | Move to target date, marked `*(moved from M.D)*` |

## Priority Labels

| Level | Heading Format |
|-------|---------------|
| High (must finish today) | `## 🔴 High Priority` |
| Medium | `## 🟡 Medium Priority` |
| Low (optional) | `## 🟢 Low Priority` |
