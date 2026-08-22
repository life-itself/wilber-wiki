# Text annotation system — research + plan

Status: research done, nothing built yet. Written 2026-08-22; copied into this repo
from a parallel private repo where it originated. A second, independent research pass
in this repo's own session that same day reached the same conclusions (Recogito
`text-annotator-js` as the engine, Hypothes.is as a zero-build fallback, Flowershow's
`config.json` `head` field confirmed for script injection) — worth noting as
corroboration, not just one researcher's opinion.

## What we want

Two use cases, in priority order:

1. **Show existing annotations (primary).** Rufus already has, in his own
   notes on books like *Sex, Ecology, Spirituality*, a quote from the text
   plus a comment/heading about it. Render the book's text with these
   showing as inline highlights + a comment alongside (margin/sidenote
   style, à la Google Docs comments or Genius.com), not as a separate
   document.
2. **Add new annotations dynamically (bonus).** Let annotations be added
   live in the browser — Rufus adding more as he rereads, and ideally
   other people commenting too — without a full CMS/editor build.

A third, explicitly lower-priority option was raised and set aside: fully
pre-rendered sidenotes (annotations baked into the HTML at build time,
static, no JS). Worth keeping in mind as a fallback/simplification but not
the target — the ask is for something at least somewhat dynamic.

## Landscape survey

