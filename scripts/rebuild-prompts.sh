#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${REPO_ROOT}/scripts/generate-usage-prompts.sh"
"${REPO_ROOT}/scripts/sync-template.sh"

echo
echo "Prompt artifacts regenerated (workspace) and template synced (source-only)."
