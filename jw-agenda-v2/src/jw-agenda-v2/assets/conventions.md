# 约定（所有 Skill 统一引用）

## 路径查找

本约定位于**本 Skill 的 `assets/conventions.md`**。所有 Skill 在运行前应读取此文件（相对于本 Skill 的安装目录），以获取下方约定。用户工作区中仅存放**数据**与**可选的用户配置**（作息配置、总结分类配置），见「jw-agenda 根目录」与「目录路径」、「文件命名规则」。

## jw-agenda 根目录（可配置）

所有日程数据均在「jw-agenda 根目录」下（即用户数据根目录）。**jw-agenda** 为本技能组名称；默认在用户工作目录（workspace）下使用 **`jw-agenda-data`** 存放用户数据。该根目录**优先**从 workspace 根目录的 `.jw-agenda.json`（或 `jw-agenda.json`）中的 `agendaRoot` 读取；若文件不存在或未设置 `agendaRoot`，则使用默认 `jw-agenda-data`。

**约定**：Agent 在执行任何读写前，先确定 workspace 根，再读取该配置得到 jw-agenda 根目录（缺省 `jw-agenda-data`），后续所有路径均为「jw-agenda 根目录」下的相对路径。路径建议使用正斜杠、相对 workspace 根；解析时可做规范化（如去除末尾 `/`、避免 `..`）。

## 目录路径（用户工作区）

`{agendaRoot}` 由上述配置或默认值得到。日程计划与完成情况统一放在 workspace 的 `{agendaRoot}` 目录下，按时间粒度分子目录：

| 用途 | 路径 |
|------|------|
| 年规划（可选） | `{agendaRoot}/yearly/` |
| 月规划、月总结 | `{agendaRoot}/monthly/` |
| 周规划、周总结 | `{agendaRoot}/weekly/` |
| 日 Todo、日日志 | `{agendaRoot}/daily/` |
| 其他任务与清单（含阅读清单、采购清单等） | `{agendaRoot}/tasks/` |
| 用户作息配置（可选） | `{agendaRoot}/schedule-config.md` |
| 总结分类配置（可选） | `{agendaRoot}/summary-categories.md` |

**daily 目录归档规则**：当日及近期的 todo、log 放在 `daily/` 根下。超过归档阈值的文件移入按年月命名的子目录（如 `202601/`、`202602/`，格式 `YYYYMM`）。

**归档阈值配置**：默认 14 天（2 周）。可在 `.jw-agenda.json` 中通过 `archiveAfterDays` 字段自定义：

```json
{
  "agendaRoot": "jw-agenda-data",
  "archiveAfterDays": 14
}
```

设为 `0` 或负数则禁用自动归档。

## 文件命名规则

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| 年规划（可选） | `YYYY-plan.md` | `2026-plan.md` |
| 月规划 | `YYYY-MM-plan.md`（如 `2026-02-plan.md`，2 月即 2026-02） | `2026-02-plan.md` |
| 周规划 | `Week{N}-plan.md`（N = 年内周号，1–52） | `Week6-plan.md` |
| 日 Todo | `YYYY-MM-DD-todo.md` | `2026-02-05-todo.md` |
| 日志 | `YYYY-MM-DD-log.md` | `2026-02-05-log.md` |
| 周总结 | `Week{N}-review.md`（N = 年内周号，与周规划一致） | `Week6-review.md` |
| 月总结 | `YYYY-MM-review.md` | `2026-02-review.md` |
| 阅读清单 | `todo-readinglist.md` | `{agendaRoot}/tasks/todo-readinglist.md` |
| 未定日期 / 待办池 | `TODO.md` | `{agendaRoot}/tasks/TODO.md` |
| 作息时间配置（可选） | `schedule-config.md` | `{agendaRoot}/schedule-config.md`（若不存在，daily-todo 使用本 Skill 的 `assets/schedule-config.example.md`） |
| 总结分类配置（可选） | `summary-categories.md` | `{agendaRoot}/summary-categories.md`（若不存在，使用本 Skill 的 `assets/summary-categories.example.md`） |

