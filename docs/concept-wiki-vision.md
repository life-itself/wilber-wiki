# Concept Wiki — Vision

Status: vision, not a design. This describes *what* the concept wiki is and *why* it
matters, deliberately without committing to a data model, file layout, or UI
implementation — that comes next, as a separate design pass.

This is one of two related but distinct pieces of work identified for wilber-wiki. The
other — a web-viewable, annotatable edition of Wilber's texts, personally and
potentially collaboratively commented on — is described in
[`annotatable-reading-layer-vision.md`](annotatable-reading-layer-vision.md). The two
can eventually feed each other, but neither depends on the other existing. **This
document is the priority: it's what actually makes this project a wiki**, rather than a
bibliography with notes attached.

## Thesis

Reading Wilber, especially a dense work like *Sex, Ecology, Spirituality*, means
repeatedly noticing "he's talking about X here" — holons, postmodernism, complexity
theory, Gaia theorists, growth vs. dominator hierarchies — without any way to see, in
one place, everything he's said about X. A book's own index gets you a list of page
numbers for a term; it doesn't synthesize his view, and it definitely doesn't span
multiple books. If you want to know "what does Wilber actually think about complexity
theory, and where does he say it," today the answer is "reread and remember, or go
hunting."

The concept wiki inverts this. Instead of a work containing scattered mentions of a
concept, a **concept page** collects the concept: a synthesized account of Wilber's
view (including a critical take — what's strong about it, what's contestable), sitting
directly alongside the actual passages where he makes that case, pulled from wherever
in his corpus he makes it. It's the annotated index a book never gives you, standing on
its own as a reference.

## What counts as a "concept" here

Not only Wilber's own named terms (holon, holarchy, AQAL, the four quadrants, the
pre/trans fallacy, flatland). Just as valuable, and arguably more interesting, are
**Wilber's take on a topic** — his critique of postmodernism as an ideology, his view of
complexity/systems theory and its limits, his read on Gaia-theory advocates, his account
of growth vs. dominator hierarchies. These "Wilber on X" concepts are a distinct,
first-class category alongside the canonical vocabulary — a concept page for "Wilber's
critique of postmodernism" is a different, more interesting thing than a concept page
that just defines postmodernism.

## What a concept page contains

- A synthesis of Wilber's position — not a neutral encyclopedia definition, but *his*
  take, written with enough perspective to note where it's strong and where it's
  contestable.
- A curated set of excerpts evidencing that synthesis, each drawn from a specific work.
  A concept relates to **many** passages, potentially across **many** works — this is a
  many-to-many relationship, not one concept-to-one-quote.
- Each excerpt starts short (a sentence or two — enough to place it) and can be expanded
  to its fuller passage and surrounding context, read in place, without leaving the
  concept page to go hunt through the source work. The point of the wiki is that you
  never have to "go somewhere else to read it" — short and long forms of the same
  excerpt live together.
- No page-number citation. Source texts are read from ebook/EPUB editions, not
  paginated print copies, so citation is by structural location (work title, and
  section/chapter if useful) — good enough to place an excerpt, not intended to support
  print-style page references.

## Relationship to works

