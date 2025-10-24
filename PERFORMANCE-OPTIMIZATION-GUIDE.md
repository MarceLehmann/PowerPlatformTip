# Performance & PageSpeed Optimierungs-Guide – PowerPlatformTip

**Erstellt:** 24. Oktober 2025  
**Zweck:** Konkrete Massnahmen zur Verbesserung von Core Web Vitals und PageSpeed Score

---

## Übersicht

Performance-Optimierung ist entscheidend für SEO (Google Ranking-Faktor) und Nutzererlebnis. Dieser Guide fokussiert auf:
- **Core Web Vitals** (LCP, CLS, INP/FID)
- **PageSpeed Insights Score**
- **Ladezeit-Optimierung**
- **Mobile Performance**

---

## 1. Core Web Vitals – Zielwerte

### Largest Contentful Paint (LCP)
**Ziel:** < 2.5 Sekunden  
**Was es misst:** Zeit bis grösstes sichtbares Element geladen ist

**Optimierungen:**
- [ ] Bilder komprimieren (WebP, AVIF)
- [ ] Lazy-loading für Below-the-Fold Bilder
- [ ] Kritisches CSS inline
- [ ] Preload wichtiger Ressourcen (Fonts, Hero-Image)
- [ ] Server Response Time optimieren (< 200ms)

### Cumulative Layout Shift (CLS)
**Ziel:** < 0.1  
**Was es misst:** Visuelle Stabilität (unerwartete Layout-Shifts)

**Optimierungen:**
- [ ] Width/Height für alle Bilder definieren
- [ ] Reserviere Platz für Ads/Embeds
- [ ] Fonts mit `font-display: swap` laden
- [ ] Keine dynamischen Inhalts-Injections Above-the-Fold

### Interaction to Next Paint (INP) / First Input Delay (FID)
**Ziel:** INP < 200ms, FID < 100ms  
**Was es misst:** Interaktivität/Reaktionszeit

**Optimierungen:**
- [ ] JavaScript minimieren/deferred laden
- [ ] Long Tasks aufteilen
- [ ] Event Handlers optimieren
- [ ] Web Workers für schwere Tasks

---

## 2. Jekyll-spezifische Optimierungen

### Jekyll Build-Optimierung

#### Minimierung & Compression
```yaml
# _config.yml (bereits vorhanden)
compress_html:
  clippings: all
  ignore:
    envs: development
```

#### Sass Compression
```yaml
# _config.yml (bereits aktiviert)
sass:
  sass_dir: _sass
  style: compressed
```

### Asset-Optimierung

#### CSS
- [ ] **Kritisches CSS inline** (Above-the-Fold)
- [ ] **Non-kritisches CSS** async/defer laden
- [ ] **Unused CSS** entfernen (PurgeCSS)

**Beispiel für async CSS:**
```html
<!-- _includes/head.html -->
<link rel="preload" href="{{ '/assets/css/main.css' | relative_url }}" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}"></noscript>
```

#### JavaScript
- [ ] **Defer JavaScript** (nicht Above-the-Fold nötig)
- [ ] **Async für Analytics** (bereits für FontAwesome)
- [ ] **Code-Splitting** für grosse Scripts

**Beispiel:**
```html
<!-- Defer non-critical JS -->
<script defer src="{{ '/assets/js/main.min.js' | relative_url }}"></script>
```

---

## 3. Bilder-Optimierung

### Kompression & Format

#### WebP/AVIF
**Vorteile:**
- 25-35% kleinere Dateigrösse vs. JPEG/PNG
- Bessere Qualität bei gleicher Grösse

**Implementierung:**
```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description" width="800" height="600">
</picture>
```

#### Lazy-Loading
```html
<img src="image.jpg" alt="Description" loading="lazy" width="800" height="600">
```

**Jekyll Plugin (optional):**
```ruby
# Gemfile
gem 'jekyll-imagemagick'  # Auto-Resize & Convert
```

### Responsive Images (srcset)
```html
<img 
  src="image-800.jpg" 
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="Description"
  width="800"
  height="600"
  loading="lazy">
```

### Tools für Bildoptimierung
- **ImageOptim** (Mac)
- **TinyPNG** / **TinyJPG** (Web)
- **Squoosh** (Web, von Google)
- **imagemagick** (CLI)

