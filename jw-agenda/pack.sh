#!/usr/bin/env bash
# 在 jw-agenda 目录下执行，于上级目录生成 jw-agenda-<版本号>.zip，便于分发给他人使用。
# 用法: ./pack.sh [版本号]  默认版本号 0.0.1

VERSION="${1:-0.0.1}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
NAME="$(basename "$SCRIPT_DIR")"

cd "$PARENT_DIR" || exit 1
zip -r "${NAME}-${VERSION}.zip" "$NAME" \
  -x "*.git*" \
  -x "*__pycache__*" \
  -x "*.DS_Store" \
  -x "*.zip"

echo "已生成: $PARENT_DIR/${NAME}-${VERSION}.zip"
