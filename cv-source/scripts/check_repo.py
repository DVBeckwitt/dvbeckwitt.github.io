#!/usr/bin/env python3
"""Repository verification gate for the Beckwitt_CV project."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.application_docx import extract_docx_text  # noqa: E402

DATA_DIR = ROOT / "data"
SOURCE_CV = DATA_DIR / "cv_master.json"
SCRIPTS_DIR = ROOT / "scripts"
EXPORT_SCRIPT = SCRIPTS_DIR / "export_cv_ai.py"
EXPORTS_DIR = ROOT / "exports"
APPLICATIONS_DIR = ROOT / "applications"
OUTPUTS_DIR = ROOT / "outputs"
DOCS_DIR = ROOT / "docs"
SECTIONS_DIR = ROOT / "sections"
REFEREE_TEX = SECTIONS_DIR / "referee.tex"
MAIN_TEX = ROOT / "main.tex"
BUILD_DIR = ROOT / "build"
LATEX_CHECK_DIR = BUILD_DIR / "check-latex"

EXPORT_FILES = {
    "Beckwitt_CV_AI.md": EXPORTS_DIR / "Beckwitt_CV_AI.md",
    "Beckwitt_CV_AI.json": EXPORTS_DIR / "Beckwitt_CV_AI.json",
    "Beckwitt_CV_AI.txt": EXPORTS_DIR / "Beckwitt_CV_AI.txt",
}

REQUIRED_PATHS = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "Makefile",
    ROOT / "pyproject.toml",
    ROOT / "requirements-dev.txt",
    ROOT / "uv.lock",
    ROOT / ".coveragerc",
    ROOT / ".gitleaks.toml",
    ROOT / "CONTRIBUTING.md",
    ROOT / ".editorconfig",
    ROOT / ".pre-commit-config.yaml",
    ROOT / "SECURITY.md",
    ROOT / ".github" / "CODEOWNERS",
    ROOT / ".github" / "dependabot.yml",
    ROOT / ".github" / "workflows" / "check.yml",
    ROOT / ".github" / "workflows" / "gitleaks.yml",
    ROOT / ".github" / "workflows" / "strict-latex.yml",
    ROOT / ".github" / "pull_request_template.md",
    DATA_DIR,
    SOURCE_CV,
    SCRIPTS_DIR,
    EXPORT_SCRIPT,
    SCRIPTS_DIR / "application_docx.py",
    SCRIPTS_DIR / "build_cv.py",
    SCRIPTS_DIR / "clean_build.py",
    APPLICATIONS_DIR,
    APPLICATIONS_DIR / "common" / "application_quality_checklist.md",
    OUTPUTS_DIR,
    DOCS_DIR,
    DOCS_DIR / "architecture.md",
    DOCS_DIR / "index.md",
    DOCS_DIR / "setup-windows-latex.md",
    DOCS_DIR / "decisions" / "0001-evidence-controlled-generated-outputs.md",
    DOCS_DIR / "decisions" / "0002-repository-validation-design.md",
    DOCS_DIR / "decisions" / "0003-application-output-evidence-control.md",
    EXPORTS_DIR,
    *EXPORT_FILES.values(),
    SECTIONS_DIR,
    REFEREE_TEX,
    MAIN_TEX,
]

TEXT_SUFFIXES = {
    ".bib",
    ".cfg",
    ".gitignore",
    ".json",
    ".md",
    ".py",
    ".sty",
    ".tex",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
TEXT_FILE_NAMES = {"Makefile", ".editorconfig", ".pre-commit-config.yaml"}
DOCX_SUFFIXES = {".docx"}

PUBLIC_SCAN_ROOTS = [EXPORTS_DIR, OUTPUTS_DIR, APPLICATIONS_DIR, DOCS_DIR]
PUBLIC_SCAN_FILES = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "Makefile",
    MAIN_TEX,
    ROOT / "settings.sty",
]
PLACEHOLDER_SCAN_ROOTS = [APPLICATIONS_DIR, OUTPUTS_DIR]
TRACKED_PUBLIC_BINARY_ROOTS = [DOCS_DIR / "compiled", APPLICATIONS_DIR / "examples"]
PUBLIC_BINARY_SUFFIXES = {".docx", ".pdf"}

EXPORT_DATE_LINE_RE = re.compile(r"Export date: \d{4}-\d{2}-\d{2}")
JSON_EXPORT_DATE_RE = re.compile(r'("export_date":\s*)"\d{4}-\d{2}-\d{2}"')
LATEX_INCLUDE_RE = re.compile(r"\\(?:input|makerubric)\s*\{\s*([^{}]+?)\s*\}")


@dataclass(frozen=True)
class ScanPattern:
    label: str
    regex: re.Pattern[str]


@dataclass(frozen=True)
class ScanIssue:
    path: Path
    line_number: int
    label: str
    snippet: str


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    message: str


PRIVACY_PATTERNS = [
    ScanPattern(
        "phone number",
        re.compile(r"\b(?:\+?1[\s.-]*)?(?:\(?\d{3}\)?[\s.-]*)\d{3}[\s.-]*\d{4}\b"),
    ),
    ScanPattern(
        "international phone number",
        re.compile(r"\+\d{1,3}[\s(.-]*\d{2,4}[\s).-]*\d{3,4}[\s.-]*\d{3,4}\b"),
    ),
    ScanPattern(
        "street-address-like string",
        re.compile(
            r"\b\d{1,6}\s+[A-Za-z0-9][A-Za-z0-9 .'-]{2,80}\s+"
            r"(?:Street|St\.?|Avenue|Ave\.?|Road|Rd\.?|Drive|Dr\.?|Lane|Ln\.?|"
            r"Boulevard|Blvd\.?|Court|Ct\.?|Circle|Cir\.?|Way|Trail|Trl\.?|"
            r"Parkway|Pkwy\.?|Place|Pl\.?|Building|Bldg\.?)\b",
            re.IGNORECASE,
        ),
    ),
    ScanPattern(
        "environment secret",
        re.compile(r"(?im)^\s*[A-Z0-9_]*(?:SECRET|TOKEN|API_KEY|PASSWORD|PRIVATE_KEY)\s*=\s*\S+"),
    ),
    ScanPattern(
        "private key",
        re.compile(r"BEGIN [A-Z0-9 ]*PRIVATE KEY", re.IGNORECASE),
    ),
    # Reference names can appear as advisor/collaborator context. Contact details cannot.
    ScanPattern(
        "reference contact email",
        re.compile(
            r"\b(?:micelip@missouri\.edu|guhas@missouri\.edu|cjarendse@uwc\.ac\.za)\b",
            re.IGNORECASE,
        ),
    ),
]

PLACEHOLDER_PATTERNS = [
    ScanPattern("TODO placeholder", re.compile(r"\bTODO\b", re.IGNORECASE)),
    ScanPattern("FIXME placeholder", re.compile(r"\bFIXME\b", re.IGNORECASE)),
    ScanPattern("TK placeholder", re.compile(r"\bTK\b")),
    ScanPattern(
        "insert placeholder",
        re.compile(r"\[insert[^\]]*\]|<insert[^>]*>", re.IGNORECASE),
    ),
    ScanPattern(
        "unsupported-claim marker",
        re.compile(r"unsupported[- ]claim(?:s)?", re.IGNORECASE),
    ),
]

# Narrow policy-prose allowlist. Allows checklist rule, not arbitrary unsupported-claim text.
ALLOWED_PLACEHOLDER_LINES = {
    ("applications/common/cover_letter_base_format.md", "- No unsupported claims."),
}


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def repo_relative_path(path: Path) -> Path | None:
    candidate = path if path.is_absolute() else ROOT / path
    try:
        return candidate.resolve().relative_to(ROOT)
    except ValueError:
        return None


def is_excluded_scan_path(path: Path) -> bool:
    relative_path = repo_relative_path(path)
    if relative_path is None:
        return False

    parts = relative_path.parts
    if parts[:2] == ("docs", "compiled"):
        return True
    if parts[:2] == ("applications", "examples") and "originals" in parts[2:]:
        return True
    return bool(parts and parts[0] == "outputs" and "private" in parts[1:])


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_cv() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(read_text(SOURCE_CV)))


def is_text_file(path: Path) -> bool:
    return path.name in TEXT_FILE_NAMES or path.suffix.lower() in TEXT_SUFFIXES


def is_scan_file(path: Path) -> bool:
    return is_text_file(path) or path.suffix.lower() in DOCX_SUFFIXES


def iter_text_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if path.is_file() and is_text_file(path):
            files.append(path)
            continue
        if path.is_dir():
            files.extend(
                sorted(item for item in path.rglob("*") if item.is_file() and is_text_file(item))
            )
    return sorted(set(files))


def iter_scan_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            continue
        if is_excluded_scan_path(path):
            continue
        if path.is_file() and is_scan_file(path):
            files.append(path)
            continue
        if path.is_dir():
            files.extend(
                sorted(
                    item
                    for item in path.rglob("*")
                    if item.is_file() and is_scan_file(item) and not is_excluded_scan_path(item)
                )
            )
    return sorted(set(files))


def iter_docx_files(paths: list[Path]) -> list[Path]:
    return [path for path in iter_scan_files(paths) if path.suffix.lower() in DOCX_SUFFIXES]


def read_scan_text(path: Path) -> str:
    if path.suffix.lower() in DOCX_SUFFIXES:
        return extract_docx_text(path)
    return read_text(path)


def strip_latex_comment_line(line: str) -> str:
    for index, character in enumerate(line):
        if character != "%":
            continue
        slash_count = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            slash_count += 1
            cursor -= 1
        if slash_count % 2 == 0:
            return line[:index]
    return line


def active_tex_text(path: Path) -> str:
    return "\n".join(strip_latex_comment_line(line) for line in read_text(path).splitlines())


def resolve_latex_input(raw_path: str, base_dir: Path) -> Path:
    candidate = base_dir / raw_path.strip()
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    return candidate.resolve()


def active_latex_input_paths(path: Path = MAIN_TEX) -> list[Path]:
    active_text = active_tex_text(path)
    base_dir = path.parent
    return [
        resolve_latex_input(match.group(1), base_dir)
        for match in LATEX_INCLUDE_RE.finditer(active_text)
    ]


def public_scan_files() -> list[Path]:
    files = iter_scan_files(PUBLIC_SCAN_ROOTS + PUBLIC_SCAN_FILES + active_latex_input_paths())
    return sorted(set(files))


def placeholder_scan_files() -> list[Path]:
    return iter_scan_files(PLACEHOLDER_SCAN_ROOTS)


def normalize_export_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = EXPORT_DATE_LINE_RE.sub("Export date: <DATE>", normalized)
    return JSON_EXPORT_DATE_RE.sub(r'\1"<DATE>"', normalized)


def run_command(command: list[str], timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def check_cv_json() -> CheckResult:
    required_keys = {
        "metadata",
        "identity",
        "education",
        "experience",
        "projects",
        "skills",
        "publications",
        "presentations",
        "teaching",
        "service_and_outreach",
        "awards",
        "claims_requiring_confirmation_before_use",
    }
    try:
        cv = load_cv()
    except json.JSONDecodeError as exc:
        return CheckResult("structured CV JSON", "FAIL", f"{rel(SOURCE_CV)} does not parse: {exc}")

    missing = sorted(required_keys - set(cv))
    if missing:
        return CheckResult("structured CV JSON", "FAIL", f"missing keys: {', '.join(missing)}")

    metadata = cv.get("metadata", {})
    if not isinstance(metadata, dict):
        return CheckResult("structured CV JSON", "FAIL", "metadata must be an object")
    expected_degree = "Ph.D. candidate, Physics, University of Missouri, expected May 2026"
    if metadata.get("degree_status_required_phrase") != expected_degree:
        return CheckResult("structured CV JSON", "FAIL", "required Ph.D. status phrase changed")

    return CheckResult("structured CV JSON", "PASS", f"{rel(SOURCE_CV)} parses")


def check_required_paths() -> CheckResult:
    missing = [rel(path) for path in REQUIRED_PATHS if not path.exists()]
    if missing:
        return CheckResult("required paths", "FAIL", "missing: " + ", ".join(missing))
    return CheckResult("required paths", "PASS", f"{len(REQUIRED_PATHS)} expected paths exist")


def git_tracked_files(paths: list[Path]) -> tuple[list[str], str | None]:
    result = run_command(["git", "ls-files", *[rel(path) for path in paths]], timeout=30)
    if result.returncode != 0:
        return [], (result.stdout + result.stderr).strip()
    return [line.strip() for line in result.stdout.splitlines() if line.strip()], None


def public_binary_artifact_issues(tracked_paths: list[str]) -> list[str]:
    issues: list[str] = []
    for tracked_path in tracked_paths:
        normalized = tracked_path.replace("\\", "/")
        suffix = Path(normalized).suffix.lower()
        in_compiled_pdf = normalized.startswith("docs/compiled/") and suffix == ".pdf"
        in_originals = (
            normalized.startswith("applications/examples/")
            and "/originals/" in normalized
            and suffix in PUBLIC_BINARY_SUFFIXES
        )
        if in_compiled_pdf or in_originals:
            issues.append(normalized)
    return issues


def check_public_binary_artifacts() -> CheckResult:
    tracked_paths, error = git_tracked_files(TRACKED_PUBLIC_BINARY_ROOTS)
    if error:
        return CheckResult("public binary artifacts", "FAIL", error)
    issues = public_binary_artifact_issues(tracked_paths)
    if issues:
        return CheckResult(
            "forbidden binary artifacts",
            "FAIL",
            "tracked public/private binary artifacts: " + ", ".join(issues),
        )
    return CheckResult(
        "forbidden binary artifacts",
        "PASS",
        "no tracked compiled PDFs or archived original application binaries",
    )


def compare_generated_exports() -> list[str]:
    diffs: list[str] = []
    with tempfile.TemporaryDirectory(prefix="beckwitt_cv_exports_") as tmp:
        temp_exports = Path(tmp)
        result = run_command(
            [sys.executable, str(EXPORT_SCRIPT), "--output-dir", str(temp_exports)],
            timeout=60,
        )
        if result.returncode != 0:
            output = (result.stdout + result.stderr).strip()
            return [f"export command failed: {output}"]

        for file_name, tracked_path in EXPORT_FILES.items():
            generated_path = temp_exports / file_name
            if not generated_path.exists():
                diffs.append(f"{file_name} was not generated")
                continue
            tracked = normalize_export_text(read_text(tracked_path))
            generated = normalize_export_text(read_text(generated_path))
            if tracked != generated:
                diffs.append(file_name)
    return diffs


def check_exports_fresh() -> CheckResult:
    diffs = compare_generated_exports()
    if diffs:
        return CheckResult(
            "AI export freshness",
            "FAIL",
            "stale or mismatched: " + ", ".join(diffs),
        )
    return CheckResult("AI export freshness", "PASS", "tracked exports match temp regeneration")


def find_scan_issues(paths: list[Path], patterns: list[ScanPattern]) -> list[ScanIssue]:
    issues: list[ScanIssue] = []
    for path in paths:
        if is_excluded_scan_path(path):
            continue
        try:
            text = read_scan_text(path)
        except (OSError, ValueError, zipfile.BadZipFile, ElementTree.ParseError, KeyError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for pattern in patterns:
                if pattern.regex.search(line):
                    issues.append(
                        ScanIssue(
                            path=path,
                            line_number=line_number,
                            label=pattern.label,
                            snippet=line.strip(),
                        )
                    )
    return issues


def find_docx_readability_issues(paths: list[Path] | None = None) -> list[ScanIssue]:
    issues: list[ScanIssue] = []
    for path in iter_docx_files(paths or PUBLIC_SCAN_ROOTS):
        try:
            text = extract_docx_text(path)
        except (OSError, ValueError, zipfile.BadZipFile, ElementTree.ParseError, KeyError) as exc:
            issues.append(
                ScanIssue(
                    path=path,
                    line_number=1,
                    label="unreadable DOCX",
                    snippet=str(exc),
                )
            )
            continue
        if not text.strip():
            issues.append(
                ScanIssue(
                    path=path,
                    line_number=1,
                    label="empty DOCX",
                    snippet="no readable document text",
                )
            )
    return issues


def find_privacy_issues(paths: list[Path] | None = None) -> list[ScanIssue]:
    return find_scan_issues(paths or public_scan_files(), PRIVACY_PATTERNS)


def is_allowed_placeholder(issue: ScanIssue) -> bool:
    return (rel(issue.path), issue.snippet) in ALLOWED_PLACEHOLDER_LINES


def find_placeholder_issues(paths: list[Path] | None = None) -> list[ScanIssue]:
    issues = find_scan_issues(paths or placeholder_scan_files(), PLACEHOLDER_PATTERNS)
    return [issue for issue in issues if not is_allowed_placeholder(issue)]


def format_issues(issues: list[ScanIssue]) -> str:
    return "; ".join(
        f"{rel(issue.path)}:{issue.line_number} {issue.label}: {issue.snippet}"
        for issue in issues[:10]
    )


def check_privacy() -> CheckResult:
    issues = find_privacy_issues()
    if issues:
        return CheckResult("privacy scan", "FAIL", format_issues(issues))
    return CheckResult(
        "privacy scan",
        "PASS",
        f"scanned {len(public_scan_files())} public text and DOCX files",
    )


def check_placeholders() -> CheckResult:
    issues = find_placeholder_issues()
    if issues:
        return CheckResult("placeholder scan", "FAIL", format_issues(issues))
    return CheckResult(
        "placeholder scan",
        "PASS",
        f"scanned {len(placeholder_scan_files())} template/output text and DOCX files",
    )


def check_docx_readability() -> CheckResult:
    issues = find_docx_readability_issues()
    if issues:
        return CheckResult("DOCX readability", "FAIL", format_issues(issues))
    return CheckResult(
        "DOCX readability",
        "PASS",
        f"scanned {len(iter_docx_files(PUBLIC_SCAN_ROOTS))} public DOCX files",
    )


def reference_exclusion_issues() -> list[str]:
    issues: list[str] = []
    active_inputs = {path.resolve() for path in active_latex_input_paths(MAIN_TEX)}
    if REFEREE_TEX.resolve() in active_inputs:
        issues.append("main.tex includes sections/referee.tex in active LaTeX")

    export_text = "\n".join(read_text(path) for path in EXPORT_FILES.values())
    for pattern in PRIVACY_PATTERNS:
        if pattern.label == "reference contact email" and pattern.regex.search(export_text):
            issues.append("exports include reference contact email")
    if re.search(r"Phone:\s*\+?\d", export_text, re.IGNORECASE):
        issues.append("exports include reference-style phone contact")
    return issues


def check_reference_exclusion() -> CheckResult:
    issues = reference_exclusion_issues()
    if issues:
        return CheckResult("reference exclusion", "FAIL", "; ".join(issues))
    return CheckResult(
        "reference exclusion",
        "PASS",
        "sections/referee.tex is excluded from default public CV/export paths",
    )


def latex_failure_is_toolchain_unavailable(output: str) -> bool:
    normalized = output.lower()
    toolchain_markers = [
        "could not find the script engine",
        "script engine 'perl'",
        "make sure 'perl' is installed",
        "perl' is required to execute 'latexmk'",
    ]
    return any(marker in normalized for marker in toolchain_markers)


def check_latex_compile(require_latex: bool = False) -> CheckResult:
    latexmk_name = os.environ.get("LATEXMK", "latexmk")
    latexmk = shutil.which(latexmk_name)
    if latexmk is None:
        if require_latex:
            return CheckResult("LaTeX compile", "FAIL", f"{latexmk_name} not found")
        return CheckResult("LaTeX compile", "SKIP", f"{latexmk_name} not found")

    LATEX_CHECK_DIR.mkdir(parents=True, exist_ok=True)
    try:
        result = run_command(
            [
                latexmk,
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-outdir={LATEX_CHECK_DIR}",
                str(MAIN_TEX),
            ],
            timeout=180,
        )
    except OSError as exc:
        if require_latex:
            return CheckResult("LaTeX compile", "FAIL", str(exc))
        return CheckResult("LaTeX compile", "SKIP", f"LaTeX toolchain unavailable: {exc}")
    if result.returncode != 0:
        combined_output = (result.stdout + result.stderr).strip()
        output = combined_output.splitlines()
        tail = "\n".join(output[-12:])
        if not require_latex and latex_failure_is_toolchain_unavailable(combined_output):
            return CheckResult("LaTeX compile", "SKIP", tail)
        return CheckResult("LaTeX compile", "FAIL", tail)
    return CheckResult("LaTeX compile", "PASS", f"compiled with {latexmk}")


def run_checks(require_latex: bool = False) -> list[CheckResult]:
    return [
        check_cv_json(),
        check_required_paths(),
        check_public_binary_artifacts(),
        check_docx_readability(),
        check_exports_fresh(),
        check_privacy(),
        check_placeholders(),
        check_reference_exclusion(),
        check_latex_compile(require_latex=require_latex),
    ]


def latex_required_from_env() -> bool:
    return os.environ.get("LATEX_REQUIRED", "").strip().lower() in {"1", "true", "yes", "on"}


def parse_args() -> Namespace:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-latex",
        action="store_true",
        help="Fail when latexmk is missing or LaTeX compilation fails.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run_checks(require_latex=args.require_latex or latex_required_from_env())
    for result in results:
        print(f"{result.status}: {result.name} - {result.message}")
    failures = [result for result in results if result.status == "FAIL"]
    if failures:
        print(f"FAIL: {len(failures)} required check(s) failed")
        return 1
    print("PASS: required repository checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
