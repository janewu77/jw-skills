---
name: jw-agenda-v2
description: "日程管理全套工具：生成今日计划、整理每日日志、生成本周规划、生成周总结回顾、检查规划一致性。触发词：'生成今天的计划'、'today plan'、'加一项'、'把X移到周三'、'明天要'、'整理昨天的日志'、'总结昨天'、'汇报今天'、'记录一下今天'、'我完成了X'、'作业做完了'、'daily log'、'生成本周计划'、'周规划'、'weekly plan'、'周总结'、'本周回顾'、'上周回顾'、'weekly review'、'同步规划'、'检查一致性'、'planning sync'、'运行 daily-todo'、'运行 daily-log'、'运行 weekly-plan'、'运行 weekly-review'、'运行 planning-sync'。"
metadata:
  author: Jing Wu
  version: "1.0.0"
  updated: "2026-03-19"
---

# jw-agenda-v2

五个日程管理模式合一：每日 Todo、每日日志、周规划、周总结、规划同步。

## 触发路由

根据用户意图自动选择模式：

| 触发场景 | 模式 |
|---------|------|
| 「生成今天的计划」「today plan」「加一项」「把 X 移到周三」「推迟到下周」「明天要」「运行 daily-todo」 | **模式一**：每日 Todo |
| 「整理昨天的日志」「总结昨天」「汇报今天」「记录一下今天」「我完成了 X」「作业做完了」「daily log」「运行 daily-log」 | **模式二**：每日日志 |
| 「生成本周计划」「周规划」「weekly plan」「运行 weekly-plan」 | **模式三**：周规划 |
| 「周总结」「本周回顾」「上周回顾」「weekly review」「运行 weekly-review」 | **模式四**：周总结 |
| 「同步规划」「检查一致性」「planning sync」「运行 planning-sync」 | **模式五**：规划同步 |

---

## 执行说明

收到用户指令后，根据上方路由表判断模式，然后读取对应的 references 文件按其指令执行：

| 模式 | 读取文件 |
|------|---------|
| 每日 Todo | `references/mode-daily-todo.md` |
| 每日日志 | `references/mode-daily-log.md` |
| 周规划 | `references/mode-weekly-plan.md` |
| 周总结 | `references/mode-weekly-review.md` |
| 规划同步 | `references/mode-planning-sync.md` |
| 添加/移动任务（模式一子模式 C） | `references/mode-add-or-move.md` |

共用约定见 `assets/conventions.md`。
