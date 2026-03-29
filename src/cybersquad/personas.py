from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Persona:
    id: str
    name: str
    role: str
    communication_style: str = ""
    consult_when: list[str] = field(default_factory=list)


def _clean_scalar(value: str) -> str:
    text = value.strip()
    if (text.startswith('"') and text.endswith('"')) or (
        text.startswith("'") and text.endswith("'")
    ):
        return text[1:-1].strip()
    return text


def parse_personas_yaml(content: str) -> list[Persona]:
    """Parse personas from our constrained YAML shape without external deps."""
    lines = content.splitlines()

    in_squad = False
    personas: list[Persona] = []
    current: Persona | None = None
    list_mode: str | None = None

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if not in_squad:
            if stripped == "squad:":
                in_squad = True
            continue

        if in_squad and line and not line.startswith(" "):
            break

        if line.startswith("  - id:"):
            if current and current.id and current.name and current.role:
                personas.append(current)
            current = Persona(id=_clean_scalar(line.split(":", 1)[1]), name="", role="")
            list_mode = None
            continue

        if current is None:
            continue

        if line.startswith("    name:"):
            current.name = _clean_scalar(line.split(":", 1)[1])
            list_mode = None
            continue

        if line.startswith("    role:"):
            current.role = _clean_scalar(line.split(":", 1)[1])
            list_mode = None
            continue

        if line.startswith("    communication_style:"):
            current.communication_style = _clean_scalar(line.split(":", 1)[1])
            list_mode = None
            continue

        if line.startswith("    consult_when:"):
            list_mode = "consult_when"
            continue

        if list_mode == "consult_when" and line.startswith("      - "):
            current.consult_when.append(_clean_scalar(line[8:]))
            continue

        if line.startswith("    ") and not line.startswith("      - "):
            list_mode = None

    if current and current.id and current.name and current.role:
        personas.append(current)

    return personas


def load_personas(path: Path) -> list[Persona]:
    return parse_personas_yaml(path.read_text(encoding="utf-8"))
