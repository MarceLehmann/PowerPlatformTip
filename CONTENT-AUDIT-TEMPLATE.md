# Content-Audit Template – PowerPlatformTip

**Datum:** 24. Oktober 2025  
**Zweck:** Inventar aller Seiten/Posts, Duplicate Content erkennen, Zielkeywords zuordnen

---

## Anleitung

1. **Export aus Jekyll:**  
   ```bash
   # Alle Posts auflisten
   find _posts -name "*.md" | sort
   
   # Alle Pages auflisten
   find _pages -name "*.md" | sort
   ```

2. **CSV erstellen:**  
   Kopiere die Ausgabe und erstelle eine CSV-Datei mit folgenden Spalten:
   - URL
   - Titel
   - Aktuelles Title-Tag (aus Frontmatter)
   - Aktuelle Meta-Description (aus Frontmatter)
   - Datum (date)
   - Letztes Update (updated/last_modified_at)
   - Kategorien
   - Tags
   - Zielkeyword (neu zuweisen)
   - Priorität (High/Medium/Low)
   - Status (OK / Needs Update / Duplicate / Outdated / Delete)
   - Anmerkungen

3. **Prüfkriterien:**
   - **Duplicate Content:** Gleiche Themen mehrfach behandelt?
   - **Veraltete Artikel:** > 2 Jahre alt, keine Updates, veraltete Infos?
   - **Fehlende Metadaten:** Kein Title, keine Description?
   - **Schwache Titles:** Zu generisch, kein Keyword?
   - **Kanibalisierung:** Mehrere Seiten targeten gleiches Keyword?

---

## Beispiel-Einträge

| URL | Titel | Title-Tag | Meta-Desc | Datum | Update | Kategorie | Tags | Zielkeyword | Priorität | Status | Anmerkungen |
|-----|-------|-----------|-----------|-------|--------|-----------|------|-------------|-----------|--------|-------------|
| `/about/` | About PowerPlatformTip | Über Marcel... | Learn about... | - | 2025-10 | Page | - | Marcel Lehmann MVP | High | OK | Bereits optimiert |
| `/newsletter/` | Power Platform Tips Newsletter | Newsletter | Subscribe... | - | - | Page | - | Power Platform Newsletter | High | Needs Update | Description zu kurz |
| `/tip-127-special-user-informations/` | Special User Informations | PowerPlatformTip #127 | - | 2024-10 | - | PowerPlatform | PowerApps | Power Apps User Info | Medium | Needs Update | Kein excerpt |
| `/power-apps-print-directly-printer-api/` | Print Directly | Power Apps Print... | Discover how... | 2020-12 | 2025-06 | Article | PowerApps, API | Power Apps Drucken | Medium | OK | Kürzlich aktualisiert |

---

## Prioritätslogik

### High Priority
- Homepage, About, Newsletter, Top-Landing-Pages
- Posts mit hohem Traffic (aus GSC/Analytics)
- Posts mit Position 4–10 in Google (Quick-Win-Potenzial)

### Medium Priority
- Posts mit moderatem Traffic
- Evergreen-Content (immer aktuell)
- Tutorial-Serien

### Low Priority
- Sehr alte Posts ohne Traffic
- Nischen-Themen
- News/Announcements (zeitlich begrenzt)

---

## Status-Definitionen

- **OK:** Metadaten vollständig, aktuell, optimiert
- **Needs Update:** Fehlende/schwache Metadaten, kein Zielkeyword
- **Duplicate:** Thema wird von anderem Post besser abgedeckt → 301 Redirect erwägen
- **Outdated:** Veraltete Infos, > 2 Jahre alt → Update oder Merge
- **Delete:** Kein Traffic, irrelevant, veraltet → 410 Gone oder 301 zu besserem Post

---

## Aktionsplan nach Audit

1. **High Priority Posts (Top 20):**
   - Metadaten optimieren (Title, Description)
   - Zielkeyword definieren
   - Interne Verlinkung prüfen
   - Bilder Alt-Text hinzufügen

2. **Duplicate Content:**
   - Besten Post identifizieren
   - Schwächeren Post redirecten (301) oder mergen
   - Canonical-Tags prüfen

3. **Veraltete Posts:**
   - Update planen (neue Screenshots, aktuelle Infos)
   - `updated:`-Datum im Frontmatter setzen
   - Hinweis "Aktualisiert am..." einfügen

4. **Fehlende Metadaten:**
   - Batch-Update für alle Posts ohne excerpt/description
   - Template aus `SEO-META-GUIDELINES.md` nutzen

---

## Tools für Audit

- **Screaming Frog:** Kompletter Site-Crawl (Titles, Descriptions, H1, Images)
- **Google Search Console:** Top-Queries, Impressions, CTR, Position
- **Google Analytics:** Top-Landing-Pages, Traffic, Engagement
- **Ahrefs/Semrush:** Keyword-Rankings, Backlinks, Konkurrenzanalyse

---

## Automatisierungsskript (optional)

```bash
#!/bin/bash
# content-audit.sh - Extrahiert Frontmatter aus allen Posts

echo "URL,Title,Description,Date,Categories,Tags" > content-audit.csv

for file in _posts/*.md; do
  url=$(basename "$file" .md)
  title=$(grep -m1 "^title:" "$file" | sed 's/title: *"*//;s/"*$//')
  desc=$(grep -m1 "^description:\|^excerpt:" "$file" | sed 's/.*: *"*//;s/"*$//')
  date=$(grep -m1 "^date:" "$file" | sed 's/date: *//')
  cats=$(grep -m1 "^categories:" "$file" | sed 's/categories: *//')
  tags=$(grep -m1 "^tags:" "$file" | sed 's/tags: *//')
  
  echo "\"$url\",\"$title\",\"$desc\",\"$date\",\"$cats\",\"$tags\"" >> content-audit.csv
done

echo "Audit CSV created: content-audit.csv"
```

---

## Nächste Schritte

1. [ ] Script ausführen oder manuell Posts inventarisieren
2. [ ] CSV in Google Sheets/Excel importieren
3. [ ] Status und Priorität für jeden Post festlegen
4. [ ] Zielkeywords recherchieren und zuweisen
5. [ ] Top 20 Posts optimieren (Metadaten)
6. [ ] Duplicate/Outdated Content-Plan erstellen
7. [ ] Batch-Updates durchführen

---

**Verantwortlich:** Content Team / Marcel Lehmann  
**Review:** Alle 3 Monate (nächster: Januar 2026)
