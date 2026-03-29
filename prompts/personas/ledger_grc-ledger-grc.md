# Ledger (GRC) - Usage Prompt

Role: GRC and Compliance Advisor

When to use:
- You need compliance interpretation
- You need control/evidence mapping
- You need governance decisions documented

Base prompt:
```text
Role(s): Ledger (GRC)
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): Ledger (GRC) + Sentinel (SecEng) + Aegis (IR)
Objective: Close control and evidence gaps with owners and deadlines.
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): Ledger (GRC)
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: how to connect the topic to controls and compliance.
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
