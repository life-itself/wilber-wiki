# The Pre/Trans Fallacy, in one picture

Option 05 from the [visual brainstorm gallery](../gallery.html#o5), rebuilt on 2026-10-25 in the shared [design language](../design-language/README.md). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

One SVG source, two outputs. The static image is a 1200 × 800 landscape canvas: title block, then the three bands of development on the left (prerational, rational, transrational, with Wilber's "pre-ego → ego → trans-ego" axis), the untutored eye's two bins on the right (rational, nonrational) with dashed feeds showing the outer two bands landing in one bin, the two errors drawn as arrows along the spectrum's edges (reductionism down, elevationism up), and two verbatim passages with locators at the bottom. The animated version plays in four steps and settles on exactly that frame: (1) the bands; (2) the eye's bins appear and ghost copies of the transrational and prerational bands fly into the nonrational bin while the feeds fade in; (3) reductionism draws in; (4) elevationism draws in; (5) the passages and footer.

Files: `source.svg` (the drawing, authored in its settled state), `page.html` (the page template), and the generated outputs `index.html`, `pre-trans-fallacy.svg`, `pre-trans-fallacy.png` (2400 × 1600), `pre-trans-fallacy-og.png` (1200 × 630, the top of the canvas), `pre-trans-fallacy-square.png` (1080 × 1080, letterboxed). Regenerate with `python3 ../design-language/export.py pre-trans-fallacy`.

## Sources

All quoted text is verbatim from `library/1995-sex-ecology-spirituality-full-text.md` (revised second edition text). Line numbers are for that file.

- "The essence of the pre/trans fallacy is itself fairly simple: since both prerational states and transrational states are, in their own ways, nonrational, they appear similar or even identical to the untutored eye." — SES ch. 6, line 2551. On the canvas and the page; the fragment "they appear similar or even identical" is also set inside the nonrational bin.
- "Freud was a reductionist, Jung an elevationist—the two sides of the pre/trans fallacy. And the point is that they are *both* half right and half wrong." — SES ch. 6, line 2561. On the canvas and the page.
- "pre-ego to ego to trans-ego" — SES ch. 14 note, line 8925 (Wilber's gloss beside the Engler quotation). The axis label.
- Band descriptions (infantile, egocentric, magical, mythic / mystical, contemplative, postformal) follow `concepts/pre-trans-fallacy.md`, which summarises SES ch. 6. They are labels in the wiki's words, set in sans.
- Essay history (ReVision 1980, Eye to Eye 1983): `docs/plans/2026-10-09-pre-trans-fallacy-essay-source.md`. The essay is not in `library/`, so nothing is quoted from it.

## Faithfulness

Wilber's: the three bands and their names; pre-ego/ego/trans-ego; the resemblance claim and "untutored eye"; the two fallacies, their names and directions; Freud and Jung as the pair; "both half right and half wrong".

Ours, marked ◇ on the canvas: the two-bin "eye" as a picture of his resemblance sentence; the collapse animation (the outer bands flying into the bin); the fallacy arrows along the spectrum's edges; the one-line band descriptions. The footer says "◇ marks this wiki's own device". No published figure was reproduced.

Changes from the first build: landscape instead of portrait (so the OG crop keeps title and figure); both fallacies in the fallacy colour rather than amber/rose (they are the same kind of error); the Engler line ("You have to be somebody before you can be nobody") moved from the canvas to the page, because it is Engler's sentence from a footnote and the canvas should carry only Wilber's; band descriptions in sans, quotations in serif, per the language.

## How it would integrate into the site

See the design-language README, "Embedding in Flowershow". Static first: `pre-trans-fallacy.svg` or `.png` as an `<img>` at the top of `concepts/pre-trans-fallacy.md`, `alt` from the text alternative on the page. Animated: the figure block from `page.html` pasted as raw HTML, with `visuals.css` and `wv-motion.js` registered in `config.json` `head`. The OG crop is the candidate `og:image` for that page (`wilberwiki-4qc`, pending a check that Flowershow allows a per-page image).

## Open questions for Rufus

1. Is the collapse animation (ghost bands flying into the bin) a help or a gimmick? The static frame does not depend on it.
2. Keep the Engler line off the canvas?
3. Same-colour fallacies: readable enough, or bring back a second hue?
