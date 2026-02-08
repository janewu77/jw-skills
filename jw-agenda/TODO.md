# jw-agenda 改进清单

适用于 `jw-agenda/` 目录下的脚本、文档、示例与 CI。来源：仓库根 [TODO.md](../TODO.md)、`_tmp/jw-skills-evaluation-2026-02.md` 与 `_tmp/jw-skills-evaluation-2026-02-06.md`。完成一项可勾选。标有 🆕 的为 2026-02-06 评估新增。

---

## P0 — 高优先级

- [x] **dedup_todos 路径安全**：对 `dedup_todos.py` 的传入路径做规范化并限制在 workspace 或 `personal/agenda` 子树内；或在脚本与文档中明确「仅传入约定目录下的路径」，避免路径遍历风险。已实现：脚本校验两路径均在 `WORKSPACE_ROOT`（或 cwd）之下，conventions 中已说明仅传约定目录路径。
- [ ] **脚本多副本同步**：在 jw-agenda CONTRIBUTING 或 CI 中强化「修改 _common 后必须执行 sync-common-to-skills.sh」的检查（如 CI 检查 _common 与各 skill assets 是否一致），降低多副本不同步风险。
- [x] 🆕 **sync-common-to-skills.sh Glob 不安全**：已改为 `for f in ...; do [ -f "$f" ] && cp ...; done` 及 LICENSE 单独复制，避免无 .py 时 glob 字面展开导致静默失败。

---

## P1 — 中优先级

- [x] **date_utils.py 单元测试**：已在 `jw-agenda/tests/test_date_utils.py` 增加 pytest 测试（get_date_info 结构/固定日期/年内周/周起止、CLI 指定日期/--yesterday/--week-range/无效日期 exit）。可通过 `DATE_UTILS_TODAY` 固定「今天」便于测试。
- [x] **dedup_todos.py 单元测试**：已在 `jw-agenda/tests/test_dedup_todos.py` 增加 pytest 测试（normalize、extract_items、main 去重结果与路径校验），与 date_utils 同目录。
- [ ] **CI**：添加 GitHub Actions（或等价 CI）：运行上述 Python 单元测试；可选检查 SKILL.md 含 name/version、conventions 与 SKILL 中路径关键词一致。
- [ ] **文档：Python 与运行环境**：在 jw-agenda README 或 CONTRIBUTING 中注明 Python 版本（如 3.9+）、已在 Cursor/Claude 下验证的版本或环境，便于用户和贡献者对齐。
- [ ] **路径假设文档化**：在 jw-agenda README 或 conventions 中明确「workspace 根目录即包含 personal/agenda 的目录」及选错时的表现，减少用户困惑。
- [ ] 🆕 **dedup_todos.py 正则可靠性**：`re.sub(r"\*\(.*?\)\*", ...)` 非贪婪匹配在多标记同行时可能异常；未处理任务名本身含星号的情况。建议增加转义处理或改用更精确的匹配模式。
- [ ] 🆕 **date_utils.py 输入验证**：当前仅接受 ISO 格式（`date.fromisoformat()`），非 ISO 输入（如 "2026/02/05"）报错不清晰。建议增加友好的错误提示或格式转换。

---

## P2 — 中低优先级

- [ ] **完整示例 workspace**：在 jw-agenda 下提供 `examples/` 或 `sample-workspace/`，包含至少一份月规划、周规划、日 todo 示例，README 可引用为「复制即用」。
- [ ] **1～2 个完整对话示例**：在 jw-agenda 文档中补充 1～2 个从用户话到产出的完整对话示例（或链接到示例），便于新用户理解用法。
- [ ] **向后兼容策略**：在 jw-agenda 的 conventions 或 CONTRIBUTING 中说明约定变更时的 breaking change 与迁移方式（如文件命名、路径变更时如何迁移旧数据）。
- [ ] 🆕 **weekly-plan SKILL.md 分配策略**：当前 Step 4 仅说「合理分配」，缺乏具体准则（按优先级？按时间可用性？按领域均衡？）。建议在 SKILL.md 中细化分配逻辑。
- [ ] 🆕 **planning-sync SKILL.md 匹配规则**：Step 2 的「内容对齐」检查未明确匹配方式（精确匹配 / 关键词匹配 / 模糊匹配），建议文档化具体比对策略。
- [ ] 🆕 **冲突裁决策略**：当多数据源出现矛盾时（如 daily-log 记录完成但 weekly-plan 仍显示进行中），缺乏优先级裁决规则。建议在 conventions 或 planning-sync 中定义冲突处理原则。
- [ ] 🆕 **package-skills.sh 健壮性**：不检查 SKILLS_DIR 是否存在、旧 zip 不清理直接覆盖、`-q` 标志使错误难以排查。建议增加前置校验和日志输出。

---

## P3 — 可选

- [ ] **快速开始一键命令**：在 jw-agenda README 中提供一段「创建目录 + 解压/复制 skill 到 Cursor」的复制即用命令，降低上手摩擦。
- [ ] 🆕 **重复任务支持（Recurrence）**：当前所有任务为一次性，不支持周期性任务（如「每周一 1:1 会议」）。考虑增加 `recurs: weekly/monthly` 标签与自动生成机制。
- [ ] 🆕 **撤销/回滚机制**：Skill 修改文件后无法回退。考虑在修改前自动创建 `.bak` 备份，或利用 git stash 保存还原点。
- [ ] 🆕 **趋势分析**：weekly-review 当前只统计当期完成率，不支持趋势对比。建议增加「周环比完成率」、「时间分配趋势」等指标。
- [ ] 🆕 **标签分类**：当前无任务标签体系（如 `#work` / `#health` / `#learning`），无法做跨领域时间分析。考虑在 conventions 中定义标签语法并在 weekly-review 中支持按标签聚合。

---

## 优先级说明

| 级别 | 含义 |
|------|------|
| **P0** | 安全与一致性，建议优先完成 |
| **P1** | 质量与可维护性，有利于长期维护与贡献 |
| **P2** | 体验与开源规范，提升采用与协作 |
| **P3** | 可选，按需与社区反馈补充 |

完成某项后请将对应 `- [ ]` 改为 `- [x]`。
