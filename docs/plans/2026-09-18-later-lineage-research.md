# Later concept-lineage research: initial pass

Date: 2026-09-18. Bead: `wilberwiki-at6.4.3`, in progress.
Contract: version 2. Scope: Task 3 only; no prototypes, styling or publication.

This pass begins the question-led research required by the
[execution handoff](2026-09-18-works-visualization-review-and-execution.md).
It adds nine appearances, one terminology record, one provisional comparison and
five unresolved findings to the [ledger](2026-09-17-works-concept-lineage-data.yaml).
The three previous IP appearances and earlier-research gap are preserved.
These are candidates for audit, not approved historical edges.

## Source access and editions

All six assigned catalog works and both provisional excerpt targets were inventoried.
Local wiki sources, the explicitly identified sibling-library source, existing work
pages and their linked records were checked. A bounded web search used author,
publisher and excerpt titles; no exhaustive acquisition effort was attempted.

| Target | Available and inspected | Edition/access limitation | Consequence |
|---|---|---|---|
| SES | Local full text, chapter 4, The Four Quadrants; copyright/cataloging page | Second edition; copyright 1995, 2000; original uncollated | Supports the fourfold architecture in this text, not an invention date of 1995 |
| A Brief History of Everything | [2007 Shambhala reprint record and contents](https://books.google.com/books/about/A_Brief_History_of_Everything.html?id=c9shMX7HLY0C), chapters 5–6 identified | No substantive primary passage inspected; no local copy found | No exact SES restatement/abridgment claim |
| Integral Psychology | Local ebook; chapter 9 note 15, chapter 12 note 12, existing chapter 14 note 20 record | EPUB metadata 2011; original print uncollated | Direct exposition and labeled author retrospection; no inferred first appearance |
| Integral Spirituality | Existing checked 2011 ebook transcription; introduction, selected chapters 1, 3, 4 and Appendix II opening | Copyright 2006 does not date the wording to 2006 | Seven exact selections retained in this wiki with provenance; original-edition comparison remains open |
| The Religion of Tomorrow | [Publisher-hosted author introduction](https://www.shambhala.com/future-religion-excerpt-ken-wilber/), particularly growth/awakening passages | Initial retrieval failed; later retrieval succeeded. Full chapters unavailable locally; online excerpt not collated to 2017 print | Supports the stated religious program only |
| Finding Radical Wholeness | [Publisher description](https://www.shambhala.com/finding-radical-wholeness.html) through indexed search | Direct retrieval failed; no primary book passages or local full text | Publisher positions it around five aspects of wholeness; detailed additions and overlap unknown |
| Kosmos II Excerpt A | [Integral Life hosted PDF](https://integral-life-home.s3.amazonaws.com/Wilber-AnIntegralAgeAtTheLeadingEdge.pdf), 203 pages; chapter 5 opening, printed pp. 177–178; p. 143 reference checked | Hosted version undated; reference to Integral Life Practice makes unchanged early-release dating unsafe | Methods/enactment appearance with unresolved date; no A→IS historical edge |
| Kosmos II Excerpt C | [Search-indexed mirror PDF](https://www.integralesforum.org/attachments/KKC_Excerpt_C.pdf) located; secondary roadmap used only for discovery | Direct PDF retrieval failed; body and edition not inspected | Access lead only; no appearance inferred from title or contents |

The earlier assumption that only reader notes were available for *Integral
Spirituality* is corrected. Its checked transcription already existed in the private
library; this pass reads that available source and retains only selected evidence in
[a self-contained source note](2026-09-18-integral-spirituality-source-selections.md).
The ledger has no external local-file paths or private-repo runtime dependency.
No full text or images were imported. The provenance hash identifies the inspected
transcription; it does not certify the original print edition.

## Findings and comparative limits

**Quadrants broaden the dimensions described.** SES chapter 4 explicitly crosses
individual/social with interior/exterior and discusses their correlation. IP's
chapter 9 note 15 retrospectively describes phase IV as adding quadrant dimensions
to levels and lines. That is an author's historical account; an independently
supported phase-III→IV change still needs earlier endpoints from Task 2. IS chapter 1
then explicitly describes inside/outside views of each quadrant. We record that
formulation without asserting that SES lacked it or that IS invented it.

**State/structure differentiation predates its later named presentation in the
works' publication order, but the passage dates remain unverified.** IP chapter 12
note 12 describes states interpreted through developmental structures. IS chapter 4
states the same relation while naming the Wilber-Combs Lattice. The ledger records
a narrow `retains` comparison, with medium confidence and an unresolved date. This
does not certify original-edition chronology, the entire lattice's equivalence, or
influence between the authors. The separate terminology record establishes the name
in the inspected 2011 ebook only. IS also distinguishes trained state sequences
(`state-stages`) from `structure-stages`; this warrants a separate appearance.

**Later methods and post-metaphysics are explicit programs.** IS connects eight
perspectives to methods and proposes an account of levels without metaphysical
thinking. The inspected Excerpt A also connects AQAL dimensions with methods that
enact their objects. These are supported expositions. Calling either a revision of
a specific earlier Wilber proposition requires paired evidence still to be selected;
chronological resemblance alone is insufficient. Excerpt A's release/version history
also prevents placing its inspected wording confidently before IS.

**Later synthesis remains only partly accessible.** The Religion of Tomorrow
introduction proposes bringing developmental growth into religious practice alongside
awakening. The Radical Wholeness publisher description identifies a practical
five-part organization. Neither source establishes the extent of novelty or reuse.
No sixth phase, exact-overlap claim or unsupported `applies` edge was added.

## Source-dependent blockers in Beads

| Bead | Missing evidence | Claims blocked |
|---|---|---|
| `wilberwiki-at6.4.3.1` | Edition-identified Brief History chapters 5–6 and detailed Religion of Tomorrow / Radical Wholeness comparison passages | Specific restatement, additions and later synthesis/overlap claims |
| `wilberwiki-at6.4.3.2` | Inspectable Excerpt C and dated version history for both A and C | Dated Kosmos II→IS methods/perspectives lineage |
| `wilberwiki-at6.4.3.3` | Original-edition counterparts for SES/IP/IS selections; phase-III endpoints coordinated with Task 2 | Historical priority, verified transition dates, and promotion of provisional continuity to a dated edge |

These are blockers for the named claims, not reasons to stop all research. Parent
`.4.3` remains in progress. No dependency on the private library's acquisition tasks
is introduced. Unavailable evidence is represented by unresolved findings rather
than inferred absence or invented edges.

## Next bounded work

1. Use available SES/IP passages to select explicit earlier ontology claims for
   comparison with IS Appendix II. Decide whether they support retention,
   qualification or revision; leave unproved comparisons unresolved.
2. Compare quadrant/perspective formulations more fully and coordinate the earlier
   developmental bridge with Task 2. Keep editions distinct.
3. Resolve the source tasks when evidence becomes available, or hand the audit a
   deliberately limited corpus with those claims excluded. Source completion is
   not required to manufacture an exhaustive matrix.
4. Review every proposed historical comparison before completing Task 3 and passing
   the combined dataset to `.4.4`. No visual work is authorized by this pass.

## Verification and execution arrangement

One Codex GPT-6 lead session performed discovery, extraction and interpretation;
no subagents or Sol extraction pass were used. No separate model-effort configuration
was verified, so no such review is claimed. Work was isolated on
`research/later-lineage` and is handed back through tracked project files.

Validation commands: `ruby scripts/validate_lineage.rb`,
`ruby scripts/test_lineage_validator.rb`, and `git diff --check`.
A separate exact-string check compared all seven selected blockquotes against the
hashed IS transcription and checked their line locators. Structural validation and
quote occurrence do not certify historical entailment; `.4.4` remains the audit gate.
No reader-facing changelog entry is added because this is an initial internal
research pass and nothing has been published.
