# 📅 jw-agenda-v2

**一个 skill，六种模式——在编辑器里完成规划与执行。**

`jw-agenda-v2` 是 [jw-agenda](../jw-agenda/) 技能组的**单 skill 版**演进：同样的「月计划 → 周分解 → 每日执行 → 日志 → 复盘」闭环，外加全新的**月总结**模式，全部合并进**一个可安装的 Skill**,内置路由表。你用自然语言说话，skill 自动匹配对应模式，并保持你的 Markdown 工作区一致。所有数据都以本地 Markdown 文件存储。

**🌐 语言**：英文版为权威版本，见 [README.md](README.md)。本文为中文版。

**📜 许可**：代码 **Apache 2.0**，文档 **CC-BY-4.0**。见 [LICENSE](../LICENSE)、[LICENSE-CODE](../LICENSE-CODE)、[LICENSE-DOCS](../LICENSE-DOCS)。

---

## 🔀 jw-agenda 与 jw-agenda-v2 的区别

两者覆盖同一套规划流程，**数据格式和配置完全相同**，所以你的 `jw-agenda-data/` 两边通用。差别只在打包方式：

| | [jw-agenda](../jw-agenda/) | **jw-agenda-v2** |
|---|---|---|
| **形态** | 5 个独立 Skill | 1 个 Skill、6 种模式 |
| **安装** | 可按需只装其中几个 | 安装一个文件夹 |
| **路由** | 各 skill 各自触发 | 中央触发表分发到模式 |
| **模式** | 每日 Todo · 日志 · 周规划 · 周总结 · 规划同步 | + **月总结**（支持季度/自定义范围） |
| **适合** | 想要细粒度、模块化安装 | 想一次装好、含月总结的完整闭环 |

一句话：**v2 是「开箱即全」的单一 skill**；原 `jw-agenda` 组保留给偏好只装所需部分的人。

---

## 🎯 概览

你说话，skill 路由到对应模式：

| 💬 你说… | ⚡ 它做… |
|----------|----------|
| "生成本周计划" | 📖 读月计划 + 上周结转 → 📊 按天分解 |
| "生成今天的计划" | 📖 读周计划 + 昨天可结转项 → ✅ 生成带日程的今日 Todo |
| "简历更新完成了" | 📝 写日志并 ✅ 勾选对应 Todo |
| "把投递挪到周三" | 🔄 从今天移除 → ➕ 加到周三 → 🔗 同步计划文件 |
| "总结昨天" | 📖 读昨日 Todo → 📝 生成日志 → ➡️ 把可结转项带到今天 |
| "周总结" | 📊 汇总本周日志 → 📈 完成率 + 时间分配 → 📄 周报 |
| "月总结" / "Q1 总结" | 📊 汇总当月/季度 → 📈 趋势与合计 → 📄 月度（或季度）报告 |
| "同步规划" | 🔍 检查各层一致性 → 📋 列出差异 → ✨ 确认后修正 |

### 核心优势

- **本地优先**：数据都在你的 Markdown 文件里——无云端、完全掌控。
- **一次安装**：单个 skill 文件夹覆盖完整闭环，不必管理多个包。
- **AI 原生**：用自然语言表达，路由表自动挑选模式。
- **级联同步**：规划类模式自上而下级联（tasks/TODO → 月 → 周 → 日）；日志类模式自下而上以轻量状态标记级联，各层自动保持一致。

---

## 🛠️ 六种模式

所有模式都在同一个 skill 内，由 [`SKILL.md`](skills/jw-agenda-v2/SKILL.md) 的触发表选择。

### ✅ 每日 Todo — `references/mode-daily-todo.md`
从月/周计划和昨天的**可结转**项生成今日 todo（日程 + 优先级任务）。含查询进度、更新状态（取消/推迟）子模式，以及**加/移任务**子模式（[`mode-add-or-move.md`](skills/jw-agenda-v2/references/mode-add-or-move.md)）。
**💬 触发**："生成今天的计划"、"today plan"、"加一项"、"把 X 移到周三"

