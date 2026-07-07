# jw-skills

[![License: Apache 2.0](https://img.shields.io/badge/License-Code%20Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-Docs%20CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](CHANGELOG.md)

个人维护的、可在 Cursor / Claude 等环境中使用的 Skill 集合。

**English (default)** → [README.md](README.md)

---

## ⭐ 推荐：jw-agenda

**不用切出编辑器，就能规划与执行。**

jw-agenda 是一套 5 个 Agent Skill，用自然语言完成从规划到执行再到回顾的闭环。在你真正干活的地方管理日程——助手会选对 skill 并同步工作区。数据全部在本地 Markdown 中。

**🔄 完整循环**：📅 月规划 → 📊 周拆解 → ✅ 日执行 → 📝 日志 → 📈 周回顾

只需说：
- 💬「生成本周计划」→ 从月目标拆出按天计划
- 💬「生成今天的计划」→ 按周计划与昨日未完成生成今日待办
- 💬「我完成了简历更新」→ 写日志并自动勾选
- 💬「把申请移到周三」→ 改期并同步各规划文件
- 💬「周总结」→ 汇总日志、完成率与待延续事项

**核心特点**：本地优先（无云、你掌控）· 模块化（5 个 skill，可只装部分）· AI 原生（说人话即可，助手选对 skill）

---

## 📚 包含

| 技能组 | 说明 |
|--------|------|
| [jw-agenda](jw-agenda/) | 📅 个人日程管理，**5 个模块化 skill**：月规划 → 周拆解 → 日执行 → 日志 → 周回顾。详见 [jw-agenda/README.md](jw-agenda/README.md)。 |
| [jw-agenda-v2](jw-agenda-v2/) | 📅 同一套闭环的**单 skill、6 模式**版（新增月总结）。一次安装、中央路由。详见 [jw-agenda-v2/README.zh-CN.md](jw-agenda-v2/README.zh-CN.md)。 |

### 🚀 jw-agenda：完整的个人生产力系统

**5 个互补的技能** 🤝，共同协作以自动化你的规划和执行工作流程：

- ✅ **jw-agenda-daily-todo**：生成今日计划、重新安排任务、添加临时事项。管理你的每日待办，自动集成时间表。
- 📝 **jw-agenda-daily-log**：将随意的进度汇报转化为结构化日志。总结昨天或记录今天的工作，保留想法和感受。
- 📊 **jw-agenda-weekly-plan**：将月度目标拆解为按天的周计划。自动合并上周的延续任务。
- 📈 **jw-agenda-weekly-review**：汇总周日志、计算完成率、追踪时间分配，并识别需要延续的事项。
- 🔄 **jw-agenda-planning-sync**：检查日/周/月计划的一致性，检测偏差，并在你确认后同步。

### 📦 jw-agenda-v2：同一闭环，单个 skill

`jw-agenda-v2` 把上述工作流合并进**一个含六种模式的 Skill**，配中央路由表，并新增**月总结**模式（支持季度/自定义范围）。它与 `jw-agenda` 使用**相同的数据格式和配置**，因此 `jw-agenda-data/` 两边通用。

- 想要细粒度、模块化安装（只挑需要的 skill）→ 选 **jw-agenda**。
- 想一次装好、覆盖含月总结的完整闭环 → 选 **jw-agenda-v2**。

模式、安装与数据布局详见 [jw-agenda-v2/README.zh-CN.md](jw-agenda-v2/README.zh-CN.md)。

**✨ 核心优势**：
- 💬 **自然语言**：只需与 AI 助手对话——无需复杂的命令或语法
- 🔒 **本地存储**：所有数据以 Markdown 文件形式存储在您的工作区——注重隐私且可移植
- 🧩 **模块化设计**：只安装需要的技能；每个技能独立工作
- 🔗 **无缝集成**：技能在可用时自动读取彼此的输出
- 🎯 **灵活工作流**：支持结构化规划和随意的进度汇报

**🎯 适合**：个人生产力、项目管理、习惯追踪、目标管理，以及任何希望通过 AI 辅助自动化规划工作流程的人。

详见[详细文档](jw-agenda/README.md)了解安装、示例和完整功能列表。**预打包 zip** 可在 [Releases](https://github.com/janewu77/jw-skills/releases) 下载。

---

## 🚀 快速开始

### jw-agenda

1. 📁 **创建数据目录**：
   ```bash
   mkdir -p jw-agenda-data/{monthly,weekly,daily,tasks}
   ```

2. 📦 **安装技能**：从 [Releases](https://github.com/janewu77/jw-skills/releases) 下载 5 个技能的 zip，分别解压到 Cursor 技能目录（如 `~/.cursor/skills/`）。若本地已有仓库，也可直接复制 `jw-agenda/skills/` 下的文件夹。

3. 📅 **创建第一个月度计划**：在 `jw-agenda-data/monthly/` 中添加 `YYYY-MM-plan.md`（如 `2026-02-plan.md`）。

4. 🎉 **开始使用**：在 Cursor 中打开工作区，说"生成本周计划"或"生成今天的计划"。

详细的安装说明、示例和自定义选项，请参阅 [jw-agenda/README.md](jw-agenda/README.md)。

---

## 🛠️ 开发

改进计划与已知问题见 [TODO.md](TODO.md)。

## 🔒 安全

漏洞报告相关信息见 [SECURITY.md](SECURITY.md) 或 [SECURITY.zh-CN.md](SECURITY.zh-CN.md)。

## 社区与反馈

本项目是 **#BuildInPublic** 的一部分。若你使用 Cursor 或 Claude，且喜欢少干扰、基于 Markdown 的流程，欢迎反馈。欢迎❤️贡献，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## License

本仓库整体采用：**代码 Apache 2.0，文档 CC-BY-4.0**。适用于仓库内全部内容（含 jw-agenda 等子目录）。详见 [LICENSE](LICENSE)、[LICENSE-CODE](LICENSE-CODE)、[LICENSE-DOCS](LICENSE-DOCS)。
