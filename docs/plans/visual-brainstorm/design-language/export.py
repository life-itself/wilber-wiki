#!/usr/bin/env python3
"""One SVG source, two outputs. Deterministic export for the Wilber visuals.

For every piece listed in PIECES (a folder beside design-language/ holding
`source.svg` and `page.html`) this script writes:

  <slug>.svg          standalone static image: the source in its settled state
                      with the design-language tokens and SVG classes inlined
  <slug>.png          the same at 2x (viewBox width x 2)
  <slug>-og.png       1200 x 630 Open Graph crop (data-og="x y w h" on the root)
  <slug>-square.png   1080 x 1080 crop (data-square="x y w h" on the root)
  index.html          page.html with the source SVG inlined at <!-- @svg -->

The source is authored in its *settled* state. Animation CSS only overrides
earlier steps, so "static = source" holds by construction. PNGs are rendered
with headless Chrome (set WV_CHROME to the binary if it isn't found). Fonts are
loaded from Google Fonts, so PNG export needs network access; the SVG does not.

Usage:  python3 export.py            all pieces
        python3 export.py pre-trans-fallacy
        python3 export.py --no-png    skip the Chrome renders
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PIECES = ["pre-trans-fallacy", "states-and-stages", "four-quadrants", "holarchy", "wilber-phases"]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')
CSS = (HERE / "visuals.css").read_text(encoding="utf-8")


def block(name):
    m = re.search(r"/\* %s \*/(.*?)/\* %s \*/" % (re.escape(name[0]), re.escape(name[1])), CSS, re.S)
    if not m:
        sys.exit("block %s not found in visuals.css" % (name,))
    return m.group(1)


def svg_style():
    """Standalone <style> for an exported SVG: tokens on :root, svg classes unscoped."""
    light = block(("@tokens", "@tokens-end"))
    svg = block(("@svg-start", "@svg-end"))
    svg = svg.replace(".wv-root svg ", "").replace(".wv-root svg", "svg")
    fonts = ('--wv-serif:"Fraunces","Iowan Old Style",Georgia,"Times New Roman",serif;'
             '--wv-sans:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;')
    return ("<style>\n:root{" + light + fonts + "}\n"
            "svg{font-family:var(--wv-sans);color:var(--wv-ink);background:var(--wv-paper)}\n"
            ".t-title,.t-sub,.t-name,.t-name-s,.t-quote,.t-quote-s{font-family:\"Fraunces\",\"Iowan Old Style\",Georgia,serif}\n"
            ".wv-ghost{opacity:0}\n"
            + svg + "</style>")


def find_chrome():
    cands = [os.environ.get("WV_CHROME"),
             "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
             shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser"),
             shutil.which("chrome")]
    for c in cands:
        if c and Path(c).exists():
            return c
    return None


def render_png(svg_markup, viewbox, width, height, out, chrome):
    """Render svg_markup (already containing its own <style>) at width x height px."""
    x, y, w, h = viewbox
    svg_markup = re.sub(r'viewBox="[^"]*"', 'viewBox="%s %s %s %s"' % (x, y, w, h), svg_markup, count=1)
    svg_markup = re.sub(r"<svg ", '<svg width="%d" height="%d" preserveAspectRatio="xMidYMid slice" ' % (width, height), svg_markup, count=1)
    html = ('<!doctype html><html><head><meta charset="utf-8">' + FONTS +
            '<style>html,body{margin:0;background:#f8f6f1}svg{display:block}</style></head><body>' +
            svg_markup + '</body></html>')
    with tempfile.TemporaryDirectory() as td:
        page = Path(td) / "render.html"
        page.write_text(html, encoding="utf-8")
        cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
               "--virtual-time-budget=6000", "--window-size=%d,%d" % (width, height),
               "--screenshot=%s" % out, page.as_uri()]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def export(slug, do_png=True):
    d = ROOT / slug
    src = (d / "source.svg").read_text(encoding="utf-8")
    page = (d / "page.html").read_text(encoding="utf-8")
    root = re.search(r"<svg[^>]*>", src).group(0)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', root).group(1).split()]
    og = re.search(r'data-og="([^"]+)"', root)
    sq = re.search(r'data-square="([^"]+)"', root)

    # 1. page: inline the source as-is (classes resolve against visuals.css)
    if "<!-- @svg -->" not in page:
        sys.exit("%s/page.html has no <!-- @svg --> placeholder" % slug)
    (d / "index.html").write_text(page.replace("<!-- @svg -->", src.strip()), encoding="utf-8")

    # 2. standalone static svg: strip step attributes, inline the style
    static = re.sub(r'\s(data-wv-steps|data-step|data-wv-dur)="[^"]*"', "", src)
    static = re.sub(r'\sdata-at="[^"]*"', "", static)
    static = static.replace("</svg>", "", 1)
    if "<style>" not in static:
        static = re.sub(r"(<svg[^>]*>)", lambda m: m.group(1) + "\n" + svg_style(), static, count=1)
    static = static.rstrip() + "\n</svg>\n"
    if not static.lstrip().startswith("<?xml"):
        static = '<?xml version="1.0" encoding="UTF-8"?>\n' + static
    (d / (slug + ".svg")).write_text(static, encoding="utf-8")

    # 3. pngs
    if do_png:
        chrome = find_chrome()
        if not chrome:
            print("  no Chrome found; set WV_CHROME. Skipping PNG renders.")
            return
        body = static.split("?>", 1)[1] if static.startswith("<?xml") else static
        render_png(body, vb, int(vb[2] * 2), int(vb[3] * 2), d / (slug + ".png"), chrome)
        if og:
            render_png(body, [float(v) for v in og.group(1).split()], 1200, 630, d / (slug + "-og.png"), chrome)
        if sq:
            render_png(body, [float(v) for v in sq.group(1).split()], 1080, 1080, d / (slug + "-square.png"), chrome)
    print("  wrote index.html, %s.svg%s" % (slug, ", pngs" if do_png else ""))


def main(argv):
    do_png = "--no-png" not in argv
    slugs = [a for a in argv if not a.startswith("--")] or PIECES
    for slug in slugs:
        print(slug)
        export(slug, do_png)


if __name__ == "__main__":
    main(sys.argv[1:])
