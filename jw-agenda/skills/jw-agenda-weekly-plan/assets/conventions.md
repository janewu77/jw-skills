# 约定（所有 Skill 统一引用）

## 路径查找

本约定位于**本 Skill 的 `assets/conventions.md`**。所有 Skill 在运行前应读取此文件（相对于本 Skill 的安装目录），以获取下方约定。用户工作区中仅存放**数据**与**可选的用户作息配置**，见「jw-agenda 根目录」与「目录路径」、「文件命名规则」。

## jw-agenda 根目录（可配置）

所有日程数据均在「jw-agenda 根目录」下（即用户数据根目录）。**jw-agenda** 为本技能组名称；默认在用户工作目录（workspace）下使用 **`jw-agenda-data`** 存放用户数据。该根目录**优先**从 workspace 根目录的 `.jw-agenda.json`（或 `jw-agenda.json`）中的 `agendaRoot` 读取；若文件不存在或未设置 `agendaRoot`，则使用默认 `jw-agenda-data`。

**约定**：Agent 在执行任何读写前，先确定 workspace 根，再读取该配置得到 jw-agenda 根目录（缺省 `jw-agenda-data`），后续所有路径均为「jw-agenda 根目录」下的相对路径。路径建议使用正斜杠、相对 workspace 根；解析时可做规范化（如去除末尾 `/`、避免 `..`）。

## 目录路径（用户工作区）

`{agendaRoot}` 由上述配置或默认值得到。日程计划与完成情况统一放在 workspace 的 `{agendaRoot}` 目录下，按时间粒度分子目录：

| 用途 | 路径 |
|------|------|
| 月规划、月总结 | `{agendaRoot}/monthly/` |
| 周规划、周总结 | `{agendaRoot}/weekly/` |
| 日 Todo、日日志 | `{agendaRoot}/daily/` |
| 其他任务与清单（含阅读清单、采购清单等） | `{agendaRoot}/tasks/` |

**daily 目录归档规则**：当日及近期（约 2 周内）的 todo、log 放在 `daily/` 根下。**二周以前**的文件移入按年月命名的子目录（如 `202601/`、`202602/`，格式 `YYYYMM`）。之后如需归档某月文件，在 `daily/` 下新建对应 `YYYYMM/` 子目录，并将超过两周的该月文件移入其中。
| 用户作息配置（可选） | 单文件 `{agendaRoot}/schedule-config.md`，见下方文件命名。 |

## 文件命名规则

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| 月规划 | `YYYY-MM-plan.md`（如 `2026-02-plan.md`，2 月即 2026-02） | `2026-02-plan.md` |
| 周规划 | `Week{N}-plan.md`（N = 年内周号，1–52） | `Week6-plan.md` |
| 日 Todo | `YYYY-MM-DD-todo.md` | `2026-02-05-todo.md` |
| 日志 | `YYYY-MM-DD-log.md` | `2026-02-05-log.md` |
| 周总结 | `Week{N}-review.md`（N = 年内周号，与周规划一致） | `Week6-review.md` |
| 阅读清单 | `todo-readinglist.md` | `{agendaRoot}/tasks/todo-readinglist.md` |
| 未定日期 / 待办池 | `TODO.md` | `{agendaRoot}/tasks/TODO.md` |
| 作息时间配置（可选） | `schedule-config.md` | `{agendaRoot}/schedule-config.md`（若不存在，daily-todo 使用本 Skill 的 `assets/schedule-config.example.md`） |

上述示例中的路径均相对于 jw-agenda 根目录；默认 `agendaRoot` 为 `jw-agenda-data`，实际以当前解析到的配置为准。

**tasks 目录下以 `todo` 开头的文件**（如 `TODO.md`、`todo-readinglist.md`、`todo-xxx.md`）均视为待办/清单。生成周规划或日计划时，应将上述文件中的未勾选项作为可选来源纳入考虑。

**日志中的「今日想法/随口记」**：用户口语化汇报进度时，想法、感受、碎碎念记入该区块，原意保留，便于日后回顾。

## 周数计算规则

**周起止**：周一至周日。

**周数**：该周在**当年**内的第几周（ISO 周），通常一年 52 周，少数年份有 53 周。使用 Python `date.isocalendar()` 的 `iso_week`（1–52 或 53）。

**计算示例**：2026-02-05（周四）所在周为 2026 年第 6 周 → 周规划 `Week6-plan.md`，周总结 `Week6-review.md`。

