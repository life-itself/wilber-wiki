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
now at `library/1995-sex-ecology-spirituality-full-text.md` (15,232 lines, copied from
the private `library` repo's EPUB→Markdown conversion — see that repo's
`books/wilber-sex-ecology-spirituality/` for the source of truth, raw EPUB included).
The existing 7 concept pages aren't wrong, just under-sourced — revisit them against
the full text rather than starting over.

Per the site owner: don't worry about copyright/excerpt-length for now — the site isn't
meaningfully public yet. Use whatever excerpting works; that policy can be revisited
later if this ever becomes a genuinely public/promoted site.

## For Rufus

- Skim `people/habermas.md` — first example of a "people" page built from the real
  book text (chapter-cited, not notes-cited). If the shape's right, the remaining 6
  people already researched in the `library` repo's `PEOPLE.md` (Joseph Campbell,
  Piaget, Freud & Jung, Foucault, Plotinus, Hegel) can be ported the same way.
- The two independent annotation-system research passes (this session's, and the
  parallel one in the `library` repo's `docs/annotation-system.md`) landed on the same
  recommendation — worth reading `docs/annotation-system.md` there once, since it's more
  complete than anything written up in this repo yet.

## For the AI (next session)

- Read this file, then the relevant GitHub issue(s) and the doc(s) they link to, before
  doing anything.
- **Don't run `fl .` (or any Flowershow publish) without checking `library/` first.**
  `library/1995-sex-ecology-spirituality-full-text.md` is the actual book text, git-committed
  per the site owner's explicit instruction, but Flowershow's CLI publish path does NOT
  honor `config.json`'s `contentExclude` (confirmed this session — see AGENTS.md) —
  publishing would make the full text live-reachable by URL. That may be fine (the site
  owner has said not to worry about this for now), but it's a deliberate call to make
  each time, not something to do reflexively via a habitual `fl .`.
- Concept wiki (#1): re-derive/extend the 7 existing `concepts/*.md` pages against
  `library/1995-sex-ecology-spirituality-full-text.md` instead of the old notes file.
- People index (#3): port the remaining 6 entries from the `library` repo's
  `books/wilber-sex-ecology-spirituality/people/PEOPLE.md` into `people/*.md` here,
  following `people/habermas.md`'s shape. Add `people/index.md` (mirror
  `concepts/index.md`), cross-link from `concepts/` and `works/1995-sex-ecology-spirituality.md`,
  and add a card to root `index.md`.
- Annotation system (#2): reconcile this session's 3 research write-ups (not yet
  committed anywhere — see the session transcript, or ask to have them redone) with the
  `library` repo's `docs/annotation-system.md`, then write one merged doc here (probably
  updating `docs/annotatable-reading-layer-vision.md` or a new
  `docs/annotation-system-plan.md`) before building anything.
