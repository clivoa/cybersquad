# Cyber Squad Prompt Template: Detection QA / Validation

## When to use
Use this template before deploying critical detections or after SIEM/EDR changes that may break existing logic.

## Recommended roles
- Primary: `Gauge (DetQA) (Detection QA / Validation Specialist)`
- Core collaborator: `Forge (Detection) (Detection Engineer)`
- Optional collaborator: `Atlas (SOC) (SOC Analyst)` for operational realism

## Prompt
```text
Role(s): Gauge (DetQA) + Forge (Detection) [+ Atlas (SOC) optional]
Context:
- Detection package in scope: [rules/use cases]
- Data sources: [EDR, SIEM tables, identity, network]
- Environment: [dev/test/prod]
Objective:
- Validate detection quality (coverage, precision, latency) and release readiness.
Inputs:
- Rule logic/config: [queries, thresholds, exclusions]
- Test scenarios: [ATT&CK techniques, benign controls, replay datasets]
- Baseline metrics: [current FP rate, alert volume, MTTD]
Constraints:
- Release deadline: [date/time]
- Operational limits: [max acceptable alert increase]
Output format:
- 1) Validation matrix (test -> pass/fail -> evidence)
- 2) Quality metrics (precision/recall proxy/latency)
- 3) Regression risks found
- 4) Required tuning before release
- 5) Go/No-Go recommendation
Decision needed:
- [Approve release / Tune and retest / Block deployment]
```

## Example filled prompt
```text
Role(s): Gauge (DetQA) + Forge (Detection) + Atlas (SOC)
Context:
- Detection package: 6 new credential abuse rules
- Data sources: MDE + Sentinel IdentityInfo/SigninLogs
- Environment: pre-prod
Objective:
- Decide if this package can be safely deployed this week.
Inputs:
- Rule pack v1.3 + test replay with 40 malicious and 120 benign events
- Baseline FP rate: 18%
- Target max alert volume increase: 8%
Constraints:
- Release cutoff: Friday 16:00 UTC
- SOC can absorb up to 25 additional alerts/day
Output format:
- Validation matrix + quality metrics + go/no-go.
Decision needed:
- Approve or block release
```

## Expected collaboration pattern
- Detection QA specialist validates effectiveness with repeatable tests.
- Detection engineer tunes logic based on failures and tradeoffs.
- SOC confirms operational fit and triage impact.
