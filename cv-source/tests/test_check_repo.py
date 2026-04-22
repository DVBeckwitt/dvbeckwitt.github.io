from __future__ import annotations

import subprocess
from argparse import ArgumentTypeError
from pathlib import Path

import pytest

from scripts import application_docx, check_repo, export_cv_ai


def test_cv_json_required_fields() -> None:
    cv = check_repo.load_cv()

    assert cv["metadata"]["degree_status_required_phrase"] == (
        "Ph.D. candidate, Physics, University of Missouri, expected May 2026"
    )
    assert cv["identity"]["name"] == "David Beckwitt"
    assert cv["education"]
    assert cv["experience"]
    assert cv["claims_requiring_confirmation_before_use"]


def test_export_normalization_only_masks_export_date_and_newlines() -> None:
    first = 'Export date: 2026-01-01\r\n{"export_date": "2026-01-01", "name": "David"}\r\n'
    second = 'Export date: 2026-04-21\n{"export_date": "2026-04-21", "name": "David"}\n'
    changed = 'Export date: 2026-04-21\n{"export_date": "2026-04-21", "name": "Other"}\n'

    assert check_repo.normalize_export_text(first) == check_repo.normalize_export_text(second)
    assert check_repo.normalize_export_text(first) != check_repo.normalize_export_text(changed)


def test_generated_exports_are_fresh() -> None:
    assert check_repo.compare_generated_exports() == []


def test_latex_missing_executable_skips(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: None)

    result = check_repo.check_latex_compile()

    assert result.status == "SKIP"


def test_latex_missing_executable_fails_when_required(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: None)

    result = check_repo.check_latex_compile(require_latex=True)

    assert result.status == "FAIL"


def test_latex_required_env_matches_strict_mode(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LATEX_REQUIRED", "1")
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: None)

    result = check_repo.check_latex_compile(require_latex=check_repo.latex_required_from_env())

    assert result.status == "FAIL"


def test_latex_found_perl_failure_skips_by_default(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: "latexmk")
    monkeypatch.setattr(check_repo, "LATEX_CHECK_DIR", tmp_path)
    monkeypatch.setattr(
        check_repo,
        "run_command",
        lambda *_args, **_kwargs: subprocess.CompletedProcess(
            ["latexmk"],
            1,
            "",
            "MiKTeX could not find the script engine 'perl'",
        ),
    )

    result = check_repo.check_latex_compile()

    assert result.status == "SKIP"
    assert "perl" in result.message


def test_latex_found_perl_failure_fails_when_required(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: "latexmk")
    monkeypatch.setattr(check_repo, "LATEX_CHECK_DIR", tmp_path)
    monkeypatch.setattr(
        check_repo,
        "run_command",
        lambda *_args, **_kwargs: subprocess.CompletedProcess(
            ["latexmk"],
            1,
            "",
            "MiKTeX could not find the script engine 'perl'",
        ),
    )

    result = check_repo.check_latex_compile(require_latex=True)

    assert result.status == "FAIL"
    assert "perl" in result.message


def test_latex_found_compile_failure_fails_by_default(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: "latexmk")
    monkeypatch.setattr(check_repo, "LATEX_CHECK_DIR", tmp_path)
    monkeypatch.setattr(
        check_repo,
        "run_command",
        lambda *_args, **_kwargs: subprocess.CompletedProcess(
            ["latexmk"],
            1,
            "LaTeX Error: Missing file",
            "",
        ),
    )

    result = check_repo.check_latex_compile()

    assert result.status == "FAIL"
    assert "Missing file" in result.message


def test_latex_found_compile_failure_fails_when_required(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: "latexmk")
    monkeypatch.setattr(check_repo, "LATEX_CHECK_DIR", tmp_path)
    monkeypatch.setattr(
        check_repo,
        "run_command",
        lambda *_args, **_kwargs: subprocess.CompletedProcess(
            ["latexmk"],
            1,
            "LaTeX Error: Missing file",
            "",
        ),
    )

    result = check_repo.check_latex_compile(require_latex=True)

    assert result.status == "FAIL"
    assert "Missing file" in result.message


