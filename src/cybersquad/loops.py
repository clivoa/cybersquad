from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

from .workspace import template_root

AGENT_COMMANDS: dict[str, str] = {
    "codex": "codex exec --yolo --skip-git-repo-check -",
    "claude": 'claude -p --dangerously-skip-permissions "$(cat {prompt})"',
    "droid": "droid exec --skip-permissions-unsafe -f {prompt}",
    "opencode": 'opencode run "$(cat {prompt})"',
}

LOOP_REQUIRED_FILES = [
    ".agents/ralph/loop.sh",
    ".agents/ralph/PROMPT_build.md",
    ".agents/ralph/agents.sh",
    ".agents/ralph/config.sh",
    ".agents/tasks/prd.json",
]


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


def _resolve_path(workspace: Path, value: str | None, default_relative: str) -> Path:
    if value:
        candidate = Path(value)
        if candidate.is_absolute():
            return candidate
        return (workspace / candidate).resolve()
    return (workspace / default_relative).resolve()


def _normalize_status(value: object) -> str:
    if value is None:
        return "open"
    return str(value).strip().lower()


def install_loop_templates(workspace: Path, force: bool) -> int:
    workspace = workspace.resolve()
    workspace.mkdir(parents=True, exist_ok=True)

    agents_src = template_root().joinpath(".agents")
    if not agents_src.exists():
        print("Loop templates not found in package template (.agents).")
        return 1

    created: list[str] = []
    skipped: list[str] = []
    _copy_tree(agents_src, workspace / ".agents", force, created, skipped)

    (workspace / ".ralph").mkdir(parents=True, exist_ok=True)

    print(f"Installed loop templates into: {workspace / '.agents'}")
    print(f"Created/updated: {len(created)} files")
    if skipped:
        print(f"Skipped (already exists): {len(skipped)} files")
        print("Use --force to overwrite existing loop template files.")

    print("\nSuggested next steps:")
    print("1) Edit .agents/tasks/prd.json to match your operation")
    print("2) Run: cybersquad loop doctor --workspace .")
    print("3) Run: cybersquad loop build --workspace . --iterations 1 --agent codex --no-commit")
    return 0


def loop_doctor(workspace: Path, agent: str | None) -> int:
    workspace = workspace.resolve()
    missing: list[str] = []

    for rel in LOOP_REQUIRED_FILES:
        if not (workspace / rel).exists():
            missing.append(rel)

    selected_agent = (agent or "codex").strip().lower()
    if selected_agent not in AGENT_COMMANDS:
        print(f"Unknown agent: {selected_agent}")
        print("Valid options: codex, claude, droid, opencode")
        return 1

    agent_bin = AGENT_COMMANDS[selected_agent].split(" ", 1)[0]
    agent_ok = shutil.which(agent_bin) is not None

    print(f"\nCyberSquad loop doctor report for: {workspace}")
    print(f"- Loop templates present: {'yes' if not missing else 'no'}")
    print(f"- Agent selected: {selected_agent}")
    print(f"- Agent CLI available ({agent_bin}): {'yes' if agent_ok else 'no'}")

    if missing:
        print("\nMissing loop files:")
        for rel in missing:
            print(f"- {rel}")

    if missing or not agent_ok:
        print("\nStatus: FAIL")
        if missing:
            print("Run: cybersquad loop install --workspace .")
        if not agent_ok:
            print(f"Install/authenticate the '{agent_bin}' CLI before running loops.")
        return 1

    print("\nStatus: OK")
    return 0


def loop_overview(workspace: Path, prd: str | None) -> int:
    workspace = workspace.resolve()
    prd_path = _resolve_path(workspace, prd, ".agents/tasks/prd.json")

    if not prd_path.exists():
        print(f"PRD not found: {prd_path}")
        return 1

    try:
        data = json.loads(prd_path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - error formatting only
        print(f"Invalid PRD JSON: {exc}")
        return 1

    stories = data.get("stories") if isinstance(data, dict) else None
    if not isinstance(stories, list):
        print("PRD does not contain a valid 'stories' list.")
        return 1

    total = len(stories)
    done = sum(1 for s in stories if isinstance(s, dict) and _normalize_status(s.get("status")) == "done")
    in_progress = sum(
        1 for s in stories if isinstance(s, dict) and _normalize_status(s.get("status")) == "in_progress"
    )
    open_count = total - done - in_progress

    print(f"\nLoop overview: {prd_path}")
    print(f"- Stories: {total} total ({open_count} open, {in_progress} in_progress, {done} done)")

    if total == 0:
        print("- No stories defined.")
        return 0

    print("\nStories:")
    for story in stories:
        if not isinstance(story, dict):
            continue
        status = _normalize_status(story.get("status"))
        story_id = story.get("id", "US-???")
        title = story.get("title", "")
        depends_on = story.get("dependsOn") or []
        if isinstance(depends_on, list) and depends_on:
            depends_text = f" (depends on: {', '.join(str(item) for item in depends_on)})"
        else:
            depends_text = ""
        print(f"- [{status}] {story_id}: {title}{depends_text}")

    return 0


def loop_build(
    workspace: Path,
    iterations: int,
    agent: str | None,
    prd: str | None,
    progress: str | None,
    no_commit: bool,
    dry_run: bool,
) -> int:
    workspace = workspace.resolve()
    loop_script = workspace / ".agents" / "ralph" / "loop.sh"
    if not loop_script.exists():
        print(f"Loop runtime not found: {loop_script}")
        print("Run: cybersquad loop install --workspace .")
        return 1

    agent_name = (agent or "codex").strip().lower()
    if agent_name not in AGENT_COMMANDS:
        print(f"Unknown agent: {agent_name}")
        print("Valid options: codex, claude, droid, opencode")
        return 1

    env = os.environ.copy()
    env["RALPH_ROOT"] = str(workspace)
    env["AGENT_CMD"] = AGENT_COMMANDS[agent_name]
    env["PRD_PATH"] = str(_resolve_path(workspace, prd, ".agents/tasks/prd.json"))
    if progress:
        env["PROGRESS_PATH"] = str(_resolve_path(workspace, progress, ".ralph/progress.md"))
    if dry_run:
        env["RALPH_DRY_RUN"] = "1"

    cmd = ["bash", str(loop_script), "build", str(iterations)]
    if no_commit:
        cmd.append("--no-commit")

    print(f"Running loop in: {workspace}", flush=True)
    print(f"- Agent: {agent_name}", flush=True)
    print(f"- Iterations: {iterations}", flush=True)
    print(f"- PRD: {env['PRD_PATH']}", flush=True)
    if dry_run:
        print("- Mode: dry-run", flush=True)

    result = subprocess.run(cmd, cwd=workspace, env=env)
    return result.returncode
