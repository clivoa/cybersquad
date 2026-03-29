# Patch (VulnOps) - Usage Prompt

Role: Vulnerability Management Analyst

When to use:
- You need patch prioritization
- You need to justify remediation order
- You need executive-ready vulnerability posture summaries

Base prompt:
```text
Role(s): Patch (VulnOps)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Patch (VulnOps) + Nimbus (CloudSec)
Objective: Adjust priority based on exposure and cloud blast radius.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Patch (VulnOps)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to prioritize remediation based on real business risk.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
