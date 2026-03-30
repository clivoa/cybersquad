# CyberSquad Ralph Loop

This folder contains a Ralph-style loop runtime adapted for CyberSquad workflows.

Core files:
- `loop.sh`: iteration loop runtime (one story per iteration)
- `PROMPT_build.md`: build prompt template for each run
- `config.sh`: optional overrides
- `agents.sh`: agent command map (codex/claude/droid/opencode)
- `references/`: guardrails and context engineering references

Default PRD path:
- `.agents/tasks/prd.json`

Run manually:

```bash
bash .agents/ralph/loop.sh build 1
```

Use CyberSquad CLI wrappers (recommended):

```bash
cybersquad loop doctor --workspace .
cybersquad loop overview --workspace .
cybersquad loop build --workspace . --iterations 1 --agent codex --no-commit
```
