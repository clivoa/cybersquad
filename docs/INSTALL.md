# Installation and Distribution

## Requirements

- Python 3.10+
- Windows, macOS, or Linux

## Install methods

### 1) From local clone

```bash
git clone <your-repo-url>
cd cybersquad
python3 -m pip install .
cybersquad version
```

Windows:

```powershell
git clone <your-repo-url>
cd cybersquad
py -m pip install .
py -m cybersquad version
```

### 2) Editable install (for maintainers)

```bash
python3 -m pip install -e .
cybersquad version
```

If editable install fails due older `pip`, either:

```bash
python3 -m pip install --upgrade pip
```

or use standard install:

```bash
python3 -m pip install .
```

Windows:

```powershell
py -m pip install -e .
py -m cybersquad version
```

### 3) Direct from GitHub

```bash
python3 -m pip install "git+https://github.com/your-org/cybersquad.git"
cybersquad version
```

Windows:

```powershell
py -m pip install "git+https://github.com/your-org/cybersquad.git"
py -m cybersquad version
```

## Bootstrap a workspace

```bash
cybersquad init ./my-cybersquad
```

macOS/Linux helper script (local repo):

```bash
./scripts/bootstrap-workspace.sh ./my-cybersquad
```

Windows:

```powershell
py -m cybersquad init .\my-cybersquad
```

## Validate workspace

```bash
cd ./my-cybersquad
cybersquad doctor
```

Windows:

```powershell
py -m cybersquad doctor
```

macOS/Linux:

```bash
python3 -m cybersquad doctor --workspace ./my-cybersquad
```

## Generate usage prompts

```bash
cd ./my-cybersquad
cybersquad generate prompts --workspace . --overwrite
```

Windows:

```powershell
py -m cybersquad generate prompts --workspace . --overwrite
```

macOS/Linux helper script:

```bash
./scripts/generate-usage-prompts.sh .
```

## macOS/Linux helper scripts (repo maintainers)

- `./scripts/bootstrap-workspace.sh`
- `./scripts/generate-usage-prompts.sh`
- `./scripts/sync-template.sh`
- `./scripts/rebuild-prompts.sh`

## Windows helper scripts (repo maintainers)

PowerShell helpers:

- `.\scripts\bootstrap-workspace.ps1`
- `.\scripts\generate-usage-prompts.ps1`
- `.\scripts\sync-template.ps1`
- `.\scripts\rebuild-prompts.ps1`

If PowerShell blocks script execution, run once in your session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Upgrade strategy

Current versioning is file-based:

- Workspace version marker: `_cybersquad/.cybersquad-version`
- Package version: `pyproject.toml`

For updates:

1. Upgrade installed package
2. Re-run `cybersquad init <workspace> --force`
3. Re-apply local customizations if needed
