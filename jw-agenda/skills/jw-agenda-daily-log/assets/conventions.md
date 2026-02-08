# 约定（所有 Skill 统一引用）

## 路径查找

本约定位于**本 Skill 的 `assets/conventions.md`**。所有 Skill 在运行前应读取此文件（相对于本 Skill 的安装目录），以获取下方约定。用户工作区中仅存放**数据**与**可选的用户作息配置**，见「目录路径」与「文件命名规则」。

## 目录路径（用户工作区）

日程计划与完成情况统一放在用户 workspace 的 `personal/agenda/` 下，按时间粒度分子目录：

| 用途 | 路径 |
|------|------|
| 月规划、月总结 | `personal/agenda/monthly/` |
| 周规划、周总结 | `personal/agenda/weekly/` |
| 日 Todo、日日志 | `personal/agenda/daily/` |
| 其他任务与清单（含阅读清单） | `personal/agenda/tasks/` |
| 用户作息配置（可选） | 单文件 `personal/agenda/schedule-config.md`，见下方文件命名。 |

## 文件命名规则

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| 月规划 | `YYYY-MM-plan.md`（如 `2026-02-plan.md`，2 月即 2026-02） | `2026-02-plan.md` |
| 周规划 | `Week{N}-plan.md`（N = 年内周号，1–52） | `Week6-plan.md` |
| 日 Todo | `YYYY-MM-DD-todo.md` | `2026-02-05-todo.md` |
| 日志 | `YYYY-MM-DD-log.md` | `2026-02-05-log.md` |
| 周总结 | `Week{N}-review.md`（N = 年内周号，与周规划一致） | `Week6-review.md` |
| 阅读清单 | `todo-readinglist.md` | `personal/agenda/tasks/todo-readinglist.md` |
| 未定日期 / 待办池 | `TODO.md` | `personal/agenda/tasks/TODO.md` |
| 作息时间配置（可选） | `schedule-config.md` | `personal/agenda/schedule-config.md`（若不存在，daily-todo 使用本 Skill 的 `assets/schedule-config.example.md`） |

**tasks 目录下以 `todo` 开头的文件**（如 `TODO.md`、`todo-readinglist.md`、`todo-xxx.md`）均视为待办/清单。生成周规划或日计划时，应将上述文件中的未勾选项作为可选来源纳入考虑。

**日志中的「今日想法/随口记」**：用户口语化汇报进度时，想法、感受、碎碎念记入该区块，原意保留，便于日后回顾。

## daily-log 与 daily-todo 的分工

两个 Skill 有明确分工，唯一重叠点是「更新今日 todo 的勾选」：

| | daily-log | daily-todo |
|--|-----------|------------|
| **定位** | 记录&留痕&执行 | 计划，只处理未完成的 |
| **典型触发** | 「总结昨天」「汇报今天（口语化、带想法）」「我完成了 X」等完成/汇报类 | 「生成今天的计划」「把 X 移到周三」「加一项」等计划与调整类 |
| **产出** | 日志文件（`YYYY-MM-DD-log.md`） | Todo 文件（`YYYY-MM-DD-todo.md`）+ 同步周/月规划 |
| **不做** | 不生成/修改今日计划结构, | 不写日志 |

**选择规则**：凡与「完成进度、汇报今天」相关的，均由 **daily-log** 处理（写日志 + 顺带更新今日 todo 勾选）。成段汇报（「今天做了…还有…感觉…」）→ daily-log；单句更新（「我完成了简历」「作业做完了」等）→ 也由 daily-log。**daily-todo** 只负责「生成今天的计划」「把 X 移到周三」「加一项」等计划生成与日程调整，不负责标记完成。

## 周数计算规则

**周起止**：周一至周日。

**周数**：该周在**当年**内的第几周（ISO 周），通常一年 52 周，少数年份有 53 周。使用 Python `date.isocalendar()` 的 `iso_week`（1–52 或 53）。

**计算示例**：2026-02-05（周四）所在周为 2026 年第 6 周 → 周规划 `Week6-plan.md`，周总结 `Week6-review.md`。

**推荐**：使用**本 Skill 的** `assets/scripts/date_utils.py` 计算日期和周数，避免手算错误。`assets/scripts/dedup_todos.py` 供合并 todo 时去重（如 daily-todo 模式 A 幂等合并）；可选，Skill 也可在逻辑内自行去重。**调用 dedup_todos.py 时仅传入约定目录（如 personal/agenda 下）内的路径**，脚本会校验路径位于 workspace 内，避免路径遍历。

## 临时追加的归属

用户临时想到要加一项时，按时间范围写入对应文件，并**始终向用户汇报写入了哪个文件**：

| 时间范围 | 写入文件 |
|----------|----------|
| **无法确定日期** / **不是当月会做的事** | `personal/agenda/tasks/TODO.md` |
| 今天 / 明天 / 本周某天 | `personal/agenda/daily/YYYY-MM-DD-todo.md` |
| 本周（无具体日） / 下周 / 某周 | `personal/agenda/weekly/Week{W}-plan.md` |
| 本月 / 以后（更远） | `personal/agenda/monthly/YYYY-MM-plan.md`（或对应周规划） |

详见 jw-agenda-daily-todo 的「模式 D：临时追加」（`references/mode-d-adhoc.md`）。

## 来源标记

| 来源 | 标记格式 |
|------|---------|
| 昨天未完成 | `*(从昨天转移)*` |
| 月/周规划 | `*(来自规划)*` |
| 昨天未完成 + 也在规划中 | `*(从昨天转移)*` |
| 从其他日期移入 | `*(从 M.D 移入)*` |
| 来自阅读清单 | `*(来自阅读清单)*` |
| 来自 tasks 清单（含上述及其他 todo 开头文件） | `*(来自 tasks 清单)*` |

## 状态标记（daily-todo 更新状态时使用）

| 状态 | 在 todo 条目上的写法 |
|------|----------------------|
| 已完成 | `- [x] 事项内容` |
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

`jw-agenda-planning-sync` 是事后一致性检查工具，建议在以下时机运行：每周中期（如周三）检查本周执行与规划的偏差；每周末生成周总结前运行一次，确保数据干净；大量调整日程后（如连续使用 daily-todo 模式 C/D）运行一次。

## 错误处理默认策略

| 情况 | 处理方式 |
|------|---------|
| 文件不存在 | 跳过该来源，继续用已有数据，向用户说明缺少哪个文件 |
| 格式不符预期 | 尽力解析，无法解析时向用户展示文件内容并请求确认 |
| 所有来源都缺失 | 生成最小框架（仅标题和空白区块），标注"无数据来源，请手动补充" |
| 文件已存在（幂等性） | 先读取现有内容，仅追加不重复的新条目，保留用户已有的勾选和备注 |
| 日期歧义（如"下周"） | 推算具体日期后向用户确认 |
