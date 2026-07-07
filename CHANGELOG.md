# Changelog

This repository hosts **independently versioned skill sets** — there is no single repo-wide version. Each skill set maintains its own changelog and Git tags:

| Skill set | Changelog | Tag prefix |
|-----------|-----------|------------|
| [jw-agenda](jw-agenda/) (5 modular skills) | [jw-agenda/CHANGELOG.md](jw-agenda/CHANGELOG.md) | `jw-agenda-vX.Y.Z` |
| [jw-agenda-v2](jw-agenda-v2/) (single skill, 6 modes) | [jw-agenda-v2/doc/CHANGELOG.md](jw-agenda-v2/doc/CHANGELOG.md) | `jw-agenda-v2-vX.Y.Z` |

See [CONTRIBUTING.md](CONTRIBUTING.md) → *Versioning* for how versions and tags are managed.

Repo-level infrastructure changes (licenses, CI, top-level docs) that don't belong to any single skill set are recorded below.

## Repo infrastructure

- 2026-07: Switched to per-skill-set versioning; moved the former repo-level changelog (jw-agenda history) to `jw-agenda/CHANGELOG.md`; removed the single repo version badge.
