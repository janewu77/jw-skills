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

## Release process and versioning

### Version numbering

This repository follows [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH):

- **Repository-level version**: Tracked in `CHANGELOG.md` (e.g., `0.1.0`)
- **Skill set version**: For skill sets like `jw-agenda`, the version matches the repository version
- **Individual skill version**: Each skill’s `SKILL.md` metadata includes a `version` field (e.g., `version: "0.1.0"`)

**Version alignment**: When releasing a new version:
1. Update `CHANGELOG.md` with the new version and changes
2. Update all skill `SKILL.md` metadata `version` fields to match
3. Update skill set-level version (if applicable) to match

### Versioning & tagging

This repo does **not** use GitHub Releases. Distribution is source-based: users clone the repo and copy the skill folders (see each README's install section). Versions are tracked in `CHANGELOG.md`, in each skill's `SKILL.md` metadata, and with Git tags.

To publish a new version:

1. **CHANGELOG**: Update `CHANGELOG.md` with the new version and changes.
2. **Skill versions**: Bump the `version` field in every affected skill's `SKILL.md` metadata to match.
3. **Commit & tag**: Commit, then create a Git tag matching the version (e.g., `v0.1.0`).

### Example versioning workflow

```bash
# 1. Update CHANGELOG.md with the new version
# 2. Update all affected skill SKILL.md version fields
# 3. Commit changes
git add CHANGELOG.md jw-agenda/skills/*/SKILL.md
git commit -m "chore: bump version to 0.2.0"

# 4. Create and push the tag
git tag -a v0.2.0 -m "v0.2.0"
git push origin v0.2.0
```

*(Optional: to hand someone a single bundle instead of the repo, run `./jw-agenda/package-skills.sh` to build local zips under `jw-agenda/output/`.)*
