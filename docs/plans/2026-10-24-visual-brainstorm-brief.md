# Visual brainstorm: posters and images of Wilber's work

Date: 2026-10-24. Bead: `wilberwiki-clq`. Related: `wilberwiki-at6.4` (works concept-lineage visualization), `wilberwiki-uze` (network map), `wilberwiki-4qc` (social-share images).

## Why this brief exists

The planned works visualization (`wilberwiki-at6.4`) is one narrow idea, a sourced concept-lineage graph across books. It is gated behind a long research chain (`.4.2`–`.4.4`) before any prototype, and Rufus isn't sure the idea works at all. This brief opens the visual work up to broader brainstorming: what posters, diagrams and images would help a reader *get* Wilber, or would make someone want to share the site?

It does not cancel `at6.4`. If a lineage view comes out of this as a strong option, it goes back into that track with its research gates intact.

## Goal

1. **Options gallery (checkpoint for Rufus).** 8–12 distinct directions, each shown as a rough but real visual sketch (SVG or HTML, not just words), with: what it shows, who it's for, what source material it rests on, how faithful it is to Wilber, effort, and risks. Rufus reviews this later; nothing goes live from it.
2. **One or two directions taken further.** Pick the strongest 1–2 and build them to a polished, standalone state (HTML + inline SVG, JS only where interaction really earns it; a static SVG/PNG export where useful). These are still review candidates, not site changes.

## Audience and use

- A curious reader landing on wilber.wiki who knows little about Wilber: does the image make one idea click?
- Someone sharing the site: is there an image worth posting (and usable as an Open Graph card, `wilberwiki-4qc`)?
- Rufus and collaborators teaching Wilber: a poster you could put on a wall or a slide.

## Directions to consider (seed list, not a constraint)

- **Four quadrants** (I, We, It, Its) as a poster, with examples filled in from `concepts/four-quadrants.md`.
- **Holarchy / holons:** nested wholes and parts; the twenty tenets as a visual.
- **Great Nest of Being / spectrum of consciousness:** concentric spheres, matter → body → mind → soul → spirit.
- **Waves and streams / integral psychograph:** lines of development rising through levels to different heights (`concepts/integral-psychograph.md`, the IP charts in `charts/`).
- **Pre/trans fallacy:** the two failure modes (reductionism vs elevationism) as a single diagram.
- **Flatland:** the collapse of the left-hand quadrants into the right-hand ones.
- **Big Three:** art / morals / science; the I / We / It.
- **Involution and evolution / Eros and Agape:** the arcs of descent and ascent.
- **Wilber I–V timeline:** phases, books and the ideas each introduced (`works/phases.md`, `works/catalog.md`).
- **Interlocutor constellation:** the people Wilber engages with, placed by tradition or quadrant (`people/`).
- **Concept map:** the wiki's own link graph, curated (`wilberwiki-uze`).
- **Correlation charts reimagined:** the IP appendix tables (`charts/`) as one grand visual.
- **Social card system:** a consistent visual identity for share images.
- Anything else that's better than the above.

## Constraints

- **Faithful to Wilber.** Every visual must rest on something in the repo: concept pages, `charts/`, `works/`, or the full texts in `library/`. Name the source per option. Don't invent structure Wilber doesn't propose; if an option is an interpretation rather than Wilber's own diagram, say so on its face.
- **No verbatim reproduction of Wilber's published figures as images.** Redrawing a concept (quadrants are a grid; that's fine) is OK; tracing a specific book figure is not. Any quoted text in a visual must be verbatim from `library/` (check with `skills/add-excerpt-page/scripts/verify_quotes.py` conventions, or keep text to labels and paraphrase marked as such).
- **Honest uncertainty.** Lines between things must not imply influence or derivation unless sourced (lesson from the `at6.4` review).
- **Works on the site eventually.** Flowershow renders markdown with raw HTML; custom CSS/JS can be loaded via `config.json` `head` (see `assets/roadmap/`, `assets/annotator/`). Prefer self-contained SVG that looks good in light and dark, works on a phone, and has a text alternative.
- **Location.** Work in `docs/plans/visual-brainstorm/` (excluded from production). Do not edit site content pages, `config.json`, or publish anything.

## Deliverables

- `docs/plans/visual-brainstorm/gallery.html` — the options gallery, self-contained (inline SVG sketches, no external deps beyond Google Fonts / cdnjs if needed).
- `docs/plans/visual-brainstorm/<option-slug>/` — the 1–2 polished builds, each with a short `README.md` (what it is, sources, how it would be integrated into the site, open questions).
- A short recommendation: which 1–2 to put on the site and where, and whether `at6.4` should continue, change shape, or be parked.

## Decision gate

Rufus picks what (if anything) goes on the site. Silence is not approval.

## Origin

Rufus asked on 2026-10-24, after a backlog review, whether a Fable sub-agent could do "some cool visualizations". He wasn't sure the planned `at6.4` visualization really works, so he wanted the visual work opened up to "more open brainstorming of cool posters or images to visualize wilbers work and concepts". The first output was to be an artifact of options and directions for him to review later as a checkpoint, with the best 1–2 optionally built out as HTML + SVG + JS or as static images.

