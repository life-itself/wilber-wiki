# Wilber Works Visualization — Research and Design Plan

Date: 2026-09-17. Status: shaping; job stories accepted, visual form not selected.
Parent Bead: `wilberwiki-at6.4`.

> **For implementers:** Use `superpowers:executing-plans` to execute the Beads in
> dependency order. Do not start production visualization code until the research
> dataset and structural-prototype decision are complete.

**Goal:** Develop a source-grounded, visually compelling account of how Wilber's
system of ideas emerged, changed, combined, and moved through his books, with a
canonical view that works as a standalone share image and an interactive version
that rewards exploration.

**Architecture hypothesis:** Books are evidence-bearing containers; concepts are
the evolving units. Use one structured evidence ledger to generate both a composed
overview and interactive concept/book focus states. Preserve chronology, but do not
assume that a conventional linear timeline is the right visual form.

**Likely delivery medium:** Data-driven SVG on the web, capable of deterministic
high-resolution export. This remains a hypothesis until the prototype-selection task.

---

## 1. Why this plan exists

The initial task proposed a visual timeline of works, phases, themes, and book
relationships. A first visual exploration produced polished timeline/poster concepts,
but Rufus rejected all of them. They styled the bibliography before establishing the
visualization's analytical purpose and the data needed to support its claims.

The reset is deliberate:

1. Define the jobs the visualization must perform.
2. Establish what evidence exists and what must be researched.
3. Build a small, auditable concept-to-work dataset.
4. Compare structural visualization models using the same real data.
5. Select a form only after seeing which questions each model answers.
6. Write a separate implementation plan for the selected form.

The rejected comps under `.impeccable/mocks/decision/` are exploration history, not
an approved visual direction and not an implementation reference.

## 2. Situation, complication, question

### Situation

The site now has a validated 40-entry works catalog, a selective reading guide, and
a sourced overview of Wilber I–V. Readers can browse publications chronologically and
read prose about major changes in Wilber's thought.

### Complication

Those pages do not make the system's development visible. A list of books cannot show
which concepts recur, combine, change names, receive fuller formulation, move into new
domains, or disappear. At the same time, the current concept dataset cannot yet support
a corpus-wide visualization: all 45 concept pages draw from only *Sex, Ecology,
Spirituality* (1995) and *Integral Psychology* (2000). Plotting those pages as though
they represented 1977–2024 would manufacture a phase-IV origin story.

### Question

How can the project create a memorable and shareable visual account of the evolution
of Wilber's thought while ensuring that every claim about emergence, revision,
inheritance, or application is traceable to evidence and appropriately qualified?

## 3. Job stories

### Primary analytical job

> When I encounter Wilber's large body of work, I want to see what ideas emerged,
> what changed, and what became integrated, so I can understand the shape of his
> intellectual project rather than treating every publication as equally important.

### Concept-tracing job

> When I encounter a concept such as quadrants, the pre/trans fallacy, developmental
> lines, or integral post-metaphysics, I want to see its earliest confirmed occurrence,
> major formulations, revisions, and later applications across the works.

### Book-contribution job

> When I select a book, I want to see which ideas it carries forward and what it adds,
> revises, integrates, applies, restates, or merely republishes.

### Change-comparison job

> When two works appear to present different versions of the theory, I want to see
> what was retained, rejected, differentiated, or added and what evidence supports
> that interpretation.

### Sharing job

> When I want to introduce this intellectual history publicly, I want one striking,
> self-contained image that reveals a meaningful pattern and invites people into the
> explorable, sourced version.

The sharing job is a distribution requirement, not a substitute for the analytical
job. A beautiful image with no defensible visual argument fails.

## 4. Why use a visualization at all?

The visualization should expose relationships that are difficult to hold in prose:

- coexistence of multiple concepts at one moment;
- first confirmed appearance versus later explicit naming;
- persistence, recurrence, combination, branching, and revision;
- the difference between a new theoretical contribution and an application,
  introduction, anthology, revised edition, or retitling;
- approximate phase changes without forcing every book into a hard interval;
- an overview/detail transition from the whole system to one concept or book.

If the researched data cannot support these comparisons, the correct deliverable is
an improved editorial diagram or matrix, not a misleading genealogy.

## 5. Current data audit

### Strong enough to use

- `works/catalog.md`: 40 title/edition entries in chronological order.
- `docs/plans/2026-09-14-works-bibliography-audit.md`: dates, roles, formats,
  edition relationships, evidence, and residual uncertainty.
- `works/phases.md`: five phases, representative books, transition explanations,
  approximate boundaries, and the unfinished Kosmos trilogy.
- `works/reading-guide.md`: editorial judgments about major contributions,
  introductions, applications, overlap, and reading routes.
