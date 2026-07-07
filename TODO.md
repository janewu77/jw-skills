# jw-skills 项目改进清单

来源：`_tmp/jw-skills-evaluation-2026-02.md`、`_tmp/jw-skills-evaluation-2026-02-06.md` 与评估报告中的建议。按**项目层级**与**jw-agenda 层级**分列，各层内按优先级排序。完成一项可勾选。标有 🆕 的为 2026-02-06 评估新增。

---

## 项目层级（仓库级）

适用于仓库根目录、`.github/`、根 README / CONTRIBUTING 等，与具体技能组无关的改进。

### P0 — 高优先级

- [x] **SECURITY.md**：在仓库根新增 `SECURITY.md`，说明漏洞报告方式（如私下邮件/Issue）、支持范围（仅本仓库代码与脚本）、无第三方依赖的说明。GitHub 会在仓库安全页展示。

### P1 — 中优先级

- [x] **CHANGELOG**：在仓库根新增 `CHANGELOG.md`，随版本记录变更；可与 Git tag / GitHub Release 对应。已创建 `CHANGELOG.md`，记录版本历史和功能。
- [x] **发布流程与版本号约定**：根 CONTRIBUTING（中英）已有版本号约定章节。_2026-07 修订：改为按技能组独立版本（scoped tag、各组 CHANGELOG），取消仓库级统一版本与 GitHub Release；jw-agenda 历史迁至 `jw-agenda/CHANGELOG.md`。_
- [x] 🆕 **.DS_Store 残留清理**：已执行清理（`git ls-files | grep '\.DS_Store$' | xargs git rm --cached`）。当前无被跟踪的 `.DS_Store`，`.gitignore` 已有规则可防再次误提交。

### P2 — 中低优先级

- [x] **中英 README 分工**：在根 README 中明确「以英文为权威」或「中文概览 + 链到英文详情」，减少重复维护。

### P3 — 可选

- [x] **CODE_OF_CONDUCT**：已在仓库根添加 Contributor Covenant 2.1 行为准则，明确投诉方式（通过 GitHub Security Policy 或联系维护者）和处理流程。
- [x] **Issue / PR 模板**：已添加 `.github/ISSUE_TEMPLATE/`（包含 bug_report.md、feature_request.md、config.yml）和 `.github/pull_request_template.md`，规范贡献者提 issue/PR。
- [x] **徽章**：已在根 README 和 README.zh-CN 顶部添加徽章（License Apache 2.0、CC-BY-4.0、Python 3.9+、Version 0.1.0），提升信息密度。
- [x] **跨平台说明**：已在根 CONTRIBUTING 和 CONTRIBUTING.zh-CN 中添加「跨平台兼容性」章节，说明 Bash 脚本需 WSL/Git Bash，Python 脚本可独立运行，以及各平台的开发环境要求。
- [ ] **依赖/许可证扫描**：若将来引入第三方依赖，增加 Dependabot 或依赖扫描、许可证合规检查。_当前无第三方依赖，待需要时添加。_
- [ ] **NOTICE**：若引入第三方代码或需专利声明，在仓库根增加 NOTICE 文件并随分发保留。_当前无第三方代码，待需要时添加。_

### 待办 — 新 skill 目录结构约定

新增 skill 或 skill 组时，目录结构统一如下（与 `jw-agenda`、`jw-agenda-v2` 平级）：

```
<skill-name>/
├── doc/    # 当前 skill 的文档
├── src/    # 当前 skill 的源码（jw-agenda-v2 目前用 skills/，后续统一）
└── tests/  # 测试代码（如有）
```

- `jw-agenda` — 一组紧密相关的 skills
- `jw-agenda-v2` — 单个 skill

每新增一个 skill，就在仓库根增加一个同级目录，按上述结构组织。

---

### 子层级引用（jw-agenda）

**jw-agenda 技能组** 改进，详见 **[jw-agenda/TODO.md](jw-agenda/TODO.md)**：

---

## 优先级说明

| 级别   | 含义                                 |
| ------ | ------------------------------------ |
| **P0** | 安全与一致性，建议优先完成           |
| **P1** | 质量与可维护性，有利于长期维护与贡献 |
| **P2** | 体验与开源规范，提升采用与协作       |
| **P3** | 可选，按需与社区反馈补充             |

完成某项后请将对应 `- [ ]` 改为 `- [x]`。
