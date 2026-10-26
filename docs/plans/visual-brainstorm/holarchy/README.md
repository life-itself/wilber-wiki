# Pull a rung out

Option 04 from the [visual brainstorm gallery](../gallery.html#o4), built on 2026-10-26 in the shared [design language](../design-language/README.md) (spec: [`docs/figure-design.md`](../../../figure-design.md)). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

One SVG source, two outputs. The static image is a 1200 × 800 before-and-after: on the left Wilber's example holistic sequence drawn as a ladder of five rungs (subatomic particles, atoms, molecules, cells, organisms, each "contains the one below · not vice versa"); on the right the same ladder after the molecules rung has been pulled out and destroyed. The pulled rung sits between the two ladders in the fallacy colour with a short arrow back to its slot; the slot and the two rungs above it (cells, organisms) are dotted outlines, the language's mark for absence, with the reason in two words ("needed molecules", "needed cells"); the two rungs below (atoms, subatomic particles) are untouched ("exist without molecules", "existed before molecules"). A bracket beside the right ladder reads off the rule: "gone with it, so they are higher" / "untouched, so they are lower". Below, three of Wilber's sentences from tenet 9: the tenet, the thought-experiment question, and the rule.

The animation performs the experiment and settles on exactly that frame (N = 5, 1500 ms a step, about 7.5 s): (0) the sequence; (1) a copy appears to experiment on, intact; (2) the molecules rung turns and slides out of its slot, the dotted slot and the arrow appear; (3) cells and organisms fall away (ghost copies drop and fade) and leave dotted outlines, the "gone with it" bracket appears; (4) the lower rungs get their "exist without molecules" glosses and the "untouched" bracket; (5) the quotations, the ◇ note, the footer and the signature.

Files: `source.svg`, `page.html`, and the generated `index.html`, `holarchy.svg`, `holarchy.png` (2400 × 1600), `holarchy-og.png` (1200 × 630), `holarchy-square.png` (1080 × 1080). Regenerate with `python3 ../design-language/export.py holarchy` (the slug is passed explicitly; it is not yet in `PIECES`).

### One mechanism beyond the shared grammar

The shared step CSS only lets elements *appear*. This piece needs three things that exist before the pull and are gone after it: the copy's molecules rung in its slot (step 1 only) and the copy's cells and organisms rungs (steps 1–2). They are authored hidden (`opacity="0"`, classes `hol-upto-1` / `hol-upto-2`) so the settled source, the standalone SVG and the PNGs contain none of them, and a three-selector rule inside the figure block in `page.html` (`#hol-fig[data-step="1"] .hol-upto-1, …`) shows them at those steps. The rule lives inside the `[data-wv-steps]` div so `scripts/sync-visuals.py` would carry it to the site with the block. The proper home is a `data-until="k"` verb in `visuals.css` ("hidden from step k on"), which would also serve any future figure that removes something; see the report.

## Sources

Verbatim from `library/1995-sex-ecology-spirituality-full-text.md` (revised second edition text), chapter 2, "The Pattern That Connects". Line numbers are for that file; each was grepped on 2026-10-26.

- Line 1112, tenet 9, on the canvas (column 1; italic throughout in the source, reproduced): "Destroy any type of holon, and you will destroy all of the holons above it and none of the holons below it." The full paragraph is on the page.
- Line 1114, the question, on the canvas (column 2) and the page: "What other types of holons would be destroyed if we destroyed this type of holon?" (and "as a type of thought experiment").
- Line 1116, the example sequence, on the page: "take the holistic sequence: subatomic particles, atoms, molecules, cells. Everybody agrees that that is indeed a holistic sequence—each member includes its predecessor(s) but not vice versa".
- Line 1118, the molecules example, on the page: "If we destroyed, for example, all of the molecules in the universe, we would also destroy all of the cells in the universe … but atoms and subatomic particles would or could still exist". Source of the right-hand head "destroy all the molecules" and of the choice of molecules as the rung.
- Line 1122, on the page: "Molecules cannot exist without atoms; atoms can exist without molecules." Source of the gloss "exist without molecules".
- Line 1124, the rule, on the canvas (column 3, with a leading elision) and the page: "destroy the particular holon, and everything else that is also destroyed is higher; those holons not destroyed are lower."
- Line 986, tenet 4, quoted on the page: "Organisms contain cells, but not vice versa; cells contain molecules, but not vice versa; molecules contain atoms, but not vice versa." Source of organisms as the rung above cells and of the "contain …" glosses on the left ladder.
- Prose: `concepts/holarchy.md`, `concepts/holons.md`, `concepts/dominator-vs-growth-hierarchy.md`.

## Faithfulness

Wilber's: the test and its three sentences; the sequence subatomic particles → atoms → molecules → cells (tenet 9) with organisms above cells (tenet 4); molecules as the holon destroyed; the result (cells go, atoms and subatomic particles remain); "not vice versa"; "atoms can exist without molecules"; "higher" and "lower" as what the test yields, not a value judgement.

Ours, marked ◇ on the canvas ("the ladder and the pulled rung are this wiki's picture; the sequence, the test and the result are Wilber's"): the ladder, the rung, the pull and the fall. Wilber speaks of levels in a holistic sequence; he does not draw it, and "rung" is the wiki's word here. Also ours, in sans as labels: the two-word glosses on the rungs ("contain cells", "needed molecules", "exist without molecules", "existed before molecules"), which condense his sentences; the read-off bracket, which restates his rule; the heads; "pulled out and destroyed". The "existed before molecules" gloss on subatomic particles rests on tenet 3's order of emergence ("First subatomic particles, then atoms, then molecules", line 968) and the chronological claim at line 1122, not on a sentence about subatomic particles and molecules specifically.

Not shown on purpose: polymers (between molecules and cells, line 1122) and plants, animals, societies (above cells, same line); the "retreat" to the next lower level when a holon dissolves (line 1126); depth and span (tenets 7–8); the chapter 3 applications (biosphere and noosphere, Gaia). One pull, one rule.

The test is logical, on types, as Wilber says; "destroying every molecule" is a hypothesis to reason from. The page says so (gallery risk: physics pedants).

No published figure was reproduced; the footer says "Redrawn from his description".

## How it would integrate into the site

See `docs/figure-design.md`, "Embedding in Flowershow". Where: `concepts/holarchy.md` (the gallery and the recommendation both place it there), possibly `concepts/dominator-vs-growth-hierarchy.md` (static) since the test is Wilber's answer to "hierarchy means ranking". Add `holarchy` to `PIECES` in `design-language/export.py` and `scripts/sync-visuals.py`; the figure block carries its own three-line `<style>`, which the sync script would paste with the block (to be checked in Flowershow once; if it strips `<style>` inside raw HTML, move the rule to `visuals.css` as the `data-until` verb). The HTML table on the page is the text alternative and should travel with the figure.

## Open questions for Rufus

1. The pulled rung sits between the two ladders. Alternative: to the right of the after-ladder, with the read-off bracket between the ladders. The middle placement reads as "taken out of the sequence" and keeps the arrow short; say if it reads as belonging to the before-ladder instead.
2. Five rungs with organisms on top (from tenet 4), or exactly Wilber's tenet-9 four (subatomic particles, atoms, molecules, cells)? Five shows two rungs going, which makes "all of the holons above it" visible; four is the stricter quotation of the example.
3. The "existed before molecules" gloss on subatomic particles (see Faithfulness): keep, or repeat "exist without molecules" on both lower rungs?
4. The piece-only step rule (`hol-upto-*`): accept as is, or add `data-until` to the shared CSS and export script so this and future figures can remove things cleanly?

## Decisions (2026-10-26, Rufus)

Five rungs with organisms on top. Both lower rungs now read "exist without molecules", which stays on Wilber's sentence. The pulled rung stays between the ladders. The piece-local step rule was replaced by a shared `data-from`/`data-until` mechanism in `wv-motion.js`.
