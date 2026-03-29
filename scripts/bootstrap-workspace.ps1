param(
    [string]$TargetDir = ".\my-cybersquad"
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$env:PYTHONPATH = "$repoRoot\src;$env:PYTHONPATH"

python -m cybersquad init $TargetDir
Write-Host "`nWorkspace ready at $TargetDir"
Write-Host "Open $TargetDir\prompts\master-prompt.md to begin."
