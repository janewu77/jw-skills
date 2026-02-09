---
name: jw-agenda-weekly-plan
description: "Weekly plan generator: create day-by-day breakdown from monthly goals and last week's carry-over. Triggers: '生成本周计划', '周规划', 'weekly plan', '运行 weekly-plan'."
metadata:
  author: Jing Wu
  version: "0.1.2"
  updated: "2026-02-09"
---

# Weekly Plan（周规划生成器）

基于月规划目标和上周延续任务，生成本周按天拆解的规划。

**注意**：本 Skill 生成的是规划草稿。用户可在生成后调整每日安排。daily-todo 会读取本文件作为当日计划的来源之一。

## 安装前提

本 Skill 仅依赖用户 workspace 下存在 **jw-agenda 根目录**（默认 `jw-agenda-data`，可经 workspace 根目录的 `.jw-agenda.json` 或 `jw-agenda.json` 配置）及子目录 monthly、weekly、daily、tasks。约定与脚本已随本 Skill 安装，无需用户另行复制。先按 conventions 解析 jw-agenda 根目录。

## 约定

开始前读取**本 Skill 的 `assets/conventions.md`** 获取周数计算规则、文件命名和路径。

## Workflow

### Step 1: 确定当前周

使用本 Skill 的 `assets/scripts/date_utils.py` 计算：年内周数（1–52）、本周起止日期（周一至周日）、上周日期范围。

### Step 2: 读取月规划

- **路径**：`{agendaRoot}/monthly/YYYY-MM-plan.md`（当前月，如 2026-02-plan.md，可用 date_utils 推算）
- **提取**：月规划中 `Week {W}` 对应小节的重点、核心任务、产出目标
- 若月规划不存在，见 Error Handling

### Step 3: 读取上周延续任务

按优先级读取：
1. **上周总结**（若有）：`{agendaRoot}/weekly/Week{W-1}-review.md` 中的「转入下周」部分
2. **上周日志**：`{agendaRoot}/daily/` 下上周日期范围内的日志，提取「未完成」部分
3. **上周 todo**：`{agendaRoot}/daily/{上周各日期}-todo.md` 中未勾选项
4. **tasks 目录下以 todo 开头的文件**（可选）：如 `{agendaRoot}/tasks/TODO.md`、`todo-readinglist.md`、`todo-*.md`。其中未勾选项作为「待纳入本周」的候选，在按日分配时酌情纳入（可集中在某几天或按优先级分散）

汇总为延续任务清单。

### Step 4: 生成周规划

使用 `assets/week-template.md` 模板结构。

**分配原则**（按优先级与依赖执行）：
- **优先级**：🔴 高 → 周初（周一至周三）；🟡 中 → 中周（周二至周四）；🟢 低 → 周末或周后期。延续任务中高优/紧急的优先于新任务，安排在周一或周二。
- **依赖**：识别依赖链（如 研究→准备→提交），前置任务在前、依赖任务在后，可间隔 1 天。
- **拆分与平衡**：大任务拆成 2–3 天的子任务；每日任务在总览表「现在排在哪天」标为「Daily」；每天约 2–4 项，时间敏感项靠近截止日。

**操作**：从月规划与延续清单提取任务并识别优先级与依赖 → 按上述原则分配到各天 → 填「📋 本周计划内事项总览」表与每日小节（`- [ ] ...`），来源标记：`*(来自规划)*` / `*(从上周转移)*`。

**若 `Week{W}-plan.md` 已存在**：增量更新。保留已完成（`- [x]`）、用户添加与手动调整；仅追加归一化后不重复的新任务；不覆盖用户对日期、优先级、状态的修改。

### Step 5: 写入文件

**路径**：`{agendaRoot}/weekly/Week{W}-plan.md`

若目录不存在则创建。

### Step 6: 汇报

说明：文件路径、本周重点、延续任务数量。提示可用 daily-todo 生成每日计划。

## Error Handling

| 情况 | 处理 |
|------|------|
| 月规划不存在 | 向用户说明，询问是否仅基于上周延续任务生成框架 |
| 月规划中无当前周小节 | 使用月规划的整体目标作为参考 |
| 上周日志/总结不存在 | 跳过延续任务，仅基于月规划生成 |
| 周规划已存在 | 增量更新，保留用户已有内容 |
| 跨月边界（如 1.29–2.4） | 归属 Week 结束日所在月份，参见 conventions.md |

## 与其他 Skill 的配合（可选）

- **月规划**：由用户维护，本 Skill 只读不写。
- 若安装了 **daily-todo**：它会读取本 Skill 产出的周规划生成每日 todo。未安装时不影响本 Skill。
- 若安装了 **weekly-review**：其产出的「转入下周」可作为本 Skill 的延续任务来源。未安装时跳过该数据来源。

## Resources

- `assets/week-template.md`：周规划输出模板
- `assets/conventions.md`：约定
- `assets/scripts/date_utils.py`：日期计算脚本
