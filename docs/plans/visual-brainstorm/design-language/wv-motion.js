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
 */
(function () {
  'use strict';
  if (typeof document === 'undefined') return;
  var roots = document.querySelectorAll('[data-wv-steps]');
  if (!roots.length) return;
  document.documentElement.classList.add('wv-js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  Array.prototype.forEach.call(roots, function (root) {
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
  });
})();
