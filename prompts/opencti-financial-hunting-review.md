# Cyber Squad Prompt Template: OpenCTI Financial Threat Hunting Review

## When to use
Use for recurring or on-demand translation of recent OpenCTI content into threat-hunting hypotheses relevant to financial organizations.

## Recommended roles
- Primary: `Raven (Hunter) (Threat Hunter)`
- Supporting lenses: `Orion (CTI) (Threat Intelligence)`, `Pulse (Fraud) (Fraud Analyst)`, `Forge (Detection) (Detection Engineer)`
- Optional collaborator: `Atlas (SOC) (SOC Analyst)`

## Prompt
```text
Role(s): Raven (Hunter)
Context:
- Platform: OpenCTI
- Focus: financial-sector relevance
- Time range: recent content / last 24h / last 7d
Objective:
- Turn recent CTI intake into concise, practical hunting hypotheses with detection-oriented follow-up.
Inputs:
- Recent OpenCTI indicators, ATT&CK techniques, malware, reports, and vulnerability context
- Optional: existing rule/query content from Sigma, CrowdStrike LogScale, Splunk, or Elastic repositories
Constraints:
- Use English for final analytical output
- Prioritize practical hunting value over generic commentary
Output format:
- 1) Threat theme
- 2) Why it matters for financial organizations
- 3) Hunt hypotheses
- 4) Suggested telemetry
- 5) Detection opportunities
- 6) Confidence and caveats
- 7) Detection logic starter pack (Sigma + one platform-specific draft query when confidence is sufficient)
- 8) Existing content check (list matching/near-matching rules from reference repositories, or state none found)
Decision needed:
- [Close / Continue hunting / Escalate / Create detection translation follow-up]
```

## Expected collaboration pattern
- Raven defines hunt hypotheses and telemetry pivots.
- Orion adds threat and ATT&CK context.
- Pulse adds fraud and account-takeover relevance.
- Forge turns findings into detection opportunities.

## Reference repositories for existing detections
- Sigma rules: `https://github.com/SigmaHQ/sigma/tree/master/rules`
- CrowdStrike LogScale queries: `https://github.com/CrowdStrike/logscale-community-content/tree/main/Queries-Only`
- Splunk detection content: `https://github.com/splunk/security_content/tree/develop/detections`
- Elastic detection rules: `https://github.com/elastic/detection-rules`
