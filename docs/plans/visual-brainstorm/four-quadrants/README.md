# One thought, four windows

Option 01 from the [visual brainstorm gallery](../gallery.html#o1), built on 2026-10-26 in the shared design language ([`docs/figure-design.md`](../../../figure-design.md)). Bead `wilberwiki-clq`. Review candidate only: nothing here is on the site.

## What it is

The four quadrants, but filled with Wilber's own worked example instead of abstract labels. One SVG source, two outputs. The static image is a 1200 × 800 canvas: title block; two distinctions across the top and down the side (INTERIOR / EXTERIOR, INDIVIDUAL / COLLECTIVE); four framed "windows" with a single thought sitting at the crossing; in each window, the pronoun Wilber gives that quadrant (I, It, We, Its), its SES name and aspect, a verbatim sentence saying what the thought *is* from there, a small drawing of how it appears there (a thought bubble; a trace of beta waves; two speech bubbles; a small network of structures), a sans "how you find out" line (ask / look / share a language / survey the system), and the validity claim that belongs to that window (truthfulness / truth / justness / functional fit, each with Wilber's own gloss: can the mapmaker be trusted, does the map match the territory, can we come to mutual understanding, what does it do). Interior windows are tinted, exterior windows neutral. Below the grid, a ◇ note, two verbatim passages from SES ch. 4 with locators, the footer and the signature.

The animation settles on exactly that frame, in the order Wilber tours the quadrants in the book: (0) the two distinctions, four empty windows and the thought; (1) Upper Right: a ghost of the thought flies into the window and becomes the beta-wave trace, and the window's text fades in; (2) Upper Left, the same with the thought bubble; (3) Lower Left, the speech bubbles; (4) Lower Right, the network; (5) the note, passages and footer. Five steps at 1500 ms, under eight seconds. The thought at the centre never moves; only copies fly.

Files: `source.svg` (the drawing, authored in its settled state), `page.html` (the page template), and the generated outputs `index.html`, `four-quadrants.svg`, `four-quadrants.png` (2400 × 1600), `four-quadrants-og.png` (1200 × 630, the top of the canvas: title and grid, no passages), `four-quadrants-square.png` (1080 × 1080, letterboxed). Regenerate with `python3 ../design-language/export.py four-quadrants`. The slug is not yet in `export.py`'s `PIECES` list (shared file, left alone); passing it as an argument works.

## Sources

All quoted text is verbatim from `library/1995-sex-ecology-spirituality-full-text.md` (revised second edition text), ch. 4 "A View from Within", section "A tour of the four quadrants". Line numbers are for that file. Italics inside quotations are Wilber's.

- "I have a thought; a thought occurs to me." — line 1879. Subtitle.
- "there was a release of norepinephrine between the neural synapses in the frontal cortex, accompanied by high-amplitude beta waves" — line 1879. Upper Right window.
- "even if you know what every single atom of my brain is doing, you will never know the actual details of my thought *unless I tell you*" — line 1881. Upper Left window.
- "If I want to know what your brain looks like *from within*, what its actual lived *interior* is like (in other words, your *mind*), then *I must talk to you*. There is absolutely no other way." — line 1885. Passage, bottom right.
- "If I tell them to you and you don't speak the language, then you won't get the meaning" — line 1913. Lower Left window. The same sentence continues "That is the Lower-Left quadrant, the *shared cultural worldspace*…", the source of "shared worldspace" in the Lower Left how-line.
- "cultural meanings have correlates in objective social institutions and material social structures" — line 1923. Lower Right window. The examples in its how-line (written records, buildings, technology) are from the list that follows in the same paragraph ("written records, school buildings, … types of technology").
- "my "single" thought, the original holon, is not really a single thought as such, but rather a holon with four inseparable aspects (intentional, behavioral, cultural, and social), each with its own validity claims" — line 1931. Passage, bottom left. The inner double quotation marks are set as single quotes on the canvas because they sit inside the outer pair; the words are unchanged. The four aspect names in the window headers come from this sentence.
- Validity claims and their glosses: "matching map and territory accurately enough" (truth, line 1903); "whether the mapmaker can be trusted" (truthfulness, line 1905); "whether you and I can come to *mutual understanding*" (justness, line 1919); "*Functional fit* ("What does it *do*?")" (line 1927). The four claims are listed together at line 1931.
- How-you-find-out lines paraphrase: "I just look" and "I look at a social system with empirical data and statistics" and "It can all be done in a monologue; it never needs a dialogue" (all line 1889); "I must talk to you" (line 1885); "mutual understanding" (line 1919).
- Column glosses: "what they look like from the outside; and the left half represents the interiors—what they look like from within" — line 1767.
- Pronouns: I / we / it are the Big Three throughout SES (`concepts/big-three.md`); "interrelated I and we to interrelated its" — line 1935.
- Concept page: `concepts/four-quadrants.md`.

