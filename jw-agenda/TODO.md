# jw-agenda 改进清单

适用于 `jw-agenda/` 目录下的脚本、文档、示例与 CI。来源：仓库根 [TODO.md](../TODO.md) 与 `_tmp/jw-skills-evaluation-2026-02.md`。完成一项可勾选。

---

## P0 — 高优先级

- [ ] **dedup_todos 路径安全**：对 `dedup_todos.py` 的传入路径做规范化并限制在 workspace 或 `personal/agenda` 子树内；或在脚本与文档中明确「仅传入约定目录下的路径」，避免路径遍历风险。
- [ ] **脚本多副本同步**：在 jw-agenda CONTRIBUTING 或 CI 中强化「修改 _common 后必须执行 sync-common-to-skills.sh」的检查（如 CI 检查 _common 与各 skill assets 是否一致），降低多副本不同步风险。

---

## P1 — 中优先级

- [ ] **date_utils.py 单元测试**：为 `date_utils.py` 增加单元测试（如 `get_date_info` 对固定日期的输出、`--yesterday` / `--week-range` 行为），放在 `tests/` 或 `jw-agenda/_common/scripts/tests/`。
- [ ] **dedup_todos.py 单元测试**：为 `dedup_todos.py` 增加单元测试（normalize、extract_items、去重结果），与 date_utils 测试同目录。
- [ ] **CI**：添加 GitHub Actions（或等价 CI）：运行上述 Python 单元测试；可选检查 SKILL.md 含 name/version、conventions 与 SKILL 中路径关键词一致。
- [ ] **文档：Python 与运行环境**：在 jw-agenda README 或 CONTRIBUTING 中注明 Python 版本（如 3.9+）、已在 Cursor/Claude 下验证的版本或环境，便于用户和贡献者对齐。
- [ ] **路径假设文档化**：在 jw-agenda README 或 conventions 中明确「workspace 根目录即包含 personal/agenda 的目录」及选错时的表现，减少用户困惑。

---

## P2 — 中低优先级

- [ ] **完整示例 workspace**：在 jw-agenda 下提供 `examples/` 或 `sample-workspace/`，包含至少一份月规划、周规划、日 todo 示例，README 可引用为「复制即用」。
- [ ] **1～2 个完整对话示例**：在 jw-agenda 文档中补充 1～2 个从用户话到产出的完整对话示例（或链接到示例），便于新用户理解用法。
- [ ] **向后兼容策略**：在 jw-agenda 的 conventions 或 CONTRIBUTING 中说明约定变更时的 breaking change 与迁移方式（如文件命名、路径变更时如何迁移旧数据）。

---

## P3 — 可选

- [ ] **快速开始一键命令**：在 jw-agenda README 中提供一段「创建目录 + 解压/复制 skill 到 Cursor」的复制即用命令，降低上手摩擦。

---

## 优先级说明

| 级别 | 含义 |
|------|------|
| **P0** | 安全与一致性，建议优先完成 |
| **P1** | 质量与可维护性，有利于长期维护与贡献 |
| **P2** | 体验与开源规范，提升采用与协作 |
| **P3** | 可选，按需与社区反馈补充 |

完成某项后请将对应 `- [ ]` 改为 `- [x]`。
