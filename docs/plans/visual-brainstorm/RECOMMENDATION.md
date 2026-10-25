# Visual brainstorm: recommendation

Date: 2026-10-24. Bead `wilberwiki-clq`. Brief: [`../2026-10-24-visual-brainstorm-brief.md`](../2026-10-24-visual-brainstorm-brief.md). Gallery: [`gallery.html`](gallery.html) (12 directions, sketches, sources, faithfulness, effort, risks). Builds: [`pre-trans-fallacy/`](pre-trans-fallacy/), [`states-and-stages/`](states-and-stages/). Decision gate: Rufus picks; silence is not approval.

## Ranked picks

1. **The pre/trans fallacy, in one picture** (gallery 05, built). Wilber's own structure end to end (three bands, "untutored eye", two named errors, Freud/Jung), a genuine newcomer "aha", works as a static poster and as a share card, and it cost a day. Where: header image on `concepts/pre-trans-fallacy.md`; the 1200 × 630 crop as that page's Open Graph image once per-page `og:image` is confirmed possible (`wilberwiki-4qc`). Ship static (`<img>` of the SVG) first; move to inline SVG with a scoped stylesheet if the OS-only dark mode bothers anyone.
2. **Taking states off the ladder** (gallery 07, built). The correction most readers of Wilber need (a state is not a stage; a meditator is not "higher"), and the one between-books change the repo can source completely from both sides. Where: `concepts/from-ses-to-integral-spirituality.md` (interactive) and `works/phases.md` under IV → V (static two-panel SVG). Needs one small CSS and one small JS file in `assets/` registered in `config.json` `head`, the same mechanism as the annotator.
3. **One thought, four windows** (gallery 01, not built). The obvious homepage/OG image and the cheapest thing in the gallery; ranked third only because every integral site has a quadrant grid and ours would need the concrete-example treatment to be worth looking at. Where: `index.md` and `concepts/four-quadrants.md`.
4. **Pull a rung out** (gallery 04). Best candidate for a third build: an interaction that performs Wilber's tenet-9 thought experiment. Where: `concepts/holarchy.md`.
5. **Wilber I–V: the books on a line** (gallery 08). Belongs on `works/phases.md`; fully sourced from the catalog; no arrows between books.

Lower-ranked and why, briefly: the Great Circle (11) is strong but second-read; Big Three → Big One (02) is a good slide, modest as an image; the Great Nest poster (03) is the prettiest wall piece but sits closest to a published figure; the psychograph (06) will be read as a quiz; the card system (12) wants glyphs from 1, 4, 5 first and an `og:image` check; the SES chapter map (09) is sound but low on newcomer value; the hundred-models transit map (10) should be parked until the chart transcriptions are verified, because it would make Wilber's correlations look more exact than he claims.

## Where things go, in one list

- `index.md`: option 1 (quadrants) as the site's lead image; option 12 later for a consistent card.
- `concepts/pre-trans-fallacy.md`: option 5.
- `concepts/from-ses-to-integral-spirituality.md`, `works/phases.md`: option 7.
- `concepts/four-quadrants.md`: option 1; `concepts/holarchy.md`: option 4; `concepts/great-chain-of-being.md`: option 3; `concepts/involution-and-evolution.md` and siblings: option 11; `concepts/flatland.md`, `concepts/big-three.md`: option 2; `concepts/integral-psychograph.md`: option 6.
- `works/phases.md`: option 8. `people/index.md`: option 9. `charts/index.md`: option 10, eventually.

Mechanics for all of them: Flowershow renders raw HTML in markdown; one scoped stylesheet (`assets/visuals/visuals.css`, `.wv-root` prefix, light only, same scoping pattern as `assets/roadmap/roadmap.css`) and, for the two interactive pieces, one deferred script that no-ops when its root element is absent, both registered in `config.json` `head`. Static SVGs can go in `assets/visuals/` and be embedded with `<img>` straight away. Nothing in this brainstorm touches `config.json` or site pages yet.

