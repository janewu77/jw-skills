# 📅 jw-agenda-v2

**One skill, six modes — plan and execute without leaving your editor.**

`jw-agenda-v2` is the **single-skill** evolution of the [jw-agenda](../jw-agenda/) set: the same monthly → weekly → daily → log → review loop, plus a new **Monthly Review** mode, all merged into **one installable Skill** with a built-in routing table. You talk in natural language; the skill matches the right mode and keeps your Markdown workspace in sync. All data stays in local Markdown files.

**🌐 Language**: This document is the authoritative version in English. For a Chinese version, see [README.zh-CN.md](README.zh-CN.md).

**📜 License**: Code **Apache 2.0**, documentation **CC-BY-4.0**. See [LICENSE](../LICENSE), [LICENSE-CODE](../LICENSE-CODE), [LICENSE-DOCS](../LICENSE-DOCS).

---

## 🔀 jw-agenda vs jw-agenda-v2

Both cover the same planning workflow and use the **same data format and configuration**, so your `jw-agenda-data/` works with either. They differ in packaging:

| | [jw-agenda](../jw-agenda/) | **jw-agenda-v2** |
|---|---|---|
| **Shape** | 5 separate Skills | 1 Skill, 6 modes |
| **Install** | Install any subset independently | Install one folder |
| **Routing** | Each skill triggers on its own phrases | Central trigger table dispatches to a mode |
| **Modes** | Daily Todo · Daily Log · Weekly Plan · Weekly Review · Planning Sync | + **Monthly Review** (with quarter / custom-range support) |
| **Best when** | You want fine-grained, modular installs | You want one install and the full loop, incl. monthly review |

In short: **v2 is the "batteries-included" single skill**; the original `jw-agenda` set stays available for people who prefer to install only the pieces they use.

---

## 🎯 Overview

You talk; the skill routes to the right mode:

| 💬 You say… | ⚡ It does… |
|----------|----------|
| "Generate this week's plan" | 📖 Reads monthly plan + last week's carry-over → 📊 breaks it down by day |
| "Generate today's plan" | 📖 Reads weekly plan + yesterday's deferrable items → ✅ builds today's Todo with schedule |
| "I finished the resume update" | 📝 Writes the log and ✅ checks the matching Todo item |
| "Move applications to Wednesday" | 🔄 Removes from today → ➕ adds to Wednesday → 🔗 syncs plan files |
| "Summarize yesterday" | 📖 Reads yesterday's Todo → 📝 generates log → ➡️ carries deferrable items to today |
| "Weekly summary" | 📊 Aggregates this week's logs → 📈 completion rate + time allocation → 📄 weekly report |
| "Monthly review" / "Q1 review" | 📊 Aggregates the month/quarter → 📈 trends and totals → 📄 monthly (or quarterly) report |
| "Sync plans" | 🔍 Checks consistency across all levels → 📋 lists discrepancies → ✨ fixes after confirmation |

### Core benefits

- **Local-first:** All data lives in your Markdown files — no cloud, full control.
- **One install:** A single skill folder covers the full loop; no juggling multiple packages.
- **AI-native:** Say what you want in plain language; the routing table picks the mode.
- **Cascading sync:** Planning modes cascade top-down (tasks/TODO → monthly → weekly → daily); logging modes cascade bottom-up with lightweight status marks, so every layer stays consistent automatically.

---

## 🛠️ The Six Modes

All modes live in one skill and are selected by the trigger table in [`SKILL.md`](skills/jw-agenda-v2/SKILL.md).

### ✅ Daily Todo — `references/mode-daily-todo.md`
Generates today's todo (schedule + prioritized tasks) from the monthly/weekly plan and yesterday's **deferrable** carry-over. Includes sub-modes to query progress, update status (cancel/postpone), and an **Add/Move Task** sub-mode ([`mode-add-or-move.md`](skills/jw-agenda-v2/references/mode-add-or-move.md)).
**💬 Triggers**: "Generate today's plan", "today plan", "add a task", "move X to Wednesday"

