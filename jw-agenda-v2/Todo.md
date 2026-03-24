## Todo

### 原有计划

-1 [ ] 写 jw-agenda-v2 的文档（skill 介绍、与 jw-agenda 的关系）
-2 [ ] 是否要写成英文的 prompt？
-3 [ ] 更新上一层的文档（先列出有哪些要更新改的）
-4 [ ] **考虑增加月总结模式** — 当前只有 weekly-review，可增加 mode-monthly-review.md（或明确说明由用户手动维护）

---

### 代码审阅改进项（2026-03-23）

#### 🔴 高优先级

- [x] **修复模板 Handlebars 语法** — `log-template.md` 和 `review-template.md` 中的 `{{#each}}` 循环语法不会被执行，改为占位符说明 ✅
- [x] **修复 week-template.md 第18行** — 表格中有不完整的行 `| 2 |`，需补全或删除 ✅
- [x] **消除内容重复** — `mode-add-or-move.md` 与 `mode-daily-todo.md` 子模式 C 内容几乎完全相同，选择一处保留 ✅

#### 🟡 中优先级

- [x] **精简 SKILL.md description** — 当前 ~400 字符过长，触发词移到正文路由表 ✅
- [x] **统一周数格式** — `Week6` vs `Week 6`（有/无空格），建议统一为无空格 ✅（已确认一致）
- [x] **扩展 date_utils.py** — 增加 `--next-week`、`--prev-week`、`--tomorrow`、`--month-range` 等功能 ✅

#### 🟢 低优先级

- [x] **整合 conventions.md 表格** — 「用户作息配置」和「总结分类配置」放在目录路径表格外，建议整合进表格 ✅
- [x] **补充来源标记优先级说明** — 说明「从昨天转移 > 来自规划」的优先级规则 ✅
- [x] **dedup_todos.py 添加注释** — 说明正则 `\*\([^)]+\)\*` 对嵌套括号的限制 ✅
- [x] **提取通用错误处理** — 各 mode 文件的错误处理表格有重复，可提取到 conventions.md ✅（添加引用说明）
- [x] **schedule-config.example.md 添加说明** — 提示用户这是示例，需根据自己作息调整 ✅

#### 📝 小改进

- [x] SKILL.md 增加 `tags: ["agenda", "todo", "planning"]` ✅（放入 metadata）
- [x] conventions.md 增加跨年周说明（如 2025-12-29 属于 2026 年 Week1） ✅
- [x] mode-planning-sync.md Step 5 支持「仅执行 ⚠️ 需行动项」的快捷选项 ✅
- [x] 统一模板变量命名风格 ✅（`{{W}}` → `{{WEEK_NUM}}`，添加命名约定文档）

---

### 第二轮审阅改进项（2026-03-23）

#### 🔴 高优先级

- [x] **修复 conventions.md 脚本路径** — 第 82 行 `assets/scripts/date_utils.py` 和 `assets/scripts/dedup_todos.py` 路径错误，实际应为 `scripts/date_utils.py` 和 `scripts/dedup_todos.py` ✅
- [x] **统一模式编号** — mode-planning-sync.md 自称「模式五」、mode-monthly-review.md 自称「模式六」，与 routing.md（月总结=5、规划同步=6）矛盾，以 routing.md 为准修改两个 mode 文件标题 ✅
- [x] **mode-add-or-move.md 增加错误处理段落** — 其他 mode 文件均有独立错误处理表，此文件缺失。至少覆盖：目标日期歧义、目标文件不存在、源任务找不到、跨月/跨年边界 ✅

#### 🟡 中优先级

- [x] **提取级联同步逻辑到 conventions.md** — 级联更新步骤在 5 个 mode 文件中大量重复，提取为 conventions.md「级联同步标准步骤」子章节，各 mode 改为引用 ✅
- [x] **date_utils.py 增加 `--prev-month` / `--next-month`** — 月总结模式需要上月日期范围，当前缺少直接支持 ✅
- [x] **新增 test_date_utils.py** — date_utils.py 无单元测试，需覆盖：跨年周、闰年、`--prev-week`/`--next-week` 边界等 ✅（30 个测试，全部通过）
- [x] **扩充 routing.md 触发词** — 英文触发词过少，补充中英混合和口语化表达（如「帮我安排明天」「规划下周」「review this week」），可分精确匹配与模糊匹配两层 ✅
- [x] **支持季度/自定义时间范围总结** — 在月总结模式中增加参数支持（如 `monthly-review Q1` 或 `monthly-review 2026-01 to 2026-03`） ✅

#### 🟢 低优先级

- [x] **添加 .gitignore** — 排除 `__pycache__/`、`.DS_Store`、`*.pyc` ✅
- [x] **dedup_todos.py 归一化增加英文括号处理** — 当前只清理中文括号备注 `（.*?）`，英文 `(.*?)` 未处理，导致英文条目去重可能失败 ✅
- [x] **周总结归档功能可拆分** — Step 6 归档逻辑可提取为独立触发命令（如 `归档日志` / `archive daily`），周总结中默认调用但也可单独使用 ✅
- [x] **模板增加可选区块标记** — 用 `<!-- OPTIONAL: 仅在有数据时生成 -->` 标记可省略区块，给 Agent 明确的省略依据 ✅
- [x] **优化 SKILL.md description 触发词** — 补充英文关键词和常见触发场景，提升跨语言触发准确性 ✅

#### 📝 小改进

- [x] conventions.md「临时追加的归属」表格标注写入顺序（「依次写入」或「同时写入」） ✅
- [x] sync-report-template.md 检查范围补充 `tasks/TODO.md` 和年规划字段，与 mode-planning-sync.md 实际检查范围对齐 ✅
- [x] week-template.md 总览表增加「来源」列（来自规划/从上周转移） ✅
- [x] conventions.md 增加版本号或变更日志段落 ✅
