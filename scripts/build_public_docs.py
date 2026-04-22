#!/usr/bin/env python3
"""Build public website documents from cv-source."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CV_ROOT = ROOT / "cv-source"
ASSET_DIR = ROOT / "assets" / "docs"
INCLUDE_DIR = ROOT / "_includes" / "generated"

CV_SCRIPT = CV_ROOT / "scripts" / "build_cv.py"
CV_COMPILED = CV_ROOT / "docs" / "compiled" / "Beckwitt_CV_Compiled.pdf"
CV_PUBLIC = ASSET_DIR / "beckwitt-cv.pdf"

TEACHING_TEX = (
    CV_ROOT
    / "applications"
    / "examples"
    / "teaching"
    / "teaching_philosophy_example.tex"
)
TEACHING_PUBLIC = ASSET_DIR / "teaching-philosophy.pdf"
TEACHING_INCLUDE = INCLUDE_DIR / "teaching-philosophy.md"


def run(command: list[str], cwd: Path) -> None:
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, text=True, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def run_result(command: list[str], cwd: Path) -> int:
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, text=True, check=False)
    return result.returncode


def direct_pdf_engine() -> str:
    engine = shutil.which("pdflatex") or shutil.which("xelatex")
    if engine is None:
        raise FileNotFoundError("Neither pdflatex nor xelatex was found")
    return engine


def latexmk_usable() -> bool:
    return shutil.which("latexmk") is not None and shutil.which("perl") is not None


def run_latex_passes(tex_path: Path, build_dir: Path, with_biber: bool) -> Path:
    engine = direct_pdf_engine()
    build_dir.mkdir(parents=True, exist_ok=True)
    command = [
        engine,
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={build_dir}",
        str(tex_path),
    ]
    run(command, cwd=CV_ROOT)
    if with_biber:
        biber = shutil.which("biber")
        if biber is None:
            raise FileNotFoundError("biber not found; cannot build bibliography")
        run(
            [
                biber,
                f"--input-directory={build_dir}",
                f"--output-directory={build_dir}",
                tex_path.stem,
            ],
            cwd=CV_ROOT,
        )
    run(command, cwd=CV_ROOT)
    run(command, cwd=CV_ROOT)
    return build_dir / f"{tex_path.stem}.pdf"


def replace_textbf(text: str) -> str:
    pattern = re.compile(r"\\textbf\{([^{}]*)\}")
    previous = None
    while previous != text:
        previous = text
        text = pattern.sub(r"**\1**", text)
    return text


def teaching_tex_to_markdown(tex: str) -> str:
    body_match = re.search(r"\\begin\{document\}(.*)\\end\{document\}", tex, re.S)
    if body_match is None:
        raise ValueError(f"Could not find document body in {TEACHING_TEX}")

    body = body_match.group(1)
    body = re.sub(r"\\href\{([^{}]+)\}\{([^{}]+)\}\\\\", r"[\2](\1)", body)
    body = re.sub(r"\\section\*\{[^{}]+\}", "", body)
    body = body.replace(r"\begin{enumerate}[label=\arabic*.]", "")
    body = body.replace(r"\end{enumerate}", "")
    body = re.sub(r"\s*\\item\s+", "\n1. ", body)
    body = body.replace(r"\pagebreak", "")
    body = replace_textbf(body)
    body = body.replace(r"\\", "\n")
    body = body.replace(r"\&", "&")
    body = re.sub(r"\{([^{}\n]+)\}", r"\1", body)
    body = re.sub(r"\n{3,}", "\n\n", body)

    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped == "Phone: [phone omitted]":
            continue
        lines.append(stripped)

    content = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return f"{content}\n"


def build_cv_pdf() -> None:
    result = 1
    if latexmk_usable():
        result = run_result([sys.executable, str(CV_SCRIPT)], cwd=CV_ROOT)
    if result != 0:
        print("Using direct TeX passes for CV PDF")
        built_pdf = run_latex_passes(CV_ROOT / "main.tex", CV_ROOT / "build" / "latex", True)
        compiled_dir = CV_COMPILED.parent
        compiled_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(built_pdf, CV_COMPILED)
    if not CV_COMPILED.exists():
        raise FileNotFoundError(f"Missing generated CV PDF: {CV_COMPILED}")
    shutil.copy2(CV_COMPILED, CV_PUBLIC)
    print(f"Wrote {CV_PUBLIC.relative_to(ROOT).as_posix()}")


def build_teaching_pdf() -> None:
    build_dir = CV_ROOT / "build" / "teaching"
    build_dir.mkdir(parents=True, exist_ok=True)
    if not latexmk_usable():
        built_pdf = run_latex_passes(TEACHING_TEX, build_dir, False)
    else:
        result = run_result(
            [
                shutil.which("latexmk") or "latexmk",
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-outdir={build_dir}",
                str(TEACHING_TEX),
            ],
            cwd=CV_ROOT,
        )
        if result != 0:
            print("latexmk teaching build failed; falling back to direct TeX passes")
            built_pdf = run_latex_passes(TEACHING_TEX, build_dir, False)
        else:
            built_pdf = build_dir / "teaching_philosophy_example.pdf"
    if not built_pdf.exists():
        raise FileNotFoundError(f"Missing generated teaching PDF: {built_pdf}")
    shutil.copy2(built_pdf, TEACHING_PUBLIC)
    print(f"Wrote {TEACHING_PUBLIC.relative_to(ROOT).as_posix()}")


def build_teaching_include() -> None:
    markdown = teaching_tex_to_markdown(TEACHING_TEX.read_text(encoding="utf-8"))
    TEACHING_INCLUDE.write_text(markdown, encoding="utf-8", newline="\n")
    print(f"Wrote {TEACHING_INCLUDE.relative_to(ROOT).as_posix()}")


def main() -> int:
    if not CV_ROOT.exists():
        raise FileNotFoundError(f"Missing CV source directory: {CV_ROOT}")
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    INCLUDE_DIR.mkdir(parents=True, exist_ok=True)

    build_teaching_include()
    build_cv_pdf()
    build_teaching_pdf()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
