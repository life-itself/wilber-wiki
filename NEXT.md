# Next

What to do next in this repo, written so a fresh session (human or AI) can pick this up
cold. Detailed history lives in `changelog.md` (reader-facing) and in each GitHub issue
below (which now carry their own checklists/backlogs) — this file stays short and
points there rather than duplicating it.

Live site: **https://wilber.wiki**. Before touching `concepts/` or `people/`, read
[`skills/add-excerpt-page/SKILL.md`](skills/add-excerpt-page/SKILL.md) — it's mandatory
and includes a required quote-verification step
(`python3 skills/add-excerpt-page/scripts/verify_quotes.py`, should always pass before
you're done).

## Work streams

- **[#1 Concept wiki](https://github.com/life-itself/wilber-wiki/issues/1)** —
  40 pages, all quote-verified. Only the P3 tier (5 thinner/niche candidates) of the
  backlog checklist is still open; everything else on the original list is done.
- **[#2 Annotatable reading layer](https://github.com/life-itself/wilber-wiki/issues/2)** —
  Phase 1 prototype live (one hand-annotated chapter excerpt), not yet linked from site
  nav. A prioritized gap list is on the issue (2026-08-25 comment) — top item is nearly
  free (add the nav link), then the real test is trying the same pattern on a second,
  longer excerpt.
- **[#3 People index](https://github.com/life-itself/wilber-wiki/issues/3)** — 23 of 27
  *SES* interlocutors done (roster complete for this book; the other 4 are documented
  name-drops, not gaps). Next step is picking a second Wilber book to mine — candidates
  and reasoning are on the issue.
- **[#4 Finer-grained indexing](https://github.com/life-itself/wilber-wiki/issues/4)** —
  someday; subsumed by #3 in practice.
- **[#7 Second book: Integral Psychology](https://github.com/life-itself/wilber-wiki/issues/7)** —
  planned, not yet executed. Design:
  [`docs/integral-psychology-import-design.md`](docs/integral-psychology-import-design.md).
  Full-text import + a new `charts/` content type reconstructing the book's 21 appendix
  correlation charts as 11 web-readable pages, plus concept/people extension. Broken
  into 23 beads under epic `wilberwiki-vxk` (`bd list -l integral-psychology`) — start
  with the P0s (full-text import, then the Chart 1 spike). Open questions logged in the
  design doc, notably the copyright posture on reproducing the charts themselves.
- **[#6 Notes/materials inbox](https://github.com/life-itself/wilber-wiki/issues/6)** —
  4 external pieces imported so far into `notes/` (2 of Rufus's own book reviews, 2
  Second Renaissance newsletter pieces on quadrants/levels, attributed to all three
  people behind the newsletter — Rufus Pollock, Catherine Tran, and Rosie Bell). Still
  open: Rufus's wider Obsidian vault (unsearched), and confirming whether a third found piece
  (*Integral Psychology*, same newsletter) is distinct or a misremembered duplicate of
  one of the two already imported.

## For Rufus

- People index: the 4 skipped *SES* names (Bateson, Gould, Comte, Assagioli) are a
  judgment call about what counts as "substantive" — worth a skim if you disagree with
  where that line was drawn.
- The annotation prototype's hand-rolled highlighter (instead of the originally
  recommended `@recogito/text-annotator` library) was a judgment call under time
  pressure — see `docs/annotation-system.md` if you want to weigh in before more
  chapters get built that way.
