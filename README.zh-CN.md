# jw-skills

[![License: Apache 2.0](https://img.shields.io/badge/License-Code%20Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: CC-BY-4.0](https://img.shields.io/badge/License-Docs%20CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.1.2-green.svg)](CHANGELOG.md)

个人维护的、可在 Cursor / Claude 等环境中使用的 Skill 集合。

**English (default)** → [README.md](README.md)

---

## ⭐ 推荐：jw-agenda-v2

**不用切出编辑器，就能规划与执行。**

jw-agenda-v2 是一个含六种模式的 Agent Skill，用自然语言完成从规划到执行再到回顾的闭环。在你真正干活的地方管理日程——skill 会路由到对应模式并同步工作区。数据全部在本地 Markdown 中。

**🔄 完整循环**：📅 月规划 → 📊 周拆解 → ✅ 日执行 → 📝 日志 → 📈 周回顾 → 🗓️ 月总结

只需说：
- 💬「生成本周计划」→ 从月目标拆出按天计划
- 💬「生成今天的计划」→ 按周计划与昨日未完成生成今日待办
- 💬「我完成了简历更新」→ 写日志并自动勾选
- 💬「把申请移到周三」→ 改期并同步各规划文件
- 💬「周总结」/「月总结」→ 汇总日志、完成率与待延续事项

**核心特点**：本地优先（无云、你掌控）· 一次安装（单个 skill、六种模式）· AI 原生（说人话即可，路由表选对模式）

> 想要细粒度、模块化安装？原版 **[jw-agenda](jw-agenda/)** 把同一套工作流做成 5 个可独立安装的 skill。

---

## 📚 包含

| 技能组 | 说明 |
|--------|------|
| [jw-agenda](jw-agenda/) | 📅 个人日程管理，**5 个模块化 skill**：月规划 → 周拆解 → 日执行 → 日志 → 周回顾。详见 [jw-agenda/README.zh-CN.md](jw-agenda/README.zh-CN.md)。 |
| [jw-agenda-v2](jw-agenda-v2/) | 📅 同一套闭环的**单 skill、6 模式**版（新增月总结）。一次安装、中央路由。详见 [jw-agenda-v2/README.zh-CN.md](jw-agenda-v2/README.zh-CN.md)。 |

### 🚀 jw-agenda —— 5 个模块化 skill

**5 个互补的技能** 🤝，共同协作以自动化你的规划和执行工作流程：

- ✅ **jw-agenda-daily-todo**：生成今日计划、重新安排任务、添加临时事项。管理你的每日待办，自动集成时间表。
- 📝 **jw-agenda-daily-log**：将随意的进度汇报转化为结构化日志。总结昨天或记录今天的工作，保留想法和感受。
- 📊 **jw-agenda-weekly-plan**：将月度目标拆解为按天的周计划。自动合并上周的延续任务。
- 📈 **jw-agenda-weekly-review**：汇总周日志、计算完成率、追踪时间分配，并识别需要延续的事项。
- 🔄 **jw-agenda-planning-sync**：检查日/周/月计划的一致性，检测偏差，并在你确认后同步。

📖 安装、示例与完整功能列表详见 **[jw-agenda/README.zh-CN.md](jw-agenda/README.zh-CN.md)**。

### 📦 jw-agenda-v2 —— 同一闭环，单个 skill

`jw-agenda-v2` 把上述工作流合并进**一个含六种模式的 Skill**，配中央路由表，并新增**月总结**模式（支持季度/自定义范围）。它与 `jw-agenda` 使用**相同的数据格式和配置**，因此 `jw-agenda-data/` 两边通用。

- 想要细粒度、模块化安装（只挑需要的 skill）→ 选 **jw-agenda**。
- 想一次装好、覆盖含月总结的完整闭环 → 选 **jw-agenda-v2**。

📖 模式、安装与数据布局详见 **[jw-agenda-v2/README.zh-CN.md](jw-agenda-v2/README.zh-CN.md)**。

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
