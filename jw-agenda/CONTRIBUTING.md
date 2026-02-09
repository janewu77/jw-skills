# Maintenance

**Language**: This document is the authoritative version in English. For a Chinese version, see [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md).

---

## Running tests

### Prerequisites

- **Python 3.9+** (scripts use type hints such as `list[str]`)
- **pytest**: `pip install pytest`

### How to run tests

From the repo root or from this directory (jw-agenda):

```bash
# From repo root
pytest jw-agenda/tests/ -v

# Or from jw-agenda
cd jw-agenda
pytest tests/ -v
```

Tests live in `jw-agenda/tests/` and currently include `test_date_utils.py` (date_utils) and `test_dedup_todos.py` (dedup_todos). `conftest.py` adds `_common/scripts` to the Python path so scripts can be imported without extra setup.

## Keeping all 5 Skills in sync after changing conventions or scripts

The **single source** for conventions, schedule template (`schedule-config.example`), and scripts (`date_utils.py`, `dedup_todos.py`) is `_common/`. After changing any file under `_common/`, run:

```bash
./scripts/sync-common-to-skills.sh
```

The script syncs `_common/` into each skill’s `assets/` (conventions.md, schedule-config.example.md, scripts/). When committing, include both `_common/` and the updated skill `assets/` changes.

## Packaging and release (generating zips)

To distribute or release the skill set as zips, run from the **jw-agenda directory**:

```bash
./package-skills.sh
```

The script produces one zip per skill under `output/`. Before running it, ensure you have run `./scripts/sync-common-to-skills.sh` so each skill’s `assets/` matches `_common/`.

## Versioning and maintenance

- **Naming and paths**: Follow each Skill’s `assets/conventions.md` (or this repo’s `_common/conventions.md`): monthly `YYYY-MM-plan.md`, weekly `Week{N}-plan.md`, weekly review `Week{N}-review.md`. If a Skill’s docs disagree with conventions, conventions win.
- **Skill version**: Each Skill’s SKILL.md has `author: Jing Wu`, `version`, and `updated`. Version format `0.M.P`: for a single-skill change bump patch (e.g. 0.0.1 → 0.0.2); for a **coordinated release** bump minor for all skills (e.g. 0.1.0) so the set ships together.

## Before you commit

From this directory (jw-agenda):

```bash
pytest tests/ -v
./scripts/sync-common-to-skills.sh
```

Ensure tests pass and `_common/` changes are synced to all skill `assets/` before committing.
