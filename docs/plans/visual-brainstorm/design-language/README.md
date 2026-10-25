# Wilber visuals: design language

Date: 2026-10-25. Bead `wilberwiki-clq`. Brief: [`../../2026-10-24-visual-brainstorm-brief.md`](../../2026-10-24-visual-brainstorm-brief.md). Review page: [`index.html`](index.html) (swatches, type, stroke vocabulary, motion demo, both pieces). Nothing here is on the site.

This is the shared language for the whole series of Wilber visuals (the twelve directions in [`../gallery.html`](../gallery.html)). It is proven on two rebuilt pieces, [`../pre-trans-fallacy/`](../pre-trans-fallacy/) and [`../states-and-stages/`](../states-and-stages/). Files in this folder:

- `visuals.css` — tokens (light and dark), SVG classes, page chrome (figure frame, controls, quote/label/interpretation roles), step-visibility and motion rules. Scoped under `.wv-root`.
- `wv-motion.js` — the play / step controller. Deferred, no-ops when no `[data-wv-steps]` root exists.
- `export.py` — one SVG source, two outputs. Generates each piece's `index.html`, standalone `.svg`, 2× `.png`, 1200×630 `-og.png` and 1080×1080 `-square.png`.
- `contrast.py` — WCAG contrast check of the palette (run it after changing a token).
- `index.html` — the visual spec and review page.

## One principle: one SVG source, two outputs

Every piece is a folder with `source.svg` (the drawing) and `page.html` (the page around it, with a `<!-- @svg -->` placeholder). The source is authored in its **settled state**: what you see with no CSS and no JS is the static image. Animation only ever *subtracts* from that state for earlier steps (elements carry `data-at="k"`, "appears at step k"), so the settled frame and the exported image are the same drawing by construction, not by discipline. `export.py` inlines the source into the page, strips the step attributes for the standalone SVG, and renders the PNGs with headless Chrome from a viewBox crop declared on the SVG root (`data-og`, `data-square`). Edit `source.svg` or `page.html`, never `index.html` or the exports.

## Series format

Master canvas **1200 × 800** (3:2), 60-unit margins. Title block at the top (eyebrow, title, one-line subtitle), the figure in the middle band (y ≈ 170–640), passages and footer in the bottom band (y ≥ 664). The 1200 × 630 Open Graph crop is the top of the canvas (`data-og="0 0 1200 630"`): title plus figure, no passages. The square is the full canvas letterboxed (`data-square="0 -200 1200 1200"`). A portrait poster (the first pre/trans build) was rejected because it could not yield an OG crop that kept both the title and the whole figure; landscape with the passages at the bottom gives all three outputs from one layout.

## Type

Two families, each with a job. **Fraunces** (serif, optical sizes, Google Fonts) is the book's voice: titles, subtitles, the names of Wilber's terms inside a figure, and every verbatim quotation. **Inter** (sans) is the wiki's voice: labels, headers, locators, footers, controls, and our own notes. The rule a reader learns without being told is *serif = Wilber's words or his named things; sans = our apparatus*. Fallbacks are Iowan Old Style / Georgia and system-ui. Rejected: a single family (loses the Wilber/wiki distinction), and a display face with more personality (the site itself is quiet; Fraunces at weight 600 is as far as it should go).

Scale, in canvas units (the 1200-wide SVG), with the CSS class:

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
| site mark | `t-mark` | 11, tracked 1 | sans 600, muted |

Minimum text size on the canvas is 10.5 (footer); at the 2× PNG that is 21 px, at phone width on the page it is small but still legible because the whole figure scales uniformly.

## Palette and semantic roles

Tokens live on `.wv-root` (light) and `html[data-theme="dark"] .wv-root` (dark), with an OS fallback for pages that have no `data-theme`. All values below are in `visuals.css`; `contrast.py` checks every text role against paper and surface.

