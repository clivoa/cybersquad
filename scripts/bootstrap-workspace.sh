#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-./my-cybersquad}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${REPO_ROOT}/bin/cybersquad" init "${TARGET_DIR}"

echo
echo "Workspace ready at ${TARGET_DIR}"
echo "Open ${TARGET_DIR}/prompts/master-prompt.md to begin."
