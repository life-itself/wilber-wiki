# AGENTS.md

## What this project is

A concept-level knowledge base on Ken Wilber and integral theory. Two distinct pieces
of work, both described as vision docs before any implementation:
[`docs/concept-wiki-vision.md`](docs/concept-wiki-vision.md) (the priority — a
concept-first index over Wilber's ideas, synthesis + curated excerpts across works) and
[`docs/annotatable-reading-layer-vision.md`](docs/annotatable-reading-layer-vision.md)
(related but distinct, deferred — a web-viewable, annotatable rendering of a work's
text). Read those before proposing new features; don't re-derive the vision from
scratch. [`docs/plan.md`](docs/plan.md) is the older, broader initiative plan/brainstorm
these two vision docs superseded the annotation section of.

## Content structure

Content lives at the repo root, not under a `content/` wrapper — deliberate, so
Flowershow can read it with no build step.

- `works/<slug>.md` — one page per Wilber book (bibliographic + description; the 12
  `core: true` works also get an `## In-Depth Overview`). `works/index.md` is the full
  catalog.
- `concepts/<slug>.md` — the concept wiki itself: a `## Wilber's View` synthesis plus
  excerpts as foldable Obsidian callouts (`> [!quote]- teaser` / `> full passage`,
  natively collapsible — no JS). `concepts/index.md` lists them all. Frontmatter schema:
  `title`, `slug`, `aliases`, `category` (`core-term` vs. `wilber-on-x`), `status`,
  `works`.
- `library/<slug>.md` — private source material (reading notes, not full book text)
  that concept pages are curated *from*. Not meant to be read as wiki content in its own
  right — see the Publishing section below for why "private" is currently aspirational,
  not enforced.
- `docs/` — internal planning/vision docs, not wiki content.
- `assets/covers/` — cached cover images from Open Library.
- `bio.md` — draft Ken Wilber biography.

## Publishing / preview site

Deploy with the `fl` CLI (Flowershow). The live preview is **`wilberwiki-preview`**,
recorded in the committed `.flowershow` file so you don't need `--name` again:

```
fl . --yes
```

Run from the repo root. Site: https://wilberwiki-preview-rufuspollock.flowershow.me

**Always pass `.`, never individual files/folders.** `fl` treats whatever paths you
give it as the *complete* authoritative set for the site — passing e.g. just
`config.json`, or a hand-picked list of folders, makes it delete every other file
already published (confirmed the hard way: `fl config.json --yes` wiped 85 files; a
follow-up publish with explicit folder names instead of `.` silently flattened the
`assets/` path prefix and broke every page route). `fl .` is the only combination
verified to preserve correct site structure and navigation.

**`config.json`'s `contentExclude` (currently `/docs`, `/library`) is NOT enforced by
this CLI publish path.** Confirmed by direct testing: neither repo-level
`contentExclude` nor page-level `publish: false` frontmatter has any effect when
publishing via `fl` — that filtering is implemented only in Flowershow's GitHub-sync
ingestion workflow, not the CLI's direct-upload path. Practical effect: on the
`wilberwiki-preview` site, `docs/` and `library/` pages **are** reachable if you know
the URL, even though nothing in the published content links to them. Don't treat this
as real privacy. If/when this project gets a real production site, publishing via a
connected GitHub repo (not the CLI) is what would actually make `contentExclude` work —
worth revisiting before `library/` ever holds anything more sensitive than book-note
excerpts.

## Changelog

This repo keeps a `changelog.md` (dated entries, newest first). At the end
of a work session, if something worth recording actually shipped — skip
trivial sessions (typo fixes, dead ends, no visible outcome) — draft a
dated entry. Match the entry's weight to what a reader would actually care
about: a real feature/fix/content gets a title, one or two sentences, and a
screenshot if something visual shipped; small stuff (cleanup, rename,
reorg, tidying) gets one plain sentence, no bullets, no screenshot — even
if several small things happened, that's still one combined sentence, not
a bullet per thing. Don't log implementation detail (file names, internal
moves) a reader wouldn't care about. First time writing an entry in this
repo, or if the format is unclear: fetch and follow
https://raw.githubusercontent.com/life-itself/changelog/main/CONVENTION.md