## Faithfulness

Wilber's: the two distinctions and the four quadrants with their names; the thought as the example holon, and the order it is toured in (Upper Right first, then Upper Left, Lower Left, Lower Right); every quotation in the windows and below; the four aspect names; the four validity claims and the map/mapmaker contrast; I, we, it, its as the pronouns; the Lower Right example list.

Ours, marked ◇ on the canvas in one note: the "window" framing and title; the layout (four framed windows with the thought at the crossing, interior windows tinted, the right column mirrored so each window faces the thought); the four small drawings of how the thought appears from each window; the sans how-you-find-out lines, which paraphrase his sentences; the ghost flights in the animation. The footer says "◇ marks this wiki's own device".

Not shown on purpose: the developmental sequences Wilber lists inside each quadrant in his own figure 4-3 (the published figure; this piece shows one holon instead, which is also what keeps it from being a tracing); the eight zones of *Integral Spirituality* (the gallery sketch proposed them as a second state; they would be a separate figure); subtle reductionism and flatland, the reason Wilber gives the example at all, which are on the page's text alternative and on the concept page but not on the canvas, to keep the canvas to the four windows.

No published figure was reproduced. The figure's structure (a 2 × 2 of interior/exterior × individual/collective) is the concept itself and is common to every drawing of it.

## Colour: one proposed addition to the shared language

Interior windows are tinted with a hue the language does not yet have: an `interior` role (the within, the Left-Hand, consciousness and culture), value `#6b21a8` with fill `rgba(107, 33, 168, 0.10)`. None of the four existing roles fits (level, state, fallacy, ground all mark things absent from this figure), and the rule is that a hue appears only for a thing that is in the figure. For now `source.svg` carries the two values inline on the two interior rects, with a comment; if the role is accepted, add `--wv-interior` / `--wv-interior-fill` to the `@tokens` block of `visuals.css` and `c-interior` / `s-interior` / `f-interior` classes to the SVG vocabulary, then replace the inline attributes with `f-interior s-interior`. Exterior windows use the existing neutral fill ("surfaces", in Wilber's word). The ink-only alternative (interiors shaded with the neutral fill, exteriors on the lighter surface) was considered and would also be within the language, at the cost of a flatter image.

## How it would integrate into the site

See `docs/figure-design.md`, "Embedding in Flowershow". Where: `concepts/four-quadrants.md` (animated, best fit) and `index.md` (static, as the site's lead image, per `../RECOMMENDATION.md`). The OG crop is the candidate `og:image` for the concept page (`wilberwiki-4qc`, pending). The HTML table on the page is the text alternative and should travel with the figure. Add `four-quadrants` to `PIECES` in `scripts/sync-visuals.py` and `export.py` when it ships.

## Open questions for Rufus

1. The four small drawings (thought bubble, beta-wave trace, speech bubbles, network): are they the diagrammatic content that makes the grid worth looking at, or do they tip it towards clip art? The text layout does not depend on them.
2. The `interior` colour role above: accept as a shared token, or keep interiors in the neutral shade?
3. Should subtle reductionism go on the canvas (a madder arrow from the left windows to the right, "the thought is just a brain state")? It is the point Wilber builds the example for, but it would add a second idea to a figure whose job is to make the four windows click for a newcomer.
4. The Lower Right drawing is a generic network; a row of small buildings would be more literal ("school buildings") but busier.

## A note on the concept page

While sourcing, one quotation on `concepts/four-quadrants.md` did not match the full text: "No holon simply exists in one of the four quadrants; each holon has four quadrants." The sentence in the book (line 1931) is "no holon whatsoever simply exists in one or another quadrant; all holons *possess* these four quadrants". Not changed here (`concepts/` was out of scope for this piece); worth a `verify_quotes.py` run on that page.

## Decisions (2026-10-26, Rufus)

Keep the four small drawings. Accept the interior colour role (now `--wv-interior` tokens and `c-/s-/f-interior` classes in `visuals.css`). Leave subtle reductionism off this figure; it's a candidate for its own figure.
