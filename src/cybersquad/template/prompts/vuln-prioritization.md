# Cyber Squad Prompt Template: Vulnerability Prioritization

## When to use
Use for daily or weekly remediation planning when vulnerability counts are high and time is limited.

## Recommended roles
- Primary: `Patch (VulnOps) (Vulnerability Management Analyst)`
- Core collaborator: `Nimbus (CloudSec) (Cloud Security Specialist)` for cloud-exposed assets
- Optional collaborator: `Ghost (Offensive) (Pentester)` for exploitability checks

## Prompt
```text
Role(s): Patch (VulnOps) + Nimbus (CloudSec) [+ Ghost (Offensive) optional]
Context:
- Asset environment: [on-prem / cloud / hybrid]
- Asset criticality: [business critical tiers]
- Exposure profile: [internet-facing/internal]
Objective:
- Produce a risk-ranked remediation backlog with clear ownership and SLA.
Inputs:
- Vulnerability list: [CVE, CVSS, affected asset]
- Exploit context: [KEV, EPSS, exploit availability]
- Compensating controls: [WAF, segmentation, EDR coverage]
Constraints:
- Patch window: [dates/time]
- Change limitations: [freeze periods, uptime requirements]
Output format:
- 1) P1/P2/P3 table
- 2) Rationale per vulnerability/cluster
- 3) Recommended SLA per priority
- 4) Quick wins this week
- 5) Deferred items + risk acceptance notes
Decision needed:
- [Approve remediation plan / request exceptions]
```

## Example filled prompt
```text
Role(s): Patch (VulnOps) + Nimbus (CloudSec)
Context:
- Environment: Hybrid, 60% AWS workloads
- Criticality: Tier-0 identity and payment systems
- Exposure: 35 internet-facing assets
Objective:
- Prioritize top 50 vulnerabilities for this sprint.
Inputs:
- CVE list includes CVE-2025-XXXX, CVE-2026-YYYY, CVE-2024-ZZZZ
- KEV matched: 7
- EPSS > 0.7: 12
- Compensating controls: WAF on public apps, EDR on servers
Constraints:
- Patch window only Saturday 01:00-05:00 UTC
- Payment platform downtime max 5 minutes
Output format:
- P1/P2/P3 with SLA and owner team.
Decision needed:
- Approve plan and define exceptions
```

## Expected collaboration pattern
- Vulnerability analyst builds risk-ranked queue.
- Cloud specialist adjusts priority based on cloud exposure and IAM blast radius.
- Pen tester validates uncertain exploitability for top disputed items.
