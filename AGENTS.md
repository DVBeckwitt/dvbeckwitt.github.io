# AGENTS.md

## Scope

This file governs the public website at the repository root. The site is a Jekyll site using the Hydejack theme. It is David Beckwitt's public academic and professional site.

The nested `cv-source/AGENTS.md` governs CV, resume, cover-letter, and application-source work. Follow that file inside `cv-source/`. Do not replace it with this guide.

## Primary objective

Maintain a clear, credible, scannable website for a scientist whose work connects scattering physics, thin-film materials, instrumentation, Python modeling, and teaching.

The site should help visitors answer these questions quickly:

1. Who is David Beckwitt?
2. What does he work on?
3. What evidence supports that work?
4. What should I read, download, or click next?

Every public page should have a visible purpose, a short lead, meaningful sections, useful links, and accessible images. Do not treat Markdown as a place to dump unstructured text.

## Audience and positioning

Primary audiences:

- Research collaborators and faculty.
- Hiring committees and technical recruiters.
- Students and teaching reviewers.
- Readers interested in scattering, materials characterization, scientific software, and data analysis.

Default positioning:

- Physicist and data scientist.
- Quantitative X-ray scattering and GIWAXS analysis.
- Disorder in layered van der Waals thin films.
- Python-based modeling, simulation, and machine-learning-assisted structure analysis.
- Practical experimental work with custom instrumentation, detector data, and reproducible analysis.
- Clear teaching, active learning, peer instruction, and outreach.

Use plain technical language. Keep specialized terms when they matter, but explain them when a reader outside scattering physics would otherwise lose the thread.

## Non-negotiable content rules

Do not invent facts, titles, dates, metrics, affiliations, awards, publications, talks, tools, or project outcomes.

Use this source order for David's facts:

1. David's current explicit instruction.
2. User-provided factual updates.
3. `cv-source/data/cv_master.json`.
4. LaTeX CV source files in `cv-source/sections/`.
5. Teaching documents in `cv-source/applications/examples/teaching/`.
6. Existing public pages.
7. Generated exports, only as derived references.

State degree status conservatively unless David says otherwise: `Ph.D. candidate in Physics, University of Missouri, expected May 2026`.

Do not publish private phone numbers, addresses, references, private drafts, or job-application details unless David explicitly approves them for the website.

## UX principles for this site

People scan pages before they commit to reading. Structure pages so headings, first sentences, image captions, and link text communicate the page without requiring full linear reading.

Use these patterns:

- Put the main point in the first screen.
- Use one visible H1, normally supplied by the layout title.
- Use H2 sections for major content blocks.
- Use H3 sections for subtopics under an H2.
- Keep paragraphs short. One paragraph should usually carry one idea.
- Front-load sentences with the useful information.
- Use lists for comparisons, steps, outputs, and selected evidence.
- Use buttons only for primary actions such as CV download, project source, or contact-adjacent links.
- Put images near the text they explain.
- Add captions that explain why the image matters.
- Make link text descriptive. Avoid `click here`, `read more`, or bare URLs in body copy.
- Avoid long pages with no table of contents. Add a ToC seed list for pages longer than roughly 1200 words.
- Prefer progressive disclosure: summary first, details later.

A good public Markdown page should not feel like a PDF converted to text. If source material comes from a PDF, LaTeX file, or application document, reshape it for the web.

## Evidence-based design basis

These rules are grounded in durable UX and web-development guidance:

- Nielsen Norman Group's eye-tracking work identifies multiple web text-scanning patterns and supports strong headings, meaningful first words, and scannable structure.
- Nielsen's usability heuristics support familiar language, consistency, recognition over recall, error prevention, and minimalist design.
- W3C WCAG 2.2 requires text alternatives for non-text content unless it is decorative.
- W3C WAI image guidance says informative image alt text should communicate the meaning of the image, not merely describe pixels.
- Google Search Central recommends clear titles, unique page descriptions, people-first content, crawlable links, and useful alt text and link text.
- web.dev recommends responsive images, constrained image sizing, lazy loading where appropriate, and explicit image dimensions to reduce layout and loading problems.

Reference URLs for maintainers:

- https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/tutorials/images/informative/
- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/snippet
- https://developers.google.com/search/docs/essentials
- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- https://web.dev/learn/design/responsive-images
- https://web.dev/articles/browser-level-image-lazy-loading

