# Cyber Squad Prompt Template: Fraud Triage and Response

## When to use
Use this template for account takeover suspicion, payment abuse, promo abuse, and coordinated fraud events.

## Recommended roles
- Primary: `Pulse (Fraud) (Fraud Analyst)`
- Core collaborator: `Atlas (SOC) (SOC Analyst)`
- Optional collaborator: `Nova (AppSec) (Application Security Engineer)` for app-flow weaknesses

## Prompt
```text
Role(s): Pulse (Fraud) + Atlas (SOC) [+ Nova (AppSec) optional]
Context:
- Fraud scenario: [ATO/card abuse/refund abuse/promo abuse]
- Channels in scope: [web/mobile/api]
- Time window: [UTC timestamps]
Objective:
- Classify fraud risk and define immediate containment with minimal customer friction.
Inputs:
- Transaction/account events: [attempts, success rate, geolocation/device patterns]
- Identity signals: [MFA resets, impossible travel, new devices]
- Existing controls: [velocity rules, MFA, blocklists]
Constraints:
- Customer impact tolerance: [max false block rate]
- Response time target: [e.g., 30 minutes]
Output format:
- 1) Fraud confidence and severity
- 2) Attack pattern summary
- 3) Immediate controls (Now)
- 4) Short-term tuning plan (Next)
- 5) Strategic improvements (Later)
- 6) User friction and business impact tradeoff
Decision needed:
- [Block / Step-up verification / Monitor / Escalate incident]
```

## Example filled prompt
```text
Role(s): Pulse (Fraud) + Atlas (SOC)
Context:
- Scenario: account takeover + suspicious withdrawals
- Channels: mobile app + API
- Window: 2026-03-28 10:00-11:15 UTC
Objective:
- Contain possible active fraud campaign without broad customer lockouts.
Inputs:
- 42 affected accounts, same ASN, repeated MFA reset attempts
- 11 successful withdrawals above normal profile
- Controls: basic velocity limits, no device binding
Constraints:
- Max false block rate: 2%
- Decision deadline: 20 minutes
Output format:
- Fraud severity + containment actions + tradeoff notes.
Decision needed:
- Step-up all risky sessions or full block by ASN
```

## Expected collaboration pattern
- Fraud analyst quantifies abuse confidence and business impact.
- SOC analyst correlates with security telemetry and potential compromise.
- AppSec engineer addresses application flow weaknesses that enable abuse.
