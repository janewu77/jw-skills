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

> **⚠️** Source of truth is `_common/`. After changing anything under `_common/`, you must sync changes to all skills' `assets/` directories.
>
> **🔄 Auto-sync**: When pushing to `main` or `dev`, GitHub Actions will automatically sync and commit changes if needed. For pull requests, you must sync manually before pushing.

### Workflow: Modifying `_common/` files

When you modify files in `_common/` (e.g., `conventions.md`, `schedule-config.example.md`, or scripts), follow this workflow:

#### Step 1: Before committing — Check sync status

First, verify if there are any existing sync issues:

```bash
cd jw-agenda
./scripts/check-common-sync.sh
```

- ✅ **If it passes**: All skills are in sync, proceed to modify `_common/` files.
- ❌ **If it fails**: Fix existing sync issues first before making new changes.

#### Step 2: Make your changes

Edit files in `_common/` as needed:
- `_common/conventions.md`
- `_common/schedule-config.example.md`
- `_common/scripts/*.py`
- `_common/scripts/LICENSE`

#### Step 3: Sync changes to all skills

After modifying `_common/`, sync the changes to all 5 skills:

```bash
cd jw-agenda
./scripts/sync-common-to-skills.sh
```

This copies updated files from `_common/` to each skill's `assets/` directory.

> **Note**: If you're pushing directly to `main` or `dev`, GitHub Actions will auto-sync and commit if you forget. However, it's still recommended to sync locally before pushing to keep your commit history clean.

#### Step 4: Verify sync (before committing)

Run the check script again to ensure everything is synchronized:

```bash
./scripts/check-common-sync.sh
```

Expected output: `✓ All skills are in sync with _common/`

#### Step 5: Commit all changes

Commit both `_common/` changes and the synchronized `skills/*/assets/` files:

```bash
git add jw-agenda/_common/
git add jw-agenda/skills/*/assets/
git commit -m "Your commit message"
git push
```

#### Step 6: After pushing — Verify CI status

After pushing, check GitHub Actions to ensure the CI check passed:

1. **Via GitHub web UI**:
   - Go to: `https://github.com/janewu77/jw-skills/actions`
   - Find the latest workflow run for "Check Common Sync"
   - Verify it shows ✅ (green checkmark)
   - If you pushed to `main`/`dev` without syncing, the workflow will auto-sync and create a commit

2. **Via GitHub CLI** (if installed):
   ```bash
   gh run list --workflow=check-sync.yml --limit 5
   gh run view <run-id>  # View details of a specific run
   ```

**Auto-sync behavior**:
- ✅ **Push to `main`/`dev`**: If sync is needed, GitHub Actions will automatically sync and commit
- ❌ **Pull Requests**: Must sync manually; CI will fail if out of sync (for review purposes)

### Quick reference

```bash
# Check sync status
./scripts/check-common-sync.sh

# Sync _common → each skill assets/
./scripts/sync-common-to-skills.sh

# Verify again before committing
./scripts/check-common-sync.sh
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
