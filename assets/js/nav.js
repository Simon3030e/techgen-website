/**
 * Nokto Studio — nav.js
 * Sticky header · Mobile menu · Scroll-to-top · FAQ accordion · AOS
 */
(function () {
  const header    = document.getElementById('site-header');
  const hamburger = document.getElementById('hamburger');
  const navMobile = document.getElementById('nav-mobile');
  const scrollBtn = document.getElementById('scroll-top');

  /* ── Sticky header + scroll-to-top visibility ── */
  window.addEventListener('scroll', () => {
    if (header)    header.classList.toggle('scrolled', window.scrollY > 20);
    if (scrollBtn) scrollBtn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  /* ── iOS-compatible scroll lock ── */
  let savedScrollY = 0;

  function lockScroll() {
    savedScrollY = window.scrollY;
    document.body.style.position = 'fixed';
    document.body.style.top      = '-' + savedScrollY + 'px';
    document.body.style.width    = '100%';
  }

  function unlockScroll() {
    document.body.style.position = '';
    document.body.style.top      = '';
    document.body.style.width    = '';
    window.scrollTo(0, savedScrollY);
  }

  function closeMenu() {
    if (!navMobile.classList.contains('open')) return;
    navMobile.classList.remove('open');
    hamburger.classList.remove('active');
    if (header) header.classList.remove('menu-open');
    unlockScroll();
  }

  /* ── Mobile menu toggle ── */
  if (hamburger && navMobile) {
    hamburger.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = navMobile.classList.toggle('open');
      hamburger.classList.toggle('active', open);
      if (header) header.classList.toggle('menu-open', open);
      if (open) {
        lockScroll();
      } else {
        unlockScroll();
      }
    });

    /* Close on nav link tap */
    navMobile.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeMenu);
    });

    /* Close on outside tap */
    document.addEventListener('click', (e) => {
      if (navMobile.classList.contains('open') &&
          !navMobile.contains(e.target) &&
          !hamburger.contains(e.target)) {
        closeMenu();
      }
    });

    /* Close on Escape key */
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* ── Scroll to top ── */
  if (scrollBtn) {
    scrollBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  /* ── FAQ accordion ── */
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item   = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
      if (!isOpen) item.classList.add('open');
    });
  });

  /* ── AOS init ── */
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof AOS !== 'undefined') {
      AOS.init({ duration: 700, easing: 'ease-out-cubic', once: true, offset: 60 });
    }
  });
})();
