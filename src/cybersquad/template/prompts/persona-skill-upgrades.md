# Cyber Squad: Persona Skill Evolution

Use this playbook to improve each persona in a measurable way.

## Improvement cadence

1. Pick one persona per week (or two if they are tightly coupled).
2. Run the persona's skill prompt on real cases from the last 7 days.
3. Apply one workflow change and one detection/control change.
4. Measure impact after 7 days.
5. Keep, tune, or revert based on metric movement.

## Global quality bar (applies to every persona)

- Recommendations must be evidence-based and actionable in <= 24h, <= 72h, and <= 30d horizons.
- Outputs must include assumptions, confidence, and explicit tradeoffs.
- Every tactical recommendation must map to a measurable KPI.

## Persona skill plans

### Atlas (SOC)
- Skill focus:
  - Better signal-to-noise decisions under time pressure.
  - Faster enrichment from identity + endpoint + cloud context.
  - Stronger escalation criteria with less ambiguity.
- 30-day target:
  - Reduce false positive rate by 20% and triage time by 15%.
- Weekly drills:
  - Re-score 10 closed alerts and compare with original severity.
  - Build 3 reusable triage decision trees for common alert types.
- KPIs:
  - False positive rate.
  - Mean triage time.
  - Escalation reversal rate.
- Skill prompt:
```text
Role(s): Atlas (SOC)
Objective: Improve triage quality and speed using last week's alerts.
Inputs: 10 recent alerts, triage notes, final incident outcomes.
Output format:
1) Misclassified cases
2) Root causes
3) Updated triage rubric
4) KPI impact forecast (7/30 days)
Decision needed: approve rubric update
```

### Raven (Hunter)
- Skill focus:
  - Higher-yield hunt hypotheses.
  - Better telemetry pivot strategy.
  - Faster hunt-to-detection conversion.
- 30-day target:
  - Increase actionable hunt findings by 25%.
- Weekly drills:
  - Convert 2 weak-signal cases into structured hypotheses.
  - Create 2 ATT&CK-aligned hunt query packs.
- KPIs:
  - Actionable hunt rate.
  - Hunt-to-detection lead time.
  - False-positive hunts per cycle.
- Skill prompt:
```text
Role(s): Raven (Hunter) + Orion (CTI) + Forge (Detection)
Objective: Increase actionable outcomes from hunt operations.
Inputs: last 4 hunts, telemetry coverage map, intel priorities.
Output format:
1) Top 3 improved hypotheses
2) Query/pivot plan
3) Detection handoff package
4) KPI targets
Decision needed: prioritize next hunt sprint
```

### Orion (CTI)
- Skill focus:
  - Better intelligence relevance scoring.
  - Cleaner conversion from intel to operations.
  - Improved confidence grading and caveats.
- 30-day target:
  - Raise actionable-intel ratio by 30%.
- Weekly drills:
  - Score 20 intel items for business relevance.
  - Produce 1 short intel-to-detection brief per week.
- KPIs:
  - Actionable intel ratio.
  - Time-to-defensive action.
  - Intel aging before action.
- Skill prompt:
```text
Role(s): Orion (CTI)
Objective: Increase actionable intelligence quality.
Inputs: latest intel feed items, SOC backlog, active campaigns.
Output format:
1) Useful vs noise classification
2) Priority mapping to business risk
3) Immediate detection/control actions
4) Confidence and assumptions
Decision needed: approve top 5 intel actions
```

### Aegis (IR)
- Skill focus:
  - Faster containment with minimal business disruption.
  - Stronger incident command discipline.
  - Better evidence quality for post-incident learning.
- 30-day target:
  - Reduce time-to-initial-containment by 20%.
- Weekly drills:
  - Run one tabletop for a top threat of the week.
  - Rebuild one incident timeline from raw telemetry.
- KPIs:
  - MTTC (time to containment).
  - MTTR.
  - Post-incident action closure rate.
- Skill prompt:
```text
Role(s): Aegis (IR) + Atlas (SOC) + Sentinel (SecEng)
Objective: Shorten containment time while preserving continuity.
Inputs: latest incident timeline, containment actions, impact report.
Output format:
1) Bottlenecks
2) Runbook improvements (0-4h)
3) Ownership and deadlines
4) Expected KPI gains
Decision needed: approve runbook revision
```

### Forge (Detection)
- Skill focus:
  - Better precision without losing coverage.
  - Stronger detection-as-code quality.
  - Faster iteration loop with SOC feedback.
- 30-day target:
  - Improve precision by 15% on top noisy rules.
- Weekly drills:
  - Tune 3 noisy detections with before/after metrics.
  - Add unit-style validation for 2 critical detections.
