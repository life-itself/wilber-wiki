# Two ways to flatten the Kosmos

Subtle reductionism, the figure the four-quadrants piece deliberately left room for (its README, "Decisions": "Leave subtle reductionism off this figure; it's a candidate for its own figure"). Built on 2026-10-26 in the shared design language ([`docs/figure-design.md`](../../../figure-design.md)). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

The sequel to [One thought, four windows](../four-quadrants/): the same quadrant grid, the same four windows with their pronouns and small drawings and the same interior purple, drawn three times. One SVG source, two outputs. The static image is a 1200 × 800 canvas: title block ("Two ways to flatten the Kosmos"); then three grids side by side under column heads INTERIOR / EXTERIOR. Left, **the Kosmos**: all four windows filled (I, It, We, Its, each with its drawing from the previous figure and a one-word gloss: a meaning, a brain state, a shared language, a social system), the thought at the crossing; under it, the sans line "every interior has an exterior correlate, which is what makes both reductions tempting" and Wilber's "each quadrant is intimately correlated with, dependent upon, but not reducible to, the others". Middle, **gross reductionism**: three windows are empty dotted outlines with madder arrows into the Upper Right, which is tinted madder and holds only scattered dots labelled "atoms"; under it, "nothing but atoms: no interiors anywhere, yet not, in Wilber's telling, the main story", his verdict "by and large it has *not* been historically that influential", and his targets (the Epicureans, Holbach, La Mettrie). Right, **subtle reductionism**: the two interior windows are empty dotted outlines, two madder arrows carry "I reduced to It · thoughts as brain states" and "We reduced to Its · culture as social integration" into the exterior half, which is tinted madder and holds one web of connected nodes labelled "the great interlocking web"; under it, "the web is kept whole and every within is gone: a holism of surfaces, with nothing inside it", his verdict "the truly devastating contributor to modern flatland ontology", and his targets (systems theorists, structural/functionalists, "new paradigm" and "ecological/holistic" theories). The interior purple is present only in the first grid: in both reductions it is gone, and madder is where the windows were emptied into. Below, a ◇ note, two verbatim passages from SES ch. 4 with locators, the footer and the signature.

The animation settles on exactly that frame, N = 5 at 1500 ms (7.5 s):

0. The Kosmos grid, as the previous figure drew it.
1. Gross reductionism's head and grid appear with all four windows filled (copies of the Kosmos windows; they exist only at this step).
2. The collapse: ghost copies of the Upper Left, Lower Left and Lower Right windows fly into the Upper Right; the three windows are left as dotted outlines; the arrows draw; the Upper Right turns madder and its brain-state trace gives way to atoms. The gross grid's summary, verdict and targets appear.
3. Subtle reductionism's head and grid appear with all four windows filled (the interior copies and the exterior drawings exist only at this step).
4. The collapse: ghost copies of the two interior windows fly right; they are left as dotted outlines; the arrows draw with their labels; the exterior half turns madder and the web is drawn over it. The subtle grid's summary, verdict and targets appear.
5. The ◇ note, the passages, the footer and the signature.