**Batch-Kompression:**
```bash
# Alle JPGs im Verzeichnis komprimieren
find assets/images -name "*.jpg" -exec mogrify -quality 85 -strip {} \;

# WebP-Konvertierung
for img in assets/images/*.jpg; do
  cwebp -q 85 "$img" -o "${img%.jpg}.webp"
done
```

---

## 4. Font-Optimierung

### Font-Loading-Strategie

#### Aktuell (FontAwesome via CDN)
```html
<!-- _includes/head.html -->
<link rel="preload" href="https://cdn.jsdelivr.net/.../fontawesome.min.css" as="style" onload="...">
```

#### Optimierungen
- [ ] **Self-host Fonts** (vermeidet CDN-Latency)
- [ ] **font-display: swap** (vermeidet FOIT - Flash of Invisible Text)
- [ ] **Subset Fonts** (nur verwendete Zeichen)
- [ ] **Variable Fonts** (weniger Dateien)

**Beispiel:**
```css
@font-face {
  font-family: 'Custom Font';
  src: url('/assets/fonts/font.woff2') format('woff2');
  font-display: swap; /* Wichtig für CLS */
  font-weight: 400;
  font-style: normal;
}
```

### Google Fonts-Optimierung (falls verwendet)
```html
<!-- Preconnect für schnellere Verbindung -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Font mit display=swap -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```

---

## 5. Caching & Server-Optimierung

### Browser-Caching (via HTTP Headers)

**GitHub Pages Limitation:**
- GitHub Pages setzt automatisch Caching-Header
- Keine direkte Kontrolle über `.htaccess` oder Server-Config

**Alternative: Service Worker (PWA)**
```javascript
// sw.js - Service Worker für Offline-Caching
const CACHE_NAME = 'ppt-v1';
const urlsToCache = [
  '/',
  '/assets/css/main.css',
  '/assets/js/main.min.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

### CDN (GitHub Pages nutzt bereits Fastly CDN)
- ✅ GitHub Pages hat globales CDN
- ✅ Automatische Gzip/Brotli-Kompression
- ✅ HTTP/2 Support

**Falls Custom Domain mit Cloudflare:**
- [ ] Cloudflare CDN aktivieren
- [ ] Auto-Minify (CSS, JS, HTML)
- [ ] Rocket Loader (async JS)
- [ ] Polish (Bildoptimierung)

---

## 6. Third-Party-Scripts minimieren

### Aktuell verwendete Scripts
- ✅ FontAwesome (bereits async)
- systeme.io (Newsletter-Form)
- Giscus (Comments)
- Analytics (falls vorhanden)

### Optimierungen
- [ ] **Lazy-load Comments** (nur wenn Nutzer scrollt)
- [ ] **Defer Analytics** (nicht kritisch)
- [ ] **Self-host** wo möglich (vermeidet Third-Party-Latency)

**Lazy-load Giscus:**
```html
<!-- Nur laden wenn in Viewport -->
<div id="giscus-container"></div>
<script>
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      const script = document.createElement('script');
      script.src = 'https://giscus.app/client.js';
      script.async = true;
      document.getElementById('giscus-container').appendChild(script);
      observer.disconnect();
    }
  });
  observer.observe(document.getElementById('giscus-container'));
</script>
```

---

## 7. Monitoring & Baseline

### PageSpeed Insights Baseline

**Schritte:**
1. Öffne https://pagespeed.web.dev/
2. URL eingeben: `https://www.powerplatformtip.com`
3. Beide Tabs prüfen: **Mobile** & **Desktop**
4. Metriken dokumentieren:

| Metrik | Desktop (Vorher) | Desktop (Nachher) | Mobile (Vorher) | Mobile (Nachher) |
|--------|------------------|-------------------|-----------------|------------------|
| Performance Score | [Wert] | [Ziel: > 90] | [Wert] | [Ziel: > 85] |
| LCP | [Wert] | [< 2.5s] | [Wert] | [< 2.5s] |
| CLS | [Wert] | [< 0.1] | [Wert] | [< 0.1] |
| INP/FID | [Wert] | [< 200ms] | [Wert] | [< 200ms] |

### Tools für kontinuierliches Monitoring

#### Lighthouse CI (GitHub Actions)
```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on: [push, pull_request]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: treosh/lighthouse-ci-action@v9
        with:
          urls: |
            https://www.powerplatformtip.com
            https://www.powerplatformtip.com/about/
          uploadArtifacts: true
```

#### WebPageTest (manuell)
- URL: https://www.webpagetest.org/
- Ausführliche Performance-Analyse
- Waterfall-Diagramme
- Vergleich verschiedener Standorte