## Current repository facts to respect

Root site files:

- `_config.yml` controls site metadata, menu links, collections, defaults, plugins, and Hydejack settings.
- `index.md` is currently the profile-first home page using `layout: page`.
- `posts.md` is the post archive page using `layout: list`.
- `about.md` is the public biography page using `layout: about`.
- `research.md` is the research overview page.
- `cv.md` embeds and links the public CV PDF.
- `teaching-philosophy.md` embeds a generated Markdown include and links the teaching philosophy PDF.
- `scripts/build_public_docs.py` generates public CV and teaching outputs from `cv-source/`.
- `_includes/generated/teaching-philosophy.md` is generated. Do not hand-edit it as a durable fix.
- `_sass/my-style.scss` is the main custom stylesheet.
- `_sass/my-inline.scss` is for CSS inlined into each document.
- `_includes/my-head.html` and `_includes/my-body.html` add custom HTML and scripts.

Important current facts:

- `_config.yml` uses David-specific site metadata and a `Projects` menu link to `/projects/`.
- `index.md` is a profile-first landing page. Revisit the homepage strategy only after the post library is credible.
- `posts.md` is a holding archive page for future public writing, with links back to research, projects, CV, and teaching.
- `_data/authors.yml` contains David-specific author text and public profile links.
- Check `_config.yml` for accidental punctuation in asset paths before build. The logo path should not contain a trailing backtick.

## Build and validation workflow

Before editing:

1. Inspect `_config.yml`, the target page, and any generated-source script that may overwrite the target.
2. Check whether the page is static, generated, a Jekyll post, or a Jekyll collection item.
3. If editing anything inside `cv-source/`, follow `cv-source/AGENTS.md`.

After editing public site content:

```bash
bundle install
bundle exec jekyll build
```

When CV or teaching documents need to refresh:

```bash
python scripts/build_public_docs.py
bundle exec jekyll build
```

For local preview:

```bash
bundle exec jekyll serve
```

After preview, check these pages in a browser or inspect the generated `_site` HTML:

- `/`
- `/research/`
- `/projects/` if present
- `/cv/`
- `/teaching-philosophy/`
- `/about/`
- `/posts/` or the archive URL used by the site
- At least one individual post
- At least one individual project if projects exist

Do not rely only on a successful build. Also check scannability, headings, images, captions, links, mobile width, PDF fallback text, and the first screen of each major page.

## Markdown UX rules

Every front-facing Markdown or HTML content file should include:

- Clear YAML front matter.
- A unique `title`.
- A unique `description` that accurately summarizes the page.
- A lead paragraph using `{:.lead}` when supported by the layout.
- Section headings that tell the reader what each block is for.
- At least one next action, unless the page is purely archival.

Recommended page pattern:

```md
---
layout: page
title: Page Title
description: >
  Specific one-sentence description of this page for search previews and social context.
permalink: /page-slug/
image:
  path: /assets/img/page/example.jpg
---

One to two sentences that summarize the page and make clear why it matters.
{:.lead}

## First useful section

Short paragraph. Avoid long blocks.

## Selected evidence

- Specific item with link and context.
- Specific item with link and context.

[Primary action](/target/){:.btn}
```

Do not publish a page that is only a sequence of long paragraphs. Break it into sections, figures, cards, lists, callouts, or a shorter summary plus a PDF link.

## Images, figures, and media

Store public images under `assets/img/` with clear subfolders such as:

- `assets/img/research/`
- `assets/img/projects/`
- `assets/img/posts/`
- `assets/img/about/`

Use descriptive filenames. Prefer lowercase words separated by hyphens.

For inline Markdown images, include alt text, dimensions, lazy loading, and a caption when the image carries meaning:

```md
![GIWAXS detector image showing off-specular arcs from an oriented thin film](/assets/img/research/pbi2-giwaxs-arcs.jpg){:.lead width="1200" height="800" loading="lazy"}

Off-specular arcs preserve orientational and disorder information that would be reduced in a one-dimensional profile.
{:.figcaption}
```

Alt text should communicate the image's function or meaning in context. Do not write `image`, `screenshot`, or `logo` unless that is the useful information.

