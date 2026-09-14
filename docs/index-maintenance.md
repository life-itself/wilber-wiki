# Maintaining the public indexes

Public index introductions should explain what readers can find and where to go
next. Keep schemas, source-file paths, scan methodology, and implementation progress
in this folder or in Beads. Preserve useful source-book attribution and explain
uncertainty in ordinary reader-facing language.

## Navigation

The top menu links to the reader-first Works hub at `/works`. It presents three
routes: an inline recommendation with a link to the full reading guide, the complete
chronological catalog at `/works/catalog`, and the phases guide. Those guides link to
one another and to individual books. No dropdown is needed. See
[Maintaining the works catalog](works-catalog.md) for the book-page standard.

## Concepts

`concepts/index.md` groups `category: core-term` and `category: wilber-on-x` pages.
Explain these publicly as core vocabulary and views on broader topics. The rationale
is in [the concept wiki vision](concept-wiki-vision.md).

Sources are the actual full-text books in `library/`, currently SES and Integral
Psychology. Each excerpt page's `works` field identifies its source books; its
status captures editorial state. Do not expose those implementation details or link
to excluded planning/source documents from the public introduction.

## People

Keep the existing per-book rosters and counts. A person's single page can carry
excerpts from several works. The scan records are:

- `library/1995-sex-ecology-spirituality-people-source.md`
- `library/2000-integral-psychology-people-source.md`

The current SES roster has 23 linked pages and four unlinked names; the IP roster
has 14 linked pages, eight shared with SES and six additional people. These are
coverage records, not instructions to present task-completion statistics to readers.

Counts should be described as indicative frequency, not substantive importance.
The previous public introduction described all SES counts as main-body-only, but
its own exception notes contradicted that. Before standardizing or combining counts,
check the scans and their counting rules. The consolidated overview is separately
tracked in `wilberwiki-002`; this copy cleanup does not recalculate counts.

The prior substance review recorded these reasons for leaving four SES names unlinked:

- Bateson: the eight recorded mentions were in endnotes, principally through Berman.
- Gould: a passing credit for the punctuational model, with Eldredge; the displayed
  scan count and the substantive occurrence count are not interchangeable.
- Comte: a name in a list of structural-functionalists, without a developed argument.
- Assagioli: a bibliography reference, without substantive main-body discussion.

These are historical editorial decisions, not proof that further source books
cannot support pages. Reassess against the actual text when extending coverage.

## Adding or editing excerpt pages

Read [the excerpt-page skill](../skills/add-excerpt-page/SKILL.md) in full before
editing `people/` or `concepts/`. It is the authoritative standard for frontmatter,
sourcing, synthesis, chapter attribution, and quote verification; do not maintain
a competing copy here. Update the relevant index when a page is added.

After index edits, check local links and run the required quote verifier. Keep
changes to count methodology, new pages, and new navigation features separately
scoped from editorial cleanup.
