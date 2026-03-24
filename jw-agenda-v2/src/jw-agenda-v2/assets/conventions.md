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

**推荐**：使用**本 Skill 的** `scripts/date_utils.py` 计算日期和周数，避免手算错误。`scripts/dedup_todos.py` 供合并 todo 时去重（如 daily-todo 模式 A 幂等合并）；可选，Skill 也可在逻辑内自行去重。**调用 dedup_todos.py 时仅传入 jw-agenda 根目录下的路径**（即已按用户配置解析后的路径），脚本会校验路径位于 workspace 内，避免路径遍历。

## 临时追加的归属

详见 `references/mode-add-or-move.md` Step 1 中的写入规则表。操作完成后**始终向用户汇报写入了哪些文件**。

## 标记约定（来源 / 状态 / 优先级）

详见 `assets/conventions-marks.md`（daily-todo 和 add-or-move 在开始前加载）。

## 级联更新与冲突裁决

详见 `assets/conventions-cascade.md`（daily-log、weekly-review、monthly-review、weekly-plan、add-or-move、planning-sync 在开始前加载）。

## 错误处理默认策略

| 情况 | 处理方式 |
|------|---------|
| 文件不存在 | 跳过该来源，继续用已有数据，向用户说明缺少哪个文件 |
| 格式不符预期 | 尽力解析，无法解析时向用户展示文件内容并请求确认 |
| 所有来源都缺失 | 生成最小框架（仅标题和空白区块），标注"无数据来源，请手动补充" |
| 文件已存在（幂等性） | 先读取现有内容，仅追加不重复的新条目，保留用户已有的勾选和备注 |
| 日期歧义（如"下周"） | 推算具体日期后向用户确认 |


