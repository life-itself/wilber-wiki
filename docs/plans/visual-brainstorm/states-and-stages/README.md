# Taking states off the ladder

Option 07 from the [visual brainstorm gallery](../gallery.html#o7), taken to a polished state. Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

An animated "what changed" diagram. Ten labelled rungs start as one ladder (the *Integral Psychology* picture, 2000: archaic through integral, then psychic, subtle, causal, nondual on top). Press play and the four top rungs slide off to become column headers while the six stage rungs become row labels: the *Integral Spirituality* picture (2006), the Wilber-Combs lattice of structure-stages × states. In the lattice state, each cell can be hovered or tabbed to; the caption then reads "stage × state: a state experience interpreted through that stage", which applies Wilber's own rule from IS ch. 4. Beside the figure, the relevant passages from both books, and a section titled "What changed, honestly" that says the change is in the picture rather than the claim: IP already says the states are available at any stage.

Files: `index.html` (interactive page; small vanilla JS, CSS transitions, `prefers-reduced-motion` respected, keyboard-reachable cells, HTML table as the text alternative), `states-and-stages.svg` (static two-panel export: ladder | lattice, with an arrow between them).

## Sources

Verbatim passages, with line numbers in the full-text files:

- *Integral Psychology* (2000), ch. 1, `library/2000-integral-psychology-full-text.md` line 491: "Nonetheless, although the major states of gross, subtle, causal, and nondual are available to human beings at virtually any stage of growth, the way in which those states or realms are experienced and interpreted depends to some degree on the stage of development of the person having the peak experience. This means, as I suggested in A Sociable God, that we can create a grid of the types of spiritual experiences that are generally available to individuals at different stages of growth."
- *Integral Spirituality* (2006), ch. 4, `library/2006-integral-spirituality-full-text.md` line 1207 (lattice construction: structure-stages "running up the left side of the grid or lattice", states "across the top (gross, subtle, causal, nondual)"; Gebser-like stage list "archaic, magic, mythic, rational, pluralistic, integral"), line 1214 ("a person at any stage can have a peak experience of a gross, subtle, causal, or nondual state. But a person will interpret that state according to the stage they are at"), line 1216 ("no longer stages stacked on top … alongside any of those stages"), line 1205 ("variations on the natural states of gross-waking, subtle-dreaming, and causal-formlessness", source for the one-word state glosses).
- Structure spine with Psychic, Subtle, Causal, Nondual at the top, and the worldview column used for the small labels on the stage rungs: `charts/chart-1-wilber-correlations.md` (status draft, first-pass transcription).
- Prose account of the same shift: `concepts/from-ses-to-integral-spirituality.md`; phase framing: `works/phases.md` (IV → V).

## Faithfulness

Wilber's: both pictures. The 2000 spine is his master chart's left column; the 2006 lattice is built exactly as he describes it, with his stage names and his state names. "A person will interpret that state according to the stage they are at" is his sentence; the cell captions apply it mechanically.

Ours: presenting the two as one animation in which rungs become headers. This is a framing of his own words ("no longer stages stacked on top … alongside"), and the page says so. Also ours: pairing IS's Gebser-like stage names with IP chart-1 worldview names on the small rung labels. The two books use different vocabularies, and the pairing is approximate ("mythic" spans two chart-1 rows; chart 1 also has Archaic-magical and Mythic-rational rows that are not shown). The one-word state glosses come from IS's "gross-waking, subtle-dreaming, causal-formlessness"; "ever-present" for nondual is our gloss and is flagged on the page.

Not shown on purpose: cell contents. Wilber gives examples of how particular states are read at particular stages; none have been quote-verified for this page, so the cells carry only "stage × state".

Known simplification: IP lists psychic/subtle/causal/nondual as *structures* in the chart while also saying in the text that the *states* of the same names are available at any stage. The animation shows the chart picture, not the text's caveat; the caveat is quoted beside it. Rufus should decide whether that is fair or whether the 2000 panel needs a visible footnote on the figure itself.

## How it would integrate into the site

- **Where:** `concepts/from-ses-to-integral-spirituality.md` (best fit: the page is about this change), `works/phases.md` under IV → V, and possibly `concepts/psychic-subtle-causal-nondual.md` as the static two-panel image.
- **Static first:** `states-and-stages.svg` as an `<img>` costs nothing and makes the point. Same dark-mode caveat as the pre/trans poster (OS media query, not the site toggle).
- **Interactive:** needs `assets/visuals/states-and-stages.css` and `assets/visuals/states-and-stages.js` registered in `config.json` `head`, exactly as `assets/annotator/annotator.js` is today (`defer`, runs on every page, so it must no-op when `#stage` is absent). The SVG and controls are pasted into the markdown as raw HTML. CSS must be scoped under a root class (Flowershow's Tailwind bundle is pre-purged, as `roadmap.css` notes) and use `html[data-theme="dark"]` overrides.
- **Accessibility:** the HTML table in `index.html` is the text alternative and should travel with the figure.

## Open questions for Rufus

1. Is the ladder → lattice animation an honest picture of the change, given IP's caveat? The page argues yes with the caveat visible; an alternative is a static side-by-side with no motion.
2. Row vocabulary: keep IS's Gebser-like names as the main labels with chart-1 names small, or use chart-1's names throughout and lose the clean six-row lattice?
3. Cell contents: leave empty (current), or research and quote-verify Wilber's own stage-by-state examples from IS ch. 4 so hovering a cell shows his words?
4. Does this want to be the IV → V piece of a wider "what changed" series (see `../RECOMMENDATION.md` on the at6.4 track)?
