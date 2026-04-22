# 0002: Repository Validation Design

## Status

Accepted

## Context

Agents and contributors need a single reliable way to verify changes without requiring a complete local LaTeX installation. The repository also needs stricter optional validation for release-quality printable CV checks.

## Decision

`scripts/check_repo.py` is the primary repository gate. It validates required paths, structured CV JSON, generated export freshness, forbidden binary-artifact policy, `.docx` readability, privacy scans, placeholder scans, reference exclusion, and optional LaTeX compilation.

Default validation may skip only missing or incomplete optional LaTeX tooling. Strict validation uses `python scripts/check_repo.py --require-latex` or `LATEX_REQUIRED=1 python scripts/check_repo.py` and fails when LaTeX tooling is unavailable or compilation fails.

Pytest, Ruff, mypy, coverage, Gitleaks, and CI remain separate focused gates so their output stays clear and actionable.

## Consequences

- Normal CI stays usable on machines without TeX, MiKTeX, or Perl.
- Strict LaTeX validation remains available through local commands and manual CI.
- Agents can run one repository gate before sharing application materials, then use focused tools for code quality and security checks.
