# Changelog

## v1.2.0 — 2026-03-23

- 增加级联同步标准步骤（从下往上/从上往下），各 mode 文件改为引用
- 扩充路由触发词（中英文口语化表达，精确/模糊两层匹配）
- 月总结支持季度（Q1–Q4）及自定义时间范围
- 添加 .gitignore、tests/ 目录及 46 个单元测试
- 模板增加 OPTIONAL 可选区块标记
- conventions.md 精简：迁移仅单模式使用的章节至对应文件

## v1.1.0 — 2026-03-23

- 修复 conventions.md 脚本路径（`assets/scripts/` → `scripts/`）
- 统一模式编号（规划同步=六，月总结=五）
- date_utils.py 新增 `--prev/next-week`、`--prev/next-month`、`--tomorrow`
- 整合 conventions.md 配置表格；添加来源标记优先级说明
- mode-add-or-move.md 补充错误处理段落

## v1.0.0 — 2026-03-01

- 初始版本，包含六个模式：每日 Todo、每日日志、周规划、周总结、月总结、规划同步
