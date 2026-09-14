# Works Hub Design

## Purpose

The Works landing page should help a reader choose how to enter Ken Wilber's
bibliography. A first-time visitor usually needs a recommendation, while returning
or research-oriented visitors may instead want the complete chronology or the
development of Wilber's thought.

## Information architecture

`/works` becomes a reader-first hub with three routes:

1. **What should I read?** — the recommended and visually dominant route. It jumps
   to a concise recommendation on the same page and links onward to the full guide.
2. **Browse all works** — the complete chronological catalog at `/works/catalog`.
3. **Follow the evolution of his thought** — Wilber I–V and the Kosmos trilogy at
   `/works/phases`.

The existing complete reading guide remains at `/works/reading-guide`. The existing
chronological content moves from `works/index.md` to `works/catalog.md`; it is not
duplicated below the hub.

## Page composition

The page opens with a brief explanation of the three ways into the works. The route
chooser is asymmetric: the recommended route is a large feature panel, with the two
reference routes presented as quieter secondary panels.

Below it, an editorial book sequence makes the recommendation useful without another
click. *A Brief History of Everything* is presented as an optional, accessible
entrance. The main route then connects *Sex, Ecology, Spirituality*, *Integral
Psychology*, and *Integral Spirituality*. Each entry uses the existing cover image,
a functional role label, a short explanation, and a link to the work page.

The sequence ends with a clear link to the full reading guide, which retains subject
branches, intellectual-history additions, edition relationships, and advice about
introductions and collections.

## Visual and responsive behavior

The design should feel like an edited bookshelf rather than a generic card grid.
Covers retain their portrait proportions inside consistent frames. On wide screens,
the main route reads left to right as a connected sequence; on narrow screens it
stacks in reading order. All links remain ordinary semantic anchors with visible
keyboard focus and descriptive text.

No new images or factual claims are needed. The page uses existing cover assets and
the established Markdown-plus-HTML/Tailwind capabilities already used by the site.

## Success criteria

- A newcomer can identify the recommended starting point in the first viewport.
- A catalog-seeking visitor can reach the complete chronology without scrolling.
- The recommended sequence and the distinction between an optional introduction and
  the three-book main route are clear without reading the full guide.
- The layout remains legible and correctly ordered on mobile and desktop.
- Existing links intended to reach the chronological catalog point to its new route.

