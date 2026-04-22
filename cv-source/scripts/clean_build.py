#!/usr/bin/env python3
"""Remove local LaTeX/build artifacts."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
ROOT_ARTIFACT_GLOBS = [
    "*.aux",
    "*.bbl",
    "*.bcf",
    "*.blg",
    "*.fdb_latexmk",
    "*.fls",
    "*.log",
    "*.out",
    "*.run.xml",
    "*.synctex.gz",
    "comment.cut",
]


def safe_remove_build_dir() -> None:
    target = BUILD_DIR.resolve()
    if target == ROOT.resolve() or ROOT.resolve() not in target.parents:
        raise RuntimeError(f"refusing to remove unsafe path: {target}")
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)


def main() -> int:
    safe_remove_build_dir()
    for pattern in ROOT_ARTIFACT_GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file():
                path.unlink()
    print("Cleaned local build artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
