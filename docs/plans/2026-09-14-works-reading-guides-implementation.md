# Works and Reading Guides Implementation Plan

> **For implementers:** Use superpowers:executing-plans where available to work
> task-by-task. Beads is the canonical task tracker; use `bd`.

**Goal:** Give readers a trustworthy catalog and concise ways to choose Wilber's
books by contribution, intellectual phase, and subject.

**Architecture:** Preserve the chronological index and existing book URLs. Add two
Markdown guides backed by sourced book-level relationship notes. Record verified
edition relationships separately from editorial judgments about influence and overlap.

**Tech Stack:** Markdown/frontmatter, Flowershow, local Beads CLI. No application
code or new rendering framework is required for the basic pages.

## Scope and execution

Epic: `wilberwiki-at6`. Research baseline:
[research note](2026-09-14-works-reading-guides-research.md).

Recommended execution is to continue in this session, completing one bead at a time.
The same plan supports handoff without another design exercise. Read `AGENTS.md` and
`NEXT.md` first; preserve unrelated working-tree changes. Use `bd show` for current
task details and `bd update <id> --status in_progress` when starting a task. Close
only after its evidence and checks are complete. Publishing is a separate action.

Plans and audit working records belong in `docs/plans/`. Operational documentation
belongs in `docs/`. This work moves its own proposal; migration of unrelated older
planning documents is outside this change.

## Task 1 — Validate the catalog and explain reworkings

Bead: `wilberwiki-at6.1`.

Files: all existing `works/<year>-<slug>.md`, `works/index.md`; create
`docs/plans/2026-09-14-works-bibliography-audit.md` as the evidence ledger.

1. Inventory the current work pages and index rows. Establish the actual count,
   including format and draft status; do not assume the old total remains current.
2. Create a ledger row per entry: title, first publication, edition date, authorship
   role, format, source URL, related work, resolution, remaining uncertainty.
3. Verify in small chronological batches against publisher catalogs, title/copyright
   pages, author sources, and library records. Distinguish original dates from reprints.
4. Resolve the initial findings: Integral Politics format/access; Post-Truth World
   edition relationship; Integral Buddhism / Fourth Turning; Finding Radical
   Wholeness authorship and unsupported overview claims. Inspect contents or prefaces
   before estimating the extent of changes.
5. Correct book pages and corresponding index cells together. Preserve existing URLs;
   record alternate titles so readers can find either edition. Add an explicit scope
   statement that the inventory includes selected digital/audio works.
6. Add concise reader-facing relationship notes on relevant book pages and in index
   title cells, e.g. “Retitled edition of …”, “Revised edition of …”, or “Accessible
   condensation of …”. Use these labels only when supported. For substantial reworking,
   explain what changed in one or two sentences; if extent is unknown, say so.
7. Give reciprocal links where helpful. Never conflate similar subject matter with
   a retitling or abridgment. No need to impose graph metadata before visual design.

Acceptance: every catalog entry has a ledger outcome; corrections are sourced;
unresolved entries remain visibly qualified; editions are discoverable without being
presented as wholly independent contributions. Descriptions and overviews do not
contradict corrected metadata. Chronology and existing links remain intact.

## Task 2 — Explain phases and the Kosmos trilogy

Bead: `wilberwiki-at6.2`; depends on Task 1.

Files: create `works/phases.md`; update relevant book pages where a relationship
is verified; extend the audit ledger with phase/trilogy evidence.

1. Find Wilber's retrospective phase descriptions and compare scholarly accounts.
2. For each phase, record approximate dates, conceptual change, representative books,
   and what was revised from earlier work. Distinguish publication from composition.
3. Write the five-phase guide with a compact comparison table, short explanations,
   direct links to books and sources, and clear qualifications at disputed boundaries.
4. Research trilogy announcements and title changes, surviving excerpts, and explicit
   statements about reuse in later books. Recheck current publication status.