### 📝 Daily Log — `references/mode-daily-log.md`
Turns a casual progress report into a structured log, checks the matching Todo items, and carries deferrable incomplete items forward.
**💬 Triggers**: "Summarize yesterday", "report today", "I finished X", "log it"

### 📊 Weekly Plan — `references/mode-weekly-plan.md`
Breaks the monthly plan into a day-by-day weekly plan, merging last week's carry-over.
**💬 Triggers**: "Generate this week's plan", "weekly plan", "plan next week"

### 📈 Weekly Review — `references/mode-weekly-review.md`
Aggregates the week's logs and todos into completion rate, time allocation, and a carry-over list. Also hosts the **Archive Logs** step (movable older daily files into `YYYYMM/` subfolders).
**💬 Triggers**: "Weekly summary", "review this week", "archive daily"

### 🗓️ Monthly Review — `references/mode-monthly-review.md`
Aggregates the month's weekly reviews and logs into a monthly report. Supports **quarters** (`Q1`–`Q4`) and **custom ranges** (e.g. `2026-01 to 2026-03`).
**💬 Triggers**: "Monthly review", "月总结", "Q1 review", "recap this month"

### 🔄 Planning Sync — `references/mode-planning-sync.md`
Cross-checks consistency across tasks/TODO, yearly, monthly, weekly, and daily levels; classifies discrepancies as action-needed vs. informational and applies fixes only after confirmation. A post-hoc safety net over the cascading updates.
**💬 Triggers**: "Sync plans", "check consistency", "planning sync"

---

## 🔄 Workflow

```
┌─────────────┐
│ 📅 Monthly  │  ← 👤 User maintains (goals, weekly focus)
│ YYYY-MM-plan│
└──────┬──────┘
       │ 📊 weekly-plan reads this week's goals
       ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 📊 Weekly    │────→│ 📈 Weekly   │────→│ 🗓️ Monthly  │
│ Week{N}-plan │     │ Week{N}-review    │ YYYY-MM-review
└──────┬──────┘     └──────▲──────┘     └─────────────┘
       │ ✅ daily-todo      │ 📈 weekly-review    ▲ monthly-review
       ▼                   │                     │ aggregates weeks
┌─────────────┐     ┌─────────────┐              │
│ ✅ Daily Todo│────→│ 📝 Log      │──────────────┘
│ date-todo   │     │ date-log    │
└─────────────┘     └─────────────┘

        ↕ 🔄 planning-sync (check all layers)
```

**🌅 Daily**: morning "generate today's plan" → during day "I finished X" → evening "summarize today"
**📅 Weekly**: Monday "generate this week's plan" → mid-week "sync plans" → weekend "weekly summary"
**🗓️ Monthly**: month-end "monthly review" (or "Q1 review" at quarter close)

---

## 🚀 Installation

### 📋 Prerequisites

- ✅ An AI environment that supports Agent Skills (e.g. Cursor, Claude Desktop).
- 🐍 **Python 3.9+** (for the bundled `date_utils.py` / `dedup_todos.py`; tested on 3.9–3.13).
- 📁 A workspace folder for your agenda data (defaults to `jw-agenda-data/` at the workspace root).

### ⚡ Setup

```bash
# 1. Create the data directory
mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}

# 2. Install the skill — copy the skill folder into your skills directory
#    (Cursor user-level shown; use .cursor/skills/ for project-level)
cp -r jw-agenda-v2/skills/jw-agenda-v2 ~/.cursor/skills/
```

**Optional — custom schedule**: copy [`assets/schedule-config.example.md`](skills/jw-agenda-v2/assets/schedule-config.example.md) to your jw-agenda root as `schedule-config.md` and edit the time slots. Without it, the built-in default template is used.