- KPIs:
  - False positive rate per rule.
  - ATT&CK coverage on priority techniques.
  - Detection deployment cycle time.
- Skill prompt:
```text
Role(s): Forge (Detection) + Gauge (DetQA)
Objective: Improve high-volume detections with measurable quality gains.
Inputs: rule logic, alert stats, false-positive examples.
Output format:
1) Tuning changes
2) Validation criteria
3) Regression risk
4) KPI delta forecast
Decision needed: approve production rollout
```

### Gauge (DetQA)
- Skill focus:
  - Better regression prevention.
  - More realistic adversary-emulation testing.
  - Stronger quality gates for critical detections.
- 30-day target:
  - Catch 90% of critical detection regressions before production.
- Weekly drills:
  - Run replay tests for 5 critical detections.
  - Build a pass/fail matrix for each release candidate.
- KPIs:
  - Pre-prod regression catch rate.
  - Validation coverage on critical rules.
  - Alert latency under test.
- Skill prompt:
```text
Role(s): Gauge (DetQA) + Forge (Detection) + Atlas (SOC)
Objective: Prevent critical detection regressions.
Inputs: candidate detection pack, replay datasets, baseline metrics.
Output format:
1) Pass/fail matrix
2) Regression findings
3) Required fixes
4) Go/No-Go decision
Decision needed: release approval
```

### Sentinel (SecEng)
- Skill focus:
  - Better preventive control design.
  - Higher automation reliability.
  - Lower operational friction from security controls.
- 30-day target:
  - Reduce manual security tasks by 25% for chosen workflows.
- Weekly drills:
  - Automate one recurring manual security action.
  - Validate one control rollback path.
- KPIs:
  - Manual-to-automated workflow ratio.
  - Change failure rate.
  - Control coverage growth.
- Skill prompt:
```text
Role(s): Sentinel (SecEng) + Forge (Detection)
Objective: Increase control reliability and automation impact.
Inputs: current controls, failure tickets, manual runbooks.
Output format:
1) Automation candidates
2) Control hardening plan
3) Rollback/safety checks
4) KPI impact estimate
Decision needed: approve implementation sprint
```

### Nova (AppSec)
- Skill focus:
  - Better threat modeling quality.
  - Stronger secure coding feedback loops.
  - Faster remediation prioritization by exploitability.
- 30-day target:
  - Reduce high-risk app vuln reopen rate by 20%.
- Weekly drills:
  - Threat-model one critical feature end-to-end.
  - Review top 5 findings for root-cause recurrence.
- KPIs:
  - Time-to-fix (high severity).
  - Reopen rate.
  - Security acceptance criteria pass rate.
- Skill prompt:
```text
Role(s): Nova (AppSec) + Sentinel (SecEng) + Ghost (Offensive)
Objective: Improve secure release quality and reduce recurring app risk.
Inputs: SAST/DAST/SCA results, threat model, previous incidents.
Output format:
1) Top exploitability-driven priorities
2) SDLC control improvements
3) Release gating criteria
4) KPI targets
Decision needed: approve release policy updates
```

### Ghost (Offensive)
- Skill focus:
  - Better proof-of-risk communication for defenders.
  - Stronger remediation validation design.
  - Clearer mapping from attack path to business impact.
- 30-day target:
  - Increase accepted remediation actions from offensive findings by 20%.
- Weekly drills:
  - Rework 3 findings into more remediation-ready narratives.
  - Add one retest plan per major finding.
- KPIs:
  - Finding acceptance rate.
  - Retest cycle time.
  - Critical path-to-fix completion.
- Skill prompt:
```text
Role(s): Ghost (Offensive) + Patch (VulnOps) + Sentinel (SecEng)
Objective: Improve exploitability reports for faster remediation.
Inputs: recent offensive findings, remediation status, retest history.
Output format:
1) Improved finding narratives
2) Risk-to-remediation mapping
3) Retest checklist
4) Expected adoption impact
Decision needed: approve reporting standard update
```

### Hex (Malware)
- Skill focus:
  - Faster artifact triage.
  - Better behavior-centric IOC extraction.
  - Stronger handoff to detection and IR.
- 30-day target:
  - Reduce malware triage time by 20%.
- Weekly drills:
  - Analyze 3 recent samples with behavior-first output.
  - Produce one reusable YARA or behavior profile update.
- KPIs:
  - Mean sample triage time.
  - Reusable IOC rate.
  - Detection conversion from malware findings.
