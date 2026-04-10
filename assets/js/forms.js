/**
 * noktostudio — forms.js
 * Client-side form validation with smooth feedback
 */

(function () {
  const forms = document.querySelectorAll('.noktostudio-form');

  forms.forEach(form => {
    const inputs   = form.querySelectorAll('[data-required]');
    const submitBtn = form.querySelector('[type="submit"]');

    function validateField(field) {
      const value = field.value.trim();
      let valid = true;

      if (field.dataset.required !== undefined && value === '') {
        valid = false;
      }
      if (field.type === 'email' && value !== '') {
        valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
      }

      field.classList.toggle('error',   !valid);
      field.classList.toggle('success',  valid && value !== '');
      return valid;
    }

    inputs.forEach(field => {
      field.addEventListener('blur',  () => validateField(field));
      field.addEventListener('input', () => {
        if (field.classList.contains('error')) validateField(field);
      });
    });

    form.addEventListener('submit', e => {
      e.preventDefault();

      let allValid = true;
      inputs.forEach(field => {
        if (!validateField(field)) allValid = false;
      });

      if (!allValid) {
        const first = form.querySelector('.error');
        if (first) first.focus();
        return;
      }

      // Success state
      submitBtn.disabled = true;
      submitBtn.textContent = '✓ Sent! We\'ll be in touch soon.';
      submitBtn.style.background = '#4caf82';

      // Reset after 4s (demo)
      setTimeout(() => {
        form.reset();
        inputs.forEach(f => f.classList.remove('success', 'error'));
        submitBtn.disabled = false;
        submitBtn.textContent = submitBtn.dataset.label || 'Book My Free Consultation';
        submitBtn.style.background = '';
      }, 4000);
    });
  });

  // Smooth scroll for anchor CTAs
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Word reveal animation for hero headline
  const headline = document.querySelector('.hero-headline');
  if (headline) {
    const text  = headline.textContent;
    const words = text.trim().split(/\s+/);
    headline.innerHTML = words
      .map((w, i) => `<span class="word" style="animation-delay:${0.08 * i}s">${w}</span>`)
      .join(' ');
  }
})();
