# SEO-Roadmap für PowerPlatformTip
**Erstellt:** 24. Oktober 2025  
**Eigentümer:** Marcel Lehmann  
**Webseite:** https://www.powerplatformtip.com

---

## Übersicht
Diese Roadmap organisiert alle SEO-Massnahmen nach dem offiziellen Google SEO-Startleitfaden in priorisierte Bereiche. Alle Änderungen müssen in `SEO-CHANGELOG.md` dokumentiert werden.

---

## Prioritätsstufen

### P0 – Kritische Grundlagen (sofort/innerhalb 2 Wochen)
**Ziel:** Technische Blocker beseitigen, Indexierung sicherstellen, Basis-Metadaten optimieren

#### 1. Crawlability & Indexierung ✅
- **Status:** ✅ Abgeschlossen (24.10.2025)
- **Massnahmen:**
  - robots.txt erstellt und optimiert
  - Sitemap-Plugin vorhanden (jekyll-sitemap)
  - Canonical-Tags implementiert (via seo.html)
  - CSS/JS für Crawler erlaubt
- **Nächste Schritte:**
  - Site:-Check in Google durchführen
  - In Google Search Console verifizieren

#### 2. Google Search Console + Sitemap
- **Tasks:**
  - Property anlegen (Domain- oder URL-Präfix)
  - Sitemap einreichen: `https://www.powerplatformtip.com/sitemap.xml`
  - Indexabdeckung baseline exportieren
  - E-Mail-Benachrichtigungen aktivieren
- **Verantwortlich:** Site Owner
- **Deadline:** KW 44/2025
- **Akzeptanz:** GSC-Property verifiziert, sitemap eingereicht, erste Fehlerübersicht vorhanden

#### 3. Sofort-Fixes: Noindex/Robots/HTTP-Header
- **Tasks:**
  - Prüfen: keine produktiven Seiten mit unbeabsichtigtem noindex
  - Staging/Dev-Umgebungen von Indexierung ausschliessen (falls vorhanden)
  - 404-Seite in robots.txt disallowed (bereits erledigt)
- **Akzeptanz:** Alle wichtigen Seiten indexierbar