| role | meaning in a Wilber figure | light | dark |
|---|---|---|---|
| ink / ink-soft / muted | neutral structure and text | `#1c1917` / `#57534e` / `#6f6861` | `#f0ebe3` / `#b8b0a6` / `#978e84` |
| paper / surface | page ground / figure ground | `#f8f6f1` / `#fffdf9` | `#121110` / `#1b1917` |
| line / line-strong | hairlines, rules, grid | `#ddd7cd` / `#aaa198` | `#312d29` / `#534c45` |
| **level** | structures, stages, levels, bands of development, the "higher" | `#4338ca` (indigo) | `#a5b4fc` |
| **state** | states of consciousness; also the site's accent amber | `#b45309` | `#f5b041` |
| **fallacy** | errors, pathologies, dissociation, collapse | `#be123c` (madder) | `#fb7185` |
| **ground** | the prerational, body, nature, the "lower" | `#0f766e` (teal) | `#3dd6c0` |
| neutral fill | anything not carrying one of the roles | 5.5% ink | 7.5% ink |

Each role has a text/stroke value (`c-*`, `s-*`) and a 10–18% tinted fill (`f-*`). Contrast, measured: every text role is ≥ 4.65:1 on paper and surface in light mode and ≥ 5.4:1 in dark mode (`python3 contrast.py` prints the table).

Decisions worth knowing: the two fallacies in the pre/trans piece are the *same* colour (madder), distinguished by direction and label, because they are the same kind of thing; the earlier build coloured them differently and it read as if one were worse. "State" shares the site's amber so the series feels native to wilber.wiki; the cost is that a figure must not use amber for both a state and an interactive highlight, so interactive highlight is done with ink (filled button) and the accent ring, never a fourth hue. Rejected: Wilber's own "altitude" rainbow for levels (it would import a specific later-Wilber convention into every figure, and it is unreadable in dark mode), and a purely monochrome scheme (loses the state/structure distinction that the states piece exists to make).

## Lines, strokes and arrows

| weight | class | use |
|---|---|---|
| 1 | `w-hair` | band and box outlines, grid, rules |
| 1.5 | `w-struct` | axes, connectors, anything structural |
| 2.5 | `w-path` | a movement or reading: the fallacy arrows |
| 3.5 | `w-arc` | the big arcs (Great Circle, Ascent/Descent) |

| pattern | class | meaning |
|---|---|---|
| solid | `k-solid` | Wilber's own structure: a boundary, rung, arc or sequence he describes |
| dashed (7 6) | `k-dash` | a relation we draw to explain his claim (the feeds into the "untutored eye" bins) |
| dotted (1.5 5) | `k-dot` | absence or uncertainty: an unpublished volume, an unverified early panel |

Arrows are rare. A marker goes on a line only when the source gives the direction: "reads down", "reads up", Ascent, Descent, "transcends and includes", the axis of development. Never between two books or two concepts to suggest influence (the at6.4 lesson). Markers are defined inside each SVG (`<marker>` with a `c-ink` or `c-fallacy` path) so colours follow the theme.

## Label, quotation, interpretation

Three kinds of text, three looks, on the canvas and on the page:

- **Label** (ours, descriptive): sans, `t-label` / `t-small`. "mystical · contemplative · postformal".
- **Verbatim quotation**: serif, in curly quotes, always followed on the next line by a locator in sans muted: author, *title* (year), chapter. The line number of `library/*-full-text.md` goes in the page and README, not on the canvas. Elisions are marked "…"; italics inside a quotation reproduce the source's italics. Every quotation is grepped against `library/` before it ships.
- **Marked interpretation** (ours, a device or a judgement): sans italic muted, prefixed with ◇, class `t-ours` on the canvas and `.wv-ours` on the page. The footer explains the mark once: "◇ marks this wiki's own device". The two-bin "eye" and the "what changed is the picture" note are examples.

## Attribution footer

Every canvas ends with a one-line footer in `t-foot` and the site mark `wilber.wiki` right-aligned: sources (book, chapter, chart), "redrawn for wilber.wiki; not a reproduction of a published figure", and the ◇ explanation when the mark is used. The page repeats the sources with line numbers in a Sources section.

