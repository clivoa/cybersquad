# Cyber Squad Prompt Template: Application Security Review

## When to use
Use this template for threat modeling, AppSec backlog prioritization, and secure release decisions.

## Recommended roles
- Primary: `Nova (AppSec) (Application Security Engineer)`
- Core collaborator: `Sentinel (SecEng) (Security Engineer)`
- Optional collaborator: `Ghost (Offensive) (Pentester)` for exploitability validation

## Prompt
```text
Role(s): Nova (AppSec) + Sentinel (SecEng) [+ Ghost (Offensive) optional]
Context:
- Application/service: [name, business criticality]
- Architecture: [monolith/microservices/API]
- Release stage: [design/dev/pre-prod/prod]
Objective:
- Identify and prioritize application security risks with practical mitigations.
Inputs:
- Threat model inputs: [data flows, trust boundaries, auth model]
- Findings: [SAST/DAST/SCA results, manual review notes]
- Compensating controls: [WAF, API gateway, feature flags]
Constraints:
- Release timeline: [date]
- Engineering capacity: [story points/team availability]
Output format:
- 1) Top risks (Critical/High/Medium)
- 2) Exploitability and business impact summary
- 3) Immediate fixes for this release
- 4) Hardening roadmap (next 30 days)
- 5) Security acceptance criteria and validation checks
Decision needed:
- [Approve release / Block until fixes / Approve with exceptions]
```

## Example filled prompt
```text
Role(s): Nova (AppSec) + Sentinel (SecEng)
Context:
- Application: Checkout API (Tier-0)
- Architecture: Public API + internal payment service
- Release stage: pre-prod
Objective:
- Decide if release can proceed with current AppSec findings.
Inputs:
- Findings: 2 High (authz bypass risk, dependency CVE), 6 Medium
- Threat model: token-based auth, third-party webhook integration
- Controls: WAF enabled, rate limit only at edge
Constraints:
- Release date: next Tuesday
- Team can deliver max 3 fixes this sprint
Output format:
- Risk ranking + immediate fixes + release recommendation.
Decision needed:
- Approve, block, or approve with compensating controls
```

## Expected collaboration pattern
- AppSec engineer ranks risk by exploitability and impact.
- Security engineer defines feasible implementation changes.
- Offensive role validates disputed exploit paths when needed.
