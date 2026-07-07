# jw-skills

[![License: Apache 2.0](https://img.shields.io/badge/License-Code%20Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-Docs%20CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](CHANGELOG.md)

A collection of skills for use in Cursor, Claude, and similar environments. Maintained by Jing Wu.

**Language**: This document is the authoritative version in English. For a Chinese overview, see [README.zh-CN.md](README.zh-CN.md).

---

## ⭐ Featured: jw-agenda-v2

**Plan and execute without leaving your editor.**

jw-agenda-v2 is a single Agent Skill with six modes that close the loop from planning to execution to review—all through natural language. Manage your life where you actually work; the skill routes to the right mode and keeps your workspace in sync. All data stays in local Markdown files.

**🔄 The complete loop**: 📅 Monthly plan → 📊 Weekly breakdown → ✅ Daily execution → 📝 Log → 📈 Weekly review → 🗓️ Monthly review

Simply say things like:
- 💬 "Generate this week's plan" → Breaks down monthly goals into a day-by-day plan
- 💬 "Generate today's plan" → Builds today's todo from weekly plan and yesterday's incomplete
- 💬 "I finished the resume update" → Logs progress and updates checkboxes automatically
- 💬 "Move applications to Wednesday" → Reschedules and syncs across plan files
- 💬 "Weekly summary" / "Monthly review" → Aggregates logs, completion rate, and carry-over items

**Core benefits:** Local-first (no cloud, full control) · One install (a single skill, six modes) · AI-native (talk in plain language, the routing table picks the mode)

> Prefer fine-grained, modular installs? The original **[jw-agenda](jw-agenda/)** ships the same workflow as 5 independently installable skills.

---

## 📚 Contents

| Skill set | Description |
|-----------|-------------|
| [jw-agenda](jw-agenda/) | 📅 Personal agenda as **5 modular skills**: monthly plan → weekly breakdown → daily execution → log → weekly review. See [jw-agenda/README.md](jw-agenda/README.md). |
| [jw-agenda-v2](jw-agenda-v2/) | 📅 The same loop as a **single skill with 6 modes** (adds Monthly Review). One install, central routing. See [jw-agenda-v2/README.md](jw-agenda-v2/README.md). |

### 🚀 jw-agenda — 5 modular skills

**5 complementary skills** 🤝 that work together to automate your planning and execution workflow:

- ✅ **jw-agenda-daily-todo**: Generate today's plan, reschedule tasks, add ad-hoc items. Manages your daily todo with automatic schedule integration.
- 📝 **jw-agenda-daily-log**: Turn casual progress reports into structured logs. Summarize yesterday or record today's work with thoughts and feelings preserved.
- 📊 **jw-agenda-weekly-plan**: Break down monthly goals into day-by-day weekly plans. Merges carry-over tasks from last week automatically.
- 📈 **jw-agenda-weekly-review**: Aggregate weekly logs, calculate completion rates, track time allocation, and identify items to carry forward.
- 🔄 **jw-agenda-planning-sync**: Check consistency across daily/weekly/monthly plans, detect discrepancies, and sync after your confirmation.

📖 Installation, examples, and the complete feature list: **[jw-agenda/README.md](jw-agenda/README.md)**.

### 📦 jw-agenda-v2 — same loop, one skill

`jw-agenda-v2` merges the workflow above into a **single Skill with six modes** and a central routing table, and adds a **Monthly Review** mode (with quarter / custom-range support). It uses the **same data format and configuration** as `jw-agenda`, so `jw-agenda-data/` is interchangeable between them.

- Prefer **jw-agenda** for fine-grained, modular installs (pick only the skills you want).
- Prefer **jw-agenda-v2** for a single install that covers the full loop, including monthly review.

📖 Modes, installation, and data layout: **[jw-agenda-v2/README.md](jw-agenda-v2/README.md)**.

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
