# Cyber Squad Prompt Library

This folder contains ready-to-use prompt templates for common day-to-day cybersecurity operations.

## Files
- `master-prompt.md`: Reusable wrapper with role auto-selection guidance.
- `persona-prompts.md`: Curated guidance and usage notes.
- `persona-prompts.generated.md`: Auto-generated usage prompts from `personas.yaml` (generated during `cybersquad init` or `cybersquad generate prompts`).
- `persona-skill-upgrades.md`: Continuous skill improvement playbook per persona.
- `triage.md`: Fast alert triage and severity decisions.
- `incident.md`: Incident containment, eradication, and recovery planning.
- `vuln-prioritization.md`: Risk-based remediation prioritization.
- `threat-hunting.md`: Hypothesis-driven proactive hunting workflow.
- `detection-validation.md`: Detection QA and validation workflow before release.
- `cloud-misconfig-review.md`: Cloud configuration risk review and remediation planning.
- `appsec-review.md`: Application security review and secure release decisions.
- `fraud-triage.md`: Fraud/abuse triage with risk-friction tradeoff guidance.
- `compliance-control-mapping.md`: Framework control mapping and audit evidence planning.
- `security-architecture-review.md`: Architecture risk assessment and control planning.
- `study-attack-perspectives.md`: Multi-role educational analysis of attack techniques.
- `study-learning-path.md`: Role-guided 30/60/90 cybersecurity study plan.
- `personas/*.md`: One generated prompt file per persona (generated during `cybersquad init` or `cybersquad generate prompts`).

## Quick Start
1. Start with `master-prompt.md`.
2. Add `persona-prompts.generated.md` to choose role prompts generated from personas.
3. Use `persona-prompts.md` if you prefer curated/manual prompt examples.
4. Add the scenario-specific template that best matches your task.
5. Fill every field with concrete inputs and constraints.
6. Use `persona-skill-upgrades.md` weekly to improve role performance.
7. Regenerate usage prompts whenever personas change:

```bash
cybersquad generate prompts --workspace . --overwrite
```

## Suggested workflow
1. Paste `master-prompt.md` into your assistant session.
2. Paste one persona prompt from `persona-prompts.generated.md`.
3. Paste one scenario template and fill placeholders.
4. Review decision options and choose a path.
5. Re-run with updated context as new evidence appears.
