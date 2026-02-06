#!/usr/bin/env bash
# Package each skill under skills/ into a zip file under output/

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SCRIPT_DIR}/skills"
OUTPUT_DIR="${SCRIPT_DIR}/output"

mkdir -p "${OUTPUT_DIR}"

for skill_dir in "${SKILLS_DIR}"/*/; do
  [ -d "${skill_dir}" ] || continue
  name="$(basename "${skill_dir}")"
  zip_path="${OUTPUT_DIR}/${name}.zip"
  (cd "${SKILLS_DIR}" && zip -r -q "${zip_path}" "${name}")
  echo "Created: ${zip_path}"
done

echo "Done. Zips are in: ${OUTPUT_DIR}"
