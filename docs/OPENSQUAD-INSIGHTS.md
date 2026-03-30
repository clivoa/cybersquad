# Opensquad-Inspired Improvements Applied to CyberSquad

This document records what was borrowed from `opensquad` and how it was adapted for cybersecurity workflows.

## What we adopted

| Idea from opensquad | Applied in cybersquad | Benefit |
|---|---|---|
| `init` command for fast bootstrap | `cybersquad init <path>` | Faster onboarding with one command |
| Template-based installation | `src/cybersquad/template/` | Consistent workspace structure |
| Internal versioned folder (`_opensquad`) | `_cybersquad/` | Clear internal state and upgrade marker |
| File-first architecture | Prompt files + YAML personas | Easy customization, low infrastructure cost |
| CLI discoverability | `list`, `doctor`, `version` commands | Better usability for non-maintainers |
| Opinionated docs and contribution path | README + INSTALL + USAGE + CONTRIBUTING | Easier adoption and community contribution |
| Prompt-driven extensibility | Generated persona prompts + study templates | Faster onboarding for operations and learning |
| File-based iterative loops (Ralph-inspired) | `.agents/ralph` + `.ralph` + `cybersquad loop ...` | Repeatable one-story iterations with durable memory |

## What we intentionally did not copy

- Heavy runtime dependencies
- Dashboard/frontend runtime
- Multi-agent orchestration engine complexity

CyberSquad focuses on practical, prompt-first cybersecurity operations with lightweight tooling.

Current scope now explicitly includes:

- Day-to-day operations (triage, IR, vulnerability, cloud, compliance)
- Study workflows (multi-role attack/defense learning perspectives)
- Cross-platform usage (Windows, macOS, Linux)

## Next improvements suggested

1. Add `cybersquad update` with merge-safe workspace upgrades.
2. Add `cybersquad validate-prompts` for schema/style checks.
3. Add language packs (`en-US`, `es-ES`, `fr-FR`) for prompt output defaults.
4. Publish to PyPI for simpler global install.
