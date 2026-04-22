# Data sources

`cv_master.json` is the structured evidence source for AI-readable exports and application drafting.

Update this file when David confirms new roles, metrics, publications, teaching evidence, credentials, or contact preferences. Then run:

```bash
python scripts/export_cv_ai.py
```

The LaTeX CV remains the printable academic CV source. Keep the JSON and LaTeX source aligned when content changes.
