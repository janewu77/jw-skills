# jw-skills 项目改进清单

来源：`_tmp/jw-skills-evaluation-2026-02.md`、`_tmp/jw-skills-evaluation-2026-02-06.md` 与评估报告中的建议。按**项目层级**与**jw-agenda 层级**分列，各层内按优先级排序。完成一项可勾选。标有 🆕 的为 2026-02-06 评估新增。

---

## 项目层级（仓库级）

适用于仓库根目录、`.github/`、根 README / CONTRIBUTING 等，与具体技能组无关的改进。

### P0 — 高优先级

- [ ] **SECURITY.md**：在仓库根新增 `SECURITY.md`，说明漏洞报告方式（如私下邮件/Issue）、支持范围（仅本仓库代码与脚本）、无第三方依赖的说明。GitHub 会在仓库安全页展示。

### P1 — 中优先级

- [ ] **CHANGELOG**：在仓库根新增 `CHANGELOG.md`，随版本记录变更；可与 Git tag / GitHub Release 对应。
- [ ] **发布流程与版本号约定**：在根 CONTRIBUTING 或单独文档中说明：Release 附 zip（5 个或 1 个捆绑）、CHANGELOG 摘要；仓库级或 jw-agenda 组级版本号与各 Skill metadata version 的对应关系。
- [ ] 🆕 **.DS_Store 残留清理**：Git 中已 tracked 5 个 `.DS_Store` 文件（仓库根、_tmp、jw-agenda、output、skills），需执行 `git rm --cached -r '*.DS_Store'` 清理。`.gitignore` 已有规则但在规则生效前已被提交。

### P2 — 中低优先级

- [ ] **中英 README 分工**：在根 README 中明确「以英文为权威」或「中文概览 + 链到英文详情」，减少重复维护。

### P3 — 可选

- [ ] **CODE_OF_CONDUCT**：在仓库根添加行为准则（如 Contributor Covenant），明确投诉与处理方式。
- [ ] **Issue / PR 模板**：添加 `.github/ISSUE_TEMPLATE/`、`.github/PULL_REQUEST_TEMPLATE.md`，规范贡献者提 issue/PR。
- [ ] **徽章**：在根 README 顶部增加徽章（如 license、Python version、version），提升信息密度。
- [ ] **跨平台说明**：在根 CONTRIBUTING 或 README 中注明：sync/package 脚本需 bash（Windows 建议 WSL 或 Git Bash）；Python 脚本可在 Windows 单独运行。
- [ ] **依赖/许可证扫描**：若将来引入第三方依赖，增加 Dependabot 或依赖扫描、许可证合规检查。
- [ ] **NOTICE**：若引入第三方代码或需专利声明，在仓库根增加 NOTICE 文件并随分发保留。

### 子层级引用（jw-agenda）

以下改进属于 **jw-agenda 技能组**，详见 **[jw-agenda/TODO.md](jw-agenda/TODO.md)**：

| 优先级 | 引用摘要 |
|--------|----------|
| **P0** | dedup_todos 路径安全、脚本多副本同步、🆕 sync 脚本 Glob 不安全 |
| **P1** | date_utils / dedup_todos 单元测试、CI、Python 与运行环境文档、路径假设文档化、🆕 dedup_todos 正则可靠性、🆕 date_utils 输入验证 |
| **P2** | 完整示例 workspace、1～2 个完整对话示例、向后兼容策略、🆕 weekly-plan 分配策略、🆕 planning-sync 匹配规则、🆕 冲突裁决策略、🆕 package-skills.sh 健壮性 |
| **P3** | 快速开始一键命令、🆕 重复任务支持、🆕 撤销/回滚机制、🆕 趋势分析、🆕 标签分类 |

---

## 优先级说明

| 级别 | 含义 |
|------|------|
| **P0** | 安全与一致性，建议优先完成 |
| **P1** | 质量与可维护性，有利于长期维护与贡献 |
| **P2** | 体验与开源规范，提升采用与协作 |
| **P3** | 可选，按需与社区反馈补充 |

完成某项后请将对应 `- [ ]` 改为 `- [x]`。
