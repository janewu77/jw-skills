# 示例

**语言**：本文档为中文版。其他语言版本请参见：
- [README.md](README.md) (English)

本目录包含示例工作区和对话示例，展示如何使用 jw-agenda。

## 示例工作区

### 中文版 (`sample-workspace-zh/`)

完整的中文示例工作区，包含：
- 月规划 (`monthly/2026-02-plan.md`)
- 周规划 (`weekly/Week6-plan.md`)
- 日待办 (`daily/2026-02-05-todo.md`)
- 日日志 (`daily/2026-02-05-log.md`)
- 周总结 (`weekly/Week6-review.md`)
- 通用任务 (`tasks/TODO.md`)

## 使用方法

1. **复制工作区**：将 `sample-workspace-zh/` 复制到你的工作区根目录
2. **重命名**：重命名为 `jw-agenda-data`（默认）或通过 `.jw-agenda.json` 配置
3. **自定义**：编辑文件，填入你自己的计划和任务
4. **开始使用**：安装 jw-agenda 技能，开始使用自然语言命令

## 文件说明

- **月规划** (`monthly/YYYY-MM-plan.md`)：高级目标和每周重点
- **周规划** (`weekly/Week{N}-plan.md`)：本周任务的逐日分解
- **日待办** (`daily/YYYY-MM-DD-todo.md`)：今天的任务，包含时间表和优先级
- **日日志** (`daily/YYYY-MM-DD-log.md`)：记录完成情况、时间分配和反思
- **周总结** (`weekly/Week{N}-review.md`)：本周总结，包含完成统计和延续事项
- **通用待办** (`tasks/TODO.md`)：没有具体日期的任务

## 对话示例

参见 [conversations.zh-CN.md](conversations.zh-CN.md) 了解使用自然语言与 jw-agenda 技能交互的完整示例。

其他语言版本的示例：
- [conversations.md](conversations.md) (English)

## 示例工作流程

1. **月初**：创建包含目标的月规划
2. **周初**：从月规划生成周规划
3. **每天早晨**：从周规划生成今日待办
4. **白天**：使用技能添加任务、重新安排或汇报进度
5. **晚上**：从随意汇报生成日志
6. **周末**：生成周总结并规划下周

详细使用说明请参见主 [README.md](../README.md)。
