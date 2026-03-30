# Cyber Squad Prompt Template: OpenCTI Hunting Detection Translation

## When to use
Use when a hunting hypothesis is strong enough to be translated into reusable detection logic.

## Recommended roles
- Primary: `Forge (Detection) (Detection Engineer)`
- Supporting lenses: `Raven (Hunter) (Threat Hunter)`, `Orion (CTI) (Threat Intelligence)`
- Optional collaborator: `Atlas (SOC) (SOC Analyst)`

## Prompt
```text
Role(s): Forge (Detection)
Context:
- Source: OpenCTI hunting output (for example from `prompts/opencti-financial-hunting-review.md`)
- Focus: financial-sector relevance
- Detection targets: SPL, CQL (LogScale), Sigma, Elastic (KQL/EQL)
Objective:
- Convert validated hunt hypotheses into portable detection logic drafts.
Inputs:
- Hunting hypotheses with telemetry assumptions
- ATT&CK context and threat theme
- Existing detections (if any) from the reference repositories below
Reference repositories to check first:
- https://github.com/SigmaHQ/sigma/tree/master/rules
- https://github.com/CrowdStrike/logscale-community-content/tree/main/Queries-Only
- https://github.com/splunk/security_content/tree/develop/detections
- https://github.com/elastic/detection-rules
Constraints:
- Use English for final analytical output
- Prefer adapting existing quality content before creating fully new logic
- Mark confidence per detection draft
- Clearly separate tested logic from draft logic
Output format:
- 1) Hypothesis summary and required telemetry
- 2) Existing content matches (repo, path, rule/query name, match rationale)
- 3) Sigma draft (or adaptation notes)
- 4) SPL draft query
- 5) CQL (LogScale) draft query
- 6) Elastic draft logic (KQL or EQL)
- 7) Tuning notes (false positives, filters, field dependencies)
- 8) Validation plan (data needed, replay approach, expected signal)
Decision needed:
- [Create detection ticket / Tune and test / Keep as hunt-only / Discard]
```

## Expected collaboration pattern
- Raven validates the hunting intent and telemetry pivots.
- Orion validates threat relevance and ATT&CK grounding.
- Forge translates into practical detection logic drafts and validation steps.
