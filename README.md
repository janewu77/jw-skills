# jw-skills

[![License: Apache 2.0](https://img.shields.io/badge/License-Code%20Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-Docs%20CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](CHANGELOG.md)

A collection of skills for use in Cursor, Claude, and similar environments. Maintained by Jing Wu.

**Language**: This document is the authoritative version in English. For a Chinese overview, see [README.zh-CN.md](README.zh-CN.md).

---

## ⭐ Featured: jw-agenda

**Plan and execute without leaving your editor.**

jw-agenda is a set of 5 Agent Skills that close the loop from planning to execution to review—all through natural language. Manage your life where you actually work; the assistant picks the right skill and keeps your workspace in sync. All data stays in local Markdown files.

**🔄 The complete loop**: 📅 Monthly plan → 📊 Weekly breakdown → ✅ Daily execution → 📝 Log → 📈 Weekly review

Simply say things like:
- 💬 "Generate this week's plan" → Breaks down monthly goals into a day-by-day plan
- 💬 "Generate today's plan" → Builds today's todo from weekly plan and yesterday's incomplete
- 💬 "I finished the resume update" → Logs progress and updates checkboxes automatically
- 💬 "Move applications to Wednesday" → Reschedules and syncs across plan files
- 💬 "Weekly summary" → Aggregates logs, completion rate, and carry-over items

**Core benefits:** Local-first (no cloud, full control) · Modular (5 skills, install any subset) · AI-native (talk in plain language, assistant picks the right skill)

---

## 📚 Contents

| Skill set | Description |
|-----------|-------------|
| [jw-agenda](jw-agenda/) | 📅 Personal agenda as **5 modular skills**: monthly plan → weekly breakdown → daily execution → log → weekly review. See [jw-agenda/README.md](jw-agenda/README.md). |
| [jw-agenda-v2](jw-agenda-v2/) | 📅 The same loop as a **single skill with 6 modes** (adds Monthly Review). One install, central routing. See [jw-agenda-v2/README.md](jw-agenda-v2/README.md). |

### 🚀 jw-agenda: Complete Personal Productivity System

**5 complementary skills** 🤝 that work together to automate your planning and execution workflow:

- ✅ **jw-agenda-daily-todo**: Generate today's plan, reschedule tasks, add ad-hoc items. Manages your daily todo with automatic schedule integration.
- 📝 **jw-agenda-daily-log**: Turn casual progress reports into structured logs. Summarize yesterday or record today's work with thoughts and feelings preserved.
- 📊 **jw-agenda-weekly-plan**: Break down monthly goals into day-by-day weekly plans. Merges carry-over tasks from last week automatically.
- 📈 **jw-agenda-weekly-review**: Aggregate weekly logs, calculate completion rates, track time allocation, and identify items to carry forward.
- 🔄 **jw-agenda-planning-sync**: Check consistency across daily/weekly/monthly plans, detect discrepancies, and sync after your confirmation.

### 📦 jw-agenda-v2: Same Loop, One Skill

`jw-agenda-v2` merges the workflow above into a **single Skill with six modes** and a central routing table, and adds a **Monthly Review** mode (with quarter / custom-range support). It uses the **same data format and configuration** as `jw-agenda`, so `jw-agenda-data/` is interchangeable between them.

- Prefer **jw-agenda** for fine-grained, modular installs (pick only the skills you want).
- Prefer **jw-agenda-v2** for a single install that covers the full loop, including monthly review.

See [jw-agenda-v2/README.md](jw-agenda-v2/README.md) for modes, installation, and data layout.

**✨ Key benefits**:
- 💬 **Natural language**: Just talk to your AI assistant—no complex commands or syntax
- 🔒 **Local storage**: All data stored as Markdown files in your workspace—privacy-focused and portable
- 🧩 **Modular design**: Install only the skills you need; each works independently
- 🔗 **Seamless integration**: Skills automatically read from each other's outputs when available
- 🎯 **Flexible workflow**: Supports both structured planning and casual progress reporting

**🎯 Perfect for**: Personal productivity, project planning, habit tracking, goal management, and anyone who wants to automate their planning workflow with AI assistance.

See the [detailed documentation](jw-agenda/README.md) for installation, examples, and complete feature list. To install, clone this repo and copy the skill folders from `jw-agenda/skills/` into your product's skills directory.

---

## 🚀 Quick Start

### For jw-agenda

1. 📁 **Create data directory**:
   ```bash
   mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}
   ```

2. 📦 **Install skills**: Clone this repo and copy the skill folders from `jw-agenda/skills/` into your Cursor skills directory (e.g., `~/.cursor/skills/`).

3. 📅 **Create your first monthly plan**: Add `YYYY-MM-plan.md` in `jw-agenda-data/monthly/` (e.g., `2026-02-plan.md`).

4. 🎉 **Start using**: Open your workspace in Cursor and say "Generate this week's plan" or "Generate today's plan".

For detailed installation instructions, examples, and customization options, see [jw-agenda/README.md](jw-agenda/README.md).

---

## 🛠️ Development

See [TODO.md](TODO.md) for planned improvements and known issues.

## 🔒 Security

See [SECURITY.md](SECURITY.md) for information about reporting security vulnerabilities.

## Community and feedback

This project is part of a **#BuildInPublic** journey. If you use Cursor or Claude and value a distraction-free, Markdown-based workflow, feedback is welcome. ❤️Contributions are welcome—see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

This repository as a whole is licensed under **Apache 2.0 for code** and **CC-BY-4.0 for documentation**. Applies to all contents (including subdirectories such as jw-agenda). See [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), [LICENSE-DOCS](LICENSE-DOCS).
