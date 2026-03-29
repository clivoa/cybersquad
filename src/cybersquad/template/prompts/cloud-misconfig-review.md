# Cyber Squad Prompt Template: Cloud Misconfiguration Review

## When to use
Use this template for recurring cloud security checks or ad-hoc reviews of risky IAM, networking, storage, and service configurations.

## Recommended roles
- Primary: `Nimbus (CloudSec) (Cloud Security Specialist)`
- Core collaborator: `Sentinel (SecEng) (Security Engineer)`
- Optional collaborator: `Patch (VulnOps) (Vulnerability Management Analyst)` for prioritization integration

## Prompt
```text
Role(s): Nimbus (CloudSec) + Sentinel (SecEng) [+ Patch (VulnOps) optional]
Context:
- Cloud platform: [AWS / Azure / GCP / multi-cloud]
- Accounts/subscriptions/projects in scope: [list]
- Workload criticality: [tier levels]
Objective:
- Identify and prioritize cloud misconfigurations with actionable remediation.
Inputs:
- Config snapshots or findings: [CSPM output, IaC scans, manual findings]
- IAM policies/roles: [high-risk identities]
- Network/storage exposure details: [public endpoints, bucket access]
Constraints:
- Change windows: [allowed maintenance periods]
- Operational constraints: [services with strict uptime requirements]
Output format:
- 1) Risk-ranked findings (Critical/High/Medium/Low)
- 2) Blast radius assessment per finding
- 3) Immediate fixes (24-72h)
- 4) Structural fixes (30-day roadmap)
- 5) Owner/team mapping
- 6) Validation checks after remediation
Decision needed:
- [Approve immediate remediations / Stage rollout / Accept exceptions]
```

## Example filled prompt
```text
Role(s): Nimbus (CloudSec) + Sentinel (SecEng)
Context:
- Cloud platform: AWS
- Scope: 12 accounts (prod + shared services)
- Criticality: Tier-0 identity and customer data services
Objective:
- Review top CSPM findings and produce remediation plan for this week.
Inputs:
- CSPM: 4 critical, 19 high findings
- IAM: 3 cross-account roles with wildcard actions
- Exposure: 2 S3 buckets publicly accessible, 1 admin API endpoint open to internet
Constraints:
- Change window: Sat 00:00-04:00 UTC
- Payment systems downtime max 10 minutes
Output format:
- Provide immediate vs structural fixes with owners.
Decision needed:
- Approve emergency remediation set
```

## Expected collaboration pattern
- Cloud specialist assesses technical risk and cloud-native blast radius.
- Security engineer translates findings into safe, implementable change plans.
- Vulnerability analyst aligns cloud findings with enterprise risk backlog.
