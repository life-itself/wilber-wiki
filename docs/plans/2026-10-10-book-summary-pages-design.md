# Book summary pages: structure and process

Design for epic `wilberwiki-o1s` (bead `wilberwiki-o1s.1`), 2026-10-10. Covers summary pages for the three books held in full text: *Sex, Ecology, Spirituality* (SES), *Integral Psychology* (IP) and *Integral Spirituality* (IS). Writing waits for Rufus's decision on the open questions at the end (`wilberwiki-o1s.2`).

## Starting point

- Each book already has a works page (`works/1995-sex-ecology-spirituality.md`, `works/2000-integral-psychology.md`, `works/2006-integral-spirituality.md`) with a Description and an `## In-Depth Overview` of roughly 300–600 words. The overviews were written from memory and reading notes before the full texts were in the repo, and they cite no chapters. At least one is wrong about structure: the SES overview refers to "Part One, 'The Patterns of Existence'", but the book is actually Book One (ch. 1–8) and Book Two (ch. 9–14).
- Every excerpt attribution on the wiki (436+) already links to these works pages (`wilberwiki-e9q`), so they are already where readers land for "this book".
- Concept and people pages carry verified excerpts. The new concept page `concepts/from-ses-to-integral-spirituality.md` already compares all three books, so the summaries should link to it rather than repeat it.

The three books' shapes, which the structure has to fit:

| Book | Structure in the full text | Size |
|---|---|---|
| SES (revised 2nd ed.) | Preface to the 2nd ed.; Introduction; Book One, ch. 1–8 (holons → quadrants → human development → the transpersonal); Book Two, ch. 9–14 (the Ascending/Descending history of Western thought and modernity's "collapse of the Kosmos"); very long endnotes | ~15,200 lines, about a third of it endnotes |
| IP | Note to the Reader; Part 1 "Ground" (ch. 1–4: levels, lines, self, self-related streams); Part 2 "Path" (ch. 5–7: modernity, integrating premodern and modern, modern pioneers); Part 3 "Fruition" (ch. 8–15); the Charts | ~5,600 lines |
| IS | Note to the Reader; Introduction (the integral approach); ch. 1–10; Appendixes I–III | ~5,300 lines |

## Recommendation: extend the existing works page

Turn each of the three works pages into the book's summary page, rather than creating a parallel `summaries/` page. One page per book keeps all the existing attribution links pointing at the richest page, avoids two half-overlapping pages, and the works hub and catalog already lead there. Only these three "full-text" books get the expanded shape; the other works pages keep their short form. (Alternative: a separate `works/<slug>-summary.md`, linked from the works page. It's cleaner if you want works pages to stay purely bibliographic, but every attribution link would land one click short of the summary.)

## Page structure

Sections in order, with target lengths. Headings are fixed, so the three pages read as a set.

1. **Header (existing).** Title, subtitle, year, format and cover, unchanged, plus a one-line orientation such as "Wilber's central theoretical work; volume one of the unfinished Kosmos trilogy."
2. **`## At a glance`** (~100 words). What the book is and does, and who should read it. This replaces the current `## Description`.
3. **`## Context`** (150–250 words). Where it sits in Wilber's development (link [phases](../works/phases.md) and [from SES to Integral Spirituality](../concepts/from-ses-to-integral-spirituality.md)), what it builds on and what later revised it, and which edition the wiki's text and citations use (SES = revised second edition; IP and IS = Shambhala ebooks of the original editions).
4. **`## Summary`** (250–400 words). The book's core argument in a short run of plain paragraphs, or 6–8 bullets if that reads better. A reader who stops here should know the main claims.
5. **`## Overview`** (1,500–3,000 words). A walk through the book in its own order, with one subsection (`###`) per part, plus subsections for chapters where a part is long. Chapter titles come from the full text. Each content claim cites a chapter (and an endnote where the point lives there, which matters for SES). Concept and people pages are linked inline where they come up naturally. Short phrases in quotation marks are fine; full passages go in Key passages.
6. **`## Key passages`** (6–10 excerpts). Verified blockquotes in chapter order, each preceded by a one-sentence lead-in saying why it matters. No per-excerpt headings, consistent with `skills/add-excerpt-page/SKILL.md`. Choose passages that carry the book's argument, not just ones already used on concept pages (some overlap is fine).
7. **`## What's contested`** (150–300 words). Tensions and weak points, in the same register as concept pages: what's strong, what's contestable, and where later Wilber revised himself. Only Wilber-internal points and clearly sourced external critiques; the broader critical layer is a separate epic (`wilberwiki-dxr`).
8. **`## Concepts in this book`**. A grouped list of concept pages drawing on this book, each with a one-line note on its role here. **`## People`**: the main interlocutors, linked to people pages, a short list rather than the full index.
9. **`## Publication history`** (existing facts, kept) and **`## Notes`** (Rufus's personal notes, kept; the IS page also keeps its link to the 2019 notes).

Total: roughly 2,500–4,500 words per page.

## Sourcing and verification rules

- Write from `library/<slug>-full-text.md` only, never from the old overview or from memory. Nothing in the existing overviews survives unless the full text confirms it.
- Every content claim in Summary, Overview and What's contested cites a chapter, an endnote, the preface or an appendix. Bibliographic claims keep their existing source links.
- Key passages follow the excerpt rules in `skills/add-excerpt-page/SKILL.md`. On the book's own page the attribution names only the location: `— ch. 4, “A View from Within”`. This doesn't trip the title-link check, and linking a page to itself would be odd.
- Extend `verify_quotes.py` to cover these pages. A works page that sets `works: [<its own slug>]` in its frontmatter gets checked, and other works pages are skipped rather than failed. Small change; it lands with the pilot (`o1s.3`).
- Keep SES's endnotes in mind: several of its main arguments (and its replies to critics) are in the notes.

## Process

1. **Pilot: SES** (`o1s.3`). One writer works through the whole full text, so that the overview's coverage is balanced across both Books and the notes. SES first because it's the largest and hardest, and it's the book the other two build on.
2. **Independent review** (`o1s.4`). A fresh reviewer, without the writer's context, checks claims against the cited chapters, quote integrity, balance of coverage, newcomer readability, and the links. Fix the findings, then update this doc with lessons for the next two writers.
3. **IP and IS in parallel** (`o1s.5`, `o1s.6`). Separate agents apply the revised template, then a lighter review pass on each.
4. Changelog entry when the set ships.

## Open questions for Rufus

1. **Location.** Extend the existing works pages (recommended) or create separate summary pages?
2. **Excerpts.** A separate Key passages section (recommended; it keeps the overview readable), or passages interleaved through the overview?
3. **Overview depth.** One subsection per part, with chapter subsections where needed (recommended), or strictly chapter-by-chapter (15 chapters for IP)?
4. **What's contested.** Include it now with Wilber-internal and clearly sourced points (recommended), or leave it out until the critical-layer epic is scoped?
5. **Length.** Is 2,500–4,500 words per page about right?
