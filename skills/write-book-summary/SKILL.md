---
name: write-book-summary
description: Use when writing, revising or reviewing a book summary page in the wilber-wiki repo, i.e. the expanded works/<slug>.md page for a book whose full text is in library/. Covers page structure, sourcing, excerpt verification and the review checklist.
---

# Writing a book summary page

## What this is

A book summary page is the expanded form of `works/<slug>.md`, used only for books whose full text is in `library/<slug>-full-text.md`. Currently that means *Sex, Ecology, Spirituality*, *Integral Psychology* and *Integral Spirituality*. Every excerpt attribution on the wiki links to the book's works page, so this page is where readers land when they want "the book". Other works pages keep their short bibliographic form.

Design rationale and decisions: `docs/plans/2026-10-10-book-summary-pages-design.md` (Rufus approved 2026-10-10).

**Also read [`skills/add-excerpt-page/SKILL.md`](../add-excerpt-page/SKILL.md) before starting.** Its excerpt rules (verbatim only, `...` for every elision, keep the source's capitalisation, never close a quotation early) apply here unchanged.

## The one rule that matters most

**Write from the full text, not from memory or the old page.** The existing `## In-Depth Overview` sections were written before the full texts were in the repo, cite nothing, and contain at least one structural error. Treat them as unreliable: nothing from them survives unless you've confirmed it in `library/<slug>-full-text.md`. Every claim about what the book says needs a location (chapter, endnote, preface or appendix) that you have actually read.

## The goal: a page a human wants to read

Accuracy is necessary, not sufficient. The page exists for a curious reader, so judge it by whether it reads well: clear, coherent, not repetitive, and useful for deciding what the book says and whether to read it. The first three pages passed every sourcing check and still read like annotated contents notes, because the sourcing review was the only review. Rufus's standard (2026-10-11): what matters is what a critical reader makes of the page, not whether it hits a word count.

## Process (Rufus's guidance, 2026-10-10/11)

1. **Beads first.** Log an epic and child beads (design, pilot, review, other books, ship) before writing anything.
2. **Design the structure before writing**, in a doc under `docs/plans/`, with recommendations. Get Rufus's sign-off on the structure; record his decisions in the doc.
3. **Pilot one book, review it properly, then do the rest.** Write one page, have it reviewed by fresh agents, fold the lessons into this skill, then write the others (in parallel, by separate agents).
4. **Two reviews, by fresh agents who are not the writer:** an accuracy review (checklist items 1–7) and a separate reader-quality review (items 8–13), done by an editor reading the page as a newcomer. The editor reports findings with quoted lines and rewrites, without editing; then a writer revises against the report, keeping sourcing intact.
5. **Report the critics' views, not just the checks.** When summarising the work for Rufus, say what the reviewers thought of the page as reading, not only how many claims verified.
6. **Ship by pushing to `main`; never run `fl`.** If something needs Rufus's judgement, leave a note on the bead and in `NEXT.md` and move on.

Other conventions from Rufus:

- **Date a book by its original publication** (SES is 1995) even when the wiki quotes a later revised edition; mention the revision, don't headline it.
- **Spend effort where readers notice it.** Don't research trivia (minor editions, audio releases, pen-name or collaborative side projects); the works catalog is for books.
- **The page's own judgements are acceptable in What's contested** when fairly put and grounded in the text; external critics still need a link.

## Page structure

Keep the frontmatter. Add `works: [<own-slug>]` so `verify_quotes.py` checks the page. Then use these sections, in this order, with these exact headings:

1. **Header** (existing title/subtitle/year/format line), plus one plain orientation sentence.
2. `## At a glance` (~100 words). What the book is, what it argues, who should read it, and what to read instead if it's not for them (link an existing works page). Replaces `## Description`.
3. `## Context` (150–250 words). Where it sits in Wilber's development; link [The evolution of Wilber's thought](phases.md) and [From SES to Integral Spirituality](../concepts/from-ses-to-integral-spirituality.md) rather than repeating them. Say what it builds on and what later revised it, and which edition the wiki quotes (SES: revised second edition; IP and IS: Shambhala ebooks of the original editions).
4. `## Summary` (250–400 words). The core argument. A reader who stops here should know the main claims.
5. `## Overview` (1,300–2,000 words). The book in its own order, told as an argument unfolding, not a contents list: open each part and chapter with what it does for the book's argument, keep the two or three points that serve it, and add transitions. Use one `###` subsection per part (SES: Book One / Book Two; IP: Ground / Path / Fruition; IS: Introduction, chapters, Appendixes), with chapter-level subsections only where a part is long. Use the full text's chapter titles. Cite locations inline, like *(ch. 9, note 15)*, but inside a chapter's own subsection cite only *other* locations (notes, other chapters, appendixes); say so once at the top of the Overview. Don't cite in At a glance or Summary. Don't repeat in the Overview what Key passages quote in full. Link concept and people pages inline where they come up naturally; don't force them. Short quoted phrases are fine; full passages belong in Key passages. For SES, cover the endnotes: several main arguments and the replies to critics live there.
6. `## Key passages` (6–10 excerpts). Verified blockquotes in chapter order. Give each a one-sentence lead-in saying why it matters, and no per-excerpt heading. On the book's own page the attribution gives only the location: `— ch. 4, “A View from Within”`. Pick passages that carry the book's argument; overlap with concept pages is fine but shouldn't be the default.
7. `## What's contested` (150–300 words). Tensions, weak points, and where Wilber later revised himself. Use the same register as concept pages: what's strong and what's contestable. Only Wilber-internal points and external critiques you can cite with a link. The broader critical layer is a separate epic (`wilberwiki-dxr`), so don't attempt a survey of the critical literature.
8. `## Concepts in this book`. A grouped list of the concept pages that draw on this book, each with a one-line note on its role here. Check `works:` frontmatter in `concepts/` to find them. `## People`: the main interlocutors, linked to people pages, a short curated list.
9. `## Publication history` (existing facts, kept) and `## Notes` (kept as is, including any link to Rufus's notes).

Target total: 3,000–4,000 words. The Concepts and People lists are long by necessity (SES's runs to ~500 words), so a page slightly over the total because of them is fine; the prose sections should stay inside their own ranges. Write in plain prose that a newcomer can follow: define Wilber's terms the first time they appear, or link the concept page.

## Mechanics

- **Line style:** one line per paragraph, list item or blockquote paragraph; no hard wrapping.
- **Links:** relative markdown links (`../concepts/holons.md`, `../people/habermas.md`, `phases.md`). Check every linked file exists.
- **Verification:** `python3 skills/add-excerpt-page/scripts/verify_quotes.py works/<slug>.md` must pass. (The first summary page extends the script to cover works pages that set `works:`; see "Script support" below.) Then run it with no arguments to check the whole repo.
- **Chapter location for a line:** find the nearest heading above it in the full text. SES's chapter headings all read `## Sex, Ecology, Spirituality`, so count them from the Contents order. The other two books' headings carry the chapter number.

## Script support (one-time, with the first page)

`verify_quotes.py` checks `concepts/*.md` and `people/*.md` by default. Extend the default file set to include `works/*.md` pages whose frontmatter has `works:`, and skip works pages without it rather than reporting them as failures. Make sure explicit `works/<slug>.md` arguments work too. The unlinked-attribution check needs no change: own-page attributions don't name the book's title.

## Review checklist (for the reviewer, who must not be the writer)

1. Run `verify_quotes.py` on the page: it must pass.
2. Sample at least 10 chapter-cited claims across the whole page and confirm each against the cited location. Report any that are wrong, or that are supported somewhere else.
3. Coverage: is each part of the book represented roughly in proportion to its weight? For SES, are the endnotes represented?
4. Nothing carried over unverified from the old overview.
5. Read it as a newcomer: are terms defined or linked? Does the Summary stand on its own?
6. Links: every concept, people and works link resolves, and Concepts in this book matches the concept pages that actually cite this book.
7. What's contested is fair, with external claims linked and nothing invented.

Then a separate **reader-quality pass**, ideally by another fresh reviewer, reading the page start to finish as an intelligent newcomer would:

8. Clarity: can each paragraph be understood on first reading? Flag dense, abstract or jargon-stacked sentences.
9. Coherence and flow: does each section have a clear thread, and does the Overview read as an argument unfolding rather than a list of chapter contents?
10. Redundancy: do At a glance, Summary, Overview and Key passages repeat each other? Each layer should add something.
11. Prose: sentence-level quality, monotony (e.g. every paragraph opening "In ch. N…"), filler, hedging, and stock phrasing.
12. Length and pacing for a human reader: where does attention flag, and what could go?
13. Usefulness: after reading, does the reader understand what the book argues, why it matters, and whether to read it?

Report findings with quoted lines and suggested rewrites, ranked by impact on a reader.

Fix the findings, then record lessons for later writers in the design doc.

## Rationalizations to watch for

| Thought | Reality |
|---|---|
| "The old overview is basically right, I'll tidy it" | It has no citations and contains at least one structural error. Rewrite from the source. |
| "I know what SES says" | Knowing isn't citing. Find the chapter. |
| "This chapter is minor, I'll skip it" | Say so in a sentence; don't silently drop it. Coverage is part of the review. |
| "The endnotes are optional" | For SES, much of the argument and the replies to critics are in them. |
| "Every sentence needs a citation" | Inside a chapter's section, the heading is the citation. Cite only other locations. |
| "It passed review, so it's done" | Which review? Accuracy and reader quality are separate passes. |
| "Covering every chapter point is thorough" | A list of contents isn't a summary. Keep what carries the argument. |
| "Repeating the key idea helps it land" | Once in Summary, once in Overview at most. Readers notice the third time. |
