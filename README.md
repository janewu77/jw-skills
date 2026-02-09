# jw-skills

[![License: Apache 2.0](https://img.shields.io/badge/License-Code%20Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-Docs%20CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](CHANGELOG.md)

A collection of skills for use in Cursor, Claude, and similar environments. Maintained by Jing Wu.

**Language**: This document is the authoritative version in English. For a Chinese overview, see [README.zh-CN.md](README.zh-CN.md).

---

## ⭐ Featured: jw-agenda

**📋 Plan, execute, and review your personal agenda with natural language.** jw-agenda is a complete skill set that automates your workflow from monthly planning through daily execution to weekly review—all through simple conversations with your AI assistant. Your data stays local in Markdown files, giving you full control and privacy.

**🔄 The complete loop**: 📅 Monthly plan → 📊 Weekly breakdown → ✅ Daily execution → 📝 Log → 📈 Weekly review

Simply say things like:
- 💬 "Generate this week's plan" → Creates a day-by-day breakdown from your monthly goals
- 💬 "Generate today's plan" → Builds your daily todo with schedule from weekly plan and yesterday's incomplete tasks
- 💬 "I finished the resume update" → Logs your progress and updates checkboxes automatically
- 💬 "Move applications to Wednesday" → Reschedules tasks and syncs your plans
- 💬 "Weekly summary" → Aggregates logs, calculates completion rates, and identifies carry-over items

All 5 skills work together seamlessly 🤝, but you can install only what you need—each skill is independent and gracefully handles missing dependencies.

---

## 📚 Contents

| Skill set | Description |
|-----------|-------------|
| [jw-agenda](jw-agenda/) | 📅 Personal agenda: monthly plan → weekly breakdown → daily execution → log → weekly review. See [jw-agenda/README.md](jw-agenda/README.md). |

### 🚀 jw-agenda: Complete Personal Productivity System

**5 complementary skills** 🤝 that work together to automate your planning and execution workflow:

- ✅ **jw-agenda-daily-todo**: Generate today's plan, reschedule tasks, add ad-hoc items. Manages your daily todo with automatic schedule integration.
- 📝 **jw-agenda-daily-log**: Turn casual progress reports into structured logs. Summarize yesterday or record today's work with thoughts and feelings preserved.
- 📊 **jw-agenda-weekly-plan**: Break down monthly goals into day-by-day weekly plans. Merges carry-over tasks from last week automatically.
- 📈 **jw-agenda-weekly-review**: Aggregate weekly logs, calculate completion rates, track time allocation, and identify items to carry forward.
- 🔄 **jw-agenda-planning-sync**: Check consistency across daily/weekly/monthly plans, detect discrepancies, and sync after your confirmation.

**✨ Key benefits**:
- 💬 **Natural language**: Just talk to your AI assistant—no complex commands or syntax
- 🔒 **Local storage**: All data stored as Markdown files in your workspace—privacy-focused and portable
- 🧩 **Modular design**: Install only the skills you need; each works independently
- 🔗 **Seamless integration**: Skills automatically read from each other's outputs when available
- 🎯 **Flexible workflow**: Supports both structured planning and casual progress reporting

**🎯 Perfect for**: Personal productivity, project planning, habit tracking, goal management, and anyone who wants to automate their planning workflow with AI assistance.

See the [detailed documentation](jw-agenda/README.md) for installation, examples, and complete feature list. **Pre-built zips** for all 5 skills are available in [Releases](https://github.com/janewu77/jw-skills/releases).

---

## 🚀 Quick Start

### For jw-agenda

1. 📁 **Create data directory**:
   ```bash
   mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}
   ```

2. 📦 **Install skills**: Download the 5 skill zips from [Releases](https://github.com/janewu77/jw-skills/releases), unzip each into your Cursor skills directory (e.g., `~/.cursor/skills/`). Or copy the folders from `jw-agenda/skills/` if you have the repo locally.

3. 📅 **Create your first monthly plan**: Add `YYYY-MM-plan.md` in `jw-agenda-data/monthly/` (e.g., `2026-02-plan.md`).

4. 🎉 **Start using**: Open your workspace in Cursor and say "Generate this week's plan" or "Generate today's plan".

For detailed installation instructions, examples, and customization options, see [jw-agenda/README.md](jw-agenda/README.md).

---

## 🛠️ Development

See [TODO.md](TODO.md) for planned improvements and known issues.

## 🔒 Security

See [SECURITY.md](SECURITY.md) for information about reporting security vulnerabilities.

## License

This repository as a whole is licensed under **Apache 2.0 for code** and **CC-BY-4.0 for documentation**. Applies to all contents (including subdirectories such as jw-agenda). See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), [LICENSE-DOCS](LICENSE-DOCS).
