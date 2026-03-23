# 路由规则

根据用户输入自动选择执行模式。匹配时忽略大小写、首尾空格。

## 触发词映射

| 模式 | 触发场景（任一匹配即触发） |
|------|---------------------------|
| **模式一：每日 Todo** | `生成今天的计划`、`today plan`、`加一项`、`把 X 移到`、`推迟到`、`明天要`、`本周要`、`下周要`、`运行 daily-todo`、`daily-todo` |
| **模式二：每日日志** | `整理日志`、`总结昨天`、`汇报今天`、`记录一下`、`我完成了`、`作业做完了`、`daily log`、`运行 daily-log`、`daily-log` |
| **模式三：周规划** | `生成本周计划`、`周规划`、`weekly plan`、`运行 weekly-plan`、`weekly-plan` |
| **模式四：周总结** | `周总结`、`本周回顾`、`上周回顾`、`weekly review`、`运行 weekly-review`、`weekly-review` |
| **模式五：月总结** | `月总结`、`本月回顾`、`上月回顾`、`monthly review`、`运行 monthly-review`、`monthly-review` |
| **模式六：规划同步** | `同步规划`、`检查一致性`、`planning sync`、`运行 planning-sync`、`planning-sync` |

## 模式对应文件

| 模式 | 执行指令文件 |
|------|-------------|
| 每日 Todo | `references/mode-daily-todo.md` |
| 每日日志 | `references/mode-daily-log.md` |
| 周规划 | `references/mode-weekly-plan.md` |
| 周总结 | `references/mode-weekly-review.md` |
| 月总结 | `references/mode-monthly-review.md` |
| 规划同步 | `references/mode-planning-sync.md` |
| 添加/移动任务（模式一子模式） | `references/mode-add-or-move.md` |

## 匹配优先级

当用户输入可能匹配多个模式时，按以下优先级判断：

1. **精确命令匹配**：如 `运行 daily-todo` 优先于模糊匹配
2. **关键动作词**：如 `加一项`、`移到` 指向每日 Todo；`完成了` 指向每日日志
3. **时间范围词**：`今天` → 日级别；`本周/上周` → 周级别；`本月/上月` → 月级别
4. **歧义时询问**：若仍无法判断，向用户确认意图

## 子模式路由（模式一内部）

模式一（每日 Todo）内部根据意图进一步细分：

| 子模式 | 触发场景 |
|--------|---------|
| A：生成今日 Todo | `生成今天的计划`、`today plan` |
| B1：查询进度 | `完成得怎么样`、`还剩哪些` |
| B2：更新状态 | `不做了`、`取消`、`推迟`（无目标日） |
| C：添加/移动任务 | `加一项`、`明天要`、`移到周三`、`推迟到 2.10` |
