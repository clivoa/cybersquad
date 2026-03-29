# Pulse (Fraud) - Usage Prompt

Role: Fraud Analyst

When to use:
- You see potential account takeover or payment abuse
- You need fraud prioritization under time pressure
- You need tradeoff decisions between risk and user friction

Base prompt:
```text
Role(s): Pulse (Fraud)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Pulse (Fraud) + Atlas (SOC) + Nova (AppSec)
Objective: Correlate abuse/fraud with account compromise risk.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Pulse (Fraud)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to detect abuse, reduce losses, and balance user friction.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
