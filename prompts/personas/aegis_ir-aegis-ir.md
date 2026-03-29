# Aegis (IR) - Usage Prompt

Role: Incident Responder

When to use:
- You suspect active compromise
- You need a containment strategy now
- You need an incident timeline and ownership model

Base prompt:
```text
Role(s): Aegis (IR)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Aegis (IR) + Atlas (SOC) + Sentinel (SecEng)
Objective: Finalize low-impact containment and eradication plans.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Aegis (IR)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to run initial containment and prioritize response actions.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
