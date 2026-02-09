#!/usr/bin/env bash
# Package each skill under skills/ into a zip file under output/

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SCRIPT_DIR}/skills"
OUTPUT_DIR="${SCRIPT_DIR}/output"

if [ ! -d "${SKILLS_DIR}" ]; then
  echo "Error: SKILLS_DIR does not exist: ${SKILLS_DIR}" >&2
  exit 1
fi

mkdir -p "${OUTPUT_DIR}"
echo "Packaging skills from: ${SKILLS_DIR}"
echo "Output directory: ${OUTPUT_DIR}"

for skill_dir in "${SKILLS_DIR}"/*/; do
  [ -d "${skill_dir}" ] || continue
  name="$(basename "${skill_dir}")"
  zip_path="${OUTPUT_DIR}/${name}.zip"
  (cd "${SKILLS_DIR}" && zip -r "${zip_path}" "${name}")
  echo "Created: ${zip_path}"
done

echo "Done. Zips are in: ${OUTPUT_DIR}"
