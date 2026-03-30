# Practical Examples

This guide provides copy/paste examples to operate CyberSquad in real workflows.

## 0) Setup check (once)

```bash
cybersquad doctor --workspace .
cybersquad list personas --workspace .
cybersquad list prompts --workspace .
```

## 1) Fast alert triage (single-role)

Use when you need a quick decision.

Prompt:

```text
Role(s): Atlas (SOC)
Context:
- Environment: Production M365 + endpoint fleet
- Asset(s): FIN-LT-223, user: apayne@company.com
- Time window: 2026-03-28 07:10-07:45 UTC
Objective:
- Determine if this is true positive vs false positive and assign severity.
Inputs:
- Alert source/rule: Sentinel - "Suspicious OAuth App Consent"
- Relevant telemetry: user granted app consent, app requested Mail.Read + offline_access
- Known IOCs/TTPs: app publisher unknown, redirect URI newly registered
Constraints:
- Response deadline: 20 minutes
- Operational constraints: cannot disable mailbox immediately
Output format:
- Triage verdict, severity, confidence, top evidence, immediate actions
Decision needed:
- [Close / Monitor / Escalate to Incident]
```

## 2) Incident handling (multi-role)

Use when active compromise is plausible.

Prompt:

```text
Role(s): Aegis (IR) + Atlas (SOC) + Sentinel (SecEng)
Context:
- Environment: Hybrid AD + Azure
- Scope: 3 suspected hosts + 1 privileged account
- Timeline: suspicious activity started ~2h ago
Objective:
- Build a 0-24h containment and eradication plan with owners.
Inputs:
- EDR telemetry, failed/successful logons, suspicious PowerShell execution
Constraints:
- Business-critical systems cannot be fully shut down
Output format:
- Role-by-role findings
- Consolidated recommendation
- Actions (Now/Next/Later)
- Assumptions, confidence, risks
Decision needed:
- [Approve containment plan]
```

## 3) Morning Call analysis from S33R with full squad + PDF

Use when you want a daily executive analysis from S33R outputs.

### 3.1 Validate source data

```bash
python3 - <<'PY'
import json
from pathlib import Path
p = Path('/Users/clivoa/Documents/Github/S33R/data/morning_call_latest.json')
d = json.loads(p.read_text())
print('analysis_date:', d.get('analysis_date'))
print('generated_at:', d.get('generated_at'))
print('source_generated_at:', d.get('source_generated_at'))
PY
```

### 3.2 Prompt to run

```text
You are my Virtual Cybersecurity Squad.

Task:
Analyze today's S33R Morning Call and produce a professional multi-role report with participation from all personas.

Read input from:
- /Users/clivoa/Documents/Github/S33R/data/morning_call_latest.json

Use these fields:
- analysis_date
- generated_at
- source_generated_at
- morning_call_markdown
- highlights

Role(s):
Atlas (SOC), Raven (Hunter), Orion (CTI), Aegis (IR), Forge (Detection), Gauge (DetQA), Sentinel (SecEng), Nova (AppSec), Ghost (Offensive), Hex (Malware), Patch (VulnOps), Nimbus (CloudSec), Pulse (Fraud), Ledger (GRC)

Hard requirements:
- Every role must contribute explicitly.
- Include a Participation Matrix with 14/14 roles and each role's concrete contribution.
- Keep offensive content high-level and defensive-first.
- Tie all recommendations to evidence from the morning call.
- Prioritize practical actions for the next 24h.

Output format (Markdown):
1) Executive Summary
2) Role-by-role Findings
3) Consolidated Risk View (Critical/High/Medium)
4) Action Plan (Now / Next / Later)
5) Detection & Validation Plan
6) Business/Compliance Impact
7) Participation Matrix
8) Final Decision Needed

Then save files:
- /Users/clivoa/Documents/Github/cybersquad/outputs/morning-call-YYYY-MM-DD-squad.md
- /Users/clivoa/Documents/Github/cybersquad/outputs/morning-call-YYYY-MM-DD-squad.pdf

If a PDF tool is available, generate the PDF automatically.
If not, still save Markdown and clearly state which command I should run to generate the PDF.
```

### 3.3 PDF fallback command

```bash
# Option A: pandoc (if installed)
pandoc /Users/clivoa/Documents/Github/cybersquad/outputs/morning-call-YYYY-MM-DD-squad.md \
  -o /Users/clivoa/Documents/Github/cybersquad/outputs/morning-call-YYYY-MM-DD-squad.pdf

# Option B: macOS cupsfilter
cupsfilter -m application/pdf \
  /Users/clivoa/Documents/Github/cybersquad/outputs/morning-call-YYYY-MM-DD-squad.md \
  > /Users/clivoa/Documents/Github/cybersquad/outputs/morning-call-YYYY-MM-DD-squad.pdf
```

## 4) Detection engineering + QA gate

Use when adding or tuning detections before production.

Prompt:

```text
Role(s): Forge (Detection) + Gauge (DetQA) + Atlas (SOC)
Context:
- Detection package: credential abuse rules v1.3
- Data sources: SIEM + EDR + identity logs
Objective:
- Decide go/no-go for production rollout.
Inputs:
- Rule logic, replay datasets, baseline noise metrics
Constraints:
- Maximum acceptable alert volume increase: 10%
Output format:
- Validation matrix
- Precision/recall proxy
- Regression risks
- Required tuning
- Go/No-Go recommendation
Decision needed:
- [Approve release / Tune and retest / Block deployment]
```

## 5) Cloud misconfiguration review

