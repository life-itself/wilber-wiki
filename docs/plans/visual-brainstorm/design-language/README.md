# Wilber visuals: design language (tooling and exploration notes)

**The spec lives in [`docs/figure-design.md`](../../../figure-design.md).** This folder holds the implementation and the review page; this file records how the language was arrived at. Bead `wilberwiki-clq`. Brief and status log: [`../../2026-10-24-visual-brainstorm-brief.md`](../../2026-10-24-visual-brainstorm-brief.md).

## Files

- `visuals.css` — tokens (light only), SVG classes, page chrome (figure frame, controls, quote/label/interpretation roles), step-visibility and motion rules. Scoped under `.wv-root`.
- `wv-motion.js` — the play / step controller. Deferred, no-ops when no `[data-wv-steps]` root exists.
- `export.py` — one SVG source, two outputs. Generates each piece's `index.html`, standalone `.svg`, 2× `.png`, 1200×630 `-og.png` and 1080×1080 `-square.png`.
- `contrast.py` — WCAG contrast check of the palette tokens.
- `index.html` — the review page: swatches, type, stroke vocabulary, text roles, motion demo, share crops, and both pieces with static and animated outputs side by side.

## How it was arrived at

- **2026-10-24.** An options gallery of twelve directions (`../gallery.html`) and two builds: a portrait pre/trans poster and a page-only ladder-to-lattice toggle.
- **2026-10-25.** This language: two type voices (serif for Wilber, sans for the wiki), four semantic colour roles, a stroke vocabulary with meanings, the ◇ mark for our devices, a 1200 × 800 series canvas, and the one-source/two-outputs principle with `export.py`. Both pieces rebuilt in it.
- **2026-10-26, morning.** Rufus: "not at all beautiful yet". A separate pass rebuilt everything on the Seeds of Renaissance diagram grammar (https://design.seedsofrenaissance.org/diagrams): Apfel Grotezk, no bold, no outlines, straight ink arrows, panels in a pale tint, text as outlines. Kept in git at `822a1d3`.
- **2026-10-26, later.** Rufus compared the two and chose this one: "the old diagrams were often diagrammatically much better … just go with it". Dark mode dropped; curved arrows welcome; the figures signed with the SoR mark and "WILBER WIKI · SEEDS OF RENAISSANCE". Seeds of Renaissance is the signature partner and the reference for restraint.
- **Polish pass, same day.** Nits fixed (the fallacy labels now sit beside the middle of their own arrows; the "formless sleep" header gloss no longer overflows), dark tokens and exports removed, signature added, spacing tidied, spec moved to `docs/figure-design.md`.

Two lessons recorded in the spec: polish rather than restyle, and diagrammatic content is what makes these engaging.

## Alternatives that were tried or rejected

- A single typeface (loses the Wilber/wiki voice distinction); a display face with more personality (the site is quiet).
- Wilber's altitude rainbow for levels; monochrome.
- Two hues for the two fallacies (read as a ranking).
- Portrait canvas (no good OG crop).
- Straight arrows and no outlines (the SoR pass): cleaner, but it cut the diagrammatic content.
- Dark-mode theming of the figures: built, then dropped as not needed.

## Still open (see also each piece's README)

1. Fonts and colours are tokens and may be swapped at the end; nothing else should need to change.
2. Whether Flowershow honours a per-page `og:image` (`wilberwiki-4qc`).
3. The square crop is letterboxed rather than recomposed.
