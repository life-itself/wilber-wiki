"""Wilber Wiki figures: the house style as code, and the exporter.

A piece is a folder beside this one with a `figure.py` that calls `draw(fig)` using the
helpers here, and a `page.html` with an `<!-- @svg -->` placeholder. `build(piece)` writes:

  <slug>.svg            tight, transparent, text as outlines: for the page (light and dark via CSS)
  <slug>.png, @2x.png   the full canvas with its margin, on white: for sharing alone
  <slug>-og.png         1200 x 630, the canvas fitted on white: Open Graph card
  <slug>-dark.png       the full canvas on night, for review
  <slug>-accent-*.png   the canvas in each accent, for review
  index.html            page.html with the SVG inlined, steps intact: the animated page

Grammar (after the Seeds of Renaissance diagram system, design-language/README.md): one face,
Apfel Grotezk, no bold, hierarchy by size; panels with no outline in a pale tint; full accent
only on the marks the figure is about; ink lines with round caps, 4 for what matters, 2 for
scaffolding; solid arrowheads; no legends; title top left, grey subtitle under it, signature
bottom right. Sizes are for a 1600 px canvas with a 72 px margin.

Text is set as outlines (fontTools + HarfBuzz, with kerning), so the SVG renders without the
font installed. Needs: fonttools, uharfbuzz; Google Chrome for the PNGs ($CHROME).
"""
import io, math, os, pathlib, re, subprocess, tempfile
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

# ── Canvas ─────────────────────────────────────────────────────────
W, M = 1600, 72                 # canvas width and margin
SIG_FOOT, SIG_GAP = 56, 36      # signature to the bottom edge; drawing to the signature (as SoR)
PAD = 40                        # inside a panel, all four sides
LW, LW2, HEAD = 4, 2, 18        # line for what matters, line for scaffolding, arrowhead length

# ── Type: Apfel Grotezk, Regular and Mittel only (SoR's scale at 1600 px) ──
TITLE, SUBTITLE, HEADING, GROUP, LABEL, SECOND, TAG, SIG = 46, 28, 32, 34, 29, 26, 21, 20

# ── Colour ─────────────────────────────────────────────────────────
INK, CHALK, NIGHT, WHITE = "#1b1916", "#ece7dc", "#171613", "#ffffff"
ACCENTS = {
    # SoR's logo red, and its tint (red at 16% on white, 40% on night)
    "red":   dict(name="SoR red", acc="#e5201c", acc_dark="#f0423e", tint="#fbdbdb", tint_dark="#6b1a17"),
    # the site's amber family: a deeper ochre that passes as text, a warm cream tint
    "rust":  dict(name="rust", acc="#b5451b", acc_dark="#f09a52", tint="#f8e8d6", tint_dark="#5a2a14"),
}
DEFAULT_ACCENT = "rust"


class Face:
    def __init__(self, path):
        self.tt = TTFont(path)
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.upem = self.tt["head"].unitsPerEm
        self.cap = self.tt["OS/2"].sCapHeight / self.upem
        self.xh = self.tt["OS/2"].sxHeight / self.upem
        self.hb = hb.Font(hb.Face(hb.Blob.from_file_path(str(path))))

    def path(self, text, size, x=0.0, y=0.0, track=0.0):
        """SVG path d for `text` with its baseline at (x, y). Returns (d, advance width)."""
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True, "liga": True})
        sc, cx = size / self.upem, 0.0
        pen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.1f}")
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            t = (sc, 0, 0, -sc, x + cx + pos.x_offset * sc, y - pos.y_offset * sc)
            self.glyphs[self.order[info.codepoint]].draw(TransformPen(pen, t))
            cx += pos.x_advance * sc + track
        return pen.getCommands(), cx - track

    def width(self, text, size, track=0.0):
        return self.path(text, size, track=track)[1]


regular = Face(HERE / "fonts/ApfelGrotezk-Regular.otf")
medium = Face(HERE / "fonts/ApfelGrotezk-Mittel.otf")   # Mittel: the heavier of the two weights allowed


