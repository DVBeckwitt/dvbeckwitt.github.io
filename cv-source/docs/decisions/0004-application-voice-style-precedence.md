# 0004: Application Voice Style Precedence

## Status

Accepted

## Date

2026-06-24

## Context

The application-material workflow already controlled factual claims through
`data/cv_master.json`, the LaTeX CV source, teaching documents, and
user-provided updates. The remaining quality problem was editorial: active
guidance still encouraged some generic job-application patterns that David
removed in manual edits.

Those patterns included mandatory role-need to evidence to contribution
paragraph flow, cautious `I believe ... maps well ...` sentences, default
`Re:` subject lines, target-role banners, and contribution sentences after
body paragraphs where the evidence was already clear.

The risk was not fabricated facts. It was a resume or cover letter that used
true evidence but sounded over-explained, too promotional, or less like
David's preferred first-person application voice.

## Decision

User-edited application documents are authoritative for voice, density,
structure, and degree of self-promotion. They are not authoritative for
factual claims, grammar mistakes, or job-specific terminology.

Cover letters and resume summaries now default to direct first person unless
David requests another convention or a specific document type justifies it.
Tailoring should happen primarily through evidence selection, ordering,
section names, and accurate employer terminology.

Body paragraphs may end directly on evidence. The opening and close may
connect David's evidence to the employer, but each evidence paragraph does
not need a separate mapping or contribution sentence.

The older over-interpretive style is deprecated in active guidance:

- `I believe ... maps well ...` is prohibited-language guidance, not a
  recommended template.
- `Re:` subject lines are optional exceptions for employer requirements,
  application-channel expectations, or explicit user requests.
- Resume target-role banners are optional exceptions, with teaching-specific
  `Target Role` guidance preserved where it clarifies a highly tailored
  teaching resume.
- Supporting communication or employer-context paragraphs are optional and
  should appear only when they materially help the role.

## Alternatives Considered

### Keep generic mapping language as a cautious-fit tool

- Pros: It can prevent overclaiming in adjacent-fit roles.
- Cons: It repeatedly explains evidence the reader can already interpret and
  makes concise drafts sound like templates.
- Rejected: Adjacent-fit boundaries are still handled directly through
  training-area language without mandatory mapping sentences.

### Make preferred examples the only style source

- Pros: Examples capture real edited voice.
- Cons: Examples can contain stale facts, accidental wording, or
  job-specific terminology.
- Rejected: Examples are style references only. Evidence rules remain the
  factual authority.

### Remove every `Target Role` reference

- Pros: Simpler global rule.
- Cons: Teaching-specific resume guidance has a legitimate exception where a
  `Target Role` line can clarify a highly tailored one-page teaching resume.
- Rejected: The general default is no target-role banner, with narrow
  teaching-specific exceptions preserved.

## Consequences

- Future application materials should be shorter, more direct, and less
  interpretive.
- First-person resume summaries become the normal starting point.
- Cover-letter body paragraphs can stop after strong evidence instead of
  restating transferability.
- Human-editor passes are deletion-biased before they are polish-biased.
- Existing examples remain useful for style calibration but cannot override
  CV evidence, grammar, or application-specific terminology.
- Verification must distinguish active guidance from prohibited-language
  examples and teaching-specific exceptions.