Concept pages are a second axis over the same underlying works already catalogued in
`works/`. A work page stays the bibliographic/descriptive entry point ("what is this
book"); concept pages are the cross-cutting index over it and others ("where does this
idea show up, across everything he's written"). Both need to coexist and stay
consistent — a work isn't fully covered by the concept wiki, and a concept page doesn't
replace needing a work's own overview.

## Relationship to the annotatable reading layer

Secondary, optional connection, not a dependency: personal annotations made against a
work's text (see the companion vision doc) sometimes tag a passage as relevant to a
concept, and could surface there as a candidate excerpt. But most annotations won't be
concept-tagged at all — they're personal reactions, not concept curation — so the
concept wiki must stand on its own, populated by direct curation (manual and/or
AI-assisted from source notes), independent of whether the annotation layer exists yet.

## Incremental path

Starting material is not raw book text but existing partially-structured personal
reading notes (already excerpt-heavy, already organized by theme/section, already
carrying some editorial commentary) for *Sex, Ecology, Spirituality* — plus similar
notes that exist for a few other Wilber works, and a handful of existing notebook pages
that are already informal concept pages in miniature (e.g., an existing note quoting
Wilber on growth vs. dominator hierarchies, sourced to a specific book).

Proposed sequencing:
1. Pilot: pick roughly 5-10 concepts and build real concept pages against *SES* only, to
   prove the model (synthesis + multi-excerpt list + expand-in-place reading) is
   actually the right shape before investing further.
2. Scale out: repeat against other works with existing source notes, and fold in the
   existing notebook's informal concept notes.
3. Only after the model is proven: revisit whether/how the annotatable reading layer
   should feed it.

Explicitly not attempting exhaustive concept coverage, or coverage of every work, on the
first pass.

## Design update — excerpt display (2026-08-23)

The first build of "expand to fuller passage" (line 52-56 above) used Obsidian's
foldable callout syntax (`> [!quote]- "one-line teaser"`, click to expand to the full
quote). Rufus's feedback: this isn't what he meant, and isn't useful — reduces the
excerpt to a hidden one-liner when the quote itself *is* the point, and reads as the
kind of accordion-chain digital-garden pattern he specifically doesn't want. **Removed
across all concept and people pages** (2026-08-23): every excerpt now shows in full,
directly, no per-excerpt heading (the surrounding prose already frames it), with its
most load-bearing sentence bolded in place where a clean match exists.

What "context" actually means, per Rufus, clarifying the original brainstorm note
above: not a second, longer version of *the same excerpt* revealed by expanding it —
scrolling the actual **surrounding pages of the source book itself**, in place, without
losing where you are on the concept/person page. Described as "almost iframing the book
into the side of the page, linking to this place" — i.e. a side panel that can show and
scroll a live rendering of the book around the cited location, not just a bigger
blockquote. This is a genuinely different, larger feature than anything built so far —
it needs a scrollable, addressable rendering of full book text to link *into*, which is
exactly the [annotatable reading layer](annotatable-reading-layer-vision.md)'s territory
(that project's Phase 1 prototype, as of this date, already renders one book excerpt
with per-passage anchors — the natural link target once this is designed properly).
**Not built. Flagged here so the "expand excerpt" idea doesn't quietly get re-attempted
as the accordion's replacement** — the actual ask is a link out to a live, scrollable
book view, not a fancier inline expansion.

## Non-goals (for now)

- A full web-viewable/annotatable rendering of entire works (that's the companion
  project).
- Multi-user/social commentary.
- Page-accurate citation.
- Publishing full copyrighted book text — excerpts stay at the length needed to
  evidence a point, not to reproduce the work.
- Exhaustive concept coverage on day one.

## Appendix: raw brainstorm (source material)

Condensed from the original outflow that prompted this doc:

- Motivating frustration: reading *SES* and constantly thinking "he's talking about
  topic X" with no index back to a common concept register — the richness of
  Wilber/integral thought is scattered and hard to retrieve across a huge back
  catalogue.
- Desired shape: "an inverted index... but annotated" — not just a term with page
  numbers, but a concept written up with description, then excerpts from the different
  places it shows up, so you can see everywhere a concept appears across the corpus in
  one place.
- Explicit examples given: the holonic material set out in a particular section of
  *SES*; commentary on postmodernism as an ideology; commentary on complexity theory
  (what's good about it, what its limits are per Wilber); commentary on Gaia-theory
  advocates. These recur across multiple books, not just one.
- On UI (design-level, noted here only to preserve intent, not committed to): imagined
  a wide-screen layout where clicking a short excerpt reveals the full passage
  alongside it — reading concept and source side by side, without navigating away. That
  becomes a design decision for the next phase, not part of this vision.
- Source-material discovery during brainstorming: a private personal notebook
  (`~/src/me/rufuspollock.com/`) already contains a structured, quote-heavy notes file
  for *SES*, similar note files for several other Wilber books, a `Ken Wilber.md` hub
  page, and at least one existing note (`Growth Hierarchies.md`) that is already, in
  effect, a proto concept page: a quote from a named book with a claim about what
  Wilber is saying with it. This is the natural seed material for the pilot, rather than
  starting from a fresh full-text conversion.
- Confirmed decision: no page-number citation is needed — text is sourced from ebooks,
  not paginated print, so section/structural citation is sufficient.
