# 0003: Application Output Evidence Control

## Status

Accepted

## Context

The repository produces targeted resumes, cover letters, teaching materials, job-specific `.docx` application packages, and AI-readable CV exports. The main quality risk is unsupported or stale application claims rather than code behavior alone.

## Decision

Job-specific application outputs must be drafted from the structured CV, LaTeX CV source, teaching documents, user-provided updates, and the job posting only for employer needs. Unsupported requirements are recorded as gaps in an evidence matrix instead of being converted into candidate experience.

Finished job-specific application documents default to simple, AI-legible `.docx` files in `outputs/<company>/<role>/`. They should use normal document text, semantic headings, hyphen bullets, and simple tables only where needed for evidence matrices. They should avoid columns, text boxes, images, tracked changes, comments, and decorative layout.

Generated exports are refreshed from canonical data and checked for freshness. Generated PDFs, original application binaries, private drafts, and reference-contact material stay outside tracked public outputs unless there is a deliberate documented exception. Public `.docx` outputs are allowed when they are the current finished application package and pass readability, privacy, and placeholder checks.

Default validation excludes ignored/private application originals, private output folders, and local compiled artifacts from `.docx` scans so local source-only material cannot leak through check output. Public job-specific `.docx` files under the normal output package path remain scanned before sharing. DOCX conversion preserves literal underscores in identifiers, filenames, and tool names because AI-legible application materials often contain repository paths and software names.

## Consequences

- Application materials remain targeted without inventing facts, metrics, credentials, or outcomes.
- Future agents have a clear boundary between source evidence, generated exports, and private application artifacts.
- `.docx` becomes the normal final format for generated application documents while preserving AI readability.
- Private local binaries are not opened by the default validation scans.
- Technical identifiers remain intact during DOCX conversion.
- Privacy and evidence-control checks remain part of the default validation workflow.