- `assets/covers/`: 28 cached cover images with provenance in `SOURCES.md`.

### Partial

- Documented work relationships: two retitled-edition pairs, the relationship from
  *The Fourth Turning* to *The Religion of Tomorrow*, SES to *A Brief History of
  Everything*, plus several anthology/application relationships.
- Phase assignment: representative works are supported, but every catalog entry is
  not mechanically assigned to exactly one phase, intentionally.
- Later concepts: `notes/2019-integral-spirituality-notes.md` provides a reader's
  account, not a substitute for primary-text verification.

### Not yet sufficient

- `concepts/` has 45 pages, but their `works` fields name only SES and *Integral
  Psychology*.
- Only those two books have full text locally.
- The project has not established corpus-wide first appearances for concepts.
- Concept-to-work roles are prose judgments, not structured data.
- Confidence and evidence are not encoded per conceptual relationship.
- The catalog is not exhaustive of articles, forewords, talks, and pseudonymous work;
  “first appearance” cannot silently mean “first ever in any Wilber publication.”

## 6. Research scope

### Pilot works

Use a phase-spanning corpus large enough to test the model but small enough to audit:

- Phase I: *The Spectrum of Consciousness*; *No Boundary*.
- Phase II: *The Atman Project*; *Up from Eden*.
- Phase III: *A Sociable God*; *Eye to Eye*; *Transformations of Consciousness*.
- Phase IV: *Sex, Ecology, Spirituality*; *A Brief History of Everything*;
  *Integral Psychology*.
- Phase V: selected Kosmos II excerpts; *Integral Spirituality*;
  *The Religion of Tomorrow*.
- Late practical synthesis, as a test case rather than an assumed new phase:
  *Finding Radical Wholeness*.

If primary text cannot be obtained for a pilot work, record the gap and use prefaces,
contents, publisher excerpts, author retrospectives, and high-quality scholarship
without pretending they establish detailed textual claims.

### Pilot concepts

Finalize a controlled list during the schema task. Candidate families include:

- spectrum/levels of consciousness;
- return-to-unity versus developmental growth;
- pre/trans fallacy;
- structures, states, stages, lines/streams, and types;
- the self-system;
- evolution and involution;
- holons and holarchy;
- the four quadrants and the Big Three;
- AQAL as an integrating formulation;
- perspectives, zones, and integral methodological pluralism;
- state-stage relations / the Wilber–Combs lattice;
- integral post-metaphysics;
- integral practice and later formulations of wholeness.

The pilot should prefer 12–18 concepts that explain the major transitions. It should
not inherit all 45 current concept pages merely because they already exist.

## 7. Evidence and data model

Create a human-auditable YAML research ledger at:

`docs/plans/2026-09-17-works-concept-lineage-data.yaml`

The pilot schema should contain:

```yaml
concepts:
  - id: four-quadrants
    label: Four quadrants
    aliases: [quadrants, AQAL quadrants]
    definition: Short editorial definition.

appearances:
  - concept: four-quadrants
    work: 1995-sex-ecology-spirituality
    role: introduces
    claim: First major book-length formulation in the examined corpus.
    evidence:
      kind: primary-text
      citation: "Sex, Ecology, Spirituality, chapter …"
      locator: "…"
    confidence: high
    scope: examined-corpus

work_relationships:
  - from: 2014-the-fourth-turning
    to: 2018-integral-buddhism
    type: retitled-edition
    evidence:
      kind: bibliographic-record
      citation: "…"
    confidence: high
```

### Controlled concept-to-work roles

- `introduces`: earliest confirmed substantive formulation in the examined corpus.
- `develops`: adds substantial distinctions, argument, or structure.
- `revises`: explicitly changes or rejects part of an earlier formulation.
- `integrates`: combines previously separate concepts into a larger architecture.
- `applies`: carries an existing framework into a new subject or practice.
- `restates`: makes an existing formulation more accessible without a demonstrated
  major theoretical change.
- `mentions`: present but not substantively developed; normally hidden from the
  overview.

Retitling, revision, abridgment, anthology extraction, and edition identity belong in
`work_relationships`, not in the conceptual-role vocabulary.

### Evidence rules

- Every material node and edge needs a citation and a short rationale.
- Use `high`, `medium`, or `low` confidence with a recorded reason.
- Distinguish primary text, author retrospective, bibliographic fact, independent
  scholarship, and editorial inference.
- Use “earliest confirmed in the examined corpus” unless broader priority is proven.
- Record terminology changes separately from conceptual emergence.
- Do not infer influence from semantic similarity.
- Unknown revision extent remains unknown.
- The research ledger may contain short verification excerpts, but the public map
  should cite sources rather than publish source-book text by default.