上述示例中的路径均相对于 jw-agenda 根目录；默认 `agendaRoot` 为 `jw-agenda-data`，实际以当前解析到的配置为准。

**tasks 目录下以 `todo` 开头的文件**（如 `TODO.md`、`todo-readinglist.md`、`todo-xxx.md`）均视为待办/清单。生成周规划或日计划时，应将上述文件中的未勾选项作为可选来源纳入考虑。

**日志中的「今日想法/随口记」**：用户口语化汇报进度时，想法、感受、碎碎念记入该区块，原意保留，便于日后回顾。

## 总结分类配置

daily-log 和 weekly-review 的「学习/产出」模块按**可配置的分类维度**进行总结。

**配置来源**：优先读取 `{agendaRoot}/summary-categories.md`；若不存在，使用本 Skill 的 `assets/summary-categories.example.md`。

**配置格式**：`## Categories / 分类列表` 下以 `- ` 开头的每行即为一个分类。Agent 在生成日志或周总结时，从该文件解析分类列表，在「学习/产出」区块下按顺序为每个分类生成子段落（`- **分类名**：内容`）。

**空分类处理**：当天/当周若某分类无相关内容，该分类行显示「无」或直接省略，由 Agent 根据数据丰富度决定——若大部分分类有内容则保留「无」以保持结构一致，若仅少数分类有内容则省略空分类以减少噪音。

## 周数计算规则

**周起止**：周一至周日。

**周数**：该周在**当年**内的第几周（ISO 周），通常一年 52 周，少数年份有 53 周。使用 Python `date.isocalendar()` 的 `iso_week`（1–52 或 53）。

**计算示例**：2026-02-05（周四）所在周为 2026 年第 6 周 → 周规划 `Week6-plan.md`，周总结 `Week6-review.md`。

**跨年周说明**：ISO 周以周四所在年份为准。例如 2025-12-29（周一）至 2026-01-04（周日）这一周，周四为 2026-01-01，故属于 **2026 年 Week1**。同理，若某年 12 月 31 日是周一至周三，则该日属于下一年的 Week1；若是周四至周日，则属于当年最后一周。

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

**来源标记优先级**：当任务同时满足多个来源条件时，按以下顺序选择第一个匹配的标记（不叠加）：
1. `*(从昨天转移)*` — 昨日未完成优先级最高，即使任务也在规划中
2. `*(从 M.D 移入)*` — 从其他日期显式移入
3. `*(来自规划)*` — 纯粹来自周/月规划
4. `*(来自阅读清单)*` / `*(来自 tasks 清单)*` — 来自清单
5. `*(临时追加)*` — 当次对话中新增

**原则**：优先标记「已发生的事实」（昨日遗留），其次是「显式操作」（移入），最后是「来源出处」（规划/清单）。

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

## 级联更新机制

规划体系有五个层级，从上到下为：tasks/TODO（总待办）→ 年规划（可选）→ 月规划 → 周规划 → 日计划。各 Skill 在操作时需按方向逐层检查并同步，确保各层一致。

**从上往下（规划类操作）**：调整任务或生成规划时，从 tasks/TODO 开始向下检查到日计划，确保任务正确分解到各层。适用于 daily-todo（添加/移动任务）和 weekly-plan。

**从下往上（回顾类操作）**：记录日志或生成回顾时，从日计划/日志开始向上检查到年规划，同步完成状态。适用于 daily-log 和 weekly-review。对上层规划文件只做**轻量标记**（`[x]`、进行中等），不改动规划内容本身。

**共同规则**：每一层只在确实受影响时才修改，但必须逐层检查，不可跳过。操作完成后必须向用户汇报所有修改过的文件路径。

