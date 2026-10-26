# Wilber I–V: the books on a line

Option 08 from the [visual brainstorm gallery](../gallery.html#o8), built on 2026-10-26 in the shared [design language](../design-language/README.md) (spec: [`docs/figure-design.md`](../../../figure-design.md)). Bead `wilberwiki-clq`; recommendation item 5. Review candidate only: nothing here is on the site. Intended home: `works/phases.md` and `/visuals`.

## What it is

One SVG source, two outputs. The static image is a 1200 × 800 **shelf**: a horizontal time axis from 1977 to 2024, to scale (21 units a year), on which every entry in `works/catalog.md` stands as a book spine at its year of first publication, title running up the spine with the year after it. Five soft bands above the axis mark the periods of Wilber I–V as `works/phases.md` dates them, each headed by its numeral, the wiki's short name and the page's period ("late 1970s", "around 1980–82", "1980s", "mid-1990s–2000", "early 2000s onward"); band V fades out to the right because it is open-ended. Because the axis is to scale, the shape of the catalog is visible at a glance: the crowded shelf from 1995 to 2008, the empty stretch from 1987 to 1994 with only a co-edited collection and the memoir *Grace and Grit* on it, the empty stretch 2009–13, the late cluster of thin titles around 2014–18. Under the gap, bracketed, Wilber's own sentence about SES: "the first theoretical book I had written in almost ten years". Inside band V, a dotted spine stands for the unpublished second volume of the Kosmos trilogy, placed where Wilber said it would be ready. Below the shelf, a key gives Wilber's own one-clause description of each of phases 1–4, verbatim from *Integral Psychology*, and a ◇ note that phase V is not in his list.

There are no lines or arrows between books. The figure shows when, not what came from what (the lesson of the works-lineage review and the reason `wilberwiki-at6.4` was reshaped).

The animation builds the shelf phase by phase and settles on exactly that frame (N = 6, 1400 ms a step, about 8.4 s): (0) the empty shelf: title, axis, decade ticks; (1) band I rises with its header, *The Spectrum of Consciousness* and *No Boundary* stand up, and the key's heading and column I appear; (2) band II, *The Atman Project*, *Up from Eden*, the 1982 anthology; (3) band III, *A Sociable God*, *Eye to Eye*, *Quantum Questions*, *Transformations of Consciousness*; (4) the gap: *Spiritual Choices* and *Grace and Grit* stand up alone, the bracket and Wilber's "almost ten years" sentence appear, then band IV with SES, *A Brief History of Everything*, *The Eye of Spirit*, the two 1998 titles, *One Taste*, *A Theory of Everything*, *Integral Psychology*; (5) band V and everything from *Boomeritis* to *Finding Radical Wholeness*, with the dotted Kosmos vol. 2; (6) the ◇ note, the footer and the signature. Spines rise 28 units into place with a 90 ms stagger (`wv-move`); bands, headers and key columns fade (`wv-fade`). Nothing exists mid-animation that is absent from the settled frame, so no `data-from`/`data-until` is needed.

Files: `source.svg`, `page.html`, and the generated `index.html`, `wilber-phases.svg`, `wilber-phases.png` (2400 × 1600), `wilber-phases-og.png` (1200 × 630), `wilber-phases-square.png` (1080 × 1080). Regenerate with `python3 ../design-language/export.py wilber-phases` (the slug is passed explicitly; it is not yet in `PIECES`, see "Integration").

## The selection rule

Every entry in the catalog is on the shelf (33 entries, 31 distinct works plus two retitled editions). What differs is weight, and the weights are the wiki's existing editorial decisions, not new ones:

- **Filled spine, title on it:** the twelve books whose page carries `core: true` (the ★ selection in the catalog): *Spectrum*, *Grace and Grit*, SES, *A Brief History of Everything*, *One Taste*, *A Theory of Everything*, *Integral Psychology*, *Boomeritis*, *Integral Spirituality*, *Integral Life Practice*, *The Religion of Tomorrow*, *Finding Radical Wholeness*.
- **Outlined spine, title on it:** the six other books `works/phases.md` names as representative of a phase: *No Boundary* (I), *The Atman Project* and *Up from Eden* (II), *A Sociable God*, *Eye to Eye* and *Transformations of Consciousness* (III). Without this tier bands I–III would hold almost nothing prominent, since the ★ selection cuts across theory, practice and personal writing rather than tracking the phases.
- **Thin tick, small label:** the other fifteen entries: edited anthologies and collections (*The Holographic Paradigm*, *Quantum Questions*, *Spiritual Choices*, *The Essential Ken Wilber*, *The Simple Feeling of Being*, *The Pocket Ken Wilber*), the co-authored *Wicked and Wise*, and the books outside the selection (*The Eye of Spirit*, *The Marriage of Sense and Soul*, *The Integral Vision*, *The Fourth Turning*, *Integral Meditation*, *Trump and a Post-Truth World*) and the two retitled editions. Labels carry the catalog's format tag ("ed.", "co-ed.", "anth.", "ebook", "co-auth.") where there is one.
- **Dotted:** anything the catalog is less sure of or that is not a new work: *The Holographic Paradigm* (catalog status `draft`: "some publication details or the description still need verification"), *Integral Buddhism* (2018, "previously *The Fourth Turning*"), *A Post-Truth World* (2024, "retitled second edition of the 2017 Trump book"), and Kosmos vol. 2 (never published). Dotted is the language's mark for absence or uncertainty.

The footer states the rule in one line; the page's text alternative lists every entry with its weight.

## Sources

Data, none from memory:

- `works/catalog.md`: every title, first-publication year, format, and the revised and retitled editions ("1995 (rev. 2001)" for SES, "1999 (rev. 2000)" for *One Taste*, both printed on the spine; the two retitled editions; the `draft` label on the 1982 anthology). *Eye to Eye* is dated 1983 (the catalog and its page: "First published by Anchor Books in 1983"), although its file is `works/1984-eye-to-eye.md`; the figure follows the record, not the filename.
- `works/<slug>.md` frontmatter: `core: true` on twelve pages (checked 2026-10-26 by grep).
- `works/phases.md`: the five phases, their periods, the books named for each, "Why the boundaries are approximate" (Helfrich dates by composition, Integral World by publication; *A Sociable God* is "near the II/III transition"; "a retitled edition does not create a new phase"), and "What happened to the Kosmos trilogy?".

Verbatim quotations, each grepped on 2026-10-26:

- `library/2000-integral-psychology-full-text.md`, line 2811 (chapter 9, note 15), the four phase clauses on the canvas, each cut at "…" after its first clause: "Phase-1 was Romantic (a “recaptured-goodness” model)", "Phase-2 was more specifically evolutionary or developmental (a “growth-to-goodness” model)", "Phase-3 added developmental lines to those developmental levels", "Phase-4 added the idea of the four quadrants"; the key's heading, "I have, for convenience, divided my overall work into four general phases."; and on the page, the whole note including "The present book is, of course, a phase-4 work." The double quotation marks inside the clauses become single on the canvas because they sit inside a quotation.
- `library/1995-sex-ecology-spirituality-full-text.md`, line 304 (preface to the revised edition): "the first theoretical book I had written in almost ten years", on the canvas under the gap; the page quotes the sentence and the next, which also say *Transformations* "was completed in 1984" (published 1986 per the catalog, which is where the spine stands) and "I wrote *Grace and Grit* in 1991".
- Same file, line 440 ("The Kosmos Trilogy"): "volume 2 would be ready around the year 2005", quoted in the ◇ note, and "Volume 2 is more or less fully written. Volume 3 exists in outline.", on the page; line 474, "This book is the first of three volumes", on the page.

## What is Wilber's and what is ours

Wilber's: the division of his work into four numbered phases and his one-sentence description of each (IP ch. 9 n. 15); that IP is a phase-4 work; the titles and years (bibliographic facts, via the catalog); the "almost ten years" sentence; the plan for volume 2 "around the year 2005" and its status.

Ours, marked ◇ on the canvas and in the footer: the shelf and the spines; the bands as periods with soft edges, dated from `works/phases.md` (which follows Wilber's retrospective and commentators; the page itself says the dates are approximate and that commentators differ); the short phase names, which are the phases page's, not Wilber's; **phase V itself**, which is not in Wilber's 2000 list and which the phases page attributes to later commentators (Akalin's publisher guide, Helfrich); the three weights, which are the wiki's editorial selection; placing the unpublished volume at 2005 on the strength of Wilber's stated plan. The ◇ note says in so many words that a book standing inside a band is not thereby a statement of that phase (*Boomeritis* is a novel; the anthologies collect earlier writing; memoirs and retitled editions carry no phase).

Not shown on purpose: any line or arrow between books; Kosmos volume 3 ("exists in outline", undated); the *Collected Works* volumes (the catalog says not to count them); the unpublished textbook *System, Self, and Structure* that IP abridges (line 304); commentators' alternative phase dates; the three-book reading route from `works/index.md` (SES → IP → IS, with *A Brief History* as the entrance), which would be a fourth encoding on an already full canvas and is better left to the page beside it.

No published figure was reproduced; the figure is drawn from the catalog's data.

## Honest uncertainty

- **Dates are first publication, as the catalog gives them.** Where the catalog notes a revision the spine says so ("1995 · rev. 2001"); where it notes a retitling the mark is dotted and the label says "retitled" or "2nd ed."; the one `draft` entry is dotted.
- **Horizontal nudges.** In crowded years spines cannot all stand exactly on their year, so they are packed by least squares (the smallest total displacement that keeps 2 units between neighbours). Most move under 0.4 of a year; the largest are *Integral Psychology* (+0.8 yr, because 1999–2000 hold three filled spines), *The Essential Ken Wilber* (−0.6) and *Eye to Eye* (+0.55, sharing 1983 with *A Sociable God*). The printed year is the date; the page says so.
- **Band edges** are the wiki's dates, feathered over 6 units so they do not read as boundaries; `phases.md` dates II as "around 1980–82" and III as "1980s", and the figure draws them abutting with a small gap at 1982.5, which is the figure's choice of where to break, not a date in the sources. *A Sociable God* (1983) stands at the start of band III, nudged left toward the break, which happens to match the page's "near the II/III transition" but is a packing artefact, not a drawn claim.
- **Kosmos vol. 2 at 2005** is Wilber's planned date, not a publication; the "excerpts only" on its label refers to the Kosmos II excerpts `phases.md` lists under phase V, which the page does not date and the figure does not either.
- *Transformations of Consciousness* was "completed in 1984" by Wilber's account (line 304) and published in 1986; the spine stands at 1986.

## Integration

See `docs/figure-design.md`, "Embedding in Flowershow". Where: `works/phases.md` above "The five phases at a glance" (the table is the figure's text alternative in prose), and `/visuals`. Shared changes needed, not made here: add `wilber-phases` to `PIECES` in `design-language/export.py` and in `scripts/sync-visuals.py`. The figure uses only existing classes and tokens; the band fills are `linearGradient`s of ink at the neutral-fill opacity (0.055) so the feathered edges need no new token.

## Open questions for Rufus

1. The figure is monochrome by design: no role in the colour table (level, state, fallacy, ground, interior) names a book or a phase, so nothing is tinted. If the shelf reads as too grey, the honest option is one accent for the twelve filled spines, but any of the existing hues would import a meaning (indigo says "level"). Say if you want colour and which meaning you would accept.
2. Three weights (filled, outlined, thin) or two? The outlined tier exists so bands I–III show their representative books; dropping it would leave *Spectrum* alone on the left.
3. Phase V's name and period are the wiki's; the key says so with a ◇. Alternative: head band V with "V" only and no name, which is stricter but leaves the OG crop without a word for the last twenty years.
4. The reading route (BHE as entrance; SES → IP → IS) is deliberately not on the canvas. It could be a small ◇ "start here" on *A Brief History* if the figure is to carry the works hub's advice too.
