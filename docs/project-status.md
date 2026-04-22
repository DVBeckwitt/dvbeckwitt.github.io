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
| Feature | Root website agent guide | Done | Added `AGENTS.md` at the repository root using the downloaded website guide. |
| Documentation | Root project README | Done | Replaced Hydejack starter README text with site-specific setup, structure, generated-document, and agent-instruction notes. |
| Documentation | Docs index status link | Done | Added this status page to `docs/README.md`. |
| Bug/error | Active runtime bug tied to this change | None open | This update documented guidance and project status only. No runtime bug fix was requested or applied. |
| Error | Local build command | Blocked | `bundle exec jekyll build` could not run because `bundle` is not available on PATH in this shell. `ruby` is also not available on PATH. |

## Validation

- Confirmed `AGENTS.md` matches `C:\Users\Kenpo\Downloads\AGENTS.website.md`.
- Confirmed `cv-source/AGENTS.md` was not modified.
- Build status for this docs update: blocked by missing local Ruby/Bundler on PATH.

## Follow-up

- Replace remaining Hydejack starter metadata in `_config.yml` before release-quality site work.
- Remove or create the `/projects/` target before treating main navigation as final.
- Rebuild generated CV and teaching public docs when their source files change.
