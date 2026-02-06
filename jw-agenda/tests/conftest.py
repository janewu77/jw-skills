"""Pytest conftest: ensure date_utils/dedup_todos are importable from _common/scripts/."""
import sys
from pathlib import Path

# jw-agenda/tests/conftest.py → jw-agenda/_common/scripts
_scripts_dir = Path(__file__).resolve().parent.parent / "_common" / "scripts"
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))
