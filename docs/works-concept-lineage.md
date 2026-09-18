# Maintaining the works concept-lineage ledger

The research ledger is
[`plans/2026-09-17-works-concept-lineage-data.yaml`](plans/2026-09-17-works-concept-lineage-data.yaml).
Its version-2 `contract` and controlled vocabularies define the record shapes.
Execution scope and model recommendations live in the
[review handoff](plans/2026-09-18-works-visualization-review-and-execution.md);
Beads owns current status and dependencies.

From the repository root, run:

```sh
ruby scripts/validate_lineage.rb
ruby scripts/test_lineage_validator.rb
```

The tools use Ruby's YAML library and Minitest (verified with the system Ruby 2.6).
To validate a candidate ledger elsewhere, pass its path and the repository root:

```sh
ruby scripts/validate_lineage.rb /absolute/path/to/candidate.yaml /absolute/path/to/wilber-wiki
```

The validator checks unique IDs, existing local work/source files, record fields,
controlled values, targets, date shapes, comparative endpoints and evidence coverage,
and exact local verification excerpts. It exits nonzero on invalid input. Tests create
explicitly synthetic records in temporary files, including valid and invalid excerpts,
comparisons, terminology, and edition relationships. They are not corpus evidence.

## Research rules

- Give each appearance exactly one `work` or `source_unit` target. Register sources
  with edition details, a local path or external URL, and a citation. An external
  URL's content/accessibility is not verified automatically.
- Use `expounds` for substantial treatment when historical contribution is unknown.
  `develops`, `revises`, `restates`, and `applies` need matching `comparison_ids`.
  Every comparison references earlier appearance IDs and one later appearance,
  with evidence marked `supports: <appearance-id>` for every endpoint. Its confidence
  assesses the historical interpretation separately from the appearance's confidence.
- `introduces` requires `priority_basis`: a nonempty list of `examined_targets`
  (objects with one `work` or `source_unit`), `search_method`, and `remaining_gaps`.
  Even an empty gap list does not certify universal priority; scope stays limited.
- Every appearance, term, comparison, and work relationship has a `date` with `basis`,
  `year`, and `reason`. Unknown years stay null. `unresolved` cannot have a year;
  `original-edition-verified` must have one. Date evidence still requires human review.
  The script never copies a publication year from a work into an assertion.
- Integration within a book identifies `integrates_concepts`; claiming historical
  integration of earlier formulations additionally requires an evidenced comparison.
- Work relationships describe edition/reuse facts separately. If `revision_extent`
  is `compared`, supply `comparison_citation` to the actual comparison, not a guessed
  magnitude of revision.
- Keep unsupported cross-work hypotheses in `unresolved_findings`, with the checked
  evidence, missing evidence, and next research action. They do not create graph edges.

## Limits of automated checks

Passing validation is not approval for publication or for an overview-visible edge.
The script checks structure and source occurrence, not whether a citation entails a
claim, whether editions are correctly identified, or whether historical direction is
justified. Known reversed endpoint years are rejected; unknown years require review.
In particular, two citations from the same source can pass structural checks while
failing historical scrutiny. Task `wilberwiki-at6.4.4` must inspect every consequential
origin, revision, or integration claim against the actual passages and editions.