## Status log

### 2026-10-24: options gallery delivered (checkpoint)

- A Fable sub-agent ran on this brief. Output is in [`visual-brainstorm/`](visual-brainstorm/): [`gallery.html`](visual-brainstorm/gallery.html) (12 directions), two polished builds ([`pre-trans-fallacy/`](visual-brainstorm/pre-trans-fallacy/), a static poster, and [`states-and-stages/`](visual-brainstorm/states-and-stages/), an animated before/after showing the IP ladder becoming the IS stage-by-state grid), and [`RECOMMENDATION.md`](visual-brainstorm/RECOMMENDATION.md).
- Review artifact (private, gallery plus both builds): https://claude.ai/artifact/BSjNzQ7gxxCnbaGFBhti4r
- Verification: the lead session grepped every quotation in the gallery and builds against `library/*-full-text.md` and all matched verbatim, apart from italic markup. The sub-agent checked rendering at 1280px and 390px in light and dark mode.
- Ranked picks: (1) pre/trans fallacy poster, (2) states off the ladder, (3) four quadrants with one concrete example, (4) "pull a rung out" holarchy explorable, (5) Wilber I–V timeline. Site placements are in `RECOMMENDATION.md`.
- On `at6.4`, the recommendation is to change its shape. Replace the graph of lineage edges, where every edge is a historical claim needing research, with one before/after diptych per Wilber-named transition (I→II … IV→V), with the passages beside each diptych and no derivation arrows. Keep the ledger, validator, date-basis discipline and the decision gate. IV→V is effectively done by the states-and-stages build. The lead session agrees.

### 2026-10-25: Rufus's response

- Rufus said "this is *amazing*", loves all the options, and thinks some can be animated. He wants each piece to be both a static image that is easy to share on the web and an animation on a site page where that fits.
- Next: do a first one or two pieces, with the main work being a good shared **design language** for the whole series, then see how they look.
- Approach agreed: design language first, proven on the two existing builds, rather than detailed per-piece plans written before any shared visual style exists. Plans for the remaining directions come after Rufus approves the language.

### 2026-10-25: design language pass (in progress)

Scope for the Fable sub-agent:

- A design-language spec covering type, palette (light and dark), line weights and stroke vocabulary, label vs verbatim quotation vs marked interpretation, source attribution, animation timing and easing, and share-card crops. It comes with a shared stylesheet and reusable SVG building blocks.
- Every piece is **one SVG source with two outputs**: a static, shareable image (a key or final frame, exported as SVG and PNG, plus a 1200×630 Open Graph crop) and an animated version for its page. The animation's settled state must equal the static image.
- Rebuild the pre/trans poster (adding an animation) and states off the ladder (adding a static diptych) in the new language.
- Present the spec and both pieces in one review artifact. Nothing goes on the site.
- Delivered 2026-10-26: [`visual-brainstorm/design-language/`](visual-brainstorm/design-language/) (spec `README.md`, `visuals.css`, `wv-motion.js`, `export.py`, `contrast.py`, review page `index.html`). Both pieces were rebuilt as `source.svg` + `page.html`, from which `export.py` generates the animated page, a standalone SVG, a PNG, a 1200×630 OG crop and a square crop.
- Review artifact (private): https://claude.ai/artifact/1xYfJAtaZqo1TEPiYAA9a1
- Key decisions for Rufus: serif for Wilber's voice and sans for the wiki's; four semantic colours (structure, state, fallacy, ground); a 1200×800 series canvas so the OG crop keeps the title and figure; the static frame is the source and animation only hides earlier steps; solid lines for Wilber's structure, dashed for relations we draw, dotted for absence or unverified, and arrows only where the text gives a direction; a ◇ mark for our interpretations.
- Open questions: the six listed in `design-language/README.md`. The lead session noticed two nits: "formless sleep" overflows its header box in states-and-stages, and in the pre/trans figure each fallacy label sits at the tail of its arrow, next to the other arrow's head.
- New quotes were re-grepped in `library/`: IS l.1206, SES l.8925, IP l.491. All match.

### 2026-10-26: Rufus's review of the design language: not beautiful yet

- Rufus: "this is not at all beautiful yet ... elegance and beauty matters here." He pointed to the Seeds of Renaissance diagram system for inspiration: https://design.seedsofrenaissance.org/diagrams (source: https://raw.githubusercontent.com/life-itself/design/refs/heads/main/projects/sor-design-system/diagrams.md).
- What the reference does that ours didn't: it follows the FT, the Economist and Tufte in putting restraint over decoration. It uses one typeface, Apfel Grotezk, with no bold, so hierarchy comes from size alone. Groups are panels in a pale tint with no outlines. Full colour is kept for the one mark the figure is about. Lines are solid ink with solid arrowheads, there are no legends, and labels sit on the things they name. A title sits top left with a grey subtitle beneath, and the signature bottom right. There is a lot of white space, and every figure must read at 400px and in black and white. Ours had outlined rounded boxes, four colours, two typefaces, dashed and dotted lines, and crowded labels.
- Next pass: a fresh Fable agent rebuilds the design language from this grammar and redraws both pieces. The content and faithfulness work in the existing READMEs and `source.svg` files is kept. Decided by default, and open to change: borrow SoR's diagram grammar, but give the figures a wilber.wiki identity and signature rather than SoR branding. The agent will show the accent colour both as SoR red and as one alternative.

