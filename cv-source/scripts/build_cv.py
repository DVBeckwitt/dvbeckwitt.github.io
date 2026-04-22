#!/usr/bin/env python3
"""Build the printable LaTeX CV into docs/compiled/."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build" / "latex"
COMPILED_DIR = ROOT / "docs" / "compiled"
MAIN_TEX = ROOT / "main.tex"
COMPILED_PDF = COMPILED_DIR / "Beckwitt_CV_Compiled.pdf"


def main() -> int:
    latexmk_name = os.environ.get("LATEXMK", "latexmk")
    latexmk = shutil.which(latexmk_name)
    if latexmk is None:
        print("FAIL: latexmk not found; install LaTeX or run repository checks without CV build")
        return 1

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            latexmk,
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-outdir={BUILD_DIR}",
            str(MAIN_TEX),
        ],
        cwd=ROOT,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return result.returncode

    built_pdf = BUILD_DIR / "main.pdf"
    if not built_pdf.exists():
        print(f"FAIL: expected PDF not found at {built_pdf}")
        return 1
    shutil.copy2(built_pdf, COMPILED_PDF)
    print(f"Wrote {COMPILED_PDF.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
