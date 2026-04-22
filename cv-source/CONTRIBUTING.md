# Contributing

This repository is evidence-controlled. Changes must preserve the privacy boundary and must not add unsupported CV or application claims.

## Branch and change expectations

- Use a focused branch for each change.
- Keep CV facts, claims, publications, dates, and degree status unchanged unless David provides confirmed source evidence.
- Keep generated exports synchronized when `data/cv_master.json` changes.
- Use simple, AI-legible `.docx` files as the default final format for job-specific application documents in `outputs/<company>/<role>/`.
- Do not track generated PDFs, archived original application binaries, private contact details, or reference-contact material.
- Do not add additional broad tooling such as Docker, Nix, ownership, or security scanners without a clear repository-specific need.

## Commands before PR

Run these before opening a PR:

```bash
python -m pip install -r requirements-dev.txt -e .
python scripts/export_cv_ai.py
python scripts/check_repo.py
python -m pytest
python -m pytest --cov=scripts --cov-report=term-missing
python -m ruff check .
python -m ruff format --check .
python -m mypy .
```

If `make` is available, these wrappers should also work:

```bash
make check
make build
make coverage
make typecheck
```

Run strict LaTeX validation when a full LaTeX toolchain is expected:

```bash
python scripts/check_repo.py --require-latex
```

## Evidence-control rules

- Every resume or cover-letter claim must be supported by `data/cv_master.json`, the source CV, teaching documents, a user-provided update, or the job posting when describing employer needs.
- Unsupported requirements must be listed as gaps in the evidence matrix.
- Do not invent metrics, certifications, sales outcomes, teaching roles, instrument experience, publications, or dates.
- Keep degree language as `Ph.D. candidate, Physics, University of Missouri, expected May 2026` unless David confirms the degree has been awarded.
- Save final generated application documents as `.docx` by default. Temporary Markdown drafts are acceptable during writing, but they are not the normal final package format.

## Privacy rules

- Do not include private phone numbers, home addresses, `.env` secrets, private keys, or reference contact details in public or generated outputs.
- `sections/referee.tex` may contain source-only reference material, but it must stay excluded from default CV builds and AI exports unless an application explicitly asks for references and David approves inclusion.
- Original application binaries and generated PDFs remain local/private artifacts unless there is a deliberate documented exception.
- Public `.docx` application outputs must remain AI-legible: one column, semantic headings, normal paragraphs, hyphen bullets, no text boxes, images, comments, tracked changes, or decorative layout.

## Generated exports

Refresh AI-readable exports after any canonical CV evidence change:

```bash
python scripts/export_cv_ai.py
```

`python scripts/check_repo.py` regenerates exports in a temporary directory and fails if tracked exports drift beyond normalized export dates and newlines.

## LaTeX unavailable or skipped

Default repository checks may report `SKIP: LaTeX compile` only when optional LaTeX tooling is missing or incomplete, such as missing `latexmk` or a known MiKTeX Perl toolchain failure.

Document skipped LaTeX checks in the PR verification notes. Use `EXPECTED FAIL` for strict LaTeX mode on machines where `latexmk` is present but the local toolchain is incomplete. Non-LaTeX checks must still pass.
