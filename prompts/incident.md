# Cyber Squad Prompt Template: Incident Response

## When to use
Use for active or suspected incidents requiring containment, ownership, timeline, and recovery planning.

## Recommended roles
- Primary: `Aegis (IR) (Incident Responder)`
- Core collaborators: `Atlas (SOC) (SOC Analyst)`, `Sentinel (SecEng) (Security Engineer)`
- Add `Nimbus (CloudSec) (Cloud Security Specialist)` for cloud-scoped incidents

## Prompt
```text
Role(s): Aegis (IR) + Atlas (SOC) + Sentinel (SecEng) [+ Nimbus (CloudSec) optional]
Context:
- Incident type: [ransomware / credential compromise / data exfil / etc.]
- Scope known so far: [users, hosts, cloud accounts, regions]
- Detection timeline: [first seen, last seen]
Objective:
- Build an actionable incident plan for containment, eradication, and recovery.
Inputs:
- Confirmed indicators: [hashes, domains, IPs, accounts]
- Key telemetry findings: [EDR, SIEM, IAM logs, cloud trails]
- Business critical systems impacted: [list]
Constraints:
- Business continuity limits: [systems that cannot go offline]
- Legal/compliance obligations: [breach notification timelines]
Output format:
- 1) Incident classification + severity
- 2) 0-4h action plan
- 3) 4-24h action plan
- 4) Evidence collection checklist
- 5) Roles and owners
- 6) Recovery validation criteria
- 7) Residual risks and assumptions
Decision needed:
- [Contain now / partial containment / continue investigation]
```

## Example filled prompt
```text
Role(s): Aegis (IR) + Atlas (SOC) + Sentinel (SecEng)
Context:
- Incident type: Suspected credential compromise with lateral movement
- Scope known: 2 privileged AD accounts, 5 servers
- Timeline: First seen 2026-03-28 01:12 UTC, ongoing alerts until 03:05 UTC
Objective:
- Produce containment and recovery plan for next 24 hours.
Inputs:
- Indicators: abnormal Kerberos ticket activity, unusual remote service creation
- Telemetry: EDR shows suspicious LSASS access on APP-SRV-02
- Critical systems: ERP DB cannot be offline > 15 minutes
Constraints:
- No full domain shutdown during business hours
- Must preserve forensics evidence
Output format:
- Use 0-4h and 4-24h runbook sections.
Decision needed:
- Full vs phased containment
```

## Expected collaboration pattern
- IR lead sets priorities, command structure, and incident phases.
- SOC validates scope and new detections in real time.
- Security engineer proposes safe control changes and isolation method.
- Cloud security specialist contributes when cloud identities/resources are involved.
