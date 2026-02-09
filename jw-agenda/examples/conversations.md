# Conversation Examples

This document shows complete examples of how to interact with jw-agenda skills using natural language.

## Example 1: Generate Weekly Plan

**User**: "Generate this week's plan"

**Assistant** (using `jw-agenda-weekly-plan`):
- Reads `monthly/2026-02-plan.md` to get this week's goals
- Checks `weekly/Week5-review.md` for carry-over items from last week
- Creates `weekly/Week6-plan.md` with day-by-day breakdown
- Assigns tasks to specific days based on priorities

**Output**: Creates `weekly/Week6-plan.md` with:
- Overview section with focus and goals
- Task list table with priorities and status
- Day-by-day breakdown (Monday through Sunday)
- Source markers showing where tasks came from

**User**: "Move the application tracking system setup to Friday"

**Assistant** (using `jw-agenda-daily-todo`):
- Reads `weekly/Week6-plan.md`
- Removes the task from its current day
- Adds it to Friday's section
- Updates the weekly plan file
- Confirms the change

**Output**: "Moved 'Set up job application tracking system' to Friday (2026-02-06). Updated Week6-plan.md."

---

## Example 2: Daily Progress Report

**User**: "Today I finished researching 3 companies and submitted my first 3 applications. Still need to practice English. Feeling good about the progress!"

**Assistant** (using `jw-agenda-daily-log`):
- Reads `daily/2026-02-05-todo.md` to see planned tasks
- Generates `daily/2026-02-05-log.md` with:
  - Completed tasks section (marked as done)
  - Time allocation based on reported activities
  - Learning/output section
  - Incomplete tasks (English practice)
  - Summary and reflection
  - Notes section with the feeling/thoughts
- Updates `daily/2026-02-05-todo.md` checkboxes:
  - ✅ Research remaining 3 target companies
  - ✅ Submit first 3 job applications
  - ⬜ Practice English speaking 30 min (moved to incomplete)

**Output**: 
- Created `daily/2026-02-05-log.md` with structured log
- Updated `daily/2026-02-05-todo.md` checkboxes
- Message: "Logged your progress! Created today's log and updated your todo. English practice is still pending - would you like to do it now or move it to tomorrow?"

---

## Example 3: Generate Today's Todo

**User**: "Generate today's plan"

**Assistant** (using `jw-agenda-daily-todo`):
- Reads `weekly/Week6-plan.md` to find today's tasks
- Checks `daily/2026-02-04-log.md` for incomplete items from yesterday
- Reads `monthly/2026-02-plan.md` for context
- Generates `daily/2026-02-05-todo.md` with:
  - Schedule table with time slots
  - High priority tasks (from weekly plan)
  - Medium priority tasks
  - Low priority tasks
  - Source markers showing origin

**Output**: Creates `daily/2026-02-05-todo.md`:
```
# Todo - 2026-02-05

## 🔴 High Priority
- [ ] Research remaining 3 target companies *(from plan)*
- [ ] Submit first 3 job applications *(from plan)*

## 🟡 Medium Priority
- [ ] Practice English speaking 30 min *(from plan)*
```

---

## Example 4: Add Ad-hoc Task

**User**: "Add: review application materials one more time"

**Assistant** (using `jw-agenda-daily-todo`):
- Determines this is for today (no date specified)
- Adds to `daily/2026-02-05-todo.md` under low priority
- Marks as *(ad-hoc)*
- Confirms the addition

**Output**: "Added 'review application materials one more time' to today's todo (low priority)."

---

## Example 5: Weekly Review

**User**: "Weekly summary"

**Assistant** (using `jw-agenda-weekly-review`):
- Reads all daily logs from the week (`daily/2026-02-02-log.md` through `daily/2026-02-08-log.md`)
- Reads `weekly/Week6-plan.md` to compare planned vs actual
- Generates `weekly/Week6-review.md` with:
  - Overall completion rate
  - Completed tasks list
  - Incomplete tasks list
  - Time allocation summary
  - Learning and outputs
  - Items to carry over to next week

**Output**: Creates `weekly/Week6-review.md`:
```
# Week 6 Review (2026-02-02 ~ 2026-02-08)

## Overall Overview
- **Completion Rate**: 80% (4 completed / 5 total tasks)
- **Data Coverage**: 5/7 days with log records
- **Week Highlights**: Successfully submitted first batch of applications

## Carry Over to Next Week
- Set up job application tracking system (carried over)
```

---

## Example 6: Plan Consistency Check

**User**: "Sync plans"

**Assistant** (using `jw-agenda-planning-sync`):
- Reads `daily/2026-02-05-todo.md`
- Reads `weekly/Week6-plan.md`
- Reads `monthly/2026-02-plan.md`
- Compares tasks across all three levels
- Identifies discrepancies:
  - Task in daily todo but not in weekly plan
  - Task marked complete in daily but still active in weekly
  - Priority mismatch
- Shows discrepancies and asks for confirmation before fixing

**Output**: 
```
Found 2 discrepancies:

1. "Review application materials" is in daily todo but not in weekly plan
   → Add to weekly plan? (y/n)

2. "Research companies" marked complete in daily log but still active in weekly
   → Update weekly plan status? (y/n)
```

---

## Tips for Natural Language Usage

- **Be specific**: "Generate this week's plan" works better than "plan"
- **Be casual**: "Today I did X, still have Y" is perfectly fine
- **Use context**: The assistant understands "today", "tomorrow", "this week", "next week"
- **Combine actions**: "Move X to Wednesday and add Y for tomorrow" works
- **Ask questions**: "What's on my todo today?" or "How's this week going?"

The skills are designed to understand natural, conversational language while maintaining data consistency.