Use `image.path` and `image.srcset` in front matter when a page, post, or project needs a social preview, header image, or card thumbnail.

Constrain images through CSS. Do not add fixed pixel widths that break mobile layouts. Add `width` and `height` attributes to reduce layout shift. Use `loading="lazy"` for non-critical inline images.

Avoid decorative images that add no information. If an image is decorative and implemented in HTML, use empty alt text and ensure it is ignored by assistive technology.

## Links and calls to action

Links should tell readers what they will get.

Good:

- `Download CV PDF`.
- `View 2D_Mosaic_Sim on GitHub`.
- `Read the ACS Applied Materials & Interfaces paper`.
- `See selected research outputs`.

Bad:

- `Click here`.
- `More`.
- `Link`.
- Bare URLs in body text.

Every major page should end with one or two useful next actions. Avoid giving the reader five equal-weight choices at the bottom.

## Site metadata and navigation

When updating `_config.yml`:

- Replace starter text with David-specific site description.
- Keep `title` as `David Beckwitt` unless David requests otherwise.
- Keep `tagline` short and professional.
- Keep menu labels stable and familiar: `Research`, `Projects`, `CV`, `Teaching`, `About`.
- Remove or hide a menu item if its target page does not exist.
- Use root-relative internal links such as `/research/`.
- Use full `https://` URLs only for external links.
- Do not put private contact data in config.

Recommended site description:

```yml
description: >
  David Beckwitt is a Physics Ph.D. candidate working on quantitative X-ray scattering,
  thin-film disorder, detector-space modeling, and scientific Python tools.
```

## Home and blog page instructions

Current file: `index.md`.

The home page currently uses a profile-first `page` layout because the site does not yet have enough public posts for a blog-first homepage. If the post library becomes credible, reassess whether the homepage should become `layout: blog`.

Do not leave the homepage with generic Hydejack starter metadata.

Use the home/blog page for one of these strategies:

1. Blog-first strategy. Keep `layout: blog`, retitle the page as `Notes` or `Research Notes`, and make the first screen a credible list of recent posts.
2. Profile-first strategy. Replace the home page with a static or welcome-style landing page if the site does not yet have enough posts.

For a blog-first homepage, use front matter like:

```yml
---
layout: blog
title: Research Notes
description: >
  Short posts by David Beckwitt on scattering, thin-film materials, Python modeling,
  scientific software, teaching, and research workflow.
no_link_title: false
no_excerpt: false
hide_image: false
cover: true
---
```

Homepage quality rules:

- There should be at least three real posts before making the blog layout the primary homepage.
- The newest post should not be a generic placeholder or site-update note.
- Post titles should be specific enough to stand alone in a card.
- Post descriptions should explain the value of the post, not repeat the title.
- Post images should not all use the same generic sidebar background.
- The first 40 words of each post should work as an excerpt.
- If the homepage is empty or weak, use the profile-first strategy until the post library is credible.

Recommended homepage post themes:

- Detector-space thinking for area-detector diffraction.
- Why oriented powders are not ordinary powders.
- Practical notes on GIWAXS simulation.
- Lessons from maintaining custom X-ray instrumentation.
- Teaching notes on active learning in introductory physics.
- Research software notes for `2D_Mosaic_Sim`, `ra_sim`, and `OSC_Reader`.

## Post listing and archive instructions

Current file: `posts.md`.

`posts.md` should be an archive, not a second homepage. It should help readers find writing by date, theme, or category.

Replace starter metadata. Use a title such as `Writing`, `Post Archive`, or `Notes Archive`.

Recommended front matter:

```yml
---
layout: list
title: Writing
description: >
  Archive of David Beckwitt's posts on scattering, thin-film materials,
  scientific Python, teaching, and research workflow.
permalink: /posts/
grouped: true
---
```

Archive quality rules:

- Use `grouped: true` when the archive has enough posts to benefit from year grouping.
- Use post categories and tags consistently.
- Avoid one-off category names that create sparse navigation.
- Keep post titles concise and front-loaded with specific nouns.
- Add category or tag landing pages only when there are enough posts to justify them.
- If the archive has fewer than three posts, consider hiding it from main navigation until there is enough content.

Each post should have this minimum front matter:

