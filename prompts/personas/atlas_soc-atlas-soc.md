# Atlas (SOC) - Usage Prompt

Role: SOC Analyst

When to use:
- You need rapid alert triage
- You need severity classification
- You want a first-pass incident decision

Base prompt:
```text
Role(s): Atlas (SOC)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Atlas (SOC) + Orion (CTI)
Objective: Validate campaign context and improve prioritization.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Atlas (SOC)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to explain this topic for practical learning.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