### 📝 每日日志 — `references/mode-daily-log.md`
把口语化的进度汇报变成结构化日志，勾选对应 Todo 项，并把可结转的未完成项带到今天。
**💬 触发**："总结昨天"、"汇报今天"、"我完成了 X"、"记录一下"

### 📊 周规划 — `references/mode-weekly-plan.md`
把月计划分解成逐天的周计划，合并上周结转。
**💬 触发**："生成本周计划"、"周规划"、"规划下周"

### 📈 周总结 — `references/mode-weekly-review.md`
把一周的日志和 todo 汇总为完成率、时间分配和结转清单。也承载**归档日志**步骤（把较旧的 daily 文件移入 `YYYYMM/` 子目录）。
**💬 触发**："周总结"、"本周回顾"、"归档日志"

### 🗓️ 月总结 — `references/mode-monthly-review.md`
把当月的周总结和日志汇总为月度报告。支持**季度**（`Q1`–`Q4`）和**自定义范围**（如 `2026-01 to 2026-03`）。
**💬 触发**："月总结"、"本月回顾"、"Q1 总结"、"recap this month"

### 🔄 规划同步 — `references/mode-planning-sync.md`
跨 tasks/TODO、年、月、周、日各层交叉检查一致性；把差异分为「需行动」与「仅告知」，仅在确认后修正。是级联更新之上的事后安全网。
**💬 触发**："同步规划"、"检查一致性"、"planning sync"

---

## 🔄 工作流

```
┌─────────────┐
│ 📅 月计划    │  ← 👤 用户维护（目标、每周重点）
│ YYYY-MM-plan│
└──────┬──────┘
       │ 📊 周规划读取本周目标
       ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 📊 周计划    │────→│ 📈 周总结   │────→│ 🗓️ 月总结   │
│ Week{N}-plan │     │ Week{N}-review    │ YYYY-MM-review
└──────┬──────┘     └──────▲──────┘     └─────────────┘
       │ ✅ 每日 Todo       │ 📈 周总结          ▲ 月总结
       ▼                   │ 汇总日志           │ 汇总各周
┌─────────────┐     ┌─────────────┐            │
│ ✅ 每日 Todo │────→│ 📝 日志     │────────────┘
│ date-todo   │     │ date-log    │
└─────────────┘     └─────────────┘

        ↕ 🔄 规划同步（检查所有层级）
```

**🌅 每日**：早上"生成今天的计划" → 白天"我完成了 X" → 晚上"总结今天"
**📅 每周**：周一"生成本周计划" → 周中"同步规划" → 周末"周总结"
**🗓️ 每月**：月底"月总结"（季度末"Q1 总结"）

---

## 🚀 安装

### 📋 前置要求

- ✅ 支持 Agent Skills 的 AI 环境（如 Cursor、Claude Desktop）。
- 🐍 **Python 3.9+**（用于内置的 `date_utils.py` / `dedup_todos.py`；已在 3.9–3.13 测试）。
- 📁 一个存放日程数据的工作区文件夹（默认为工作区根下的 `jw-agenda-data/`）。

### ⚡ 步骤

```bash
# 1. 创建数据目录
mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}

# 2. 安装 skill —— 把 skill 文件夹拷进你的 skills 目录
#    （示例为 Cursor 用户级；项目级用 .cursor/skills/）
cp -r jw-agenda-v2/skills/jw-agenda-v2 ~/.cursor/skills/
```

**可选 — 自定义作息**：把 [`assets/schedule-config.example.md`](skills/jw-agenda-v2/assets/schedule-config.example.md) 拷到 jw-agenda 根目录并改名为 `schedule-config.md`，编辑时间段。没有它时使用内置默认模板。

**可选 — 自定义总结分类**：把 [`assets/summary-categories.example.md`](skills/jw-agenda-v2/assets/summary-categories.example.md) 拷到 jw-agenda 根目录并改名为 `summary-categories.md`。

