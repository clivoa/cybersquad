# OpenClaw Scheduling for OpenCTI Persona Jobs

This file explains how to use the ready OpenClaw cron job template for the CyberSquad OpenCTI chain.

## Template File

- `docs/OPENCLAW-OPENCTI-JOBS.example.json`

## Jobs Included

- Daily Financial CTI Brief (`09:00`, Europe/Paris)
- Financial KEV Prioritization Review (`09:20`, Europe/Paris)
- Financial Threat Hunting Review (`09:40`, Europe/Paris)
- Hunting Detection Translation (`10:00`, Europe/Paris, weekdays, disabled by default)

## Delivery Mode

The template uses:

- `delivery.mode: announce`
- `delivery.channel: webchat`

This avoids WhatsApp target errors if no E.164/JID destination is configured.

## How to Apply Safely

1. Backup your current OpenClaw jobs file.
2. Merge the `jobs` entries from the template into your existing `jobs.json`.
3. Keep IDs unique in your final `jobs` array.
4. Save and restart OpenClaw/scheduler if required by your setup.

Example paths (Windows):

- Source template: `D:\Github\cybersquad\docs\OPENCLAW-OPENCTI-JOBS.example.json`
- Live file: `C:\Users\CVini\.openclaw\cron\jobs.json`

## Security Notes

- Do not put API keys, tokens, or passwords in cron payload messages.
- Keep OpenCTI secrets only in local environment files or secret stores.
- Keep persona ownership in prompts and output metadata, not in hardcoded credentials.
