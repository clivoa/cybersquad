from __future__ import annotations

import datetime as dt
from pathlib import Path

from .personas import Persona, load_personas

COLLAB_HINTS: dict[str, tuple[str, str]] = {
    "atlas_soc": ("Orion (CTI)", "Validate campaign context and improve prioritization."),
    "raven_hunter": (
        "Orion (CTI) + Forge (Detection)",
        "Generate hunting hypotheses and convert findings into durable detections.",
    ),
    "orion_cti": ("Atlas (SOC)", "Translate intelligence into actionable detections."),
    "aegis_ir": (
        "Atlas (SOC) + Sentinel (SecEng)",
        "Finalize low-impact containment and eradication plans.",
    ),
    "forge_detection": (
        "Atlas (SOC) + Raven (Hunter)",
        "Tune detections using SOC feedback and hunt hypotheses.",
    ),
    "gauge_detqa": (
        "Forge (Detection) + Atlas (SOC)",
        "Validate detection quality and reduce production regressions.",
    ),
    "sentinel_seceng": (
        "Forge (Detection)",
        "Implement controls and automation that sustain detections.",
    ),
    "nova_appsec": (
        "Sentinel (SecEng) + Ghost (Offensive)",
        "Prioritize application flaws by real risk and remediation feasibility.",
    ),
    "ghost_offensive": (
        "Patch (VulnOps) + Sentinel (SecEng)",
        "Prioritize remediation based on real exploitability risk.",
    ),
    "hex_malware": (
        "Orion (CTI) + Forge (Detection)",
        "Extract IOCs and behaviors for intelligence and detection updates.",
    ),
    "patch_vulnops": (
        "Nimbus (CloudSec)",
        "Adjust priority based on exposure and cloud blast radius.",
    ),
    "nimbus_cloudsec": (
        "Sentinel (SecEng)",
        "Turn findings into automated preventive guardrails.",
    ),
    "pulse_fraud": (
        "Atlas (SOC) + Nova (AppSec)",
        "Correlate abuse/fraud with account compromise risk.",
    ),
    "ledger_grc": (
        "Sentinel (SecEng) + Aegis (IR)",
        "Close control and evidence gaps with owners and deadlines.",
    ),
}

def _slugify(value: str) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug

def _when_to_use(persona: Persona) -> list[str]:
    if persona.consult_when:
        return persona.consult_when
    return [f"You should consult {persona.name} when this role is needed."]


def _collaboration(persona: Persona) -> tuple[str, str]:
    return COLLAB_HINTS.get(
        persona.id,
        ("another relevant specialist", "Validate decisions through cross-role collaboration."),
    )


def _study_focus(persona: Persona) -> str:
    role = persona.role.lower()
    if "threat hunter" in role:
        return "which hunt hypotheses to build and which signals to pursue."
    if "threat intelligence" in role:
        return "how to map relevant actors, campaigns, and TTPs."
    if "incident responder" in role:
        return "how to run initial containment and prioritize response actions."
    if "detection engineer" in role:
        return "how to convert the concept into effective detection rules."
    if "detection qa" in role or "validation specialist" in role:
        return "how to validate detection efficacy, coverage, and regressions."
    if "application security" in role:
        return "how to reduce application risk and strengthen the SDLC."
    if "security engineer" in role:
        return "which preventive and architectural controls to implement."
    if "pentester" in role:
        return "how to assess exploitability ethically in an authorized lab."
    if "malware analyst" in role:
        return "how to analyze malicious artifacts and behavior patterns."
    if "vulnerability management" in role:
        return "how to prioritize remediation based on real business risk."
    if "cloud security" in role:
        return "how to reduce blast radius and cloud risk."
    if "fraud analyst" in role or "fraud" in role:
        return "how to detect abuse, reduce losses, and balance user friction."
    if "grc" in role:
        return "how to connect the topic to controls and compliance."
    return "how to explain this topic for practical learning."


