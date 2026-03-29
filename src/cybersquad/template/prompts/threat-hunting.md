# Cyber Squad Prompt Template: Threat Hunting

## When to use
Use this template for proactive hunting when you want to find stealthy or pre-incident attacker behavior not yet detected by alerts.

## Recommended roles
- Primary: `Raven (Hunter) (Threat Hunter)`
- Core collaborator: `Orion (CTI) (Threat Intelligence)`
- Optional collaborator: `Forge (Detection) (Detection Engineer)` for detection engineering follow-up
- Optional collaborator: `Atlas (SOC) (SOC Analyst)` for operational validation

## Prompt
```text
Role(s): Raven (Hunter) + Orion (CTI) [+ Forge (Detection) + Atlas (SOC) optional]
Context:
- Environment: [on-prem/cloud/hybrid]
- Scope: [business units, endpoints, servers, identities]
- Time range: [last 24h / 7d / 30d]
Objective:
- Build and execute a hypothesis-driven hunt for suspicious activity.
Inputs:
- Threat hypothesis: [e.g., token theft, living-off-the-land abuse]
- Relevant logs/telemetry: [EDR, SIEM, auth logs, DNS, proxy]
- Known TTP references: [ATT&CK techniques, campaign notes]
Constraints:
- Time budget: [e.g., 2 hours]
- Data limitations: [missing telemetry, retention windows]
Output format:
- 1) Hunt hypothesis
- 2) Data sources and query plan
- 3) Findings (confirmed/suspicious/none)
- 4) Confidence level and gaps
- 5) Recommended detections or controls
- 6) Next hunt iteration
Decision needed:
- [Close hunt / Expand scope / Escalate to incident]
```

## Example filled prompt
```text
Role(s): Raven (Hunter) + Orion (CTI) + Atlas (SOC)
Context:
- Environment: Hybrid AD + M365 + EDR
- Scope: Finance and IT admin users
- Time range: Last 14 days
Objective:
- Hunt for signs of token abuse tied to recent phishing activity.
Inputs:
- Hypothesis: Attacker used stolen refresh tokens to access mail and SharePoint
- Telemetry: AAD sign-ins, app consent logs, mailbox audit logs, EDR process events
- TTP references: ATT&CK T1528, T1078
Constraints:
- Time budget: 3 hours
- AAD logs available for only 14 days
Output format:
- Provide findings, confidence, and next detections.
Decision needed:
- Escalate to incident or continue iterative hunt
```

## Expected collaboration pattern
- Threat hunter defines and executes hypothesis-driven hunts.
- Threat intelligence adds adversary context and ATT&CK alignment.
- SOC validates operational relevance and escalation signals.
- Detection engineer turns findings into durable detections and tuning updates.
