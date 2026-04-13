/**
 * Nokto Studio — cookie-banner.js
 * GDPR / UK GDPR compliant cookie consent banner.
 * Language auto-detected from URL path (/sk/ = Slovak, default = English).
 *
 * Usage — fire code only after consent:
 *   window.cookieConsent.onAccept(function() {
 *     // load Google Analytics, Meta Pixel, etc. here
 *   });
 *
 * Check consent state anywhere:
 *   window.cookieConsent.hasConsented()  // true | false | null (not yet decided)
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'nokto_cookie_consent';
  var BANNER_VERSION = '1';

  /* ── Language detection ── */
  var isSk = window.location.pathname.indexOf('/sk') === 0 ||
             window.location.pathname.indexOf('/sk/') !== -1;

  var copy = {
    en: {
      text:    'We use cookies to analyse traffic and improve your experience. Essential cookies are always active.',
      accept:  'Accept all',
      decline: 'Essential only',
      policy:  'Privacy policy',
    },
    sk: {
      text:    'Používame cookies na analýzu návštevnosti a zlepšenie vášho zážitku. Nevyhnutné cookies sú vždy aktívne.',
      accept:  'Prijať všetko',
      decline: 'Len nevyhnutné',
      policy:  'Zásady ochrany súkromia',
    },
  };

  var t = isSk ? copy.sk : copy.en;

  /* ── Consent callbacks ── */
  var acceptCallbacks = [];

  function fireAccept() {
    acceptCallbacks.forEach(function (fn) { try { fn(); } catch (e) {} });
  }

  /* ── Public API ── */
  window.cookieConsent = {
    /**
     * Register a callback to run when/if the user accepts analytics cookies.
     * If they already accepted in a previous session, the callback fires immediately.
     */
    onAccept: function (fn) {
      var stored = readStored();
      if (stored && stored.accepted) {
        try { fn(); } catch (e) {}
      } else {
        acceptCallbacks.push(fn);
      }
    },
    /** Returns true (accepted), false (declined), or null (not yet decided). */
    hasConsented: function () {
      var stored = readStored();
      if (!stored) return null;
      return stored.accepted;
    },
  };

  /* ── Persistence ── */
  function readStored() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var data = JSON.parse(raw);
      return data.version === BANNER_VERSION ? data : null;
    } catch (e) { return null; }
  }

  function writeStored(accepted) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        version:  BANNER_VERSION,
        accepted: accepted,
        date:     new Date().toISOString(),
      }));
    } catch (e) {}
  }

  /* ── Already decided in a previous session ── */
  var stored = readStored();
  if (stored) {
    if (stored.accepted) fireAccept();
    return; // Don't show banner
  }

  /* ── Inject CSS ── */
  var style = document.createElement('style');
  style.textContent = [
    '#nk-cookie{',
      'position:fixed;bottom:0;left:0;right:0;z-index:10000;',
      'background:rgba(20,29,56,0.97);',
      'backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);',
      'border-top:1px solid rgba(108,99,255,0.25);',
      'padding:16px 28px;',
      'display:flex;align-items:center;gap:20px;flex-wrap:wrap;',
      'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif;',
      'transform:translateY(100%);transition:transform 0.35s ease;',
    '}',
    '#nk-cookie.nk-visible{transform:translateY(0);}',
    '#nk-cookie p{',
      'font-size:0.82rem;color:rgba(196,192,240,0.85);line-height:1.6;',
      'flex:1;min-width:220px;margin:0;',
    '}',
    '#nk-cookie a{color:#9490FF;text-decoration:underline;white-space:nowrap;}',
    '#nk-cookie a:hover{color:#C4C0F0;}',
    '#nk-cookie-btns{display:flex;gap:10px;flex-shrink:0;flex-wrap:wrap;}',
    '#nk-cookie-accept,#nk-cookie-decline{',
      'font-size:0.8rem;font-weight:600;padding:9px 18px;border-radius:8px;',
      'cursor:pointer;border:none;font-family:inherit;white-space:nowrap;',
      'transition:opacity 0.2s ease;',
    '}',
    '#nk-cookie-accept{background:#6C63FF;color:#fff;}',
    '#nk-cookie-accept:hover{opacity:0.88;}',
    '#nk-cookie-decline{background:rgba(255,255,255,0.07);color:rgba(196,192,240,0.9);border:1px solid rgba(255,255,255,0.12);}',
    '#nk-cookie-decline:hover{background:rgba(255,255,255,0.12);}',
    '@media(max-width:600px){',
      '#nk-cookie{padding:14px 16px;gap:14px;}',
      '#nk-cookie-btns{width:100%;}',
      '#nk-cookie-accept,#nk-cookie-decline{flex:1;text-align:center;justify-content:center;}',
    '}',
  ].join('');
  document.head.appendChild(style);

  /* ── Inject HTML ── */
  var banner = document.createElement('div');
  banner.id = 'nk-cookie';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', isSk ? 'Súhlas s cookies' : 'Cookie consent');

  var policyHref = isSk ? '/sk/privacy/' : '/en/privacy/';

  banner.innerHTML =
    '<p>' + t.text + ' <a href="' + policyHref + '">' + t.policy + '</a></p>' +
    '<div id="nk-cookie-btns">' +
      '<button id="nk-cookie-decline">' + t.decline + '</button>' +
      '<button id="nk-cookie-accept">' + t.accept + '</button>' +
    '</div>';

  /* ── Mount and animate in ── */
  function mount() {
    document.body.appendChild(banner);
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        banner.classList.add('nk-visible');
      });
    });
  }

  function dismiss() {
    banner.classList.remove('nk-visible');
    setTimeout(function () {
      if (banner.parentNode) banner.parentNode.removeChild(banner);
    }, 400);
  }

  /* ── Button handlers ── */
  banner.querySelector('#nk-cookie-accept').addEventListener('click', function () {
    writeStored(true);
    fireAccept();
    dismiss();
  });

  banner.querySelector('#nk-cookie-decline').addEventListener('click', function () {
    writeStored(false);
    dismiss();
  });

  /* ── Show banner after a short delay (less jarring than instant) ── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(mount, 600);
    });
  } else {
    setTimeout(mount, 600);
  }

})();
