/**
 * Nokto Studio - forms.js
 * 1) Contact form delivery to hello@noktostudio.com via FormSubmit
 * 2) Auto-reply (_autoresponse) to the submitter in their language
 * 3) Alert copy to simsitermi@gmail.com (explicit notification)
 * NOTE: first submission after changing the mailbox triggers a FormSubmit
 * activation email to hello@noktostudio.com; click it once to start delivery.
 */
(function () {
  var ENDPOINT = 'https://formsubmit.co/ajax/hello@noktostudio.com';
  var ALERT_ENDPOINT = 'https://formsubmit.co/ajax/simsitermi@gmail.com';
  var SITE_NAME = 'noktostudio.com';

  var AUTOREPLY = {
    sk: 'Dakujeme za vas dotaz!\n\n' +
        'Prijali sme spravu z noktostudio.com. Ozvem sa osobne do 24 hodin z e-mailu hello@noktostudio.com.\n\n' +
        'Ak to mate hlad, zavolajte rovno +421 917 316 105.\n\n' +
        'Simon Stermensky\nNokto Studio\nhello@noktostudio.com',
    cs: 'Dekujeme za vas dotaz!\n\n' +
        'Prijali jsme zpravu z noktostudio.com. Ozvu se osobne do 24 hodin z e-mailu hello@noktostudio.com.\n\n' +
        'Kdyz mate hvez, zavolejte +421 917 316 105.\n\n' +
        'Simon Stermensky\nNokto Studio\nhello@noktostudio.com',
    en: 'Thank you for your message!\n\n' +
        'We received your request from noktostudio.com. I will personally reply within 24 hours from hello@noktostudio.com.\n\n' +
        'Simon Stermensky\nNokto Studio\nhello@noktostudio.com'
  };

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
        btn.textContent = 'Posielam...';
        btn.disabled = true;

        const wrap    = form.closest('.contact-form-wrap');
        const success = wrap && wrap.querySelector('.form-success');
        const data = new FormData(form);

        const lang = document.documentElement.lang || 'sk';
        data.append('_autoresponse', AUTOREPLY[lang] || AUTOREPLY['sk']);
        data.append('_template', 'table');

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
              btn.textContent = 'Odoslane ✓';
            }
            const obj = {};
            new FormData(form).forEach((v, k) => { if (!k.startsWith('_')) obj[k] = v; });
            return fetch(ALERT_ENDPOINT, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
              body: JSON.stringify({
                _subject: 'NOVY DOTAZ: noktostudio.com | ' + (obj.email || ''),
                zdroj: 'kontaktny formular noktostudio.com',
                ...obj
              })
            }).catch(() => {});
          })
          .catch(() => {
            btn.textContent = orig;
            btn.disabled = false;
            const note = document.createElement('p');
            note.className = 'form-note';
            note.style.color = '#C5221F';
            note.textContent = 'Odoslanie sa nepodarilo. Zavolajte +421 917 316 105 alebo napiste na hello@noktostudio.com.';
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
