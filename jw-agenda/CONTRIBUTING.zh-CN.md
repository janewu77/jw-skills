# 维护说明

**语言**：中文版。英文版见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 运行测试

- **环境**：Python 3.9+，`pip install pytest`
- **本地执行**（在仓库根或 `jw-agenda` 下）：

```bash
pytest jw-agenda/tests/ -v   # 或：cd jw-agenda && pytest tests/ -v
```

### CI 测试

当你推送更改到 `main`/`dev` 或打开修改以下路径的 Pull Request 时，GitHub Actions 会自动运行测试：
- `jw-agenda/_common/scripts/**`
- `jw-agenda/skills/**/assets/scripts/**`
- `jw-agenda/tests/**`

**Workflow**：`jw-agenda-test.yml` 会在 Python 3.9、3.10、3.11 和 3.12 上运行 pytest 测试。

**查看结果**：访问 `https://github.com/janewu77/jw-skills/actions`，查找 "Run Tests" workflow 运行记录。

**最佳实践**：推送前在本地运行测试，及早发现问题：
```bash
cd jw-agenda
pytest tests/ -v
```

## 保持 5 个 Skill 一致

> **⚠️** 唯一来源是 `_common/`。修改 `_common/` 后必须同步到所有 skill 的 `assets/` 目录。
>
> **🔄 自动同步**：推送到 `main` 或 `dev` 时，GitHub Actions 会在需要时自动同步并提交更改。对于 Pull Request，必须在推送前手动同步。

### 工作流程：修改 `_common/` 文件

当你修改 `_common/` 下的文件（如 `conventions.md`、`schedule-config.example.md` 或脚本文件）时，请遵循以下流程：

#### 步骤 0：拉取最新代码

始终先拉取最新代码以避免冲突，特别是因为自动同步可能已更新了文件：

```bash
git pull origin dev  # 或 main，取决于你的分支
```

这确保你使用的是最新版本，包括 GitHub Actions 自动同步的任何更改。

#### 步骤 1：提交前 — 检查同步状态

首先，检查是否存在已有的同步问题：

```bash
cd jw-agenda
./scripts/check-common-sync.sh
```

- ✅ **如果通过**：所有 skill 已同步，可以继续修改 `_common/` 文件。
- ❌ **如果失败**：先修复现有的同步问题，再进行新的修改。

#### 步骤 2：进行修改

根据需要编辑 `_common/` 下的文件：
- `_common/conventions.md`
- `_common/schedule-config.example.md`
- `_common/scripts/*.py`
- `_common/scripts/LICENSE`

#### 步骤 3：同步更改到所有 skill

修改 `_common/` 后，将更改同步到所有 5 个 skill：

```bash
cd jw-agenda
./scripts/sync-common-to-skills.sh
```

此命令会将 `_common/` 中的更新文件复制到每个 skill 的 `assets/` 目录。

> **注意**：如果直接推送到 `main` 或 `dev`，即使忘记同步，GitHub Actions 也会自动同步并提交。但建议在推送前本地同步，以保持提交历史清晰。

#### 步骤 4：验证同步（提交前）

再次运行检查脚本，确保所有内容已同步：

```bash
./scripts/check-common-sync.sh
```

预期输出：`✓ All skills are in sync with _common/`

#### 步骤 5：提交所有更改

同时提交 `_common/` 的更改和同步后的 `skills/*/assets/` 文件：

```bash
git add jw-agenda/_common/
git add jw-agenda/skills/*/assets/
git commit -m "你的提交信息"
git push
```

#### 步骤 6：推送后 — 验证 CI 状态

推送后，检查 GitHub Actions 确保 CI 检查通过：

1. **通过本地脚本**（推荐；需安装 [GitHub CLI](https://cli.github.com/) 和 `jq`）：
   ```bash
   cd jw-agenda
   ./scripts/check-workflow-status.sh
   ```
   脚本会检查 `jw-agenda-check-sync` 与 `jw-agenda-test` 两个 workflow；若有失败会以错误码退出并打印 actions 链接。

2. **通过 GitHub 网页界面**：
   - 访问：`https://github.com/janewu77/jw-skills/actions`
   - 找到最新的 "Check Common Sync" 与 "Run Tests" 运行记录
   - 确认显示 ✅（绿色对勾）
   - 如果推送到 `main`/`dev` 时未同步，check-sync workflow 会自动同步并创建提交

3. **通过 GitHub CLI**（手动）：
   ```bash
   gh run list --workflow=jw-agenda-check-sync.yml --limit 5
   gh run list --workflow=jw-agenda-test.yml --limit 5
   gh run view <run-id>  # 查看特定运行的详情
   ```

**自动同步行为**：
- ✅ **推送到 `main`/`dev`**：如果需要同步，GitHub Actions 会自动同步并提交
- ❌ **Pull Request**：必须手动同步；如果未同步，CI 会失败（便于审查）

### 快速参考

```bash
# 检查同步状态
./scripts/check-common-sync.sh

# 同步 _common → 各 skill assets/
./scripts/sync-common-to-skills.sh

# 提交前再次验证
./scripts/check-common-sync.sh

# 推送后：本地检查 GitHub Actions 状态（需 gh + jq）
./scripts/check-workflow-status.sh
```

## 打包（zip）

在 **jw-agenda** 目录下执行（如需先执行 sync）：

```bash
./package-skills.sh
```

输出：`output/` 下每个 skill 一个 zip。

## 版本与命名

- **路径**：以 `assets/conventions.md` 为准 — 月规划 `YYYY-MM-plan.md`，周规划 `Week{N}-plan.md`，周总结 `Week{N}-review.md`。与 conventions 冲突时以 conventions 为准。
- **SKILL.md**：版本号 `0.M.P` — 单 skill 改 patch；整组发布改 minor（如 0.1.0）。

## 递交前

```bash
git pull origin dev  # 先拉取最新更改（或 main，取决于分支）
pytest tests/ -v
./scripts/sync-common-to-skills.sh   # 若改过 _common/
./scripts/check-common-sync.sh
```

## 安全

如果您发现了安全漏洞，请私下报告。详见 [SECURITY.md](../../SECURITY.md) 或 [SECURITY.zh-CN.md](../../SECURITY.zh-CN.md)。
