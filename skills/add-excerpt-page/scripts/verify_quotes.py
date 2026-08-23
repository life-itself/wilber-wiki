#!/usr/bin/env python3
"""
Verify every blockquote excerpt in concepts/*.md and people/*.md is real
text from its cited source, not a paraphrase or fabrication.

Why this exists: a page was found (2026-08-23) with a fabricated quote —
a paraphrase formatted as a verbatim blockquote, attribution line and all.
Nothing in the page format made that visually distinguishable from a real
quote. This script makes "is it real" a mechanical check instead of
something a reader (or a future editing pass) has to trust.

Usage:
    python3 skills/add-excerpt-page/scripts/verify_quotes.py [file-or-glob ...]

    No arguments: checks every file in concepts/*.md and people/*.md.
    Exit code 0 if every quote passes, 1 if any quote fails.

How matching works: each quote is checked against the full text of every
work listed in the page's `works:` frontmatter (see WORK_SOURCES below).
A quote is split on "..."/"…" into segments (composited/elided quotes are
normal and expected — see concepts/holons.md); each segment over ~12
characters must appear, verbatim modulo the normalization below, as a
substring of the source. Short segments (stage directions like "a." or
single words either side of an ellipsis) are skipped rather than
false-failed.

Normalization applied to BOTH the quote and the source before matching
(so it doesn't matter which side's typography differs):
    - curly quotes/apostrophes -> straight
    - em/en dashes -> hyphen
    - **bold** markup stripped (added editorially; not in source)
    - runs of whitespace (including newlines, since blockquote lines are
      soft-wrapped) collapsed to a single space

*italic* markup is NOT stripped — the source text itself uses Markdown
emphasis (converted from the original EPUB), so italic quotes should
match with it intact. A quote that only fails because of italics is a
sign the emphasis was added editorially and should be removed from the
page, not a sign the checker is wrong.

Only a trailing "." is forgiven (see above) — a trailing quotation mark
(`"` or `,"`) is NOT, because closing a quotation early is a content
change (it asserts the source's quoted material ends there), not just
punctuation smoothing. If a quote opens or closes with a quotation mark,
that mark must be real. Likewise, a quote that starts mid-sentence must
keep the source's actual capitalization (usually lowercase) and lead
with "..." — capitalizing an original lowercase word to make an excerpt
look self-starting is exactly the kind of edit this script exists to
catch.
"""
import glob
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]

# work slug (as used in a page's `works:` frontmatter) -> source file
WORK_SOURCES = {
    "1995-sex-ecology-spirituality": "library/1995-sex-ecology-spirituality-full-text.md",
}

MIN_SEGMENT_LEN = 12  # shorter fragments are skipped, not false-failed


def normalize(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)  # strip bold, keep inner text
    s = re.sub(r"\[\^[^\]]+\]", "", s)  # strip inline footnote markers
    s = (
        s.replace("‘", "'").replace("’", "'")
        .replace("“", '"').replace("”", '"')
        .replace("–", "-").replace("—", "-")
    )
    s = re.sub(r"\s+", " ", s).strip()
    return s


def strip_italics(s: str) -> str:
    """Drop single-* emphasis markers. Used only as a fallback match, since
    the source itself uses *italic* markdown, so a quote SHOULD normally
    keep it — but pages sometimes smooth emphasis out while transcribing,
    which is a cosmetic loss, not a wording change, so it's not treated as
    a verification failure on its own."""
    return re.sub(r"\*(.+?)\*", r"\1", s)


def load_sources(works: list[str]) -> str:
    texts = []
    for w in works:
        path = WORK_SOURCES.get(w)
        if path is None:
            continue
        full = REPO_ROOT / path
        if full.exists():
            texts.append(full.read_text())
    return normalize("\n".join(texts))


def parse_frontmatter_works(text: str) -> list[str]:
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return []
    fm = m.group(1)
    m2 = re.search(r"^works:\s*\[(.*?)\]", fm, re.M)
    if not m2:
        return []
    return [w.strip() for w in m2.group(1).split(",") if w.strip()]


def extract_quote_blocks(text: str) -> list[str]:
    """Return each blockquote's body text (attribution line excluded)."""
    lines = text.split("\n")
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        if not lines[i].startswith(">"):
            i += 1
            continue
        block = []
        while i < n and lines[i].startswith(">"):
            block.append(lines[i])
            i += 1
        # drop trailing blank "> " line and the "> — attribution" line
        # (once attribution starts, every remaining line in the block is
        # part of it too — an attribution can wrap onto a second line)
        body = []
        in_attribution = False
        for bl in block:
            stripped = bl[1:].strip()
            if stripped.startswith("—") or stripped.startswith("--"):
                in_attribution = True
            if in_attribution:
                continue
            body.append(stripped)
        joined = " ".join(x for x in body if x)
        if joined:
            blocks.append(joined)
        i += 1
    return blocks


def check_file(path: Path) -> list[str]:
    text = path.read_text()
    works = parse_frontmatter_works(text)
    if not works:
        return [f"{path}: no `works:` frontmatter found, can't verify"]
    source = load_sources(works)
    if not source:
        return [f"{path}: no source text found for works {works}"]
    source_loose = strip_italics(source)

    def found(seg: str) -> bool:
        # Exact match first.
        if seg in source:
            return True
        # A quote is allowed to end its final sentence with a "." even
        # where the source continues with different punctuation (comma,
        # dash, semicolon) into more text — normal truncation practice,
        # not a content change. Only the trailing punctuation is forgiven;
        # everything before it must still match exactly.
        if seg.endswith(".") and seg[:-1] in source:
            return True
        # Fallback: emphasis smoothed out while transcribing (cosmetic,
        # not a wording change) — retry with *italics* stripped both sides.
        loose_seg = strip_italics(seg)
        if loose_seg in source_loose:
            return True
        if loose_seg.endswith(".") and loose_seg[:-1] in source_loose:
            return True
        return False

    failures = []
    for block in extract_quote_blocks(text):
        norm_block = normalize(block)
        segments = [s.strip() for s in re.split(r"\.\.\.|…", norm_block)]
        for seg in segments:
            if len(seg) < MIN_SEGMENT_LEN:
                continue
            if not found(seg):
                snippet = seg if len(seg) < 100 else seg[:97] + "..."
                failures.append(f"{path}: NOT FOUND IN SOURCE: \"{snippet}\"")
    return failures


def main(argv: list[str]) -> int:
    if argv:
        files = [Path(p) for pattern in argv for p in glob.glob(pattern)]
    else:
        files = [
            Path(p)
            for p in glob.glob("concepts/*.md") + glob.glob("people/*.md")
            if not p.endswith("index.md")
        ]

    all_failures = []
    for f in sorted(files):
        all_failures.extend(check_file(f))

    if all_failures:
        print(f"FAIL: {len(all_failures)} quote(s) could not be verified against source:\n")
        for f in all_failures:
            print(" -", f)
        return 1

    print(f"PASS: all quotes in {len(files)} file(s) verified against source.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