Prompt:

```text
Role(s): Nimbus (CloudSec) + Sentinel (SecEng)
Context:
- Cloud: AWS
- Scope: prod + shared services accounts
Objective:
- Prioritize top cloud findings and define remediation owners.
Inputs:
- CSPM output, IAM role configs, public exposure findings
Constraints:
- Change window: Saturday 00:00-04:00 UTC
Output format:
- Risk-ranked findings
- Blast radius per finding
- Immediate fixes (24-72h)
- Structural fixes (30 days)
Decision needed:
- [Approve immediate remediations / Stage rollout / Accept exceptions]
```

## 6) AppSec release gate

Prompt:

```text
Role(s): Nova (AppSec) + Sentinel (SecEng) + Ghost (Offensive)
Context:
- Service: Checkout API (Tier-0)
- Stage: pre-prod release review
Objective:
- Decide if release can proceed with current AppSec findings.
Inputs:
- SAST/DAST/SCA output, threat model, compensating controls
Constraints:
- Team can fix max 3 findings this sprint
Output format:
- Top risks
- Exploitability/business impact
- Immediate fixes
- 30-day hardening plan
Decision needed:
- [Approve / Block / Approve with exceptions]
```

## 7) Fraud/abuse triage

Prompt:

```text
Role(s): Pulse (Fraud) + Atlas (SOC) + Nova (AppSec)
Context:
- Scenario: suspicious account takeover and withdrawals
- Channels: mobile app + API
Objective:
- Contain fraud quickly while minimizing user friction.
Inputs:
- Account events, device signals, MFA reset activity, transaction anomalies
Constraints:
- Max false block rate: 2%
Output format:
- Fraud confidence/severity
- Immediate controls (Now)
- Tuning plan (Next)
- Strategic improvements (Later)
Decision needed:
- [Block / Step-up verification / Monitor / Escalate incident]
```

## 8) Study mode (multi-perspective)

Prompt:

```text
Role(s): Raven (Hunter) + Orion (CTI) + Forge (Detection) + Sentinel (SecEng) + Aegis (IR)
Context:
- Topic: Pass-the-Hash
- Environment: AD + SIEM + endpoint telemetry
- Level: Intermediate
Objective:
- Learn attacker intent, detection opportunities, and response priorities.
Constraints:
- Educational use only
- No unauthorized-access instructions
Output format:
- Concept summary
- Role-by-role perspective
- ATT&CK/kill chain mapping
- Lab-safe exercises
Decision needed:
- [Choose first 2 exercises for this week]
```

## 9) Weekly squad improvement review

Prompt:

```text
Role(s): Atlas, Raven, Orion, Aegis, Forge, Gauge, Sentinel, Nova, Ghost, Hex, Patch, Nimbus, Pulse, Ledger
Objective:
- Evaluate this week's performance and propose improvements per persona.
Inputs:
- Incidents, triage records, hunts, detection quality metrics, vuln backlog, compliance gaps
Output format:
1) Persona improvements (max 2 each)
2) Cross-role dependencies
3) Execution plan (Now/Next/Later)
4) Risks if not executed
Decision needed:
- [Approve weekly improvement plan]
```

## 10) Tips to get better outputs

- Always provide concrete context (assets, time window, business constraints).
- Always include `Decision needed`.
- Use single-role mode for speed, dual-role mode for validation, multi-role for high-impact decisions.
- Ask for confidence and assumptions when the decision is sensitive.

## 11) OpenCTI daily chain with persona owners

Use this pattern when running OpenCTI routines via scheduler (for example OpenClaw cron):

1. `09:00` Orion-led Daily Financial CTI Brief (`prompts/opencti-daily-brief.md`)
2. `09:20` Patch-led KEV Prioritization (`prompts/opencti-kev-prioritization.md`)
3. `09:40` Raven-led Financial Hunting Review (`prompts/opencti-financial-hunting-review.md`)

Suggested run constraints:

- Keep one technical OpenCTI API token for all automation jobs
- Keep persona ownership in the output header (`Lead analyst`, `Supporting lenses`)
- Write recurring outputs under `outputs/opencti/`
- Use Ralph Loop for improvement stories (layout tuning, labeling curation, feed-quality review)

## 12) Hunting hypothesis to detection logic (Sigma/SPL/CQL/Elastic)

Use when a hunting hypothesis has enough evidence to justify detection engineering follow-up.

Prompt:

```text
Role(s): Forge (Detection) + Raven (Hunter) + Orion (CTI)
Context:
- Source: latest `financial-hunting-review` output from OpenCTI workflow
- Environment: SIEM + EDR + identity telemetry for financial use cases
Objective:
- Convert 1-2 high-confidence hypotheses into practical detection logic drafts.
Inputs:
- Hypotheses, ATT&CK mapping, required fields, expected attacker behavior
- Existing rule/query candidates from:
  - https://github.com/SigmaHQ/sigma/tree/master/rules
  - https://github.com/CrowdStrike/logscale-community-content/tree/main/Queries-Only
  - https://github.com/splunk/security_content/tree/develop/detections
  - https://github.com/elastic/detection-rules
Constraints:
- Prefer adapting existing content before creating fully new logic
- Label each draft as draft/validated
Output format:
- Hypothesis summary
- Existing content matches (repo + path + rationale)
- Sigma draft
- SPL draft
- CQL draft
- Elastic draft (KQL or EQL)
- Tuning notes
- Validation plan
Decision needed:
- [Create detection ticket / Tune and test / Keep hunt-only]
```
