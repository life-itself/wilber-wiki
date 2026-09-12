# People index — Integral Psychology mention-count scan

Status: scan only, no excerpts pulled yet. Produced 2026-09-13, per the design in
[`docs/integral-psychology-import-design.md`](../docs/integral-psychology-import-design.md)
(decision 7) — the second-book equivalent of
[`1995-sex-ecology-spirituality-people-source.md`](1995-sex-ecology-spirituality-people-source.md).
No pre-existing people-source doc for this book existed to copy in (unlike *SES*), so
this is a fresh scan.

## Method

Same as the original *SES* scan: main-body mention counts only (footnotes/Notes
backmatter and the Index excluded), by name, from a full-text grep of
[`2000-integral-psychology-full-text.md`](2000-integral-psychology-full-text.md).
Main body = chapters 1–15 (lines 395–2044 of the converted file; the "Charts"
backmatter, Notes, and Index sections that follow are excluded). "Peak chapter(s)"
is the top 3 chapters by raw mention count, not a claim about where the substantive
discussion is — that needs an actual read, not just grep.

**Caveat this scan doesn't handle**: surname collisions and partial-name matches
(e.g. "Graves" could in principle match something other than Clare Graves,
though a spot check didn't turn up any). Treat counts as a prioritization signal,
not a verified figure — same caveat the *SES* scan carried.

## Mention counts (main text only)

| Person | Mentions | Peak chapter(s) | Already has a page? |
|---|---|---|---|
| James Mark Baldwin | 43 | ch. 7, ch. 4, ch. 1 | No — has own dedicated appendix chart (Chart 11) |
| Jean Piaget | 31 | ch. 1, ch. 4, ch. 7 | Yes — [piaget.md](../people/piaget.md) |
| Jürgen Habermas | 24 | ch. 7, ch. 12, ch. 13 | Yes — [habermas.md](../people/habermas.md) |
| Lawrence Kohlberg | 23 | ch. 4, ch. 7, ch. 9 | Yes — [kohlberg.md](../people/kohlberg.md) |
| Clare Graves | 21 | ch. 4, ch. 13, ch. 3 | No |
| Sri Aurobindo | 21 | ch. 7, ch. 1, ch. 12 | Yes — [aurobindo.md](../people/aurobindo.md) |
| Jean Gebser | 17 | ch. 12, ch. 13, ch. 1 | Yes — [gebser.md](../people/gebser.md) |
| Jane Loevinger | 16 | ch. 4, ch. 3, ch. 8 | Yes — [loevinger.md](../people/loevinger.md) |
| Abraham Maslow | 14 | ch. 7, ch. 4, ch. 1 | Yes — [maslow.md](../people/maslow.md) |
| Robert Kegan | 9 | ch. 4, ch. 3, ch. 2 | No |
| Plotinus | 8 | ch. 1, ch. 12, ch. 3 | Yes — [plotinus.md](../people/plotinus.md) |
| Erik Erikson | 8 | ch. 4, ch. 3, ch. 8 | No |
| Carol Gilligan | 7 | ch. 2, ch. 13, ch. 1 | No |
| Susanne Cook-Greuter | 7 | ch. 1, ch. 4, ch. 3 | No |
| Teresa of Ávila | 6 | ch. 8, ch. 12, ch. 3 | No |
| John Broughton | 5 | ch. 4, ch. 3, ch. 7 | No |
| Charles Alexander | 4 | ch. 1, ch. 2, ch. 8 | No |
| Jenny Wade | 3 | ch. 4, ch. 14 | No |
| Sigmund Freud | 3 | ch. 4, ch. 1 | Yes — [freud.md](../people/freud.md) |
| James Fowler | 3 | ch. 11, ch. 7 | No |
| Michael Commons | 3 | ch. 1, ch. 8, ch. 10 | No |
| Michael Washburn | 2 | ch. 4 | No |
| Carl Jung | 2 | ch. 4 | Yes — [jung.md](../people/jung.md) |
| Michael Basseches | 2 | ch. 1, ch. 8 | No |
| Roberto Assagioli | 2 | ch. 4, ch. 8 | No — flagged "not written up" for *SES* (1 mention there, bibliography only) |
| Evelyn Underhill | 2 | ch. 10 | No |
| William Torbert | 1 | ch. 4 | No |
| Robert Selman | 1 | ch. 4 | No |
| Erich Neumann | 1 | ch. 4 | No |

## Reading of the results

**Existing people pages that clearly warrant an IP extension** (`works:` +
excerpts, per `wilberwiki-vxk.18`) — high mention counts, all already substantive
*SES* pages: Piaget, Habermas, Kohlberg, Aurobindo, Gebser, Loevinger, Maslow,
Plotinus. Freud and Jung are thin here (3 and 2) — worth a quick check but may not
add much beyond what their *SES* pages already say.

**Strong new-page candidates** (per `wilberwiki-vxk.19`), all names that don't
appear in the *SES* roster at all: Baldwin (highest count in the whole scan, plus
his own dedicated chart — clearly substantive), Graves (21, the source of "spiral
dynamics" thinking Wilber draws on directly), Kegan (9, "the self" is largely built
on his constructive-developmental work per ch. 3–4), Erikson (8), Gilligan (7),
Cook-Greuter (7).

**Borderline** — real discussion likely present but thinner; worth a quick read of
the actual passages before committing to a page, not an automatic yes: Teresa of
Ávila (6, contemplative-stage citation), Broughton (5).

**Likely citations without much discussion attached** (same treatment as *SES*'s
"not written up" four — would need an actual passage check before ruling out, this
scan alone doesn't confirm it, but low counts make it a reasonable prior): Alexander,
Wade, Fowler, Commons, Washburn, Basseches, Assagioli, Underhill, Torbert, Selman,
Neumann.

Final call on which of these get pages is for whoever executes `wilberwiki-vxk.19` —
this scan narrows the list, it doesn't settle it.