# ── Primitives. Colour is by class so the SVG can switch to chalk on night. ──
def text(s, size, x, y, face=regular, anchor="start", muted=False, accent=False, track=0.0):
    """Outlined text, baseline at y. Returns (svg, width)."""
    d, w = face.path(s, size, 0, 0, track=track)
    dx = x - {"start": 0, "middle": w / 2, "end": w}[anchor]
    cls = "wv-acc" if accent else "wv-ink"
    op = ' fill-opacity=".6"' if muted else ""
    return f'<path class="{cls}"{op} transform="translate({dx:.1f} {y:.1f})" d="{d}"/>', w


def tag(s, x, y, anchor="start", accent=False):
    """Axis names and one-to-three-word tags: Medium, uppercase, tracked."""
    return text(s.upper(), TAG, x, y, medium, anchor=anchor, accent=accent, track=TAG * 0.1)[0]


def wrap(s, size, maxw, face=regular):
    """Break `s` into lines no wider than maxw (measured with the face itself)."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if cur and face.width(t, size) > maxw:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def line(pts, sw=LW2, accent=False, cls=""):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    c = ("wv-sacc" if accent else "wv-sink") + (" " + cls if cls else "")
    return f'<path class="{c}" d="{d}" fill="none" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'


def curve(d, sw=LW2, accent=False, cls="", extra=""):
    c = ("wv-sacc" if accent else "wv-sink") + (" " + cls if cls else "")
    return f'<path class="{c}" d="{d}" fill="none" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{extra}/>'


def _head(tip, a, L, accent):
    w = L * 0.4
    bx, by = tip[0] - L * math.cos(a), tip[1] - L * math.sin(a)
    nx, ny = -math.sin(a) * w, math.cos(a) * w
    c = "wv-acc" if accent else "wv-ink"
    return (f'<path class="{c} wv-head" d="M{tip[0]:.1f} {tip[1]:.1f} L{bx + nx:.1f} {by + ny:.1f} '
            f'L{bx - nx:.1f} {by - ny:.1f} Z"/>')


def arrow(pts, sw=LW2, accent=False, L=None, animate=False):
    """A solid line with a solid arrowhead; the line stops at the base of the head.
    animate=True marks the line to draw in and the head to follow (page only)."""
    L = L or (HEAD + 6 if sw >= LW else HEAD)
    pts = list(pts)
    a = math.atan2(pts[-1][1] - pts[-2][1], pts[-1][0] - pts[-2][0])
    tip = pts[-1]
    pts[-1] = (tip[0] - 0.8 * L * math.cos(a), tip[1] - 0.8 * L * math.sin(a))
    body = line(pts, sw, accent, cls="wv-draw" if animate else "")
    if animate:
        body = body.replace(" fill=", ' pathLength="1" fill=', 1)
    return body + _head(tip, a, L, accent)


def curved_arrow(p0, c1, c2, p1, sw=LW, accent=True, L=None, animate=False):
    """A cubic Bézier from p0 to p1 with control points c1, c2, and a solid head at p1."""
    L = L or (HEAD + 6 if sw >= LW else HEAD)
    a = math.atan2(p1[1] - c2[1], p1[0] - c2[0])
    end = (p1[0] - 0.8 * L * math.cos(a), p1[1] - 0.8 * L * math.sin(a))
    d = f"M{p0[0]:.1f} {p0[1]:.1f} C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {end[0]:.1f} {end[1]:.1f}"
    body = curve(d, sw, accent, cls="wv-draw" if animate else "", extra=' pathLength="1"' if animate else "")
    return body + _head(p1, a, L, accent)


def panel(x, y, w, h, cls=""):
    """A group: no outline, square corners, the tint."""
    c = "wv-tint" + (" " + cls if cls else "")
    return f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"/>'


def bracket(x, y0, y1, label, side="right", gap=36):
    """A square bracket beside a span, with its label on the outside at mid-height."""
    s = 1 if side == "right" else -1
    mid = (y0 + y1) / 2
    out = line([(x - s * 24, y0), (x, y0), (x, y1), (x - s * 24, y1)]) + line([(x, mid), (x + s * gap, mid)])
    out += text(label, GROUP, x + s * (gap + 18), mid + medium.cap * GROUP / 2, medium,
                anchor="start" if s > 0 else "end")[0]
    return out


DISC = 64   # the mark's disc at a 1600 px canvas (diagrams.md: 64 px mark, 20 px text)


def _b64(path):
    import base64
    return "data:image/png;base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()


_MARK = {"light": _b64(HERE / "mark/seeds-mark-colour-128.png"), "dark": _b64(HERE / "mark/seeds-mark-colour-dark-128.png")}


def sig_baseline(top):
    """Text baseline for a signature whose mark top is at `top` (as SoR's outline.py sets it)."""
    return top + DISC / 2 + medium.cap * SIG / 2


def signature(right, top):
    """The SoR mark, then WILBER WIKI · SEEDS OF RENAISSANCE · wilber.wiki at 60% ink, one line.
    Origin: mark top-left; right edge of the text at `right`. Light grounds: the colour mark on its
    white disc; dark: the colour-dark mark, no disc (switched by class). Returns (svg, width)."""
    parts = [("WILBER WIKI", medium, SIG * 0.1), ("SEEDS OF RENAISSANCE", medium, SIG * 0.1), ("wilber.wiki", regular, SIG * 0.02)]
    widths = [f.width(t, SIG, track=tr) for t, f, tr in parts]
    dot = 14 + 4 + 14
    text_w = sum(widths) + dot * (len(parts) - 1)
    total = DISC + 18 + text_w
    x0 = right - total
    r = DISC / 2
    m = DISC * 0.85
    out = [f'<g class="wv-on-light"><circle cx="{x0 + r:.1f}" cy="{top + r:.1f}" r="{r}" fill="{WHITE}"/>'
           f'<image x="{x0 + r - m / 2:.1f}" y="{top + r - m / 2:.1f}" width="{m:.1f}" height="{m:.1f}" href="{_MARK["light"]}"/></g>',
           f'<image class="wv-on-dark" x="{x0:.1f}" y="{top:.1f}" width="{DISC}" height="{DISC}" href="{_MARK["dark"]}"/>']
    y = sig_baseline(top)
    x = x0 + DISC + 18
    seg = []
    for i, ((t, f, tr), w) in enumerate(zip(parts, widths)):
        seg.append(f'<path d="{f.path(t, SIG, x, y, track=tr)[0]}"/>')
        x += w
        if i < len(parts) - 1:
            seg.append(f'<circle cx="{x + 14 + 2:.1f}" cy="{y - medium.cap * SIG / 2:.1f}" r="2.1"/>')
            x += dot
    out.append(f'<g class="wv-ink" fill-opacity=".6">{"".join(seg)}</g>')
    return "".join(out), total


# ── A figure: elements collected with their animation step ─────────
class Fig:
    """Collects SVG with an optional step (`at`): the element appears at that step on the page
    and is always present in the static image. kind: "fade" (default) or "draw" (an arrow
    made with animate=True: its line draws in and its head follows)."""

    def __init__(self, slug, title, subtitle, source=None, alt=""):
        self.slug, self.title, self.subtitle, self.source, self.alt = slug, title, subtitle, source, alt
        self.items, self.steps, self.H = [], 0, 1000

    def add(self, svg, at=None, kind="fade", delay=0):
        self.items.append((svg, at, kind, delay))
        if at is not None:
            self.steps = max(self.steps, at)

    def body(self, animated):
        out = []
        for svg, at, kind, delay in self.items:
            if animated and at is not None:
                style = f' style="transition-delay:{delay}ms"' if delay else ""
                out.append(f'<g data-at="{at}" class="wv-g-{kind}"{style}>{svg}</g>')
            else:
                out.append(svg)
        return "".join(out)

    def chrome(self):
        """Title, subtitle, source and signature, from the canvas height."""
        out = [text(self.title, TITLE, M, M + 42)[0], text(self.subtitle, SUBTITLE, M, M + 84, muted=True)[0]]
        top = self.H - SIG_FOOT - DISC                 # the mark's top; its bottom is SIG_FOOT above the edge
        out.append(signature(W - M, top)[0])
        if self.source:                                 # bottom left, on the signature's baseline
            out.append(text(self.source, SIG, M, sig_baseline(top), muted=True)[0])
        return "".join(out)


def style(accent):
    a = ACCENTS[accent]
    light = (f".wv-ink{{fill:{INK}}}.wv-sink{{stroke:{INK}}}.wv-acc{{fill:{a['acc']}}}.wv-sacc{{stroke:{a['acc']}}}"
             f".wv-tint{{fill:{a['tint']}}}.wv-on-dark{{display:none}}")
    dark = (f".wv-ink{{fill:{CHALK}}}.wv-sink{{stroke:{CHALK}}}.wv-acc{{fill:{a['acc_dark']}}}.wv-sacc{{stroke:{a['acc_dark']}}}"
            f".wv-tint{{fill:{a['tint_dark']}}}.wv-on-light{{display:none}}.wv-on-dark{{display:inline}}")
    sel = lambda pre: "".join(pre + rule for rule in re.findall(r"\.wv-[\w-]+\{[^}]*\}", dark))
    return ("<style>" + light +
            "@media (prefers-color-scheme: dark){" + sel(':root:not([data-theme="light"]) ') + "}" +
            sel(':root[data-theme="dark"] ') + "</style>")


def svg_doc(fig, accent, animated, tight, extra_attrs=""):
    body = fig.chrome() + fig.body(animated)
    H = fig.H
    pad = 8
    if tight:
        x, y, w, h = M - pad, M - pad, W - 2 * (M - pad), H - SIG_FOOT - M + 2 * pad
        vb = f"{x} {y} {w} {h:.0f}"
    else:
        vb = f"0 0 {W} {H}"
    aid = f"{fig.slug}-t"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-labelledby="{aid}"{extra_attrs}>'
            f'<title id="{aid}">{fig.title}. {fig.alt}</title>{style(accent)}{body}</svg>')