```yml
---
layout: post
title: Specific Post Title
description: >
  One accurate sentence that says what the post explains or argues.
date: YYYY-MM-DD
categories: [research-notes]
tags: [GIWAXS, X-ray diffraction, Python]
image:
  path: /assets/img/posts/example.jpg
---
```

Post body structure:

- Open with the claim, question, or practical problem.
- Use H2 headings every few screen lengths.
- Use figures only when they clarify the technical point.
- Add captions for detector images, plots, diagrams, and screenshots.
- Include a short conclusion or next step.
- Link related posts, research pages, projects, or the CV where useful.

Do not create posts that are just copied abstracts, copied slide text, or pasted notes. Convert source material into web-native structure.

## Research page instructions

Current file: `research.md`.

The research page should function as a guided technical overview. It should be readable by a physicist, a materials scientist, and a technical hiring reader.

Keep the first screen focused on:

- Quantitative X-ray diffraction and GIWAXS.
- Layered van der Waals thin films.
- Detector-space modeling of orientational disorder and stacking disorder.
- Python and machine-learning-assisted analysis.

Recommended structure:

1. Lead summary.
2. Dissertation focus.
3. Current themes.
4. Selected outputs.
5. Research software.
6. Earlier materials work.
7. Next action, usually CV or projects.

Research page UX rules:

- Use a ToC if the page grows beyond roughly 1200 words.
- Keep `Selected Outputs` selective. Do not turn the page into the full CV.
- Put the most externally legible output first, such as peer-reviewed papers, invited talks, or major presentations.
- Prefer 3 to 5 current research themes.
- Define uncommon acronyms on first use.
- Use images or diagrams only if they explain detector-space modeling, disorder, or materials context.
- Keep claims tied to actual work, publications, software, or dissertation scope.

Avoid making the research page a chronological autobiography. Chronology belongs in CV or About. Research should be organized by problem, method, and evidence.

## Projects page and project-item instructions

Current status: `_config.yml` links to `/projects/`, but `projects.md` and `_projects/` are not present.

Before the Projects menu link is considered ready, create either:

1. A Hydejack collection-based projects page if the installed theme supports it.
2. A normal `layout: page` project index if the collection layout is unavailable.

Collection-based option:

```md
---
layout: projects
title: Projects
description: >
  Research and software projects by David Beckwitt, including X-ray diffraction
  simulation, detector data tools, and scientific Python workflows.
permalink: /projects/
show_collection: projects
featured: true
---
```

Create project files in `_projects/`:

```md
---
layout: project
title: 2D_Mosaic_Sim
date: 2025
description: >
  Python tools for simulating X-ray diffraction patterns from materials with
  specified crystal orientations and mosaic spread.
caption: X-ray diffraction simulation tools for oriented materials.
image:
  path: /assets/img/projects/2d-mosaic-sim.jpg
links:
  - title: View source on GitHub
    url: https://github.com/DVBeckwitt/2D_Mosaic_Sim
featured: true
---

## What it does

Short explanation.

## Why it matters

Short explanation.

## Technical notes

- Specific language, library, or model.
- Specific input or output.
- Specific limitation if relevant.
```

Manual page option:

Use `layout: page`, a lead paragraph, and 3 to 6 project sections. Each project should have a short title, one-sentence value statement, 2 to 4 evidence bullets, and one link.

Project content rules:

- Emphasize the problem, method, artifact, and status.
- Name the concrete software, data type, instrument context, or output.
- Include GitHub links only where the repository is public and suitable to show.
- Avoid claiming production readiness unless the repository supports it.
- Include screenshots or diagrams only when they clarify the artifact.
- Add a limitation or current status when the project is experimental.

Recommended initial projects:

- `2D_Mosaic_Sim`.
- `ra_sim`.
- `OSC_Reader`.
- GIWAXS machine-learning simulation workflow, if public enough to describe.
- Detector-space fitting or dissertation modeling workflow, if public enough to describe.

## About page instructions

Current file: `about.md`.

The About page should be a credible human and professional overview. It should not duplicate the full Research page or CV.

Recommended structure:

1. Name and professional image.
2. Short lead identity paragraph.
3. Research snapshot.
4. Applied tools or technical strengths.
5. Teaching and outreach.
6. Background.
7. Selected recognition.
8. Buttons to CV, Research, and Teaching.

About page UX rules:

