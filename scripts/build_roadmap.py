#!/usr/bin/env python3
"""Generate roadmap.md from the structure defined here.

The roadmap's *sequence* is argued for in docs/concept-roadmap.md; this script
holds the same structure in machine-readable form and emits the page, so the two
never drift by hand-editing. Re-run after changing the spine:

    python3 scripts/build_roadmap.py

Styling lives in assets/roadmap/roadmap.css (loaded via config.json's "head"),
NOT in Tailwind utilities: Flowershow ships a fixed pre-purged Tailwind bundle,
so arbitrary utility classes written in page content are never compiled.
"""

import os
import sys

C = "/concepts/"

# (slug, title, blurb, essential?, flag, [(side, slug, title, note), ...])
ACTS = [
    dict(
        num="Act I",
        title="The universe has an inside",
        sub='The ontology. What sort of thing exists, and what is the basic unit? '
            '&mdash; <em>&ldquo;the single most persistent worldview in history.&rdquo;</em>',
        stops=[
            ("great-chain-of-being", "The Great Chain of Being",
             "Start here. Matter, life, mind, spirit: the picture nearly every premodern "
             "culture converged on. Wilber&rsquo;s whole project is asking whether they were "
             "onto something.", False, None, []),
            ("kosmos-vs-cosmos", "Kosmos vs. Cosmos",
             "What modernity dropped. Is reality the physical universe, or matter <em>plus</em> "
             "life, mind, and spirit? Everything follows from which one you think you live in.",
             False, None, []),
            ("holons", "Holons",
             "The basic unit: everything is a whole that is also a part. Not things, not "
             "processes &mdash; whole/parts, all the way up and down.", True, None, [
                 ("right", "systems-theory", "Systems Theory",
                  "the closest rival account, and where it falls short"),
                 ("right", "two-arrows-of-time", "Two Arrows of Time",
                  "physics says decay, biology says ascent"),
                 ("right", "eros-and-agape", "Eros and Agape",
                  "first sense: the drives of every holon (returns at stop 16)"),
             ]),
            ("holarchy", "Holarchy",
             "How holons nest &mdash; and the word that costs Wilber more readers than any "
             "other: <em>hierarchy</em>.", False, None, [
                 ("left", "dominator-vs-growth-hierarchy", "Dominator vs. Growth Hierarchy",
                  "the defence the rest of the book depends on"),
                 ("left", "great-plenitude", "The Great Plenitude",
                  "Lovejoy&rsquo;s principle as a research programme"),
             ]),
            ("interiority", "Interiority",
             "Every holon has an inside as well as an outside. The single move that separates "
             "Wilber from every systems theorist he otherwise resembles.", False, None, [
                 ("right", "limits-of-the-exterior-approach", "The Limits of the Exterior Approach",
                  "why no amount of science reaches the inside"),
             ]),
        ],
    ),
    dict(
        num="Act II",
        title="Four faces of every moment",
        sub="Interiority plus holarchy gives you a grid. The grid is the famous part &mdash; "
            "this is what people mean by AQAL. <em>Each facet requires its own mode of knowing.</em>",
        stops=[
            ("four-quadrants", "The Four Quadrants",
             "Interior/exterior by individual/collective. AQAL&rsquo;s load-bearing diagram, and "
             "the one picture most people have seen even if they have read nothing.", True, None, [
                 ("right", "micro-macro-coevolution", "Micro/Macro Coevolution",
                  "why the columns can never collapse into one another"),
             ]),
            ("big-three", "The Big Three",
             "I / We / It &mdash; art, morals, science. The quadrants in their classical, "
             "pre-Wilber clothing: Kant&rsquo;s three critiques, Popper&rsquo;s three worlds.",
             False, None, [
                 ("left", "right-hand-and-left-hand-paths", "Right-Hand and Left-Hand Paths",
                  "two different kinds of language the grid demands"),
             ]),
            ("flatland", "Flatland",
             "The diagnosis &mdash; and only nameable now you have the grid. Modernity collapsed "
             "the Left-Hand quadrants into the Right, re-describing everything interior as an "
             "&ldquo;it.&rdquo;", True, None, [
                 ("right", "dignity-and-disaster-of-modernity", "The Dignity and Disaster of Modernity",
                  "the fair version: differentiation before dissociation"),
             ]),
        ],
    ),
    dict(
        num="Act III",
        title="Growing up doesn&rsquo;t stop where you think",
        sub="Holarchy applied to consciousness. This is where Wilber gets contentious &mdash; "
            "<em>&ldquo;you have to be somebody before you can be nobody.&rdquo;</em>",
        stops=[
            ("waves-and-streams", "Waves and Streams",
             "Levels of consciousness vs. the developmental lines running through them &mdash; "
             "why someone can be cognitively advanced and morally stunted.", True, None, []),
            ("dialectic-of-progress", "The Dialectic of Progress",
             "Every stage solves the last one&rsquo;s central problem and creates a new one. The "
             "structural rebuttal to both &ldquo;it all keeps getting better&rdquo; and &ldquo;we "
             "have fallen from Eden.&rdquo;", False, None, [
                 ("left", "primal-ecological-wisdom", "The Myth of Primal Ecological Wisdom",
                  "the worked example, and a live argument"),
             ]),
            ("pre-trans-fallacy", "The Pre/Trans Fallacy",
             "Prerational and transrational both look nonrational, so they get confused &mdash; "
             "reduced downward (Freud) or elevated upward (Jung, Campbell). Almost every "
             "misreading of Wilber, in either direction, is this error. Nothing past here is "
             "readable without it.", True, "The guardrail", []),
            ("vision-logic", "Vision-Logic",
             "The first stop past formal rationality: postformal, network-and-context cognition "
             "&mdash; and where Wilber locates <em>us</em>, now.", False, None, [
                 ("right", "postmodernism", "Wilber on Postmodernism",
                  "postmodernism <em>is</em> early vision-logic: its achievement and its derailment"),
             ]),
            ("transpersonal-domains", "The Transpersonal Domains",
             "Development continuing past the personal. &ldquo;Personal plus, not personal "
             "minus&rdquo; &mdash; exactly the claim the guardrail was protecting.", False, None, [
                 ("left", "psychic-subtle-causal-nondual", "Psychic, Subtle, Causal, Nondual",
                  "the four stages, named and distinguished"),
             ]),
            ("validity-claims-of-mysticism", "Validity Claims of Mysticism",
             "The epistemology stop, and Wilber&rsquo;s most interesting move: contemplative "
             "claims can be checked &mdash; if you are willing to run the experiment.",
             False, None, [
                 ("right", "reconstruction-of-the-contemplative-path",
                  "Reconstruction of the Contemplative Path",
                  "injunction, apprehension, confirmation"),
             ]),
        ],
    ),
    dict(
        num="Act IV",
        title="How the West lost its inside",
        sub="Two thousand years of getting it half-right, and what Spirit has to do with any of "
            "it &mdash; <em>&ldquo;every neurosis is a miniature ecological crisis.&rdquo;</em>",
        stops=[
            ("ascent-and-descent", "Ascent and Descent",
             "The two eternal movements: wisdom&rsquo;s return to the One, compassion&rsquo;s "
             "embrace of the Many. Book Two of <em>SES</em> is the history of their divorce.",
             True, None, [
                 ("right", "wilber-on-plato", "Wilber&rsquo;s Non-Dual Plato",
                  "where both are still held together"),
                 ("right", "the-two-gods", "The Two Gods",
                  "the transcendent God vs. the &ldquo;schizoid God&rdquo;"),
             ]),
            ("eros-and-agape", "Eros and Agape",
             "The same pair you met at stop 3, now doing their second job: the motive forces "
             "behind Ascent and Descent &mdash; and their pathologies, Phobos and Thanatos.",
             False, None, [
                 ("left", "repression", "Repression",
                  "the pathology at civilizational scale"),
             ]),
            ("ego-camp-and-eco-camp", "The Ego Camp and the Eco Camp",
             "The book&rsquo;s central polemic, and the reason it runs 800 pages: Ascenders and "
             "Descenders, each half-right, each unable to hear the other.", False, None, [
                 ("right", "agony-of-modernity-fichte-vs-spinoza", "The Agony of Modernity",
                  "Fichte vs. Spinoza: the split at its sharpest"),
                 ("right", "legacy-of-the-idealists", "The Legacy of the Idealists",
                  "the one real attempt at synthesis, and why it collapsed"),
             ]),
            ("death-of-god", "The Death of God",
             "Not secularization as a loss of faith, but as the Descended camp&rsquo;s total "
             "historical victory &mdash; flatland becoming common sense.", False, None, []),
            ("involution-and-evolution", "Involution and Evolution",
             "The final turn: evolution as Spirit&rsquo;s unfolding <em>back</em> toward itself, "
             "having first enfolded itself into matter.", False, None, [
                 ("right", "spirit-in-action", "Spirit-in-Action",
                  "the panentheism the whole system was built to make sayable"),
             ]),
        ],
    ),
]

