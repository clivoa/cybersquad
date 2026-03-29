# Ghost (Offensive) - Usage Prompt

Role: Pentester

When to use:
- You need exploitability validation
- You need proof-of-risk for prioritization
- You need adversarial perspective on defenses

Base prompt:
```text
Role(s): Ghost (Offensive)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Ghost (Offensive) + Patch (VulnOps) + Sentinel (SecEng)
Objective: Prioritize remediation based on real exploitability risk.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Ghost (Offensive)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to assess exploitability ethically in an authorized lab.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
