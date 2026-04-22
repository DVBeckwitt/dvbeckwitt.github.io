---
layout: page
title: Project Status
description: >
  Current project status notes for the David Beckwitt public website.
hide_description: true
sitemap: false
permalink: /docs/project-status/
---

# Project Status

This page records recent maintenance work, feature status, and validation notes for the public website repository.

## 2026-04-22

| Type | Item | Status | Notes |
| --- | --- | --- | --- |
| Bug/error | Repository-support files exposed as site pages | Fixed | Added Jekyll exclusions for `docs/`, `licenses/`, root repository-support Markdown files, `_featured_categories/`, and old blog/doc image folders. Removed footer legal links to LICENSE, NOTICE, and CHANGELOG, and removed `LICENSE.md` from forced includes. |
| Feature | Public output boundary for professional site | Done | The site build config now favors actual website pages, research/project content, generated public docs, and assets meant for the public site. Root repo documentation remains in the repository but is excluded from Jekyll output. |
| Feature | Profile-first homepage | Done | Replaced the starter blog homepage with `index.md`, a profile-first landing page for research, projects, CV, and teaching. |
| Content | Notes archive metadata | Done | Replaced the starter `posts.md` metadata and added holding archive copy with useful links while public posts are pending. |
| Feature | Projects page and project collection | Done | Added `projects.md`, five project detail pages in `_projects/`, and local project card images under `assets/img/projects/`. |
| Content | Project identity and author metadata | Done | Replaced project-facing placeholder author data and fixed core site metadata used by project pages. |
| Bug/error | Broken Projects navigation target | Fixed | `/projects/` now has a collection-backed page instead of pointing to a missing route. |
| Feature | Root website agent guide | Done | Added `AGENTS.md` at the repository root using the downloaded website guide. |
| Documentation | Root project README | Done | Replaced Hydejack starter README text with site-specific setup, structure, generated-document, and agent-instruction notes. |
| Documentation | Docs index status link | Done | Added this status page to `docs/README.md`. |
| Bug/error | Active runtime bug tied to this change | None open | No runtime bug was part of this merge. |
| Error | Local build command | Blocked | `bundle install` could not run because `bundle` is not available on PATH. `ruby`, `gem`, and `jekyll` are also not available on PATH in this shell. |

## Validation

- Confirmed only `index.md` exists as the root index file after removing `index.html`.
- Confirmed `index.md`, `posts.md`, `projects.md`, and all `_projects/*.md` files have valid YAML front matter.
- Confirmed project image paths exist under `assets/img/projects/`.
- Confirmed `_config.yml` and `_data/authors.yml` parse as YAML and that referenced local images exist.
- Confirmed `_config.yml` contains all requested public-output exclusions.
- Confirmed actual content pages and `_projects/` are not excluded.
- Confirmed `_config.yml` no longer defines visible footer legal links to LICENSE, NOTICE, or CHANGELOG.
- Confirmed `cv-source/AGENTS.md` was not modified.
- Build status for this update: blocked because Bundler is not available on PATH in this shell.

## Follow-up

- Review the homepage, archive, and project pages visually after a successful Jekyll build, especially card ordering, image cropping, mobile width, and Hydejack project add-ons.
- Add public posts before reconsidering a blog-first homepage.
- Rebuild generated CV and teaching public docs when their source files change.
