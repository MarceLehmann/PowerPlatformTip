# SOCIALMEDIA Content Management

Dieses System verarbeitet KI-generierte PowerPlatformTip-Inhalte aus Chat-Protokollen und erstellt daraus Blog-Posts und Newsletter.

## 📁 Ordnerstruktur

```
SOCIALMEDIA/
├── 1_INPUT/          # KI-Chat-Protokolle hier ablegen
├── BLOG/             # Verarbeitete Blog-Posts (Jekyll Markdown)
├── NEWSLETTER/       # Verarbeitete Newsletter-Inhalte (HTML)
├── process-tip.sh    # Automatisierungs-Script
└── ANWEISUNG.md      # Diese Datei
```

## 🔄 Workflow

### 1. Input-Format (KI-Chat-Protokoll)

Lege die KI-generierte Markdown-Datei in den `1_INPUT/` Ordner. Die Datei enthält typischerweise:

- **PHASE 0**: Intake & Validation (Metadaten)
- **PHASE 1**: Review Tip (ausführlicher Content)
- **PHASE 2**: Jekyll Markdown (Blog-Post mit Frontmatter)
- **PHASE 3**: HTML Newsletter (optional)

Das Script liest **von unten nach oben**, da die KI schrittweise Content generiert hat.

### 2. Verarbeitung starten

```bash
cd /workspaces/PowerPlatformTip/SOCIALMEDIA
./process-tip.sh
```

Oder in GitHub Copilot Chat:
```
Verarbeite die PowerPlatformTips im SOCIALMEDIA/1_INPUT Ordner
```

### 3. Output

Das Script extrahiert automatisch:

**Aus PHASE 2 (Jekyll Markdown):**
- → `BLOG/YYYY-MM-DD-powerplatformtip-NNN-slug.md`
- Kompletter Blog-Post mit Frontmatter für Jekyll

**Aus PHASE 3 (HTML Newsletter):**
- → `NEWSLETTER/YYYY-MM-DD-tip-NNN.html`
- Fertiger HTML-Newsletter für E-Mail-Versand

### 4. Archivierung

Verarbeitete Dateien werden automatisch nach `1_INPUT/_PROCESSED/` verschoben.

## 📋 Typische Struktur im Input

```markdown
### PHASE 2 · JEKYLL MARKDOWN (.md)

\`\`\`markdown
---
title: "#PowerPlatformTip 145 – 'Power Platform Tools'"
date: 2025-11-25
categories:
    - Article
    - PowerPlatformTip
tags:
    - PowerAutomate
    - PowerApps
excerpt: "Kurzbeschreibung..."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: false
---

## 💡 Challenge
Content hier...

## ✅ Solution
Content hier...
\`\`\`

### PHASE 3 · HTML NEWSLETTER

\`\`\`html
<!DOCTYPE html>
<html>
<body>
Newsletter HTML Content...
</body>
</html>
\`\`\`
```

## 🔍 Was das Script macht

1. **Findet PHASE 2-Blöcke** und extrahiert den Jekyll Markdown zwischen den Code-Backticks
2. **Findet PHASE 3-Blöcke** und extrahiert das HTML für Newsletter
3. **Erkennt Tip-Nummer** aus dem Title (z.B. "#PowerPlatformTip 145")
4. **Generiert Dateinamen** automatisch:
   - Blog: `2025-11-25-powerplatformtip-145-power-platform-tools.md`
   - Newsletter: `2025-11-25-tip-145.html`
5. **Archiviert** verarbeitete Input-Dateien

## ✅ Vorteile

- **Zero-Config**: Einfach Datei ablegen und Script ausführen
- **KI-optimiert**: Versteht die Struktur von KI-Chat-Protokollen
- **Automatische Extraktion**: Kein manuelles Copy-Paste mehr
- **Sichere Archivierung**: Keine Gefahr, Input-Dateien zu verlieren

## 📝 Hinweise

- Das Script liest die Datei von unten nach oben, um die neueste Version der Phasen zu finden
- `toc_sticky: false` wird automatisch gesetzt (TOC-Problem behoben)
- Verarbeitete Dateien landen in `_PROCESSED` mit Zeitstempel
- Blog-Posts erscheinen automatisch auf der Website nach dem nächsten Jekyll-Build


## Folder Structure

```
SOCIALMEDIA/
├── 1_INPUT/          # Place combined content files here
├── BLOG/             # Processed blog posts (Markdown)
├── NEWSLETTER/       # Processed newsletter content (Markdown)
└── process-tip.sh    # Automation script
```

## Workflow

### 1. Input Format

Place your combined PowerPlatformTip file in `1_INPUT/` folder with this structure:

```markdown
---
title: "Your Tip Title"
tip_number: 123
date: 2025-12-01
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
---

<!-- BLOG START -->
# Blog Content

Your detailed blog post content here...
This section will become the blog post.

## Section 1
Content...

## Section 2
More content...

<!-- BLOG END -->

<!-- NEWSLETTER START -->
# Newsletter Version

Shorter, concise version for newsletter...
Quick tips and highlights.

## Quick Takeaways
- Point 1
- Point 2
- Point 3

<!-- NEWSLETTER END -->
```

### 2. Processing

Run the processing script:
```bash
./SOCIALMEDIA/process-tip.sh
```

Or using the GitHub Copilot command:
```
Process the PowerPlatformTip in SOCIALMEDIA/1_INPUT folder
```

### 3. Output

The script will:
- Extract BLOG content → `BLOG/YYYY-MM-DD-tip-number-slug.md`
- Extract NEWSLETTER content → `NEWSLETTER/YYYY-MM-DD-tip-number.md`
- Keep proper frontmatter for Jekyll
- Archive processed input file

## File Naming Convention

**Blog posts:**
- Format: `YYYY-MM-DD-powerplatformtip-{number}-{slug}.md`
- Example: `2025-12-01-powerplatformtip-150-power-apps-tips.md`

**Newsletters:**
- Format: `YYYY-MM-DD-tip-{number}.md`
- Example: `2025-12-01-tip-150.md`

## Markers

Use these HTML comments to separate content:
- `<!-- BLOG START -->` and `<!-- BLOG END -->` for blog content
- `<!-- NEWSLETTER START -->` and `<!-- NEWSLETTER END -->` for newsletter content

## Notes

- Ensure all required frontmatter fields are present in the input file
- The script preserves all frontmatter metadata
- Processed files are automatically moved to an `_PROCESSED` subfolder in INPUT
- Blog posts will automatically appear on the website after processing
- Newsletter content is ready for email distribution
