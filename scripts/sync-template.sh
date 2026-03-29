#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${REPO_ROOT}/bin/cybersquad" sync-template --repo-root "${REPO_ROOT}" --overwrite
