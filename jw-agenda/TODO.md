# jw-agenda 改进清单

适用于 `jw-agenda/` 目录下的脚本、文档、示例与 CI。来源：仓库根 [TODO.md](../TODO.md)、`_tmp/jw-skills-evaluation-2026-02.md` 与 `_tmp/jw-skills-evaluation-2026-02-06.md`。完成一项可勾选。标有 🆕 的为 2026-02-06 评估新增。

---

## P0 — 高优先级

- [x] **dedup_todos 路径安全**：对 `dedup_todos.py` 的传入路径做规范化并限制在 workspace 内；或在脚本与文档中明确「仅传入 agenda 根目录下的路径」（可配置，默认 jw-agenda-data），避免路径遍历风险。已实现：脚本校验两路径均在 `WORKSPACE_ROOT`（或 cwd）之下，conventions 中已说明仅传 agenda 根目录下的路径。
- [x] **脚本多副本同步**：在 jw-agenda CONTRIBUTING 或 CI 中强化「修改 _common 后必须执行 sync-common-to-skills.sh」的检查（如 CI 检查 _common 与各 skill assets 是否一致），降低多副本不同步风险。
- [x] 🆕 **sync-common-to-skills.sh Glob 不安全**：已改为 `for f in ...; do [ -f "$f" ] && cp ...; done` 及 LICENSE 单独复制，避免无 .py 时 glob 字面展开导致静默失败。

---

## P1 — 中优先级

- [x] **date_utils.py 单元测试**：已在 `jw-agenda/tests/test_date_utils.py` 增加 pytest 测试（get_date_info 结构/固定日期/年内周/周起止、CLI 指定日期/--yesterday/--week-range/无效日期 exit）。可通过 `DATE_UTILS_TODAY` 固定「今天」便于测试。
- [x] **dedup_todos.py 单元测试**：已在 `jw-agenda/tests/test_dedup_todos.py` 增加 pytest 测试（normalize、extract_items、main 去重结果与路径校验），与 date_utils 同目录。
- [x] **CI**：添加 GitHub Actions（或等价 CI）：运行上述 Python 单元测试；可选检查 SKILL.md 含 name/version、conventions 与 SKILL 中路径关键词一致。已实现：`.github/workflows/jw-agenda-test.yml` 运行 pytest 测试，支持 Python 3.9-3.12。
- [x] **文档：Python 与运行环境**：在 jw-agenda README 或 CONTRIBUTING 中注明 Python 版本（如 3.9+）、已在 Cursor/Claude 下验证的版本或环境，便于用户和贡献者对齐。已在 README 中添加 Python 3.9+ 要求和测试环境说明。
- [x] **路径假设文档化**：jw-agenda 根目录可配置（默认 jw-agenda-data），已在 README 与 conventions 中说明 workspace 根、`.jw-agenda.json` 配置及默认行为，减少用户困惑。
- [x] 🆕 **dedup_todos.py 正则可靠性**：`re.sub(r"\*\(.*?\)\*", ...)` 非贪婪匹配在多标记同行时可能异常；未处理任务名本身含星号的情况。建议增加转义处理或改用更精确的匹配模式。已修复：改用 `r"\*\([^)]+\)\*"` 模式，正确处理多标记和任务名中的星号，并添加了相应测试用例。
- [x] 🆕 **date_utils.py 输入验证**：当前仅接受 ISO 格式（`date.fromisoformat()`），非 ISO 输入（如 "2026/02/05"）报错不清晰。建议增加友好的错误提示或格式转换。已实现：支持 YYYY-MM-DD、YYYY/MM/DD、YYYY.MM.DD 三种格式，并提供友好的错误消息，包含所有支持的格式示例。

---

## P2 — 中低优先级

- [x] **完整示例 workspace**：在 jw-agenda 下提供 `examples/` 或 `sample-workspace/`，包含至少一份月规划、周规划、日 todo 示例，README 可引用为「复制即用」。已实现：`examples/sample-workspace/`（英文）和 `examples/sample-workspace-zh/`（中文），包含完整的月/周/日示例文件。
- [x] **1～2 个完整对话示例**：在 jw-agenda 文档中补充 1～2 个从用户话到产出的完整对话示例（或链接到示例），便于新用户理解用法。已实现：`examples/conversations.md`（英文）和 `examples/conversations.zh-CN.md`（中文），包含 6 个完整对话示例。
- [x] 🆕 **weekly-plan SKILL.md 分配策略**：Step 4 已细化分配原则（优先级→周初/中周/周末、依赖链、拆分与平衡），见 SKILL.md。
- [x] 🆕 **planning-sync SKILL.md 匹配规则**：Step 2 已文档化「归一化后关键词匹配」与完成状态以日执行为准的比对策略。
- [x] 🆕 **冲突裁决策略**：已在 conventions 中定义「日 > 周 > 月」的优先级及「以已发生事实为准」原则。
- [x] 🆕 **package-skills.sh 健壮性**：已增加 SKILLS_DIR 存在性检查、起止日志输出，并去掉 zip -q 便于排查错误。

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
