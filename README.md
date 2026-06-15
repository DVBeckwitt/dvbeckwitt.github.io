# David Beckwitt Website

Public academic and professional website for David Beckwitt. The site is built with Jekyll and the Hydejack theme, with custom content for research, teaching, CV, and professional profile pages.

## Tech Stack

- **Site generator:** Jekyll
- **Theme:** Hydejack
- **Language:** Ruby
- **Package manager:** Bundler
- **Content:** Markdown, HTML, YAML, Sass
- **Generated public documents:** `scripts/build_public_docs.py` exports selected CV and teaching files from `cv-source/`

## Repository Layout

- `_config.yml` controls site metadata, navigation, Hydejack settings, defaults, and plugins.
- `index.md`, `about.md`, `research.md`, `projects.md`, `cv.md`, `posts.md`, and `teaching-philosophy.md` are root public pages.
- `_projects/` contains project detail pages. `_includes/`, `_sass/`, `_data/`, and `assets/` hold theme customizations, generated includes, metadata, images, and public documents.
- `docs/` contains site documentation and project status notes.
- `scripts/build_public_docs.py` regenerates public CV and teaching exports from source material.
- `cv-source/` contains CV, resume, cover-letter, teaching, and application-source material with its own nested agent instructions.
- `AGENTS.md` governs root public-website work.
- `cv-source/AGENTS.md` governs work inside `cv-source/`.

## Local Development

Install Ruby dependencies:

```bash
bundle install
```

Build the static site:

```bash
bundle exec jekyll build
```

Preview locally:

```bash
bundle exec jekyll serve
```

Then open the local server URL printed by Jekyll, usually `http://localhost:4000`.

## Generated Public Documents

Refresh generated CV and teaching outputs before rebuilding when source material changes:

```bash
python scripts/build_public_docs.py
bundle exec jekyll build
```

Refresh only the public CV PDF from `cv-source/main.tex`:

```bash
python scripts/build_public_docs.py --cv-only
```

Do not hand-edit generated files as durable fixes. Update the source files or generator instead.

## Agent Instructions

Root website work follows `AGENTS.md`. It defines website goals, content rules, accessibility expectations, page-specific guidance, and validation workflow.

Work inside `cv-source/` follows `cv-source/AGENTS.md`. That nested guide remains the source of truth for CV, application, resume, cover-letter, and teaching-source work, including David's grounded first-person application voice.

## Current Status

See `docs/project-status.md` for the latest project status note.

Most recent documented change:

- **Content:** Synced website and drafting documentation with the current CV naming and output structure.
- **Status:** Done.
- **Bug/error status:** Fixed CV source drift by changing the area-detector item to a planned publication in structured exports and removing the duplicate 2025 BibTeX presentation entry. The old ML workflow route now redirects instead of hard-failing, but it is no longer an active tool page.
- **Validation:** Targeted stale-term searches, `git diff --check`, non-recompile CV repository checks, and pytest pass. No public-doc generation, Jekyll rebuild, or tracked CV/PDF output update was run.