- Keep the lead personal but concise.
- Use first person for direct voice.
- Avoid long dense paragraphs.
- Keep the tool list short and concrete.
- Keep selected recognition to the strongest 4 to 6 items.
- Use the professional image with meaningful alt text, width, height, and lazy loading.
- Do not use the About page as a repository for every project, award, course, or paper.

If the About page grows long, cut or move detail to Research, Projects, CV, or Teaching.

## CV page instructions

Current file: `cv.md`.

The CV page should provide a fast download path and a readable fallback for users who cannot or do not want to use the embedded PDF.

Current public PDF path:

- `/assets/docs/beckwitt-cv.pdf`

Source-generation path:

- `scripts/build_public_docs.py`.
- `cv-source/scripts/build_cv.py`.
- `cv-source/docs/compiled/Beckwitt_CV_Compiled.pdf`.

CV page UX rules:

- Keep `Download CV PDF` as the first action.
- Include a one-sentence summary above the embed when useful.
- Keep the `<object>` fallback link.
- Keep `aria-label` on the PDF embed.
- Do not hand-edit `assets/docs/beckwitt-cv.pdf` as a durable update.
- If CV content changes, update the source and regenerate.
- If embedding becomes poor on mobile, keep the button and add a short text summary rather than relying on the embed.

Recommended body pattern:

```md
[Download CV PDF](/assets/docs/beckwitt-cv.pdf){:.btn}

The embedded PDF below is provided for quick viewing. Use the download button for the most reliable format.

<object class="pdf-embed" data="/assets/docs/beckwitt-cv.pdf" type="application/pdf" aria-label="David Beckwitt CV PDF">
  <p><a href="/assets/docs/beckwitt-cv.pdf">Download the CV PDF.</a></p>
</object>
```

## Teaching Philosophy page instructions

Current file: `teaching-philosophy.md`.

Generated include:

- `_includes/generated/teaching-philosophy.md`

Source and generator:

- `cv-source/applications/examples/teaching/teaching_philosophy_example.md`.
- `cv-source/applications/examples/teaching/teaching_philosophy_example.tex`.
- `scripts/build_public_docs.py`.

Do not leave the teaching page as a continuous text dump. This page needs web-native structure.

Durable fix requirement:

- If the generated include is too flat, update `scripts/build_public_docs.py` or the source teaching Markdown so the generated site Markdown has headings and sections.
- Do not hand-edit `_includes/generated/teaching-philosophy.md` unless the change is temporary and will not be lost on regeneration.

Recommended teaching page structure:

```md
---
layout: page
title: Teaching Philosophy
description: >
  David Beckwitt's teaching philosophy, emphasizing student-centered physics instruction,
  active learning, clear expectations, and evidence-based iteration.
permalink: /teaching-philosophy/
---

[Download Teaching Philosophy PDF](/assets/docs/teaching-philosophy.pdf){:.btn}

A short teaching summary in one or two sentences.
{:.lead}

* this list will be replaced by the table of contents
{:toc .large-only}

{% include generated/teaching-philosophy.md %}
```

Recommended generated include structure:

```md
## Core teaching commitments

Short section on rapport, clarity, and student-centered instruction.

## Small-group and tutoring instruction

Short section.

## Large-course teaching design

Short section.

## Active learning methods

### Flipped classroom

### Peer instruction

### Predict-Observe-Explain demonstrations

### Design Your Own Problem activities

## Assessment and iteration

Short section with outcomes, evidence, activities, and feedback.

## Outreach and service

Short section.

## Future development

Short section.
```

Teaching page UX rules:

- Keep the PDF button at the top.
- Use the lead paragraph to summarize the philosophy.
- Use H2 headings to make the long statement scannable.
- Use H3 headings for methods.
- Keep numbered frameworks as lists.
- Use callouts only for key principles, not for every paragraph.
- Avoid repeated claims about care, rapport, or iteration. Say each clearly once, then show methods.
- Do not bury concrete classroom practices in long narrative paragraphs.

## Individual post instructions

Create posts under `_posts/` using `YYYY-MM-DD-short-slug.md`.

Use posts for short public writing, not for raw notes. Each post should have a reader-facing point.

Good post types:

