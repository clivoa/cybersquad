# Cyber Squad Prompt Template: OpenCTI Daily Brief

## When to use
Use for recurring daily review of newly visible OpenCTI content when you want a concise, threat-hunting-oriented intelligence summary.

## Recommended roles
- Primary: `Orion (CTI) (Threat Intelligence)`
- Supporting lenses: `Raven (Hunter) (Threat Hunter)`, `Patch (VulnOps) (Vulnerability Management Analyst)`, `Pulse (Fraud) (Fraud Analyst)`

## Prompt
```text
Role(s): Orion (CTI)
Context:
- Platform: OpenCTI
- Focus: financial-sector threat hunting relevance
- Time range: last 24 hours
Objective:
- Produce a concise daily intelligence brief from recent OpenCTI content.
Inputs:
- Recent OpenCTI content from connectors such as OTX, CISA KEV, URLhaus, MITRE ATT&CK, and curated reports
Constraints:
- Keep the output concise
- Focus on signal over noise
- Use English for the final analytical output
Output format:
- 1) Relevant intake
- 2) What deserves attention
- 3) Relevance to the financial sector
- 4) Hunting ideas
- 5) Notes
Decision needed:
- [No immediate decision / Review / Prioritize follow-up]
```

## Expected collaboration pattern
- Orion provides primary relevance, actor, campaign, and TTP context.
- Raven adds hunt-worthy interpretation.
- Patch highlights vulnerability-driven importance when present.
- Pulse highlights fraud, account takeover, and MFA/session abuse relevance.
