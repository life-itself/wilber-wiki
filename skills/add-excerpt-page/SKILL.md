---
name: add-excerpt-page
description: Use when adding or editing a concepts/*.md or people/*.md page in the wilber-wiki repo, or when asked to verify/audit existing excerpts there — covers page shape, sourcing, and the mandatory quote-verification step.
---

# Adding a concept or people page

## Overview

Both `concepts/*.md` and `people/*.md` pages have the same shape: a synthesis in your
own words, paired with verbatim excerpts from the source book. The two page types are
close enough to share one skill — concepts are Wilber's ideas, people are the thinkers
he engages with, but the authoring process and the quote-integrity rules are identical.

**The one rule that matters most: every quote must be real, checked text — not a
paraphrase, not a reconstruction from memory.** A page shipped once with a paraphrase
formatted as a verbatim blockquote (attribution line and all) and nothing about the
format made that visible. That is what this skill exists to prevent. See "Verifying
quotes" below — it's not optional.

## When to use

- Adding a new `concepts/<slug>.md` or `people/<slug>.md` page.
- Editing an existing page's excerpts (adding, replacing, or trimming a quote).
- Asked to audit/critique existing excerpts for accuracy (see `docs/excerpt-critique-*.md`
  for the format and depth of a full audit pass).

## Sourcing

Source from the actual book text — `library/<work-slug>-full-text.md` — never from
personal reading notes or from memory. If you're not looking at the source file with a
grep or a Read while writing a quote, you're not sourcing it, you're recalling it.

## Page shape

Frontmatter:

```yaml
---
title: <display title>
slug: <matches filename>
aliases: [<lowercase alternate names/spellings>]
category: core-term | wilber-on-x   # concepts/ only
relationship: ally | critiqued | mixed | source   # people/ only
status: draft
works: [<work-slug>, ...]           # must match a key in the verification
                                     # script's WORK_SOURCES map
---
```

Sections, in order:
1. `## Wilber's View` — synthesis in your own words. Note what's strong and what's
   contestable; this isn't a neutral encyclopedia entry.
2. `## In *<Work Title>*` — the excerpts (see below).
3. `## See Also` — `[[wikilink]]`-style cross-links to related concept/people pages.

Reference implementations: `concepts/holons.md`, `people/habermas.md`.

## Excerpts

- **Show quotes directly.** No foldable/accordion callout syntax
  (`> [!quote]- "teaser"`) — that was tried and explicitly rejected (see
  `docs/concept-wiki-vision.md`'s "Design update" section). Plain blockquote, full text,
  attribution line, done.
- **No per-excerpt heading.** The surrounding synthesis prose already gives context.
- **3-8 quotes per page** is the normal range. More is fine if the material supports it.
- **Cite the actual chapter**, not the Book/Part title ("Book 1" spans chapters 1-8 —
  don't use it as a chapter citation). If a quote is from an endnote rather than the main
  text, say so: `— *Sex, Ecology, Spirituality*, ch. 9 (footnote)`.
- **Ellipsis marks any elision.** If you're skipping text mid-quote or joining two
  non-adjacent passages, mark it with `...` — silently smoothing a join, or silently
  swapping the source's actual trailing punctuation for a period to make an excerpt read
  as a complete sentence, is exactly the kind of "close enough" edit that produces an
  unverifiable quote. Cut to the last full clause instead, or use `...`.
- **A quote starting mid-sentence keeps the source's actual capitalization** (usually
  lowercase) and leads with `...` — don't capitalize the first word to make the excerpt
  look self-starting. This was the single most common failure found when this script was
  first run against the existing wiki.
- A trailing "." can substitute for the source's real (different) closing punctuation —
  that's the one tolerance the verification script allows. A trailing quotation mark
  cannot: closing a quotation early asserts the quoted material ends there, which is a
  content change, not punctuation smoothing.
- Bold *within* a quote sparingly, only to flag the single most load-bearing phrase —
  don't bold whole sentences.

## Verifying quotes (mandatory, every time)

Before considering any page (new or edited) done, run:

```bash
python3 skills/add-excerpt-page/scripts/verify_quotes.py concepts/<slug>.md people/<slug>.md
```

(omit filenames to check the whole repo). It checks every blockquote against the actual
source file, tolerant of `...` elisions, editorially-dropped italics, and a
quote-ending "." substituted for the source's real continuation — but not tolerant of
wording that plain isn't there. **A failure means fix the quote or drop it — not
argue with the script.** See the script's own docstring for exactly what it checks and
why each tolerance exists.

### Rationalizations to watch for (yours, mid-task)

| Thought | Reality |
|---|---|
| "I'm confident this is roughly what it said" | Confidence isn't verification. Grep the source. |
| "It's basically what Wilber means here" | A paraphrase-as-quote is exactly the failure this skill exists to prevent. Either find the real sentence or write it as prose in the synthesis, not as a blockquote. |
| "I'll just end it with a period, cleaner" | If the source doesn't end there, that's a silent edit. Use `...` or stop one clause earlier. |
| "The critique/verification step is for someone else to run later" | You wrote the quote; you verify it before calling the page done. |
| "It passed a human read-through" | The fabricated Habermas quote also passed a human read-through — twice. Run the script. |

## Cross-page catalog updates

After adding a page, update `concepts/index.md` or `people/index.md` (link the new page,
keep the existing sort order), and add `[[wikilink]]`s from/to genuinely related existing
pages — don't force a link that isn't textually supported.

## Deeper background

`docs/concept-wiki-vision.md`, `docs/annotatable-reading-layer-vision.md`,
`docs/excerpt-critique-concepts.md`, `docs/excerpt-critique-people.md` — the vision docs
and the full audit-pass reports this skill's rules were distilled from.
