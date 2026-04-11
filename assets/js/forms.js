/**
 * Nokto Studio — forms.js
 * Contact form validation and submission handling
 */
(function () {
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.contact-form-el').forEach(form => {
      form.addEventListener('submit', e => {
        e.preventDefault();

        let valid = true;
        form.querySelectorAll('[required]').forEach(field => {
          const empty = !field.value.trim();
          field.classList.toggle('error', empty);
          if (empty) valid = false;
        });
        if (!valid) return;

        const btn  = form.querySelector('[type="submit"]');
        const orig = btn.textContent;
        btn.textContent = 'Sending…';
        btn.disabled = true;

        /* ── Replace with Formspree / EmailJS / backend endpoint ── */
        setTimeout(() => {
          const wrap    = form.closest('.contact-form-wrap');
          const success = wrap && wrap.querySelector('.form-success');
          if (success) {
            form.style.display = 'none';
            success.classList.add('visible');
          } else {
            btn.textContent = 'Sent ✓';
          }
        }, 1500);
      });

      form.querySelectorAll('.form-input, .form-select, .form-textarea').forEach(f => {
        f.addEventListener('input', () => f.classList.remove('error'));
      });
    });
  });
})();
