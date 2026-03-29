$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$env:PYTHONPATH = "$repoRoot\src;$env:PYTHONPATH"

python -m cybersquad generate prompts --workspace $repoRoot --overwrite
python -m cybersquad sync-template --repo-root $repoRoot --overwrite
Write-Host "`nPrompt artifacts regenerated (workspace) and template synced (source-only)."