TOPICS = [
    ("postmodernism", "Postmodernism"),
    ("environmental-ethics", "Environmental ethics"),
    ("sex-and-gender", "Sex and gender"),
    ("sexuality-and-modernity", "Sexuality and modernity"),
    ("multiculturalism-and-transnationalism", "Multiculturalism"),
]

CONTESTED = [
    ("pre-trans-fallacy", "Pre/trans fallacy"),
    ("dominator-vs-growth-hierarchy", "Hierarchy"),
    ("environmental-ethics", "Ranking value"),
    ("primal-ecological-wisdom", "Primal ecological wisdom"),
    ("sex-and-gender", "Sex and gender"),
    ("dialectic-of-progress", "Progress"),
]


def chips(items, cls="wr-chip"):
    return "\n".join(
        f'    <a href="{C}{slug}" className="{cls}">{label}</a>' for slug, label in items
    )


def render():
    out = []
    w = out.append

    w("---")
    w("title: Wilber Roadmap")
    w("layout: plain")
    w("showSidebar: false")
    w("showToc: false")
    w("---")
    w("")
    w('<div className="wr-root">')
    w('<div className="wr-wrap">')
    w("")

    # header
    w('<a href="/" className="wr-eyebrow">Wilber Wiki</a>')
    w("")
    w('<h1 className="wr-title">A Roadmap Through Ken Wilber</h1>')
    w("")
    w('<p className="wr-lede">Forty-one ideas, in an order that actually builds. Follow the '
      "spine from top to bottom, or take the six-stop express route. Side branches are "
      "optional on a first pass.</p>")
    w("")
    w('<div className="wr-banner"><strong>This is Wilber circa 1995.</strong> Every page here '
      "is sourced from <em>Sex, Ecology, Spirituality</em> &mdash; the phase-four turn in a body "
      "of work with five acknowledged phases. He revised real things afterwards. See the "
      '<a href="/bio">biography</a> and <a href="/works">the works</a> for how his thinking '
      "moved.</div>")
    w("")

    # entrances
    w('<div className="wr-panels">')
    w('  <div className="wr-panel">')
    w('    <div className="wr-panel__kicker">Entrance 1</div>')
    w('    <div className="wr-panel__title">New to Wilber?</div>')
    w('    <p className="wr-panel__body">Start at stop 1 and walk down. If you only have an '
      "afternoon, follow the six stops marked with a star &mdash; that is a genuinely coherent "
      "minimal Wilber: the units, the map, the ladder, the diagnosis, the guardrail, the "
      "payoff.</p>")
    w('    <a href="#act-1" className="wr-cta">Begin at the top &darr;</a>')
    w("  </div>")
    w('  <div className="wr-panel wr-panel--dashed">')
    w('    <div className="wr-panel__kicker">Entrance 2</div>')
    w('    <div className="wr-panel__title">Here for one topic?</div>')
    w('    <p className="wr-panel__body">Most people arrive looking for Wilber on a specific '
      "subject. Go straight there &mdash; each page links back onto the spine.</p>")
    w('    <div className="wr-chips">')
    w(chips(TOPICS))
    w("    </div>")
    w("  </div>")
    w("</div>")
    w("")

    # contested rail
    w('<div className="wr-panel wr-panel--wide">')
    w('  <div className="wr-panel__kicker">If you are unconvinced</div>')
    w('  <div className="wr-panel__title">Where Wilber is most contested</div>')
    w('  <p className="wr-panel__body">Every page on this wiki says plainly what is strong in '
      "Wilber&rsquo;s argument and what is weak. These are the six where the objections bite "
      "hardest &mdash; a fair place to start if you suspect the whole thing is too neat.</p>")
    w('  <div className="wr-chips">')
    w(chips(CONTESTED, "wr-chip wr-chip--solid"))
    w("  </div>")
    w("</div>")
    w("")

    # legend
    w('<div className="wr-legend">')
    w('  <div><span className="wr-swatch"></span><span>Spine &mdash; read in order</span></div>')
    w('  <div><span className="wr-swatch wr-swatch--star"></span><span>&#9733; The essential six</span></div>')
    w('  <div><span className="wr-swatch wr-swatch--branch"></span><span>Branch &mdash; optional depth</span></div>')
    w("</div>")
    w("")

    n = 0
    for i, act in enumerate(ACTS, start=1):
        w(f'<div className="wr-act wr-act-{i}" id="act-{i}">')
        w('  <div className="wr-act__band">')
        w(f'    <div className="wr-act__num">{act["num"]}</div>')
        w(f'    <div className="wr-act__title">{act["title"]}</div>')
        w(f'    <p className="wr-act__sub">{act["sub"]}</p>')
        w("  </div>")
        w("</div>")
        w("")
        w(f'<div className="wr-spine wr-act-{i}">')
        w("")
        for slug, title, blurb, star, flag, branches in act["stops"]:
            n += 1
            w('<div className="wr-stop">')
            node_cls = "wr-node wr-node--star" if star else "wr-node"
            w(f'  <div className="{node_cls}">')
            w(f'    <div className="wr-num">{n}</div>')
            w('    <div className="wr-node__head">')
            w(f'      <a href="{C}{slug}" className="wr-node__title">{title}</a>')
            if star:
                w('      <span className="wr-star">&#9733;</span>')
            w("    </div>")
            if flag:
                w(f'    <div className="wr-node__flag">{flag}</div>')
            w(f'    <p className="wr-node__body">{blurb}</p>')
            w("  </div>")
            for side in ("left", "right"):
                sel = [b for b in branches if b[0] == side]
                if not sel:
                    continue
                w(f'  <div className="wr-branches wr-branches--{side}">')
                for _, bslug, btitle, bnote in sel:
                    w(f'    <a href="{C}{bslug}" className="wr-branch">')
                    w(f'      <span className="wr-branch__title">{btitle}</span>')
                    w(f'      <span className="wr-branch__note">{bnote}</span>')
                    w("    </a>")
                w("  </div>")
            w("</div>")
            w("")
        w("</div>")
        w("")

    # outro
    w('<div className="wr-outro">')
    w('  <div className="wr-outro__title">You reached the end of the spine</div>')
    w(f'  <p className="wr-outro__body">{n} stops, four acts, and one argument: that the '
      "universe has an inside, that insides develop, and that modernity built a civilization "
      "which cannot see either. What Wilber does with that claim is the rest of the wiki.</p>")
    w('  <div className="wr-outro__links">')
    w('    <a href="/concepts" className="wr-cta">All 41 concepts</a>')
    w('    <a href="/people" className="wr-chip">The thinkers he argues with</a>')
    w('    <a href="/works" className="wr-chip">The books</a>')
    w("  </div>")
    w("</div>")
    w("")
    w('<p className="wr-foot">Sequence and rationale: see docs/concept-roadmap.md in the '
      "repository.</p>")
    w("")
    w("</div>")
    w("</div>")
    return "\n".join(out) + "\n", n


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    text, n = render()
    path = os.path.join(root, "roadmap.md")
    with open(path, "w") as f:
        f.write(text)

    # Sanity: every concept page must be reachable from the roadmap exactly once,
    # counting spine stops, branches, and the topic side-entrance. Guards against
    # a new concept page being added without being placed (see docs/concept-roadmap.md).
    ALLOWED_DUPES = {
        # Eros and Agape does genuine double duty: the drives of every holon
        # (stop 3) and the motive forces of Ascent/Descent (stop 16).
        "eros-and-agape",
        # Postmodernism is both the commonest search term (side entrance) and a
        # real part of the vision-logic argument (branch of stop 12).
        "postmodernism",
    }

    slugs = []
    for act in ACTS:
        for stop in act["stops"]:
            slugs.append(stop[0])
            slugs += [b[1] for b in stop[5]]
    entrance = [s for s, _ in TOPICS]
    reachable = slugs + entrance

    on_disk = {f[:-3] for f in os.listdir(os.path.join(root, "concepts"))
               if f.endswith(".md") and f != "index.md"}
    missing = sorted(on_disk - set(reachable))
    unknown = sorted(set(reachable) - on_disk)
    dupes = sorted({s for s in reachable
                    if reachable.count(s) > 1 and s not in ALLOWED_DUPES})

    print(f"wrote {path}: {n} spine stops, {len(slugs)} spine/branch placements, "
          f"{len(entrance)} side-entrance topics, {len(on_disk)} concept pages")
    ok = True
    for label, items in (("NOT PLACED", missing),
                         ("NO SUCH PAGE", unknown),
                         ("UNEXPECTED DUPLICATE", dupes)):
        if items:
            print(f"  {label}: {items}")
            ok = False
    print("  coverage OK" if ok else "  COVERAGE FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