**可选 — 自定义数据根目录**：在工作区根创建 `.jw-agenda.json`（或 `jw-agenda.json`）：

```json
{
  "agendaRoot": "jw-agenda-data",
  "archiveAfterDays": 14
}
```

`archiveAfterDays` 控制旧 `daily/` 文件何时移入 `YYYYMM/` 子目录（默认 14；设为 `0` 或负数则禁用）。

然后打开工作区，说"生成本周计划"或"生成今天的计划"即可。

---

## 📁 数据布局与文件命名

Skill 安装在产品的 skill 目录里；你的**工作区只存数据**：

```
<workspace>/
├── .jw-agenda.json            ← 可选（自定义根目录/归档阈值）
└── jw-agenda-data/            ← jw-agenda 根目录（默认）
    ├── schedule-config.md     ← 可选
    ├── summary-categories.md  ← 可选
    ├── yearly/                ← 可选
    ├── monthly/               ← YYYY-MM-plan.md、YYYY-MM-review.md
    ├── weekly/                ← Week{N}-plan.md、Week{N}-review.md
    ├── daily/                 ← YYYY-MM-DD-todo.md、YYYY-MM-DD-log.md
    └── tasks/                 ← TODO.md、阅读清单等
```

| 📄 类型 | 📋 格式 | 📁 目录 | 💡 示例 |
|------|--------|-----|---------|
| 年计划（可选） | `YYYY-plan.md` | `yearly/` | `2026-plan.md` |
| 月计划 | `YYYY-MM-plan.md` | `monthly/` | `2026-02-plan.md` |
| 月总结 | `YYYY-MM-review.md` | `monthly/` | `2026-02-review.md` |
| 季度总结 | `YYYY-Q{N}-review.md` | `monthly/` | `2026-Q1-review.md` |
| 周计划 | `Week{N}-plan.md` | `weekly/` | `Week6-plan.md` |
| 周总结 | `Week{N}-review.md` | `weekly/` | `Week6-review.md` |
| 每日 Todo | `YYYY-MM-DD-todo.md` | `daily/` | `2026-02-06-todo.md` |
| 每日日志 | `YYYY-MM-DD-log.md` | `daily/` | `2026-02-06-log.md` |

N = ISO 周数（1–52）；如 2026-02-05 → Week 6。完整规则见 [`assets/conventions.md`](skills/jw-agenda-v2/assets/conventions.md)。

---

## ⚙️ 自定义

- **⏰ 作息**：编辑 jw-agenda 根目录下的 `schedule-config.md` 调整时间段/固定活动。
- **🗂️ 总结分类**：编辑 `summary-categories.md` 控制日/周/月总结的分组方式。
- **📋 约定**：命名、路径、标记、去重、级联规则都在 [`assets/`](skills/jw-agenda-v2/assets/)。用户通常无需改动；如需自定义，可编辑你已安装的 skill 副本。
- **📅 月计划格式**：自由格式；包含"本月目标"和 `Week N` 分节有助于周规划和月总结。

---

## 👥 开发

运行单元测试（46 个，覆盖 `date_utils.py` 和 `dedup_todos.py`）：

```bash
cd jw-agenda-v2/tests
python3 -m unittest -v
```

改进 backlog 见 [Todo.md](Todo.md)，版本历史见 [doc/CHANGELOG.md](doc/CHANGELOG.md)。欢迎贡献——见仓库 [CONTRIBUTING.zh-CN.md](../CONTRIBUTING.zh-CN.md)。

## 🔒 安全

漏洞报告方式见 [SECURITY.zh-CN.md](../SECURITY.zh-CN.md)。

---

## 许可

代码：Apache 2.0。文档：CC-BY-4.0。见 [LICENSE](../LICENSE) | [LICENSE-CODE](../LICENSE-CODE) | [LICENSE-DOCS](../LICENSE-DOCS)。
