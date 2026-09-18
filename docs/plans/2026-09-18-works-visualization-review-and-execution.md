# Works visualization: critical review and execution handoff

Date: 2026-09-18. Parent: `wilberwiki-at6.4`.

This is the execution addendum to the
[research/design plan](2026-09-17-wilber-works-visualization-research-and-design.md).
It records the critical review, model recommendations, and new-session procedure.
Where they differ, this addendum supersedes the earlier task instructions.
Beads is authoritative for status and dependencies; this document explains the work.

## Actual state

- Initial ontology completed in `wilberwiki-at6.4.1`, commit `b884bd9`:
  [ledger](2026-09-17-works-concept-lineage-data.yaml), 18 concept families,
  13 catalog works, two provisional excerpt targets, three cited IP examples.
- That commit was first made on `research/pilot-ontology` in a secondary checkout.
  It has now been fast-forwarded into local `main`; the files are in this project's
  normal `docs/plans/` directory. No site publication was performed.
- Contract-hardening deliverables for `wilberwiki-at6.4.8` are now implemented:
  ledger version 2, explicit comparative records, `expounds`, required date basis,
  and a reusable validator with positive/negative fixtures. See
  [maintenance and validation](../works-concept-lineage.md). Beads records task status.
- The attempted A Sociable God/IP comparison remains explicitly unresolved: the
  inspected IP retrospective points to a 1983 grid, but the original earlier passage
  is not locally available. The finding records evidence and the next research action;
  it is not entered as a lineage edge. No new historical priority claim is established.
- Corpus research, prototypes, visual styling, and production implementation remain
  unfinished. The initial ledger is not an approved historical genealogy.

## Critical review and required follow-up

Keep the research-before-design sequence and Rufus's decision gate. Strengthen the
model before scaling research: it currently describes concept occurrence more clearly
than change between formulations.

### 1. Explicit comparative claims

Add a small collection linking earlier and later appearance IDs, with an account of
what changed and evidence for both formulations. Existing appearance records can act
as the formulations; avoid building a large separate ontology. Define the structure
of `comparison_basis` rather than leaving it as an unspecified prose convention.
Recurrence, chronology, and semantic similarity do not establish inheritance.

### 2. Exposition versus contribution

Introduce a neutral `expounds` role for substantial treatment with undetermined
historical novelty. Reserve `develops` for a supported addition relative to a named
earlier formulation. Reassess the two IP seed records accordingly. Insufficient
comparison is not evidence of `restates`; that role needs positive support too.

### 3. Consistent schema and representative validation

The current required fields include `work`, while another rule permits `source_unit`
instead. A read-only check reproduced this contradiction. Require exactly one target.
Retain a reusable validator and representative valid/invalid cases for catalog and
excerpt appearances, terminology, comparisons, and edition relationships. Synthetic
test fixtures must be clearly separate from historical evidence.

The three seed examples all concern one book and only two roles. Check at least one
real cross-work comparison before broad extraction, or record precisely why evidence
cannot establish it. Never invent a claim to satisfy a record quota.

### 4. Historical dates and consequential claims

Record each historically consequential claim's date basis: original edition verified,
later edition only, retrospective attribution, or unresolved. A work's first-publication
year must not automatically date material found only in a revised edition.
Distinguish confidence in a passage's meaning from confidence in the historical
comparison, using separate records/assessments where necessary.

Task 4 must directly review every origin, revision, and integration claim driving the
overview. Spot-checking may supplement that review for routine supporting records.
Source presence and exact quote matching do not alone establish entailment.

### 5. Bounded, question-led research

Tasks 2 and 3 begin with source-access inventories for every assigned work/excerpt.
The 18 families and 13 works imply 234 possible intersections before edition work;
an exhaustive populated matrix is not required. Prioritize these questions:

1. What changed from the early spectrum account to developmental growth?
2. What did differentiated lines add to levels?
3. How did quadrants broaden the earlier developmental architecture?
4. What changed in later accounts of states, perspectives, and post-metaphysics?

For the questions assigned to each pass, deliver supported findings or explicit
unresolved findings, with consulted editions, locators, and source gaps. After an
initial access search, document unavailable sources and continue with accessible
evidence; do not let repeated retrieval attempts substitute for research progress.
The audit decides whether the available claims support the proposed visualization.
Retain the eighteen families as a research vocabulary without filling every cell.
Treat Wilber I–V as an interpretive framework, including author retrospection, not
a predetermined historical conclusion that the research must confirm.

### 6. Fair prototype evaluation

Compare equivalent states: whole-view structures as overviews, focused genealogy as
a focus state. Do not penalize a focused view for failing to be an entire overview.
All use the same audited data and a fixed set of reader questions. Record correct
answers, misunderstandings, and whether interaction was needed. Include checks that
missing evidence is not read as absence and connecting lines are not read as influence.
The matrix remains a genuine candidate. A stream map is a hypothesis, not the default
winner. Neutral structural prototypes belong to Task 5, after the audit; polished
styling and production implementation remain behind Rufus's Task 6 decision.

