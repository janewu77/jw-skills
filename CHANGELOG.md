# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-02-23

### Added
- **Cascading update mechanism** across all planning levels
  - Top-down cascade (tasks/TODO → monthly → weekly → daily) for planning operations (daily-todo add/move, weekly-plan)
  - Bottom-up cascade (daily → weekly → monthly → yearly) with lightweight status marking for logging operations (daily-log, weekly-review)
  - Cascade mechanism documented in shared `conventions.md` as single source of truth
- **Yearly plan support** (optional): new `yearly/` directory, `YYYY-plan.md` naming, referenced in cascade chains
- **planning-sync** now covers all 5 levels (tasks/TODO, yearly, monthly, weekly, daily) instead of 3
- Cascade summary table in `conventions.md` showing each skill's direction and path

### Changed
- **daily-todo**: Added top-down cascade principle; `mode-add-or-move.md` restructured Step 5 into 5a→5d sub-steps; fixed stale "模式 C/D" references → "添加/移动任务"
- **daily-log**: Added bottom-up cascade (Step 3 restructured into 3a→3d); status sync now covers weekly/monthly/yearly plans
- **weekly-plan**: Added top-down cascade (new Step 6 with 6a→6c); syncs tasks/TODO and existing daily plans
- **weekly-review**: Added bottom-up cascade (new Step 5 with 5a→5c); data source explicitly starts from daily logs; step numbering updated
- **planning-sync**: Expanded from 3-layer to full-level check; description and error handling updated; inter-skill references updated to match new cascade behavior
- All 5 skills bumped to version 0.2.0
- `conventions.md`: Added yearly directory/file naming, cascade mechanism section, yearly entry in conflict resolution table
- README (EN/ZH): Updated workflow diagram, planning-sync description, workspace layout, file naming table, added cascade sync as core feature

## [0.1.2] - 2026-02-09

## [0.1.1] - 2026-02-09

### Added
- Auto-sync feature in CI workflow for `_common/` changes
- Complete example workspace for quick start
- Conversation examples demonstrating usage
- SECURITY.md for vulnerability reporting
- CHANGELOG.md for version history
- CI workflow for running pytest tests
- Python environment documentation
- CODE_OF_CONDUCT.md (Contributor Covenant 2.1)
- GitHub issue and PR templates
- Release process and versioning guidelines
- Cross-platform compatibility documentation
- Badges in README (license, Python version, version)

### Changed
- Improved CONTRIBUTING.md with detailed workflow steps
- Enhanced sync check script with better error messages

## [0.1.0] - 2026-02-09

### Added
- Initial release of jw-agenda skill set
- 5 installable skills:
  - `jw-agenda-daily-todo`: Daily todo management with schedule
  - `jw-agenda-daily-log`: Log and progress reporting
  - `jw-agenda-weekly-plan`: Weekly plan generation from monthly goals
  - `jw-agenda-weekly-review`: Weekly summary and statistics
  - `jw-agenda-planning-sync`: Consistency check across plans
- Common conventions and scripts in `_common/`
- Sync scripts for maintaining consistency across skills
- Unit tests for `date_utils.py` and `dedup_todos.py`
- CI workflow for checking sync status
- Comprehensive documentation (README, CONTRIBUTING)
- Bilingual support (English and Chinese)

### Features
- Natural language interface for agenda management
- Monthly → Weekly → Daily planning workflow
- Automatic schedule generation with time slots
- Progress tracking and completion statistics
- Plan consistency checking
- Local Markdown file storage
- No external dependencies (runtime)

---

## Version History

- **0.1.1**: Documentation and project structure improvements
  - Added CODE_OF_CONDUCT, issue/PR templates
  - Added release process guidelines
  - Added badges and cross-platform docs
  
- **0.2.0**: Cascading update mechanism
  - Top-down cascade for planning, bottom-up for logging
  - Yearly plan support, full-level planning-sync
  - All skills v0.2.0

- **0.1.0**: Initial public release
  - Complete skill set with 5 skills
  - Full documentation
  - Testing infrastructure
  - CI/CD workflows
