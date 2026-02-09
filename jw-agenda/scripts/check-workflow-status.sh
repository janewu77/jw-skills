#!/usr/bin/env bash
# 本地检查 GitHub Actions 状态（push 后可用此脚本查看是否失败，无需打开网页）
# 依赖：GitHub CLI (gh) 已安装并已登录
# 用法：在 jw-agenda 目录下执行 ./scripts/check-workflow-status.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JW_AGENDA="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${JW_AGENDA}/.." && pwd)"
cd "${REPO_ROOT}"

if ! command -v gh &>/dev/null; then
  echo "GitHub CLI (gh) 未安装。请安装后重试，或手动打开: https://github.com/janewu77/jw-skills/actions"
  echo "  brew install gh   # macOS"
  exit 0
fi

if ! gh auth status &>/dev/null; then
  echo "请先登录 GitHub CLI: gh auth login"
  exit 0
fi

echo "正在检查 GitHub Actions 状态（稍等几秒以便 workflow 已启动）..."
sleep 5

FAILED=0

if ! command -v jq &>/dev/null; then
  echo "未检测到 jq，仅列出最近运行（请安装 jq 以解析状态: brew install jq）"
  gh run list --limit 5
  echo ""
  echo "详情请查看: https://github.com/janewu77/jw-skills/actions"
  exit 0
fi

for WORKFLOW in jw-agenda-check-sync.yml jw-agenda-test.yml; do
  NAME="${WORKFLOW%.yml}"
  RUN=$(gh run list --workflow="$WORKFLOW" --limit 1 --json databaseId,status,conclusion,displayTitle 2>/dev/null || true)
  if [ -z "$RUN" ] || [ "$RUN" == "[]" ]; then
    echo "[$NAME] 暂无运行记录"
    continue
  fi
  STATUS=$(echo "$RUN" | jq -r '.[0].status')
  CONCLUSION=$(echo "$RUN" | jq -r '.[0].conclusion')
  if [ "$CONCLUSION" == "failure" ]; then
    echo "[$NAME] 失败"
    FAILED=1
  elif [ "$CONCLUSION" == "success" ]; then
    echo "[$NAME] 通过"
  else
    echo "[$NAME] 状态: $STATUS (结论: ${CONCLUSION:-进行中})"
  fi
done

if [ $FAILED -eq 1 ]; then
  echo ""
  echo "有 workflow 失败，请查看: https://github.com/janewu77/jw-skills/actions"
  exit 1
fi

echo ""
echo "所有已检查的 workflow 均通过（或暂无运行）。"
exit 0
