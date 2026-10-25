"""States off the ladder. Run: python3 figure.py [--no-png]

Left, Integral Psychology (2000): one ladder of ten rungs, the four highest psychic, subtle,
causal, nondual. Right, Integral Spirituality (2006): the same four words name states, a
second axis across the top of a lattice whose rows are the six lower stages. The tint marks
the four words in both places; the accent arrow is their move. Sources: README.md.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "design-language"))
from wv import (Fig, build, text, tag, panel, line, curved_arrow, regular, medium, M, W, PAD, LW, LW2, DISC,
                SIG_FOOT, SIG_GAP, HEADING, LABEL, SECOND, TAG)

STAGES = ["archaic", "magic", "mythic", "rational", "pluralistic", "integral"]   # bottom to top
STATES = ["psychic", "subtle", "causal", "nondual"]                               # the four top rungs
COLUMNS = ["gross", "subtle", "causal", "nondual"]                                # as IS lists them (l. 1208)


def draw():
    fig = Fig("states-and-stages", "States off the ladder",
              "In 2000 the mystical states top one developmental ladder; in 2006 the same words name a second axis",
              source="Sources: Integral Psychology (2000), chart 1 · Integral Spirituality (2006), ch. 4",
              alt=("Left, a ladder of ten rungs labelled archaic to integral and then psychic, subtle, causal, "
                   "nondual, the top four in a tinted panel. An accent arrow carries those four words to the "
                   "right, where they head the four columns of a lattice whose six rows are the lower stages: "
                   "every state can occur at every stage."))
    top = M + 170
    step = 54                                     # rung spacing
    cap = medium.cap * HEADING

    # ── left: the ladder ──────────────────────────────────────────
    lx = M + 40                                   # left rail
    rail_w = 110
    label_x = lx + rail_w + 28
    rungs = STAGES + STATES                       # bottom to top
    n = len(rungs)
    ladder_top = top + 150
    ys = [ladder_top + (n - 1 - i) * step for i in range(n)]   # y of rung i (0 = bottom)
    ladder_bottom = ys[0] + step * 0.5
    # the four top rungs: one tinted panel behind rails and labels
    pw = rail_w + 28 + max(regular.width(s, LABEL) for s in STATES) + 2 * 28
    panel_top = ys[n - 1] - step * 0.55
    panel_h = ys[len(STAGES)] + step * 0.55 - panel_top
    fig.add(panel(lx - 28, panel_top, pw, panel_h), at=1)
    g = text("Integral Psychology, 2000", HEADING, M, top + cap, medium)[0]
    g += text("one ladder; the four highest rungs", SECOND, M, top + cap + 40, muted=True)[0]
    g += text("are the mystical states", SECOND, M, top + cap + 74, muted=True)[0]
    g += line([(lx, ys[n - 1] - step * 0.55), (lx, ladder_bottom)], LW2)
    g += line([(lx + rail_w, ys[n - 1] - step * 0.55), (lx + rail_w, ladder_bottom)], LW2)
    for i, name in enumerate(rungs):
        g += line([(lx, ys[i]), (lx + rail_w, ys[i])], LW2)
        g += text(name, LABEL, label_x, ys[i] + regular.xh * LABEL / 2, accent=False)[0]
    fig.add(g, at=0)

    # ── right: the lattice ────────────────────────────────────────
    rows = len(STAGES)
    colw = 176
    gx = W - M - 4 * colw                         # grid left edge; right edge on the margin
    row_label_x = gx - 28
    gy_top = ys[len(STAGES) - 1] - step / 2       # rows level with the ladder's lower six rungs
    gy_bottom = ys[0] + step / 2
    hx = row_label_x - max(regular.width(s, LABEL) for s in STAGES)   # headings start where the row labels do
    g = text("Integral Spirituality, 2006", HEADING, hx, top + cap, medium)[0]
    g += text("the same four words name states,", SECOND, hx, top + cap + 40, muted=True)[0]
    g += text("available at every stage", SECOND, hx, top + cap + 74, muted=True)[0]
    fig.add(g, at=2)
    # the states, across the top, in the tint
    ph_top = gy_top - 18 - (PAD + cap + PAD - 12)
    head_h = gy_top - 18 - ph_top
    fig.add(panel(gx, ph_top, 4 * colw, head_h), at=2)
    g = ""
    for j, name in enumerate(COLUMNS):
        g += text(name, LABEL, gx + colw * (j + 0.5), ph_top + head_h / 2 + regular.xh * LABEL / 2, anchor="middle")[0]
    fig.add(g, at=2, delay=300)
    # the grid: hairline scaffolding, no cell boxes
    g = ""
    for r in range(rows + 1):
        y = gy_top + r * step
        g += line([(gx, y), (gx + 4 * colw, y)], 1.5).replace('class="wv-sink"', 'class="wv-sink" stroke-opacity=".45"')
    for c in range(5):
        x = gx + c * colw
        g += line([(x, gy_top), (x, gy_bottom)], 1.5).replace('class="wv-sink"', 'class="wv-sink" stroke-opacity=".45"')
    for i, name in enumerate(STAGES):
        g += text(name, LABEL, row_label_x, ys[i] + regular.xh * LABEL / 2, anchor="end")[0]
    fig.add(g, at=3)

    # ── the move: one accent arrow from the top rungs to the states row ──
    p0 = (lx - 28 + pw + 24, panel_top + panel_h / 2)
    p1 = (gx - 16, ph_top + head_h / 2)
    cx = (p0[0] + p1[0]) / 2
    fig.add(curved_arrow(p0, (cx, p0[1]), (cx, p1[1]), p1, LW, accent=True, animate=True), at=2, kind="draw")

    fig.H = round(ladder_bottom + SIG_GAP + DISC + SIG_FOOT)
    return fig


if __name__ == "__main__":
    build(draw(), png="--no-png" not in sys.argv)
