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

  /* ── Mobile menu toggle ── */
  if (hamburger && navMobile) {
    hamburger.addEventListener('click', () => {
      const open = navMobile.classList.toggle('open');
      hamburger.classList.toggle('active', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    navMobile.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMobile.classList.remove('open');
        hamburger.classList.remove('active');
        document.body.style.overflow = '';
      });
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
