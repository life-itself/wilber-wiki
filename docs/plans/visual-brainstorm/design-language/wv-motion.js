/* Wilber Wiki figures: step controller. Deferred; does nothing without a [data-wv-steps] root.
 * Markup sits at data-step="N" (the settled frame, which is the static image). Play rewinds to 0
 * and advances one step per data-wv-dur ms (default 2200). Steps back are instant cuts.
 * prefers-reduced-motion: Play jumps straight to the settled frame; steps still work.
 * Deep links: #step-2 opens at step 2, #play starts playing. Keyboard: arrows step, space plays. */
(function () {
  'use strict';
  var roots = document.querySelectorAll('[data-wv-steps]');
  if (!roots.length) return;
  document.documentElement.classList.add('wv-js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  Array.prototype.forEach.call(roots, function (root) {
    var N = parseInt(root.getAttribute('data-wv-steps'), 10) || 0;
    var dur = parseInt(root.getAttribute('data-wv-dur'), 10) || 2200;
    var timer = null;
    var controls = root.querySelector('[data-wv-controls]');
    var caps = root.querySelectorAll('[data-wv-caption] [data-cap]');
    var current = function () { return parseInt(root.getAttribute('data-step'), 10) || 0; };

    function show(k, animate) {
      k = Math.max(0, Math.min(N, k));
      if (!animate) root.classList.add('wv-no-motion');
      root.setAttribute('data-step', String(k));
      Array.prototype.forEach.call(caps, function (c) { c.hidden = c.getAttribute('data-cap') !== String(k); });
      if (controls) {
        Array.prototype.forEach.call(controls.querySelectorAll('button[data-step]'), function (b) {
          b.setAttribute('aria-pressed', b.getAttribute('data-step') === String(k) ? 'true' : 'false');
        });
        var play = controls.querySelector('[data-act="play"]');
        if (play && !timer) play.textContent = k === N ? 'Replay' : 'Play';
      }
      if (!animate) { void root.offsetWidth; root.classList.remove('wv-no-motion'); }
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } var p = controls && controls.querySelector('[data-act="play"]'); if (p) p.textContent = current() === N ? 'Replay' : 'Play'; }
    function play() {
      stop();
      if (reduce) { show(N, false); return; }
      show(0, false);
      var p = controls && controls.querySelector('[data-act="play"]'); if (p) p.textContent = 'Pause';
      var k = 0;
      timer = setInterval(function () { k += 1; show(k, true); if (k >= N) stop(); }, dur);
    }
    function step(d) { stop(); var k = current() + d; if (k < 0 || k > N) return; show(k, !reduce && d > 0); }

    if (controls && !controls.children.length) {
      var html = '<button type="button" data-act="play">Play</button><span class="wv-steps" role="group" aria-label="Step">';
      for (var i = 0; i <= N; i++) html += '<button type="button" data-step="' + i + '" aria-pressed="false" aria-label="Step ' + i + (i === N ? ', the settled frame' : '') + '">' + i + '</button>';
      html += '</span><span class="wv-hint">' + (reduce ? 'Reduced motion: steps cut, nothing moves.' : 'Step ' + N + ' is the image.') + '</span>';
      controls.innerHTML = html;
      controls.addEventListener('click', function (e) {
        var b = e.target.closest('button'); if (!b) return;
        if (b.getAttribute('data-act') === 'play') { timer ? stop() : play(); }
        else if (b.hasAttribute('data-step')) { stop(); show(parseInt(b.getAttribute('data-step'), 10), false); }
      });
    }
    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { step(1); e.preventDefault(); }
      else if (e.key === 'ArrowLeft') { step(-1); e.preventDefault(); }
      else if (e.key === ' ' && e.target === root) { timer ? stop() : play(); e.preventDefault(); }
    });
    if (!root.hasAttribute('tabindex')) root.setAttribute('tabindex', '0');

    var m = /#step-(\d+)/.exec(location.hash);
    if (m) show(parseInt(m[1], 10), false);
    else if (location.hash === '#play') play();
    else show(N, false);
  });
})();
