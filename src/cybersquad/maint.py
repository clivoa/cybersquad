from __future__ import annotations

import shutil
from pathlib import Path

GENERATED_PROMPT_FILES = {"persona-prompts.generated.md", "personas"}
OPENCTI_IGNORED_FILES = {".env", "data"}


def _ignore_generated_prompt_artifacts(
    _dir: str, entries: list[str]
) -> set[str]:
    return {name for name in entries if name in GENERATED_PROMPT_FILES}


def _ignore_opencti_local_artifacts(_dir: str, entries: list[str]) -> set[str]:
    return {name for name in entries if name in OPENCTI_IGNORED_FILES}


def sync_template(repo_root: Path, overwrite: bool) -> int:
    repo_root = repo_root.resolve()

    personas_src = repo_root / "personas.yaml"
    prompts_src = repo_root / "prompts"
    opencti_src = repo_root / "opencti"
    template_root = repo_root / "src" / "cybersquad" / "template"
    template_personas = template_root / "personas.yaml"
    template_prompts = template_root / "prompts"
    template_opencti = template_root / "opencti"

    if not personas_src.exists():
        print(f"personas.yaml not found at {personas_src}")
        return 1

    if not prompts_src.exists():
        print(f"prompts directory not found at {prompts_src}")
        return 1

    template_root.mkdir(parents=True, exist_ok=True)

    if template_personas.exists() and not overwrite:
        print(f"Template personas exists: {template_personas}")
        print("Use --overwrite to replace it.")
        return 1
    shutil.copy2(personas_src, template_personas)

    if template_prompts.exists():
        if not overwrite:
            print(f"Template prompts exists: {template_prompts}")
            print("Use --overwrite to replace it.")
            return 1
        shutil.rmtree(template_prompts)

    shutil.copytree(
        prompts_src,
        template_prompts,
        ignore=_ignore_generated_prompt_artifacts,
    )

    if opencti_src.exists():
        if template_opencti.exists():
            if not overwrite:
                print(f"Template OpenCTI assets exist: {template_opencti}")
                print("Use --overwrite to replace them.")
                return 1
            shutil.rmtree(template_opencti)

        shutil.copytree(
            opencti_src,
            template_opencti,
            ignore=_ignore_opencti_local_artifacts,
        )
        print(f"Synced OpenCTI assets to: {template_opencti}")
    else:
        print("Optional OpenCTI assets not found at repo root; skipping sync.")

    print(f"Synced personas to: {template_personas}")
    print(
        f"Synced prompts to: {template_prompts} "
        "(excluding generated persona artifacts)"
    )
    return 0