def _render_persona_block(index: int, persona: Persona) -> str:
    collab, collab_goal = _collaboration(persona)
    study_focus = _study_focus(persona)
    when_lines = "\n".join(f"- {item}" for item in _when_to_use(persona))
    style_line = (
        f"- Expected communication style: {persona.communication_style}"
        if persona.communication_style
        else ""
    )

    style_section = f"\n{style_line}" if style_line else ""

    return f"""## {index}) {persona.name} ({persona.role})

When to use:
{when_lines}{style_section}

Quick prompt:
```text
Role(s): {persona.name}
Context: [environment, assets, time window]
Objective: [immediate outcome needed]
Inputs: [logs, alerts, evidence, configurations]
Constraints: [time, business impact, operational limits]
Output format: [verdict, priority, confidence (0-100), 3 next actions]
Decision needed: [close / monitor / escalate]
```

Collaborative prompt:
```text
Role(s): {persona.name} + {collab}
Objective: {collab_goal}
Output format: role-by-role findings, consolidated recommendation, risks, assumptions.
```

Skill improvement prompt:
```text
Role(s): {persona.name}
Objective: Review recent responses and propose 3 practical improvements to increase quality and speed.
Output format: improvement, expected impact, effort (low/medium/high), success metric.
```

Study prompt:
```text
Role(s): {persona.name}
Context: I am studying [attack/technique/concept] in an authorized lab.
Objective: Explain from your perspective: {study_focus}
Output format:
- Attack view (high-level and ethical)
- Defense view
- Detection approach
- Where it fits (ATT&CK/kill chain)
- Common learner mistakes
```
"""


def render_persona_prompts(personas: list[Persona]) -> str:
    generated_at = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    header = f"""# Cyber Squad: Persona Prompts (Auto-generated)

> Generated by `cybersquad generate prompts` at {generated_at}.
> Do not edit this file manually; update `personas.yaml` and regenerate.

## Standard prompt format (recommended)

```text
Role(s): [primary persona + optional collaborator]
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [logs, alerts, CVEs, IOCs, configurations]
Constraints: [time, business impact, change limits]
Output format: [checklist, table, runbook, executive summary]
Decision needed: [approve, escalate, contain, prioritize]
```
"""

    blocks = [
        _render_persona_block(i, persona) for i, persona in enumerate(personas, start=1)
    ]

    footer = """
## Day-to-day usability tips

- Use a quick prompt for immediate decisions and collaborative mode for validation.
- Keep scope bounded by time and assets to avoid vague responses.
- Always include "Decision needed" in the request.
- Run a weekly skill-improvement prompt.
"""

    return header.rstrip() + "\n\n" + "\n".join(blocks).rstrip() + "\n\n" + footer.lstrip()


def render_single_persona_prompt(persona: Persona) -> str:
    collab, collab_goal = _collaboration(persona)
    study_focus = _study_focus(persona)
    when_lines = "\n".join(f"- {item}" for item in _when_to_use(persona))

    return f"""# {persona.name} - Usage Prompt

Role: {persona.role}

When to use:
{when_lines}

Base prompt:
```text
Role(s): {persona.name}
Context: [environment, assets, time window]
Objective: [outcome needed now]
Inputs: [available data]
Constraints: [time, impact, limits]
Output format: [recommended action + confidence + next steps]
Decision needed: [approve/escalate/prioritize]
```

Collaborative prompt:
```text
Role(s): {persona.name} + {collab}
Objective: {collab_goal}
Output format: role-by-role findings + consolidated recommendation + risks.
```

Study prompt:
```text
Role(s): {persona.name}
Context: Study of [attack/technique] in an authorized lab environment.
Objective: Explain the topic from your perspective: {study_focus}
Output format:
- Offensive perspective (high-level)
- Defensive perspective
- Detection and monitoring
- Related frameworks (ATT&CK/kill chain)
```
"""


def generate_usage_prompts(
    workspace: Path,
    output_file: Path,
    per_persona_dir: Path,
    overwrite: bool,
) -> int:
    personas_path = workspace / "personas.yaml"
    if not personas_path.exists():
        print(f"personas.yaml not found at {personas_path}")
        return 1

    personas = load_personas(personas_path)
    if not personas:
        print("No personas found in personas.yaml")
        return 1

    output_file.parent.mkdir(parents=True, exist_ok=True)
    if output_file.exists() and not overwrite:
        print(f"Output already exists: {output_file}")
        print("Use --overwrite to replace it.")
        return 1

    output_file.write_text(render_persona_prompts(personas), encoding="utf-8")

    per_persona_dir.mkdir(parents=True, exist_ok=True)
    if overwrite:
        for existing in per_persona_dir.glob("*.md"):
            existing.unlink()

    for persona in personas:
        filename = f"{persona.id}-{_slugify(persona.name)}.md"
        target = per_persona_dir / filename
        if target.exists() and not overwrite:
            continue
        target.write_text(render_single_persona_prompt(persona), encoding="utf-8")

    print(f"Generated: {output_file}")
    print(f"Generated per-persona prompts in: {per_persona_dir}")
    return 0
