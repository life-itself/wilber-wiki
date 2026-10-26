#!/usr/bin/env python3
"""Copy the animated figures from docs/plans/visual-brainstorm into the live site.

For each piece: copies its PNGs to assets/visuals/, and replaces the block between
<!-- figure:<slug> --> and <!-- /figure:<slug> --> in visuals.md with the piece's
animated figure (controls + inline SVG + step captions). Also copies the shared
visuals.css and wv-motion.js to assets/visuals/.

Run after export.py: python3 scripts/sync-visuals.py
"""
import base64
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs/plans/visual-brainstorm"
ASSETS = ROOT / "assets/visuals"
PAGE = ROOT / "visuals.md"
PIECES = ["pre-trans-fallacy", "states-and-stages"]

# Site-only additions: no-JS shows only the settled caption (the last one).
SITE_CSS = """
/* site additions (scripts/sync-visuals.py) */
[data-wv-steps]:not(.wv-ready) [data-wv-caption] [data-cap]:not(:last-child) { display: none; }
.wv-root > [data-wv-steps] { margin: 1.5rem 0; }
"""


MARK_RE = re.compile(r'href="data:image/png;base64,([A-Za-z0-9+/=]+)"')


def save_mark(b64):
    data = base64.b64decode(b64)
    name = "mark-" + hashlib.sha1(data).hexdigest()[:8] + ".png"
    (ASSETS / name).write_bytes(data)
    return f'href="/assets/visuals/{name}"'


def figure_block(slug):
    html = (SRC / slug / "index.html").read_text()
    start = html.index("<div data-wv-steps")
    end = html.index("</figure>", start)
    end = html.index("</div>", end) + len("</div>")
    block = html[start:end]
    # The step CSS expects the [data-step] element inside a .wv-root, so wrap it.
    block = '<div class="wv-root">\n' + block + "\n</div>"
    # Flowershow rewrites data: URIs in href into site-relative links, so serve
    # the embedded signature mark as a real file instead.
    block = MARK_RE.sub(lambda m: save_mark(m.group(1)), block)
    # A blank line would end the raw HTML block in markdown, so drop them.
    return "\n".join(line for line in block.splitlines() if line.strip())


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    css = (SRC / "design-language/visuals.css").read_text() + SITE_CSS
    (ASSETS / "visuals.css").write_text(css)
    shutil.copy(SRC / "design-language/wv-motion.js", ASSETS / "wv-motion.js")
    page = PAGE.read_text()
    for slug in PIECES:
        for suffix in ("", "-og"):
            shutil.copy(SRC / slug / f"{slug}{suffix}.png", ASSETS / f"{slug}{suffix}.png")
        pattern = re.compile(rf"(<!-- figure:{slug} -->\n)(?:.*?\n)?(<!-- /figure:{slug} -->)", re.S)
        if not pattern.search(page):
            raise SystemExit(f"markers for {slug} not found in visuals.md")
        block = figure_block(slug)
        page = pattern.sub(lambda m: m.group(1) + block + "\n" + m.group(2), page)
    PAGE.write_text(page)
    print("synced:", ", ".join(PIECES))


if __name__ == "__main__":
    main()
