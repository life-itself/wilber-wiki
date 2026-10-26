#!/usr/bin/env python3
"""Copy the animated figures from docs/plans/visual-brainstorm into the live site.

For each piece: copies its PNGs to assets/visuals/, and replaces the block between
<!-- figure:<slug> --> and <!-- /figure:<slug> --> in visuals/index.md with the piece's
share block: the PNG as a plain <img> (so right-click and long-press save or copy
work), an empty actions row that wv-motion.js fills (Watch it unfold, Copy image,
Download, Share, Copy link), and the animated figure (controls + inline SVG + step
captions), hidden until Watch is pressed. Also copies the shared visuals.css and
wv-motion.js to assets/visuals/.

Each piece also gets its own page, visuals/<slug>.md, generated from its section of
visuals/index.md (heading, figure, text) with the figure's own og:image, so a shared
link previews that figure. Edit visuals/index.md, never the generated pages.

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
PAGE = ROOT / "visuals/index.md"
PIECES = ["pre-trans-fallacy", "states-and-stages", "four-quadrants", "holarchy", "wilber-phases"]

# Site-only additions: no-JS shows only the settled caption (the last one).
SITE_CSS = """
/* site additions (scripts/sync-visuals.py) */
[data-wv-steps]:not(.wv-ready) [data-wv-caption] [data-cap]:not(:last-child) { display: none; }
.wv-root > [data-wv-steps] { margin: 1.5rem 0; }
/* share block: the image first, the animation on request */
.wv-share { margin: 1.5rem 0; }
.wv-share .wv-still { display: block; width: 100%; height: auto; margin: 0; border-radius: 6px; }
.wv-share:not(.wv-watching) > [data-wv-steps] { display: none; }
.wv-share.wv-watching > .wv-still { display: none; }
.wv-share > [data-wv-steps] { margin: 0; }
.wv-share .wv-actions { margin: 0.6rem 0 0; }
"""


MARK_RE = re.compile(r'href="data:image/png;base64,([A-Za-z0-9+/=]+)"')


def save_mark(b64):
    data = base64.b64decode(b64)
    name = "mark-" + hashlib.sha1(data).hexdigest()[:8] + ".png"
    (ASSETS / name).write_bytes(data)
    return f'href="/assets/visuals/{name}"'


def figure_block(slug):
    html = (SRC / slug / "index.html").read_text()
    start = re.search(r"<div[^>]*\sdata-wv-steps", html).start()
    end = html.index("</figure>", start)
    end = html.index("</div>", end) + len("</div>")
    block = html[start:end]
    svg = (SRC / slug / "source.svg").read_text()
    alt = ". ".join(re.search(rf"<{t}[^>]*>(.*?)</{t}>", svg, re.S).group(1).strip() for t in ("title", "desc"))
    alt = alt.replace('"', "&quot;")
    still = f'<img class="wv-still" src="/assets/visuals/{slug}.png" width="2400" height="1600" alt="{alt}">'
    actions = '<div class="wv-controls wv-actions" data-wv-actions></div>'
    # The step CSS expects the [data-step] element inside a .wv-root, so wrap it.
    block = f'<div class="wv-root wv-share" data-wv-share="{slug}" data-wv-link="/visuals/{slug}">\n{still}\n' + block + f"\n{actions}\n</div>"
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
            raise SystemExit(f"markers for {slug} not found in {PAGE.relative_to(ROOT)}")
        block = figure_block(slug)
        page = pattern.sub(lambda m: m.group(1) + block + "\n" + m.group(2), page)
    PAGE.write_text(page)
    for slug in PIECES:
        write_figure_page(slug, page)
    print("synced:", ", ".join(PIECES))


def write_figure_page(slug, page):
    """visuals/<slug>.md: the piece's section of the index, as a page of its own."""
    sections = re.split(r"^## ", page, flags=re.M)[1:]
    section = next((x for x in sections if f"<!-- figure:{slug} -->" in x), None)
    if section is None:
        raise SystemExit(f"no section for {slug} in {PAGE.relative_to(ROOT)}")
    title, body = section.split("\n", 1)
    title, body = title.strip(), body.strip()
    prose = re.sub(r"<!-- figure:.*?<!-- /figure:[^>]+-->", "", body, flags=re.S)
    first = next(l for l in prose.splitlines() if l.strip() and not l.startswith((">", "<", "!")))
    description = re.sub(r"[*_]|\[([^\]]*)\]\([^)]*\)", lambda x: x.group(1) or "", first)
    description = re.split(r"(?<=[.?!])\s", description)[0].replace('"', "'")
    (ROOT / "visuals" / f"{slug}.md").write_text(
        f'---\ntitle: "{title}"\ndescription: "{description}"\nimage: /assets/visuals/{slug}-og.png\n---\n\n'
        f"<!-- Generated by scripts/sync-visuals.py from visuals/index.md; edit that, not this. -->\n\n"
        f"{body}\n\n[All visuals](index.md)\n")


if __name__ == "__main__":
    main()
