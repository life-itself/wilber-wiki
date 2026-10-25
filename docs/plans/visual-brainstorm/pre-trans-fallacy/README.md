# The Pre/Trans Fallacy, in one picture

Option 05 from the [visual brainstorm gallery](../gallery.html#o5), taken to a polished state. Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

A poster-format explainer (portrait, 960 × 1270 drawing units) of Wilber's pre/trans fallacy. Left: the three bands of development (prerational, rational, transrational) with his "pre-ego → ego → trans-ego" axis. Right: what "the untutored eye" sees, only two bins, rational and nonrational, with both the prerational and the transrational landing in the second. Inside the spectrum, two arrows mark the two errors: reductionism (Freud) reads trans down as pre; elevationism (Jung) reads pre up as trans. Three verbatim passages sit beneath the diagram.

Files: `index.html` (the page: poster, text alternative, faithfulness notes, sources), `pre-trans-fallacy.svg` (static export of the same drawing, self-contained, light palette with a dark `prefers-color-scheme` override).

## Sources

All quoted text is verbatim from `library/1995-sex-ecology-spirituality-full-text.md` (revised second edition text). Line numbers are for that file.

- "The essence of the pre/trans fallacy is itself fairly simple: since both prerational states and transrational states are, in their own ways, nonrational, they appear similar or even identical to the untutored eye." — SES ch. 6, line 2551.
- "Freud was a reductionist, Jung an elevationist—the two sides of the pre/trans fallacy. And the point is that they are *both* half right and half wrong." — SES ch. 6, line 2561.
- "You have to be somebody before you can be nobody." — Jack Engler, quoted by Wilber in SES ch. 14 note, line 8925. The same note contains Wilber's own gloss "pre-ego to ego to trans-ego", used on the axis.
- Band descriptions (infantile, egocentric, magical, mythic / mystical, contemplative, postformal) follow `concepts/pre-trans-fallacy.md`, which summarises SES ch. 6. They are labels in the wiki's words, not quotations.
- Essay history (ReVision 1980, Eye to Eye 1983): `docs/plans/2026-10-09-pre-trans-fallacy-essay-source.md`. The essay is not in `library/`, so nothing is quoted from it.

## Faithfulness

Wilber's: the three bands and their names; the pre-ego/ego/trans-ego sequence; the resemblance claim and the phrase "untutored eye"; the two fallacies, their names and direction; Freud and Jung as the paradigm pair; "both half right and half wrong"; the Engler line.

Ours: the two-bin "eye" as a picture of his resemblance sentence; the fallacy arrows drawn along the spectrum's edges; the one-line band descriptions; type and colour. The poster says so in its footer. It does not reproduce any published figure; the pre/trans essay's own diagrams (if any) were not consulted.

Left out on purpose: Campbell and Eco-Romanticism (SES's extended cases), the "oceanic" Freud detail, and any attribution of either error to people or movements beyond the two Wilber names in the quoted sentence.

## How it would integrate into the site

Flowershow renders raw HTML inside markdown and loads site-wide CSS/JS via `config.json` `head` (precedent: `assets/roadmap/roadmap.css`, `assets/annotator/`). Three options, cheapest first:

1. **Static image.** Copy `pre-trans-fallacy.svg` to `assets/visuals/pre-trans-fallacy.svg` and embed it at the top of `concepts/pre-trans-fallacy.md` with a plain `<img>` (or `![]()`), `alt` set to the text alternative. Dark mode: the SVG carries a `prefers-color-scheme` media query, which works when the file is referenced via `<img>` in current browsers, but it tracks the OS setting rather than Flowershow's `data-theme` toggle. Acceptable for a first ship; see open question 2.
2. **Inline SVG + scoped stylesheet.** Paste the `<svg>` into the concept page inside a `<div class="wv-root">`, add `assets/visuals/visuals.css` defining the `.wv-root svg .f-*`/`.s-*`/`.t-*` classes with `html[data-theme="dark"]` overrides (the pattern `roadmap.css` already uses), and register it in `head`. Follows the site theme toggle exactly. The CSS in `index.html` under `.poster svg` is the stylesheet to lift.
3. **Open Graph card.** A 1200 × 630 crop (title + the two columns, no quotes) exported to PNG for `og:image`, if Flowershow allows a per-page image (`wilberwiki-4qc`).

The text alternative in `index.html` should travel with it, either as `alt` or as a `<details>` under the figure.

## Open questions for Rufus

1. Is the two-bin "eye" device acceptable as a labelled interpretation, or should the right-hand column be dropped so the poster shows only Wilber's own elements (three bands and two arrows)?
2. Ship as a static `<img>` first (OS-level dark mode only) or go straight to inline SVG with a scoped stylesheet (site toggle respected, more plumbing)?
3. Should the Engler quotation stay? It's the most quotable line, but it comes from a footnote and is Engler's sentence, not Wilber's.
4. Whether to pull the 1980 essay into `library/` eventually so the poster can cite the original rather than SES.