def chrome_bin():
    c = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    return c if pathlib.Path(c).exists() else None


def render(html, w, h, out, scale=1):
    chrome = chrome_bin()
    if not chrome:
        print("  no Chrome: skipped", out.name); return
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / "r.html"; p.write_text(html, encoding="utf-8")
        subprocess.run([chrome, "--headless=new", "--hide-scrollbars", "--disable-gpu",
                        f"--window-size={w},{h}", f"--force-device-scale-factor={scale}",
                        f"--screenshot={out}", p.as_uri()], check=True, capture_output=True)


def _page(svg, theme, bg, w, h, fit=False):
    size = (f"svg{{display:block;width:{w}px;height:{h}px}}" if not fit else
            "body{display:flex;align-items:center;justify-content:center;height:100vh}svg{display:block;max-width:100%;max-height:100%}")
    return (f'<!doctype html><html data-theme="{theme}"><head><meta charset="utf-8"><style>html,body{{margin:0;background:{bg}}}'
            f'{size}</style></head><body>{svg}</body></html>')


def build(fig, accent=DEFAULT_ACCENT, variants=tuple(ACCENTS), png=True):
    d = ROOT / fig.slug
    H = fig.H
    # 1. tight SVG for the page, in the chosen accent
    (d / f"{fig.slug}.svg").write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + svg_doc(fig, accent, False, True) + "\n", encoding="utf-8")
    # 2. the animated page: page.html with the full-canvas SVG inlined, steps intact
    page = (d / "page.html").read_text(encoding="utf-8")
    inline = svg_doc(fig, accent, True, True)
    (d / "index.html").write_text(page.replace("<!-- @svg -->", inline).replace("<!-- @steps -->", str(fig.steps)), encoding="utf-8")
    print(f"  {fig.slug}.svg, index.html ({fig.steps} steps, {W}x{H})")
    if not png:
        return
    full = svg_doc(fig, accent, False, False)
    render(_page(full, "light", WHITE, W, H), W, H, d / f"{fig.slug}.png", 1)
    render(_page(full, "light", WHITE, W, H), W, H, d / f"{fig.slug}@2x.png", 2)
    render(_page(full, "dark", NIGHT, W, H), W, H, d / f"{fig.slug}-dark.png", 1)
    og = full.replace("<svg ", f'<svg width="{1200 - 2 * 24}" height="{630 - 2 * 24}" ', 1)
    render(_page(og, "light", WHITE, 1200, 630, fit=True), 1200, 630, d / f"{fig.slug}-og.png", 1)
    for v in variants:
        render(_page(svg_doc(fig, v, False, False), "light", WHITE, W, H), W, H, d / f"{fig.slug}-accent-{v}.png", 1)
    print(f"  pngs: 1x, 2x, dark, og, accents {', '.join(variants)}")
