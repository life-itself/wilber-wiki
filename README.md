# Wilber Wiki

Focused, concept-level knowledge base on Ken Wilber and integral theory.

Source project doc: `~/src/me/planning/initiatives/wilber-wiki.md`
First build: `~/src/me/planning/projects/2026-wilber-wiki-first-pass.md` — set up the
site and create an initial working treatment of *Sex, Ecology, Spirituality*.

## Contents

- `config.json` — Flowershow site config. `docs/` is excluded from publishing
  (`contentExclude`) — it's internal planning, not wiki content.
- `docs/plan.md` — initiative plan, brainstorm of future wiki sections, open questions.
- `docs/concept-wiki-vision.md` — vision for the concept wiki (the priority): concept
  pages synthesizing Wilber's view on an idea, with curated excerpts across works.
- `docs/annotatable-reading-layer-vision.md` — vision for a related, deferred project:
  a web-viewable, annotatable rendering of a work's text.
- `bio.md` — draft biography of Ken Wilber.
- `works/index.md` — works list by year, linking to a dedicated page per work.
- `works/<slug>.md` — one page per work, with frontmatter (title, year, format, cover,
  core, status) plus a description, an `## In-Depth Overview` on the 12 core works, and
  a `## Notes` section reserved for future annotations.
- `concepts/index.md` — the concept wiki: one page per concept (`concepts/<slug>.md`),
  each with a synthesis of Wilber's view plus curated excerpts from `library/` sources,
  shown as foldable callouts (click a short quote to expand the full passage in place).
  Pilot pass: 7 concepts, all sourced from *Sex, Ecology, Spirituality*.
- `library/<slug>.md` — source reading notes used to curate concept excerpts from.
  Denser/rawer than what's meant to appear on a concept page. Marked private via
  `contentExclude` in `config.json`, though see AGENTS.md — that only takes effect
  under GitHub-sync publishing, not the CLI-published preview site.
- `assets/covers/` — cached cover images (28 of 39 works so far), sourced from Open
  Library; see `assets/covers/SOURCES.md` for provenance and what's still missing.

Content drafts, not yet a styled site — Flowershow reads the markdown/frontmatter
directly, so most of what's here is already publishable as-is.