## Motion

- Durations: fade 420 ms, move/flight 900 ms, draw 700 ms, stagger 90 ms. Ease `cubic-bezier(.4,0,.2,1)` for fades and moves, `cubic-bezier(.2,.7,.2,1)` for draws. Step interval (`data-wv-dur`) 1400–1700 ms; a piece should play in under eight seconds.
- Four appearance verbs, as classes on any element with `data-at`: `wv-fade` (opacity), `wv-draw` (a stroke draws in; needs `pathLength="1"`, so not for dashed lines), `wv-move` (from a `--wv-from` transform to rest), `wv-ghost` (a one-shot flight of a copy, visible only mid-animation; invisible in the settled frame and in exports).
- **The settled frame is the static image.** Step N is the source as authored. Play always ends on N; the step buttons can go back.
- `prefers-reduced-motion`: all transitions and keyframes are off; Play jumps to the settled frame; the step buttons still work as instant cuts. The controller also shows "Reduced motion" in the hint.
- No JS: the markup defaults to `data-step="N"`, so the figure is static and complete; captions other than the settled one are hidden by CSS.
- Keyboard: the figure root is focusable; ← → step, space plays. Deep links `#step-k`, `#play`.

## Share-card crops

`data-og="x y w h"` and `data-square="x y w h"` on the SVG root are viewBox crops; `export.py` renders them at 1200 × 630 and 1080 × 1080 with `preserveAspectRatio="xMidYMid slice"`. In the series format the OG crop is "0 0 1200 630" and the square is "0 -200 1200 1200" (letterboxed on paper). The page declares `<meta property="og:image">` pointing at the OG file; whether Flowershow honours a per-page `og:image` is still to check (`wilberwiki-4qc`).

PNGs are exported in the light theme (the OS and most link previews are light-first; dark previews are an open question). Font loading for the PNG render needs network access to Google Fonts; the SVG does not.

## Embedding in Flowershow

1. Copy `visuals.css` and `wv-motion.js` to `assets/visuals/` and register them in `config.json` `head`, the same way `assets/roadmap/roadmap.css` and `assets/annotator/annotator.js` are: `<link rel="stylesheet" href="/assets/visuals/visuals.css"><script defer src="/assets/visuals/wv-motion.js"></script>`. Everything is scoped under `.wv-root`, and the script returns immediately when no `[data-wv-steps]` is on the page.
2. In a markdown page, paste the piece's figure block as raw HTML: `<div class="wv-root" data-wv-steps="4" data-step="4" data-wv-dur="1500"><div class="wv-controls" data-wv-controls></div><figure class="wv-figure"><div class="wv-frame">…source.svg…</div><figcaption data-wv-caption>…</figcaption></figure></div>`. Flowershow's Tailwind bundle is pre-purged, so nothing here relies on utility classes.
3. For a static-only placement (a header image), use `<img src="/assets/visuals/<slug>.svg" alt="…">` or the PNG. The standalone SVG carries its own tokens and a `prefers-color-scheme` fallback; it follows the OS, not the site toggle, which is acceptable for an image.
4. Dark mode on the site: `html[data-theme="dark"] .wv-root` overrides, already in `visuals.css`.

## Open questions for Rufus

1. Serif for Wilber's words, sans for ours: is that distinction worth keeping as a rule for the whole series, or is it too subtle to carry meaning?
2. Both fallacies in one colour (madder) versus the earlier amber/rose pair: the single colour is more principled; is it less readable?
3. Light-only PNG exports, or also dark variants (`<slug>-dark.png`) for people who share from dark-mode screenshots?
4. The square crop is letterboxed rather than recomposed; a true square layout would need a second arrangement per piece and would break "one source". Acceptable?
5. The pre/trans canvas dropped the Engler line ("you have to be somebody before you can be nobody"); it is on the page. Keep it off the image?
