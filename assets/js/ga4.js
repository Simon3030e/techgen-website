/**
 * Nokto Studio  - ga4.js
 * Google Analytics 4 (gtag.js) integration with regional compliance.
 *
 * SK root, /sk/ and /cz/ pages: loads only after explicit consent (GDPR opt-in).
 * EN pages: loads immediately under the US / CCPA opt-out model.
 *
 * Depends on cookie-banner.js being loaded first (sets window.cookieConsent).
 */
(function () {
  'use strict';

  var MEASUREMENT_ID = 'G-KJXENRWBRW';
  var loaded = false;

  function loadGa4() {
    if (loaded) return;
    loaded = true;

    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MEASUREMENT_ID;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', MEASUREMENT_ID, { anonymize_ip: true });
  }

  var needsConsent = window.location.pathname === '/' ||
                     /^\/(sk|cz)(\/|$)/.test(window.location.pathname);

  if (needsConsent) {
    function hookConsent() {
      if (window.cookieConsent) {
        window.cookieConsent.onAccept(loadGa4);
      }
    }
    if (window.cookieConsent) {
      hookConsent();
    } else {
      document.addEventListener('DOMContentLoaded', hookConsent);
    }
  } else {
    loadGa4();
  }

})();
