# Wilber Wiki — Initial Plan

Status: draft, first pass. Written to capture scope and a brainstorm of what belongs in this
wiki before we build a real site. Nothing here is committed to a tech stack yet.

## What exists right now

- `bio.md` — draft biography, sourced from Wikipedia + the Ken Wilber Fund.
- `works/index.md` — works list by year (table with cover thumbnail, title/link, year,
  format), linking to a dedicated page per work.
- `works/<slug>.md` — one file per work (39 so far), each with YAML frontmatter (`title`,
  `subtitle`, `year`, `year_note`, `format`, `contributors`, `cover`, `core`, `status`), a
  `## Description`, and an empty `## Notes` section reserved for future annotations. The
  12 works flagged `core: true` — *The Spectrum of Consciousness*, *Grace and Grit*,
  *Sex, Ecology, Spirituality*, *A Brief History of Everything*, *One Taste*, *Integral
  Psychology*, *A Theory of Everything*, *Boomeritis*, *Integral Spirituality*,
  *Integral Life Practice*, *The Religion of Tomorrow*, *Finding Radical Wholeness* —
  each additionally have a `## In-Depth Overview` section (structure, key concepts,
  significance/reception), several paragraphs per book.
- `assets/covers/` — 28 of 39 works have a cached cover image (`<slug>.jpg`, ~150–650px
  on the long edge, "L" size from Open Library), with sourcing/provenance and the list
  of the 11 still missing a cover documented in `assets/covers/SOURCES.md`.

All content lives at the repo root, not under a `content/` wrapper. These are content
drafts, not a site — no framework, no styling, no build has been set up yet, deliberately:
get the material right first, then decide how it's presented.

Publishing target is [Flowershow](https://flowershow.app) (reads markdown + frontmatter
directly, no separate build step needed). Added `config.json` at the repo root with
`"contentExclude": ["/docs"]` so this planning folder never gets published as part of the
site — `contentExclude` fully unpublishes a path (not just hidden from nav/search, as
`contentHide` would leave it); `docs/` is internal, not wiki content.

**Decided:** one markdown file per work (with frontmatter), not a single monolithic list
or a separate YAML/JSON data file. Frontmatter carries the structured fields a future
site would need for the "cover + year + blurb" grid layout (`cover`, `year`, `format`,
`core`); the body carries the longer description and a `## Notes` section that becomes
the natural home for annotations once that feature is built — so book pages and note
pages don't end up as two separate, driftable systems.

## Immediate next steps (this phase)

1. **Verify the tail of the bibliography** (2013 onward) against a publisher catalog or
   Integral World's bibliography page (fetch 503'd during this pass, retry) — several
   `status: draft` pages under `works/` need confirming, especially whether *A Post-Truth
   World* (2024) is a distinct title or a reissue of *Trump and a Post-Truth World*
   (2017), and whether *Integral Politics* (2018, ebook) is distinct content or an
   excerpt.
2. **Source cover art — done for 28/39.** Batch-fetched via the Open Library Covers API
   (title+author search, not ISBN — turned out not to need ISBNs at all) and cached
   under `assets/covers/`. The 11 remaining are genuinely thin on Open Library (mostly
   audio programs, ebook-only titles, and 2015+ releases); see
   `assets/covers/SOURCES.md` for the per-title breakdown and next options (publisher
   site, Amazon, manual scan) if we want to chase down the rest.
3. **Pick a site approach** for when we're ready to make it "nice" — static site generator
   (e.g. Astro/Eleventy) makes sense for a content-heavy wiki like this, and can read the
   frontmatter directly to generate the works grid from `works/*.md` with no separate
   data layer; decide once the annotation-feature requirements (below) are clearer, since
   that may push toward a framework with more interactivity built in.

## Brainstorm: what else belongs in this wiki

Structured pass over what a good Ken-Wilber-and-Integral-Theory reference wiki could
eventually contain, beyond the bio and works list.

### Core reference pages
- **Concept glossary** — AQAL, the Four Quadrants, Levels/Lines/States/Types/Stages,
  holons and holarchy, the pre/trans fallacy, Wilber–Combs Lattice, Integral
  Methodological Pluralism, integral post-metaphysics, "Kosmic address," the
  "mean green meme," Boomeritis, Integral Life Practice's "modules." Each term gets its
  own short page, cross-linked from wherever it's used.
- **Timeline of Wilber's intellectual development** — several commentators (and Wilber
  himself, loosely) periodize his work into phases (sometimes called "Wilber-1" through
  "Wilber-5"); worth a page mapping which books/ideas belong to which phase, since it
  helps a reader place a given book in context.
- **People — influences on Wilber**: Aurobindo, Plotinus, Piaget, Jean Gebser, Jürgen
  Habermas, Adi Da, Da Free John, Roger Walsh, Robert Kegan, Clare Graves/Spiral
  Dynamics, Abraham Maslow, and others whose frameworks Wilber explicitly synthesizes.
