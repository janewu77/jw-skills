# jw-agenda-v2 Skill Review

整体来看，这是一个结构完整、覆盖面广的日程管理 skill（6 种模式 + 子模式），文档质量不错。以下是分类优化建议：

---

## 1. 格式不一致（优先级高）

| 问题 | 位置 | 建议 |
|------|------|------|
| **状态标记不统一** | `week-template.md` 用 emoji（✅⬜❌），`daily-todo-template.md` 用 checkbox（`[x]`/`[ ]`） | 统一为一种，或在 conventions-marks.md 明确说明：周级用 emoji、日级用 checkbox |
| **日期格式混用** | `*(moved from M.D)*` 用 `2.5` 格式，但文件命名用 `YYYY-MM-DD` | 在 `conventions-marks.md` 明确 M.D = 月.日简写，仅用于标记，非文件名 |
| **`{{ACTUAL_WORK_TIME}}`** | 同名变量在 daily log 和 monthly review 模板中含义不同（日 vs 月汇总） | 月度模板改为 `{{TOTAL_WORK_TIME}}` 或加注释说明 |

---

## 2. 模糊定义需要量化（优先级高）

- **"大任务拆分为 2–3 天子任务"**（`mode-weekly-plan.md:36`）— 什么算"大"？建议加标准，如 "预计耗时 > 4 小时"
- **去重逻辑**：多处提到 "normalized comparison" 但未定义具体算法。建议在 `conventions.md` 加一节，明确：去除标记 → 去除首尾空格 → 大小写不敏感 → 子串匹配
- **Planning Sync 的关键词匹配**（`mode-planning-sync.md:48`）— "one contains the other's key substring" 太宽松，容易误报。建议改为"去标记后文本完全相同 OR 用户确认"

---

## 3. 结构 / 架构优化

**归档应独立为子模式**：`mode-weekly-review.md` Step 6（Archive）说可以独立触发，但写在 weekly review 里。建议：
- 在 SKILL.md 的触发表中把 Archive Logs 指向独立文件 `references/mode-archive.md`（而不是 "Step 6 only"）
- 或在 mode-weekly-review.md 里将归档逻辑 extract 到一个 include/共享片段

**Add/Move 子模式的入口不清晰**：`mode-daily-todo.md` Sub-mode C 只有 3 行就跳转到 mode-add-or-move.md。建议在 Sub-mode C 处加一句话总结做什么，再跳转，而不是突然切换文档。

---

## 4. 可选节的处理矛盾

- `review-template.md` 标注 Carry Over 为 optional，但 mode-weekly-review.md 的流程总是包含它 → **统一为"无 carry-over 项时省略该节"**
- `monthly-review-template.md:9` Goal Achievement 标注 "monthly plan 不存在时跳过"，但 mode-monthly-review.md Step 2 说 "问用户是否生成骨架" → **选一个策略，保持一致**

---

## 5. 模板补充

- **`{{SCHEDULE_TABLE}}`**（`daily-todo-template.md`）：应展示期望的表结构（Time | Activity | Notes），而不是一个黑盒占位符
- **`{{ACTION_ITEMS}}` / `{{INFO_ITEMS}}`**（`sync-report-template.md`）：缺少格式示例，建议加一个 2-3 行的 example block
- **Source legend**（daily-todo-template.md）：只列了 2 个标记，但 conventions-marks.md 定义了 6 个 → 补全或注明"完整列表见 conventions-marks.md"

---

## 6. 小改进

- `conventions.md:76` 引用了 `scripts/date_utils.py`，但 skill 中没有这个文件 → 去掉引用或创建该脚本
- `template-conventions.md` 规则说 "full words, not abbreviations" 但自己用了 `{{WEEK_NUM}}`（NUM 是缩写）→ 改规则或改变量名
- `schedule-config.example.md` 午餐 30 分钟、晚餐 2 小时，不太合理 → 调整示例或注明仅为示意
- Quarter 流程（`mode-monthly-review.md:13-28`）嵌在 Step 1 中间，打断主流程 → 拆为 "Step 1a: 标准月度" 和 "Step 1b: 季度/多月"

---

## 总结优先级

| 优先级 | 动作 |
|--------|------|
| **P0** | 统一状态标记体系（emoji vs checkbox）、明确去重算法 |
| **P1** | 补全模板示例（schedule table、sync report items）、解决 optional 节矛盾 |
| **P2** | 归档独立化、Quarter 流程拆分、脚本引用清理 |
