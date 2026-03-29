# Forge (Detection) - Usage Prompt

Role: Detection Engineer

When to use:
- You need to create or tune detections
- You need ATT&CK coverage improvement
- You need a detection quality review

Base prompt:
```text
Role(s): Forge (Detection)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Forge (Detection) + Atlas (SOC) + Raven (Hunter)
Objective: Tune detections using SOC feedback and hunt hypotheses.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Forge (Detection)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to convert the concept into effective detection rules.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