## On the concept-lineage track (`wilberwiki-at6.4`)

Recommendation: **change its shape; neither continue as specified nor park it outright.**

What's wrong with the current target. The deliverable is a graph: concept families as nodes or lanes, books on an axis, and edges meaning "this formulation develops that one". Every edge is a historical priority claim. The September review ([`../2026-09-18-works-visualization-review-and-execution.md`](../2026-09-18-works-visualization-review-and-execution.md)) was right that recurrence, chronology and similarity do not establish inheritance, and right to demand a date basis and a comparative record per edge. But that makes the research chain (`.4.2`–`.4.4`) long in proportion to the number of edges, and the one real cross-work comparison attempted (A Sociable God vs IP) is still unresolved for lack of the original passage. The ledger has 18 families × 13 works; even a sparse graph needs dozens of audited edges before it says anything a reader can use. Meanwhile Rufus isn't sure the graph is the right picture at all.

What this brainstorm found. Option 7 is a "what changed" visual with zero edges. It shows one formulation as drawn in an earlier book and the same formulation as drawn in a later one, with both passages beside it, and it explicitly says how much of the change is picture versus claim. It needed two quote-verified passages per side and a chart page, all already in the repo, and took an afternoon. A reader learns something true about how Wilber's thought moved without the diagram asserting any derivation.

Proposed new shape. Replace the graph with a **series of before/after diptychs, one per transition Wilber himself names** (I → II, II → III, III → IV, IV → V, per `works/phases.md` and IP ch. 9 n. 15). Each diptych:

- draws one formulation twice (early book, later book), sourced to passages in `library/` or, where the early book is not in the library, marks the early panel as unverified and says what would verify it;
- carries the verbatim passages beside it and a "what changed, honestly" paragraph that separates a change of picture from a change of claim;
- draws no edges and makes no claim about influence or priority beyond what the quoted passages say;
- goes through the same evidence gate as before: the `.4.4`-style audit applies to each diptych's two panels, and Rufus's `.4.6` decision applies per diptych.

Candidates and their current source situation: IV → V is done (option 7; both books in `library/`). III → IV (levels-and-lines psychograph in one quadrant → the same inside four quadrants) can be drawn from IP alone, which describes both the UL psychograph and the all-quadrant view, with SES for the quadrants; the early side (Transformations, 1986) is not in `library/`. I → II (spectrum as recovery of lost wholeness → development beyond ego) and II → III (one ladder → levels with relatively independent lines) depend on books not yet in `library/` (Spectrum, Atman Project, Eye to Eye); their early panels would have to be marked unverified until a text is available, which is honest and still useful.

What to keep from at6.4: the YAML ledger as the vocabulary and evidence store (its appearance records are exactly what a diptych's panels cite), the validator, the date-basis discipline, and the human decision gate. What to drop: the lineage-edge collection as the primary deliverable, the whole-corpus matrix ambition, and the graph/stream-map prototype comparison in `.4.5`, which was comparing ways of drawing edges.

If Rufus prefers to park at6.4 entirely, option 8 (the arrow-free timeline on `works/phases.md`) and option 7 together already give the works section a visual story without any lineage research, and that is a defensible place to stop.

## Checks done and not done

Done: every quoted string in the gallery and the two builds was grepped in `library/*-full-text.md` and matched; all HTML pages render without console errors in headless Chrome at 1280 px and 390 px (light only; dark mode was dropped 2026-10-26) (screenshots in the session, not committed); both SVG exports are well-formed XML. Not done: `verify_quotes.py` was not run because it checks `concepts/`, `people/` and `works/` pages, not HTML, and no site pages were edited. The IS stage list used for the lattice rows is the six names Wilber lists explicitly; his "7 stages" count in the same passage is noted on the page but the seventh name is not asserted. Mention counts behind option 9 are the first-pass numbers already in `people/index.md`, not re-counted.