| Project | What it is | Status | Fit |
|---|---|---|---|
| [**Annotator.js**](https://github.com/openannotation/annotator) (openannotation) | The classic library Rufus used before — inject as a script tag, select text, add notes. | **Dead.** Confirmed unmaintained, explicitly described by its own maintainers as stalled and superseded. Don't build on this. | ❌ |
| [**Apache Annotator**](https://github.com/apache/incubator-annotator) (`apache-annotator` on npm) | Modular toolkit for the *anchoring* problem — algorithms (`TextQuoteSelector`, `TextPositionSelector`, `RangeSelector`) that find a quote in a live DOM, robust to re-rendering/edits. Grew out of experience with Annotator.js and Hypothes.is. | Apache Incubator project; still active but low-level — it's a library of building blocks, not a UI or a product. | ⚠️ Foundational, not turnkey. Worth knowing the concepts even if we don't use the package directly — both tools below implement the same idea. |
| [**Hypothes.is**](https://github.com/hypothesis) (`client` + `h` server) | The dominant modern web-annotation tool. `client` is a browser-side sidebar/highlighter, actively maintained (commits as recent as Aug 2026). `h` is the Python/Elasticsearch/Postgres server, open source, self-hostable but built for large-scale deployment (real infra, not a drop-in). | Actively maintained, widely used in education (LMS/LTI integrations). | ✅ for zero-effort start (see below), ⚠️ heavy if self-hosting the server. |
| [**Recogito text-annotator-js**](https://github.com/recogito/text-annotator-js) | Actively developed successor to the deprecated `recogito-js`. Vanilla-JS core (React wrapper optional), BSD-3-Clause. **Backend-agnostic**: `loadAnnotations(url)` / `setAnnotations()` to bulk-load, `createAnnotation` events to capture new ones — you supply storage. Anchors by quote text + character offsets (same family of idea as Apache Annotator's selectors), so it survives page re-renders reasonably well. | Active (1,500+ commits), from the Pelagios/Recogito scholarly-annotation project (TEI/XML + PDF extensions exist). | ✅ Best fit — see recommendation. |
| [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) | The standard (quote + target + body + selector) that Hypothes.is, Recogito, and Apache Annotator all converge on. Not a library — a data shape. | Stable W3C Recommendation. | Reference model for whatever annotation JSON we design. |
| Browser-extension annotators (Kreo, Zotero-style highlighters, etc.) | Personal, install-on-your-own-browser tools for annotating *any* page. | Various, several active in 2025–2026. | ❌ Wrong shape — these annotate pages for the individual user, not for site visitors. Not useful here. |
| [Tufte CSS](https://edwardtufte.github.io/tufte-css/) sidenotes / [sidenotes.js](https://gwern.net/sidenote) | Compile-time (pure CSS) or runtime-JS margin notes, no annotation *data model* — just a layout technique for notes you already wrote into the HTML. | Both stable/mature; Gwern's essay at gwern.net/sidenote is the best writeup of the design tradeoffs. | ✅ For the **display layer** (how a comment renders next to a highlight) regardless of which annotation engine feeds it. Also viable as the "secondary, pre-rendered" fallback on its own, with no JS annotation engine at all. |

## Recommendation

**Recogito `text-annotator-js`** as the annotation engine:
- Vanilla JS, no framework lock-in, so it can be injected as a script tag.
- Backend-agnostic — matches "storage can be somewhere else" — we can start
  with a static JSON file per chapter (zero backend) and later swap in a
  write API without changing the anchoring/highlighting logic.
- Bulk pre-load (`loadAnnotations`) is exactly use case 1: hand it a JSON
  array of `{quote, comment}`-shaped annotations for a chapter and it
  highlights every quote it can find in the rendered page and exposes
  hooks for our own comment-rendering UI (it doesn't ship an opinionated
  sidebar, which is a feature here — we want margin/sidenote-style, not a
  Hypothes.is-style right-hand sidebar).
- `createAnnotation` events are exactly use case 2's hook once we're ready
  to persist new annotations somewhere.

**Hypothes.is is the pragmatic shortcut if we want live-collaborative
annotation with near-zero build effort**: one `<script>` tag
(`https://hypothes.is/embed.js`), backed by the free public hypothes.is
service — no backend of our own at all. Tradeoffs: annotations live on
hypothes.is's infrastructure (not in this repo), the UI is their sidebar
(not the margin/sidenote look Rufus wants), and it's overkill/wrong shape
for "just show my pre-written commentary." Worth keeping as a fast fallback
or a genuine option for the "bonus" live/collaborative case specifically,
rather than for use case 1.

## Two-phase build plan

**Phase 1 — show existing annotations (matches the primary ask, "relatively
straightforward").**
1. Write a small script to turn Rufus's existing notes (quote + comment,
   currently headings in his own notes) into a per-chapter JSON file,
   shaped roughly like `[{quote, comment, chapter}]`. Location:
   `books/<slug>/annotations/<chapter>.json`, next to `digest/` and
   `anki/` following the existing per-book folder convention in
   `AGENTS.md`.
2. On the published (Flowershow-rendered) page, load `text-annotator-js`,
   call `loadAnnotations()` with that chapter's JSON, and render each
   comment as a margin note next to its highlight (own small CSS/JS layer
   on top of Recogito's highlighting — Tufte CSS/gwern-style sidenote
   layout is a good starting point for that rendering).
3. No backend. No write path. Static JSON in the repo, JS runs client-side
   at read time only.

**Phase 2 — dynamic/live annotation (bonus).**
- Simplest: `createAnnotation` events write to `localStorage` — matches
  what Rufus described doing before, personal-only, zero infra, but
  doesn't persist across devices or show to other visitors.
- Next step up: a small write API (Cloudflare Worker + KV/D1, or
  Supabase) that Recogito's `createAnnotation` posts to, and that feeds
  back into the same JSON shape `loadAnnotations()` reads — same data
  model end to end.
- Full collaborative/live: Hypothes.is public service via `embed.js`
  instead of rolling our own store — biggest scope jump, only worth it if
  multi-user live annotation becomes an actual near-term goal rather than
  "would be a bonus."

## Flowershow injection — confirmed feasible

Flowershow supports a **`head` field in `config.json`** (also editable via
Dashboard → Site Settings → Analytics → Custom Head Code) that injects raw
HTML into the `<head>` of *every page* on the site — explicitly documented
as being for "widget loader scripts." Confirmed at
[flowershow.app/docs/reference/custom-head](https://flowershow.app/docs/reference/custom-head).
Example:

```json
{
  "head": "<script defer src=\"https://our-cdn/annotator-loader.js\"></script>"
}
```

Caveat: this is **site-wide**, not per-page — fine for loading the
annotator engine itself, but the annotator then needs to fetch
page-specific annotation data at runtime based on the current URL/chapter
slug (which is exactly how Hypothes.is and Recogito are designed to work
— annotations are already scoped by target URI, not baked in per page at
build time).

## Important open question, not yet resolved

`README.md` currently states this repo is **private and deliberately
isolated from anything that syncs toward public surfaces**, because book
text is copyrighted. Rendering annotated book text via Flowershow *is*
publishing to a public surface. Before building Phase 1, we need to decide:
private/access-controlled Flowershow site vs. rethinking what text is
actually shown (e.g., only the quotes Rufus selected, not full chapters) vs.
some other resolution. Flagging this now rather than building around it
silently.

## Next steps

- [ ] Resolve the copyright/private-surface question above.
- [ ] Prototype Phase 1 on one chapter of the Wilber book: hand-write ~5
      quote+comment annotations as JSON, get `text-annotator-js` to
      highlight + sidenote them on a local render.
- [ ] Decide margin-note visual design (Tufte CSS as a starting point).
