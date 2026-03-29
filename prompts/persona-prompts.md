# Cyber Squad: Persona Prompts (Curated)

This file is intentionally short and complements the generated artifacts.

Primary sources for persona usage prompts:
- `persona-prompts.generated.md` (auto-generated)
- `personas/*.md` (one file per persona)

Regenerate after updating `personas.yaml`:

```bash
cybersquad generate prompts --workspace . --overwrite
```

## Usage tips

- Start from the generated persona prompt.
- Add concrete operational context (asset, time window, impact).
- Always include "Decision needed".
- Use multi-role collaboration only when risk justifies it.
