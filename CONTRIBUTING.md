# Contributing

**Language**: This document is the authoritative version in English. For a Chinese version, see [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md).

---

This repository contains multiple Agent Skills. Before submitting code or documentation, please note:

- **Repository-level**: Licenses and norms are in this file and the root [LICENSE](LICENSE), [LICENSE-CODE](LICENSE-CODE), [LICENSE-DOCS](LICENSE-DOCS).
- **Commit messages**: Use English for commit messages.
- **Per-skill notes**: If a skill has its own maintenance or development conventions, read that skill’s `CONTRIBUTING.md` first.

## Cross-platform compatibility

### Scripts

- **Bash scripts** (`sync-common-to-skills.sh`, `package-skills.sh`): Require Bash shell. On Windows, use **WSL** (Windows Subsystem for Linux) or **Git Bash**. These scripts are primarily for maintainers and are not required for end users.
- **Python scripts** (`date_utils.py`, `dedup_todos.py`): Can run independently on Windows, macOS, and Linux. Require Python 3.9+.

### Development environment

- **Linux/macOS**: Native Bash support; scripts run directly.
- **Windows**: 
  - Use WSL or Git Bash for running Bash scripts
  - Python scripts can run directly via `python` or `python3` command
  - CI workflows run on Linux runners, so Windows-specific issues may need testing in WSL

## Per-skill contributing

| Skill | Notes |
|-------|-------|
| [jw-agenda](jw-agenda/CONTRIBUTING.md) | After changing conventions or scripts, sync to all sub-skills; see its maintenance notes. |

When adding new skills that require special attention from contributors, extend this table and point to each skill’s `CONTRIBUTING.md`.

## Versioning

This is a **monorepo of independently versioned skill sets**. There is **no repo-wide version** — each skill set has its own version, its own changelog, and its own Git tags. This lets `jw-agenda` and `jw-agenda-v2` evolve at their own pace (they currently sit at different versions).

Each skill set follows [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH):

| Skill set | Version source | Changelog | Tag prefix |
|-----------|----------------|-----------|------------|
| **jw-agenda** (5 skills) | one shared **set version** across all 5 `SKILL.md` files | [jw-agenda/CHANGELOG.md](jw-agenda/CHANGELOG.md) | `jw-agenda-vX.Y.Z` |
| **jw-agenda-v2** (1 skill) | the skill's own `SKILL.md` `version` | [jw-agenda-v2/doc/CHANGELOG.md](jw-agenda-v2/doc/CHANGELOG.md) | `jw-agenda-v2-vX.Y.Z` |

For **jw-agenda**, the 5 skills share one set version and are bumped together. For **jw-agenda-v2** (a single skill), its `SKILL.md` version *is* the set version. The root [CHANGELOG.md](CHANGELOG.md) is only an index plus repo-level infrastructure notes; it carries no version number.

We do **not** use GitHub Releases — distribution is source-based (clone the repo, copy the skill folder; see each README's install section).

### Publishing a new version

Work on **one skill set at a time**:

1. **Changelog**: Move that set's `## Unreleased` entries into a new `## X.Y.Z — YYYY-MM-DD` section in *its* changelog.
2. **Skill version(s)**: Bump the `version` field in that set's `SKILL.md`(s) — all 5 for jw-agenda, or the one file for jw-agenda-v2.
3. **Commit & tag**: Commit, then create a prefixed Git tag for that set.

**Example — releasing jw-agenda-v2 1.4.0:**

```bash
# 1. In jw-agenda-v2/doc/CHANGELOG.md, turn "## Unreleased" into "## 1.4.0 — 2026-07-08"
# 2. Bump version in jw-agenda-v2/skills/jw-agenda-v2/SKILL.md to "1.4.0"
# 3. Commit
git add jw-agenda-v2/doc/CHANGELOG.md jw-agenda-v2/skills/jw-agenda-v2/SKILL.md
git commit -m "release(jw-agenda-v2): 1.4.0"

# 4. Tag (note the skill-set prefix)
git tag -a jw-agenda-v2-v1.4.0 -m "jw-agenda-v2 1.4.0"
git push origin jw-agenda-v2-v1.4.0
```

**Example — releasing jw-agenda 0.3.0:** same steps, but update `jw-agenda/CHANGELOG.md`, bump **all 5** `jw-agenda/skills/*/SKILL.md`, and tag `jw-agenda-v0.3.0`.

*(Optional: to hand someone a single bundle instead of the repo, run `./jw-agenda/package-skills.sh` to build local zips under `jw-agenda/output/`.)*
