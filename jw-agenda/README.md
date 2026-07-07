# 📅 jw-Agenda

**Plan and execute without leaving your editor.**

Personal agenda skill set based on [Agent Skills](https://agentskills.io/home). Drive the full loop **📅 monthly plan → 📊 weekly breakdown → ✅ daily execution → 📝 log → 📈 weekly review** with natural language—manage your life where you actually work. All data is stored locally as Markdown files.

**Why jw-agenda?** No more switching to a calendar or to-do app: you stay in the editor and talk to the assistant. It picks the right skill and keeps your workspace in sync.

**🌐 Language**: This document is the authoritative version in English. For a Chinese version, see [README.zh-CN.md](README.zh-CN.md).

**📜 License**: This repository uses **Apache 2.0 for code** and **CC-BY-4.0 for documentation**. See [LICENSE](../LICENSE), [LICENSE-CODE](../LICENSE-CODE), [LICENSE-DOCS](../LICENSE-DOCS).

---

## 🎯 Overview

You talk; the assistant picks the right Skill:

| 💬 You say… | ⚡ It does… |
|----------|----------|
| "Generate this week's plan" | 📖 Reads monthly plan + last week's incomplete → 📊 breaks down into a weekly plan by day |
| "Generate today's plan" | 📖 Reads weekly plan + yesterday's incomplete → ✅ generates today's Todo with schedule |
| "I finished the resume update" | 📝 daily-log writes the log and ✅ checks the corresponding today Todo |
| "Move applications to Wednesday" | 🔄 Removes from today → ➕ adds to Wednesday → 🔗 syncs weekly plan |
| "Add: meet advisor next week" | ➕ Writes to next week's plan file |
| "Today I did XX, still have YY left, feeling tired" | 🧠 Parses casual report → 📝 generates log → ✅ syncs checkboxes |
| "Summarize yesterday" | 📖 Reads yesterday's Todo → 📝 generates log → ➡️ moves incomplete to today |
| "Sync plans" | 🔍 Checks consistency across all levels (tasks/yearly/monthly/weekly/daily) → 📋 lists discrepancies → ✨ fixes after confirmation |
| "Weekly summary" | 📊 Aggregates this week's logs → 📈 completion rate and time allocation → 📄 weekly report |

### Core benefits

- **Local-first:** All data stays in your local Markdown files—no cloud, full control.
- **Modular:** Five distinct skills covering the full productivity cycle; each is installable on its own.
- **AI-native:** Designed for the "talk to AI" workflow—say what you want in plain language and the assistant picks the right skill.
- **Cascading sync:** Planning actions (daily-todo, weekly-plan) cascade top-down (tasks/TODO → monthly → weekly → daily); logging actions (daily-log, weekly-review) cascade bottom-up with lightweight status marks. All layers stay consistent automatically.

---

## 🔄 Workflow

```
┌─────────────┐
│ 📅 Monthly  │  ← 👤 User maintains (goals, weekly focus)
│ YYYY-MM-plan│
└──────┬──────┘
       │ 📊 weekly-plan reads this week's goals
       ▼
┌─────────────┐     ┌─────────────┐
│ 📊 Weekly    │────→│ 📈 Weekly   │
│ Week{N}-plan │     │ Week{N}-review
└──────┬──────┘     └──────▲──────┘
       │ ✅ daily-todo      │ 📈 weekly-review
       │ reads daily tasks │ aggregates logs
       ▼                   │
┌─────────────┐     ┌─────────────┐
│ ✅ Daily Todo│────→│ 📝 Log      │
│ date-todo   │     │ date-log    │
└─────────────┘     └─────────────┘
  ✅ daily-todo       📝 daily-log
  (plan & execute)   (record)

        ↕ 🔄 planning-sync (check all layers)
```

**🌅 Daily**: Morning "generate today's plan" → during day "I finished X" → evening "today I did… feeling…"

**📅 Weekly**: Monday "generate this week's plan" → mid-week "sync plans" → weekend "weekly summary"

---

## 🛠️ Skills

This set has **5 Skills**, each **installable on its own**. With multiple installed they work together 🤝 but do not depend on each other—missing one does not break the others.

### ✅ jw-agenda-daily-todo — Daily Todo

Manages today's todo: generate plan, reschedule, add ad-hoc items. **Does not mark completion** ("I finished X" is handled by daily-log).

**✨ Features**: Generate today's Todo with schedule from monthly/weekly plan and yesterday's incomplete; cancel/postpone, move items to other days and sync plan files; add ad-hoc items for today/this week/this month/later; query today's progress.

**💬 Triggers**: "Generate today's plan", "Move X to Wednesday", "Add one", "Tomorrow I need", "Later I need", "Drop Y", "How's today going"

**🔗 With others**: If daily-log is installed, recognizes "carried from yesterday" to avoid duplicates. If weekly-plan is installed, uses weekly plan as source for today.

### 📝 jw-agenda-daily-log — Log and report

Turns casual progress reports into structured logs and keeps notes and thoughts.

**✨ Features**: Summarize yesterday into a log; accept today's casual report (can be informal, with thoughts) and generate log; move incomplete to today's Todo.

**💬 Triggers**: "Summarize yesterday", "Report today", "Log today", "Today I did…", "I finished X", "Homework done"

**🔗 With others**: If daily-todo is installed, today's report also updates today's Todo checkboxes.

### 📊 jw-agenda-weekly-plan — Weekly plan

Breaks down the monthly plan into a day-by-day weekly plan.

**✨ Features**: Read this week's goals from the monthly plan; merge last week's carry-over; assign by day and write the weekly plan file.

**💬 Triggers**: "Generate this week's plan", "Weekly plan", "weekly plan"

**🔗 With others**: If weekly-review is installed, reads "carry to next week" from last week's review as carry-over source.

### 📈 jw-agenda-weekly-review — Weekly review

Aggregates the week's logs and Todo into a summary and stats.

**✨ Features**: Aggregate all logs for the week; completion rate (by priority) and time allocation; list items to carry to next week.

**💬 Triggers**: "Weekly summary", "This week review", "weekly review"

**🔗 With others**: If weekly-plan is installed, compares weekly plan vs actual. The "carry to next week" list can be read by weekly-plan next week.

### 🔄 jw-agenda-planning-sync — Plan consistency check

Checks consistency across all planning levels (tasks/TODO, yearly, monthly, weekly, daily).

**✨ Features**: Compare task content and completion status across all available levels; classify discrepancies as "action needed" or "informational"; show suggested changes and apply only after user confirmation. Acts as a post-hoc global verification to catch any inconsistencies not caught by the other skills' cascading updates.

**💬 Triggers**: "Sync plans", "Check consistency", "planning sync"

**🔗 With others**: Scope depends on which Skills produced which files. Verifies that daily-todo/weekly-plan's top-down cascades and daily-log/weekly-review's bottom-up status syncs are complete.

---

## 🚀 Installation

For **Cursor**, see [Agent Skills (install and skill directory)](https://cursor.com/docs/context/skills).

### 📋 Prerequisites

- ✅ An AI environment that supports Skills (e.g. Cursor, Claude Desktop).
- 🐍 **Python 3.9+** (required for scripts used by skills; tested on Python 3.9, 3.10, 3.11, 3.12)
- 📁 A folder for agenda data (the **workspace**). **Open your workspace root**; jw-agenda data defaults to `jw-agenda-data/` under that root, or another path via `.jw-agenda.json` or `jw-agenda.json` (see "Configure jw-agenda root" below).

**✅ Tested environments**:
- 💻 Cursor (latest versions)
- 🤖 Claude Desktop (latest versions)
- 🐍 Python 3.9, 3.10, 3.11, 3.12 on Linux, macOS, Windows (WSL/Git Bash)

### ⚡ Quick Start (One-Command Setup)

**For Cursor users**: Clone this repo, then run this in your workspace root to create the data directory and install all 5 Skills by copying the skill folders:

```bash
# Step 1: Create data directory
mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}

# Step 2: Install Skills — copy the skill folders from the cloned repo
cd jw-agenda && for skill in skills/jw-agenda-*/; do cp -r "$skill" ~/.cursor/skills/; done && cd ..
```

**Note**: Replace `~/.cursor/skills/` with `.cursor/skills/` for project-level installation, or adjust the path per your Cursor setup.

**Shell**: These are Bash commands (Linux, macOS, Git Bash, WSL). They do **not** run in Windows **cmd**; use **Git Bash** or **WSL**, or copy each skill folder manually into Cursor’s skills directory.

After running the above, open your workspace in Cursor and start using the Skills. See "Install steps" below for details and customization options.

### Repo layout (jw-agenda)

```
jw-agenda/
├── README.md
├── CONTRIBUTING.md
├── _common/                    ← Single source for conventions and scripts (maintainers)
│   ├── conventions.md
│   ├── schedule-config.example.md
│   └── scripts/
├── scripts/
│   └── sync-common-to-skills.sh
└── skills/                     ← 5 installable Skills
    ├── jw-agenda-daily-todo/
    ├── jw-agenda-daily-log/
    ├── jw-agenda-weekly-plan/
    ├── jw-agenda-weekly-review/
    └── jw-agenda-planning-sync/
```

### User workspace layout (after install)

Skills install into the product's skill directory and **do not** live inside your workspace. Your workspace only has **data** and optional **schedule config**. Default:

```
<workspace>/
└── jw-agenda-data/             ← jw-agenda root (default)
    ├── schedule-config.md      ← Optional; copy from any skill's assets/schedule-config.example.md
    ├── yearly/                 ← Optional (yearly plan)
    ├── monthly/
    │   └── YYYY-MM-plan.md
    ├── weekly/
    ├── daily/
    └── tasks/
```

### Install steps

#### Full install (recommended)

**Step 1: Create data directory**

Default jw-agenda root is **`jw-agenda-data`** in your workspace:

```bash
cd <workspace>
mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}
```

**Optional — Configure jw-agenda root**: In the workspace root create `.jw-agenda.json` or `jw-agenda.json` with `{"agendaRoot":"your/path"}` to use another directory (e.g. `docs/agenda`, `notes/plans`); then create `monthly`, `weekly`, `daily`, `tasks` under that path. Without this file, `jw-agenda-data` is used.

(Skills may create or prompt for missing directories on first run.)

**Step 2 (optional): Custom schedule**

To customize daily time slots, copy any skill's `assets/schedule-config.example.md` to the **jw-agenda root** as `schedule-config.md` (default: `jw-agenda-data/`):

```bash
cp <path-to-any-skill>/assets/schedule-config.example.md jw-agenda-data/schedule-config.md
```

Edit the file. **Without it**, daily-todo uses the built-in default template.

**Step 3: Install Skills**

- **📦 Copy from source (recommended)**: Clone this repo and copy the needed skill folders from `jw-agenda/skills/` into your product's skills directory (user: `~/.cursor/skills/`; project: `.cursor/skills/`). Conventions and scripts live inside each skill folder; no extra copy to the user dir. See [Cursor: Agent Skills](https://cursor.com/docs/context/skills).
  ```bash
  cp -r jw-agenda/skills/jw-agenda-daily-log ~/.cursor/skills/
  cp -r jw-agenda/skills/jw-agenda-daily-todo ~/.cursor/skills/
  # same for the other 3 skills
  ```
- **Optional — build local zips**: If you want a single bundle to hand to someone, run `./package-skills.sh` in `jw-agenda/` to generate zips under `output/`; the recipient unzips each into their skills directory.

**Step 4 (recommended): Create monthly plan**

In the jw-agenda root's `monthly/` (default `jw-agenda-data/monthly/`) create the current month's plan as `YYYY-MM-plan.md` (e.g. `2026-02-plan.md`). Format is free; organizing by week helps weekly-plan:

```markdown
# February 2026 plan

## This month's goals
- 30 job applications
- 30 min English speaking daily

## Week 1 (2.1–2.7)
- Focus: resume update, first batch of applications

## Week 2 (2.8–2.14)
- Focus: …
```

**Step 5: Open your workspace root** in your product (data in `jw-agenda-data/` or your configured path) and start using the Skills.

#### Install a single Skill

You can install only one Skill. Each Skill ships with its conventions and scripts; you only need the **jw-agenda root** (default `jw-agenda-data`, or via `.jw-agenda.json` / `jw-agenda.json`) and subdirs monthly, weekly, daily, tasks; optional `schedule-config.md` in that root.

1. Create the data dir: `mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}` (if using default and not yet created); for a custom path, set `.jw-agenda.json` or `jw-agenda.json` first, then create the subdirs.
2. Install only the skill folder(s) you need per your product's docs; Cursor: [Agent Skills](https://cursor.com/docs/context/skills).
3. Without other Skills, that Skill skips missing data sources and still works.

---

## 📚 Examples

### 🎯 Quick Start with Sample Workspace

We provide two versions of sample workspaces (English and Chinese). Copy one to get started:

**English version:**
```bash
cp -r jw-agenda/examples/sample-workspace jw-agenda-data
```

**Chinese version (中文版):**
```bash
cp -r jw-agenda/examples/sample-workspace-zh jw-agenda-data
```

Each includes sample files for:
- 📅 Monthly plan (`monthly/2026-02-plan.md`)
- 📊 Weekly plan (`weekly/Week6-plan.md`)
- ✅ Daily todo (`daily/2026-02-05-todo.md`)
- 📝 Daily log (`daily/2026-02-05-log.md`)
- 📈 Weekly review (`weekly/Week6-review.md`)

See [examples/README.md](examples/README.md) for details.

### 💬 Conversation Examples

- **🇬🇧 English**: See [examples/conversations.md](examples/conversations.md) for complete examples showing:
  - 📊 How to generate weekly plans
  - 📝 How to report daily progress
  - ➕ How to add ad-hoc tasks
  - 📈 How to generate weekly reviews
  - 🔄 How to sync plans for consistency

- **🇨🇳 Chinese (中文)**: 参见 [examples/conversations.zh-CN.md](examples/conversations.zh-CN.md) 了解完整示例

---

## 📖 Trigger cheat sheet

| 🎯 Goal | 💬 Say |
|------|-----|
| 📊 Generate weekly plan | "Generate this week's plan" / "Weekly plan" / "weekly plan" |
| ✅ Generate today's Todo | "Generate today's plan" / "today plan" |
| 📝 Report progress, write log | "Today I did XXX, still YYY left, feeling…" |
| 📝 Summarize yesterday | "Summarize yesterday" / "Log yesterday" |
| ✅ Mark done (log + checkbox) | "I finished XXX" / "Homework done" / "Log today" |
| 🔄 Reschedule | "Move XXX to Wednesday" / "Postpone to next week" |
| ➕ Add ad-hoc | "Add one: XXX" / "Tomorrow: YYY" / "Later: ZZZ" |
| 🔍 Check consistency | "Sync plans" / "Check consistency" / "planning sync" |
| 📈 Weekly summary | "Weekly summary" / "This week review" / "weekly review" |

---

## 📝 File naming

| 📄 Type | 📋 Format | 📁 Dir | 💡 Example |
|------|--------|-----|---------|
| 📆 Yearly plan (optional) | `YYYY-plan.md` | `yearly/` | `2026-plan.md` |
| 📅 Monthly plan | `YYYY-MM-plan.md` | `monthly/` | `2026-02-plan.md` |
| 📊 Weekly plan | `Week{N}-plan.md` | `weekly/` | `Week1-plan.md` |
| 📈 Weekly review | `Week{N}-review.md` | `weekly/` | `Week1-review.md` |
| ✅ Daily Todo | `YYYY-MM-DD-todo.md` | `daily/` | `2026-02-06-todo.md` |
| 📝 Log | `YYYY-MM-DD-log.md` | `daily/` | `2026-02-06-log.md` |

N = ISO week number (1–52). E.g. 2026-02-05 → Week 6.

Full rules: each Skill's `assets/conventions.md` (or this repo's `_common/conventions.md`).

---

## ⚙️ Customization

**⏰ Schedule**: If you create `schedule-config.md` in the jw-agenda root (default `jw-agenda-data`), edit it to add/remove time slots and fixed activities. daily-todo uses it for the daily schedule; without it, the Skill's default template is used.

**📋 Conventions**: Naming, paths, markers, priorities are in each Skill's `assets/conventions.md`. Users usually don't change them; to customize, edit the file in your installed skill dir, or change `_common/conventions.md` in this repo and re-package.

**📅 Monthly plan format**: Free-form. Including "this month's goals" and `Week N` sections helps weekly-plan.

**🐍 Scripts**: Each Skill's `assets/scripts/date_utils.py` and `dedup_todos.py` are installed with the Skill for date math and todo dedup. These require **Python 3.9+** to run.

### 👥 For Contributors

**🐍 Python environment**: Python 3.9+ is required. For running tests, install pytest:
```bash
pip install pytest
pytest jw-agenda/tests/ -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

---

## 📦 Distributing

Skills are distributed **from source**: clone or download this repo and copy the skill folders from `jw-agenda/skills/` into the product's skills directory. Each skill folder is self-contained (conventions and scripts included), so there is nothing extra to copy. Recipients then create the **jw-agenda root** (default `jw-agenda-data`, or via `.jw-agenda.json` / `jw-agenda.json`) with subdirs monthly, weekly, daily, tasks; optionally copy any skill's `assets/schedule-config.example.md` to the jw-agenda root as `schedule-config.md` to customize the schedule.

**🔨 Optional — local zip bundle**: If you'd rather hand someone a single bundle instead of the repo, run `./package-skills.sh` in the **jw-agenda directory** to generate per-skill zips under `jw-agenda/output/`; the recipient unzips each into their skills directory.

```bash
cd jw-agenda
./package-skills.sh
```

---

## 🛠️ Development

See [TODO.md](TODO.md) for planned improvements and known issues.

## 🔒 Security

See [SECURITY.md](../../SECURITY.md) for information about reporting security vulnerabilities.

## Community and feedback

This project is part of a **#BuildInPublic** journey. If you use Cursor or Claude and value a distraction-free, Markdown-based workflow, feedback is welcome. Contributions are welcome—see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

Code: Apache 2.0. Documentation: CC-BY-4.0. See [LICENSE](../LICENSE) | [LICENSE-CODE](../LICENSE-CODE) | [LICENSE-DOCS](../LICENSE-DOCS).
