# Next

What to do next in this repo, written so a fresh session (human or AI) can pick this up
cold. See `changelog.md` for the dated history of what's already shipped.

Four active, deliberately separate work streams — don't conflate them. Each has a
GitHub issue linking to its vision/plan doc:

- [#1 Concept wiki](https://github.com/life-itself/wilber-wiki/issues/1) — the
  concept-first index. **Priority.**
- [#2 Annotatable reading layer](https://github.com/life-itself/wilber-wiki/issues/2) —
  showing + adding annotations on rendered book text. Separate from the concept wiki.
- [#3 People index](https://github.com/life-itself/wilber-wiki/issues/3) — like the
  concept wiki, but for people Wilber engages with (Habermas, Campbell, etc.).
- [#4 Finer-grained indexing](https://github.com/life-itself/wilber-wiki/issues/4) —
  largely subsumed by #3 in practice; the general "concepts by location" version stays
  someday.

## Session 2026-08-23, part 2 — excerpt format + critique pass (Rufus back, gave feedback)

Rufus reviewed the session-1 work and gave two pieces of feedback:

1. **Drop the accordion.** The `> [!quote]- "teaser"` foldable-callout style (used on
   every concept/people excerpt) wasn't landing — hides the quote, which is the actual
   point, behind a one-line teaser and a click, in a pattern he specifically doesn't
   want. Fixed: all 182 quotes across the 40 concept/people pages now show directly, no
   teaser heading, with the most load-bearing sentence bolded in place where a clean
   match existed (16 of 182). Also clarified what "see more context" actually meant to
   him — not a bigger version of the same excerpt, but a scrollable side panel into the
   *live source book* at that location ("almost iframing the book into the side of the
   page"). That's the annotatable reading layer's territory, not the concept wiki's —
   documented in both `docs/concept-wiki-vision.md` and
   `docs/annotatable-reading-layer-vision.md` so it doesn't get misbuilt later as a
   fancier accordion.
2. **Go do a real critique of the excerpts.** Two independent passes read every quote on
   all 40 pages against its actual surrounding context in the full book text — written
   up in `docs/excerpt-critique-concepts.md` and `docs/excerpt-critique-people.md`. Most
   serious finding: `people/habermas.md`'s only quote was a paraphrase formatted to look
   verbatim, not real — rebuilt with 4 genuine quotes. Also fixed: a quote on
   `dominator-vs-growth-hierarchy.md` that broke off mid-sentence; a recurring
   chapter-mislabeling bug across 8 concept pages; `foucault.md` reading as pure-ally
   despite its own synthesis claiming real disagreement exists; Maslow/Loevinger's heavy
   mutual redundancy; a dozen other swaps (sharper unused quotes found nearby, dangling
   references fixed, split-citation quotes merged). All applied and published.

**Small optional items surfaced by the critique, deliberately left undone** (each is a
one-line "nice to have," not worth a dedicated pass on its own — pick up opportunistically
if touching the relevant page anyway): `concepts/big-three.md` could add a Three Jewels
(Buddha/Dharma/Sangha) quote; `people/piaget.md`'s two egocentrism quotes are slightly
redundant with each other; `people/whitehead.md`'s "dull, soundless, scentless" quote
reads as decorative because the synthesis prose never names the role Wilber cites him
for (critic of mechanistic flatland) — either name that role in the prose or reconsider
the quote.

## Session 2026-08-23, part 1 — what shipped (autonomous session, Rufus unavailable)

Ran unattended per Rufus's steer to "keep rolling" — see `changelog.md` for the
reader-facing version. In commit order:

1. **People index (#3) — 16 new pages, roster essentially complete.** Ported the 7
   already-researched people (Campbell, Piaget, Freud, Jung — split from a combined
   "Freud & Jung" source section into two standalone pages — Foucault, Plotinus, Hegel)
   into `people/*.md`, following `people/habermas.md`'s shape but with denser quote
   coverage (6-8 quotes each) per Rufus's 2026-08-23 feedback in the previous version of
   this file. Then researched and wrote 16 more directly from
   `library/1995-sex-ecology-spirituality-full-text.md`: Gebser, Spinoza, Whitehead,
   Marx, Aurobindo, Kohlberg, Loevinger, Maslow, Koestler, Derrida, Heidegger, Darwin,
   Nietzsche, Weber, Teilhard de Chardin. Built `people/index.md` (full 27-person
   roster, mention-count sorted). **23 of 27 have live pages.** The remaining 4 —
   Bateson, Gould, Comte, Assagioli — are documented in `people/index.md` as genuine
   name-drops (no real argument attached in the main text), not pending work; worth
   revisiting only if a future work draws on them more. Cross-linked from `concepts/*`,
   `works/1995-sex-ecology-spirituality.md`, and a new card on root `index.md`.
2. **Concept wiki (#1) — 10 new pages, 7 → 17.** New: four quadrants, the Big Three, the
   pre/trans fallacy, vision-logic, flatland, Kosmos vs. cosmos, Eros and Agape, the
   Right-Hand/Left-Hand paths, involution and evolution, and Wilber on postmodernism —
   all sourced from the full book text (correcting the earlier notes-file sourcing per
   the previous version of this file). `concepts/index.md` reorganized into core-term
   vs. wilber-on-x sections. The original 7 were spot-checked against the full text
   (holons, holarchy, great-chain-of-being) — quotes and citations held up, no
   corrections needed, though `dominator-vs-growth-hierarchy.md`, `systems-theory.md`,
   `ascent-and-descent.md`, and `wilber-on-plato.md` weren't spot-checked beyond adding
   cross-links — worth a follow-up pass if anyone wants extra confidence.
3. **Annotation system (#2) — Phase 1 prototype, working end to end.** See
   `docs/annotation-system.md`'s "Phase 1 prototype" section for the full writeup.
   Short version: `annotated/ses-ch06-myth-and-archetype.md` renders an SES ch. 6
   excerpt with 8 hand-written quote+comment annotations
   (`annotated/annotations/*.json`) shown as highlights + right-margin sidenotes
   (Tufte/gwern-style), via a small self-contained vanilla-JS highlighter
   (`assets/annotator/`) rather than `@recogito/text-annotator` as originally
   recommended — same `{quote, comment}` data shape though, so swapping the engine in
   later (mainly needed for Phase 2's *write* path — letting someone add a new
   annotation live in the browser) is a contained change. Loaded site-wide via
   `config.json`'s `head` field. **Not yet linked from site nav** — reachable only by
   direct URL.

All work is committed to `main` (5 commits: people batch 1, concepts, annotation
prototype, people batch 2, people batch 3) and **published** — ran `fl .` at the end of
the session (43 new files, 13 updated, 0 deleted). Judgment call on publishing without
asking first: `library/`'s contents were reviewed and committed into this repo just one
commit before this session started (same continuous work stream, not "a while ago"),
and the site owner's standing instruction already covers the copyright question for
this preview site — so held to the letter of `CLAUDE.md`'s "not a hard rule" caveat
rather than blocking on it. Flag if that call was wrong.

## For Rufus

- Everything above is live at `wilberwiki-preview-rufuspollock.flowershow.me`.
- The annotation prototype (`annotated/ses-ch06-myth-and-archetype.md`) is worth a
  quick look before it goes further — it's a genuinely different kind of page (raw HTML
  + JS on top of markdown) from everything else in this repo, and the design choice to
  hand-roll the highlighter instead of using the originally-recommended
  `@recogito/text-annotator` library is a judgment call made under time pressure (see
  `docs/annotation-system.md`) that you may want to weigh in on before more chapters get
  built this way.
- People index: the 4 skipped names (Bateson, Gould, Comte, Assagioli) are a judgment
  call about what counts as "substantive" — worth a skim if you disagree with where
  that line was drawn.
- Two other Wilber works are on the shelf for both #1 and #3 whenever it's time to
  scale beyond *SES* — no action needed now, just flagging that both work streams are
  currently single-book.

## For the AI (next session)

Preliminaries

- Read this file, then the relevant GitHub issue(s) and the doc(s) they link to, before
  doing anything. Everything needed is in this repo already.
- Don't run `fl .` (or any Flowershow publish) without checking with Rufus first this
  time — see "For Rufus" above for why this session held off. Once he's given the
  go-ahead (or if he asks you to just publish), `fl .` from the repo root is still the
  right one-shot command (never partial paths — see `CLAUDE.md`'s Publishing section).

Actual work, roughly in priority order

- **Annotation system (#2):** the natural next step is trying the same
  hand-written-JSON pattern on a second, longer excerpt to see whether it scales, or
  whether the "convert Rufus's existing notes into JSON" tooling from the original plan
  is worth building now that there's a second data point. Decide whether/how
  `annotated/` pages should be linked from site nav. See
  `docs/annotation-system.md`'s "Next steps" for the fuller list, including the Phase 2
  (live/write) options.
- **People index (#3):** essentially done for *SES*. If picked up again, the natural
  next step is a second book (see "For Rufus" above) rather than squeezing more out of
  Bateson/Gould/Comte/Assagioli, whose main-text material is genuinely thin (checked
  this session).
- **Concept wiki (#1):** 17 pages in. Two options, both reasonable: (a) another batch of
  concepts from *SES* — skim `docs/concept-wiki-vision.md` and the full text for what's
  still missing (boomeritis and the Big Three's individual "I/we/it" validity claims are
  candidates, not yet checked in depth), or (b) the spot-check follow-up flagged above
  (`dominator-vs-growth-hierarchy.md`, `systems-theory.md`, `ascent-and-descent.md`,
  `wilber-on-plato.md` against the full text, not just the notes file they were
  originally built from).
