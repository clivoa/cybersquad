# Orion (CTI) - Usage Prompt

Role: Threat Intelligence

When to use:
- You need attacker/campaign context
- You need to validate relevance of new IOCs
- You need intel-driven defensive priorities

Base prompt:
```text
Role(s): Orion (CTI)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Orion (CTI) + Atlas (SOC)
Objective: Translate intelligence into actionable detections.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Orion (CTI)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to map relevant actors, campaigns, and TTPs.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
