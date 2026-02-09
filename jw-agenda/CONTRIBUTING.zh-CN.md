# 维护说明

**语言**：中文版。英文版见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 运行测试

- **环境**：Python 3.9+，`pip install pytest`
- **执行**（在仓库根或 `jw-agenda` 下）：

```bash
pytest jw-agenda/tests/ -v   # 或：cd jw-agenda && pytest tests/ -v
```

## 保持 5 个 Skill 一致

> **⚠️** 唯一来源是 `_common/`。修改 `_common/` 后必须执行 `./scripts/sync-common-to-skills.sh`，并同时提交 `_common/` 与各 skill 的 `assets/`。未同步会导致 CI 失败。

```bash
./scripts/sync-common-to-skills.sh   # 将 _common 同步到各 skill assets/
./scripts/check-common-sync.sh       # 校验（CI 也会执行）
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
pytest tests/ -v
./scripts/sync-common-to-skills.sh   # 若改过 _common/
./scripts/check-common-sync.sh
```