## Execution order and model recommendations

These are workload recommendations, not benchmark claims or automatic model routing.
They were informed by the official [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra)
and [Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol) documentation
checked on 2026-09-18. Astra supports both research and coding; Sol is an efficiency
choice for bounded work, not a mandatory coding handoff. Use the exact model/effort
available in the runtime and report any substitution. Do not claim a review used a
particular model unless the session selection or explicit agent configuration supports it.

| Stage / Bead | Suggested model and reasoning effort | Deliverable / responsibility |
|---|---|---|
| Contract hardening, `.4.8` | Astra High | Implement review items 1–4 at schema level; validator and a checked comparison or explicit gap. |
| Source discovery/extraction, `.4.2` and `.4.3` | Sol Medium | Edition/access inventory, candidate passages, precise locators, evidence gaps. |
| Cross-work interpretation, same research Beads | Astra High | Assess continuity, additions, revisions, retrospective naming, and uncertainty. |
| Dataset audit, `.4.4` | Astra XHigh | Challenge every consequential historical claim against evidence; approve or downgrade claims. |
| Neutral prototypes, `.4.5` | Sol High; Astra High reviews | Deterministic structures; fair evaluation of explanatory performance. |
| Architecture decision, `.4.6` | Rufus, assisted by Astra High | Explicit human choice, recorded tradeoffs, and approved states. |
| Technical spike/implementation plan, `.4.7` | Sol High | Platform, rendering, export, accessibility, and implementation specification. |
| Later production implementation | Sol High; Astra High for difficult design decisions | Separate approved implementation plan; not authorized by this research handoff. |

Use High for consequential judgment, Medium for bounded extraction, XHigh for the
concentrated audit. Max is not the default. Missing primary evidence cannot be repaired
by increasing reasoning effort. Keeping Astra High throughout is also reasonable if
model switching is inconvenient and cost is secondary.

Dependency order: `.4.1` (done) → `.4.8` → `.4.2` and `.4.3` → `.4.4` → `.4.5`
→ `.4.6` (Rufus decision) → `.4.7`. Task suffixes do not determine execution order.

## One lead session with optional sub-agents

A lead Astra High session can coordinate the whole research workflow when asked to
execute it, subject to runtime availability and the Task 6 human gate. This document
describes that option; it does not itself start agents or authorize production work.

- The lead reads project instructions, checks dependencies, claims the appropriate
  Bead, assigns bounded work, reviews evidence, validates and integrates results,
  commits deliverables, and updates Beads. Delegation does not transfer accountability.
- After `.4.8`, early and later research can run independently. Give agents separate
  files or worktrees; never have both rewrite the canonical YAML simultaneously.
  The lead integrates their records and resolves ID or interpretation conflicts.
- Extraction assignments must include corpus boundaries, the contract version,
  required evidence fields, explicit exclusions, output location, model/effort, and
  completion checks. Tool/API support must actually allow a model override; metadata
  in Beads does not configure runtime model selection.
- An audit pass should re-open the cited source passages and challenge the claims,
  not merely summarize the extraction agent's reasoning. Fresh review context can
  reduce anchoring, but is not a substitute for verification.
- Delegation can be sequential if parallel agents or model selection are unavailable.
  Report the actual arrangement. Do not imply that a background agent is running
  between sessions unless the product has actually scheduled persistent work.
- Stop at `.4.6` for Rufus's decision. Do not interpret silence as approval.

## New-session handoff

1. Read `AGENTS.md`, `NEXT.md`, the original plan, this addendum, and the ledger.
2. Run `bd ready`, `bd show wilberwiki-at6.4`, and `bd children wilberwiki-at6.4`;
   use current dependencies and status to select a ready task.
3. Check Git status and where the latest commits exist. Keep changes in the project's
   `docs/plans/` regardless of which checkout is used. A worktree is temporary execution
   infrastructure; its external pathname must not be the only handoff reference.
4. For each completed task, record artifacts, commit, validation results, source gaps,
   and actual model arrangement in Beads; use `bd dolt push` for cross-checkout sync.
5. Integrate completed work into the user's main local checkout as part of handoff
   when safe; preserve unrelated changes. Ask only for genuine conflicts or authority
   changes. Pushing Git `main` publishes production and is a separate action.

Suggested prompt for a future execution session:

> Continue the works-visualization research from NEXT.md and the September 18 review
> addendum. Use Astra High as lead where available. Execute the next ready Bead and
> delegate bounded extraction to Sol Medium where useful, reporting actual model
> choices. Validate and commit the deliverables and update Beads. Keep work in this
> project's docs/plans and bring completed changes into the main local checkout.
> Do not publish or begin polished styling/production implementation. Stop for my
> architecture decision at wilberwiki-at6.4.6.
