# Design language: the exploration folder

The durable spec is [`docs/figure-design.md`](../../../figure-design.md); read that first. This folder holds the tooling the spec describes and the review material for the 2026-10-26 pass (bead `wilberwiki-clq`, brief: [`../../2026-10-24-visual-brainstorm-brief.md`](../../2026-10-24-visual-brainstorm-brief.md)). Nothing here is on the site.

The figures use the **Seeds of Renaissance diagram system** (https://design.seedsofrenaissance.org/diagrams) for typography, drawing rules, layout, exports and checks, with wilber.wiki's own colour and accent and a signature that names both. Where we follow it and where we differ is set out in the spec.

## Files

- `index.html`: the review page. Both pieces, static and animated, in the chosen accent and in SoR red for comparison, on night, at 400 px, in greyscale, as OG cards, and before/after against the rejected build.
- `wv.py`: the house style as code and the exporter (`build()`). `build.py` runs every piece.
- `wv.css`, `wv-motion.js`: the page layer: figure frame, step controls, reveal rules, reduced motion. `page.css`: chrome for these review pages only.
- `fonts/`: Apfel Grotezk Regular and Mittel (OFL; `LICENSE.txt`). `mark/`: the SoR mark, colour and colour-dark, 128 px, for the signature.
- `before/`: the two rejected renders, kept for the before/after on the review page.

Build: `python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz`, then `.venv/bin/python build.py` (add `--no-png` to skip Chrome).

## Notes from this pass

- **Typeface.** A specimen of Apfel Grotezk, Instrument Sans, IBM Plex Sans, Source Sans 3 and Albert Sans was rendered before the direction was settled on following SoR's typography. Apfel is OFL (confirmed on the Collletttivo page and in the font's name table), so there is no licence obstacle. Plex was the runner-up: a more scholarly register, but it would have made the figures a different system from SoR's rather than a sibling.
- **Accent.** Candidates were computed for contrast and greyscale value (`#c2410c` ochre, `#b5451b` rust, `#d97706` the site amber, SoR red). The site amber fails as text on white (3.2:1); ochre rendered slightly orange against the cream tint; rust held as ink-like against both the tint and chalk. SoR red is kept as a variant.
- **Cuts.** The pre/trans figure lost the "untutored eye" bins, the dashed feeds, the axis arrow, the on-canvas quotations and the ◇ interpretation mark: the shared tint says "alike", and the two arrows skipping the rational tier say the rest. The states figure lost the 24 boxed cells, the "a structure, on the ladder" repeats, the chart-1 worldview names on every rung, the state glosses, the axis tags and the on-canvas quotation and note; it keeps an empty hairline lattice whose rows sit level with the ladder's lower rungs.
- **Checks done.** Each piece went through three rounds against the SoR reference renders: baselines aligned across the tiers and their labels; the overflowing "gross/psychic" column label replaced by IS's own list form "gross"; colliding secondary lines wrapped; tags that duplicated headings removed; 400 px and greyscale sheets rendered; dark renders checked; the animated pages checked at 1100 px and 390 px, at step 0 and at the settled step.
