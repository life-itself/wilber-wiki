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
  concept wiki, but for people Wilber engages with (Habermas, Campbell, etc.). Active
  now, not someday.
- [#4 Finer-grained indexing](https://github.com/life-itself/wilber-wiki/issues/4) —
  largely subsumed by #3 in practice; the general "concepts by location" version stays
  someday.

## Important correction from this session

The concept wiki's first pass (7 pages under `concepts/`) was built from the site
owner's own reading notes (`library/1995-sex-ecology-spirituality.md`), not the actual
book. That was a mistake made early in the session, before the full text was available
here — **going forward, source concept and people pages from the actual book text**,
now at `library/1995-sex-ecology-spirituality-full-text.md` (15,232 lines, originally
converted EPUB→Markdown in a separate private repo, now copied straight into this one —
no ongoing dependency on that other repo; see the file's own header for provenance).
The existing 7 concept pages aren't wrong, just under-sourced — revisit them against
the full text rather than starting over.

Per the site owner: don't worry about copyright/excerpt-length for now — the site isn't
meaningfully public yet. Use whatever excerpting works; that policy can be revisited
later if this ever becomes a genuinely public/promoted site.

This repo is now self-contained for all four work streams below — no need to go check
another repo to pick this up.

## For Rufus

- Skim `people/habermas.md` — first example of a "people" page built from the real
  book text (chapter-cited, not notes-cited). If the shape's right, the remaining 6
  people already researched in `library/1995-sex-ecology-spirituality-people-source.md`
  (Joseph Campbell, Piaget, Freud & Jung, Foucault, Plotinus, Hegel) can be ported the
  same way.
- `docs/annotation-system.md` has the annotation-system research and recommendation
  (Recogito `text-annotator-js` + Hypothes.is fallback) — independently corroborated by
  a second research pass this session, so reasonably high confidence. Nothing built yet.

## For the AI (next session)

- Read this file, then the relevant GitHub issue(s) and the doc(s) they link to, before
  doing anything. Everything needed is in this repo already.
- **Don't run `fl .` (or any Flowershow publish) without checking `library/` first.**
  `library/1995-sex-ecology-spirituality-full-text.md` is the actual book text, git-committed
  per the site owner's explicit instruction, but Flowershow's CLI publish path does NOT
  honor `config.json`'s `contentExclude` (confirmed this session — see AGENTS.md) —
  publishing would make the full text live-reachable by URL. That may be fine (the site
  owner has said not to worry about this for now), but it's a deliberate call to make
  each time, not something to do reflexively via a habitual `fl .`.
- Concept wiki (#1): re-derive/extend the 7 existing `concepts/*.md` pages against
  `library/1995-sex-ecology-spirituality-full-text.md` instead of the old notes file.
- People index (#3): port the remaining 6 entries from
  `library/1995-sex-ecology-spirituality-people-source.md` into `people/*.md` here,
  following `people/habermas.md`'s shape (short synthesis in your own words + a couple of
  short verbatim quotes, chapter-cited — that source file's quotes run longer than what
  actually belongs on a public page, don't copy them wholesale). Add `people/index.md`
  (mirror `concepts/index.md`), cross-link from `concepts/` and
  `works/1995-sex-ecology-spirituality.md`, and add a card to root `index.md`.
- Annotation system (#2): `docs/annotation-system.md` already has a clear recommendation
  and two-phase build plan — read it and either start Phase 1 or write a short design
  update to `docs/annotatable-reading-layer-vision.md` reflecting the chosen approach
  before building.