5. Add a trilogy section separating announced manuscripts, published excerpts, and
   later conceptual continuations. Provide a reading recommendation with its basis;
   do not relabel later books as numbered volumes without evidence.

Acceptance: phase assignments and historical claims are sourced; phases are not
confused with human developmental levels; incomplete evidence is visible; no unsupported
claim that a later book simply is volume II or III.

## Task 3 — Write the selective annotated bibliography

Bead: `wilberwiki-at6.3`; depends on Tasks 1 and 2.

Files: create `works/reading-guide.md`; update `works/index.md` with links to both
guides. Use existing book pages for long descriptions.

1. Compare contents/prefaces of the proposed mature-theory route and alternatives.
2. Lead with a short recommended route. For each selection explain its distinctive
   contribution, reader fit, overlap, and when to choose an alternative.
3. Add a historical route linked to the phase guide and concise subject routes for
   psychology, religion/practice, politics, science/religion, and lived experience.
4. Explain retitlings and revisions directly wherever readers might otherwise read
   both expecting different works. Distinguish modest updates, substantial revision,
   accessible restatement, and new application; unknown extent stays unknown.
5. Keep annotations around 50–100 words, shorter when possible. Do not duplicate
   full overviews or imply that every later synthesis is dispensable.
6. Review core stars against the actual recommendations. Explain their meaning;
   any change in designation needs an editorial rationale in the ledger.
7. Link the two guides from the chronological index. Keep themes within the reading
   guide and the trilogy within the phases page until length justifies another page.

Acceptance: a reader can choose a small set of major works, understand why each
adds something, and avoid accidental duplicate reading. Recommendations are identified
as editorial judgments. Every recommended book links to an existing work page.

## Verification and delivery for Tasks 1–3

- Inspect `git diff -- works NEXT.md docs/plans` and run `git diff --check`.
- Check every new local Markdown link resolves relative to its containing file.
- Compare index rows to corrected frontmatter and inspect both new guides for clarity.
- Recheck cited sources for each material factual correction. Do not mark the full
  audit complete merely because the initially suspicious titles are resolved.
- If concepts or people require edits, read the excerpt-page skill first and run
  its quote verifier. Those directories are not needed for this plan.
- Record actual content delivery in the changelog using the repository convention;
  no changelog entry is needed for this planning-only session.
- Update Beads with completed work and residual uncertainties, then update NEXT.md.
  Commit only scoped changes. Do not treat a commit as publication; follow AGENTS.md
  when production publishing is authorized. For another checkout, make both plan
  files and Beads state available; `bd dolt push` alone does not transfer Markdown.

## Task 4 — Deferred visual map of the works

Bead: `wilberwiki-at6.4`; depends on Tasks 2 and 3. This is a later design/build
project, not part of delivering the basic bibliography and guides.

Create a visually striking, useful map combining publication time, phases and
relationships between works. Explore a branching graph on a timeline rather than
assuming a strict dendrogram: books can have multiple predecessors.

Required relationship distinctions: retitled edition, revised edition, abridgment,
anthology drawn from, and conceptual development/application. Documentary relationships
and editorial inferences must have different visual treatment and cited evidence.
Show revision extent only where verified. Phase bands should admit uncertainty and
overlap; do not force every publication into a single phase solely by year.

Evaluate a static poster as well as an interactive view. The visual should support
overview, following a lineage, and selecting a book to see why it matters. Explore
theme filters and accessible labels, but avoid a dense unreadable graph. Include
mobile usability, keyboard access, non-color-only encoding, a readable text alternative,
and a shareable/exportable version. Choose implementation after visual exploration
and confirmation of the site's rendering capabilities.

Acceptance for the future task: relationships are sourced, the main conceptual
branches are legible at overview scale, edition reuse is obvious, phases can be
understood without mistaking them for exact boundaries, and the map links back to
the bibliography and guides. Web reach is an aspiration, not a promised outcome.
