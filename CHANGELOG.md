# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
  
- **0.1.0**: Initial public release
  - Complete skill set with 5 skills
  - Full documentation
  - Testing infrastructure
  - CI/CD workflows
