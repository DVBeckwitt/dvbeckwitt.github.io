# Architecture

## Source-of-truth map

- `data/cv_master.json` is the structured evidence source for AI-readable exports and application drafting.
- `main.tex`, `settings.sty`, `sections/`, `bib/`, and `images/` are the printable academic CV source.
- `applications/common/` and `applications/job_families/` are reusable drafting templates.
- `applications/examples/` contains archived text examples. Reuse tone and structure only after checking claims against the evidence source. Original application binaries are local/private artifacts and are not tracked.
- `exports/Beckwitt_CV_AI.*` are generated from `data/cv_master.json` by `scripts/export_cv_ai.py`.
- `outputs/` is for job-specific application packages. Finished application documents default to simple, AI-legible `.docx` files.
- `scripts/application_docx.py` converts temporary Markdown/plain-text drafts into simple `.docx` files and extracts `.docx` text for validation.
- `docs/compiled/Beckwitt_CV_Compiled.pdf` is a local ignored compiled PDF, not the canonical source.
- `docs/decisions/0001-evidence-controlled-generated-outputs.md` records the evidence-control, generated-output, privacy, binary-artifact, and LaTeX validation decisions.
- `docs/index.md` is the compact navigation map for repository docs, commands, workflows, and decision records.
- `docs/reproducibility-governance-status.md` records the latest status of the default LaTeX skip bug, strict LaTeX expected failure, and governance features.

## Data flow

1. Update `data/cv_master.json` only when David confirms new evidence, credentials, roles, metrics, or contact preferences.
2. Keep the LaTeX CV source aligned when canonical CV content changes.
3. Run `python scripts/export_cv_ai.py` to refresh the generated AI-readable Markdown, JSON, and text exports.
4. Draft targeted applications from the job posting, evidence matrix, job-family templates, and verified source evidence.
5. Save finished application materials as `.docx` files in `outputs/<company>/<role>/`.

## Canonical vs generated

Canonical files are edited by hand: `data/cv_master.json`, LaTeX source files, application templates, `README.md`, `AGENTS.md`, and documentation.

Generated files are refreshed by commands: `exports/Beckwitt_CV_AI.md`, `exports/Beckwitt_CV_AI.json`, `exports/Beckwitt_CV_AI.txt`, application `.docx` files created from temporary drafts with `scripts/application_docx.py`, and local ignored compiled PDFs under `docs/compiled/`.

## Privacy boundary

Default public outputs must not include private phone numbers, home addresses, private keys, `.env` secrets, or reference contact details. David's public email and profile links are allowed. `sections/referee.tex` may hold reference-contact source material, but it must remain excluded from default CV builds and AI exports unless an application explicitly asks for references and David approves inclusion.

## Evidence-control rules

Every resume or cover-letter claim must be supported by `data/cv_master.json`, the source CV and teaching documents, a user-provided update, or the job posting when describing employer needs. Unsupported requirements belong in the evidence matrix as gaps, not as inflated experience claims. The Ph.D. status remains `Ph.D. candidate, Physics, University of Missouri, expected May 2026` unless David confirms the degree has been awarded.

## Validation workflow

Use `python scripts/check_repo.py` as the operator-facing gate. It parses the structured CV, checks required paths, fails forbidden tracked PDF/DOCX artifacts, verifies public `.docx` files are readable, regenerates exports in a temporary directory, compares generated outputs after normalizing only export dates and newlines, scans public text and `.docx` outputs plus active default CV sections for privacy leaks, scans reusable application materials for placeholder markers, verifies `sections/referee.tex` is excluded from default public paths, and compiles LaTeX when the optional toolchain is available.

Default repository checks may skip only missing or incomplete optional LaTeX tooling. Privacy, structured JSON, export freshness, `.docx` readability, placeholder, reference-exclusion, and forbidden binary-artifact problems still fail. Use `python scripts/check_repo.py --require-latex` or `LATEX_REQUIRED=1 python scripts/check_repo.py` when the LaTeX toolchain is required; strict mode fails if `latexmk` is missing or compilation returns a nonzero exit code.

Focused pytest tests cover helper-level invariants. Coverage reporting is available with `python -m pytest --cov=scripts --cov-report=term-missing` without enforcing a threshold. Ruff enforces Python linting and formatting. Mypy type-checks the repository with conservative strictness flags. CI runs the same core local commands with pinned development tools from `requirements-dev.txt`, while strict LaTeX validation remains manual.
