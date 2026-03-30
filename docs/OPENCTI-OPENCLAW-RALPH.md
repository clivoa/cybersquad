# OpenCTI + OpenClaw + Ralph Loop Integration

This guide documents the recommended operating model for CyberSquad when OpenCTI is the CTI source of truth and OpenClaw is used to orchestrate persona-driven routines.

## Goal

Make OpenCTI workflows repeatable and shareable for homelab and team onboarding without exposing secrets.

## Architecture Model

- OpenCTI: data platform and object graph (reports, indicators, vulnerabilities, ATTACK mapping, relationships)
- CyberSquad personas: analytical specialists and decision lenses
- Ralph Loop (`.agents/tasks/prd.json` + `.ralph/`): iterative backlog executor with progress tracking and guardrails
- OpenClaw cron jobs: schedule recurring persona-led reviews

## Current OpenCTI Stack (Lab Baseline)

The baseline stack used for this project includes:

- Data services: Redis, RabbitMQ, PostgreSQL, MinIO, Elasticsearch
- OpenCTI core: `opencti/platform:6.5.8`, `opencti/worker:6.5.8`
- Connectors: MITRE, CISA KEV, URLhaus, AlienVault OTX

Reference files:

- `opencti/docker-compose.yml`
- `opencti/.env.example`
- `opencti/README.md`

After `cybersquad init`, the same `opencti/` folder is available inside the generated workspace.

## Identity and API Key Strategy

For homelab and early-stage operations, use one technical OpenCTI identity and one API token for automation.

Recommended now:

- One service account (for example: `automation-opencti`)
- One token stored locally in `.env` or local secret manager
- Persona ownership represented in prompts, story metadata, and report headers

Only split to multiple OpenCTI users/tokens when you need:

- strict audit separation by workflow
- role-specific permissions
- production-like access boundaries

## Persona Ownership Model

Use personas as story owners, not as mandatory OpenCTI user identities:

- Orion (CTI): intelligence briefing, source curation, relevance framing
- Patch (VulnOps): KEV-driven vulnerability prioritization
- Raven (Hunter): hunt hypotheses from recent intake
- Pulse (Fraud): phishing, AiTM, session abuse, ATO/fraud relevance
- Forge (Detection): detection implications and telemetry alignment

## Ralph Loop Backlog Model

Use two tracks in backlog operations:

- Recurring operations: daily brief, KEV review, hunting review
- Improvement work: PDF tuning, labeling curation, signal quality review

The template PRD is pre-seeded with this model:

- `src/cybersquad/template/.agents/tasks/prd.json`

Hunting-to-detection extension in the backlog:

- `DF-003`: hunting hypotheses with a detection starter section
- `DF-008`: explicit translation of hypotheses into Sigma/SPL/CQL/Elastic drafts

## OpenClaw Cron Integration Pattern

OpenClaw cron is suitable for recurring routines that produce final analyst output on schedule.

Observed pattern from live lab usage:

- timezone-aware cron schedule (for example `Europe/Paris`)
- one lead persona in the instruction (for example Orion)
- supporting persona lenses in the same prompt
- direct delivery to a user channel

Suggested daily chain:

1. Daily Financial CTI Brief (Orion-led)
2. KEV Prioritization Review (Patch-led)
3. Financial Hunting Review (Raven-led)

Ready-to-use OpenClaw template files:

- `docs/OPENCLAW-OPENCTI-JOBS.example.json`
- `docs/OPENCLAW-SCHEDULING.md`

Reference repositories for detection reuse/adaptation:

- `https://github.com/SigmaHQ/sigma/tree/master/rules`
- `https://github.com/CrowdStrike/logscale-community-content/tree/main/Queries-Only`
- `https://github.com/splunk/security_content/tree/develop/detections`
- `https://github.com/elastic/detection-rules`

## Safe-by-Default Collaboration Rules

- Never commit `.env`, API tokens, or local OpenClaw credential files
- Keep templates with placeholders only (`CHANGE_ME_*`)
- Document owners and confidence in outputs
- Keep OpenCTI writes conservative unless the story explicitly requires enrichment updates

## Onboarding Checklist for Another Person

1. Clone repository and install `cybersquad`.
2. Run `cybersquad init <workspace>`.
3. Configure OpenCTI stack from the `opencti/` folder (compose + `.env`).
4. Run `cybersquad loop doctor --workspace <workspace>`.
5. Review `.agents/tasks/prd.json` and confirm persona owners.
6. Start one iteration: `cybersquad loop build --workspace <workspace> --iterations 1 --agent codex --no-commit`.
