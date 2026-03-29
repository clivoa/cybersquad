# Cyber Squad Prompt Template: Security Architecture Review

## When to use
Use this template to evaluate a planned or existing system architecture for security risks, control gaps, and implementation priorities.

## Recommended roles
- Primary: `Sentinel (SecEng) (Security Engineer)`
- Core collaborator: `Nimbus (CloudSec) (Cloud Security Specialist)`
- Optional collaborator: `Ledger (GRC) (GRC and Compliance Advisor)` for framework alignment
- Optional collaborator: `Ghost (Offensive) (Pentester)` for adversarial validation

## Prompt
```text
Role(s): Sentinel (SecEng) + Nimbus (CloudSec) [+ Ledger (GRC) / Ghost (Offensive) optional]
Context:
- System/project: [name and business purpose]
- Architecture stage: [design / pre-prod / production]
- Environment: [on-prem / cloud / hybrid]
Objective:
- Assess architecture security posture and produce prioritized improvements.
Inputs:
- Architecture details: [data flows, trust boundaries, external dependencies]
- Identity model: [users, service accounts, roles]
- Existing controls: [network controls, encryption, monitoring, secrets]
- Constraints: [timeline, budget, platform limits]
Output format:
- 1) High-level risk summary
- 2) Threat scenarios (top 5)
- 3) Control gaps mapped to risks
- 4) Prioritized remediation plan (P1/P2/P3)
- 5) Compensating controls for deferred items
- 6) Validation plan before release
Decision needed:
- [Approve architecture / Approve with conditions / Rework critical areas]
```

## Example filled prompt
```text
Role(s): Sentinel (SecEng) + Nimbus (CloudSec) + Ledger (GRC)
Context:
- System/project: Customer billing API modernization
- Architecture stage: Pre-production
- Environment: AWS + Kubernetes + managed Postgres
Objective:
- Validate security readiness before production release.
Inputs:
- Architecture details: Public API gateway, internal microservices, async event bus
- Identity model: OIDC for users, IAM roles for services
- Existing controls: WAF, secrets manager, centralized logs, encryption at rest
- Constraints: Release in 3 weeks, no major platform changes
Output format:
- Provide risk summary, top threats, and P1/P2/P3 plan.
Decision needed:
- Approve release with required controls
```

## Expected collaboration pattern
- Security engineer assesses design tradeoffs and control practicality.
- Cloud security specialist evaluates IAM, networking, and service exposure.
- GRC advisor maps critical controls to policy/framework obligations.
- Pen tester proposes attack-path validation for high-risk assumptions.
