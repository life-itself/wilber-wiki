"""The Pre/Trans Fallacy, in one picture. Run: python3 figure.py [--no-png]

Three tiers of development, bottom to top: prerational, rational, transrational. The two
outer tiers share the tint because both are nonrational and, to the untutored eye, alike.
The two errors are the only accent marks: reductionism reads the transrational down as
prerational (Freud), elevationism reads the prerational up as transrational (Jung). Each
arrow skips over the rational tier, which is the point. Source: SES ch. 6 (README.md).
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "design-language"))
from wv import (Fig, build, text, panel, arrow, regular, medium, M, W, PAD, LW, SIG_FOOT, SIG_GAP, DISC,
                HEADING, LABEL, SECOND)

TIERS = [  # top to bottom: name, secondary line, tinted?
    ("Transrational", "mystical, contemplative, postformal", True),
    ("Rational", "the ego, formal reason", False),
    ("Prerational", "infantile, magical, mythic", True),
]
ERRORS = {  # name, two secondary lines
    "down": ("Reductionism", ["the transrational read", "as prerational (Freud)"]),
    "up":   ("Elevationism", ["the prerational read", "as transrational (Jung)"]),
}


def draw():
    fig = Fig("pre-trans-fallacy", "The Pre/Trans Fallacy",
              "Before reason and beyond it both look nonrational, so each gets mistaken for the other",
              source="Source: Ken Wilber, Sex, Ecology, Spirituality (1995), ch. 6",
              alt=("Three tiers of development stacked vertically, prerational at the bottom, rational in the "
                   "middle, transrational on top; the outer two are tinted because both are nonrational. "
                   "Two accent arrows skip the rational tier: reductionism reads the transrational down as "
                   "prerational (Freud), elevationism reads the prerational up as transrational (Jung)."))
    top = M + 170
    cap = medium.cap * HEADING
    pw = max(max(medium.width(n, HEADING), regular.width(s, SECOND)) for n, s, _ in TIERS) + 2 * PAD
    ph = PAD + cap + 8 + 36 + PAD           # heading cap, gap, secondary baseline, pad
    gap = 56
    px = (W - pw) / 2
    ys = []
    for i, (name, second, tinted) in enumerate(TIERS):
        y = top + i * (ph + gap)
        ys.append(y)
        g = ""
        if tinted:
            g += panel(px, y, pw, ph)
        g += text(name, HEADING, px + PAD, y + PAD + cap, medium)[0]
        g += text(second, SECOND, px + PAD, y + PAD + cap + 8 + 36, muted=True)[0]
        fig.add(g, at=0)
    mid = [y + ph / 2 for y in ys]
    bottom = ys[-1] + ph

    # the two errors: accent arrows beside the stack, each from the tier it misreads to the tier
    # it mistakes it for, labelled at the height of the rational tier they skip
    off = 64
    for key, x, step in (("down", px + pw + off, 1), ("up", px - off, 2)):
        name, lines = ERRORS[key]
        if key == "down":
            pts = [(x, mid[0]), (x, mid[2])]
            lx, anchor = x + 34, "start"
        else:
            pts = [(x, mid[2]), (x, mid[0])]
            lx, anchor = x - 34, "end"
        fig.add(arrow(pts, LW, accent=True, animate=True), at=step, kind="draw")
        ly = ys[1] + PAD + cap                      # on the Rational tier's baselines
        g = text(name, LABEL, lx, ly, anchor=anchor)[0]
        for j, ln in enumerate(lines):
            g += text(ln, SECOND, lx, ly + 44 + j * 34, anchor=anchor, muted=True)[0]
        fig.add(g, at=step, delay=500)

    fig.H = round(bottom + SIG_GAP + DISC + SIG_FOOT)
    return fig


if __name__ == "__main__":
    build(draw(), png="--no-png" not in sys.argv)
