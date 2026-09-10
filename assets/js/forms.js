/**
 * Nokto Studio - forms.js
 * Contact form validation and delivery to the hello inbox via FormSubmit.
 * Endpoint target mailbox: hello@noktostudio.com
 * NOTE: first submission after changing the mailbox triggers a FormSubmit
 * activation email to hello@noktostudio.com; click it once to start delivery.
 */
(function () {
  const ENDPOINT = 'https://formsubmit.co/ajax/hello@noktostudio.com';

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
        btn.textContent = 'Posielam…';
        btn.disabled = true;

        const wrap    = form.closest('.contact-form-wrap');
        const success = wrap && wrap.querySelector('.form-success');
        const data = new FormData(form);

        fetch(ENDPOINT, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: data,
        })
          .then(res => {
            if (!res.ok) throw new Error('HTTP ' + res.status);
            if (success) {
              form.style.display = 'none';
              success.classList.add('visible');
            } else {
              btn.textContent = 'Odoslané ✓';
            }
          })
          .catch(() => {
            btn.textContent = orig;
            btn.disabled = false;
            const note = document.createElement('p');
            note.className = 'form-note';
            note.style.color = '#C5221F';
            note.textContent = 'Odoslanie sa nepodarilo. Zavolajte +421 917 316 105 alebo napíšte na hello@noktostudio.com.';
            const old = form.querySelector('.form-error-note');
            if (old) old.remove();
            note.classList.add('form-error-note');
            form.appendChild(note);
          });
      });

      form.querySelectorAll('.form-input, .form-select, .form-textarea').forEach(f => {
        f.addEventListener('input', () => f.classList.remove('error'));
      });
    });
  });
})();
