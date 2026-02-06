# jw-Agenda

基于 Claude Cowork 的个人日程管理技能组。

用自然语言驱动「月规划 → 周拆解 → 日执行 → 日志记录 → 周回顾」的完整闭环，所有数据以 Markdown 文件存储在本地。

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
│ todo-日期.md  │     │  日期.md      │
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

### 前提条件

- 支持 Skill 的 AI 工作环境（如 Cursor、Claude Desktop 等）
- 一个用于存放日程数据的文件夹（下文称 workspace）。**请确保在 Cursor/Claude 中打开的 workspace 根目录即为包含 `personal/agenda/` 的目录**，否则 Skill 无法找到约定路径。

### 产品目录结构

```
jw-agenda/
├── README.md                          ← 本文件
├── LICENSE                            ← 许可见仓库根目录 ../LICENSE
│
├── shared/                            ← 共享基础设施
│   ├── conventions.md                 ← 核心约定文件（安装到用户数据目录）
│   ├── schedule-config.example.md     ← 作息时段配置模板
│   └── scripts/
│       ├── date_utils.py              ← 日期/周数计算
│       └── dedup_todos.py             ← Todo 去重
│
└── skills/                            ← 5 个可独立安装的 Skill
    ├── jw-agenda-daily-todo/
    │   ├── SKILL.md
    │   ├── assets/todo-template.md
    │   └── references/
    │       ├── mode-c-reschedule.md
    │       └── mode-d-adhoc.md
    ├── jw-agenda-daily-log/
    │   ├── SKILL.md
    │   └── assets/log-template.md
    ├── jw-agenda-weekly-plan/
    │   ├── SKILL.md
    │   └── assets/week-template.md
    ├── jw-agenda-weekly-review/
    │   ├── SKILL.md
    │   └── assets/review-template.md
    └── jw-agenda-planning-sync/
        ├── SKILL.md
        └── assets/sync-report-template.md
```

### 安装后的用户 Workspace 结构

Skill 按各产品标准安装在对应目录，**不会**出现在用户选择的 workspace 里。用户 workspace 中只有**数据目录**，结构如下：

```
<workspace>/
└── personal/
    └── agenda/
        ├── shared/
        │   ├── conventions.md           ← 从 jw-agenda/shared/ 复制
        │   ├── schedule-config.md       ← 从 .example.md 复制并修改
        │   └── scripts/                 ← 从 jw-agenda/shared/scripts/ 复制
        │       ├── date_utils.py
        │       └── dedup_todos.py
        │
        ├── monthly/                     ← 用户手动维护
        │   └── YYYY-MM-plan.md
        ├── weekly/                      ← 由 Skill 生成
        ├── daily/                       ← 由 Skill 生成
        └── tasks/                       ← 可选
```

### 安装步骤

#### 全量安装（推荐）

**第 1 步：创建用户数据目录**

```bash
cd <workspace>
mkdir -p personal/agenda/{shared/scripts,monthly,weekly,daily,tasks}
```

**第 2 步：安装共享基础**

```bash
cp jw-agenda/shared/conventions.md        personal/agenda/shared/
cp jw-agenda/shared/schedule-config.example.md  personal/agenda/shared/schedule-config.md
cp jw-agenda/shared/scripts/*.py          personal/agenda/shared/scripts/
```

然后打开 `personal/agenda/shared/schedule-config.md`，**根据自己的作息修改时间表**。

**第 3 步：安装 Skill**

- **用 zip 安装（推荐，Cursor 等）**：若你拿到的是 5 个独立 zip（如 `jw-agenda-daily-log.zip`、`jw-agenda-daily-todo.zip` 等，可由本仓库运行 `./package-skills.sh` 在 `output/` 下生成），将**每个 zip 解压到 Cursor 的 skills 目录**，例如：
  ```bash
  # Cursor 用户级，对每个 zip 执行一次
  unzip jw-agenda-daily-log.zip -d ~/.cursor/skills/
  unzip jw-agenda-daily-todo.zip -d ~/.cursor/skills/
  # 其余 3 个 skill 同理
  ```
  解压后 5 个 skill 目录会出现在 `~/.cursor/skills/` 下。
- **从源码安装**：将本仓库 `jw-agenda/skills/` 下需要的 skill 目录复制到产品规定的技能目录（如 `~/.cursor/skills/`），具体见各产品文档。

