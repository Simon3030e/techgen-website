/**
 * Nokto Studio — clarity.js
 * Microsoft Clarity integration with regional compliance.
 *
 * SK pages (/sk/...): Loads ONLY after explicit cookie consent — GDPR opt-in.
 * EN pages + root:    Loads immediately — US / CCPA opt-out model (analytics
 *                     do not constitute "sale" of personal data under CCPA).
 *
 * Depends on cookie-banner.js being loaded first (sets window.cookieConsent).
 */
(function () {
  'use strict';

  var PROJECT_ID = 'wc42xmhume';

  function loadClarity() {
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', PROJECT_ID);
  }

  var isSk = /^\/(sk)(\/|$)/.test(window.location.pathname);

  if (isSk) {
    /* ── GDPR (SK) — consent required before loading ── */
    function hookConsent() {
      if (window.cookieConsent) {
        window.cookieConsent.onAccept(loadClarity);
      }
    }
    /* cookie-banner.js runs synchronously, so cookieConsent is already set
       by the time this script executes — but guard with DOMContentLoaded
       just in case script order ever changes. */
    if (window.cookieConsent) {
      hookConsent();
    } else {
      document.addEventListener('DOMContentLoaded', hookConsent);
    }
  } else {
    /* ── US / CCPA (EN + root) — load immediately ── */
    loadClarity();
  }

})();
