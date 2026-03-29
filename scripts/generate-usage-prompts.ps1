$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$env:PYTHONPATH = "$repoRoot\src;$env:PYTHONPATH"

python -m cybersquad generate prompts --workspace $repoRoot --overwrite
Write-Host "`nGenerated usage prompts in $repoRoot\prompts"
