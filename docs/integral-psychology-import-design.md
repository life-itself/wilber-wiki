# Importing *Integral Psychology* — design

Status: design, approved-by-default per Rufus's steer to keep moving and log open
questions rather than block on them (2026-09-12). Covers the second source book for the
concept wiki and people index, plus a new content type for the book's appendix charts.

## Why

[NEXT.md](../NEXT.md) issue [#3](https://github.com/life-itself/wilber-wiki/issues/3)'s
next step was "pick a second Wilber book to mine." Rufus has now pointed at *Integral
Psychology* specifically, for two reasons: it's ready (converted, sitting in the sibling
`library` repo, same as *SES* was before import), and its appendix — ~21 correlation
charts cross-indexing a hundred-plus developmental models against Wilber's own levels —
is valuable material that's currently locked inside scanned page images, hard to read
even in the source EPUB.

## Source material (already exists, not in this repo yet)

`/Users/rgrp/src/life-itself/library/books/wilber-integral-psychology/`:
- `markdown/wilber-integral-psychology.md` — 5,604 lines, converted from EPUB, 58
  images. Chapter structure: 15 chapters in 3 parts (Ground / Path / Fruition), matching
  the summary already in `works/2000-integral-psychology.md`.
- `markdown/images/00001.jpg`–`00058.jpg` — cover, in-text figures (images 1–15), and
  the "Charts" backmatter (images 16–57: 21 correlation charts, each split across 2–6
  page-images as `CHART <N><letter>` continuations; image 58 is a closing figure recap).
- `digest/DIGEST.md`, `anki/cards-*.tsv` — supplementary, not needed as a source (the
  skill's rule is to source excerpts from the full text, not derived notes).

No `people-source.md`-equivalent exists for this book (unlike *SES*, which had one
ready to copy in). That research has to be done fresh, the same way it originally was
for *SES* — a full-text mention-count scan.

## Decisions

**1. Import full text the same way as SES.** Copy
`markdown/wilber-integral-psychology.md` → `library/2000-integral-psychology-full-text.md`
in this repo. Add `"2000-integral-psychology": "library/2000-integral-psychology-full-text.md"`
to `WORK_SOURCES` in `skills/add-excerpt-page/scripts/verify_quotes.py`. Same
copyright-posture note as the original SES import applies (AGENTS.md's Publishing
section) — committing to the repo is pre-approved; nothing here changes the "check
before running `fl`" guidance.

**2. Copy the 58 chart/figure images into this repo too**, under
`library/2000-integral-psychology-images/`, as working reference for chart
reconstruction (see below) — not because they'll be published as-is. Excluded from
publish the same way `library/` already is (`contentExclude` in `config.json`).

**3. New `charts/` top-level directory for the reconstructed appendix charts** — not
`concepts/`. These aren't a synthesis-plus-excerpts argument page; they're reference
tables (Wilber's own correlation charts, redrawn as text/HTML instead of a scanned
image). Different shape deserves a different directory, same way `people/` split out
from `concepts/` for issue #3. `charts/index.md` catalogs them; link from
`concepts/index.md`, `people/index.md`, and site nav/`NEXT.md`.

**4. One page per logical chart, not per page-image.** The 21 `CHART <N><letter>`
labels are continuation halves of a wider table (e.g. Chart 1A + 1B together are one
table, just too wide for one print page) — reconstruct as **one page per chart number**,
with the full table in one place: `charts/chart-1-wilber-correlations.md`,
`chart-2-basic-structures-in-other-systems.md`, `chart-3-cognitive-development.md`,
`chart-4-self-related-stages.md`, `chart-5-morals-and-perspectives.md`,
`chart-6-stages-of-spirituality.md`, `chart-7-misc-developmental-lines.md`,
`chart-8-miscellaneous.md`, `chart-9-sociocultural-evolution.md`, `chart-10-habermas.md`,
`chart-11-baldwin.md`. 11 pages total, not 21.

> **Finding from the Chart 1 spike (2026-09-13): the shared-spine assumption above is
> only partly right.** Checked all four images for Chart 1 (00016-00019) against each
> other. 00016 and 00018 (Chart 1A p.1, Chart 1B p.1) really do share one identical
> row spine ("Correlative Basic Structures": sensorimotor → phantasmic-emotional →
> rep-mind → conop → formop → postformal → psychic → subtle → causal → nondual) and
> merge cleanly into one wide table (6 data columns: Self-Sense, Specific Aspects,
> Defenses, Affect, Levels of "Food"). But 00017 (Chart 1A p.2) uses a *different*,
> coarser spine keyed to Wilber's fulcrum numbering (F-0 to F-9 + Ground) — related to
> the same levels but not the same rows — and 00019 (Chart 1B p.2) uses a *third*,
> unrelated spine (archaic → magic → mythic → rational → pluralistic → integral gender/
> worldview stages). Revised rule: **a chart page holds however many distinct sub-tables
> the source actually has, in book order, not one forced merge** — for Chart 1 that's
> three tables under one page (Structures/Self-Sense/Affect/etc.; Fulcrums/Pathology/
> Treatment/Moral Span; Gender Identity/Worldviews), not one. Check each of the
> remaining 10 charts' page-images against each other the same way before assuming they
> merge — don't repeat the assumption unchecked.

**5. Chart page shape:**
```yaml
---
title: "Chart 1: Wilber Correlations"
slug: chart-1-wilber-correlations
works: [2000-integral-psychology]
chart_source: "Charts backmatter, images 00016-00019"
status: draft
---
```
- One paragraph of intro: what the chart correlates, why it's useful read outside the
  book.
- The reconstructed table. Standard Markdown tables can't express the row-spanning
  left-hand spine (e.g. "sensoriphysical" spanning 4 sub-rows) — use raw HTML
  `<table>` with `rowspan` for that column, confirmed this pattern renders under
  Flowershow before doing all 11 (first chart page doubles as that spike).
  every cell manually cross-checked against the source page image before commit — this
  is transcription accuracy, not the quote-fabrication risk `verify_quotes.py` guards
  against, so that script doesn't apply here. State in the page ("transcribed from
  Wilber's Chart N, cross-checked against the source image") rather than presenting it
  as a verbatim quote.
- Link back to the concept pages the chart's row-spine concepts already have pages for
  (waves-and-streams, the-psychic-subtle-causal-nondual, etc.).

**6. Concept generation: extend existing pages + a scoped new-page backlog**, same
pattern as issue #1's P3 tier rather than committing to an exact list now:
- Existing concepts that *Integral Psychology* clearly adds excerpts to (add
  `2000-integral-psychology` to `works:`, add IP excerpts alongside the SES ones):
  `waves-and-streams`, `four-quadrants`, `pre-trans-fallacy`.
- New concept candidates from the chapter list (ch. 1–15) not already covered by an
  SES-sourced page: the self-system (ch. 3–4), states vs. stages / structures (ch. 10),
  horizontal types (ch. 4), the integral psychograph as a tool (distinct from the chart
  pages — this is the *practice* of building one, not a reference table), childhood
  spirituality vs. the pre/trans fallacy (ch. 11, likely folds into the existing
  pre-trans-fallacy page rather than standing alone), the 1-2-3 of consciousness studies
  (ch. 14, likely extends `big-three`).
- Final scope (which of these become pages, in what order) is a judgment call for
  whoever executes the bead, same as the existing P3 backlog — not pinned down here.

**7. People index: run a fresh mention-count scan** of the IP full text (main body
only, same method as the original SES scan), producing an
`library/2000-integral-psychology-people-source.md` equivalent. Cross-reference against
the 23 existing SES people pages — most of IP's cited psychologists already have pages
(Piaget, Kohlberg, Loevinger, Maslow, Jung, Aurobindo, Gebser, Habermas) and just need
`works:` extended plus IP excerpts. Genuinely new names likely include James Mark
Baldwin (has his own dedicated Chart 11) and others the scan turns up (Kegan, Graves,
Erikson, Gilligan, Neumann are plausible candidates from the chapter list, not
confirmed).

## Open questions (for Rufus, not blocking)

1. **Copyright posture on the charts specifically.** AGENTS.md's existing
   "don't publish reflexively" note was written about the *full text* import
   (quotable prose). Redrawing all 21 correlation charts is closer to reproducing
   Wilber's own structural/creative work (the charts themselves, not just quoting
   sentences from them) than excerpting prose is — worth a deliberate look before these
   go live on wilber.wiki, separate from the general "check before `fl`" rule.
