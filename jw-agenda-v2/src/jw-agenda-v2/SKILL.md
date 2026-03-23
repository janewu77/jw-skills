---
name: jw-agenda-v2
description: "日程管理工具：每日 Todo、每日日志、周规划、周总结、月总结、规划同步"
metadata:
  author: Jing Wu
  version: "1.2.0"
  updated: "2026-03-23"
  tags: ["agenda", "todo", "planning"]
---

# jw-agenda-v2

六个日程管理模式合一：每日 Todo、每日日志、周规划、周总结、月总结、规划同步。

## 执行流程

1. **路由判断**：读取 `assets/routing.md`，根据用户输入匹配目标模式
2. **加载约定**：读取 `assets/conventions.md` 获取通用规则
3. **执行模式**：读取对应的 `references/mode-*.md` 按其指令执行

## 模式速查

| 模式 | 简述 | 指令文件 |
|------|------|---------|
| 每日 Todo | 生成/调整今日计划 | `references/mode-daily-todo.md` |
| 每日日志 | 记录完成情况 | `references/mode-daily-log.md` |
| 周规划 | 生成本周计划 | `references/mode-weekly-plan.md` |
| 周总结 | 汇总本周执行 | `references/mode-weekly-review.md` |
| 月总结 | 汇总本月执行 | `references/mode-monthly-review.md` |
| 规划同步 | 检查一致性 | `references/mode-planning-sync.md` |

详细触发词见 `assets/routing.md`；共用约定见 `assets/conventions.md`。