## 8. Relevant precedents

### Stemma — sourced idea genealogy

<https://stemmascience.org/>

Closest methodological precedent. Time runs across a structured field of thematic
lanes; node and link types are explicit; each connection carries sources, confidence,
and disputed status. Take the evidence discipline and focus behavior, not its exact
visual styling.

### Histomaps — continuous streams and share export

<https://histomaps.org/>

Treats history as streams that persist, divide, merge, and end. The project explicitly
calls its geometry an argument, supports overview plus semantic zoom, and includes a
dedicated share-graphic action. This is the strongest precedent for a top-down map
whose resting state is also a composed image.

### The Shape of Song — recurrence over a sequence

<https://www.bewitched.com/song.html>

Arc diagrams reveal repeated structures across time and work both interactively and
as prints. Potentially useful for a concept-focused view showing recurrence across
books; not a sufficient whole-system overview on its own.

### Map of Philosophy — semantic versus influence maps

<https://thephilosophymap.com/>

Offers separate semantic and influence layouts. This distinction is essential:
conceptual similarity and historical development must not be encoded as the same edge.
Its unlabeled overview also demonstrates that an explorable spatial map can make a
weak standalone screenshot.

### History of Philosophy — proposition graph

<https://www.denizcemonduygu.com/philo/browse/>

Connects individual philosophical statements through agreement and disagreement.
The full view is visually arresting but becomes an unreadable hairball. Use it as a
warning against showing every concept relationship simultaneously.

### Origin of Models — artifacts carry ideas

<https://originofmodels.com/>

Separates models from the ideas they carry and offers timeline, genealogy, library,
and focused views over the same subject. The useful analogy is books as artifacts and
concepts as the evolving units, not its biological rhetoric or visual treatment.

## 9. Structural hypotheses to prototype

All prototypes must use the same pilot data and neutral visual styling. They are tests
of explanatory structure, not aesthetic directions.

### A. Top-down concept-stream map

Time flows from top to bottom. Concept streams persist through time; books are moments
where streams enter, split, combine, change, or move into an application. Approximate
phase transitions form horizontal regions.

Strengths: preserves temporal change, supports an overall gestalt, and can transform
into an interactive concept focus. Risks: stream width can imply an unsupported
measure; crossings and labels may become dense.

### B. Book × concept score

Books form chronological rows and concepts form columns. Intersection glyphs encode
introduces, develops, revises, integrates, applies, and restates. Lines can connect a
concept down the score to show persistence and recurrence.

Strengths: most auditable and screenshotable; missing evidence stays visible. Risks:
can look like a reference table rather than an arresting visual argument.

### C. Focused genealogy / mind map

A selected concept becomes the root of a directed acyclic graph containing antecedent
formulations, related concepts, major book appearances, revisions, and applications.

Strengths: directly answers “show me the history of this idea.” Risks: the complete
overview becomes a hairball and chronology becomes secondary. Treat this as a likely
focus state, not an assumed default.

### Working product hypothesis

A top-down concept-stream overview becomes a focused genealogy when a concept is
selected and is backed by a matrix-like accessible data view. This is not an approved
design; the prototypes must be allowed to disprove it.

## 10. Sharing and export requirements

- The resting overview must already be a coherent, titled composition without hover.
- A canonical export should be produced from the same data and geometry as the web
  view, not separately redrawn.
- A selected concept should generate a second composed share state with title,
  selection, compact legend, evidence-status key, and canonical URL.
- Export should be explicit (“Make share graphic” or equivalent), not dependent on
  accidental browser screenshots.
- The chosen view must survive both wide desktop display and a legible social image;
  interaction controls should not dominate the export.
- A readable chronological/text alternative remains required.

## 11. Issue tree and execution order

### Research foundation

1. `wilberwiki-at6.4.1` — lock job stories, pilot concepts, source corpus, and
   schema.
2. `wilberwiki-at6.4.2` — research concept emergence and revision in phases I–III.
3. `wilberwiki-at6.4.3` — research concept integration and later development in
   phases IV–V.
4. `wilberwiki-at6.4.4` — consolidate and audit the pilot evidence ledger.

Tasks 2 and 3 can run independently after task 1. Task 4 depends on both.

### Structural design

5. `wilberwiki-at6.4.5` — produce three neutral prototypes from the same validated
   pilot data.
6. `wilberwiki-at6.4.6` — evaluate them against the job stories and choose or
   combine a structure.

### Implementation preparation

7. `wilberwiki-at6.4.7` — test rendering/export feasibility in the actual Flowershow
   environment and write the production implementation plan.

