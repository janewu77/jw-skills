# jw-Agenda

基于 [Agent Skills](https://agentskills.io/home) 的个人日程管理技能组。

用自然语言驱动「月规划 → 周拆解 → 日执行 → 日志记录 → 周回顾」的完整闭环，所有数据以 Markdown 文件存储在本地。

**语言**：本文档为中文版。英文版见 [README.md](README.md)。

**License**：本仓库整体采用「代码 Apache 2.0、文档 CC-BY-4.0」。许可见仓库根目录 [LICENSE](../LICENSE)，[LICENSE-CODE](../LICENSE-CODE)，[LICENSE-DOCS](../LICENSE-DOCS)。

---

## 功能概览

你只需要对话，Claude 会自动选择合适的 Skill 来执行：

| 你说… | Claude 做… |
|--------|-----------|
| 「生成本周计划」 | 读取月规划 + 上周未完成 → 按天拆解出周计划 |
| 「生成今天的计划」 | 读取周规划 + 昨天未完成 → 生成带时间表的今日 Todo |
| 「我完成了简历修改」 | daily-log 写日志并勾选今日 Todo 对应项 |
| 「把投递移到周三」 | 从今日移除 → 加入周三 → 同步周规划 |
| 「加一项：下周约导师」 | 写入下周的规划文件 |
| 「今天做了 XX，还有 YY 没做完，感觉有点累」 | 解析口语化汇报 → 生成日志 → 同步勾选 |
| 「总结昨天」 | 读取昨天 Todo → 生成日志 → 未完成转移到今天 |
| 「同步规划」 | 检查日/周/月三层一致性 → 列出偏差 → 确认后修正 |
| 「周总结」 | 汇总本周日志 → 统计完成率和时间分配 → 生成周报 |

---

## 工作流程

```
┌─────────────┐
│  月规划       │  ← 用户手动维护（本月目标、每周重点）
│ YYYY-MM-plan │
└──────┬──────┘
       │ weekly-plan 读取本周目标
       ▼
┌─────────────┐     ┌─────────────┐
│  周规划       │────→│  周总结       │
│ Week{N}-plan │     │ Week{N}-review  │
└──────┬──────┘     └──────▲──────┘
       │ daily-todo          │ weekly-review
       │ 读取当日任务          │ 汇总本周日志
       ▼                     │
┌─────────────┐     ┌─────────────┐
│  日 Todo      │────→│  日志         │
│ 日期-todo.md  │     │  日期-log.md  │
└─────────────┘     └─────────────┘
  daily-todo          daily-log
  (计划与执行)          (记录与留痕)

        ↕ planning-sync（检查三层一致性）
```

**一天的节奏**：早上「生成今天的计划」→ 白天「我完成了 X」→ 晚上「今天做了…感觉…」

**一周的节奏**：周一「生成本周计划」→ 周中「同步规划」→ 周末「周总结」

---

## Skill 目录

本技能组包含 5 个 Skill，**每个可独立安装**。安装多个时它们会自动配合，但彼此不依赖——缺少任何一个，其余仍可正常工作。

### jw-agenda-daily-todo — 每日 Todo 管理

管理今日 todo 的计划与调整：生成计划、调整日程、临时加项。**不负责标记完成**（「我完成了 X」由 daily-log 处理）。

**功能**：从月/周规划和昨天未完成自动生成带时间表的今日 Todo；取消/推迟事项、将事项移到其他日期并同步规划文件；临时追加事项到当天/本周/本月/以后。可查询当日进度（还剩哪些、完成得怎么样）。

**触发词**：「生成今天的计划」「把 X 移到周三」「加一项」「明天要」「以后要」「Y 不做了」「今天完成得怎么样」

**配合**：若安装了 daily-log，会识别其写入的「从昨天转移」项避免重复。若安装了 weekly-plan，会读取周规划作为当日计划来源。

### jw-agenda-daily-log — 日志与汇报

将口语化的进度汇报整理成结构化日志，保留想法和碎碎念。

**功能**：总结昨天的工作生成日志；接受今天的口语化汇报（可以很随意、带想法）解析后生成日志；未完成事项自动转移到今日 Todo。

**触发词**：「总结昨天」「汇报今天」「记录一下今天」「今天大概做了…」「我完成了 X」「作业做完了」

**配合**：若安装了 daily-todo，汇报今天时会顺带更新今日 Todo 的勾选。

### jw-agenda-weekly-plan — 周规划生成

从月规划拆解出按天的周计划。

**功能**：读取月规划中本周的目标和重点；合并上周未完成的延续任务；按天分配生成周规划文件。

**触发词**：「生成本周计划」「周规划」「weekly plan」

**配合**：若安装了 weekly-review，会读取上周总结中的「转入下周」作为延续任务来源。

### jw-agenda-weekly-review — 周回顾

汇总一周的日志和 Todo，生成统计报告。

**功能**：汇总本周所有日志；统计完成率（按优先级分类）和时间分配；识别并列出需要转入下周的事项。

**触发词**：「周总结」「本周回顾」「weekly review」

**配合**：若安装了 weekly-plan，会对比周规划 vs 实际执行。产出的「转入下周」列表可供 weekly-plan 下周读取。

### jw-agenda-planning-sync — 规划同步检查

事后一致性检查，确保日/周/月三层规划不矛盾。

**功能**：对比日 Todo、周规划、月规划的任务内容和完成状态；将偏差分为「需行动」和「信息性」两级；展示建议清单，仅在用户确认后才执行修改。

**触发词**：「同步规划」「检查一致性」「planning sync」

**配合**：检查范围取决于已安装的 Skill 产出了哪些文件。即使只安装了 daily-todo 和 weekly-plan，也能进行日-周两层对比。

---

## 安装

在 **Cursor** 上安装时，可参考官方文档：[Agent Skills（含安装方式与 Skill 目录说明）](https://cursor.com/docs/context/skills)。

### 前提条件

- 支持 Skill 的 AI 工作环境（如 Cursor、Claude Desktop 等）
- 一个用于存放日程数据的文件夹（下文称 workspace）。**请打开你的 workspace 根目录**；jw-agenda 数据默认在用户工作目录下的 `jw-agenda-data/`，也可通过 `.jw-agenda.json` 或 `jw-agenda.json` 配置其他路径（见下方「配置 jw-agenda 根目录」）。

### 产品目录结构

```
jw-agenda/
├── README.md                          ← 本文件
├── CONTRIBUTING.md                     ← 维护者：修改 _common 后需执行 sync 脚本
│
├── _common/                           ← 约定与脚本唯一来源（维护用，不发给用户）
│   ├── conventions.md
│   ├── schedule-config.example.md
│   └── scripts/
│       ├── date_utils.py
│       ├── dedup_todos.py
│       └── LICENSE
├── scripts/
│   └── sync-common-to-skills.sh        ← 将 _common 同步到各 skill 的 assets/
│
└── skills/                            ← 5 个可独立安装的 Skill（安装即用）
    ├── jw-agenda-daily-todo/
    │   ├── SKILL.md
    │   ├── assets/
    │   │   ├── conventions.md         ← 从 _common 同步
    │   │   ├── schedule-config.example.md
    │   │   ├── todo-template.md
    │   │   └── scripts/
    │   └── references/
    ├── jw-agenda-daily-log/
    │   ├── SKILL.md
    │   └── assets/
    │       ├── conventions.md
    │       ├── schedule-config.example.md
    │       ├── log-template.md
    │       └── scripts/
    ├── jw-agenda-weekly-plan/
    │   └── assets/（同上含 conventions、schedule-config.example、scripts）
    ├── jw-agenda-weekly-review/
    │   └── assets/（同上）
    └── jw-agenda-planning-sync/
        └── assets/（同上）
```

### 安装后的用户 Workspace 结构

Skill 按各产品标准安装在对应目录，**不会**出现在用户选择的 workspace 里。用户 workspace 中只有**数据目录**与**可选的作息配置**，无需再复制约定或脚本。默认结构如下（若配置了 `agendaRoot`，则下述结构位于你配置的路径下）：

```
<workspace>/
└── jw-agenda-data/                    ← jw-agenda 根目录（默认用户数据目录）
    ├── schedule-config.md             ← 可选；仅当要自定义作息时创建（可从任一 Skill 的 assets/schedule-config.example.md 复制后修改）
    ├── monthly/                       ← 用户手动维护
    │   └── YYYY-MM-plan.md
    ├── weekly/                        ← 由 Skill 生成
    ├── daily/                         ← 由 Skill 生成
    └── tasks/                         ← 可选
```

### 安装步骤

#### 全量安装（推荐）

**第 1 步：创建用户数据目录**

默认使用用户工作目录下的 **`jw-agenda-data`** 作为 jw-agenda 根目录（存放用户数据）：

```bash
cd <workspace>
mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}
```

**（可选）配置 jw-agenda 根目录**：在 workspace 根目录创建 `.jw-agenda.json` 或 `jw-agenda.json`，内容为 `{"agendaRoot":"你的/路径"}`，可指定其他目录（如 `docs/agenda`、`notes/plans`）；然后在该路径下创建 `monthly`、`weekly`、`daily`、`tasks` 子目录。不创建该配置文件时，默认使用 `jw-agenda-data`。

（若目录不存在，Skill 首次写入时也可按需创建或提示。）

**第 2 步（可选）：自定义作息**

若需要自定义每日时段，从本仓库任一 skill 的 `assets/schedule-config.example.md` 复制到 **jw-agenda 根目录**下并重命名为 `schedule-config.md`（默认即 `jw-agenda-data/`）：

```bash
cp <path-to-any-skill>/assets/schedule-config.example.md jw-agenda-data/schedule-config.md
```

然后编辑该文件修改时间表。**不创建该文件时**，daily-todo 会使用 Skill 内嵌的默认模板。

**第 3 步：安装 Skill**

- **用 zip 安装（推荐，Cursor 等）**：本仓库提供 5 个独立 zip（运行 `./package-skills.sh` 在 `output/` 下生成）。将**每个 zip 解压到 Cursor 的 skills 目录**（用户级：`~/.cursor/skills/`；项目级：`.cursor/skills/`）即可，约定与脚本已内嵌在 zip 内，**无需再复制任何文件到用户目录**。目录与从 GitHub 安装方式见 [Cursor 官方：Agent Skills](https://cursor.com/docs/context/skills)。
  ```bash
  unzip jw-agenda-daily-log.zip -d ~/.cursor/skills/
  unzip jw-agenda-daily-todo.zip -d ~/.cursor/skills/
  # 其余 3 个 skill 同理
  ```
- **从源码安装**：将本仓库 `jw-agenda/skills/` 下需要的 skill 目录复制到产品规定的技能目录（如 `~/.cursor/skills/`），具体见 [Cursor 官方文档](https://cursor.com/docs/context/skills) 或各产品文档。

**第 4 步：创建月规划（推荐）**

在 jw-agenda 根目录下的 `monthly/`（默认即 `jw-agenda-data/monthly/`）创建当月规划，文件名为 `YYYY-MM-plan.md`（如 `2026-02-plan.md`）。格式自由，建议按周组织：

```markdown
# 2月完整规划

## 本月目标
- 完成求职投递 30 家
- 每天英语口语 30 分钟

## Week 1 (2.1-2.7)
- 重点：修改简历、投递第一批

## Week 2 (2.8-2.14)
- 重点：…
```

**第 5 步：在所用产品中选择/打开你的 workspace 根目录**（jw-agenda 数据默认在 `jw-agenda-data/`，或你配置的路径），开始使用。

#### 单独安装某个 Skill

只想安装其中一个？也可以。每个 Skill 的约定与脚本已随包安装，**只需**在 workspace 下具备 **jw-agenda 根目录**（默认 `jw-agenda-data`，可经 workspace 根目录的 `.jw-agenda.json` 或 `jw-agenda.json` 配置）及子目录 monthly、weekly、daily、tasks；可选 jw-agenda 根目录下的 `schedule-config.md`。

1. 创建数据目录：`mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}`（若使用默认路径且尚未创建）；若使用自定义路径，先配置 `.jw-agenda.json` 或 `jw-agenda.json` 再创建对应子目录。
2. 按该产品的标准方式，只安装你需要的 skill 目录；Cursor 见 [官方：Agent Skills](https://cursor.com/docs/context/skills)，其他产品见各自文档。
3. 缺少其他 Skill 时，该 Skill 会跳过相关数据源并正常工作。

---

## 示例

### 快速开始：使用示例工作区

我们提供两个版本的示例工作区（英文和中文）。复制一个即可开始：

**英文版：**
```bash
cp -r jw-agenda/examples/sample-workspace jw-agenda-data
```

**中文版：**
```bash
cp -r jw-agenda/examples/sample-workspace-zh jw-agenda-data
```

每个版本都包含示例文件：
- 月规划 (`monthly/2026-02-plan.md`)
- 周规划 (`weekly/Week6-plan.md`)
- 日待办 (`daily/2026-02-05-todo.md`)
- 日日志 (`daily/2026-02-05-log.md`)
- 周总结 (`weekly/Week6-review.md`)

详见 [examples/README.md](examples/README.md)。

### 对话示例

- **英文**：参见 [examples/conversations.md](examples/conversations.md) 了解完整示例，包括：
  - 如何生成周规划
  - 如何汇报日常进度
  - 如何添加临时任务
  - 如何生成周总结
  - 如何同步规划以保持一致性

- **中文**：参见 [examples/conversations.zh-CN.md](examples/conversations.zh-CN.md) 了解完整示例

---

## 触发词速查

| 想做什么 | 说什么 |
|----------|--------|
| 生成本周规划 | 「生成本周计划」/「周规划」/「weekly plan」 |
| 生成今日 Todo | 「生成今天的计划」/「today plan」 |
| 汇报进度写日志 | 「今天做了 XXX，还有 YYY 没做完，感觉…」 |
| 总结昨天 | 「总结昨天」/「整理昨天的日志」 |
| 标记完成（写日志+勾选） | 「我完成了 XXX」/「作业做完了」/「记录一下今天」 |
| 调整日程 | 「把 XXX 移到周三」/「推迟到下周」 |
| 临时加项 | 「加一项 XXX」/「明天要 YYY」/「以后要 ZZZ」 |
| 检查一致性 | 「同步规划」/「检查一致性」/「planning sync」 |
| 周总结 | 「周总结」/「本周回顾」/「weekly review」 |

---

## 文件命名规则

| 类型 | 格式 | 目录 | 示例 |
|------|------|------|------|
| 月规划 | `YYYY-MM-plan.md` | `monthly/` | `2026-02-plan.md` |
| 周规划 | `Week{N}-plan.md` | `weekly/` | `Week1-plan.md` |
| 周总结 | `Week{N}-review.md` | `weekly/` | `Week1-review.md` |
| 日 Todo | `YYYY-MM-DD-todo.md` | `daily/` | `2026-02-06-todo.md` |
| 日志 | `YYYY-MM-DD-log.md` | `daily/` | `2026-02-06-log.md` |

N = 年内周号（ISO 周，1–52）。例如 2026-02-05 所在周 → Week 6。

完整规则见各 Skill 的 `assets/conventions.md`（或本仓库 `_common/conventions.md`）。

---

## 自定义

**作息时段**：若你在 jw-agenda 根目录（默认 `jw-agenda-data`）下创建了 `schedule-config.md`，编辑该文件即可增删时间段、调整固定活动（如出门、晚餐时间）。daily-todo 生成今日时间表时优先按该文件的「时段定义」表；不存在则使用 Skill 内嵌的默认模板。

**约定规则**：命名、路径、标记、优先级等定义在各 Skill 的 `assets/conventions.md` 中。用户一般无需修改；若需自定义，可编辑本地已安装 Skill 目录下的该文件，或修改本仓库 `_common/conventions.md` 后重新打包安装。

**月规划格式**：完全自由。建议包含「本月目标」和按 `Week N` 分的小节，便于 weekly-plan 提取。

**脚本**：各 Skill 的 `assets/scripts/date_utils.py`、`dedup_todos.py` 已随 Skill 安装，供日期计算与 todo 去重使用。

---

## 分发给他人使用

本仓库提供 **5 个独立的 zip**（每个 Skill 一个），用于分发给他人安装。

**如何生成 zip**：在 **jw-agenda 目录下**执行：

```bash
cd jw-agenda
./package-skills.sh
```

脚本会把 `skills/` 下每个 skill 打成一个 zip，输出到 `jw-agenda/output/`。**何时执行**：需要把技能组以 zip 形式分发或发布时（例如发布新版本、发给未克隆仓库的用户）执行一次即可。生成后，分发给他人时提供这 5 个 zip 即可。使用者将**每个 zip 解压到 Cursor 的 skills 目录**，并在 workspace 下创建 **jw-agenda 根目录**（默认 `jw-agenda-data`，可经 `.jw-agenda.json` 或 `jw-agenda.json` 配置，见上方「配置 jw-agenda 根目录」）及子目录（monthly、weekly、daily、tasks）；**无需再复制约定或脚本**，zip 内已包含。若需自定义作息，可选：从任一 zip 解压后的 skill 的 `assets/schedule-config.example.md` 复制到 jw-agenda 根目录下并重命名为 `schedule-config.md` 后修改。

---

## 开发

改进计划与已知问题见 [TODO.md](TODO.md)。

## License

本仓库整体许可：代码 Apache 2.0，文档 CC-BY-4.0。许可见仓库根目录 [LICENSE](../LICENSE) | [LICENSE-CODE](../LICENSE-CODE) | [LICENSE-DOCS](../LICENSE-DOCS)。
