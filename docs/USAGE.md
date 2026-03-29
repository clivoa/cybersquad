# Usage Guide

## Primary entrypoint

Always start with:

- `prompts/master-prompt.md`

Then combine with:

- `prompts/persona-prompts.generated.md` for auto-generated persona-specific usage
- `prompts/persona-prompts.md` for curated/manual examples
- one scenario template from `prompts/`

For copy/paste operational examples, see:

- `docs/EXAMPLES.md`

## Study mode (multi-perspective learning)

Use these templates when learning attacks/techniques:

- `prompts/study-attack-perspectives.md`
- `prompts/study-learning-path.md`

Recommended pattern:

1. Choose 3-6 personas depending on the topic.
2. Ask for both offensive intent (high-level) and defensive actions.
3. Require ATT&CK mapping, detection opportunities, and lab-safe exercises.

## Prompt generation

Persona usage prompts are auto-generated during `cybersquad init`.

When you update `personas.yaml`, regenerate usage prompts manually:

```bash
cybersquad generate prompts --workspace . --overwrite
```

This updates:

- `prompts/persona-prompts.generated.md`
- `prompts/personas/*.md`

## Recommended operating rhythm

### Daily

- Alert triage: `prompts/triage.md`
- Cloud checks: `prompts/cloud-misconfig-review.md`
- Vulnerability prioritization: `prompts/vuln-prioritization.md`
- Fraud triage: `prompts/fraud-triage.md`

### Weekly

- Threat hunting: `prompts/threat-hunting.md`
- Detection QA validation: `prompts/detection-validation.md`
- AppSec review: `prompts/appsec-review.md`
- Skill improvement review: `prompts/persona-skill-upgrades.md`
- Study deep-dive: `prompts/study-attack-perspectives.md`

### Monthly

- Architecture review: `prompts/security-architecture-review.md`
- Compliance control mapping: `prompts/compliance-control-mapping.md`

## Suggested collaboration modes

- Single-role: quick focused decisions
- Dual-role: validation and better signal quality
- Multi-role: incident and high-impact decisions

## Output quality checklist

Require these fields in every response:

- Findings
- Recommended actions (Now/Next/Later)
- Decision needed
- Assumptions
- Confidence (0-100)
