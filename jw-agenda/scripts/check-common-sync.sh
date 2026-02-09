#!/usr/bin/env bash
# 检查 _common/ 与各 skill 的 assets/ 是否一致。
# 用于验证 sync-common-to-skills.sh 是否已正确执行。

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JW_AGENDA="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMMON="${JW_AGENDA}/_common"
SKILLS_DIR="${JW_AGENDA}/skills"

ERRORS=0

# 检查单个文件是否一致
check_file() {
  local common_file="$1"
  local skill_file="$2"
  local skill_name="$3"
  
  if [ ! -f "$common_file" ]; then
    echo "ERROR: Source file not found: $common_file" >&2
    return 1
  fi
  
  if [ ! -f "$skill_file" ]; then
    echo "ERROR [$skill_name]: Missing file: $skill_file" >&2
    return 1
  fi
  
  if ! cmp -s "$common_file" "$skill_file"; then
    echo "ERROR [$skill_name]: Files differ:" >&2
    echo "  Source: $common_file" >&2
    echo "  Target: $skill_file" >&2
    echo "  Diff:" >&2
    diff -u "$common_file" "$skill_file" | head -20 >&2
    return 1
  fi
  
  return 0
}

# 检查所有 skill
for skill_dir in "${SKILLS_DIR}"/*/; do
  [ -d "${skill_dir}" ] || continue
  skill_name="$(basename "${skill_dir}")"
  assets="${skill_dir}/assets"
  
  # 检查 conventions.md
  if ! check_file "${COMMON}/conventions.md" "${assets}/conventions.md" "$skill_name"; then
    ERRORS=$((ERRORS + 1))
  fi
  
  # 检查 schedule-config.example.md
  if ! check_file "${COMMON}/schedule-config.example.md" "${assets}/schedule-config.example.md" "$skill_name"; then
    ERRORS=$((ERRORS + 1))
  fi
  
  # 检查 scripts 目录下的文件
  if [ ! -d "${assets}/scripts" ]; then
    echo "ERROR [$skill_name]: Missing directory: ${assets}/scripts" >&2
    ERRORS=$((ERRORS + 1))
    continue
  fi
  
  # 检查每个 Python 文件
  for py_file in "${COMMON}/scripts/"*.py; do
    [ -f "$py_file" ] || continue
    py_name="$(basename "$py_file")"
    if ! check_file "$py_file" "${assets}/scripts/${py_name}" "$skill_name"; then
      ERRORS=$((ERRORS + 1))
    fi
  done
  
  # 检查 LICENSE
  if [ -f "${COMMON}/scripts/LICENSE" ]; then
    if ! check_file "${COMMON}/scripts/LICENSE" "${assets}/scripts/LICENSE" "$skill_name"; then
      ERRORS=$((ERRORS + 1))
    fi
  fi
done

if [ $ERRORS -eq 0 ]; then
  echo "✓ All skills are in sync with _common/"
  exit 0
else
  echo "" >&2
  echo "✗ Found $ERRORS error(s). Please run ./scripts/sync-common-to-skills.sh to sync changes." >&2
  exit 1
fi
