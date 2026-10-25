# The Pre/Trans Fallacy, in one picture

Option 05 from the [visual brainstorm gallery](../gallery.html#o5), redrawn on 2026-10-26 under the rules in [`docs/figure-design.md`](../../../figure-design.md) (the Seeds of Renaissance diagram grammar with wilber.wiki's accent). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

One drawing, built by `figure.py` with `../design-language/wv.py`. The static image is a 1600 × 944 canvas: title, subtitle ("Before reason and beyond it both look nonrational, so each gets mistaken for the other"), three tiers stacked in the middle, prerational at the bottom, rational, transrational on top, each with a name and a one-line gloss. The two outer tiers sit in the tint because both are nonrational and, to the untutored eye, alike; the rational tier is open between them. Two accent arrows beside the stack are the only coloured marks: reductionism on the right, from the transrational down to the prerational, labelled "the transrational read as prerational (Freud)"; elevationism on the left, from the prerational up to the transrational, "the prerational read as transrational (Jung)". Each skips the rational tier, which is the fallacy. Source line bottom left; signature bottom right.

The animated page plays in three steps and settles on that frame: (0) the three tiers; (1) reductionism draws in, its label follows; (2) elevationism. Captions change with the step.

Files: `figure.py` (the drawing), `page.html` (the page template), and the generated `index.html`, `pre-trans-fallacy.svg` (tight, transparent, outlines; light and dark), `pre-trans-fallacy.png` and `@2x.png` (the canvas on white), `pre-trans-fallacy-og.png` (1200 × 630), `pre-trans-fallacy-dark.png` and `-accent-red.png` / `-accent-rust.png` (review). Regenerate with `python3 figure.py` (see the spec for the environment).

## Sources

Nothing on the canvas is set as a quotation. The tier names, the fallacy names and directions, and Freud and Jung are Wilber's; the glosses summarise `concepts/pre-trans-fallacy.md`. On the page, verbatim from `library/1995-sex-ecology-spirituality-full-text.md` (line numbers for that file):

- "The essence of the pre/trans fallacy is itself fairly simple: since both prerational states and transrational states are, in their own ways, nonrational, they appear similar or even identical to the untutored eye. And once pre and trans are confused, then one of two fallacies occurs:" — SES ch. 6, line 2551.
- "Freud was a reductionist, Jung an elevationist—the two sides of the pre/trans fallacy. And the point is that they are *both* half right and half wrong." — SES ch. 6, line 2561.
- "pre-ego to ego to trans-ego" — SES ch. 14 note, line 8925; the order of the tiers.
- The two directions as Wilber states them, lines 2553 ("all higher and transrational states are *reduced* to lower and prerational states … the route taken by Freud") and 2557 ("one will *elevate* all prerational states to some sort of transrational glory … Jung and his followers"), paraphrased in the arrow labels.

## Faithfulness

Wilber's: the three bands and their names; the resemblance "to the untutored eye"; the two fallacies, their names and directions; Freud and Jung; "both half right and half wrong".

Ours: the stack as a picture with the two nonrational tiers in one tint and the rational tier open between them; the arrows beside the stack, each skipping the middle; the glosses; the subtitle. No published figure was reproduced.

Left out on purpose: Campbell and Eco-Romanticism (SES's extended cases); the Engler line (a footnote, and Engler's sentence); the earlier build's "untutored eye" bins, dashed feeds, axis arrow, on-canvas quotations and ◇ mark. The resemblance claim is now carried by the shared tint and the subtitle rather than a second diagram.

## How it would integrate into the site

Static: `pre-trans-fallacy.svg` as an `<img>` at the top of `concepts/pre-trans-fallacy.md`, alt text from the figure's `<title>`. Animated: the `.wv-fig` block from `index.html` as raw HTML, with `wv.css` and `wv-motion.js` registered in `config.json` `head`. The OG crop is the candidate `og:image` for that page (`wilberwiki-4qc`, pending a check that Flowershow allows a per-page image).

## Open questions for Rufus

1. The rational tier is open (no panel) between the two tinted ones: does it read as "seen as what it is", or as a missing box?
2. Quotations off the canvas: right for this piece, or should the "untutored eye" sentence be allowed on the image as the one verbatim line?
3. Accent: rust (as built) or SoR red (`pre-trans-fallacy-accent-red.png`)?
