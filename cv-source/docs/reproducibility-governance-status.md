# Reproducibility and Governance Status

Last reviewed: 2026-04-22.

## What changed

- A real `uv.lock` was generated with `uv lock`; `requirements-dev.txt` remains the pinned pip fallback.
- Default repository verification no longer fails only because optional LaTeX tooling is missing or incomplete.
- Strict LaTeX verification was added through `python scripts/check_repo.py --require-latex` and `LATEX_REQUIRED=1`.
- Manual strict LaTeX CI was added for full TeX validation without making normal CI depend on TeX, MiKTeX, or Perl.
- LaTeX behavior is covered by mocked tests for missing `latexmk`, MiKTeX missing Perl, real compile failures, strict mode, and successful compile.
- Development tools are pinned in `requirements-dev.txt`, and CI installs with `python -m pip install -r requirements-dev.txt -e .`.
- Coverage reporting was added through pytest-cov without enforcing a threshold.
- Mypy type checking now runs with conservative stricter flags.
- Make targets now include `build`, `check-strict`, `coverage`, and `typecheck`.
- Contribution workflow, PR checklist, architecture notes, and ADR 0001 now document evidence control, privacy control, export refresh, LaTeX skip policy, and skipped-check reporting.
- ADRs now also document repository validation design and application-output evidence control.
- Job-specific application outputs now default to simple, AI-legible `.docx` files, with validation reading `.docx` text for privacy and placeholder checks.
- DOCX validation now excludes ignored/private application originals, private output folders, and compiled local artifacts while preserving validation for public output packages.
- DOCX conversion now preserves literal underscores in filenames, identifiers, and tool names while stripping safe Markdown markers.
- Dependabot now covers pip dependencies and GitHub Actions.
- Gitleaks and CODEOWNERS were added for working-tree secret scanning and ownership metadata.
- Gitleaks CI now uses the pinned Docker CLI image directly with `gitleaks dir` instead of unsupported action arguments.
- Local uv and virtual-environment directories are ignored through `.gitignore`.
- `.gitattributes` pins YAML files and `.gitignore` to LF line endings to avoid workflow and ignore-file churn across platforms.
- Agent and application-format guidance now includes the resume and cover-letter targeting philosophy for analytics, data science, technical analyst, and People Analytics roles.
- Evidence-control rules now explicitly block unsupported People Analytics, compensation, labor capitalization, workforce planning, quality-of-hire, employee-listening, HR dashboard, R programming, and advanced-professional-SQL-duration claims.
- EquipmentShare Data Analyst - People positioning and screening-answer cautions are recorded for future application work.

## Bug, error, and feature status

| Item | Status | Notes |
| --- | --- | --- |
| Bug: default `python scripts/check_repo.py` failed on Windows when MiKTeX had `latexmk` but Perl was missing | Fixed | Default check reports `SKIP: LaTeX compile`; non-LaTeX checks still fail normally. |
| Bug: DOCX scan read ignored/private originals | Fixed | Scans exclude `applications/examples/**/originals/**`, `outputs/**/private/**`, and `docs/compiled/**`; normal public `outputs/<company>/<role>/*.docx` files remain scanned. |
| Bug: DOCX converter deleted literal underscores | Fixed | Markdown cleanup preserves identifiers such as `Beckwitt_CV_AI`, `cover_letter`, and `R_Axis`; single-underscore emphasis is intentionally not stripped. |
| Bug: Gitleaks workflow used unsupported action arguments | Fixed | `.github/workflows/gitleaks.yml` now runs `ghcr.io/gitleaks/gitleaks:v8.30.1` directly with `gitleaks dir --redact --verbose --config .gitleaks.toml .`. |
| Regression risk: workflow and ignore files could churn line endings on Windows | Fixed | `.gitattributes` keeps `*.yml`, `*.yaml`, and `.gitignore` normalized to LF. |
| Error: strict LaTeX validation on the current Windows setup | Expected fail | `latexmk.exe` is present, but Perl is missing. Strict mode correctly fails until the TeX toolchain is fixed. |
| Feature: reproducible dev install | Added | Prefer `uv sync --extra dev`; use `python -m pip install -r requirements-dev.txt -e .` as the pinned pip fallback. |
| Feature: local virtual-environment ignores | Added | `.venv/`, `venv/`, `env/`, and `ENV/` are ignored. |
| Feature: coverage reporting | Added | Use `python -m pytest --cov=scripts --cov-report=term-missing`; no threshold is enforced. |
| Feature: type checking | Added | Use `python -m mypy .` or `make typecheck`. |
| Feature: contribution governance | Added | See `CONTRIBUTING.md` and the PR template. |
| Feature: AI-legible DOCX application outputs | Added | Final job-specific documents default to `.docx`; `scripts/application_docx.py` can create and read simple application documents. |
| Feature: decision history | Added | See `docs/decisions/`. |
| Feature: dependency governance | Added | Dependabot tracks pip and GitHub Actions ecosystems. |
| Feature: ownership metadata | Added | `.github/CODEOWNERS` assigns default review ownership to `@DVBeckwitt`. |
| Feature: secret scanning | Added | Gitleaks scans the current checkout in CI with the direct Docker CLI path; local validation requires Docker or Gitleaks on PATH. |
| Feature: industry analytics application-agent guidance | Added | `AGENTS.md`, data-science resume and cover-letter formats, the application README, and the application quality checklist now carry the People Analytics and evidence-control update. |
| Error status: unsupported HR-domain claims in future applications | Controlled | Agent rules now require those claims to remain gaps unless David provides direct evidence. |

## Latest local verification

- PASS: `python -m pip install uv`
- PASS: `uv lock`
- PASS with LaTeX SKIP: `python scripts/check_repo.py`
- PASS: `python -m pytest tests\test_check_repo.py`
- PASS: `python -m pytest`
- PASS: `python -m pytest --cov=scripts --cov-report=term-missing`
- PASS: `python -m ruff check .`
- PASS: `python -m ruff format --check .`
- PASS: `python -m mypy .`
- PASS: workflow YAML parsing for `.github/workflows/*.yml`
- PASS: `git diff --check`
- PASS: `python scripts/check_repo.py` after the industry analytics and People Analytics agent-guidance update, with LaTeX skipped for missing Perl.
- PASS: `git diff --name-only -- bib sections exports settings.sty main.tex data` returned no CV source, bibliography, settings, data, or generated-export churn.
- SKIP local execution: `make check`, `make build`, `make coverage`, and `make typecheck` because `make` is not installed on the current Windows PATH.
- SKIP local execution: `docker run --rm -v "$PWD:/repo" -w /repo ghcr.io/gitleaks/gitleaks:v8.30.1 dir --redact --verbose --config .gitleaks.toml .` because Docker is not installed on the current Windows PATH.
- SKIP local execution: `actionlint .github/workflows/gitleaks.yml` because `actionlint` is not installed on the current Windows PATH.
- SKIP strict LaTeX commands: `latexmk -v` reports that MiKTeX cannot find the script engine `perl`; `perl -v` is not recognized on PATH.
