# Cyber Squad Prompt Template: Study Learning Path

## When to use
Use this template to build a personalized cyber learning roadmap with role-specific guidance.

## Recommended roles
- Core: `Atlas (SOC)`, `Raven (Hunter)`, `Orion (CTI)`, `Forge (Detection)`, `Sentinel (SecEng)`
- Add: `Gauge (DetQA)` for detection quality and validation track
- Add: `Nova (AppSec)` for secure SDLC and application defense track
- Add: `Pulse (Fraud)` for abuse and transaction defense track
- Add: `Ghost (Offensive)` + `Hex (Malware)` for advanced tracks
- Add: `Ledger (GRC)` for governance/compliance context

## Prompt
```text
Role(s): [select roles]
Context:
- Current level: [beginner/intermediate/advanced]
- Focus area: [SOC, threat hunting, cloud, detection, DFIR, offensive]
- Weekly study time: [hours/week]
Objective:
- Build a practical study roadmap with role-based perspectives and milestones.
Inputs:
- Current skills/tools: [SIEM, EDR, cloud, scripting]
- Target outcome: [job role, certification, capability]
Constraints:
- Time limits
- Tool/lab availability
Output format:
- 1) Current gap analysis by role
- 2) 30/60/90 day roadmap
- 3) Weekly exercises (lab-safe)
- 4) Metrics to track progress
- 5) Pitfalls and anti-patterns
Decision needed:
- [Approve roadmap or rebalance by focus area]
```

## Example filled prompt
```text
Role(s): Atlas (SOC) + Raven (Hunter) + Forge (Detection) + Sentinel (SecEng)
Context:
- Current level: Intermediate
- Focus area: Detection engineering + hunting
- Weekly study time: 6h/week
Objective:
- Build a 90-day plan to improve practical detection outcomes.
Inputs:
- Current tools: Sentinel, Defender, KQL
- Target outcome: become reliable in ATT&CK-aligned detections
Constraints:
- No paid labs
- Must use internal test environment
Output format:
- 30/60/90 plan + weekly tasks + measurable KPIs.
Decision needed:
- Confirm first month objectives
```
