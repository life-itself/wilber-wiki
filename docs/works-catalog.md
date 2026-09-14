# Maintaining the works catalog

Public content lives in `works/`: one page per title/edition, a chronological
`index.md`, a selective `reading-guide.md`, and an intellectual-history `phases.md`.
Research and implementation plans belong in `docs/plans/`; this file documents
the working conventions.

## Book-page fields

Frontmatter carries `title`, `subtitle`, `year`, `year_note`, `format`,
`contributors`, `cover`, `core`, and `status`. Existing formats include `book`,
`co-authored`, `editor`, `anthology`, `audio`, `ebook`, and `multimedia`.
Use `editor` where Wilber edits a collection, and `anthology` for a selection of
his writings; name compilers/editors separately in `contributors` and the body.
`core` is an editorial selection across genres, not a prerequisite reading list.

`year` normally means first publication. Explain conflicting dates in `year_note`
and in the reader-facing year line. Keep existing page addresses when correcting a
year, so links do not break. Distinguish original publication from a later paperback,
ebook, revision, or retitling. Cover provenance is in `assets/covers/SOURCES.md`.

## Sources and uncertainty

Prefer title/copyright pages, publisher records, and edition-specific library
catalogs. Author-affiliated and independent bibliographies help locate publications
but can repeat errors. Cite the source supporting each material correction on the
public page, and keep the full audit trail in the dated research ledger.

`status: draft` signals unresolved bibliographic details or description. A verified
short description is not a certification of every sentence in an older overview.
State residual uncertainty explicitly; do not infer the amount of revision from
a changed title or page count alone. The current audit is documented in
`docs/plans/2026-09-14-works-bibliography-audit.md`.

## Relationships and reading advice

Add a short relationship/publication-history section and reciprocal book links.
Distinguish retitled edition, revised edition, accessible restatement, anthology
selection, and conceptual development/application. The last two may involve many
source works; do not force them into a single-parent hierarchy. Editorial reading
advice should be recognizable as advice, separate from bibliographic fact.

Keep index rows chronological and match the page's year, format and draft label.
Show important edition relationships beside the title. The reading guide can be
selective; the catalog should not delete a useful title simply because another
edition or introduction overlaps with it.

## Checking changes

To add a work, create `works/<year>-<slug>.md` with the fields above, a concise
description, and cited publication evidence. Add its row in the appropriate year
group in `works/index.md`; include any known edition relationship. Add it to a
reading guide only if it serves that guide's selection, not automatically. Verify
new cover provenance in `assets/covers/SOURCES.md` when adding an image.

Check all new local links, index/page consistency, and `git diff --check`. Compare
any factual correction with its cited evidence. Content-only edits do not require
application tests. No source-book text should be linked into the public guides;
cite the book and chapter/note, since `library/` is excluded on production.
Follow `AGENTS.md` for Beads, changelog, and publishing procedures.