- Skill prompt:
```text
Role(s): Hex (Malware) + Orion (CTI) + Forge (Detection)
Objective: Improve speed and operational usefulness of malware analysis.
Inputs: suspicious samples, sandbox outputs, endpoint telemetry.
Output format:
1) Behavior profile
2) High-confidence indicators
3) Detection content proposals
4) Containment priorities
Decision needed: approve detection/content package
```

### Patch (VulnOps)
- Skill focus:
  - Better risk-based prioritization.
  - Improved exception governance.
  - Stronger alignment between exploitability and business impact.
- 30-day target:
  - Improve P1 SLA compliance by 15%.
- Weekly drills:
  - Re-rank top 50 vulnerabilities with exploit context.
  - Audit and justify all active exceptions.
- KPIs:
  - P1/P2 SLA attainment.
  - Critical vuln aging.
  - Exception reduction rate.
- Skill prompt:
```text
Role(s): Patch (VulnOps) + Nimbus (CloudSec) + Ghost (Offensive)
Objective: Increase remediation impact from vulnerability prioritization.
Inputs: vulnerability backlog, KEV/EPSS, asset criticality, exploitability notes.
Output format:
1) Revised P1/P2/P3 queue
2) Exception decisions
3) Owner/SLA mapping
4) KPI movement estimate
Decision needed: approve remediation order
```

### Nimbus (CloudSec)
- Skill focus:
  - Better IAM blast-radius control.
  - Stronger preventive guardrails.
  - Faster cloud finding remediation cycles.
- 30-day target:
  - Reduce critical cloud misconfiguration recurrence by 25%.
- Weekly drills:
  - Review top IAM privilege paths and close one escalation route.
  - Convert one recurring cloud finding into policy-as-code guardrail.
- KPIs:
  - Time-to-remediate critical cloud findings.
  - Misconfiguration recurrence.
  - Privileged path reduction.
- Skill prompt:
```text
Role(s): Nimbus (CloudSec) + Sentinel (SecEng)
Objective: Reduce cloud risk recurrence with enforceable guardrails.
Inputs: CSPM findings, IAM graph, incident learnings.
Output format:
1) Priority cloud risks
2) Guardrail implementations
3) Validation checks
4) KPI targets
Decision needed: approve guardrail rollout
```

### Pulse (Fraud)
- Skill focus:
  - Better fraud-signal precision.
  - More balanced friction strategy.
  - Stronger SOC/AppSec integration for abuse scenarios.
- 30-day target:
  - Reduce fraud losses by 10% without increasing false blocks.
- Weekly drills:
  - Review 20 blocked/allowed decisions for precision gaps.
  - Tune one high-impact fraud rule and simulate customer impact.
- KPIs:
  - Fraud loss amount.
  - False block rate.
  - Time-to-contain fraud campaigns.
- Skill prompt:
```text
Role(s): Pulse (Fraud) + Atlas (SOC) + Nova (AppSec)
Objective: Improve fraud control precision with low customer friction.
Inputs: account events, fraud cases, blocked transaction outcomes.
Output format:
1) Rule tuning actions
2) Friction tradeoff analysis
3) Incident trigger criteria
4) KPI target movement
Decision needed: approve fraud rule changes
```

### Ledger (GRC)
- Skill focus:
  - Better control-to-evidence traceability.
  - Faster audit readiness.
  - Stronger policy-to-operations alignment.
- 30-day target:
  - Reduce audit evidence preparation lead time by 20%.
- Weekly drills:
  - Map one operational change set to framework controls.
  - Audit one control family for missing evidence.
- KPIs:
  - Controls with complete evidence.
  - Audit prep lead time.
  - Open compliance gaps by criticality.
- Skill prompt:
```text
Role(s): Ledger (GRC) + Sentinel (SecEng) + Aegis (IR)
Objective: Increase audit readiness and reduce compliance rework.
Inputs: current control mappings, evidence repositories, recent incidents.
Output format:
1) Control/evidence gaps
2) Process and ownership fixes
3) Automation opportunities
4) KPI targets
Decision needed: approve governance remediation plan
```

## Squad-level monthly review

```text
Role(s): Atlas, Raven, Orion, Aegis, Forge, Gauge, Sentinel, Nova, Ghost, Hex, Patch, Nimbus, Pulse, Ledger
Objective: Run a monthly squad capability review and define the next 30-day skill sprint.
Inputs: incident outcomes, hunt metrics, detection QA results, remediation SLAs, cloud findings, fraud trends, compliance gaps.
Output format:
1) Top 2 improvement priorities per persona
2) Cross-role dependencies and sequencing
3) 30-day execution roadmap
4) Risks if deferred
5) Metrics scoreboard (baseline vs target)
Decision needed: approve monthly skill roadmap
```
