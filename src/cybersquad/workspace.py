from __future__ import annotations

import datetime as dt
import os
from pathlib import Path

try:
    from importlib import resources
except ImportError:  # pragma: no cover
    import importlib_resources as resources  # type: ignore

from .personas import parse_personas_yaml
from .promptgen import generate_usage_prompts

REQUIRED_PATHS = [
    "personas.yaml",
    "prompts/master-prompt.md",
    "_cybersquad/.cybersquad-version",
    "_cybersquad/config.yaml",
]


def template_root():
    return resources.files("cybersquad").joinpath("template")


def read_template_text(relative_path: str) -> str:
    return template_root().joinpath(relative_path).read_text(encoding="utf-8")


def _copy_tree(src, dst: Path, force: bool, created: list[str], skipped: list[str]) -> None:
    if src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        for child in src.iterdir():
            _copy_tree(child, dst / child.name, force, created, skipped)
        return

    if dst.exists() and not force:
        skipped.append(str(dst))
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())
    created.append(str(dst))


def _render_preferences(language: str) -> str:
    user = os.environ.get("USER") or os.environ.get("USERNAME") or "unknown"
    now = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return (
        "# CyberSquad Preferences\n\n"
        f"- User: {user}\n"
        f"- Output Language: {language}\n"
        "- Timezone: UTC\n"
        f"- Created At: {now}\n"
    )


def init_workspace(target: Path, force: bool, language: str) -> int:
    target = target.resolve()
    target.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    skipped: list[str] = []

    _copy_tree(template_root(), target, force, created, skipped)

    prefs_path = target / "_cybersquad" / "_memory" / "preferences.md"
    prefs_path.parent.mkdir(parents=True, exist_ok=True)
    prefs_path.write_text(_render_preferences(language), encoding="utf-8")
    if str(prefs_path) not in created:
        created.append(str(prefs_path))

    # Generate persona prompt artifacts on workspace bootstrap to keep
    # template packaging lean and avoid duplicated tracked prompt trees.
    prompt_result = generate_usage_prompts(
        workspace=target,
        output_file=target / "prompts" / "persona-prompts.generated.md",
        per_persona_dir=target / "prompts" / "personas",
        overwrite=True,
    )
    if prompt_result != 0:
        print("\nWarning: failed to generate persona prompt artifacts.")
        print("Run: cybersquad generate prompts --workspace . --overwrite")

    print(f"\nCyberSquad initialized at: {target}")
    print(f"Created: {len(created)} files")
    if skipped:
        print(f"Skipped (already exists): {len(skipped)} files")
        print("Tip: run with --force to overwrite existing files.")

    print("\nNext steps:")
    print("1) Open prompts/master-prompt.md")
    print("2) Pick one prompt from prompts/persona-prompts.generated.md")
    print("3) Run a scenario template from prompts/")

    return 0


def prompt_files(path: Path) -> list[Path]:
    prompts_dir = path / "prompts"
    if not prompts_dir.exists():
        return []
    return sorted(p for p in prompts_dir.glob("*.md") if p.is_file())


def list_prompt_names(workspace: Path, from_template: bool) -> list[str]:
    if from_template:
        return sorted(
            p.name
            for p in template_root().joinpath("prompts").iterdir()
            if p.is_file() and p.name.endswith(".md")
        )
    return [p.name for p in prompt_files(workspace)]


def doctor(workspace: Path) -> int:
    workspace = workspace.resolve()
    missing: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (workspace / rel).exists():
            missing.append(rel)

    prompts = prompt_files(workspace)
    personas_ok = False
    personas_path = workspace / "personas.yaml"

    if personas_path.exists():
        parsed = parse_personas_yaml(personas_path.read_text(encoding="utf-8"))
        personas_ok = len(parsed) > 0

    print(f"\nCyberSquad doctor report for: {workspace}")
    print(f"- Required paths present: {'yes' if not missing else 'no'}")
    print(f"- Prompts found: {len(prompts)}")
    print(f"- Personas parseable: {'yes' if personas_ok else 'no'}")

    if missing:
        print("\nMissing required paths:")
        for rel in missing:
            print(f"- {rel}")

    if missing or not personas_ok:
        print("\nStatus: FAIL")
        print("Run: cybersquad init . --force")
        return 1

    print("\nStatus: OK")
    return 0