**第 4 步：创建月规划（推荐）**

在 `personal/agenda/monthly/` 下创建当月规划，文件名为 `YYYY-MM-plan.md`（如 `2026-02-plan.md`）。格式自由，建议按周组织：

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

**第 5 步：在所用产品中选择/打开你的 workspace 文件夹（即包含 `personal/agenda/` 的根目录），开始使用。**

#### 单独安装某个 Skill

只想安装其中一个？也可以。**每个 Skill 都依赖 `personal/agenda/shared/` 下的 conventions、schedule-config 和 scripts，必须先完成第 1、2 步。**

1. **必须先完成上面的第 1、2 步**（创建目录 + 安装共享基础）。
2. 按该产品的标准方式，只安装你需要的 skill 目录（如 `jw-agenda/skills/jw-agenda-daily-todo`），具体步骤见 Cursor / Claude 等各产品文档。
3. 缺少其他 Skill 时，该 Skill 会跳过相关数据源并正常工作。

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
| 日 Todo | `todo-YYYY-MM-DD.md` | `daily/` | `todo-2026-02-06.md` |
| 日志 | `YYYY-MM-DD.md` | `daily/` | `2026-02-06.md` |

N = 月内周号，`ceil(day / 7)`。例如 2 月 5 日 → Week 1。

完整规则见 `shared/conventions.md`。

---

## 自定义

**作息时段**：编辑 `personal/agenda/shared/schedule-config.md`，增删时间段、调整固定活动（如出门、晚餐时间）。daily-todo 生成今日时间表时按该文件的「时段定义」表逐行生成，固定活动（如出门、晚餐）不会覆盖，仅「（填入当日任务）」的时段会填入具体事项。

**约定规则**：`personal/agenda/shared/conventions.md` 定义了命名、路径、标记、优先级等所有约定。如需修改（如改变优先级 emoji），直接编辑即可。

**月规划格式**：完全自由。建议包含「本月目标」和按 `Week N` 分的小节，便于 weekly-plan 提取。

**共享脚本**：`shared/scripts/date_utils.py` 用于日期与月内周数计算，各 Skill 推荐使用以保持一致。`dedup_todos.py` 供合并 todo 时去重（如 daily-todo 模式 A 幂等合并）；可选，Skill 也可在逻辑内自行去重。

---

## 分发给他人使用

本仓库提供 **5 个独立的 zip**（每个 Skill 一个），由 `package-skills.sh` 在 `jw-agenda/output/` 下生成。分发给他人时，提供这 5 个 zip 即可；使用者将**每个 zip 解压到 Cursor 的 skills 目录**，例如：

```bash
# 解压单个 skill（对每个 zip 执行一次）
unzip jw-agenda-daily-log.zip -d ~/.cursor/skills/
unzip jw-agenda-daily-todo.zip -d ~/.cursor/skills/
# … 其余 3 个同理
```

**注意**：zip 内只含对应一个 Skill，不含 `shared/`。使用者仍需完成「安装步骤」第 1、2 步（在 workspace 创建 `personal/agenda/shared/` 并从本仓库复制 conventions、schedule-config、scripts）；可从 GitHub 克隆本仓库或下载仓库 zip 获取 `shared/` 内容。

---

## 版本与维护

命名与路径以 `shared/conventions.md` 为准：月规划 `YYYY-MM-plan.md`，周规划 `Week{N}-plan.md`，周总结 `Week{N}-review.md`。若某 Skill 内路径描述与 conventions 不一致，以 conventions 为准。

**Skill 版本**：各 Skill 的 SKILL.md 中含 `author: Jing Wu`、`version`、`updated`。版本号格式 `0.M.P`：单 skill 更新时第三位 +0.0.1（如 0.0.1→0.0.2）；**配合版本升级**时，所有 skill 的第二位（0.X）对齐升级（如统一升为 0.1.0），便于整组协同发布。

**常见问题**：周规划/周总结找不到？请确认文件名为 `Week{N}-plan.md`、`Week{N}-review.md`（如 Week1-plan.md），不要使用旧版「最终版」「总结」等命名。

---

## License

本仓库整体许可：代码 Apache 2.0，文档 CC-BY-4.0。许可见仓库根目录 [LICENSE](../LICENSE) | [LICENSE-CODE](../LICENSE-CODE) | [LICENSE-DOCS](../LICENSE-DOCS)。
