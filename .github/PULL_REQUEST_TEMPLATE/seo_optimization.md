# SEO Pull Request Template

**PR-Typ:** SEO-Optimierung  
**Datum:** [Datum einfügen]  
**Autor:** [Name]

---

## Zusammenfassung
[Kurze Beschreibung der SEO-Änderungen in 1-2 Sätzen]

---

## Änderungen

### 📝 Metadaten
- [ ] Title-Tags optimiert (≤60 Zeichen)
- [ ] Meta-Descriptions optimiert (120-160 Zeichen)
- [ ] Keywords recherchiert und integriert
- [ ] Schweizer Schreibweise geprüft

**Betroffene Dateien:**
- [ ] `_includes/seo.html`
- [ ] `_config.yml`
- [ ] `_pages/*.md`
- [ ] `_posts/*.md`
- [ ] Andere: [angeben]

### 🏗️ Strukturierte Daten
- [ ] JSON-LD Schema hinzugefügt/erweitert
- [ ] Article-Schema für Posts
- [ ] BreadcrumbList-Schema
- [ ] Organization/Person-Schema
- [ ] Andere: [angeben]

**Betroffene Dateien:**
- [ ] `_includes/schema.html`
- [ ] `_layouts/*.html`

### 🔗 Technische SEO
- [ ] Canonical-Tags geprüft/optimiert
- [ ] robots.txt aktualisiert
- [ ] Sitemap-Konfiguration angepasst
- [ ] Noindex/Nofollow-Tags gesetzt
- [ ] 301-Redirects eingerichtet
- [ ] Breadcrumbs aktiviert/optimiert

**Betroffene Dateien:**
- [ ] `robots.txt`
- [ ] `_config.yml`
- [ ] `_includes/seo.html`
- [ ] Andere: [angeben]

### 🖼️ Bilder & Media
- [ ] Alt-Texte hinzugefügt/optimiert
- [ ] Bildgrössen optimiert (Kompression)
- [ ] Responsive srcset implementiert
- [ ] Dateinamen beschreibend umbenannt
- [ ] Lazy-loading aktiviert

**Betroffene Dateien:**
- [ ] `assets/images/`
- [ ] `_posts/*.md` (Bild-Referenzen)

### 📄 Content
- [ ] Duplicate Content bereinigt
- [ ] Veraltete Inhalte aktualisiert
- [ ] Interne Verlinkung verbessert
- [ ] Keywords natürlich integriert
- [ ] Überschriften-Hierarchie (H1-H6) optimiert

**Betroffene Dateien:**
- [ ] `_posts/*.md`
- [ ] `_pages/*.md`

### ⚡ Performance
- [ ] CSS/JS optimiert
- [ ] Caching-Header konfiguriert
- [ ] Core Web Vitals geprüft
- [ ] PageSpeed Score verbessert

**Betroffene Dateien:**
- [ ] `assets/css/`
- [ ] `assets/js/`
- [ ] `_includes/head.html`

---

## Tests & Validierung

### ✅ Vor Merge durchgeführt:
- [ ] **Rich Results Test** (https://search.google.com/test/rich-results)  
  Ergebnis: [Link zu Screenshot oder Beschreibung]
  
- [ ] **PageSpeed Insights** (https://pagespeed.web.dev/)  
  Desktop Score: [Wert] | Mobile Score: [Wert]
  
- [ ] **W3C Markup Validation** (https://validator.w3.org/)  
  Ergebnis: [Anzahl Fehler/Warnungen]
  
- [ ] **Broken Links Check**  
  Tool: [z.B. Screaming Frog, broken-link-checker]  
  Ergebnis: [OK / Anzahl Fehler]
  
- [ ] **Schema Markup Validator**  
  Ergebnis: [Link oder Beschreibung]

- [ ] **Local Build Test**  
  ```bash
  bundle exec jekyll serve
  # Browser-Check: http://localhost:4000
  ```
  Ergebnis: [OK / Fehler beschreiben]

### 📊 Metriken (vor/nach)
| Metrik | Vorher | Nachher | Änderung |
|--------|--------|---------|----------|
| PageSpeed Desktop | [Wert] | [Wert] | [+/- %] |
| PageSpeed Mobile | [Wert] | [Wert] | [+/- %] |
| LCP (Largest Contentful Paint) | [Wert] | [Wert] | [+/- ms] |
| CLS (Cumulative Layout Shift) | [Wert] | [Wert] | [+/-] |
| Schema Errors | [Anzahl] | [Anzahl] | [+/-] |

---

## SEO-Changelog-Eintrag

- [ ] **Eintrag in `SEO-CHANGELOG.md` erstellt**

```markdown
#### [Datum] | [Autor] | [Bereich] | [Kurzbeschreibung]

**Änderungen:**
- [Detaillierte Beschreibung]

**Dateien:**
- [Datei 1] (neu/geändert)
- [Datei 2] (neu/geändert)

**Impact:**
- [Erwartete SEO-Auswirkung]

**Commit/PR:** #[PR-Nummer]
```

---

## Checkliste vor Merge

- [ ] Alle Tests bestanden (siehe oben)
- [ ] SEO-Changelog aktualisiert
- [ ] Branch von `master` aktuell
- [ ] Keine Merge-Konflikte
- [ ] Code-Review von mindestens 1 Person
- [ ] Lokaler Build erfolgreich
- [ ] Keine neuen Console-Errors im Browser
- [ ] Mobile Responsiveness geprüft

---

## Zusätzliche Informationen

### Verwandte PRs/Issues:
- [Liste verwandter PRs/Issues]

### Nächste Schritte nach Merge:
- [ ] Google Search Console: Indexierung anfragen (falls nötig)
- [ ] PageSpeed Insights: neue Baseline erstellen
- [ ] GSC Performance beobachten (7-14 Tage)
- [ ] Ggf. weitere Optimierungen planen

### Screenshots/Links:
[Falls relevant: Screenshots von Rich Results Test, PageSpeed, etc.]

---

## Review-Notizen
[Platz für Reviewer-Kommentare]

---

**Commit-Message-Format:**
```
seo: [kurze Beschreibung der Änderung]

- Detail 1
- Detail 2
- Detail 3

Siehe SEO-CHANGELOG.md für vollständige Dokumentation.
Closes #[Issue-Nummer falls vorhanden]
```

---

**Reviewer:** [@mention]  
**Merge nach:** Code-Review ✅ + alle Tests ✅
