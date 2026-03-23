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
