/**
 * Mobile Navigation Enhancements
 * 
 * Features:
 * - Animated hamburger menu (transforms to X)
 * - Smooth dropdown animations
 * - Touch gesture support
 * - Swipe to close
 * - Focus trap for accessibility
 * - Body scroll lock when menu open
 * - Backdrop overlay
 * - Keyboard shortcuts (Escape to close)
 */

(function() {
  'use strict';

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }

  function initMobileNav() {
    const toggle = document.querySelector('.greedy-nav__toggle');
    const hiddenLinks = document.querySelector('.hidden-links');
    const body = document.body;
    let backdrop = null;
    let isOpen = false;
    let startY = 0;

    if (!toggle || !hiddenLinks) return;

    // Create backdrop element
    createBackdrop();

    // Toggle menu
    toggle.addEventListener('click', toggleMenu);

    // Close on backdrop click
    backdrop.addEventListener('click', closeMenu);

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && isOpen) {
        closeMenu();
      }
    });

    // Touch gesture support (swipe up to close)
    if ('ontouchstart' in window) {
      hiddenLinks.addEventListener('touchstart', handleTouchStart, { passive: true });
      hiddenLinks.addEventListener('touchmove', handleTouchMove, { passive: false });
      hiddenLinks.addEventListener('touchend', handleTouchEnd, { passive: true });
    }

    // Close menu when clicking a link
    const menuLinks = hiddenLinks.querySelectorAll('a');
    menuLinks.forEach(link => {
      link.addEventListener('click', function() {
        // Small delay to allow navigation
        setTimeout(closeMenu, 100);
      });
    });

    // Close menu on window resize (if transitioning to desktop)
    let resizeTimer;
    window.addEventListener('resize', function() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function() {
        if (window.innerWidth > 768 && isOpen) {
          closeMenu();
        }
      }, 250);
    });

    // Focus trap
    setupFocusTrap();

    /**
     * Create backdrop element
     */
    function createBackdrop() {
      backdrop = document.createElement('div');
      backdrop.className = 'nav-backdrop';
      document.body.appendChild(backdrop);
    }

    /**
     * Toggle menu open/close
     */
    function toggleMenu(e) {
      e.preventDefault();
      e.stopPropagation();

      if (isOpen) {
        closeMenu();
      } else {
        openMenu();
      }
    }

    /**
     * Open menu
     */
    function openMenu() {
      isOpen = true;
      toggle.classList.add('close');
      hiddenLinks.classList.add('show');
      backdrop.classList.add('show');
      body.classList.add('nav-open');

      // Set ARIA attributes
      toggle.setAttribute('aria-expanded', 'true');
      hiddenLinks.setAttribute('aria-hidden', 'false');

      // Focus first link
      const firstLink = hiddenLinks.querySelector('a');
      if (firstLink) {
        setTimeout(() => firstLink.focus(), 300);
      }

      // Announce to screen readers
      announceToScreenReader('Menu opened');
    }

    /**
     * Close menu
     */
    function closeMenu() {
      if (!isOpen) return;

      isOpen = false;
      toggle.classList.remove('close');
      hiddenLinks.classList.remove('show');
      backdrop.classList.remove('show');
      body.classList.remove('nav-open');

      // Set ARIA attributes
      toggle.setAttribute('aria-expanded', 'false');
      hiddenLinks.setAttribute('aria-hidden', 'true');

      // Return focus to toggle button
      toggle.focus();

      // Announce to screen readers
      announceToScreenReader('Menu closed');
    }

    /**
     * Touch gesture handlers
     */
    function handleTouchStart(e) {
      startY = e.touches[0].clientY;
    }

    function handleTouchMove(e) {
      if (!isOpen) return;

      const currentY = e.touches[0].clientY;
      const diff = startY - currentY;

      // If swiping up more than 50px, close menu
      if (diff > 50) {
        e.preventDefault();
        closeMenu();
      }
    }

    function handleTouchEnd() {
      startY = 0;
    }

    /**
     * Setup focus trap for accessibility
     */
    function setupFocusTrap() {
      const focusableElements = hiddenLinks.querySelectorAll(
        'a[href], button, [tabindex]:not([tabindex="-1"])'
      );

      if (focusableElements.length === 0) return;

      const firstFocusable = focusableElements[0];
      const lastFocusable = focusableElements[focusableElements.length - 1];

      hiddenLinks.addEventListener('keydown', function(e) {
        if (!isOpen || e.key !== 'Tab') return;

        // Shift + Tab
        if (e.shiftKey) {
          if (document.activeElement === firstFocusable) {
            e.preventDefault();
            lastFocusable.focus();
          }
        }
        // Tab
        else {
          if (document.activeElement === lastFocusable) {
            e.preventDefault();
            firstFocusable.focus();
          }
        }
      });
    }

    /**
     * Announce to screen readers
     */
    function announceToScreenReader(message) {
      const announcement = document.createElement('div');
      announcement.setAttribute('role', 'status');
      announcement.setAttribute('aria-live', 'polite');
      announcement.className = 'visually-hidden';
      announcement.textContent = message;
      document.body.appendChild(announcement);

      // Remove after announcement
      setTimeout(() => {
        document.body.removeChild(announcement);
      }, 1000);
    }

    /**
     * Initialize ARIA attributes
     */
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', 'hidden-links');
    toggle.setAttribute('aria-label', 'Toggle navigation menu');
    hiddenLinks.setAttribute('id', 'hidden-links');
    hiddenLinks.setAttribute('aria-hidden', 'true');

    // Add keyboard shortcut hint
    const shortcutHint = document.createElement('span');
    shortcutHint.className = 'visually-hidden';
    shortcutHint.textContent = 'Press Escape to close menu';
    hiddenLinks.appendChild(shortcutHint);
  }

  /**
   * Enhance existing greedy-nav behavior
   * (The theme already has greedy-nav.js, this extends it)
   */
  function enhanceGreedyNav() {
    // Wait for greedy-nav to initialize
    setTimeout(function() {
      const visibleLinks = document.querySelector('.visible-links');
      const hiddenLinks = document.querySelector('.hidden-links');

      if (!visibleLinks || !hiddenLinks) return;

      // Observe changes to hidden-links (when items move)
      const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
          if (mutation.addedNodes.length > 0 || mutation.removedNodes.length > 0) {
            // Re-apply animations when items change
            const items = hiddenLinks.querySelectorAll('li');
            items.forEach((item, index) => {
              item.style.animationDelay = (index * 0.05) + 's';
            });
          }
        });
      });

      observer.observe(hiddenLinks, {
        childList: true,
        subtree: false
      });
    }, 500);
  }

  // Enhance after page load
  if (document.readyState === 'complete') {
    enhanceGreedyNav();
  } else {
    window.addEventListener('load', enhanceGreedyNav);
  }

  /**
   * Add swipe gesture indicator hint
   */
  function addSwipeHint() {
    if (window.innerWidth <= 768 && 'ontouchstart' in window) {
      const hiddenLinks = document.querySelector('.hidden-links');
      if (!hiddenLinks || hiddenLinks.querySelector('.swipe-hint')) return;

      const hint = document.createElement('div');
      hint.className = 'swipe-hint visually-hidden';
      hint.setAttribute('aria-live', 'polite');
      hint.textContent = 'Swipe up to close menu';
      hiddenLinks.insertBefore(hint, hiddenLinks.firstChild);

      // Remove hint after first interaction
      let hintRemoved = false;
      hiddenLinks.addEventListener('touchstart', function() {
        if (!hintRemoved) {
          hint.style.display = 'none';
          hintRemoved = true;
        }
      }, { once: true });
    }
  }

  // Add swipe hint after DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addSwipeHint);
  } else {
    addSwipeHint();
  }

})();