**Optional — custom summary categories**: copy [`assets/summary-categories.example.md`](skills/jw-agenda-v2/assets/summary-categories.example.md) to your jw-agenda root as `summary-categories.md`.

**Optional — custom data root**: create `.jw-agenda.json` (or `jw-agenda.json`) at the workspace root:

```json
{
  "agendaRoot": "jw-agenda-data",
  "archiveAfterDays": 14
}
```

`archiveAfterDays` controls when old `daily/` files are moved into `YYYYMM/` subfolders (default 14; set `0` or negative to disable).

Then open your workspace and say "Generate this week's plan" or "Generate today's plan".

---

## 📁 Data Layout & File Naming

Skills install into your product's skill directory; your **workspace only holds data**:

```
<workspace>/
├── .jw-agenda.json            ← Optional (custom root / archive threshold)
└── jw-agenda-data/            ← jw-agenda root (default)
    ├── schedule-config.md     ← Optional
    ├── summary-categories.md  ← Optional
    ├── yearly/                ← Optional
    ├── monthly/               ← YYYY-MM-plan.md, YYYY-MM-review.md
    ├── weekly/                ← Week{N}-plan.md, Week{N}-review.md
    ├── daily/                 ← YYYY-MM-DD-todo.md, YYYY-MM-DD-log.md
    └── tasks/                 ← TODO.md, reading lists, etc.
```

| 📄 Type | 📋 Format | 📁 Dir | 💡 Example |
|------|--------|-----|---------|
| Yearly plan (optional) | `YYYY-plan.md` | `yearly/` | `2026-plan.md` |
| Monthly plan | `YYYY-MM-plan.md` | `monthly/` | `2026-02-plan.md` |
| Monthly review | `YYYY-MM-review.md` | `monthly/` | `2026-02-review.md` |
| Quarterly review | `YYYY-Q{N}-review.md` | `monthly/` | `2026-Q1-review.md` |
| Weekly plan | `Week{N}-plan.md` | `weekly/` | `Week6-plan.md` |
| Weekly review | `Week{N}-review.md` | `weekly/` | `Week6-review.md` |
| Daily Todo | `YYYY-MM-DD-todo.md` | `daily/` | `2026-02-06-todo.md` |
| Daily Log | `YYYY-MM-DD-log.md` | `daily/` | `2026-02-06-log.md` |

N = ISO week number (1–52); e.g. 2026-02-05 → Week 6. Full rules: [`assets/conventions.md`](skills/jw-agenda-v2/assets/conventions.md).

---

## ⚙️ Customization

- **⏰ Schedule**: edit `schedule-config.md` in your jw-agenda root to change time slots / fixed activities.
- **🗂️ Summary categories**: edit `summary-categories.md` to control how daily/weekly/monthly summaries are grouped.
- **📋 Conventions**: naming, paths, marks, dedup, and cascade rules live in [`assets/`](skills/jw-agenda-v2/assets/). Users rarely change these; to customize, edit them in your installed skill copy.
- **📅 Monthly plan format**: free-form; including "this month's goals" and `Week N` sections helps Weekly Plan and Monthly Review.

---

## 👥 Development

Run the unit tests (46 tests covering `date_utils.py` and `dedup_todos.py`):

```bash
cd jw-agenda-v2/tests
python3 -m unittest -v
```

See [Todo.md](Todo.md) for the improvement backlog and [doc/CHANGELOG.md](doc/CHANGELOG.md) for version history. Contributions welcome — see the repo [CONTRIBUTING.md](../CONTRIBUTING.md).

## 🔒 Security

See [SECURITY.md](../SECURITY.md) for reporting security vulnerabilities.

---

## License

Code: Apache 2.0. Documentation: CC-BY-4.0. See [LICENSE](../LICENSE) | [LICENSE-CODE](../LICENSE-CODE) | [LICENSE-DOCS](../LICENSE-DOCS).
