# Project Status Summary

## Reorganization complete

- Added reusable resume and cover-letter formats for five job families: metrology, data science, scientific sales, teaching, and neutron/X-ray scattering.
- Added common application workflow templates: job-posting intake, evidence matrix, base resume format, and base cover-letter format.
- Added `data/cv_master.json` as a structured evidence source.
- Added `scripts/export_cv_ai.py` to generate AI-readable CV exports in Markdown, JSON, and plain text.
- Added generated exports under `exports/`.
- Moved example materials into `applications/examples/`.
- Added text/Markdown versions of example materials for AI readability.
- Kept `docs/compiled/` as the local destination for compiled PDFs.
- Removed root LaTeX build artifacts from the working tree.
- Updated `README.md`, `.gitignore`, and added a `Makefile`.
- Updated `main.tex` to omit professional contacts by default unless an application requests references.

## Verification upgrade status

- Feature complete: added `scripts/check_repo.py` as the operator-facing verification gate.
- Feature complete: added pytest coverage for JSON validity, export freshness, privacy invariants, active CV section scanning, reference exclusion, binary artifact policy, and export-date validation.
- Feature complete: added Ruff, pytest configuration, editor settings, optional pre-commit, and GitHub Actions CI.
- Feature complete: added `docs/architecture.md`, `SECURITY.md`, and a pull-request checklist.
- Privacy complete: removed tracked generated/sensitive binaries from `docs/compiled/` and `applications/examples/**/originals/`.
- Bug fixed: strict LaTeX mode fails when `latexmk` is found but the required Perl engine is missing.
- Bug fixed: default verification now reports missing or incomplete optional LaTeX tooling as a skip while still enforcing non-LaTeX checks.
- Bug fixed: privacy scans now include active default CV section files parsed from `main.tex`.
- Bug fixed: Gitleaks CI no longer uses unsupported `gitleaks/gitleaks-action@v2` arguments or the deprecated `detect` mode; it now runs the pinned Docker CLI with `gitleaks dir`.
- Regression fixed: workflow and ignore files are pinned to LF through `.gitattributes` to avoid CRLF-only churn.
- Feature complete: `.gitignore` excludes local uv and virtual-environment directories: `.venv/`, `venv/`, `env/`, and `ENV/`.
- Feature complete: merged the resume and cover-letter targeting philosophy for analytics, data science, technical analyst, and People Analytics roles into `AGENTS.md`, reusable data-science formats, the application README, and the application quality checklist.
- Feature complete: added evidence-control cautions for unsupported People Analytics, compensation, labor capitalization, workforce planning, quality-of-hire, employee-listening, HR dashboard, R programming, and advanced-professional-SQL-duration claims.
- Feature complete: recorded the EquipmentShare Data Analyst - People positioning and screening-answer cautions for future application work.
- Documentation checkpoint complete: project docs now record the analytics and People Analytics agent update, the controlled HR-domain claim risks, current validation status, and known local-tool limitations.
- Current local status: `python scripts/check_repo.py` passes on this Windows machine with LaTeX skipped because MiKTeX finds `latexmk` but lacks the Perl script engine. Strict LaTeX validation remains expected to fail until Perl or the LaTeX toolchain is fixed.
- Current local limitation: Docker and `actionlint` are not installed on PATH, so the Gitleaks Docker scan and workflow lint could not be executed locally.

## Cover-letter voice update

- Added `applications/common/cover_letter_voice_guide.md` to capture David's preferred cover-letter voice from the Beamport Engineer revision.
- Updated `AGENTS.md`, `applications/README.md`, `applications/common/cover_letter_base_format.md`, and all job-family cover-letter formats to use direct first-person, concrete technical evidence, neutral gap-control, and restrained closes.
- Added `applications/examples/cover_letter_voice/beamport_engineer_preferred_voice.md` as a style calibration example, not an evidence source.
- Verification complete: `python scripts/check_repo.py` passes and `python -m pytest -q` reports 28 passed.

## Grounded application voice update

- Updated application guidance so cover letters and resume summaries start from David's identity, concrete evidence, and candid transition language rather than generic application openings.
- Added explicit banned language for inflated or template-like phrasing such as `I am applying for...`, `uniquely qualified`, `proven track record`, `passionate about`, `leverage my skills`, `strong fit`, and `hit the ground running`.
- Updated the common resume and cover-letter formats, job-family cover-letter templates, application checklist, nested README, and Beamport voice example to reflect the grounded first-person style.

## Evidence-control note

The example resume and cover-letter files are treated as archived writing samples. New application materials should be drafted from `data/cv_master.json`, the source CV, the teaching documents, user-provided updates, and the job posting. Unsupported claims should be listed as gaps rather than reused.

For industry analyst and People Analytics roles, the current approved posture is to translate David's physics-based Python, modeling, data wrangling, visualization, documentation, and communication evidence into business-readable data work without inventing direct HR-domain or compensation experience.

## AI and simulation-to-ML evidence-control update

- Reframed AI use as bounded scientific-computing workflow support for simulation, PyTorch CNN development, documentation, reproducibility checks, literature triage, and validation planning.
- Updated canonical evidence, LaTeX CV sections, AI-readable exports, website research pages, and application templates to keep AI claims tied to simulation, ML, and scattering-constraint validation.
- Avoided unsupported claims about commercial LLM product ownership, production AI-agent deployment, production MLOps, cloud deployment ownership, or formal prompt-engineering roles.
