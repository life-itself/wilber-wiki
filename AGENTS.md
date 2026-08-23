# AGENTS.md

## What this project is

A concept-level knowledge base on Ken Wilber and integral theory. **Read
[`NEXT.md`](NEXT.md) first** — it's the up-to-date map of the active work streams
(concept wiki, people index, annotation system, text indexing), each with a GitHub
issue linking to its vision/plan doc. Don't re-derive the vision from scratch, and don't
conflate the work streams — they're deliberately separate.

There's a separate private repo (`life-itself/library`) that originally converted the
Wilber book from EPUB and did some independent people/annotation research — this repo
now has its own copies of everything from there that's actually needed
(`library/1995-sex-ecology-spirituality-full-text.md`,
`library/1995-sex-ecology-spirituality-people-source.md`, `docs/annotation-system.md`),
committed here at the site owner's explicit instruction (he doesn't want copyright
excerpting concerns to slow down building this site right now — see NEXT.md). **No
ongoing dependency on that other repo** — everything needed to work on this project is
in this repo. That instruction covers committing the full text to this repo; it does
**not** by itself mean *publish it live* — see the Publishing section below before ever
running `fl`.

## Skills

`skills/` holds this repo's own reusable-process skills — tool-agnostic (not
`.claude`-specific, since this repo gets worked on from more than one agent runtime).
Claude Code discovers them via a symlink at `.claude/skills/<name>` → `../../skills/<name>`
(same pattern as `CLAUDE.md` → `AGENTS.md`); other runtimes should read this section and
follow the referenced `SKILL.md` directly, since project-level skill auto-discovery isn't
guaranteed everywhere. Add a matching symlink for any other runtime's expected skills
path if that runtime doesn't otherwise find these.

- **[`skills/add-excerpt-page/SKILL.md`](skills/add-excerpt-page/SKILL.md)** — the
  process for adding/editing a `concepts/*.md` or `people/*.md` page: sourcing,
  page shape, and a **mandatory** quote-verification script
  (`skills/add-excerpt-page/scripts/verify_quotes.py`) that checks every excerpt is
  real text from the source book, not a paraphrase or reconstruction. Built after a
  page shipped once with a fabricated quote formatted as verbatim — read this before
  touching either folder.

## Content structure

Content lives at the repo root, not under a `content/` wrapper — deliberate, so
Flowershow can read it with no build step.

- `works/<slug>.md` — one page per Wilber book (bibliographic + description; the 12
  `core: true` works also get an `## In-Depth Overview`). `works/index.md` is the full
  catalog.
- `concepts/<slug>.md` — the concept wiki itself: a `## Wilber's View` synthesis plus
  excerpts shown directly (no accordion — see `skills/add-excerpt-page/SKILL.md` for the
  page shape and the mandatory quote-verification step before adding/editing one of
  these). `concepts/index.md` lists them all. Frontmatter schema: `title`, `slug`,
  `aliases`, `category` (`core-term` vs. `wilber-on-x`), `status`, `works`.
- `library/` — source material concept/people pages are curated *from*, not meant to be
  read as wiki content in its own right. `1995-sex-ecology-spirituality.md` is the site
  owner's reading notes (partial, thin coverage); `1995-sex-ecology-spirituality-full-text.md`
  is the actual book, copied from the private `library` repo — **this is the real
  source to build concept/people pages from**, not the notes file (an earlier session
  mistakenly used the notes file before the full text was available here). See the
  Publishing section below for why "private" is currently aspirational, not enforced.
- `people/<slug>.md` — same shape as `concepts/`, but for people Wilber engages with
  (Habermas, Joseph Campbell, etc.). `people/index.md` lists them. See NEXT.md/issue #3.
- `docs/` — internal planning/vision docs, not wiki content.
- `assets/covers/` — cached cover images from Open Library.
- `bio.md` — draft Ken Wilber biography.
- `index.md` — the site's homepage (landing page). `README.md` is the short
  GitHub-facing blurb only; it isn't what renders as the site root.

## Publishing / preview site

Built and deployed with [Flowershow](https://flowershow.app) — for anything Flowershow
config/CSS/setup-related beyond what's below, install their skill rather than guessing:
`npx skills add flowershow/skills --global` (or read
`https://raw.githubusercontent.com/flowershow/skills/main/SKILL.md` directly), and see
https://flowershow.app/docs/agents.

The live preview is **`wilberwiki-preview`**, recorded in the committed `.flowershow`
file so you don't need `--name` again:

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
worth revisiting **now that `library/` holds the actual full book text**, not just
excerpts. Check with the site owner before running `fl`/publishing if it's been a while
since `library/`'s contents were last reviewed — this isn't a hard rule, just don't
publish reflexively without thinking about what's currently in that folder.

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
