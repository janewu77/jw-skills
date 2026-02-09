---
name: jw-agenda-weekly-review
description: "Weekly review: aggregate daily logs, compute completion rate and time allocation, generate summary, list carry-over items. Triggers: '周总结', '本周回顾', 'weekly review', '运行 weekly-review'."
metadata:
  author: Jing Wu
  version: "0.1.2"
  updated: "2026-02-09"
---

# Weekly Review（周回顾）

汇总本周日志与 todo，统计完成率和时间分配，生成周总结报告，识别转入下周的事项。

## 安装前提

本 Skill 仅依赖用户 workspace 下存在 **jw-agenda 根目录**（默认 `jw-agenda-data`，可经 workspace 根目录的 `.jw-agenda.json` 或 `jw-agenda.json` 配置）及子目录 monthly、weekly、daily、tasks。约定与脚本已随本 Skill 安装，无需用户另行复制。先按 conventions 解析 jw-agenda 根目录。

## 约定

开始前读取**本 Skill 的 `assets/conventions.md`** 获取文件命名、路径和周数规则。

## Workflow

### Step 1: 确定回顾范围

使用本 Skill 的 `assets/scripts/date_utils.py` 计算本周/上周的日期范围和年内周数（1–52）。

- **默认**：本周（周一至周日）
- 若用户说「上周回顾」，则使用上周日期范围

### Step 2: 汇总数据

读取本周范围内的所有文件：

**主要来源**：
- `{agendaRoot}/daily/{日期}-log.md`：逐日读取，提取已完成、未完成、时间分配、学习/产出
- `{agendaRoot}/daily/{日期}-todo.md`：逐日读取勾选状态，交叉验证日志

**可选来源**：
- `{agendaRoot}/weekly/Week{W}-plan.md`：对比计划 vs 实际

记录哪些天有数据、哪些天缺失。

### Step 3: 统计分析

**完成率**：`已勾选项总数 / 总项数 × 100%`，某天无 todo 文件则不纳入。分别统计高/中/低优先级。

**时间分配**：从每日日志的「时间分配」部分提取，按类别汇总。

**产出汇总**：从每日日志的「学习/产出」部分汇总为列表。

### Step 4: 生成周总结

使用 `assets/review-template.md` 模板，填充后写入：

**路径**：`{agendaRoot}/weekly/Week{W}-review.md`（W = 年内周数，1–52，与周规划命名一致）

**内容**：整体概览（完成率、主要成就）、分类统计、未完成/待处理、**转入下周**清单。

### Step 5: 汇报

说明：周总结文件路径、完成率、时间分配要点、转入下周事项数量。

## Error Handling

| 情况 | 处理 |
|------|------|
| 部分日期缺少日志 | 用已有日志统计，在报告中标注缺失日期 |
| 全部日期无日志 | 询问用户是否仍需生成空框架 |
| 日志中无时间分配信息 | 跳过时间统计，在报告中标注 |
| 周总结已存在 | 向用户确认是否覆盖，默认不覆盖 |
| 无 todo 文件 | 仅统计日志中的完成/未完成项 |

## 与其他 Skill 的配合（可选）

- 若安装了 **daily-log**：本 Skill 汇总其产出的每日日志。未安装时从 daily todo 文件推断完成情况。
- 若安装了 **daily-todo**：每日 todo 的完成状态用于计算完成率。未安装时从日志推断。
- 若安装了 **weekly-plan**：下周生成周规划时，可读取本 Skill 的「转入下周」部分。未安装时不影响本 Skill。

## Resources

- `assets/review-template.md`：周总结输出模板
- `assets/conventions.md`：约定
- `assets/scripts/date_utils.py`：日期计算脚本
