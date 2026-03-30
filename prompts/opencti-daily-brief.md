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
- Focus on signal over noise; do not list everything that arrived
- Keep the output concise and professional
- Do not invent facts or overstate weak content
- Use English for the final analytical output
Mandatory response structure:
Daily Financial CTI Brief
Date: [today's date]
Scope: Financial-sector threat hunting relevance
Sources reviewed: OpenCTI (OTX, CISA KEV, URLhaus, MITRE ATT&CK, curated content)
Lead analyst: Orion (CTI)
Supporting lenses: Raven (Hunter), Patch (VulnOps), Pulse (Fraud)

Executive Summary
- one short paragraph

Key Points
- 3 to 5 bullets maximum

Threat Highlights
For each highlighted theme, use:
- Theme:
- What was observed:
- Why it matters:
- Confidence:
- Source family:

Relevance to Financial Organizations
- short focused section

Hunting Opportunities
- 1 to 3 short, actionable hypotheses

Priority Watchlist
- short list of themes, campaigns, vulnerabilities, or activity to keep under watch

Notes and Caveats
- ingestion gaps, low-signal periods, and confidence limitations
```

## Expected collaboration pattern
- Orion provides primary relevance, actor, campaign, and TTP context.
- Raven adds hunt-worthy interpretation.
- Patch highlights vulnerability-driven importance when present.
- Pulse highlights fraud, account takeover, and MFA/session abuse relevance.
