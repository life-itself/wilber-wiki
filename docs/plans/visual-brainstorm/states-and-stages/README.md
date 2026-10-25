# States off the ladder

Option 07 from the [visual brainstorm gallery](../gallery.html#o7), rebuilt on 2026-10-25 in the shared [design language](../design-language/README.md). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

One SVG source, two outputs. The static image is a 1200 × 800 before/after diptych: on the left the *Integral Psychology* (2000) ladder, ten rungs with psychic, subtle, causal and nondual on top marked as "drawn as structures"; on the right the *Integral Spirituality* (2006) Wilber-Combs lattice, six structure-stages up the side and four states across the top, twenty-four cells; below, Wilber's "no longer stages stacked on top … alongside" sentence with its locator and a ◇ note that IP already said the states are available at any stage. The animation settles on exactly that frame: (1) the ladder; (2) ghost copies of the four top rungs fly across to become the state headers; (3) ghost copies of the six lower rungs fly to become the row labels; (4) the cells fade in row by row; (5) the passage and the note. The ladder itself never moves, so the settled frame is a true diptych.

Files: `source.svg`, `page.html`, and the generated `index.html`, `states-and-stages.svg`, `states-and-stages.png` (2400 × 1600), `states-and-stages-og.png` (1200 × 630), `states-and-stages-square.png` (1080 × 1080). Regenerate with `python3 ../design-language/export.py states-and-stages`. Cells carry a `<title>` so hovering shows the sentence the label abbreviates.

## Sources

Verbatim passages, with line numbers in the full-text files:

- *Integral Psychology* (2000), ch. 1, `library/2000-integral-psychology-full-text.md` line 491: "Nonetheless, although the major states of gross, subtle, causal, and nondual are available to human beings at virtually any stage of growth, the way in which those states or realms are experienced and interpreted depends to some degree on the stage of development of the person having the peak experience. This means, as I suggested in A Sociable God, that we can create a grid of the types of spiritual experiences that are generally available to individuals at different stages of growth." On the page; the fragment "available to human beings at virtually any stage of growth" is in the ◇ note on the canvas.
- *Integral Spirituality* (2006), ch. 4, `library/2006-integral-spirituality-full-text.md` line 1206 ("variations on the natural states of gross-waking, subtle-dreaming, and causal-formlessness", source of the header glosses waking / dreaming / formless sleep), line 1207 (lattice construction and the stage list "archaic, magic, mythic, rational, pluralistic, integral"), line 1214 ("a person at any stage can have a peak experience of a gross, subtle, causal, or nondual state. But a person will interpret that state according to the stage they are at"; also "7 stages × 4 states = 28"), line 1216 (the canvas quotation: "gross/psychic, subtle, causal, and nondual were no longer stages *stacked on top* of the Western conventional stages, but were states (including altered states and peak experiences) that can and did occur *alongside* any of those stages").
- Structure spine with Psychic, Subtle, Causal, Nondual at the top, and the worldview column used for the small labels on the ladder rungs: `charts/chart-1-wilber-correlations.md` (status draft, first-pass transcription).
- Prose account of the same shift: `concepts/from-ses-to-integral-spirituality.md`; phase framing: `works/phases.md` (IV → V).

## Faithfulness

Wilber's: both pictures. The 2000 spine is his master chart's left column; the 2006 lattice is built as he describes it, with his stage names and state names. "A person will interpret that state according to the stage they are at" is his; the cell tooltips apply it mechanically.

Ours, marked ◇ on the canvas: the "what changed is the picture" note; the framing of the two pictures as one animation in which rungs become headers and rows. Also ours, stated on the page: pairing IS's Gebser-like stage names with IP chart-1 worldview names on the small ladder labels (approximate: "mythic" spans two chart-1 rows); the one-word state glosses; "a state" with no gloss for nondual (the earlier build's "ever-present" was our word and has been dropped).

Not shown on purpose: cell contents. Wilber gives examples of how particular states are read at particular stages; none have been quote-verified, so cells carry only "stage × state".

Known simplification, unchanged: IP lists psychic/subtle/causal/nondual as *structures* in the chart while saying in the text that the *states* of the same names are available at any stage. The canvas shows the chart picture on the left and quotes the caveat on the right; whether that is fair is open question 1.

Changes from the first build: a real static output (the diptych) instead of a page-only toggle; the ladder stays put and copies fly, so the settled frame contains both pictures; colour roles from the language (indigo for structures, amber for states) replace the earlier ad-hoc amber/neutral; the controller is the shared one.

## How it would integrate into the site

See the design-language README, "Embedding in Flowershow". Where: `concepts/from-ses-to-integral-spirituality.md` (animated, best fit), `works/phases.md` under IV → V (static diptych), possibly `concepts/psychic-subtle-causal-nondual.md` (static). The figure block from `page.html` goes in as raw HTML; `visuals.css` and `wv-motion.js` are registered once in `config.json` `head`. The HTML table on the page is the text alternative and should travel with the figure.

## Open questions for Rufus

1. Is the ladder → lattice animation an honest picture, given IP's caveat is on the canvas beside it? The alternative is the static diptych only.
2. Row vocabulary: IS names large with chart-1 names small (current), or chart-1 names throughout?
3. Cell contents: leave as "stage × state", or research and quote-verify Wilber's own stage-by-state examples so the tooltips carry his words?
4. Should this become the IV → V entry of a "what changed" series replacing the at6.4 lineage graph (see `../RECOMMENDATION.md`)?
