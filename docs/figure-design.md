# Figure design for wilber.wiki

The settled rules for the explanatory figures (diagrams, posters, animated explainers) that go on wilber.wiki and get shared on their own. This is operational documentation: what a new figure must follow and how to build one. The exploration that produced it, the options gallery, both pieces and the review page, is in [`plans/visual-brainstorm/`](plans/visual-brainstorm/) (bead `wilberwiki-clq`). Decisions date from 2026-10-25 and 2026-10-26.

## Where the rules come from, and two lessons

This language was built on 2026-10-25 and proven on two pieces, [the pre/trans fallacy](plans/visual-brainstorm/pre-trans-fallacy/) and [states off the ladder](plans/visual-brainstorm/states-and-stages/). A second pass then rebuilt everything on the restrained grammar of the **Seeds of Renaissance diagram system** (https://design.seedsofrenaissance.org/diagrams; one face, no bold, no outlines, straight ink arrows, lots of white space). Rufus compared the two and chose the first: the earlier figures were "diagrammatically much better". The SoR attempt stays in git history (`822a1d3`) and SoR remains the reference for restraint: when a figure is getting busy, its rules (fewer things, labels on the things they name, one accent, read at 400 px) are the ones to apply. Seeds of Renaissance is also the signature partner: every figure is signed with the SoR mark and "SEEDS OF RENAISSANCE · WILBER WIKI".

Two lessons, recorded so they are not relearned:

1. **Polish rather than restyle.** "More beauty" was a request to tidy the existing pieces (spacing, alignment, label placement), not to replace their structure. Fix nits and adjust rhythm before touching the grammar.
2. **Diagrammatic content is what makes these engaging.** The "untutored eye" bins, the rungs flying off the ladder, the quotation on the canvas: those are the figure. A cleaner drawing that cuts them is a worse figure.

## One principle: one SVG source, two outputs

A piece is a folder with `source.svg` (the drawing) and `page.html` (the page around it, with a `<!-- @svg -->` placeholder). The source is authored in its **settled state**: what you see with no CSS and no JS is the static image. Animation only ever subtracts from that state for earlier steps (elements carry `data-at="k"`, "appears at step k"), so the settled frame and the exported image are the same drawing by construction. `export.py` inlines the source into the page, strips the step attributes for the standalone SVG, and renders the PNGs from viewBox crops declared on the SVG root. Edit `source.svg` or `page.html`, never `index.html` or the exports.

## Series format

Master canvas **1200 × 800** (3:2), 60-unit margins. Title block at the top (eyebrow, title, one-line subtitle), the figure in the middle band (y ≈ 170–640), passages and footer in the bottom band (y ≥ 664). The 1200 × 630 Open Graph crop is the top of the canvas (`data-og="0 0 1200 630"`): title plus figure, no passages. The square is the full canvas letterboxed (`data-square="0 -200 1200 1200"`). Portrait was rejected because it could not yield an OG crop that kept both the title and the whole figure.

## Type

Two families, each with a job, both held as tokens (`--wv-serif`, `--wv-sans`) so they can be swapped later. **Fraunces** (serif) is the book's voice: titles, subtitles, the names of Wilber's terms inside a figure, and every verbatim quotation. **Inter** (sans) is the wiki's voice: labels, headers, locators, footers, controls, our notes. The reader learns without being told: serif is Wilber's words or his named things, sans is our apparatus. Fallbacks: Iowan Old Style / Georgia and system-ui.

Scale in canvas units (the 1200-wide SVG), with the class in `visuals.css`:

| role | class | size | face |
|---|---|---|---|
| eyebrow | `t-eyebrow` | 12, tracked 2.2, caps | sans 600, muted |
| title | `t-title` | 46 | serif 600 |
| subtitle | `t-sub` | 19 italic | serif, ink-soft |
| column head | `t-head` | 12, tracked 2, caps | sans 600, muted |
| term name | `t-name` / `t-name-s` | 28 / 20 | serif 600 |
| label | `t-label` / `t-label-b` | 13 | sans / sans 600 |
| small label | `t-small` | 11 | sans |
| quotation | `t-quote` / `t-quote-s` | 16 / 14 | serif |
| locator | `t-loc` | 11 | sans, muted |
| our note | `t-ours` | 11 italic | sans, muted, prefixed ◇ |
| footer | `t-foot` | 10.5 | sans, muted |
| signature text | `t-mark` | 11, tracked 1 | sans 600, muted |

Nothing below 10.5 on the canvas (21 px in the 2× PNG).

## Colour and semantic roles

Light only; the figures are not themed for dark mode (Rufus, 2026-10-26). Tokens live on `.wv-root` in `visuals.css` and are the thing to change if the palette is swapped; the roles stay. `contrast.py` checks every text role against paper and surface (all ≥ 4.65:1).

| role | meaning in a Wilber figure | value |
|---|---|---|
| ink / ink-soft / muted | neutral structure and text | `#1c1917` / `#57534e` / `#6f6861` |
| paper / surface | page ground / figure ground | `#f8f6f1` / `#fffdf9` |
| line / line-strong | hairlines, rules, grid | `#ddd7cd` / `#aaa198` |
| **level** | structures, stages, levels, bands of development, the "higher" | `#4338ca` (indigo) |
| **state** | states of consciousness; also the site's accent amber | `#b45309` |
| **fallacy** | errors, pathologies, dissociation, collapse | `#be123c` (madder) |
| **ground** | the prerational, body, nature, the "lower" | `#0f766e` (teal) |
| neutral fill | anything carrying no role | 5.5% ink |

Each role has a text/stroke value (`c-*`, `s-*`) and a tinted fill (`f-*`). A hue appears in a figure only when the thing it marks is in the figure. Two things of the same kind share a colour: the two fallacies in the pre/trans piece are both madder, distinguished by direction and label, never by a second hue that would rank them. "State" shares the site's amber so the series feels native to wilber.wiki; a figure therefore never uses amber for both a state and a highlight (interactive highlight is ink). Rejected: Wilber's own "altitude" rainbow for levels (imports a late-Wilber convention into every figure) and monochrome (loses the state/structure distinction the states piece exists to make).

## Lines, strokes and arrows

| weight | class | use |
|---|---|---|
| 1 | `w-hair` | band and box outlines, grid, rules |
| 1.5 | `w-struct` | axes, connectors, anything structural |
| 2.5 | `w-path` | a movement or a reading: the fallacy arrows |
| 3.5 | `w-arc` | the big arcs (Great Circle, Ascent/Descent) |

| pattern | class | meaning |
|---|---|---|
| solid | `k-solid` | Wilber's own structure: a boundary, rung, arc or sequence he describes |
| dashed (7 6) | `k-dash` | a relation we draw to explain his claim (the feeds into the "untutored eye" bins) |
| dotted (1.5 5) | `k-dot` | absence or uncertainty: an unpublished volume, an unverified early panel |

Arrows are rare. A marker goes on a line only when the source gives the direction: "reads down", "reads up", Ascent, Descent, "transcends and includes", the axis of development. Never between two books or two concepts to suggest influence (the lesson of the works-lineage review). Curved arrows are welcome wherever they read better than straight ones. A label belongs beside the middle of its own arrow, on that arrow's side of the figure, never at one arrow's tail next to another arrow's head. Markers are defined inside each SVG so colours follow the tokens.

## Label, quotation, interpretation

- **Label** (ours, descriptive): sans, `t-label` / `t-small`. "mystical · contemplative · postformal".
- **Verbatim quotation**: serif, in curly quotes, always followed on the next line by a locator in sans muted: author, *title* (year), chapter. The line number of `library/*-full-text.md` goes on the page and in the README, not on the canvas. Elisions are marked "…"; italics inside a quotation reproduce the source's. Every quotation is grepped against `library/` before it ships.
- **Marked interpretation** (ours, a device or a judgement): sans italic muted, prefixed with ◇, class `t-ours` on the canvas and `.wv-ours` on the page. The footer explains the mark once: "◇ marks this wiki's own device".
- **Faithfulness** (from the brief): every figure rests on something in the repo (`concepts/`, `charts/`, `works/`, `library/`), named on the page. Redraw a concept; never trace a published figure, and say "redrawn" in the footer and README. Honest uncertainty is written down (a ◇ note, the README) rather than drawn around.

## Footer and signature

Bottom band of every canvas, on one baseline at y = 786: left, a `t-foot` line with the sources (book, chapter, chart), "redrawn for wilber.wiki; not a reproduction of a published figure", and the ◇ key when the mark is used. Right, the **signature**: a small Seeds of Renaissance colour mark (18 units), embedded as a base64 data URI so the SVG travels on its own, followed by `SEEDS OF RENAISSANCE · WILBER WIKI` in `t-mark`, right-aligned to the 60-unit margin. "Wilber Wiki" appears once, at the end (Rufus, 2026-10-26). The mark file is SoR's `system/logo/mark/sizes/seeds-mark-colour-128.png`. Scale the figure, never the signature. The page repeats the sources with line numbers in a Sources section.

## Motion

- Durations: fade 420 ms, move/flight 900 ms, draw 700 ms, stagger 90 ms. Ease `cubic-bezier(.4,0,.2,1)` for fades and moves, `cubic-bezier(.2,.7,.2,1)` for draws. Step interval (`data-wv-dur`) 1400–1700 ms; a piece plays in under eight seconds.
- Four appearance verbs, as classes on any element with `data-at`: `wv-fade` (opacity), `wv-draw` (a stroke draws in; needs `pathLength="1"`, so not for dashed lines), `wv-move` (from a `--wv-from` transform to rest), `wv-ghost` (a one-shot flight of a copy, visible only mid-animation; invisible in the settled frame and in exports).
- **The settled frame is the static image.** Step N is the source as authored. Play always ends on N; the step buttons can go back.
- `prefers-reduced-motion`: transitions and keyframes are off; Play jumps to the settled frame; the step buttons still work as cuts. No JS: the markup defaults to `data-step="N"`, so the figure is static and complete and only the settled caption shows.
- Keyboard: the figure root is focusable; ← → step, space plays. Deep links `#step-k`, `#play`.

## Share crops and exports

`data-og="x y w h"` and `data-square="x y w h"` on the SVG root are viewBox crops; `export.py` renders them with `preserveAspectRatio="xMidYMid slice"`. From one source it writes `index.html` (page + inlined SVG), `<slug>.svg` (standalone, tokens inlined), `<slug>.png` (2400 × 1600), `<slug>-og.png` (1200 × 630) and `<slug>-square.png` (1080 × 1080). The page declares `<meta property="og:image">` pointing at the OG file; whether Flowershow honours a per-page `og:image` is still to check (`wilberwiki-4qc`). PNG rendering uses headless Chrome and needs network access for Google Fonts; the SVG does not.

Commands, from the repo root: `python3 docs/plans/visual-brainstorm/design-language/export.py` (all pieces), `… export.py <slug>` (one), `--no-png` to skip the Chrome renders (`WV_CHROME` overrides the Chrome path). `python3 …/contrast.py` after changing a colour token.

## Embedding in Flowershow

The site is plain markdown (not MDX): raw HTML, inline SVG and scripts loaded through `config.json` `head` all work. This is live on [`/visuals`](../visuals.md).

1. `config.json` `head` loads `/assets/visuals/visuals.css`, `/assets/visuals/wv-motion.js` and the Fraunces and Inter Google Fonts. Everything is scoped under `.wv-root`, and the script returns immediately when no `[data-wv-steps]` is on the page.
2. In a markdown page, put the markers `<!-- figure:<slug> -->` and `<!-- /figure:<slug> -->` on consecutive lines, add the slug to `PIECES` in `scripts/sync-visuals.py`, and run `python3 scripts/sync-visuals.py` after `export.py`. The script copies the CSS, JS and PNGs into `assets/visuals/` and pastes the piece's animated figure block (controls, inline SVG, step captions) between the markers. It drops blank lines because a blank line would end the raw HTML block in markdown. Never edit the pasted block by hand.
3. For a static-only placement (a header image), use `<img src="/assets/visuals/<slug>.svg" alt="…">` or the PNG. The standalone SVG carries its own tokens.
4. The text alternative on the page (prose or an HTML table) travels with the figure. Alt text says what the figure claims, not what it looks like.

## Check before publishing

- [ ] Serif for Wilber's words and named terms, sans for ours; title, subtitle and eyebrow in place; nothing smaller than 10.5 on the canvas.
- [ ] Colour roles used only for things present in the figure; same-kind things share a colour; contrast script passes.
- [ ] Solid for Wilber's structure, dashed for our relations, dotted for absence; arrows only where the source gives a direction; each label beside its own arrow.
- [ ] Every quotation grepped against `library/`, line numbers on the page and in the README; ◇ on every device of ours, explained in the footer; "what is Wilber's and what is ours" written; no published figure traced.
- [ ] Footer with sources bottom left; signature (small SoR mark + SEEDS OF RENAISSANCE · WILBER WIKI) bottom right.
- [ ] The animation settles on the static frame; reduced motion honoured; the page shows the static image without JavaScript.
- [ ] Exported with `export.py`; rendered at desktop and 390 px with no overflow or collisions.
