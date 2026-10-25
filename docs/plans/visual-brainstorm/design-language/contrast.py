#!/usr/bin/env python3
"""Contrast check for the Wilber visuals palette.

Reads the token block in visuals.css and prints WCAG 2.x contrast ratios of
every ink-like role against paper and surface. Run from
anywhere: `python3 docs/plans/visual-brainstorm/design-language/contrast.py`.
Exit code 1 if any role that carries small text drops below 4.5:1.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSS = (HERE / "visuals.css").read_text(encoding="utf-8")

TEXT_ROLES = ["ink", "ink-soft", "muted", "level", "state", "fallacy", "ground", "accent"]
LARGE_ONLY = {"accent"}          # used for links/underlines/large marks, checked at 3:1
GROUNDS = ["paper", "surface"]


def block(name):
    m = re.search(r"/\* @%s \*/(.*?)/\* @tokens-end \*/" % name, CSS, re.S)
    if not m:
        sys.exit("token block %s not found" % name)
    return dict(re.findall(r"--wv-([a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{6})", m.group(1)))


def lum(hexcol):
    r, g, b = (int(hexcol[i:i + 2], 16) / 255 for i in (1, 3, 5))
    def ch(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    bad = 0
    for theme in ("tokens",):
        t = block(theme)
        print("\nLIGHT")
        print("%-10s" % "role" + "".join("%12s" % g for g in GROUNDS))
        for role in TEXT_ROLES:
            if role not in t:
                continue
            row = "%-10s" % role
            for g in GROUNDS:
                r = ratio(t[role], t[g])
                need = 3.0 if role in LARGE_ONLY else 4.5
                flag = "" if r >= need else " !"
                if r < need:
                    bad += 1
                row += "%10.2f%s" % (r, flag.ljust(2))
            print(row)
    print()
    if bad:
        print("%d role/ground pairs below target" % bad)
        sys.exit(1)
    print("all text roles meet 4.5:1 (accent 3:1)")


if __name__ == "__main__":
    main()
