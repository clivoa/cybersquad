#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE="${1:-${REPO_ROOT}}"

"${REPO_ROOT}/bin/cybersquad" generate prompts \
  --workspace "${WORKSPACE}" \
  --output "prompts/persona-prompts.generated.md" \
  --per-persona-dir "prompts/personas" \
  --overwrite

echo
echo "Generated usage prompts in ${WORKSPACE}/prompts"
