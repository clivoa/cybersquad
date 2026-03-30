# Contributing to CyberSquad

CyberSquad should stay practical, lightweight, and easy to onboard.

Source of truth:

- `personas.yaml` in repo root is the canonical persona catalog.
- `src/cybersquad/template/personas.yaml` is generated/synced for packaging.

## Golden Rule

Add capability without adding friction.

Prefer:

- Better prompts
- Better persona design
- Better runbooks
- Better validation and onboarding

Avoid:

- Heavy infrastructure
- Complex runtime dependencies
- Breaking simple file-based workflow

## Common contributions

- Persona updates in `personas.yaml` (then regenerate prompt artifacts)
- Curated prompt edits in `prompts/persona-prompts.md`
- Auto-generated persona usage prompts in `prompts/persona-prompts.generated.md`
- Per-persona generated prompts in `prompts/personas/`
- New scenario templates in `prompts/`
- New study templates in `prompts/study-*.md`
- Better skill loops in `prompts/persona-skill-upgrades.md`
- CLI improvements in `src/cybersquad/cli.py`
- Prompt generation logic in `src/cybersquad/promptgen.py`
- Persona parser in `src/cybersquad/personas.py`
- Workspace lifecycle in `src/cybersquad/workspace.py`
- Ralph loop runtime in `src/cybersquad/loops.py` and `src/cybersquad/template/.agents/ralph/`
- Documentation and onboarding improvements

## Prompt change flow

1. Edit source files in root:
   - `personas.yaml`
   - `prompts/*.md`
2. Regenerate prompt artifacts in workspace source:
   - `cybersquad generate prompts --workspace . --overwrite`
3. Sync template from source files:
   - `cybersquad sync-template --repo-root . --overwrite`
4. Test CLI:
   - `./bin/cybersquad list personas --from-template`
   - `./bin/cybersquad init /tmp/cybersquad-test --force`
   - `./bin/cybersquad doctor --workspace /tmp/cybersquad-test`
   - `./bin/cybersquad loop doctor --workspace /tmp/cybersquad-test`
   - `./bin/cybersquad loop overview --workspace /tmp/cybersquad-test`
   - `./bin/cybersquad loop build --workspace /tmp/cybersquad-test --iterations 1 --dry-run --no-commit`

Notes:

- Generated persona prompt artifacts are created during `cybersquad init`.
- Template sync excludes generated artifacts (`persona-prompts.generated.md` and `prompts/personas/`) to avoid duplicated tracked files.

Windows maintainers can run:

- `py -m cybersquad sync-template --repo-root . --overwrite`

## Release checklist

1. Bump version in:
   - `pyproject.toml`
   - `src/cybersquad/__init__.py`
   - `src/cybersquad/template/_cybersquad/.cybersquad-version`
2. Run local install test
3. Publish package or tag release
