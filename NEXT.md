# Next

Orientation for a fresh session: this file maps the work streams and their plans.
Beads owns current task status, priorities, dependencies, and execution order. Run
`bd ready`, then inspect the relevant parent with `bd show <id>` and
`bd children <id>` before claiming work. Do not treat the historical summaries below
as a current task queue. `changelog.md` is reader-facing history; linked GitHub issues
are historical/project-level references.

Live site: **https://wilber.wiki**. Before touching `concepts/` or `people/`, read
[`skills/add-excerpt-page/SKILL.md`](skills/add-excerpt-page/SKILL.md) — it's mandatory
and includes a required quote-verification step
(`python3 skills/add-excerpt-page/scripts/verify_quotes.py`, should always pass before
you're done).

## Checkpoint 2026-10-26

- Shipped: a [Visuals](visuals.md) page with two figures, the pre/trans fallacy and states off the ladder (bead `wilberwiki-clq`, closed; follow-ups in `wilberwiki-b5y`). The figure rules are in [`docs/figure-design.md`](docs/figure-design.md); the brief and full decision log are in `docs/plans/2026-10-24-visual-brainstorm-brief.md`; the gallery of 12 directions is in `docs/plans/visual-brainstorm/`.
- Next for visuals: the animated versions aren't on the site yet. The site is MDX, so they need an embedding approach; see figure-design.md "Embedding in Flowershow". Write plans for the other gallery directions (quadrants, holarchy, I–V timeline next). Reshape `at6.4` into before/after diptychs per `RECOMMENDATION.md`, pending Rufus.
- Open for Rufus: drop the 24 cell labels in the states grid? Shorten its ◇ note? Swap fonts or colours later?

## Checkpoint 2026-10-11

- Shipped: epic `wilberwiki-o1s` (book summary pages). SES pilot (644b726, independent review fixes in a later commit), *Integral Spirituality* (ae8542f), *Integral Psychology* (57ba74f), each reviewed against the full text. Pattern: [`skills/write-book-summary/SKILL.md`](skills/write-book-summary/SKILL.md); design and lessons: `docs/plans/2026-10-10-book-summary-pages-design.md`. `verify_quotes.py` now also checks works pages that declare `works:`.
- Earlier (2026-10-09/10): attribution links (e9q), pre/trans essay identified (qxv), catalog trimmed to books only (2ie), IS full text imported (s7g), SES→IS concept page (pmf), IS excerpts on five concept pages (evl), changelog in navbar (53r).
- For Rufus: (1) the SES header says "rev. 2001", while the edition's copyright page reads © 1995, 2000. Kept 2001 per the earlier audit (2000 revision first appeared in Collected Works VI); change it if you prefer. (2) IP and IS pages run about 4,800–5,000 words, over the 4,500 target because of Key passages and the concept/people lists; trim if wanted. (3) IS's What's contested includes the page's own judgements without an external critic. (4) Several concept pages that IS discusses (great-chain-of-being, pre-trans-fallacy, repression…) could gain IS excerpts. Not yet a bead. (5) A copy of *Eye to Eye* for the pre/trans essay; at6.4 visualization; dxr/uze scope.
- Next ready: `bd ready`. The remaining items are P2/P3 and mostly need scope decisions.

## Work streams

- **Works validation and reading guides** — epic `wilberwiki-at6`.
  Catalog audit and basic guides implemented locally: [reading guide](works/reading-guide.md),
  [Wilber I–V and Kosmos trilogy](works/phases.md), and a
  [40-entry audit ledger](docs/plans/2026-09-14-works-bibliography-audit.md).
  Uncertain publication details remain explicit. Visual lineage research and design
  is now active under `wilberwiki-at6.4`, with a source-grounded
  [research/design plan](docs/plans/2026-09-17-wilber-works-visualization-research-and-design.md)
  and a [critical review and execution handoff](docs/plans/2026-09-18-works-visualization-review-and-execution.md)
  with model/effort recommendations and delegation guidance. Inspect the children
  of `wilberwiki-at6.4` for current readiness and execution order. Do not
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