No visual styling, generated poster comps, or production renderer should precede the
prototype-selection decision.

## 12. Task specifications

### Task 1 — Define the pilot ontology and evidence contract

**Outcome:** A valid initial YAML ledger containing the controlled concept list, pilot
work list, relationship vocabulary, source categories, confidence rules, and at least
three fully evidenced example relationships.

**Files:** Create
`docs/plans/2026-09-17-works-concept-lineage-data.yaml`; update this plan only if
the schema changes.

**Constraints:** Do not research the whole corpus yet; do not call a semantic
similarity an influence; do not use unqualified “first appearance.”

**Verification:** Parse the YAML; validate unique IDs, allowed roles/confidence, known
work slugs, and required evidence fields with a small script or one-off command whose
result is recorded in the Bead.

### Task 2 — Research phases I–III

**Outcome:** Evidence-backed appearance records for the agreed concepts in the seven
pilot works from 1977–1987, including explicit revisions from the early spectrum to
the developmental and differentiated-lines accounts.

**Context:** `works/phases.md`; relevant work pages; Wilber's retrospective in local
*Integral Psychology*; primary texts/prefaces where obtainable.

**Constraints:** Record source gaps; distinguish publication date from composition;
do not extrapolate from later retrospective vocabulary without labeling it.

### Task 3 — Research phases IV–V

**Outcome:** Evidence-backed appearance records for the pilot works from 1995 onward,
including quadrants/AQAL, differentiation of states/structures/lines, perspectives and
methods, post-metaphysics, state-stage relations, and later application/synthesis.

**Context:** Local SES and *Integral Psychology* full texts; `works/phases.md`;
`works/reading-guide.md`; primary excerpts/prefaces for phase-V works.

**Constraints:** Existing concept pages are leads, not complete coverage; do not
present the 2006 vocabulary as proof that every underlying distinction began in 2006.

### Task 4 — Audit and freeze the pilot dataset

**Outcome:** One internally consistent pilot ledger with duplicate concepts resolved,
terminology history recorded, claims spot-checked, uncertainties visible, and a short
coverage report stating what the dataset can and cannot support.

**Verification:** Every overview-visible appearance and work relationship has evidence;
all referenced work slugs exist; every role is from the controlled vocabulary; the
coverage report identifies missing primary sources and examined-corpus limits.

### Task 5 — Build neutral structural prototypes

**Outcome:** Three grayscale, data-driven prototypes—stream map, score/matrix, and
focused genealogy—using identical pilot data, each with a static whole-view image and
a short interaction note.

**Constraints:** No polished aesthetic world; no generated imagery; no invented data;
no force-directed graph whose layout changes between renders.

**Evaluation prompts:** Can a reader locate a phase change, trace one concept, explain
one book's contribution, distinguish fact from inference, and understand the image
without operating it?

### Task 6 — Select the information architecture

**Outcome:** A recorded decision selecting one structure or a clearly specified
combination, with rejected alternatives and tradeoffs preserved.

**Required review:** Rufus evaluates the three prototypes. This task is not autonomous;
do not infer approval from silence.

**Acceptance:** The decision identifies the default overview, concept-focus state,
book-focus state, text alternative, and share/export states.

### Task 7 — Technical spike and implementation plan

**Outcome:** Evidence that the selected structure can render in the site's real
Flowershow environment, plus a separate implementation plan with exact files, tests,
responsive behavior, keyboard behavior, export mechanics, and rollout steps.

**Constraints:** Preserve `works/catalog.md`; do not publish; do not introduce a large
framework before a small SVG/data spike proves it necessary.

**Likely checks:** deterministic SVG render; stable layout from YAML/JSON; desktop and
mobile inspection; keyboard focus; non-color encoding; static export; text fallback;
local-link validation; `git diff --check`.

## 13. Definition of success

Research/design is complete when:

- the visualization's primary and secondary jobs are explicit;
- the pilot dataset supports its visible claims with sources and confidence;
- “earliest confirmed” scope is honest;
- three structural models have been tested on the same data;
- Rufus has selected the information architecture;
- the static share view and interactive focus states are both specified;
- a new session can begin the technical plan without reconstructing this history.

Production is explicitly outside this plan until those conditions are met.

## 14. New-session handoff

Start with:

1. `AGENTS.md`, then `NEXT.md`.
2. `bd show wilberwiki-at6.4` and `bd children wilberwiki-at6.4`.
3. This plan.
4. `docs/plans/2026-09-14-works-bibliography-audit.md`.
5. `works/phases.md`, `works/reading-guide.md`, and `works/catalog.md`.

Claim only the first ready child Bead. Do not return to visual styling until the
dependency chain reaches the prototype task.
