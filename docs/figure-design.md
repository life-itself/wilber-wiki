# Figure design for wilber.wiki

The settled rules for the explanatory figures (diagrams, charts, posters) that go on wilber.wiki and get shared on their own. This is operational documentation: what a new figure must follow and how to build one. The exploration that produced it, with both pieces and the review page, is in [`plans/visual-brainstorm/`](plans/visual-brainstorm/) (bead `wilberwiki-clq`). Decisions date from 2026-10-26.

## Where the rules come from

The figures follow the **Seeds of Renaissance diagram system**: https://design.seedsofrenaissance.org/diagrams (source: [`diagrams.md`](https://raw.githubusercontent.com/life-itself/design/refs/heads/main/projects/sor-design-system/diagrams.md) in `life-itself/design`). Its one-paragraph summary applies here unchanged: after the FT, the Economist and Tufte, restraint over decoration; one face, no bold; ink lines and solid arrowheads; no outlines on boxes; one accent for the one thing the figure is about; title and grey subtitle top left, signature bottom right; every figure must read at 400 px in a feed and printed in black and white. Rufus chose it on 2026-10-26 after an earlier design language (two typefaces, four colour roles, outlined rounded boxes, dashed and dotted lines) was judged "not at all beautiful yet". We also reuse its tooling: text set as outlines with `fontTools` and HarfBuzz (its `outline.py` approach), its `figure.py` helpers, its export shape (tight SVG for the page, padded PNG for sharing).

**What we follow exactly:** typography (Apfel Grotezk, Regular and Mittel, never Fett), the drawing rules (line weights, panels, arrowheads, padding, labelling on the thing named, no legends), the layout (1600 px canvas, 72 px margin, title and subtitle placement, source bottom left, signature bottom right), the exports, and the 400 px and black-and-white checks.

**Where we differ, deliberately:** colour and accent are wilber.wiki's own (below); the signature names both Wilber Wiki and Seeds of Renaissance; a Wilber figure also carries conventions about quotation, interpretation and sourcing that SoR's figures don't need. The type scale may be varied for a figure that needs it (none has so far).

## Colour

Light grounds are transparent on the page and white in a shared PNG; dark grounds are night. Ink becomes chalk on night; the tint takes its night value. Nothing relies on colour alone: the tint prints light grey and the accent prints darker than the tint.

| Role | Light | Night | Use |
|---|---|---|---|
| ink | `#1b1916` | `#ece7dc` (chalk) | text, lines, arrowheads |
| muted | ink at 60% opacity | chalk at 60% | subtitle, secondary lines, source, signature text |
| tint | `#f8e8d6` (cream) | `#5a2a14` | panels (groups) and the key area; never text |
| accent | `#b5451b` (rust) | `#f09a52` | the marks the figure is about: a line, an arrow, a ring; the label of the key area at most |
| ground for PNGs | `#ffffff` | `#171613` | sharing and review renders only |

Why rust and cream rather than SoR's red and pink: the site already uses an amber family (`#d97706` for the roadmap star), and a warm red-brown ink with a cream tint reads as book paper and ink, which suits a wiki about a writer; it also prints well in greyscale (accent ≈ 90 grey, tint ≈ 233). Contrast: rust on white 5.5:1, the night accent on night 8.1:1. SoR red (`#e5201c`, tint `#fbdbdb`, night tint `#6b1a17`) stays available in `wv.py` as the `red` variant so a figure can be rendered in it for comparison; it is not used on the site.

One accent per figure, and only on the mark that carries the claim. Two things that are the same kind of thing share the accent (the two fallacies in the pre/trans figure); never a second hue to rank them. The tint says "these belong together" (the two nonrational tiers; the four words that move from ladder to lattice).

## Type

Apfel Grotezk only, Regular and Mittel (SIL Open Font License; files and licence in `plans/visual-brainstorm/design-language/fonts/`). No Fett, no italic: hierarchy comes from size and from 60% ink. Sizes at a 1600 px canvas, as SoR's scale:

| Role | Face | px | Use |
|---|---|---|---|
| title | Regular | 46 | top left; ideally the claim, not the topic |
| subtitle | Regular, 60% | 28 | one line under the title: what the figure shows |
| heading | Mittel | 32 | panel and column headings |
| group label | Mittel | 34 | bracket and group labels |
| label | Regular | 29 | annotations, rung and axis names, on the thing they name |
| secondary | Regular, 60% | 26 | second lines, glosses |
| tag | Mittel, caps, tracked .1em | 21 | one-to-three-word tags only; use sparingly, a heading usually does the job |
| source and signature | Regular / Mittel caps, 60% | 20 | bottom line |

Nothing below 26 px except tags and the bottom line, so the smallest text is still about 7 px at 400 px wide. The scale may be varied for a figure that needs it (a wide table, a long list) provided the hierarchy stays size-based and the 400 px check passes; say so in the piece's README. On HTML pages around a figure, Apfel is loaded from the repo copies with Hanken Grotesk (Google Fonts) as the fallback.

## Signature

Bottom right, its right edge on the content's right edge (the 72 px margin), its bottom 56 px above the canvas edge. The Seeds of Renaissance mark, 64 px, then one line at 20 px in 60% ink: `WILBER WIKI · SEEDS OF RENAISSANCE · wilber.wiki` (the first two in Mittel capitals tracked .1em, the URL in Regular). Light grounds: the colour mark on its white disc. Dark grounds: the colour-dark mark, no disc. The mark files are SoR's (`system/logo/mark/sizes/seeds-mark-colour-128.png` and `-colour-dark-128.png`), embedded in the SVG as data URIs so it travels with the image. Scale the figure, never the signature. The source line sits bottom left on the signature's baseline: `Source: Ken Wilber, Sex, Ecology, Spirituality (1995), ch. 6`, or `Sources: … · …`.

