# Annotatable Reading Layer — Vision

Status: vision, not a design. Deliberately undesigned — this doc exists so the idea
isn't lost or accidentally foreclosed while the [concept wiki](concept-wiki-vision.md)
is built first, not because it's less real.

This is the second of two related but distinct pieces of work identified for
wilber-wiki. The concept wiki is the priority right now; this doc holds the vision for
later.

## Thesis

Separate from wanting a concept-level index over Wilber's ideas, there's a wish to make
the actual texts readable on the web with a commentary layer attached directly to
passages — not a summary or an index standing apart from the work, but the work itself,
annotated. Personally, that means being able to comment on specific passages as you read
them, the way you would mark up a physical book, but persistently and in a form that can
be shared. Beyond that, it's also a form of collective sense-making: what other readers
notice and highlight in a text this dense and this open to interpretation is itself
interesting — worth being able to see, and potentially worth inviting.

## What this is, roughly

- A web-viewable rendering of (some portion of) a work's text.
- A commentary/annotation layer attached to specific passages within it — your own
  reactions and notes as you read, not necessarily tied to any concept-wiki vocabulary.
- Authored primarily by one person to start, with real interest in opening it up so
  others can annotate the same text too — collective sense-making on a shared reading,
  not just a private margin.
- Sharing scope is genuinely open: could be personal-only, shared with a small group, or
  public, and that likely varies by work or by reading group rather than having one
  fixed answer for the whole project.

## Why this is distinct from the concept wiki

An annotation made while reading is a personal reaction to a passage — it might note
"this connects to concept X," but very often it won't reference any concept-wiki
vocabulary at all; it's just a response to the text in the moment. The concept wiki
needs to stand on its own, populated by direct curation, and can't depend on this layer
existing or being complete. Conversely, this layer's value doesn't depend on the
concept wiki either — reading Wilber with commentary attached is worthwhile on its own
terms, concept-tagged or not.

## The optional connection

Where an annotation *does* tag a passage as relevant to a concept, that's a plausible
future feed into the concept wiki's excerpt curation — a lightweight bridge between the
two projects, not a required dependency in either direction. Not designed here.

A second, more concrete connection surfaced 2026-08-23 (see
[concept-wiki-vision.md](concept-wiki-vision.md)'s "Design update" section): what Rufus
actually wants when he says he wants "context" on a concept/people-page excerpt is a
side panel that can show and scroll the live source book around that excerpt's
location — not a bigger version of the excerpt itself. That's this project's territory,
not the concept wiki's: it needs an addressable, scrollable rendering of book text to
link *into*, which is exactly what a mature version of this reading layer would provide.
Worth designing the excerpt pages' "see in context" link and this project's own
addressing scheme together, once this project is picked up for real (see
`docs/annotation-system.md`'s Phase 1 prototype for where the addressing groundwork
already starts).

## The open question this project has to resolve before it can go beyond fully private
use

Copyright. Wilber's books are not out of copyright, and displaying substantial rendered
text of them — even with substantial original commentary layered on — raises a
licensing question this vision doc does not resolve. Any real design for this project
has to start by working out how much of a work's text can legitimately be shown, to
whom, and under what sharing scope, before anything else about it gets built.

## Non-goals (for now)

- No data model, file format, or UI decisions — that's the next phase, once this
  project is actually picked up.
- Not assumed to be public by default — sharing scope is an open design question, not a
  settled "yes, publish it."
- Not required to feed, or be fed by, the concept wiki.

## Appendix: raw brainstorm (source material)

Condensed from the original outflow that prompted this doc:

- Desire: "I want to be able to comment or make notes on the works and have those
  highlighted somehow... I'd like that to actually be publishable on here" — with an
  explicit awareness that copyright is an open question standing in the way of just
  publishing full text.
- Framing: list the works, have the published text where possible, but be able to
  annotate them — the annotation and the underlying text need to live together, not as
  two separate, driftable systems.
- Later clarification: this is meaningfully separate from the concept-wiki project. Two
  related but distinct workflows: (1) sharing an annotated version of Wilber's actual
  work, personally commented and potentially open to others to comment too — "just
  interesting what people are taking from it... a kind of form of sense-making" — versus
  (2) the concept wiki's curated, concept-first index. The annotation workflow *can*
  feed concept seeding when a note happens to name a concept, but that's explicitly
  called out as a secondary connection, not the main point of either project.
- Sharing scope floated as open, not fixed: "web viewable maybe not public but at least
  group shared maybe is public or it's shared privately with a group of people."
