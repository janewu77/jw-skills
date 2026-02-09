# 贡献指南

本仓库包含多个 Agent Skills。提交代码或文档前请留意：

- **仓库级**：许可与规范见本文件及根目录 [LICENSE](LICENSE)、[LICENSE-CODE](LICENSE-CODE)、[LICENSE-DOCS](LICENSE-DOCS)。
- **提交信息**：Commit message 请使用英文。
- **各 Skill 特有说明**：若某个 skill 有单独的维护或开发约定，请先阅读该 skill 目录下的 `CONTRIBUTING.md`。

## 各 Skill 的贡献说明

| Skill | 说明 |
|-------|------|
| [jw-agenda](jw-agenda/CONTRIBUTING.zh-CN.md) | 约定与脚本修改后需同步到各子 skill，见其维护说明。 |

将来若有新增 skills 且需要开发者特别注意的事项，可在此表补充并对应到该 skill 的 `CONTRIBUTING.md`。

## 发布流程与版本号约定

### 版本号规则

本仓库遵循[语义化版本](https://semver.org/lang/zh-CN/)（MAJOR.MINOR.PATCH）：

- **仓库级版本**：记录在 `CHANGELOG.md` 中（如 `0.1.0`）
- **技能组版本**：如 `jw-agenda` 技能组，版本与仓库版本一致
- **单个 Skill 版本**：每个 skill 的 `SKILL.md` metadata 中包含 `version` 字段（如 `version: "0.1.0"`）

**版本对齐**：发布新版本时：
1. 更新 `CHANGELOG.md` 中的版本号和变更内容
2. 更新所有 skill 的 `SKILL.md` metadata 中的 `version` 字段，使其与仓库版本一致
3. 更新技能组级版本（如适用）使其与仓库版本一致

### 发布流程

创建 GitHub Release 时：

1. **版本标签**：创建与版本号匹配的 Git 标签（如 `v0.1.0`）
2. **CHANGELOG 摘要**：在 Release 说明中包含 `CHANGELOG.md` 的摘要
3. **分发文件**：附加分发文件：
   - **方式 A（推荐）**：5 个独立的 zip 文件（每个 skill 一个），通过在 `jw-agenda/` 目录下运行 `./package-skills.sh` 生成
   - **方式 B**：一个包含所有 skill 的捆绑 zip（如需要批量分发）
4. **Release 说明**：包含：
   - 变更内容（来自 CHANGELOG）
   - 安装说明（链接到 README）
   - 破坏性变更（如有）

### 发布流程示例

```bash
# 1. 更新 CHANGELOG.md 中的新版本
# 2. 更新所有 skill 的 SKILL.md version 字段
# 3. 提交更改
git add CHANGELOG.md jw-agenda/skills/*/SKILL.md
git commit -m "chore: bump version to 0.2.0"

# 4. 创建标签
git tag -a v0.2.0 -m "Release v0.2.0"

# 5. 生成分发 zip（针对 jw-agenda）
cd jw-agenda
./package-skills.sh
cd ..

# 6. 推送标签
git push origin v0.2.0

# 7. 通过 GitHub Web UI 创建 Release，附加 jw-agenda/output/ 下的 zip 文件
```