## Wilber-specific conventions

- **Labels** are ours and are set as labels: a tier name, a gloss ("mystical, contemplative, postformal"), a heading. They summarise the concept page or chart they come from. Sentence case; no quotation marks.
- **Verbatim quotations** are rare on a canvas and never paraphrased when present: they are set in curly quotes exactly as the full text has them, with the book and chapter beside them. Every quotation, on the canvas or on the page, is grepped against `library/*-full-text.md` before it ships and its line number is recorded in the piece's README and on its page (the line number itself stays off the canvas). Elisions are marked "…"; italics in the source are kept on the page (the canvas has no italic, so a quotation with italics belongs on the page).
- **Interpretation**: anything that is our device rather than Wilber's (a way of drawing, an arrow we placed, a pairing of names from two books) is listed under "What is Wilber's and what is ours" on the page and in the README. A figure doesn't carry a legend or a mark for this; the subtitle and the page carry it. If a device could be mistaken for Wilber's own diagram, don't draw it.
- **Faithfulness rules** (from the brief): every figure rests on something in the repo (`concepts/`, `charts/`, `works/`, `library/`), named on the page. Redraw a concept; never trace a published figure, and say "redrawn" in the README. Lines between things never imply influence or derivation unless the text gives the direction; arrows are for a direction the source states (reads down, reads up, moves across). Honest uncertainty is written down, not drawn around: a known simplification goes in the README and on the page.
- **Fewer things.** Ask what the one idea is and how little ink conveys it. Cells can be empty; a second diagram that restates the first is cut; glosses that don't change the reading are cut.

## Motion

The static image comes first and must stand alone. Animation is a page-only enhancement that settles exactly on the static frame: every element is authored in its settled state and carries `data-at="k"`, the step it appears at, so the settled frame and the export are the same drawing by construction. Steps only add; nothing moves off, and nothing flies. Verbs: a fade (0.9 s) and, for an accent arrow, a draw (1.5 s, the head following). Step interval about 2.4 s; a piece plays in under ten seconds. Captions change with the step; the markup defaults to the last step, so with no JavaScript the page shows the static image and its caption. `prefers-reduced-motion`: transitions are off, Play jumps to the settled frame, the step buttons cut. Keyboard: arrows step, space plays; `#step-k` and `#play` deep links.

## Exports and building a figure

Everything lives in `plans/visual-brainstorm/design-language/` until a first figure goes on the site, when `wv.py`, `wv.css`, `wv-motion.js`, `fonts/` and `mark/` move to `assets/figures/`.

- `wv.py`: the house style as code (type, colour, `text`, `tag`, `wrap`, `line`, `arrow`, `curved_arrow`, `panel`, `bracket`, `signature`) and `build()`.
- A piece is a folder with `figure.py` (its `draw()` returns a `Fig`), `page.html` (the page around it, with `<!-- @svg -->` and `<!-- @steps -->` placeholders) and `README.md`.
- `build()` writes, from one drawing: `<slug>.svg` (tight, transparent, text as outlines, light and dark via CSS inside the SVG, so it renders without the font installed and follows the site's `data-theme` when inlined); `<slug>.png` and `<slug>@2x.png` (the full 1600 px canvas with its margin, on white, for sharing alone); `<slug>-og.png` (1200 × 630, the canvas fitted on white, for Open Graph); `<slug>-dark.png` (on night, for review); `<slug>-accent-<name>.png` for each accent variant (review only); `index.html` (the animated page).
- Commands, from the repo root: `python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz` once; then `.venv/bin/python docs/plans/visual-brainstorm/design-language/build.py` (all pieces) or `.venv/bin/python docs/plans/visual-brainstorm/<slug>/figure.py` (one), with `--no-png` to skip the Chrome renders (`$CHROME` overrides the Chrome path).
- Embedding on the site: register `wv.css` and `wv-motion.js` in `config.json` `head`, paste the piece's figure block (the `.wv-fig` div from its `index.html`) as raw HTML in the markdown page, or use `<img src="…/<slug>.svg">` for a static placement. The HTML table or prose on the page is the text alternative and travels with the figure. Alt text says what the figure claims, not what it looks like.

## Check before publishing

- [ ] Apfel only, Regular and Mittel; title, grey subtitle, labels on the things they name; no legend.
- [ ] Solid ink lines with round caps, 4 px for what matters and 2 px for scaffolding; solid arrowheads, only where the source gives a direction; no dashes.
- [ ] Panels without outlines, sized to their text, 40 px padding; the tint only for groups and the key area; the accent only on the mark the figure is about.
- [ ] Reads at 400 px wide and in greyscale (the review page shows both); dark render checked.
- [ ] Signed bottom right with the mark; source bottom left; content's right edge on the signature's.
- [ ] Every quotation grepped against `library/`, line numbers in the README and on the page; "what is Wilber's and what is ours" written; no published figure traced.
- [ ] The animation settles on the static frame; reduced motion honoured; the page shows the static image without JavaScript.
- [ ] Exported with `build()`: tight SVG, PNG and @2x, OG crop.