- Explainer: defines a technical idea with a figure.
- Lab note: describes a method, tool, or workflow lesson.
- Research note: summarizes a result or poster in plain technical language.
- Teaching note: describes a classroom technique and why it worked.
- Software note: introduces a tool, input, output, limitation, and link.

Do not publish:

- Unreviewed private lab details.
- Sensitive instrument or facility procedure details.
- Job-specific application writing.
- Placeholder posts.
- Slide decks copied into prose without restructuring.

Post structure:

1. One-paragraph hook or problem.
2. Brief context.
3. H2 sections for the main explanation.
4. Figure, code, or list only when useful.
5. Short ending with what the reader should take away.
6. Related link or next action.

## Styles and custom components

Use `_sass/my-style.scss` for durable custom styling. Use `_sass/my-inline.scss` only for critical styles that should be inlined.

When creating visual blocks, keep them simple and semantic. Prefer Markdown headings, lists, tables, and Hydejack-supported classes before custom HTML.

Acceptable custom components:

- Small callout boxes for key takeaways.
- Responsive card grids for project summaries.
- Figure wrappers if Markdown is insufficient.
- Compact metadata lists for project status, tools, or outputs.

Avoid:

- Heavy JavaScript for static content.
- CSS that overrides Hydejack globally without need.
- Fixed-width layouts.
- Text embedded in images.
- Decorative animations.
- Low-contrast text.

If adding CSS, verify mobile layout and dark-mode behavior.

## Accessibility checklist

Before considering a page done:

- Heading order is logical.
- There is one clear page title.
- Images have useful alt text or are explicitly decorative.
- Captions explain technical figures.
- Link text is descriptive.
- Buttons are real links with clear labels.
- PDF embeds have fallback links.
- Tables are not used for layout.
- Tables have readable headers when used for data.
- Color is not the only way information is communicated.
- Page works at mobile width.
- No important content depends on hover only.

## SEO and social preview checklist

For every public page, post, and project:

- `title` is unique, clear, and compact.
- `description` is unique and human-readable.
- The visible H1 or layout title matches the page purpose.
- Important terms appear naturally in title, H1, lead, alt text, or link text.
- Internal links use crawlable `<a href>` links generated by Markdown or HTML.
- External links point to stable, reputable targets.
- Image filenames, captions, and alt text are descriptive.
- No keyword stuffing.
- No repeated generic metadata across pages.

## Content quality checklist

Use this checklist before committing public-facing content:

- The first screen says what the page is and why it matters.
- The page is scannable without reading every paragraph.
- Long source text has been converted into sections.
- Every claim is supportable.
- No placeholders remain.
- No Hydejack starter copy remains.
- Images are compressed, local where practical, and accessible.
- Buttons and links lead somewhere useful.
- The page has a clear next action.
- Build passes.
- The generated page looks acceptable on mobile and desktop.

## When to ask David

Ask before publishing or changing:

- Degree status.
- Contact information.
- Claims about unpublished results.
- New biographical claims.
- Photos of people other than David.
- Private lab, facility, or instrument details.
- Project repositories that are not already public.
- Any claim that sounds impressive but is not directly supported.

## Preferred edits by page

Use this as a fast routing guide:

- Site identity and menu: `_config.yml`.
- Author/sidebar identity: `_data/authors.yml` and `_data/social.yml`.
- Home/blog landing: `index.md`.
- Post archive: `posts.md`.
- Individual posts: `_posts/YYYY-MM-DD-slug.md`.
- Research overview: `research.md`.
- Project index: `projects.md` or manual project page.
- Project detail pages: `_projects/<slug>.md` if collection layout is used.
- About page: `about.md`.
- CV page wrapper: `cv.md`.
- CV source and PDF: `cv-source/` plus `scripts/build_public_docs.py`.
- Teaching page wrapper: `teaching-philosophy.md`.
- Teaching generated include: update source or generator, not only `_includes/generated/teaching-philosophy.md`.
- Public PDFs: generated into `assets/docs/`.
- Public images: `assets/img/`.
- Custom styles: `_sass/my-style.scss`.

## Strongest design tradeoff

A highly structured page can feel less personal than an essay, especially for teaching philosophy and About content.

The rebuttal is that structure does not remove voice. It lets more readers find the voice. Keep the strongest personal language in the lead and section openings, then use headings, figures, and short sections to make the page usable on the web.
