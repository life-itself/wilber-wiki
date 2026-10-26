/* Wilber visuals: step controller.
 *
 * Loaded deferred on every page (config.json "head"); it does nothing unless a
 * [data-wv-steps] root exists. Contract:
 *
 *   <div class="wv-root" data-wv-steps="4" data-step="4" data-wv-dur="1400">
 *     <div class="wv-controls" data-wv-controls></div>     <- buttons are built here
 *     <p data-wv-caption><span data-cap="0">…</span><span data-cap="1">…</span>…</p>
 *     <svg>… elements with data-at="k" …</svg>
 *   </div>
 *
 * The markup defaults to data-step = N (the settled frame), which is also the
 * exported static image. Play rewinds to 0 and advances one step per
 * data-wv-dur ms (default 1400). prefers-reduced-motion: steps still work, the
 * CSS transitions are off, and Play jumps straight to the settled frame.
 * Deep links: #step-2 opens at step 2, #play starts playing.
 * Elements that exist mid-animation but not in the settled frame carry
 * data-from="a" data-until="b" and opacity="0"; they show for steps a..b-1.
 *
 * Share blocks (the site's /visuals page, built by scripts/sync-visuals.py):
 *
 *   <div class="wv-root wv-share" data-wv-share="<slug>">
 *     <img class="wv-still" src="/assets/visuals/<slug>.png" alt="…">
 *     <div data-wv-steps …>…</div>                                <- hidden until Watch
 *     <div class="wv-controls wv-actions" data-wv-actions></div>  <- buttons are built here
 *   </div>
 *
 * The image comes first so right-click and long-press work. The buttons are
 * Watch it unfold (swap in the animation and play it), Copy image (PNG to the
 * clipboard), Download (saves the file rather than opening it) and Share (the
 * system share sheet, only where it can take a file). Copy, Download and Share
 * fetch the PNG, which works across origins because the asset host sends CORS *
 * (bypassing the browser cache; see getBlob).
 */
