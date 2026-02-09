# Maintenance

**Language**: English is authoritative. 中文见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md).

---

## Running tests

- **Prerequisites**: Python 3.9+, `pip install pytest`
- **Run** (from repo root or `jw-agenda`):

```bash
pytest jw-agenda/tests/ -v   # or: cd jw-agenda && pytest tests/ -v
```

## Keeping all 5 Skills in sync

> **⚠️** Source of truth is `_common/`. After changing anything under `_common/`, run `./scripts/sync-common-to-skills.sh` and commit both `_common/` and updated `skills/*/assets/`. CI will fail if out of sync.

```bash
./scripts/sync-common-to-skills.sh   # sync _common → each skill assets/
./scripts/check-common-sync.sh       # verify (also run in CI)
```

## Packaging (zips)

From **jw-agenda** (run sync first if needed):

```bash
./package-skills.sh
```

Output: one zip per skill under `output/`.

## Versioning

- **Paths**: `assets/conventions.md` — monthly `YYYY-MM-plan.md`, weekly `Week{N}-plan.md`, `Week{N}-review.md`. Conventions win over skill docs.
- **SKILL.md**: `version` format `0.M.P` — patch for single-skill change; minor for coordinated release (e.g. 0.1.0).

## Before you commit

```bash
pytest tests/ -v
./scripts/sync-common-to-skills.sh   # if you changed _common/
./scripts/check-common-sync.sh
```
