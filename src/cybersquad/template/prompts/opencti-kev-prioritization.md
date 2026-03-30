# Cyber Squad Prompt Template: OpenCTI KEV Prioritization Review

## When to use
Use for recurring or on-demand prioritization of CISA KEV-related vulnerability content visible in OpenCTI.

## Recommended roles
- Primary: `Patch (VulnOps) (Vulnerability Management Analyst)`
- Supporting lenses: `Orion (CTI) (Threat Intelligence)`, `Forge (Detection) (Detection Engineer)`

## Prompt
```text
Role(s): Patch (VulnOps)
Context:
- Platform: OpenCTI
- Focus: CISA KEV and recently visible vulnerability content
- Environment type: enterprise / financial-sector oriented interpretation
Objective:
- Produce a concise KEV prioritization note with practical remediation and monitoring value.
Inputs:
- Recently visible vulnerabilities in OpenCTI
- KEV-related context and any linked software, campaign, or ATT&CK information
Constraints:
- Use English for the final analytical output
- Keep prioritization conservative when asset or software context is weak
Output format:
- 1) Priority vulnerabilities
- 2) Defensive implications
- 3) Detection and monitoring considerations
- 4) Recommended next steps
- 5) Notes
Decision needed:
- [Accept priorities / Re-review / Hold until more context]
```

## Expected collaboration pattern
- Patch sets the remediation and risk priority.
- Orion adds threat and sector relevance.
- Forge adds defensive visibility and monitoring implications.
