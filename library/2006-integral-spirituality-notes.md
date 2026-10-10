# Integral Spirituality import: provenance and conversion notes

Imported 2026-10-10 for `wilberwiki-s7g`, with the site owner's approval, from `life-itself/library` commit `c9d903590ee2eac7c2021bb4a08e7186cd0ef6f4`, file `books/wilber-integral-spirituality/markdown/wilber-integral-spirituality.md` (SHA-256 `d9df2c76ba9586167adf9b3a231c957f60cd1a80f00191950c130e86f0b2b42b`). The only change on import was rewriting image links from `images/` to `2006-integral-spirituality-images/`, so line numbers match the source file and the line references in `docs/plans/2026-09-18-integral-spirituality-source-selections.md`. Source edition: Shambhala ebook (2011) of the 2006 book.

The upstream conversion notes follow unchanged.

## Conversion notes

## Source and method

- Converted with `books-for-bots` v0.1.1 (commit
  `f4d9940f46db8c2471797ddead38035705950d81`). Its complete test suite passed
  before use.
- The archived EPUB is unchanged. Its SHA-256 digest is
  `f940933691e62b4d57f3503eb724b66db8fb259f805d86964a6b85594ad8c69b`.
- The EPUB identifies the original publication as 2006 and its ebook edition
  as 2011. The Markdown metadata preserves the EPUB's 2006 publication date.
- The source used styled paragraphs, rather than semantic HTML headings and
  footnotes. A temporary copy was normalized before conversion; the copy in
  `raw/` was not altered.

## Corrections

- Restored all 124 semantic section headings encoded as `H1`, `H1x`, or `H2`
  paragraphs in the EPUB. Appendix I also received a combined descriptive
  heading, giving the Markdown 116 level-three and 9 level-four headings.
- Corrected misleading or malformed source/navigation titles: the imprint page
  is `Integral Books`; chapter 7 is `A Miracle Called “We”`; Appendix II is
  `Integral Post-Metaphysics`; and Appendix III is `The Myth of the Given Lives
  On`.
- Restored the internal headings `Boomeritis`, `Boomeritis Buddhism`, `What Is
  Post-Metaphysics?`, and `The Two Cultures`, which would otherwise have been
  mistaken for running titles or chapter titles during conversion.
- Repaired several emphasis spans whose tags overlap incorrectly in the source
  XHTML, including the zone-number examples and an orange-stage reference.
- Converted all 65 source notes to paired Markdown footnote references and
  definitions, including two source notes with irregular identifiers.
- The converter intentionally does not preserve arbitrary source anchor IDs.
  Thirty-two figure and table cross-references therefore link to the containing
  chapter or appendix instead of becoming broken fragment links; their visible
  figure/table labels are unchanged.

## Quality checks

- Output: 5,334 lines and 792,632 bytes, with 24 indexed top-level sections.
- All 65 footnote definitions are referenced, and every reference has a
  definition.
- All 50 Markdown image placements resolve. The converter extracted 42 image
  files; 41 are used by the text, while `pg_81.jpg` is present in the EPUB
  manifest but not referenced from its reading-order documents.
- Source-to-Markdown paragraph sampling and normalized-text comparison found no
  substantive prose omissions. Lists, notes, headings, and deliberate markup
  repairs account for non-identical source paragraphs.
- The final Markdown parses successfully as GitHub-Flavored Markdown with
  footnotes. Its internal links resolve, and checks found no empty links, raw
  HTML tags, or leftover HTML entities.
- Representative simple, color, and fine-print diagrams were visually checked
  after extraction and are legible.
