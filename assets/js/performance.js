// Performance Optimization Scripts
// Lazy Loading Images
(function() {
  'use strict';
  
  // Lazy load images with Intersection Observer
  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          
          // Load image
          if (img.dataset.src) {
            img.src = img.dataset.src;
          }
          if (img.dataset.srcset) {
            img.srcset = img.dataset.srcset;
          }
          
          img.classList.add('loaded');
          img.removeAttribute('data-src');
          img.removeAttribute('data-srcset');
          
          observer.unobserve(img);
        }
      });
    }, {
      rootMargin: '50px 0px',
      threshold: 0.01
    });
    
    // Observe all images with loading="lazy"
    document.addEventListener('DOMContentLoaded', () => {
      const lazyImages = document.querySelectorAll('img[loading="lazy"]');
      lazyImages.forEach(img => imageObserver.observe(img));
    });
  }
  
  // Defer non-critical resources
  function loadDeferredStyles() {
    const addStylesNode = document.getElementById("deferred-styles");
    if (addStylesNode) {
      const replacement = document.createElement("div");
      replacement.innerHTML = addStylesNode.textContent;
      document.body.appendChild(replacement);
      addStylesNode.parentElement.removeChild(addStylesNode);
    }
  }
  
  // Load deferred styles after page load
  if (window.addEventListener) {
    window.addEventListener('load', loadDeferredStyles);
  } else if (window.attachEvent) {
    window.attachEvent('onload', loadDeferredStyles);
  }
  
  // Prefetch links on hover
  let prefetched = new Set();
  
  function prefetchLink(url) {
    if (prefetched.has(url)) return;
    
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = url;
    document.head.appendChild(link);
    
    prefetched.add(url);
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a[href^="/"]');
    
    links.forEach(link => {
      link.addEventListener('mouseenter', () => {
        const href = link.getAttribute('href');
        if (href && !href.includes('#')) {
          prefetchLink(href);
        }
      }, { once: true });
    });
  });
  
  // Service Worker Registration (optional - for PWA features)
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      // Uncomment to enable service worker
      // navigator.serviceWorker.register('/sw.js')
      //   .then(registration => console.log('SW registered'))
      //   .catch(err => console.log('SW registration failed'));
    });
  }
  
  // Performance monitoring
  if ('PerformanceObserver' in window) {
    // Monitor Largest Contentful Paint
    const lcpObserver = new PerformanceObserver((entryList) => {
      const entries = entryList.getEntries();
      const lastEntry = entries[entries.length - 1];
      
      // Log LCP for debugging (remove in production)
      if (window.location.search.includes('debug=perf')) {
        console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
      }
    });
    
    try {
      lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
    } catch (e) {
      // LCP not supported
    }
    
    // Monitor First Input Delay
    const fidObserver = new PerformanceObserver((entryList) => {
      const entries = entryList.getEntries();
      
      entries.forEach(entry => {
        if (window.location.search.includes('debug=perf')) {
          console.log('FID:', entry.processingStart - entry.startTime);
        }
      });
    });
    
    try {
      fidObserver.observe({ entryTypes: ['first-input'] });
    } catch (e) {
      // FID not supported
    }
  }
  
  // Reduce layout thrashing
  const debounce = (func, wait) => {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  };
  
  // Optimize scroll events
  let ticking = false;
  
  function optimizedScroll(callback) {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        callback();
        ticking = false;
      });
      ticking = true;
    }
  }
  
  // Export for use in other scripts
  window.performanceUtils = {
    debounce,
    optimizedScroll,
    prefetchLink
  };
  
})();
