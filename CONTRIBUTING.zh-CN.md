# 贡献指南

本仓库包含多个 Agent Skills。提交代码或文档前请留意：

- **仓库级**：许可与规范见本文件及根目录 [LICENSE](LICENSE)、[LICENSE-CODE](LICENSE-CODE)、[LICENSE-DOCS](LICENSE-DOCS)。
- **提交信息**：Commit message 请使用英文。
- **各 Skill 特有说明**：若某个 skill 有单独的维护或开发约定，请先阅读该 skill 目录下的 `CONTRIBUTING.md`。

## 跨平台兼容性

### 脚本

- **Bash 脚本**（`sync-common-to-skills.sh`、`package-skills.sh`）：需要 Bash 环境。在 Windows 上，请使用 **WSL**（Windows Subsystem for Linux）或 **Git Bash**。这些脚本主要用于维护者，最终用户无需运行。
- **Python 脚本**（`date_utils.py`、`dedup_todos.py`）：可在 Windows、macOS、Linux 上独立运行。需要 Python 3.9+。

### 开发环境

- **Linux/macOS**：原生支持 Bash，脚本可直接运行。
- **Windows**：
  - 运行 Bash 脚本时使用 WSL 或 Git Bash
  - Python 脚本可通过 `python` 或 `python3` 命令直接运行
  - CI 工作流在 Linux runner 上运行，Windows 特定问题可能需要在 WSL 中测试

## 各 Skill 的贡献说明

| Skill | 说明 |
|-------|------|
| [jw-agenda](jw-agenda/CONTRIBUTING.zh-CN.md) | 约定与脚本修改后需同步到各子 skill，见其维护说明。 |

将来若有新增 skills 且需要开发者特别注意的事项，可在此表补充并对应到该 skill 的 `CONTRIBUTING.md`。

## 版本号约定与打 tag

本仓库是一个**按技能组各自独立版本的 monorepo**。**没有仓库级统一版本号**——每个技能组有自己的版本、自己的 CHANGELOG、自己的 Git tag。这样 `jw-agenda` 和 `jw-agenda-v2` 可以各自按节奏演进（目前两者版本号就不同）。

每个技能组遵循[语义化版本](https://semver.org/lang/zh-CN/)（MAJOR.MINOR.PATCH）：

| 技能组 | 版本来源 | CHANGELOG | tag 前缀 |
|--------|----------|-----------|----------|
| **jw-agenda**（5 个 skill） | 5 个 `SKILL.md` 共用一个**组版本** | [jw-agenda/CHANGELOG.md](jw-agenda/CHANGELOG.md) | `jw-agenda-vX.Y.Z` |
| **jw-agenda-v2**（1 个 skill） | 该 skill 自己的 `SKILL.md` `version` | [jw-agenda-v2/doc/CHANGELOG.md](jw-agenda-v2/doc/CHANGELOG.md) | `jw-agenda-v2-vX.Y.Z` |

对 **jw-agenda**：5 个 skill 共用一个组版本，一起升。对 **jw-agenda-v2**（单个 skill）：它的 `SKILL.md` 版本就是组版本。根 [CHANGELOG.md](CHANGELOG.md) 只是索引 + 仓库级基建说明，本身不带版本号。

本仓库**不使用 GitHub Release**——分发采用源码方式（克隆仓库、复制 skill 文件夹，见各 README 的安装章节）。

### 发布新版本

**一次只处理一个技能组**：

1. **CHANGELOG**：把该组的 `## Unreleased` 内容收进新的 `## X.Y.Z — YYYY-MM-DD` 小节（写在**该组自己**的 CHANGELOG 里）。
2. **skill 版本**：升该组 `SKILL.md` 的 `version`——jw-agenda 是全部 5 个，jw-agenda-v2 是那一个。
3. **提交并打 tag**：提交后为该组创建带前缀的 Git tag。

**示例 —— 发布 jw-agenda-v2 1.4.0：**

```bash
# 1. 在 jw-agenda-v2/doc/CHANGELOG.md 里把 "## Unreleased" 改为 "## 1.4.0 — 2026-07-08"
# 2. 把 jw-agenda-v2/skills/jw-agenda-v2/SKILL.md 的 version 升到 "1.4.0"
# 3. 提交
git add jw-agenda-v2/doc/CHANGELOG.md jw-agenda-v2/skills/jw-agenda-v2/SKILL.md
git commit -m "release(jw-agenda-v2): 1.4.0"

# 4. 打 tag（注意技能组前缀）
git tag -a jw-agenda-v2-v1.4.0 -m "jw-agenda-v2 1.4.0"
git push origin jw-agenda-v2-v1.4.0
```

**示例 —— 发布 jw-agenda 0.3.0：** 步骤相同，但改 `jw-agenda/CHANGELOG.md`、升**全部 5 个** `jw-agenda/skills/*/SKILL.md`、tag 打 `jw-agenda-v0.3.0`。

*（可选：若想把技能打成单个包发给别人、而非直接给仓库，可运行 `./jw-agenda/package-skills.sh` 在 `jw-agenda/output/` 生成本地 zip。）*
