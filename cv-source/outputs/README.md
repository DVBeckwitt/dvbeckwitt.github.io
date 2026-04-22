# Job-specific outputs

Save finished materials here using this structure:

`outputs/<company>/<role>/resume.docx`
`outputs/<company>/<role>/cover_letter.docx`
`outputs/<company>/<role>/evidence_matrix.docx`
`outputs/<company>/<role>/screening_notes.docx`

Use simple, AI-legible `.docx` files: normal paragraphs, semantic headings, hyphen bullets, one column, and no text boxes, images, tracked changes, comments, or decorative layout. Temporary Markdown drafts are fine during drafting, but they are not the default final output.

Optional files: `resume.tex`, `cover_letter.tex`, `teaching_statement.docx`, `evidence_of_teaching_effectiveness.docx`, and `application_email.docx`.

Convert a temporary Markdown draft with:

```bash
python scripts/application_docx.py outputs/<company>/<role>/resume.md outputs/<company>/<role>/resume.docx
```