| Skill | 方向 | 级联路径 |
|-------|------|---------|
| daily-todo（添加/移动） | 从上往下 | tasks/TODO → 月 → 周 → 日 |
| weekly-plan | 从上往下 | tasks/TODO → 月(只读) → 周 → 已有日计划 |
| daily-log | 从下往上 | 日 → 周 → 月 → 年（轻量标记） |
| weekly-review | 从下往上 | 日志(事实来源) → 周 → 月 → 年（轻量标记） |
| planning-sync | 双向检查 | 全层级事后一致性验证 |

## Planning Sync 建议时机

`jw-agenda-planning-sync` 是事后一致性检查工具，建议在以下时机运行：每周中期（如周三）检查本周执行与规划的偏差；每周末生成周总结前运行一次，确保数据干净；大量调整日程后（如连续使用 daily-todo 添加/移动任务模式）运行一次。

## 冲突裁决策略（多数据源不一致时）

当日 todo / 日日志与周规划、月规划对同一任务的描述或状态不一致时，按以下优先级裁决（用于 planning-sync 及日常同步）：

| 优先级 | 数据源 | 说明 |
|--------|--------|------|
| 1（最高） | 日 todo / 日日志 | 以**当日执行记录**为准。例如：日 todo 已勾选完成，则周规划中对应项应同步为已完成；日日志记录「未完成」或「取消」，则周规划中对应项以日为准。 |
| 2 | 周规划 | 日层级未记录时，以周规划为准；周与月冲突时，以周为准（周更贴近执行）。 |
| 3 | 月规划 | 仅当周、日均无记录时，以月规划为准。 |
| 4 | 年规划 | 仅当月、周、日均无记录时，以年规划为准。年规划为可选层级。 |

原则：**谁更贴近「已发生的事实」谁优先**。日执行是事实记录，周/月/年是计划层，同步时由日→周→月→年向上同步状态与变更。

## 错误处理默认策略

| 情况 | 处理方式 |
|------|---------|
| 文件不存在 | 跳过该来源，继续用已有数据，向用户说明缺少哪个文件 |
| 格式不符预期 | 尽力解析，无法解析时向用户展示文件内容并请求确认 |
| 所有来源都缺失 | 生成最小框架（仅标题和空白区块），标注"无数据来源，请手动补充" |
| 文件已存在（幂等性） | 先读取现有内容，仅追加不重复的新条目，保留用户已有的勾选和备注 |
| 日期歧义（如"下周"） | 推算具体日期后向用户确认 |

## 模板变量命名约定

模板文件（`templates/*.md`）中的占位符统一使用 `{{UPPER_SNAKE_CASE}}` 格式：

| 类别 | 示例 | 说明 |
|------|------|------|
| 日期 | `{{DATE}}`、`{{START_DATE}}`、`{{END_DATE}}` | 日期相关 |
| 周/月 | `{{WEEK_NUM}}`、`{{YEAR_MONTH}}` | 周号或年月 |
| 任务列表 | `{{COMPLETED_TASKS}}`、`{{INCOMPLETE_TASKS}}`、`{{CARRY_OVER_ITEMS}}` | 任务列表（复数） |
| 单个任务 | `{{TASK}}` | 占位符，表示此处填入具体任务 |
| 时间 | `{{TIMESTAMP}}`、`{{TIME_ALLOCATION}}`、`{{ACTUAL_WORK_TIME}}` | 时间戳或时间分配 |
| 统计计数 | `{{COMPLETED_COUNT}}`、`{{TOTAL_COUNT}}`、`{{ACTION_COUNT}}` | 数量统计（以 `_COUNT` 结尾） |
| 统计比率 | `{{COMPLETION_RATE}}` | 比率统计（以 `_RATE` 结尾） |

**命名规则**：
- 全大写，单词间用下划线分隔
- 使用完整单词而非缩写（如 `{{WEEK_NUM}}` 而非 `{{W}}`）
- 列表用 `_S`、`_ITEMS` 或 `_LIST` 后缀（如 `{{COMPLETED_TASKS}}`）
- 数量用 `_COUNT` 后缀（如 `{{COMPLETED_COUNT}}`）
- 比率用 `_RATE` 后缀（如 `{{COMPLETION_RATE}}`）