- **People — the integral movement**: Terry Patten, Diane Musho Hamilton, Sean
  Esbjörn-Hargens, Roger Walsh, Corey deVos, Marc Gafni (see Controversies below), Don
  Beck (Spiral Dynamics Integral), and others who built on or worked alongside Wilber.
- **Organizations** — Integral Institute, Integral Life, Integral Life Practice, Boulder
  Integral, the Ken Wilber Fund, and their relationships to each other over time (several
  have merged/rebranded — worth getting the institutional history straight).

### Book-level deep-dive pages
- **First pass done:** all 12 `core: true` works now carry an `## In-Depth Overview`
  section on their own page (structure/parts, key concepts introduced, significance —
  a few paragraphs each, not chapter-by-chapter). Worth revisiting later with: key
  diagrams (the four-quadrant chart, developmental-line comparison tables — currently
  described in prose only, not reproduced visually), notable quotes, and — per the
  user's goal — an annotation layer (see below).

### Reception, critique, and controversy
- **Academic and popular critique** — a fair-minded page surveying serious criticism:
  Jeff Meyerhoff's *Bald Ambition* (book-length critique of SES's scholarship), critiques
  from academic philosophy and religious studies of Wilber's synthesis method and
  secondary-source reliance, and general "guru culture" critiques of Integral Institute.
  This belongs as its own page rather than a footnote in the bio, so it can be treated
  properly rather than either whitewashed or reduced to a hit piece.
- **The Marc Gafni controversy** (2011–) — Wilber's public defense of Gafni amid sexual
  abuse allegations, and the fallout within the integral community. Also deserves its own
  page rather than a line in the bio.
- **Reception outside the "integral" niche** — notable public readers (Bill Clinton, Al
  Gore, various tech/business figures), and how integral theory has been taken up (and
  criticized) in adjacent spaces like conscious-business/leadership circles and, more
  recently, some "meta-modern" discourse.

### Browse/index views (once there's enough content)
- By **theme**: psychology, spirituality/mysticism, science-and-religion, politics,
  business/leadership, fiction.
- By **format**: books vs. ebooks vs. audio programs vs. edited anthologies vs. journal
  articles/forewords (not yet inventoried — see Gaps below).
- By **reading path**: a suggested entry-point sequence for newcomers (e.g. *A Brief
  History of Everything* → *The Integral Vision* → *Integral Psychology* → *SES*), since
  Wilber's own back-catalog is not obviously ordered for a first-time reader.

### Not yet inventoried — worth a pass later
- Standalone forewords/introductions Wilber wrote for other authors' books.
- Journal articles, especially in *ReVision* (which he co-founded).
- The *Collected Works of Ken Wilber* multi-volume set (Shambhala) — repackages earlier
  material; worth a short explanatory note rather than treating volumes as new works.
- Interviews and major public talks, if we want a "media appearances" page.

## Annotation feature (later phase)

Superseded by two dedicated vision docs, written after a proper brainstorming pass:
[`concept-wiki-vision.md`](concept-wiki-vision.md) (the priority — the concept-level
index that makes this a wiki) and
[`annotatable-reading-layer-vision.md`](annotatable-reading-layer-vision.md) (a related
but distinct, deferred project: a web-viewable, personally-and-possibly-collaboratively
annotated rendering of a work's text). The rest of this section is kept as historical
context for the open questions that prompted those docs.

Goal per the user: make core books (starting with *SES*) annotatable by them personally.
Not designed yet — flagging the open questions to resolve before building:
- **Single-user vs. multi-user?** If it's just for the user's own reading, a much simpler
  approach (e.g. local-only notes, or a personal layer stored per-user) beats building
  shared/social annotation infrastructure.
- **Granularity** — paragraph-level, sentence-level, or free-floating margin notes against
  a rendered page?
- **Build vs. embed** — a custom annotation layer vs. embedding an existing tool (e.g.
  Hypothes.is) against rendered book pages. Embedding is far less work if the licensing/
  text-availability situation allows displaying substantial book text at all (see Gaps
  below — we do not yet have rights-cleared full text for any book, only our own summaries).
- **Text availability** — we don't have licensed full text of any Wilber book to
  annotate against. Early "annotatable" pages will likely be our own chapter summaries
  and key-quote excerpts (fair-use length) rather than full book text, unless the user
  has their own copies/PDFs they want to work from privately.

Each `works/<slug>.md` page already carries an empty `## Notes` section as a placeholder
for this — cheapest possible starting point (freeform markdown notes under the relevant
book), well short of real inline/paragraph-level annotation, but enough to start
capturing notes on *SES* without blocking on the design questions above.

This needs its own design pass once the bio/works foundation is solid — not blocking, but
flagging now so it isn't a surprise later.

## Open questions for the user

- Tech stack / hosting for the eventual site — any preference, or defer until content is
  further along?
- Should the works page group by year only, or also support a by-theme / by-phase view
  from the start?
- For annotation: personal-use only, or something you'd want to eventually show others?
- Do you have physical/PDF copies of the core books already, or should sourcing text
  excerpts be part of the plan?
