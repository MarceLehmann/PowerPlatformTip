/**
 * Newsletter Prompt mit Cookie-Steuerung
 * Zeigt alle 14 Tage (oder konfigurierbar) einen Newsletter-Hinweis an
 * Wird nicht bei Suchseiten angezeigt
 */

(function() {
  'use strict';

  const CONFIG = {
    cookieName: 'newsletter_prompt_dismissed',
    daysUntilNextPrompt: 14, // Kann auf 30 für monatlich geändert werden
    excludePages: ['/search/', '/search.html'], // Seiten wo der Prompt nicht erscheint
    modalId: 'newsletter-modal',
    delay: 3000 // Verzögerung in ms vor dem Anzeigen (3 Sekunden)
  };

  // Cookie-Funktionen
  function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = name + '=' + value + ';expires=' + expires.toUTCString() + ';path=/;SameSite=Lax';
  }

  function getCookie(name) {
    const nameEQ = name + '=';
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  // Prüfen ob wir auf einer ausgeschlossenen Seite sind
  function isExcludedPage() {
    const currentPath = window.location.pathname;
    return CONFIG.excludePages.some(page => currentPath.includes(page));
  }

  // Prüfen ob der Prompt angezeigt werden soll
  function shouldShowPrompt() {
    if (isExcludedPage()) {
      return false;
    }
    
    const cookieValue = getCookie(CONFIG.cookieName);
    return cookieValue === null;
  }

  // Modal erstellen
  function createModal() {
    const modal = document.createElement('div');
    modal.id = CONFIG.modalId;
    modal.className = 'newsletter-modal';
    modal.innerHTML = `
      <div class="newsletter-modal-overlay"></div>
      <div class="newsletter-modal-content">
        <button class="newsletter-modal-close" aria-label="Schließen">&times;</button>
        <div class="newsletter-modal-body">
          <h3>📬 Newsletter abonnieren</h3>
          <p>Bleiben Sie auf dem Laufenden mit den neuesten Power Platform Tipps und Tricks!</p>
          <p>Erhalten Sie regelmäßig:</p>
          <ul>
            <li>Praktische Tutorials</li>
            <li>Best Practices</li>
            <li>Neue Features und Updates</li>
          </ul>
          <div class="newsletter-modal-buttons">
            <a href="/newsletter/" class="newsletter-modal-btn newsletter-modal-btn-primary">
              Jetzt anmelden
            </a>
            <button class="newsletter-modal-btn newsletter-modal-btn-secondary" id="newsletter-dismiss">
              Vielleicht später
            </button>
          </div>
        </div>
      </div>
    `;
    
    document.body.appendChild(modal);
    return modal;
  }

  // Modal anzeigen
  function showModal() {
    const modal = document.getElementById(CONFIG.modalId);
    if (modal) {
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  // Modal schließen
  function closeModal() {
    const modal = document.getElementById(CONFIG.modalId);
    if (modal) {
      modal.classList.remove('active');
      document.body.style.overflow = '';
      setCookie(CONFIG.cookieName, 'true', CONFIG.daysUntilNextPrompt);
    }
  }

  // Event Listeners einrichten
  function setupEventListeners(modal) {
    // Schließen-Button
    const closeBtn = modal.querySelector('.newsletter-modal-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', closeModal);
    }

    // "Vielleicht später" Button
    const dismissBtn = document.getElementById('newsletter-dismiss');
    if (dismissBtn) {
      dismissBtn.addEventListener('click', closeModal);
    }

    // Overlay klick
    const overlay = modal.querySelector('.newsletter-modal-overlay');
    if (overlay) {
      overlay.addEventListener('click', closeModal);
    }

    // "Jetzt anmelden" Button setzt auch den Cookie
    const signupBtn = modal.querySelector('.newsletter-modal-btn-primary');
    if (signupBtn) {
      signupBtn.addEventListener('click', function() {
        setCookie(CONFIG.cookieName, 'true', CONFIG.daysUntilNextPrompt);
      });
    }

    // ESC-Taste zum Schließen
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // Initialisierung
  function init() {
    if (shouldShowPrompt()) {
      setTimeout(function() {
        const modal = createModal();
        setupEventListeners(modal);
        showModal();
      }, CONFIG.delay);
    }
  }

  // Warten bis DOM geladen ist
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
