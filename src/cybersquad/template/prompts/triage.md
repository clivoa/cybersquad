# Cyber Squad Prompt Template: Alert Triage

## When to use
Use this template for day-to-day alert triage, suspicious activity review, and initial severity decisions.

## Recommended roles
- Primary: `Atlas (SOC) (SOC Analyst)`
- Optional collaborator: `Orion (CTI) (Threat Intelligence)`
- Optional collaborator: `Aegis (IR) (Incident Responder)` when compromise is plausible

## Prompt
```text
Role(s): Atlas (SOC) [+ Orion (CTI) optional]
Context:
- Environment: [prod/staging/hybrid]
- Asset(s): [hostnames, user accounts, business owner]
- Time window: [UTC timestamps]
Objective:
- Determine if this is true positive vs false positive and assign severity.
Inputs:
- Alert source/rule: [SIEM/EDR rule name]
- Relevant telemetry: [process tree, login events, network connections]
- Known IOCs/TTPs: [if any]
Constraints:
- Response deadline: [e.g., 30 minutes]
- Operational constraints: [no host isolation during business hours]
Output format:
- 1) Triage verdict (TP/FP/Suspicious)
- 2) Severity (Low/Medium/High/Critical)
- 3) Confidence (0-100)
- 4) Top evidence (max 5 bullets)
- 5) Immediate actions (next 30-60 min)
- 6) Escalation recommendation
Decision needed:
- [Close / Monitor / Escalate to Incident]
```

## Example filled prompt
```text
Role(s): Atlas (SOC) + Orion (CTI)
Context:
- Environment: Production M365 + endpoint fleet
- Asset(s): FIN-LT-223, user: apayne@company.com
- Time window: 2026-03-28 07:10-07:45 UTC
Objective:
- Confirm whether suspicious OAuth consent alert is malicious.
Inputs:
- Alert source/rule: Sentinel - "Suspicious OAuth App Consent"
- Telemetry: user granted app consent, app requested Mail.Read + offline_access
- IOC/TTP: app publisher unknown, redirect URI newly registered
Constraints:
- Deadline: 20 minutes
- Cannot disable user mailbox immediately (finance close activity)
Output format:
- Use triage format with severity/confidence.
Decision needed:
- Escalate to incident or monitor
```

## Expected collaboration pattern
- SOC analyst gives initial evidence verdict and severity.
- Threat intel adds campaign or actor relevance.
- If suspicious or true positive with significant impact, incident responder defines first containment step.
