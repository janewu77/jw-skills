---
name: jw-agenda-v2
description: "日程管理 / Agenda: daily todo, daily log, weekly plan, weekly review, monthly review, planning sync. 触发词：今天计划、日报、周规划、周总结、月总结、同步规划、today plan、weekly review、monthly review"
metadata:
  author: Jing Wu
  version: "1.2.0"
  updated: "2026-03-23"
---

# jw-agenda-v2

六个日程管理模式合一：每日 Todo、每日日志、周规划、周总结、月总结、规划同步。

## 执行流程

1. **路由判断**：根据下方触发词表匹配目标模式
2. **加载约定**：读取 `assets/conventions.md` 获取通用规则；按模式前置条件加载 `assets/conventions-marks.md` 和/或 `assets/conventions-cascade.md`
3. **执行模式**：读取对应的 `references/mode-*.md` 按其指令执行

## 触发词映射

匹配时忽略大小写、首尾空格。分两层：**精确**（直接触发）和**模糊**（结合上下文，必要时确认）。

| 模式          | 精确触发词                                                                                                                  | 模糊/口语触发词                                            | 指令文件                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| **每日 Todo** | `生成今天的计划`、`today plan`、`today's plan`、`加一项`、`把 X 移到`、`推迟到`、`明天要`、`本周要`、`下周要`、`daily-todo` | `帮我安排今天`、`今日计划`、`今天做什么`、`plan today`     | `references/mode-daily-todo.md`                 |
| **每日日志**  | `整理日志`、`总结昨天`、`汇报今天`、`记录一下`、`我完成了`、`daily log`、`daily-log`                                        | `日报`、`今天的总结`、`recap today`、`今天干了什么`        | `references/mode-daily-log.md`                  |
| **周规划**    | `生成本周计划`、`周规划`、`weekly plan`、`weekly-plan`                                                                      | `规划本周`、`规划下周`、`plan this week`、`plan next week` | `references/mode-weekly-plan.md`                |
| **周总结**    | `周总结`、`本周回顾`、`上周回顾`、`weekly review`、`weekly-review`                                                          | `这周怎么样`、`review this week`、`上周总结`               | `references/mode-weekly-review.md`              |
| **月总结**    | `月总结`、`本月回顾`、`上月回顾`、`monthly review`、`monthly-review`                                                        | `月报`、`recap this month`、`Q1总结`–`Q4总结`              | `references/mode-monthly-review.md`             |
| **规划同步**  | `同步规划`、`检查一致性`、`planning sync`、`planning-sync`                                                                  | `检查规划`、`sync plans`、`规划有没有对齐`                 | `references/mode-planning-sync.md`              |
| **归档日志**  | `归档日志`、`归档 daily`、`archive daily`、`archive logs`、`清理 daily 目录`                                                | —                                                          | `references/mode-weekly-review.md`（仅 Step 6） |

**添加/移动任务**（模式一子模式 C）：`加一项`、`明天要`、`移到周三`、`推迟到 2.10` → 详见 `references/mode-add-or-move.md`。

## 匹配优先级

1. **精确命令** > 模糊匹配
2. **关键动作词**：`加一项`/`移到` → 每日 Todo；`完成了` → 每日日志
3. **时间范围词**：`今天` → 日级别；`本周/上周` → 周级别；`本月/上月/Q1–Q4` → 月级别
4. **歧义时询问**用户确认意图

## 模式一子模式路由

| 子模式           | 触发场景                                      |
| ---------------- | --------------------------------------------- |
| A：生成今日 Todo | `生成今天的计划`、`today plan`                |
| B1：查询进度     | `完成得怎么样`、`还剩哪些`                    |
| B2：更新状态     | `不做了`、`取消`、`推迟`（无目标日）          |
| C：添加/移动任务 | `加一项`、`明天要`、`移到周三`、`推迟到 2.10` |

共用约定见 `assets/conventions.md`。
