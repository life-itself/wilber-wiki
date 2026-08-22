/**
 * Phase 1 annotation display (wilber-wiki annotatable reading layer).
 *
 * For every element with [data-annotations="<path-to-json>"], fetch the
 * JSON file (array of {id, quote, comment}), find each `quote` inside the
 * element's text, wrap it in <mark class="annotation-highlight">, and
 * render each `comment` as a margin sidenote aligned to its highlight
 * (falls back to an inline note on narrow viewports, via CSS).
 *
 * Self-contained on purpose: no external annotation-engine dependency for
 * this read-only display path. Same {quote, comment} data shape that
 * @recogito/text-annotator expects (target.selector.quote / body text), so
 * swapping in that library for the *write* path (Phase 2: adding new
 * annotations live) doesn't require changing this JSON format.
 */
(function () {
  function findTextNodes(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    const nodes = [];
    let n;
    while ((n = walker.nextNode())) nodes.push(n);
    return nodes;
  }

  // Normalizes typographic quotes/apostrophes/dashes to their plain-ASCII
  // equivalents (1 char -> 1 char, so offsets stay valid against the
  // original string) — the JSON's quotes are copied from the book source
  // (curly), but the rendered page text may or may not have been passed
  // through a "smart quotes" typography step. Matching on normalized text
  // means it works either way.
  function normalize(s) {
    return s
      .replace(/[‘’]/g, "'")
      .replace(/[“”]/g, '"')
      .replace(/[–—]/g, '-');
  }

  // Finds the first occurrence of `quote` across a run of text nodes
  // (it may span multiple nodes/tags) and wraps it in a <mark>.
  function highlightQuote(root, quote, id) {
    const nodes = findTextNodes(root);
    const full = nodes.map((n) => n.textContent).join('');
    const idx = normalize(full).indexOf(normalize(quote));
    if (idx === -1) return null;

    let pos = 0;
    let startNode, startOffset, endNode, endOffset;
    for (const node of nodes) {
      const len = node.textContent.length;
      if (startNode === undefined && idx < pos + len) {
        startNode = node;
        startOffset = idx - pos;
      }
      if (endNode === undefined && idx + quote.length <= pos + len) {
        endNode = node;
        endOffset = idx + quote.length - pos;
        break;
      }
      pos += len;
    }
    if (!startNode || !endNode) return null;

    const range = document.createRange();
    range.setStart(startNode, startOffset);
    range.setEnd(endNode, endOffset);

    const mark = document.createElement('mark');
    mark.className = 'annotation-highlight';
    mark.dataset.annotationId = id;
    try {
      range.surroundContents(mark);
    } catch (e) {
      // Range spans multiple elements (surroundContents needs one
      // container) — skip highlighting this one rather than break the page.
      return null;
    }
    return mark;
  }

  function renderSidenotes(container, annotations, highlightEls) {
    const layout = document.createElement('div');
    layout.className = 'annotation-layout';
    layout.style.display = 'grid';
    layout.style.gridTemplateColumns = '1fr 260px';
    layout.style.gap = '2rem';

    const textCol = document.createElement('div');
    while (container.firstChild) textCol.appendChild(container.firstChild);
    layout.appendChild(textCol);
    container.appendChild(layout);

    const noteCol = document.createElement('div');
    noteCol.className = 'annotation-sidenotes';
    layout.appendChild(noteCol);

    annotations.forEach((a) => {
      const mark = highlightEls[a.id];
      if (!mark) return;

      // Margin note, positioned to line up with the highlight.
      const note = document.createElement('div');
      note.className = 'annotation-sidenote';
      note.dataset.annotationId = a.id;
      note.textContent = a.comment;
      noteCol.appendChild(note);

      // Inline fallback for narrow viewports (CSS toggles which shows).
      const inline = document.createElement('div');
      inline.className = 'annotation-sidenote-inline';
      inline.textContent = a.comment;
      mark.insertAdjacentElement('afterend', inline);

      const position = () => {
        const top = mark.getBoundingClientRect().top - textCol.getBoundingClientRect().top;
        note.style.top = top + 'px';
      };
      position();
      window.addEventListener('resize', position);

      const activate = () => {
        mark.classList.add('is-active');
        note.classList.add('is-active');
      };
      const deactivate = () => {
        mark.classList.remove('is-active');
        note.classList.remove('is-active');
      };
      mark.addEventListener('mouseenter', activate);
      mark.addEventListener('mouseleave', deactivate);
      note.addEventListener('mouseenter', activate);
      note.addEventListener('mouseleave', deactivate);
    });
  }

  // Annotation data is read from an inline <script type="application/json">
  // that's the container's first child, NOT fetched from the `data-annotations`
  // URL — Flowershow serves repo files (including /assets/... and JSON data
  // files) via a redirect to its R2 storage origin, which doesn't send
  // Access-Control-Allow-Origin, so a same-origin `fetch()` that follows that
  // redirect is blocked by CORS in a real browser (confirmed against the
  // published preview site; curl doesn't enforce CORS so this was easy to
  // miss). `data-annotations` is kept as a human-readable pointer to the
  // matching JSON file in `annotated/annotations/` (for anyone editing the
  // annotations, and as the natural shape for a future fetch-based Phase 2
  // write path once that's served with proper CORS/from our own API), but
  // the inline script tag is the actual source of truth read at runtime.
  function initContainer(container) {
    if (!container.dataset.annotations) return;
    container.classList.add('annotated-text');

    const dataEl = container.querySelector('script[type="application/json"]');
    if (!dataEl) {
      console.error('annotator.js: no inline annotation data found in', container);
      return;
    }

    let annotations;
    try {
      annotations = JSON.parse(dataEl.textContent);
    } catch (err) {
      console.error('annotator.js: failed to parse inline annotation data', err);
      return;
    }
    dataEl.remove();

    const highlightEls = {};
    annotations.forEach((a) => {
      const mark = highlightQuote(container, a.quote, a.id);
      if (mark) highlightEls[a.id] = mark;
    });
    renderSidenotes(container, annotations, highlightEls);
  }

  function init() {
    document.querySelectorAll('[data-annotations]').forEach(initContainer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
