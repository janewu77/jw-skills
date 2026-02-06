#!/usr/bin/env bash
# 将 _common/ 下的 conventions、schedule 模板、scripts 同步到各 skill 的 assets/。
# 修改 _common 后执行本脚本，再提交，以保持 5 个 Skill 内容一致。

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JW_AGENDA="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMMON="${JW_AGENDA}/_common"
SKILLS_DIR="${JW_AGENDA}/skills"

for skill_dir in "${SKILLS_DIR}"/*/; do
  [ -d "${skill_dir}" ] || continue
  name="$(basename "${skill_dir}")"
  assets="${skill_dir}/assets"
  mkdir -p "${assets}/scripts"
  cp "${COMMON}/conventions.md" "${assets}/"
  cp "${COMMON}/schedule-config.example.md" "${assets}/"
  cp "${COMMON}/scripts/"*.py "${COMMON}/scripts/"LICENSE "${assets}/scripts/"
  echo "Synced: ${name}"
done

echo "Done. All skills updated from _common/."
