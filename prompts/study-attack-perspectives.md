# Cyber Squad Prompt Template: Study Attack Perspectives

## When to use
Use this template when you are studying an attack, TTP, or incident pattern and want multi-role viewpoints.

## Recommended roles
- Core: `Raven (Hunter)`, `Orion (CTI)`, `Forge (Detection)`, `Sentinel (SecEng)`
- Add: `Ghost (Offensive)` for ethical attacker perspective
- Add: `Aegis (IR)` for response playbook view
- Add: `Hex (Malware)` for artifact-centric malware scenarios
- Add: `Nova (AppSec)` for secure coding and app abuse controls
- Add: `Gauge (DetQA)` for detection validation perspective
- Add: `Pulse (Fraud)` for abuse/fraud tradeoff perspective
- Add: `Ledger (GRC)` for compliance/control mapping

## Prompt
```text
Role(s): [select 3-6 personas]
Context:
- Study topic: [e.g., credential dumping, pass-the-hash, phishing-to-oauth abuse]
- Environment: [AD, cloud, hybrid, app stack]
- Level: [beginner / intermediate / advanced]
Objective:
- Learn this topic from each role's perspective (offense, defense, detection, response, governance).
Constraints:
- Educational use only
- No unauthorized access guidance
- Focus on lab-safe and defensive understanding
Output format:
- 1) Summary of the attack concept
- 2) Perspective by role:
  - What attacker is trying to achieve
  - What defender should prioritize
  - What to monitor/detect
  - Immediate response actions if observed
  - Common mistakes
- 3) ATT&CK / kill chain mapping
- 4) Practical study plan (Now / Next / Later)
- 5) Lab-safe exercises and validation checklist
Decision needed:
- [Which learning path should I follow first?]
```

## Example filled prompt
```text
Role(s): Raven (Hunter) + Orion (CTI) + Forge (Detection) + Sentinel (SecEng) + Aegis (IR)
Context:
- Study topic: Pass-the-Hash
- Environment: AD + endpoint telemetry + SIEM
- Level: Intermediate
Objective:
- Understand attacker workflow, detection opportunities, and response priorities.
Constraints:
- Educational use in authorized lab only
- No real-world exploitation instructions
Output format:
- Role-by-role analysis + ATT&CK mapping + study plan.
Decision needed:
- Choose first 2 exercises for this week
```

## Expected collaboration pattern
- CTI provides actor/TTP context.
- Hunter defines hypotheses and telemetry pivots.
- Detection engineer translates to rules and tuning.
- Security engineer recommends prevention and hardening.
- Incident responder frames containment and escalation logic.
- Offensive role explains high-level attacker decision points ethically.
