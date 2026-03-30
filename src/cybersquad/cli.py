from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from . import __version__
from .loops import install_loop_templates, loop_build, loop_doctor, loop_overview
from .maint import sync_template
from .personas import load_personas, parse_personas_yaml
from .promptgen import generate_usage_prompts
from .workspace import doctor, init_workspace, list_prompt_names, read_template_text


def list_personas(workspace: Path, from_template: bool) -> int:
    if from_template:
        personas = parse_personas_yaml(read_template_text("personas.yaml"))
    else:
        personas_path = workspace / "personas.yaml"
        if not personas_path.exists():
            print(f"personas.yaml not found at {personas_path}")
            return 1
        personas = load_personas(personas_path)

    if not personas:
        print("No personas found.")
        return 1

    print("\nCyberSquad personas:")
    for persona in personas:
        print(f"- {persona.id}: {persona.name} ({persona.role})")
    return 0


def list_prompts(workspace: Path, from_template: bool) -> int:
    prompts = list_prompt_names(workspace, from_template)
    if not prompts:
        print("No prompts found.")
        return 1

    print("\nCyberSquad prompts:")
    for name in prompts:
        print(f"- {name}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cybersquad",
        description="CyberSquad CLI: install and operate a virtual cybersecurity squad workspace.",
    )

    sub = parser.add_subparsers(dest="command")

    init_cmd = sub.add_parser("init", help="Initialize a CyberSquad workspace")
    init_cmd.add_argument("target", nargs="?", default=".", help="Target directory")
    init_cmd.add_argument("--force", action="store_true", help="Overwrite existing files")
    init_cmd.add_argument("--language", default="en-US", help="Default output language")

    list_cmd = sub.add_parser("list", help="List personas or prompts")
    list_cmd.add_argument("what", choices=["personas", "prompts"])
    list_cmd.add_argument("--workspace", default=".", help="Workspace directory")
    list_cmd.add_argument(
        "--from-template",
        action="store_true",
        help="Read from bundled template instead of workspace",
    )

    doctor_cmd = sub.add_parser("doctor", help="Validate current workspace")
    doctor_cmd.add_argument("--workspace", default=".", help="Workspace directory")

    generate_cmd = sub.add_parser("generate", help="Generate prompt artifacts")
    generate_sub = generate_cmd.add_subparsers(dest="generate_what")

    generate_prompts_cmd = generate_sub.add_parser(
        "prompts", help="Generate persona usage prompts from personas.yaml"
    )
    generate_prompts_cmd.add_argument("--workspace", default=".", help="Workspace directory")
    generate_prompts_cmd.add_argument(
        "--output",
        default="prompts/persona-prompts.generated.md",
        help="Generated markdown file path (relative to workspace)",
    )
    generate_prompts_cmd.add_argument(
        "--per-persona-dir",
        default="prompts/personas",
        help="Directory to generate one prompt file per persona",
    )
    generate_prompts_cmd.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing generated files"
    )

    sync_cmd = sub.add_parser(
        "sync-template",
        help="Sync repo source personas/prompts into packaged template",
    )
    sync_cmd.add_argument(
        "--repo-root",
        default=".",
        help="Repository root containing personas.yaml, prompts/, optional opencti/, and src/cybersquad/template/",
    )
    sync_cmd.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing template files",
    )

    loop_cmd = sub.add_parser("loop", help="Manage Ralph-style loop runtime")
    loop_sub = loop_cmd.add_subparsers(dest="loop_command")

    loop_install = loop_sub.add_parser(
        "install",
        help="Install loop templates (.agents/ralph and .agents/tasks) into a workspace",
    )
    loop_install.add_argument("--workspace", default=".", help="Workspace directory")
    loop_install.add_argument("--force", action="store_true", help="Overwrite existing loop files")

    loop_doctor_cmd = loop_sub.add_parser("doctor", help="Validate loop runtime setup")
    loop_doctor_cmd.add_argument("--workspace", default=".", help="Workspace directory")
    loop_doctor_cmd.add_argument(
        "--agent",
        choices=["codex", "claude", "droid", "opencode"],
        default="codex",
        help="Agent CLI to validate",
    )

    loop_overview_cmd = loop_sub.add_parser(
        "overview", help="Show PRD story status summary for the loop"
    )
    loop_overview_cmd.add_argument("--workspace", default=".", help="Workspace directory")
    loop_overview_cmd.add_argument(
        "--prd",
        default=None,
        help="PRD JSON path (default: .agents/tasks/prd.json)",
    )

    loop_build_cmd = loop_sub.add_parser(
        "build", help="Run Ralph-style build loop for the selected PRD"
    )
    loop_build_cmd.add_argument("--workspace", default=".", help="Workspace directory")
    loop_build_cmd.add_argument(
        "--iterations", type=int, default=1, help="Number of loop iterations"
    )
    loop_build_cmd.add_argument(
        "--agent",
        choices=["codex", "claude", "droid", "opencode"],
        default="codex",
        help="Agent CLI to use",
    )
    loop_build_cmd.add_argument(
        "--prd",
        default=None,
        help="PRD JSON path (default: .agents/tasks/prd.json)",
    )
    loop_build_cmd.add_argument(
        "--progress",
        default=None,
        help="Progress log path override",
    )
    loop_build_cmd.add_argument(
        "--no-commit",
        action="store_true",
        help="Disable commits for this run",
    )
    loop_build_cmd.add_argument(
        "--dry-run",
        action="store_true",
        help="Run loop flow without calling the agent",
    )

    sub.add_parser("version", help="Show installed version")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "init":
        return init_workspace(Path(args.target), args.force, args.language)

    if args.command == "list":
        workspace = Path(args.workspace)
        if args.what == "personas":
            return list_personas(workspace, args.from_template)
        return list_prompts(workspace, args.from_template)

    if args.command == "doctor":
        return doctor(Path(args.workspace))

    if args.command == "generate":
        if args.generate_what == "prompts":
            workspace = Path(args.workspace).resolve()
            output_file = (workspace / args.output).resolve()
            per_persona_dir = (workspace / args.per_persona_dir).resolve()
            return generate_usage_prompts(
                workspace=workspace,
                output_file=output_file,
                per_persona_dir=per_persona_dir,
                overwrite=args.overwrite,
            )
        print("Missing generate target. Use: cybersquad generate prompts")
        return 1

    if args.command == "sync-template":
        return sync_template(Path(args.repo_root), overwrite=args.overwrite)

    if args.command == "loop":
        workspace = Path(getattr(args, "workspace", "."))
        if args.loop_command == "install":
            return install_loop_templates(workspace=workspace, force=args.force)
        if args.loop_command == "doctor":
            return loop_doctor(workspace=workspace, agent=args.agent)
        if args.loop_command == "overview":
            return loop_overview(workspace=workspace, prd=args.prd)
        if args.loop_command == "build":
            if args.iterations < 1:
                print("--iterations must be >= 1")
                return 1
            return loop_build(
                workspace=workspace,
                iterations=args.iterations,
                agent=args.agent,
                prd=args.prd,
                progress=args.progress,
                no_commit=args.no_commit,
                dry_run=args.dry_run,
            )
        print("Missing loop subcommand. Use: cybersquad loop [install|doctor|overview|build]")
        return 1

    if args.command == "version":
        print(__version__)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
