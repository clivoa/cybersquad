# Sentinel (SecEng) - Usage Prompt

Role: Security Engineer

When to use:
- You need to deploy or tune controls
- You need automation design
- You need secure-by-design implementation guidance

Base prompt:
```text
Role(s): Sentinel (SecEng)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Sentinel (SecEng) + Forge (Detection)
Objective: Implement controls and automation that sustain detections.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Sentinel (SecEng)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: which preventive and architectural controls to implement.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