### 2026-10-26: rebuilt on the SoR grammar (checkpoint)

- Rufus settled the direction during the pass: follow SoR's typography and drawing rules as written (Apfel Grotezk, no bold; the type scale, adjustable; line weights, panels, arrowheads, layout, exports, the 400 px and black-and-white checks), with wilber.wiki's own colour and accent, and a signature of the SoR mark plus "WILBER WIKI · SEEDS OF RENAISSANCE" (and wilber.wiki). SoR is credited with a link.
- The durable spec is now [`docs/figure-design.md`](../figure-design.md). [`visual-brainstorm/design-language/`](visual-brainstorm/design-language/) holds the tooling (`wv.py`, the outlined-text exporter; `wv.css` and `wv-motion.js`, the page layer; the fonts and mark) and the review page [`index.html`](visual-brainstorm/design-language/index.html). Both pieces were redrawn from scratch as `figure.py` files: [`pre-trans-fallacy/`](visual-brainstorm/pre-trans-fallacy/) (three tiers, two arrows) and [`states-and-stages/`](visual-brainstorm/states-and-stages/) (a ladder, one arrow, an open lattice). Each has a static SVG and PNG, @2x, a 1200 × 630 OG card, a night render, an SoR-red comparison render, and an animated page that settles on the static frame.
- Palette chosen: rust accent `#b5451b` with a cream tint `#f8e8d6` (night `#f09a52` / `#5a2a14`), ink and chalk as SoR. SoR red is rendered beside it for each piece so the choice can be made by eye.
- Quotes on the pages were re-grepped against `library/`: SES l. 2551, 2553, 2557, 2561, 8925; IP l. 491; IS l. 1206, 1208, 1214, 1216. Nothing on a canvas is set as a quotation.
- Open questions are listed on the review page and in each piece's README (accent; quotations off the canvas; the open rational tier; the empty lattice; rung names; signature length; motion).
- Correction from Rufus, same day: the project is associated with Seeds of Renaissance, so the figures should **reuse and credit the SoR system** as is (Apfel Grotezk, SoR red, the SoR signature with "wilber.wiki" in the slot) rather than only borrowing its grammar. Our `design-language/` covers only the Wilber-specific conventions on top of SoR and links to https://design.seedsofrenaissance.org/diagrams for everything else.
- Clarified again by Rufus, superseding the correction above: SoR was an example of the beauty and elegance wanted, not a brand to adopt. The Wilber figures may have their own colours, accent and other features, and are signed wilber.wiki. They reuse SoR's grammar and tooling where it helps, and credit the SoR design system as source and inspiration in the design-language docs.
- Final settled position: follow SoR's typography and drawing rules (Apfel Grotezk, no bold, its type scale, line weights, panels, layout and signature position, exports, and the 400px and black-and-white checks). Colour and accent may differ for wilber.wiki. The signature reads wilber.wiki, and SoR is credited.
- Refined by Rufus: figures are signed with the SoR logo mark plus "WILBER WIKI · SEEDS OF RENAISSANCE" (or similar), bottom right. The type scale may vary from SoR's where it helps.
- Review artifact for this pass (private): https://claude.ai/artifact/STTg5kwma33B9hXionsBoE. The durable spec is now [`docs/figure-design.md`](../figure-design.md), and `CLAUDE.md` points to it.

### 2026-10-26: back to the earlier design language

- Rufus, after seeing the SoR-based redesign: "personally i think the old diagrams were often diagrammatically much better ... Now i see it i think old approach was better. so just go with it". He also said that curved arrows are fine (SoR only happened to use straight ones), that dark-mode versions are not needed, and that fonts and colours are easy to change at the end.
- Lesson: "more beauty" was a request to polish, not to restyle. The restrained redesign was clean but cut the diagrammatic content (the "untutored eye" bins, the flying states, the on-canvas quotation), and that content is what made the earlier pieces engaging. Next time, polish the existing pieces before replacing their structure.
- Action: `visual-brainstorm/` was restored to commit `a64fe8e`. The SoR-based attempt stays in git history at `822a1d3`. Next: fix the earlier nits, drop the dark-mode requirement, add the SoR mark and "WILBER WIKI · SEEDS OF RENAISSANCE" signature, and rewrite `docs/figure-design.md` to describe this language.
- Polish pass done, 2026-10-26:
  - fixed the overflow and the label placement
  - light only
  - curved arrows allowed
  - SoR mark plus "WILBER WIKI · SEEDS OF RENAISSANCE · wilber.wiki" signature on each figure
  - `docs/figure-design.md` rewritten to describe this language, with both lessons

  Review artifact (updated in place): https://claude.ai/artifact/1xYfJAtaZqo1TEPiYAA9a1. Held back, for Rufus to decide: dropping the 24 "stage × state" cell labels, and shortening the ◇ note on the states canvas.
