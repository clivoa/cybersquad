# Cyber Squad Prompt Template: Compliance Control Mapping

## When to use
Use this template when you need to map technical controls to standards, assess gaps, and prepare audit evidence.

## Recommended roles
- Primary: `Ledger (GRC) (GRC and Compliance Advisor)`
- Core collaborator: `Sentinel (SecEng) (Security Engineer)`
- Optional collaborator: `Aegis (IR) (Incident Responder)` for IR/control evidence

## Prompt
```text
Role(s): Ledger (GRC) + Sentinel (SecEng) [+ Aegis (IR) optional]
Context:
- Framework: [ISO 27001 / NIST CSF / SOC 2 / custom]
- Scope: [business unit, systems, control families]
- Audit timeline: [upcoming dates]
Objective:
- Map current controls to framework requirements and identify evidence gaps.
Inputs:
- Existing controls/policies: [list]
- Technical implementation details: [tooling, configs, workflows]
- Current evidence artifacts: [reports, screenshots, logs, tickets]
Constraints:
- Resource limits: [teams available, deadlines]
- Operational constraints: [frozen systems, unavailable owners]
Output format:
- 1) Control mapping matrix
- 2) Coverage status (Covered/Partial/Missing)
- 3) Evidence required per control
- 4) Gap remediation plan with owners/dates
- 5) Residual compliance risk summary
Decision needed:
- [Approve remediation plan / Accept temporary exceptions / Re-scope]
```

## Example filled prompt
```text
Role(s): Ledger (GRC) + Sentinel (SecEng)
Context:
- Framework: SOC 2 + ISO 27001 cross-map
- Scope: Identity, access control, logging, incident response
- Audit timeline: External audit starts 2026-05-15
Objective:
- Produce mapping and close evidence gaps in 3 weeks.
Inputs:
- Controls: MFA enforced for workforce, PAM for admins, SIEM centralized
- Technical details: Sentinel + EDR + ticketing workflows
- Evidence: Last quarter access reviews, incident postmortems, policy docs
Constraints:
- Two engineers available part-time
- No control redesign until next release cycle
Output format:
- Provide matrix, gaps, owners, and target closure dates.
Decision needed:
- Approve gap closure plan and exception requests
```

## Expected collaboration pattern
- GRC advisor maps controls to requirements and defines evidence standards.
- Security engineer validates technical implementation and closes evidence gaps.
- Incident responder contributes timeline and response artifacts when IR controls are in scope.