2. **`charts/` vs folding into `concepts/`** — went with a separate directory (decision
   4 above); flag if you'd rather they live under `concepts/` with a `category:
   reference-chart` instead, to keep one fewer top-level folder.
3. **Raw HTML tables in Markdown under Flowershow — genuinely blocked, not just
   unverified.** No existing page in this repo uses a raw HTML `<table>` (checked), so
   there's no precedent either way, and there's no local Flowershow dev server — the
   only way to actually see it render is `fl . --yes` to the CLI preview. That's the
   same command AGENTS.md says to check with you before running whenever `library/`'s
   contents have changed recently and haven't been reviewed — which is exactly the
   state right now (this session just added the full IP text and all 58 chart images
   under `library/`, unreviewed, and the CLI preview doesn't enforce `contentExclude`).
   Didn't want to make that publish call unilaterally. Chart 1's content is drafted
   (see `charts/chart-1-wilber-correlations.md`) with HTML tables; it needs either a
   `fl . --yes` check (yours or mine, once you've looked at what's now in `library/`)
   or a switch to flattened plain-Markdown tables (loses the nested row-grouping, still
   legible) if you'd rather not publish-to-test right now.
4. **How many chart pages are actually worth doing.** All 11 charts have real value,
   but some (Chart 7 "Misc Developmental Lines", Chart 8 "Miscellaneous") are visibly
   thinner than the big ones (Chart 1, 4, 5, 6). Worth doing all 11, or triage like the
   P3 concept backlog?
5. **Beads vs. GitHub issues going forward.** This repo just adopted beads
   (`.beads/issues.jsonl`, 2026-09-05) alongside the existing GitHub-issue-per-work-
   stream convention in NEXT.md. Opened a GitHub issue (#7) for this work stream to
   match that convention, with beads underneath it for execution — flag if you'd rather
   beads replace GitHub issues going forward instead of layering under them.
