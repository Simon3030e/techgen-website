/**
 * Nokto Studio - slider.js
 * Results slider: scroll-snap carousel with prev/next buttons and dots.
 */
(function () {
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.results-slider').forEach(slider => {
      const viewport = slider.querySelector('.rs-viewport');
      const prev = slider.querySelector('.rs-prev');
      const next = slider.querySelector('.rs-next');
      const dots = Array.from(slider.querySelectorAll('.rs-dot'));
      if (!viewport) return;

      const slides = () => viewport.querySelectorAll('.rs-slide');
      const index = () => {
        const w = viewport.clientWidth || 1;
        return Math.min(slides().length - 1, Math.round(viewport.scrollLeft / w));
      };

      const go = (i) => {
        const w = viewport.clientWidth || 1;
        const clamped = Math.max(0, Math.min(slides().length - 1, i));
        viewport.scrollTo({ left: clamped * w, behavior: 'smooth' });
      };

      prev && prev.addEventListener('click', () => go(index() - 1));
      next && next.addEventListener('click', () => go(index() + 1));
      dots.forEach(d => d.addEventListener('click', () => go(parseInt(d.dataset.i, 10))));

      let raf = null;
      viewport.addEventListener('scroll', () => {
        if (raf) return;
        raf = requestAnimationFrame(() => {
          raf = null;
          const i = index();
          dots.forEach((d, di) => d.classList.toggle('active', di === i));
          if (prev) prev.disabled = i === 0;
          if (next) next.disabled = i === slides().length - 1;
        });
      }, { passive: true });

      // keyboard support
      viewport.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') { e.preventDefault(); go(index() + 1); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); go(index() - 1); }
      });

      // init state
      if (prev) prev.disabled = true;
      if (next) next.disabled = slides().length <= 1;
    });
  });
})();