**推荐**：使用**本 Skill 的** `assets/scripts/date_utils.py` 计算日期和周数，避免手算错误。`assets/scripts/dedup_todos.py` 供合并 todo 时去重（如 daily-todo 模式 A 幂等合并）；可选，Skill 也可在逻辑内自行去重。**调用 dedup_todos.py 时仅传入 jw-agenda 根目录下的路径**（即已按用户配置解析后的路径），脚本会校验路径位于 workspace 内，避免路径遍历。

## 临时追加的归属

用户临时想到要加一项时，按时间范围写入对应文件，并**始终向用户汇报写入了哪些文件**：

| 时间范围 | 写入文件 |
|----------|----------|
| **无法确定日期** / **不是当月会做的事** | `{agendaRoot}/tasks/TODO.md` |
| 今天 / 明天 / 本周某天 | `{agendaRoot}/daily/YYYY-MM-DD-todo.md` , `{agendaRoot}/weekly/Week{W}-plan.md`,  `{agendaRoot}/monthly/YYYY-MM-plan.md` |
| 本周（无具体日） / 下周 / 某周 | `{agendaRoot}/weekly/Week{W}-plan.md`,  `{agendaRoot}/monthly/YYYY-MM-plan.md` |
| 本月 / 以后（更远） | `{agendaRoot}/monthly/YYYY-MM-plan.md` |

详见 jw-agenda-daily-todo 的「添加/移动任务」模式（`references/mode-add-or-move.md`）。

## 来源标记

| 来源 | 标记格式 |
|------|---------|
| 昨天未完成 | `*(从昨天转移)*` |
| 月/周规划 | `*(来自规划)*` |
| 昨天未完成 + 也在规划中 | `*(从昨天转移)*` |
| 从其他日期移入 | `*(从 M.D 移入)*` |
| 来自阅读清单 | `*(来自阅读清单)*` |
| 来自 tasks 清单（含上述及其他 todo 开头文件） | `*(来自 tasks 清单)*` |
| 临时追加（通过 daily-todo 添加/移动任务模式添加） | `*(临时追加)*` |

## 状态标记（daily-todo 更新状态时使用）

| 状态 | 在 todo 条目上的写法 |
|------|----------------------|
| 已完成 | `- [x] 事项内容` |
| 进行中 | `- [ ] 事项内容（进行中）` |
| 取消 | `- [x] 事项内容（取消）` |
| 推迟（无目标日） | `- [ ] 事项内容（推迟）` 或备注中说明 |
| 推迟（有目标日） | 移至目标日，并标记 `*(从 M.D 移入)*` |

## 优先级标识

| 级别 | 标题格式 |
|------|---------|
| 高（今天必须完成） | `## 🔴 高优先级` |
| 中 | `## 🟡 中优先级` |
| 低（可选） | `## 🟢 低优先级` |

## Planning Sync 建议时机

`jw-agenda-planning-sync` 是事后一致性检查工具，建议在以下时机运行：每周中期（如周三）检查本周执行与规划的偏差；每周末生成周总结前运行一次，确保数据干净；大量调整日程后（如连续使用 daily-todo 添加/移动任务模式）运行一次。

## 冲突裁决策略（多数据源不一致时）

当日 todo / 日日志与周规划、月规划对同一任务的描述或状态不一致时，按以下优先级裁决（用于 planning-sync 及日常同步）：

| 优先级 | 数据源 | 说明 |
|--------|--------|------|
| 1（最高） | 日 todo / 日日志 | 以**当日执行记录**为准。例如：日 todo 已勾选完成，则周规划中对应项应同步为已完成；日日志记录「未完成」或「取消」，则周规划中对应项以日为准。 |
| 2 | 周规划 | 日层级未记录时，以周规划为准；周与月冲突时，以周为准（周更贴近执行）。 |
| 3 | 月规划 | 仅当周、日均无记录时，以月规划为准。 |

原则：**谁更贴近「已发生的事实」谁优先**。日执行是事实记录，周/月是计划层，同步时由日→周→月向上同步状态与变更。

## 错误处理默认策略

| 情况 | 处理方式 |
|------|---------|
| 文件不存在 | 跳过该来源，继续用已有数据，向用户说明缺少哪个文件 |
| 格式不符预期 | 尽力解析，无法解析时向用户展示文件内容并请求确认 |
| 所有来源都缺失 | 生成最小框架（仅标题和空白区块），标注"无数据来源，请手动补充" |
| 文件已存在（幂等性） | 先读取现有内容，仅追加不重复的新条目，保留用户已有的勾选和备注 |
| 日期歧义（如"下周"） | 推算具体日期后向用户确认 |
