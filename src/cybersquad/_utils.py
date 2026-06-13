from __future__ import annotations

from pathlib import Path


def copy_tree(src, dst: Path, force: bool, created: list[str], skipped: list[str]) -> None:
    if src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        for child in src.iterdir():
            copy_tree(child, dst / child.name, force, created, skipped)
        return

    if dst.exists() and not force:
        skipped.append(str(dst))
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())
    created.append(str(dst))
