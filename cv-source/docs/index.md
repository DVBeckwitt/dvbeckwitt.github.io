# Documentation Index

Compact map for maintainers and agents.

## Start here

- [README](../README.md) - setup, workflows, generated files, and application flow.
- [AGENTS.md](../AGENTS.md) - operating rules for evidence-controlled application materials.
- [Contributing](../CONTRIBUTING.md) - branch, PR, validation, privacy, and skipped-check reporting.
- [Security](../SECURITY.md) - privacy and disclosure handling.
- [Architecture](architecture.md) - source-of-truth map, data flow, privacy boundary, and validation workflow.

## Source and outputs

- [Structured CV data](../data/cv_master.json) - canonical structured evidence source.
- [LaTeX CV source](../main.tex) - printable CV entry point.
- [AI-readable exports](../exports/) - generated text, Markdown, and JSON exports.
- [Application templates](../applications/common/) - intake, evidence matrix, resume, and cover-letter formats.
- [Job-specific outputs](../outputs/) - finished AI-legible `.docx` application packages.

## Validation and automation

- [Repository verifier](../scripts/check_repo.py) - primary validation gate.
- [Application DOCX helper](../scripts/application_docx.py) - convert simple drafts to `.docx` and extract `.docx` text for validation.
- [Tests](../tests/) - pytest coverage for repository checks.
- [Makefile](../Makefile) - task wrappers, including `check`, `test`, `coverage`, and `typecheck`.
- [Python project config](../pyproject.toml) and [pinned dev requirements](../requirements-dev.txt).
- [Coverage config](../.coveragerc).
- [Normal CI](../.github/workflows/check.yml) - Python checks with LaTeX optional.
- [Secret scan CI](../.github/workflows/gitleaks.yml) - Gitleaks working-tree scan.
- [Strict LaTeX CI](../.github/workflows/strict-latex.yml) - manual full LaTeX validation.
- [Windows LaTeX setup](setup-windows-latex.md).

## Decisions

- [Decision records](decisions/).
- [0001: Evidence-Controlled Generated Outputs](decisions/0001-evidence-controlled-generated-outputs.md).
- [0002: Repository Validation Design](decisions/0002-repository-validation-design.md).
- [0003: Application Output Evidence Control](decisions/0003-application-output-evidence-control.md).

## Common commands

```bash
python scripts/check_repo.py
python -m pytest
python -m pytest --cov=scripts --cov-report=term-missing
python -m ruff check .
python -m ruff format --check .
python -m mypy .
```
