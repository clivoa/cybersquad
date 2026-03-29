$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$env:PYTHONPATH = "$repoRoot\src;$env:PYTHONPATH"

python -m cybersquad sync-template --repo-root $repoRoot --overwrite
