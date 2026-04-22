# 0001: Evidence-Controlled Generated Outputs

## Status

Accepted

## Context

This repository generates public resumes, cover letters, AI-readable exports, and a printable CV from controlled source material. The main risk is not software failure alone; it is publishing unsupported candidate claims, private contact details, stale generated exports, or reference information in the wrong output.

## Decision

CV facts come from controlled sources: `data/cv_master.json`, the LaTeX CV source, teaching documents, user-provided updates, and job postings only for employer needs. Unsupported role requirements are recorded as gaps rather than converted into experience claims.

Generated and public outputs are verified because they are easy to reuse after source material changes. `scripts/check_repo.py` checks structured JSON, required paths, generated export freshness, public privacy boundaries, placeholder markers, `.docx` readability, reference exclusion, and forbidden tracked binary artifacts.

Referee and contact material is source-only by default. `sections/referee.tex` may contain reference information, but it must stay out of default CV builds and AI exports unless an application explicitly asks for references and David approves inclusion.

Generated PDFs and original archived application binaries are not tracked because they can expose stale content or private application material. Current job-specific application packages may use tracked `.docx` files when they are simple, AI-legible, and pass repository validation.

LaTeX compilation is optional by default because agents and Windows contributors may not have a complete TeX stack. The default gate may skip only LaTeX availability or toolchain failures. Strict mode, `python scripts/check_repo.py --require-latex` or `LATEX_REQUIRED=1`, fails on missing `latexmk` or any nonzero compile result when a full toolchain is required.

## Consequences

- Default validation remains useful on machines without full LaTeX support.
- Strict validation still exists for release-quality printable CV checks.
- Privacy, evidence, export, `.docx`, binary, reference, and placeholder checks stay mandatory.
- Contributors must report skipped LaTeX checks separately from passed checks.
