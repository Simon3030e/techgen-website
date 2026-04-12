/* ================================================
   Nokto Studio — animations.js
   Scroll-reveal (IntersectionObserver) + counter animations
   ================================================ */

(function () {
  'use strict';

  /* ── 1. SCROLL-REVEAL ─────────────────────────────── */
  const revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window && revealEls.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    /* Fallback: show everything immediately */
    revealEls.forEach((el) => el.classList.add('visible'));
  }

  /* ── 2. TRUST-STAT COUNTER ────────────────────────── */
  function animateCounter(el) {
    const raw  = el.getAttribute('data-count') || el.textContent;
    const num  = parseFloat(raw.replace(/[^0-9.]/g, ''));
    const suffix = raw.replace(/[0-9.]/g, '');   // keeps "+", "k", "%" etc.
    if (isNaN(num)) return;

    const duration = 1600;   // ms
    const fps      = 60;
    const steps    = Math.round(duration / (1000 / fps));
    let   current  = 0;
    let   frame    = 0;

    const tick = () => {
      frame++;
      /* Ease-out cubic */
      const progress = 1 - Math.pow(1 - frame / steps, 3);
      current = num * progress;

      /* Display with same decimal places as original */
      const display = Number.isInteger(num)
        ? Math.round(current)
        : current.toFixed(1);

      el.textContent = display + suffix;

      if (frame < steps) requestAnimationFrame(tick);
      else el.textContent = num + suffix; /* Snap to exact value */
    };

    requestAnimationFrame(tick);
  }

  const counters = document.querySelectorAll('.trust-num');

  if ('IntersectionObserver' in window && counters.length) {
    const counterIO = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            /* Store original text as data-count before overwriting */
            if (!entry.target.hasAttribute('data-count')) {
              entry.target.setAttribute('data-count', entry.target.textContent.trim());
            }
            animateCounter(entry.target);
            counterIO.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    counters.forEach((el) => counterIO.observe(el));
  }

  /* ── 3. ACTIVE NAV LINK ───────────────────────────── */
  (function markActiveNav() {
    const links = document.querySelectorAll('.nav-links a');
    const path  = window.location.pathname.replace(/\/$/, '') || '/';

    links.forEach((a) => {
      const href = a.getAttribute('href').replace(/\/$/, '') || '/';
      if (href === path || (href !== '/' && path.startsWith(href))) {
        a.classList.add('active');
      }
    });
  })();

})();
