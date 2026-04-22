# Application Materials

This directory separates reusable job-family formats from one-off application outputs.

Use this order for each application:

1. Put the job title, company, posting URL or text, and application requirements into `common/job_posting_intake.md`.
2. Use `common/evidence_matrix_template.md` to create `outputs/<company>/<role>/evidence_matrix.docx` and complete it before drafting.
3. Start from the closest job-family `resume_format.md` and `cover_letter_format.md`.
   - For teaching roles, first choose the branch inside `job_families/teaching/resume_format.md` instead of assuming every teaching resume is a lecturer resume.
4. Save finished application documents as simple `.docx` files in `outputs/<company>/<role>/`.
5. Check all claims against `../data/cv_master.json`, the LaTeX CV, teaching documents, or a user-provided update.

Temporary Markdown drafts are acceptable while writing. Convert final drafts with `python scripts/application_docx.py <draft.md> <output.docx>` and keep the final package one-column, AI-legible, and free of text boxes, images, tracked changes, comments, and decorative layout.

Common files:

- `common/job_posting_intake.md`
- `common/evidence_matrix_template.md`
- `common/resume_base_format.md`
- `common/cover_letter_base_format.md`
- `common/screening_notes_template.md`
- `common/application_quality_checklist.md`

Job families:

- `job_families/metrology/`
- `job_families/data_science/`
- `job_families/scientific_sales/`
- `job_families/teaching/`
- `job_families/neutron_xray_scattering/`

Examples are archived under `examples/`. They are writing references, not automatic evidence sources.

Current example folders:

- `examples/data_science/` for data analysis, analytics, technical analyst, and People Analytics resume and cover-letter examples.
- `examples/metrology/` for metrology resume examples.
- `examples/teaching/` for teaching resume, cover-letter, and teaching-philosophy examples.

Use `job_families/data_science/` for data science, analytics, data analyst, technical analyst, and People Analytics roles; apply the evidence-control cautions in `AGENTS.md` before using employer-domain keywords as candidate claims.