def test_latex_found_success_passes(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(check_repo.shutil, "which", lambda _: "latexmk")
    monkeypatch.setattr(check_repo, "LATEX_CHECK_DIR", tmp_path)
    monkeypatch.setattr(
        check_repo,
        "run_command",
        lambda *_args, **_kwargs: subprocess.CompletedProcess(["latexmk"], 0, "", ""),
    )

    result = check_repo.check_latex_compile()

    assert result.status == "PASS"


def test_public_scan_files_include_active_default_sections() -> None:
    scanned = {check_repo.rel(path) for path in check_repo.public_scan_files()}

    assert "sections/education.tex" in scanned
    assert "sections/currentjob.tex" in scanned
    assert "sections/publications.tex" in scanned


def test_public_scan_files_exclude_inactive_referee_section() -> None:
    scanned = {check_repo.rel(path) for path in check_repo.public_scan_files()}

    assert "sections/referee.tex" not in scanned


def test_active_referee_section_fails_reference_exclusion(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        check_repo, "active_latex_input_paths", lambda *_args: [check_repo.REFEREE_TEX]
    )

    assert "main.tex includes sections/referee.tex in active LaTeX" in (
        check_repo.reference_exclusion_issues()
    )


def test_privacy_scanner_allows_public_email_and_flags_reference_contact(tmp_path: Path) -> None:
    allowed = tmp_path / "allowed.md"
    allowed.write_text("Email: David.Beckwitt@gmail.com\n", encoding="utf-8")
    assert check_repo.find_privacy_issues([allowed]) == []

    leaked = tmp_path / "leaked.md"
    leaked.write_text("Email: micelip@missouri.edu\nPhone: +1 573-882-8328\n", encoding="utf-8")
    issues = check_repo.find_privacy_issues([leaked])
    labels = {issue.label for issue in issues}
    assert "reference contact email" in labels
    assert "phone number" in labels or "international phone number" in labels


def test_privacy_scanner_flags_contact_data_in_active_section(tmp_path: Path) -> None:
    active_section = tmp_path / "currentjob.tex"
    active_section.write_text(
        "Phone: +1 573-882-8328\nEmail: micelip@missouri.edu\n",
        encoding="utf-8",
    )

    issues = check_repo.find_privacy_issues([active_section])
    labels = {issue.label for issue in issues}

    assert "reference contact email" in labels
    assert "phone number" in labels or "international phone number" in labels


def test_application_docx_round_trips_ai_legible_text(tmp_path: Path) -> None:
    docx_path = tmp_path / "resume.docx"
    application_docx.write_docx_from_markdown(
        "# David Beckwitt\n\n"
        "## Summary\n\n"
        "- Built `R_Axis` and Beckwitt_CV_AI tools for cover_letter drafts.\n",
        docx_path,
    )

    extracted = application_docx.extract_docx_text(docx_path)

    assert "David Beckwitt" in extracted
    assert "Summary" in extracted
    assert "- Built R_Axis and Beckwitt_CV_AI tools for cover_letter drafts." in extracted


def test_application_docx_strips_safe_markers_without_corrupting_underscores() -> None:
    cleaned = application_docx.clean_inline_markdown(
        "**Beckwitt_CV_AI** uses `cover_letter` and *R_Axis*; keep snake_case."
    )

    assert cleaned == "Beckwitt_CV_AI uses cover_letter and R_Axis; keep snake_case."


def test_privacy_scanner_reads_docx_outputs(tmp_path: Path) -> None:
    docx_path = tmp_path / "leaked.docx"
    application_docx.write_docx_from_markdown(
        "# Leaked\n\nEmail: micelip@missouri.edu\nPhone: +1 573-882-8328\n",
        docx_path,
    )

    issues = check_repo.find_privacy_issues([docx_path])
    labels = {issue.label for issue in issues}

    assert "reference contact email" in labels
    assert "phone number" in labels or "international phone number" in labels


def test_docx_readability_flags_invalid_docx(tmp_path: Path) -> None:
    bad_docx = tmp_path / "bad.docx"
    bad_docx.write_text("not a zip file", encoding="utf-8")

    issues = check_repo.find_docx_readability_issues([bad_docx])

    assert len(issues) == 1
    assert issues[0].label == "unreadable DOCX"


def test_scan_excludes_private_docx_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    private_paths = [
        check_repo.ROOT / "applications" / "examples" / "teaching" / "originals" / "leaked.docx",
        check_repo.ROOT / "outputs" / "private" / "leaked.docx",
        check_repo.ROOT / "outputs" / "company" / "role" / "private" / "leaked.docx",
        check_repo.ROOT / "docs" / "compiled" / "leaked.docx",
    ]

    for path in private_paths:
        assert check_repo.is_excluded_scan_path(path)

    assert not check_repo.is_excluded_scan_path(
        check_repo.ROOT / "outputs" / "company" / "role" / "resume.docx"
    )

    def fail_read_scan_text(_path: Path) -> str:
        raise AssertionError("private scan path should not be read")

    monkeypatch.setattr(check_repo, "read_scan_text", fail_read_scan_text)

    assert check_repo.find_privacy_issues(private_paths) == []


def test_scan_keeps_public_output_docx_visible(tmp_path: Path) -> None:
    public_docx = tmp_path / "outputs" / "company" / "role" / "resume.docx"
    application_docx.write_docx_from_markdown(
        "# Public\n\nEmail: micelip@missouri.edu\n",
        public_docx,
    )

    issues = check_repo.find_privacy_issues([public_docx])

    assert {issue.label for issue in issues} == {"reference contact email"}


def test_binary_artifact_policy_flags_public_binary_paths() -> None:
    issues = check_repo.public_binary_artifact_issues(
        [
            "docs/compiled/Beckwitt_CV_Compiled.pdf",
            "applications/examples/teaching/originals/resume.docx",
            "applications/examples/teaching/resume.md",
        ]
    )

    assert issues == [
        "docs/compiled/Beckwitt_CV_Compiled.pdf",
        "applications/examples/teaching/originals/resume.docx",
    ]


def test_no_tracked_public_binary_artifacts() -> None:
    tracked_paths, error = check_repo.git_tracked_files(check_repo.TRACKED_PUBLIC_BINARY_ROOTS)

    assert error is None
    assert check_repo.public_binary_artifact_issues(tracked_paths) == []


def test_placeholder_allowlist_is_narrow(tmp_path: Path) -> None:
    allowed_policy = check_repo.ROOT / "applications" / "common" / "cover_letter_base_format.md"
    assert check_repo.find_placeholder_issues([allowed_policy]) == []

    copied_policy = tmp_path / "copied.md"
    copied_policy.write_text("- No unsupported claims.\n", encoding="utf-8")
    issues = check_repo.find_placeholder_issues([copied_policy])
    assert len(issues) == 1
    assert issues[0].label == "unsupported-claim marker"


def test_referee_contacts_are_not_in_default_public_paths() -> None:
    assert check_repo.REFEREE_TEX.exists()
    referee_text = check_repo.REFEREE_TEX.read_text(encoding="utf-8")
    assert "micelip@missouri.edu" in referee_text
    assert check_repo.reference_exclusion_issues() == []


def test_export_date_validation() -> None:
    assert export_cv_ai.parse_export_date("2026-04-21") == "2026-04-21"

    for value in ["2026-4-21", "20260421", "2026-02-30", "tomorrow"]:
        with pytest.raises(ArgumentTypeError):
            export_cv_ai.parse_export_date(value)


def test_architecture_doc_covers_source_flow() -> None:
    architecture = (check_repo.ROOT / "docs" / "architecture.md").read_text(encoding="utf-8")

    for phrase in [
        "Source-of-truth map",
        "data/cv_master.json",
        "scripts/export_cv_ai.py",
        "Privacy boundary",
        "Evidence-control rules",
        "Validation workflow",
    ]:
        assert phrase in architecture
