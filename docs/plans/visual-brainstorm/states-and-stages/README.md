# States off the ladder

Option 07 from the [visual brainstorm gallery](../gallery.html#o7), redrawn on 2026-10-26 under the rules in [`docs/figure-design.md`](../../../figure-design.md) (the Seeds of Renaissance diagram grammar with wilber.wiki's accent). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

One drawing, built by `figure.py` with `../design-language/wv.py`. The static image is a 1600 × 1061 canvas. Left, under the heading "Integral Psychology, 2000": a literal ladder, two rails and ten rungs, labelled bottom to top archaic, magic, mythic, rational, pluralistic, integral, psychic, subtle, causal, nondual; the four highest rungs sit in a tinted panel. Right, under "Integral Spirituality, 2006": a lattice whose four columns are headed gross, subtle, causal, nondual in a tinted panel, and whose six rows, labelled with the six lower stages, sit level with the ladder's lower rungs. One accent arrow runs from the ladder's top panel to the states panel: the four words leave the ladder and become a second axis. The cells are open. Sources bottom left; signature bottom right.

The animated page plays in four steps and settles on that frame: (0) the ladder; (1) the tint on the four highest rungs; (2) the arrow draws across and the states panel appears; (3) the rows and the lattice. The ladder never moves and nothing flies; copies and ghosts from the earlier build are gone.

Files: `figure.py`, `page.html`, and the generated `index.html`, `states-and-stages.svg`, `states-and-stages.png` and `@2x.png`, `states-and-stages-og.png`, `states-and-stages-dark.png`, `-accent-red.png` / `-accent-rust.png`. Regenerate with `python3 figure.py`.

## Sources

Nothing on the canvas is set as a quotation; the words on it are Wilber's names. On the page, verbatim, with line numbers in the full-text files:

- *Integral Psychology* (2000), ch. 1, `library/2000-integral-psychology-full-text.md` line 491: "Nonetheless, although the major states of gross, subtle, causal, and nondual are available to human beings at virtually any stage of growth, the way in which those states or realms are experienced and interpreted depends to some degree on the stage of development of the person having the peak experience. This means, as I suggested in A Sociable God, that we can create a grid of the types of spiritual experiences that are generally available to individuals at different stages of growth."
- *Integral Spirituality* (2006), ch. 4, `library/2006-integral-spirituality-full-text.md`: line 1206 (states as "variations on the natural states of gross-waking, subtle-dreaming, and causal-formlessness … present, or can be present, at virtually all *stages* of growth"); line 1208 (the lattice: "Gebser’s—archaic, magic, mythic, rational, pluralistic, integral" up the left, "the major *states* across the top (gross, subtle, causal, nondual)"); line 1214 ("a person at any *stage* can have a peak experience of a gross, subtle, causal, or nondual *state*. **But a person will interpret that state according to the stage they are at**" and "7 stages × 4 states = 28"); line 1216 ("gross/psychic, subtle, causal, and nondual were no longer stages *stacked on top* of the Western conventional stages, but were states … that can and did occur *alongside* any of those stages").
- Structure spine with psychic, subtle, causal, nondual on top: `charts/chart-1-wilber-correlations.md` (draft transcription). Prose account: `concepts/from-ses-to-integral-spirituality.md`; phase framing: `works/phases.md` (IV → V).

## Faithfulness

Wilber's: both pictures. The 2000 spine is his chart's left column; the 2006 lattice is built as he describes it, with his names for stages and states.

Ours: the literal ladder; the tint on the four words in both places and the one arrow between them (our picture of the shift); rows level with the lower rungs; the headings and subtitle. The six lower rung names on the 2000 ladder are IS's Gebser-like list, used on both sides so the pictures share words; IP's chart 1 gives Archaic, Magical, Mythic (two rows), Formalism, Pluralistic-relativism, Holistic-integralism, so the pairing is approximate (open question 3). The first column is headed "gross", as IS lists the states at line 1208; the same chapter later writes "gross/psychic" (line 1216).

Known simplification, stated on the page: IP lists psychic, subtle, causal and nondual as the highest basic structures in the chart while saying in the text that the states of the same names are available at any stage. The ladder shows the chart; the page quotes the caveat.

Left out on purpose: cell contents (no stage-by-state example has been quote-verified); the one-word state glosses; the seventh stage in Wilber's "7 × 4 = 28" (the figure follows his six-name list); the chart-1 worldview names on every rung; the on-canvas quotation and ◇ note.

## How it would integrate into the site

Where: `concepts/from-ses-to-integral-spirituality.md` (animated, best fit), `works/phases.md` under IV → V (static), possibly `concepts/psychic-subtle-causal-nondual.md` (static). The `.wv-fig` block from `index.html` goes in as raw HTML with `wv.css` and `wv-motion.js` registered once in `config.json` `head`; or the SVG as an `<img>`. The prose on the page is the text alternative and travels with the figure.

## Open questions for Rufus

1. The empty lattice: keep the cells open as a matter of style, or research and quote-verify Wilber's stage-by-state examples and fill them?
2. Is the ladder → lattice arrow an honest picture, given IP's caveat is on the page beside it?
3. Rung names: IS's list on both sides (current), or chart-1 names on the 2000 ladder?
4. Should this become the IV → V entry of a "what changed" series replacing the at6.4 lineage graph (see `../RECOMMENDATION.md`)?