#### 4. Title & Meta-Description Basis
- **Tasks:**
  - Top-10 Seiten prüfen (Homepage, About, Newsletter, Top-Posts)
  - Titles ≤60 Zeichen, Meta ≈120–160 Zeichen
  - Markenname konsistent am Ende („- PowerPlatformTip")
  - Jede Seite unique Title/Description
- **Dateien:** `_includes/seo.html`, `_config.yml`, `_pages/*.md`, `_posts/*.md`
- **Akzeptanz:** Top-Seiten optimiert, Vorlage für neue Posts dokumentiert

---

### P1 – Inhalt & Onpage (2–6 Wochen)

#### 5. Strukturierte Daten (JSON-LD)
- **Tasks:**
  - Article-Schema für alle Blogposts
  - Organization/Person-Schema (Homepage)
  - BreadcrumbList-Schema
  - FAQ-Schema (falls relevante Seiten vorhanden)
- **Dateien:** `_includes/schema.html`, `_layouts/single.html`
- **Test:** Rich Results Test (https://search.google.com/test/rich-results)
- **Akzeptanz:** Keine Fehler im Rich Results Test, relevante Rich Snippets möglich

#### 6. Content-Audit + Keyword-Plan (CH-Deutsch)
- **Tasks:**
  - Inventar aller Seiten/Posts (~150+ Posts)
  - Duplicate Content markieren
  - Veraltete Artikel identifizieren (> 2 Jahre alt, ggf. Update nötig)
  - Zielkeywords pro Seite definieren (Schweizer Deutsch/Hochdeutsch)
  - Prioritäten: High/Medium/Low
- **Output:** CSV/Spreadsheet mit: URL, Titel, Zielkeyword, Kategorie, empfohlene Änderung, Priorität
- **Akzeptanz:** Audit abgeschlossen, Zielkeywords zugeordnet

#### 7. Bilder & Media optimieren
- **Tasks:**
  - Alt-Attribute für alle Content-Bilder ergänzen
  - Bildgrössen komprimieren (WebP-Option prüfen)
  - Responsive srcset wo nötig
  - Dateinamen beschreibend (power-apps-print-api.jpg statt img1.jpg)
- **Orte:** `assets/images/`, externe Bilder in Posts
- **Akzeptanz:** Alle relevanten Bilder haben Alt-Text, PageSpeed-Empfehlungen reduziert

#### 8. PageSpeed & Core Web Vitals
- **Tasks:**
  - PageSpeed Insights Baseline für wichtige Seiten (Homepage, Top-Posts)
  - LCP, CLS, INP/FID messen
  - CSS/JS kritisch inline/deferred
  - Bilder lazy-loading
  - Caching/Compression prüfen
  - CDN-Option evaluieren
- **Tools:** PageSpeed Insights, Lighthouse
- **Akzeptanz:** Dokumentierte Metriken, messbare Verbesserung (Ziel: LCP < 2.5s, CLS < 0.1)

---

### P2 – Promotion, Offpage & Langfristig (6–12 Wochen)

#### 9. Interne Verlinkung & Navigation
- **Tasks:**
  - Breadcrumbs aktivieren (`breadcrumbs: true` in `_config.yml`)
  - Thematische Gruppierung prüfen (Categories/Tags)
  - Footer-/Sidebar-Links optimieren
  - Sitemap-Konsistenz sicherstellen
- **Akzeptanz:** Logische interne Linkstruktur, bessere PageRank-Verteilung

#### 10. Offpage & Promotion
- **Tasks:**
  - Social-Sharing-Buttons (bereits vorhanden, prüfen)
  - Newsletter-Integration (bereits vorhanden auf /newsletter/)
  - Outreach-Liste erstellen (Power Platform Community, LinkedIn)
  - URL auf Offline-Materialien (Visitenkarten, E-Mail-Signatur)
  - Guest-Posting-Möglichkeiten evaluieren
- **Akzeptanz:** Veröffentlichungs-Checklist mit mindestens 3 Kanälen

#### 11. Monitoring & Reporting
- **Tasks:**
  - GSC-Dashboards konfigurieren
  - PageSpeed-Monitoring (wöchentlich)
  - KPI-Tracking: Impressions, CTR, Avg. Position, LCP/CLS
  - Wöchentliche/monatliche Reports
  - 8-Wochen-Review-Termin planen (ca. KW 52/2025)
- **Akzeptanz:** Automatisierte Reports & Kalendererinnerung

#### 12. Review nach 8 Wochen (geplant: KW 52/2025)
- **Tasks:**
  - Baseline vs. aktuelle Daten
  - Erfolgsanalyse (Traffic, Rankings, Core Web Vitals)
  - Neue Prioritäten setzen
  - Learnings dokumentieren
- **Akzeptanz:** Review-Report mit KPIs, Learnings, To-Dos für nächste 8 Wochen

---

## Konkrete Datei-Orte im Repo

| Bereich | Datei/Ordner | Beschreibung |
|---------|--------------|--------------|
| Meta/Canonical | `_includes/seo.html` | Title, Meta, Canonical, OG-Tags |
| Schema | `_includes/schema.html` | JSON-LD strukturierte Daten |
| Robots | `/robots.txt` | Crawler-Steuerung |
| Sitemap | Auto-generiert | Via jekyll-sitemap Plugin |
| Config | `_config.yml` | Site-weite Einstellungen |
| Posts | `_posts/*.md` | Frontmatter: title, description, excerpt |
| Pages | `_pages/*.md` | Frontmatter: title, description, keywords |
| Layouts | `_layouts/single.html` | Artikel-Template |
| Bilder | `assets/images/` | Lokale Bilder |

---

## Messung / KPIs

### Technisch
- Indexierungsstatus (GSC)
- Crawl Errors
- Sitemap-Status
- Core Web Vitals (LCP, CLS, INP)

### Discovery
- Impressions (GSC)
- Klicks (GSC)
- CTR (GSC)
- Avg. Position (GSC)

### Content
- Organischer Traffic pro Zielseite
- Verweildauer
- Engagement-Rate

---

## 8-Wochen-Review-Format (Template)

**Zeitraum:** [Datum-Start] → [Datum-Ende]

### Baseline-Metriken (vor Implementierung)
- Impressions: [Wert]
- Klicks: [Wert]
- CTR: [Wert]
- Avg. Position: [Wert]
- LCP: [Wert]
- CLS: [Wert]

### Verbesserungen
- Impressions: [alt] → [neu] ([+/- %])
- Klicks: [alt] → [neu] ([+/- %])
- CTR: [alt] → [neu] ([+/- %])
- Avg. Position: [alt] → [neu] ([+/- %])
- LCP: [alt] → [neu] ([+/- %])
- CLS: [alt] → [neu] ([+/- %])

### Umgesetzte Massnahmen
- [Liste mit PR-Links / Changelog-Referenzen]

### Fehler/Regressionen
- [Liste]

### Nächste Schritte (konkret, priorisiert)
1. [Task 1]
2. [Task 2]
3. [Task 3]

### Verantwortliche & Deadlines
- [Name]: [Task] – [Deadline]

---

## Empfohlene Tools

- **Google Search Console** (unbedingt)
- **PageSpeed Insights** / Lighthouse
- **Rich Results Test** / Structured Data Testing Tool
- **Screaming Frog** (für umfassenden Crawl)
- **Keyword-Tools** mit CH-Daten (Google Keyword Planner, Sistrix)
- **Looker Studio** (für automatisierte Reports)

---

## Was du NICHT tun musst (laut Google)

- ❌ Meta-Keywords-Tag verwenden (Google ignoriert es)
- ❌ Keyword-Stuffing (natürlich schreiben)
- ❌ Keywords in Domain/URL zwanghaft einbauen (geringer Einfluss)
- ❌ Mindest-/Maximalwortzahl anstreben (Qualität > Quantität)
- ❌ Subdomain vs. Unterverzeichnis diskutieren (SEO-technisch gleichwertig)
- ❌ Angst vor Duplicate Content (keine direkte Strafe, aber ineffizient)
- ❌ E-E-A-T als direkten Ranking-Faktor sehen (aber Expertise/Vertrauen wichtig)

---

## Changelog-Verweis

Alle SEO-Änderungen **müssen** in `SEO-CHANGELOG.md` dokumentiert werden.  
Jeder Pull Request mit SEO-Änderungen **muss** einen Changelog-Eintrag referenzieren.

**Commit-Format:**  
`seo: [kurze Beschreibung] (siehe SEO-CHANGELOG.md)`

---

**Nächster Review:** KW 52/2025 (ca. 19. Dezember 2025)  
**Verantwortlich:** Marcel Lehmann / Dev-Team
