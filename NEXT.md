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

- **Works validation and reading guides** — epic `wilberwiki-at6`.
  Catalog audit and basic guides implemented locally: [reading guide](works/reading-guide.md),
  [Wilber I–V and Kosmos trilogy](works/phases.md), and a
  [40-entry audit ledger](docs/plans/2026-09-14-works-bibliography-audit.md).
  Uncertain publication details remain explicit. Visual lineage research and design
  is now active under `wilberwiki-at6.4`, with a source-grounded
  [research/design plan](docs/plans/2026-09-17-wilber-works-visualization-research-and-design.md)
  and seven dependency-ordered child Beads; start with `wilberwiki-at6.4.1` and do not
  implement a polished visualization before the `wilberwiki-at6.4.6` human decision
  gate. Collaborative/pseudonymous additions are a separate follow-up
  (`wilberwiki-at6.6`). Working conventions: [catalog documentation](docs/works-catalog.md).
  Research and implementation history:
  [research note](docs/plans/2026-09-14-works-reading-guides-research.md) and
  [implementation plan](docs/plans/2026-09-14-works-reading-guides-implementation.md).
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
  name-drops, not gaps). Second book now mined too — see #7. 6 new people pages added
  from it (Baldwin, Graves, Kegan, Erikson, Gilligan, Cook-Greuter) and all 8 people
  common to both books now carry excerpts from both.
- **[#4 Finer-grained indexing](https://github.com/life-itself/wilber-wiki/issues/4)** —
  someday; subsumed by #3 in practice.
- **[#7 Second book: Integral Psychology](https://github.com/life-itself/wilber-wiki/issues/7)** —
  done. Full-text import; all 11 appendix chart pages (see the
  [Chart Index](charts/index.md)) — the book's ~21 scanned correlation charts, redrawn
  as web tables, linked into site nav; 4 concept pages new
  (proximate-self-and-distal-self, five-definitions-of-spirituality, horizontal-types,
  integral-psychograph) + 4 extended (waves-and-streams, four-quadrants, flatland,
  big-three); 6 people pages new (Baldwin, Graves, Kegan, Erikson, Gilligan,
  Cook-Greuter) + all 8 SES/IP-overlap people extended with IP excerpts. All
  quote-bearing pages pass `verify_quotes.py`. Epic `wilberwiki-vxk` closed (23/23
  beads). Design: [`docs/integral-psychology-import-design.md`](docs/integral-psychology-import-design.md).
  Left open, not tracked as beads: a few SES-overlap concept pages
  (dignity-and-disaster-of-modernity, agony-of-modernity-fichte-vs-spinoza,
  postmodernism) were flagged in the concept backlog as *likely* sources of further IP
  excerpts but never actually scanned — pick up there if extending this further.
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
