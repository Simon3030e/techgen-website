/**
 * Nokto Studio - forms.js
 * 1) Contact form delivery to hello@noktostudio.com via FormSubmit
 * 2) Auto-reply (_autoresponse) to the submitter in their language
 * 3) Alert copy to simsitermi@gmail.com (explicit notification)
 * 4) Free-audit popup (web + email), once per session, language-aware
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

    initAuditPopup();
  });

  /* ---------------- audit popup (merged, no rebuild needed) ---------------- */

  var POPUP_SHOWN = 'auditPopupShown';
  var DELAY_MS = 8000;
  var SCROLL_PCT = 45;

  var POPUP_COPY = {
    sk: { h: 'Bezplatný audit vášho webu',
          sub: 'Napíšte adresu webu a e-mail. Do 3 dní vám pošlem vstupný audit: čo brzdí váš web v Google a čo by SEO mohlo u vás znamenať. Zadarmo, bez záväzku.',
          webph: 'Adresa vášho webu (https://...)', emailph: 'Váš e-mail',
          btn: 'Chcem bezplatný audit', btn2: 'Odosielam...',
          note: 'Odoslaním súhlasíte so spracovaním e-mailu na účel zaslania auditu. Žiadny spam, žiadny predaj dát.',
          ok: '✓ Ďakujeme! Audit vám pošleme do 3 dní na e-mail.',
          subj: 'Žiadosť o bezplatný audit',
          reply: 'Dakujeme za ziadost o bezplatny audit!\n\nVstupny audit vasho webu vam posleme do 3 pracovnych dni na tento e-mail.\n\nKontaktujem vas osobne cez hello@noktostudio.com. Ak mate otazku hned, zavolajte +421 917 316 105.\n\nSimon Stermensky\nNokto Studio\nhello@noktostudio.com' },
    cs: { h: 'Bezplatný audit vašeho webu',
          sub: 'Napište adresu webu a e-mail. Do 3 dní vám pošleme vstupní audit: co brzdí váš web v Google a co by SEO mohlo u vás znamenat. Zdarma, bez závazku.',
          webph: 'Adresa vašeho webu (https://...)', emailph: 'Váš e-mail',
          btn: 'Chci bezplatný audit', btn2: 'Odesílám...',
          note: 'Odesláním souhlasíte se zpracováním e-mailu za účelem zaslání auditu. Žádný spam, žádný prodej dat.',
          ok: '✓ Děkujeme! Audit vám pošleme do 3 dní na e-mail.',
          subj: 'Žádost o bezplatný audit',
          reply: 'Dekujeme za zadost o bezplatny audit!\n\nVstupni audit vasho webu vam posleme do 3 pracovnich dni na tento e-mail.\n\nKontaktuji vas osobne cez hello@noktostudio.com. Kdyz mate otazku hned, zavolejte +421 917 316 105.\n\nSimon Stermensky\nNokto Studio\nhello@noktostudio.com' },
    en: { h: 'Free website audit',
          sub: 'Enter your website address and e-mail. Within 3 days I will send you a free mini audit: what is holding your site back in Google and what SEO could mean for you.',
          webph: 'Your website address (https://...)', emailph: 'Your e-mail',
          btn: 'Get my free audit', btn2: 'Sending...',
          note: 'By submitting you agree to receive the audit by e-mail. No spam, no data selling.',
          ok: '✓ Thank you! Your audit will arrive within 3 days.',
          subj: 'Free audit request',
          reply: 'Thank you for your free audit request!\n\nYou will receive the mini audit within 3 business days at this e-mail.\n\nI will contact you personally via hello@noktostudio.com.\n\nSimon Stermensky\nNokto Studio\nhello@noktostudio.com' }
  };

  function popupBuild(copy, reply) {
    var overlay = document.createElement('div');
    overlay.className = 'audit-popup-overlay';
    overlay.id = 'auditPopup';
    overlay.innerHTML =
      '<div class="audit-popup" role="dialog" aria-modal="true">' +
      '  <button class="audit-popup-close" type="button" aria-label="Zavriet">&times;</button>' +
      '  <div class="ap-form-wrap">' +
      '    <h3>' + copy.h + '</h3>' +
      '    <p class="ap-sub">' + copy.sub + '</p>' +
      '    <form class="ap-form">' +
      '      <div class="ap-field"><input type="url" name="web" placeholder="' + copy.webph + '" required></div>' +
      '      <div class="ap-field"><input type="email" name="email" placeholder="' + copy.emailph + '" required></div>' +
      '      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      '      <input type="hidden" name="_subject" value="' + copy.subj + '">' +
      '      <button type="submit" class="btn btn-primary">' + copy.btn + '</button>' +
      '      <p class="ap-note">' + copy.note + '</p>' +
      '    </form>' +
      '  </div>' +
      '  <div class="ap-success"><p>' + copy.ok + '</p></div>' +
      '</div>';
    document.body.appendChild(overlay);
    return overlay;
  }

  function initAuditPopup() {
    try { if (sessionStorage.getItem(POPUP_SHOWN)) return; } catch (e) {}
    var lang = document.documentElement.lang || 'sk';
    var copy = POPUP_COPY[lang] || POPUP_COPY['sk'];
    var overlay = popupBuild(copy);
    overlay.querySelector('.audit-popup-close').addEventListener('click', function () { overlay.classList.remove('open'); });
    overlay.addEventListener('click', function (e) { if (e.target === overlay) overlay.classList.remove('open'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') overlay.classList.remove('open'); });

    var form = overlay.querySelector('.ap-form');
    var wrap = overlay.querySelector('.ap-form-wrap');
    var success = overlay.querySelector('.ap-success');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button');
      btn.disabled = true;
      btn.textContent = copy.btn2;
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data['_autoresponse'] = copy.reply;
      data['_template'] = 'table';
      data['_subject'] = '[AUDIT noktostudio.com] ' + (data.web || 'web') + ' - ' + (data.email || '');

      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function () {
        wrap.style.display = 'none';
        success.style.display = 'block';
        setTimeout(function () { overlay.classList.remove('open'); }, 6000);
      }).catch(function () {
        btn.disabled = false;
        btn.textContent = copy.btn;
      });

      fetch(ALERT_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          _subject: 'NOVA ZIADOST O AUDIT: noktostudio.com | ' + (data.web || '') + ' | ' + (data.email || ''),
          web: data.web || '', email: data.email || '', zdroj: 'popup na noktostudio.com'
        })
      }).catch(function () {});
    });

    setTimeout(function () { showPopup(overlay); }, DELAY_MS);
    var scrolled = false;
    window.addEventListener('scroll', function () {
      if (scrolled) return;
      var pct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
      if (pct >= SCROLL_PCT) { scrolled = true; showPopup(overlay); }
    }, { passive: true });
  }

  function showPopup(overlay) {
    overlay.classList.add('open');
    try { sessionStorage.setItem(POPUP_SHOWN, '1'); } catch (e) {}
  }
})();