#### Chrome DevTools
- **Lighthouse** (integriert)
- **Performance Tab** (Runtime-Performance)
- **Coverage Tab** (Unused CSS/JS)
- **Network Tab** (Ressourcen-Ladezeiten)

---

## 8. Quick Wins (sofort umsetzbar)

### Priorität 1 (höchster Impact)
1. **Bilder komprimieren**
   ```bash
   # Batch-Optimierung
   find assets/images -name "*.jpg" -exec mogrify -quality 80 {} \;
   ```

2. **Lazy-loading aktivieren**
   ```html
   <!-- Alle Bilder im Content -->
   <img src="..." alt="..." loading="lazy" width="..." height="...">
   ```

3. **Width/Height für alle Bilder**
   - Verhindert CLS
   - Bereits in vielen Posts vorhanden, aber prüfen

4. **FontAwesome optimieren**
   - Nur verwendete Icons laden (Custom Subset)
   - Oder: Self-host mit Subset

### Priorität 2 (mittlerer Impact)
5. **JavaScript defer**
   ```html
   <script defer src="..."></script>
   ```

6. **Kritisches CSS inline**
   - Above-the-Fold CSS direkt in `<head>`
   - Rest async laden

7. **Preconnect für Third-Party-Domains**
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   ```

---

## 9. Langfristige Optimierungen

### Progressive Web App (PWA)
- [ ] Service Worker für Offline-Funktionalität
- [ ] Manifest.json für "Add to Homescreen"
- [ ] App-Shell-Architektur

### Server-Upgrade (falls Custom Hosting)
- [ ] HTTP/3 Support
- [ ] Brotli-Kompression
- [ ] Early Hints (HTTP 103)

### Advanced Image-Optimierung
- [ ] Automatische WebP/AVIF-Konvertierung (Build-Step)
- [ ] Responsive Image-Breakpoints optimieren
- [ ] Image CDN (Cloudinary, imgix)

---

## 10. Testing-Checklist

Vor jeder grösseren Performance-Änderung:

- [ ] **Baseline erstellen** (PageSpeed Insights)
- [ ] **Änderung implementieren**
- [ ] **Lokal testen** (`bundle exec jekyll serve`)
- [ ] **Deploy**
- [ ] **Nach 24h:** Erneuter PageSpeed-Test
- [ ] **Metriken vergleichen** (Baseline vs. Aktuell)
- [ ] **Bei Regression:** Rollback erwägen

### Red Flags (sofort prüfen)
- Performance Score sinkt > 10 Punkte
- LCP steigt > 500ms
- CLS steigt > 0.05
- Neue Console Errors im Browser

---

## 11. Performance-Budget

**Definition:** Maximale Grössen für Ressourcen, die nicht überschritten werden dürfen

| Ressourcentyp | Budget |
|---------------|--------|
| HTML | < 50 KB |
| CSS (total) | < 100 KB |
| JavaScript (total) | < 150 KB |
| Bilder (pro Seite) | < 500 KB |
| Fonts | < 100 KB |
| Total Page Weight | < 1 MB |

**Enforcement:**
```yaml
# .github/workflows/performance-budget.yml (optional)
# Warnung bei Überschreitung des Budgets
```

---

## 12. Nächste Schritte

### Sofort (diese Woche)
1. [ ] PageSpeed Insights Baseline erstellen (Homepage, Top-Posts)
2. [ ] Alle Bilder in `assets/images/` komprimieren
3. [ ] `loading="lazy"` für alle Content-Bilder
4. [ ] Width/Height für Bilder in Top-10 Posts

### Mittelfristig (nächste 2 Wochen)
5. [ ] Kritisches CSS inline
6. [ ] JavaScript defer für non-critical Scripts
7. [ ] Font-display: swap für alle Fonts
8. [ ] Lazy-load Giscus Comments

### Langfristig (nächste 4 Wochen)
9. [ ] WebP-Konvertierung für alle Bilder
10. [ ] Service Worker für Offline-Caching
11. [ ] Lighthouse CI in GitHub Actions
12. [ ] Performance-Review nach 8 Wochen

---

**Verantwortlich:** Dev-Team / Marcel Lehmann  
**Review:** Wöchentlich (PageSpeed Check)  
**Nächster Meilenstein:** PageSpeed Score > 90 (Desktop), > 85 (Mobile)
