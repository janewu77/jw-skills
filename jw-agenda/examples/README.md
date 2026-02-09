# Examples

**Language**: This document is the authoritative version in English. For other languages, see:
- [README.zh-CN.md](README.zh-CN.md) (中文)

This directory contains example workspaces and conversation examples demonstrating how to use jw-agenda.

## Sample Workspace

### English Version (`sample-workspace/`)

A complete English-language example workspace showing:
- Monthly plan (`monthly/2026-02-plan.md`)
- Weekly plan (`weekly/Week6-plan.md`)
- Daily todo (`daily/2026-02-05-todo.md`)
- Daily log (`daily/2026-02-05-log.md`)
- Weekly review (`weekly/Week6-review.md`)
- General tasks (`tasks/TODO.md`)

## How to Use

1. **Copy the workspace**: Copy `sample-workspace/` to your workspace root
2. **Rename**: Rename it to `jw-agenda-data` (default) or configure via `.jw-agenda.json`
3. **Customize**: Edit the files with your own plans and tasks
4. **Start using**: Install the jw-agenda skills and start using natural language commands

## File Descriptions

- **Monthly Plan** (`monthly/YYYY-MM-plan.md`): High-level goals and weekly focus areas
- **Weekly Plan** (`weekly/Week{N}-plan.md`): Day-by-day breakdown of tasks for the week
- **Daily Todo** (`daily/YYYY-MM-DD-todo.md`): Today's tasks with schedule and priorities
- **Daily Log** (`daily/YYYY-MM-DD-log.md`): Record of what was accomplished, time allocation, and reflections
- **Weekly Review** (`weekly/Week{N}-review.md`): Summary of the week with completion stats and carry-over items
- **General TODO** (`tasks/TODO.md`): Tasks without specific dates

## Conversation Examples

See [conversations.md](conversations.md) for complete examples showing how to interact with jw-agenda skills using natural language.

For examples in other languages:
- [conversations.zh-CN.md](conversations.zh-CN.md) (中文)

## Example Workflow

1. **Start of month**: Create monthly plan with goals
2. **Start of week**: Generate weekly plan from monthly goals
3. **Each morning**: Generate today's todo from weekly plan
4. **During day**: Use skills to add tasks, reschedule, or report progress
5. **End of day**: Generate log from casual report
6. **End of week**: Generate weekly review and plan next week

See the main [README.md](../README.md) for detailed usage instructions.