Mid-animation elements (the filled copies in grids 2 and 3; the trace, network and aspect labels in grid 3's exterior half) are authored `opacity="0"` with `data-from`/`data-until`, so the settled frame and all exports leave them out; the ghost flights are `wv-ghost` and invisible when settled.

Files: `source.svg` (the drawing, authored in its settled state), `page.html` (the page template), and the generated outputs `index.html`, `subtle-reductionism.svg`, `subtle-reductionism.png` (2400 × 1600), `subtle-reductionism-og.png` (1200 × 630, the top of the canvas: title and the three grids with their verdicts, no passages), `subtle-reductionism-square.png` (1080 × 1080, letterboxed). Regenerate with `python3 ../design-language/export.py subtle-reductionism`. The slug is not yet in `export.py`'s `PIECES` list (shared file, left alone); passing it as an argument works.

## Sources

All quoted text is verbatim from `library/1995-sex-ecology-spirituality-full-text.md` (revised second edition text), ch. 4 "A View from Within", sections "Subtle reductionism" and "A tour of the four quadrants", unless marked ch. 12. Line numbers are for that file; each was grepped on 2026-10-26 (a script matched every string below after normalising quotation marks and stripping italics). Italics inside quotations are Wilber's.

On the canvas:

- "each quadrant is intimately correlated with, dependent upon, but not reducible to, the others." — line 1931. Under the Kosmos grid, with a leading elision.
- "by and large it has *not* been historically that influential" — line 1853. Under the gross grid, with a leading elision.
- "the truly devastating contributor to modern flatland ontology" — line 1855 (the source has a capital T; set lower case inside the quotation marks as a fragment). Under the subtle grid.
- "the great interlocking web" — line 1871; the same phrase at line 1865. The web's label.
- "atoms" — line 1843 ("reduces all the higher-order structures of the Upper-Right quadrant to atomic or subatomic particles"; "atoms" is Wilber's word at 1845, "They do not reduce all holons to atoms", and 1851).
- Passage, bottom left — line 1851: "They don't reduce everything to atoms; they reduce everything in the Left-Hand to a Right-Hand description in the "system." They reduce a four-quadrant holism (or Kosmic holism) to merely a Right-Hand holism, a flatland holism." The inner double quotation marks are set as single quotes on the canvas because they sit inside the outer pair; the words are unchanged.
- Passage, bottom right — line 1863: "the downside of the Enlightenment was that it took a Kosmos of *both* Left and Right dimensions and reduced it to a cosmos that could be empirically (or monologically) described: it *collapsed the Left half to its correlates on the Right half*. Its great crime was not gross reductionism but *subtle reductionism*." With a leading elision (the sentence begins "No, the downside…").
- Targets, gross: "starting with the Epicureans and running to Holbach, La Mettrie, and the like" — line 1843.
- Targets, subtle: "they are the systems theorists and the structural/functionalists, in all their forms, from General System Theory to modern dynamic systems theory to many of the "new paradigm" and "ecological/holistic" theories" — line 1845. The canvas sets "systems theorists · structural/functionalists" and ""new paradigm" and "ecological/holistic" theories".

Behind the sans labels (ours, paraphrasing):

- Gross grid's sub-head "all quadrants to the Upper Right, then the Upper Right to atoms" and the two-move animation: "Gross reductionism *first* reduces *all* quadrants to the Upper-Right quadrant, and *second*—this is the gross part—then reduces all the higher-order structures of the Upper-Right quadrant to atomic or subatomic particles" — line 1843.
- "no interiors anywhere": "Gross reductionists, first of all, do not believe any interiors exist anywhere" — line 1841.
- "not … the main story": line 1853 above, and "Gross reductionism still rears its peculiar head every now and then" (same line).
- Subtle grid's sub-head "the Left half collapsed to its correlates on the Right half": line 1863 above; also "they reduce everything on the Left half of the diagram to a corresponding reality on the Right half" — line 1845.
- "I reduced to It", "We reduced to Its": ""I" and "we" were reduced to holistic "its"—the precise essence of subtle reductionism" — line 1865; "interwoven "I" and "we" reduced to interwoven "its"" — line 1871.
- "thoughts as brain states": "I can *always* maintain that thoughts are just brain states" — line 1933; "This position is not yet gross reductionism. It is subtle reductionism." — line 1935.
- "culture as social integration": "*Cultural meaning* (LL) is reduced to *social integration* (LR), yet another version of functional fit." — line 1999.
- "the web is kept whole and every within is gone": "orders that now had no within, no interiors, no qualitative distinctions" — line 1863; "They claim to embrace the whole of reality, when in fact they have just devastated half of it." — line 1847; "a Right-Hand holism, a flatland holism" — line 1851.
- "every interior has an exterior correlate, which is what makes both reductions tempting": "Precisely because there *are* correlations between all four quadrants, this type of reductionism can be aggressively carried out. This is what makes subtle reductionism so hard to spot and so hard to redress." — line 1877; "since every event in the Kosmos does indeed have a Right-Hand component, it can mistakenly appear that the Right-Hand path alone exhausts the Kosmos" — line 1945.
- Title's "flatten": "*interiors* tended to get lost and flattened into mere *exteriors*" — line 1865; "flatland atomists" and "flatland holists" — line 1845.
- Subtitle's "the second built flatland": "this subtle reductionism was the *fundamental Enlightenment paradigm*" — line 1951; ch. 12, "What *was* denied was that the *Left-Hand dimensions* needed to be explained in any terms *other* than those found in the *Right Hand*. This is subtle reductionism." — line 4869; "the Left reduced to its correlates in the Right" — line 4825.
- Window glosses (a meaning, a brain state, a shared language, a social system) condense the quotations in the previous figure's windows, lines 1879–1923.
- Concept pages: `concepts/flatland.md`, `concepts/four-quadrants.md`, `concepts/big-three.md`.

## Faithfulness

Wilber's: the two reductionisms and their names; gross reductionism's two moves (all quadrants to the Upper Right, then the Upper Right to atoms) and subtle reductionism's one (the Left half to its correlates on the Right half; "I" and "we" to "its"); the quadrant grid, its pronouns and aspects, from the previous figure; "atoms" and "the great interlocking web" as what each reduction leaves; the examples behind the arrow labels (thoughts as brain states; cultural meaning as social integration); both verdicts, including that gross reductionism is the historically minor one and subtle reductionism the Enlightenment's "great crime"; both lists of targets; every quotation on the canvas and the page.

Ours, marked ◇ on the canvas in one note ("The three grids, the dotted empties, the arrows and the web drawing are this wiki's; the two reductionisms, their moves, their verdicts and their targets are Wilber's"): the title; the three-grid layout, the Kosmos beside its two flattenings; the dotted empty windows as the mark of what a reduction removed (the language's "absence" pattern, as in the holarchy figure); the arrows, whose directions follow his sentences ("to the Upper-Right quadrant", "the Left half to its correlates on the Right half") but whose drawing is ours; the atom dots and the web of nodes; the madder tint on the windows everything was emptied into (the pre/trans figure's "bin"); the sans summary lines and the window glosses; the ghost flights and the step order. The footer says "◇ marks this wiki's own device" and "The quadrant frame follows "One thought, four windows"".

A caution on the subtle arrows. Wilber describes the subtle collapse at two grains: as Left to its Right-Hand correlates (Upper Left to Upper Right, "thoughts are just brain states"; Lower Left to Lower Right, "cultural meaning (LL) is reduced to social integration (LR)"), and, more loosely, as everything "reduced to the Lower-Right quadrant of functional fit" (line 1957). The two arrows draw the first; the single web over both exterior windows, with the divider between them kept, is meant to carry the second: the brain state and the social system become strands in one system. The web does not erase the individual/collective line, because he says subtle reductionism "*still recognizes holarchy*" on the Right Hand (line 1937).

Not shown on purpose: the Big Three → Big One version of the same argument (a possible separate figure, gallery 02); the Ego and Eco camps of ch. 12, both of which he places inside flatland; Habermas's "colonization of the lifeworld" and Foucault's biopower, his witnesses against systems theory (line 1849; on the page's sources only); the reduction of truth itself to functional fit (line 1929); the "footprints of the giant" image (line 1945). One distinction, two collapses.

No published figure was reproduced; the footer says "Redrawn from Wilber's account". The 2 × 2 is the concept itself and is common to every drawing of it.

## How it would integrate into the site

See `docs/figure-design.md`, "Embedding in Flowershow". Where: `concepts/flatland.md` (animated, best fit; the page currently has no figure) and as a second figure on `concepts/four-quadrants.md` below the first, or linked from it. The OG crop is the candidate `og:image` for the flatland page. The HTML table on the page is the text alternative and should travel with the figure. Add `subtle-reductionism` to `PIECES` in `scripts/sync-visuals.py` and `export.py` when it ships (both shared files, not touched here).

## Checks done

Every string above grepped against `library/1995-sex-ecology-spirituality-full-text.md` (all matched). Rendered in headless Chrome at 1100 px and 390 px: no horizontal overflow, no console errors. Mid-animation frames captured at every step; reduced motion: Play jumps to step 5; JavaScript off: the settled frame renders with only the settled caption and every `data-until` element at opacity 0. Exports regenerated with `export.py`. Not run: `contrast.py` (no colour token changed) and `verify_quotes.py` (it checks `concepts/`, `people/` and `works/` pages, none edited).

## Open question for Rufus

The subtle grid's exterior half: the brain-state trace and the social-system network are shown there only mid-animation (step 3), and the settled frame shows the web alone with "It" and "Its". A version that kept the two small drawings inside the web was tried first and was cluttered at this cell size. Is the web alone enough to say "the exteriors are kept, only woven into one system"?