(function () {
  'use strict';
  if (typeof document === 'undefined') return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // On a framework-rendered site (Flowershow is React) the page can be hydrated
  // or re-rendered after this script runs, replacing the nodes it set up, and
  // client-side navigation brings new roots without reloading scripts. So:
  // initialise each root once (marked .wv-ready), start after load, and watch
  // the DOM for roots that appear or are replaced later.
  function initAll() {
    Array.prototype.forEach.call(document.querySelectorAll('[data-wv-share]:not(.wv-share-ready)'), initShare);
    var roots = document.querySelectorAll('[data-wv-steps]:not(.wv-ready)');
    if (!roots.length) return;
    document.documentElement.classList.add('wv-js');
    Array.prototype.forEach.call(roots, init);
  }
  var pending = null;
  function schedule() { if (!pending) pending = setTimeout(function () { pending = null; initAll(); }, 150); }
  function start() {
    schedule();
    if (window.MutationObserver) new MutationObserver(schedule).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);

  function init(root) {
    root.classList.add('wv-ready');
    var N = parseInt(root.getAttribute('data-wv-steps'), 10) || 0;
    var dur = parseInt(root.getAttribute('data-wv-dur'), 10) || 1400;
    var timer = null;
    var controls = root.querySelector('[data-wv-controls]');
    var caption = root.querySelector('[data-wv-caption]');
    var caps = caption ? caption.querySelectorAll('[data-cap]') : [];

    function current() { return parseInt(root.getAttribute('data-step'), 10) || 0; }

    function show(k, opts) {
      opts = opts || {};
      k = Math.max(0, Math.min(N, k));
      if (!opts.animate) { root.classList.add('wv-no-motion'); }
      root.setAttribute('data-step', String(k));
      if (opts.animate) { root.classList.add('wv-armed'); }
      // data-from="a" data-until="b": shown only for steps a..b-1 (authored opacity="0",
      // so the settled frame and the exports leave it out)
      Array.prototype.forEach.call(root.querySelectorAll('[data-until]'), function (el) {
        var a = parseInt(el.getAttribute('data-from'), 10) || 0, u = parseInt(el.getAttribute('data-until'), 10);
        el.style.opacity = k >= a && k < u ? '1' : '0';
      });
      Array.prototype.forEach.call(caps, function (c) {
        c.hidden = c.getAttribute('data-cap') !== String(k);
      });
      if (controls) {
        var btns = controls.querySelectorAll('button[data-step]');
        Array.prototype.forEach.call(btns, function (b) {
          b.setAttribute('aria-pressed', b.getAttribute('data-step') === String(k) ? 'true' : 'false');
        });
        var prev = controls.querySelector('[data-act="prev"]'), next = controls.querySelector('[data-act="next"]');
        if (prev) prev.disabled = k === 0;
        if (next) next.disabled = k === N;
      }
      if (!opts.animate) {
        // force a reflow so the no-motion jump applies before transitions are re-enabled
        void root.offsetWidth;
        root.classList.remove('wv-no-motion');
      }
    }

    function stop() { if (timer) { clearInterval(timer); timer = null; } setPlaying(false); }

    function setPlaying(on) {
      if (!controls) return;
      var p = controls.querySelector('[data-act="play"]');
      if (p) { p.textContent = on ? '❚❚ Pause' : (current() === N ? '↺ Replay' : '▶ Play'); p.setAttribute('aria-pressed', on ? 'true' : 'false'); }
    }

    function play() {
      stop();
      if (reduce) { show(N); setPlaying(false); return; }
      show(0);
      root.classList.remove('wv-armed');
      void root.offsetWidth;
      setPlaying(true);
      var k = 0;
      timer = setInterval(function () {
        k += 1;
        show(k, { animate: true });
        if (k >= N) { stop(); }
      }, dur);
    }

    function step(delta) {
      stop();
      var k = current() + delta;
      if (k < 0 || k > N) return;
      show(k, { animate: !reduce && delta > 0 });
      if (k === N) { root.classList.remove('wv-armed'); }
    }

    if (controls && !controls.children.length) {
      var html = '<button type="button" data-act="play" class="is-primary" aria-pressed="false">▶ Play</button>'
        + '<span class="wv-steps" role="group" aria-label="Step">'
        + '<button type="button" data-act="prev" aria-label="Previous step">‹</button>';
      for (var i = 0; i <= N; i++) {
        html += '<button type="button" data-step="' + i + '" aria-pressed="false" aria-label="Step ' + i + (i === N ? ' (settled frame)' : '') + '">' + i + '</button>';
      }
      html += '<button type="button" data-act="next" aria-label="Next step">›</button></span>'
        + '<span class="wv-hint">' + (reduce ? 'Reduced motion: steps jump without animation.' : 'Step ' + N + ' is the static image.') + '</span>';
      controls.innerHTML = html;
    }
    if (controls) {
      controls.addEventListener('click', function (e) {
        var b = e.target.closest('button'); if (!b) return;
        var act = b.getAttribute('data-act');
        if (act === 'play') { if (timer) { stop(); } else { play(); } }
        else if (act === 'prev') { step(-1); }
        else if (act === 'next') { step(1); }
        else if (b.hasAttribute('data-step')) { stop(); show(parseInt(b.getAttribute('data-step'), 10)); root.classList.remove('wv-armed'); }
      });
    }
    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { step(1); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { step(-1); e.preventDefault(); }
      else if (e.key === ' ' && e.target === root) { if (timer) { stop(); } else { play(); } e.preventDefault(); }
    });
    if (!root.hasAttribute('tabindex')) root.setAttribute('tabindex', '0');

    // initial state: settled unless the hash says otherwise
    var m = /#step-(\d+)/.exec(location.hash);
    if (m) { show(parseInt(m[1], 10)); }
    else if (location.hash === '#play') { play(); }
    else { show(current() || N); }
    setPlaying(false);
  }
  function initShare(box) {
    box.classList.add('wv-share-ready');
    var img = box.querySelector('.wv-still');
    var actions = box.querySelector('[data-wv-actions]');
    var anim = box.querySelector('[data-wv-steps]');
    if (!img || !actions) return;
    var url = img.currentSrc || img.src;
    var name = (box.getAttribute('data-wv-share') || 'figure') + '.png';
    var blob = null;
    function getBlob() {
      // no-store: the asset host only adds CORS headers when asked and does not
      // send Vary: Origin, so the copy cached by the <img> would fail CORS.
      if (!blob) blob = fetch(url, { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.blob(); })
        .then(function (b) { return b.type === 'image/png' ? b : new Blob([b], { type: 'image/png' }); });
      blob.catch(function () { blob = null; });
      return blob;
    }
    var canCopy = !!(window.ClipboardItem && navigator.clipboard && navigator.clipboard.write);
    var canShare = false;
    try { canShare = !!(navigator.canShare && navigator.canShare({ files: [new File([''], name, { type: 'image/png' })] })); } catch (e) {}

    var html = '';
    if (anim) html += '<button type="button" data-act="watch" class="is-primary" aria-pressed="false">▶ Watch it unfold</button>';
    if (canCopy) html += '<button type="button" data-act="copy">Copy image</button>';
    html += '<button type="button" data-act="download">Download</button>';
    if (canShare) html += '<button type="button" data-act="share">Share…</button>';
    actions.innerHTML = html;
    // Share has to start from the tap itself, so fetch the file ahead of time.
    if (canShare) getBlob();

    function flash(b, text) {
      var label = b.getAttribute('data-label') || b.textContent;
      b.setAttribute('data-label', label);
      b.textContent = text;
      setTimeout(function () { b.textContent = label; }, 2000);
    }

    actions.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var act = b.getAttribute('data-act');
      if (act === 'watch') {
        var on = !box.classList.contains('wv-watching');
        box.classList.toggle('wv-watching', on);
        b.textContent = on ? '▣ Show the image' : '▶ Watch it unfold';
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        var play = on && anim.querySelector('[data-act="play"]');
        if (play) play.click();
      } else if (act === 'copy') {
        // Safari needs the ClipboardItem made inside the click, holding a promise.
        navigator.clipboard.write([new ClipboardItem({ 'image/png': getBlob() })])
          .then(function () { flash(b, 'Copied ✓'); }, function () { flash(b, 'Copy failed'); });
      } else if (act === 'download') {
        getBlob().then(function (data) {
          var a = document.createElement('a');
          a.href = URL.createObjectURL(data); a.download = name;
          document.body.appendChild(a); a.click(); a.remove();
          setTimeout(function () { URL.revokeObjectURL(a.href); }, 10000);
          flash(b, 'Saved ✓');
        }, function () { window.open(url, '_blank'); });
      } else if (act === 'share') {
        getBlob().then(function (data) {
          return navigator.share({ files: [new File([data], name, { type: 'image/png' })], title: img.alt.split('. ')[0] });
        }).catch(function () {});
      }
    });
  }
})();
