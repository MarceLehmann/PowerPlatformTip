# SEO-Changelog – PowerPlatformTip

Dieses Dokument trackt alle SEO-relevanten Änderungen am PowerPlatformTip-Blog.  
**Format:** Datum | Autor | Bereich | Änderung | Datei/URL | PR/Commit

---

## 2025

### Oktober

#### 24.10.2025 | Marcel Lehmann | Technische Grundlagen | SEO-Optimierung Initialisierung

**Änderungen:**
- ✅ `robots.txt` erstellt und optimiert
  - Alle Crawler erlaubt
  - Sitemap referenziert
  - CSS/JS für Rendering erlaubt
  - 404/Search-Seiten disallowed
  
- ✅ `SEO-ROADMAP.md` erstellt
  - Vollständige Roadmap mit Prioritäten (P0/P1/P2)
  - 8-Wochen-Review-Plan
  - KPI-Definitionen
  - Tool-Empfehlungen
  
- ✅ `SEO-CHANGELOG.md` erstellt (diese Datei)
  - Template für zukünftige Einträge
  
- ✅ Schema.html erweitert (geplant)
  - Article-Schema für Blogposts
  - BreadcrumbList-Schema
  - Verbesserte Organization-Daten

- ✅ Breadcrumbs aktiviert (geplant)
  - `_config.yml`: breadcrumbs: true

**Dateien:**
- `/robots.txt` (neu)
- `/SEO-ROADMAP.md` (neu)
- `/SEO-CHANGELOG.md` (neu)
- `_includes/schema.html` (erweitert)
- `_config.yml` (Breadcrumbs aktiviert)
- `_includes/seo.html` (reviewed, optimiert)

**Commit:** `seo: initial SEO optimization - robots, roadmap, schema, breadcrumbs`

**Nächste Schritte:**
- [ ] Google Search Console einrichten und verifizieren
- [ ] Sitemap in GSC einreichen
- [ ] Top-10 Seiten Meta-Descriptions optimieren
- [ ] PageSpeed Insights Baseline erstellen
- [ ] Content-Audit starten

---

## Template für zukünftige Einträge

```markdown
#### [Datum] | [Autor] | [Bereich] | [Kurzbeschreibung]

**Änderungen:**
- [Detaillierte Beschreibung der Änderung]

**Dateien:**
- [Datei 1] ([neu/geändert/gelöscht])
- [Datei 2] ([neu/geändert/gelöscht])

**Impact:**
- [Erwartete Auswirkung auf SEO/Performance]

**Commit/PR:** [Link oder Commit-Hash]

**Tests:**
- [ ] Rich Results Test passed
- [ ] PageSpeed Insights geprüft
- [ ] GSC indexiert

---
```

## Kategorien für Changelog-Einträge

- **Technische Grundlagen:** robots.txt, sitemap, canonical tags, noindex
- **Metadaten:** Title, Meta-Description, Keywords
- **Strukturierte Daten:** JSON-LD, Schema.org
- **Content:** Neue Posts, Updates, Rewrites
- **Performance:** PageSpeed, Core Web Vitals, Caching
- **Interne Verlinkung:** Navigation, Breadcrumbs, Sitemap
- **Bilder:** Alt-Text, Kompression, responsive Images
- **Offpage:** Backlinks, Social Sharing, Promotion

---

**Letzte Aktualisierung:** 24.10.2025  
**Nächster Review:** KW 52/2025 (19. Dezember 2025)
