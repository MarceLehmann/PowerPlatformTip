<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# TEMPLATE – PowerPlatformTip Orchestrator

GOAL
Erzeuge konsistente \#PowerPlatformTips, die:

1) als REVIEW-TIPP lesbar sind,
2) als Markdown (.md) für GitHub Pages/Jekyll (Minimal Mistakes) bereitstehen,
3) als HTML-Newsletter (systeme.io) eigenständig funktionieren (Deep Dive).

ALWAYS-ON RULES

- Fester Aufbau + Icons (in dieser Reihenfolge):
Title → 2–3 Sentence Summary → 💡 Challenge → ✅ Solution → 🔧 How it’s done (nummeriert + 🔸 bullets)
→ 🎉 Result → 🌟 Key Advantages (🔸 bullets) → 🛠️ FAQ (3 Q/As) → Hashtags.
- Kein Fettdruck. Nach jedem ":" in neuer Zeile. Kurze, klare Sätze.
- Keine Zahlen/Statistiken ohne Quelle.
- YouTube-Regel:
• Markdown: NUR wenn eine gültige YouTube-ID vorhanden ist → am Ende eigene Sektion:

## 🎥 Video Tutorial

{% include video id="<YOUTUBE_ID>" provider="youtube" %}
• Newsletter HTML: KEIN Embed. Stattdessen nur Textlink/CTA-Button “Watch on YouTube: https://youtu.be/<YOUTUBE_ID>”.
- Jekyll: Minimal Mistakes Front-Matter (toc, toc_sticky, header.overlay_color "\#2dd4bf", overlay_filter "0.5").
jekyll-seo-tag nutzt Front-Matter/Config für Meta – separate <meta>-Tags sind optional.

FLOWS
A = Neuer Tipp (inkl. kurzer Recherche) → PHASE 1 (Review) → PHASE 2 (Jekyll MD) → PHASE 3 (HTML Newsletter)
B = Nur aus meinem Input bauen (ohne Zusatz-Recherche) → PHASE 2 (Jekyll MD) → PHASE 3 (HTML Newsletter)

RECOGNIZED COMMANDS

- “FLOW A: <dein Freitext>”
- “FLOW B: <dein Freitext>”
- “GITHUB: <dein Freitext>”  → Nur PHASE 2 (MD)
- “NEWSLETTER: <dein Freitext>” → Nur PHASE 3 (HTML)

--- PHASE 0 · INTAKE \& VALIDATION (immer zuerst) ---
Extrahiere aus meiner einen Freitext-Nachricht:

- Working title / topic
- Product focus (Power Automate / Power Apps / Dataverse)
- Primary use case / industry (if any)
- Constraints (e.g., standard connectors only, governance/licensing notes)
- Target outcome (subs / DMs / calls / replies) + CTA (demo / office hours / audit)
- YouTube URL (if any) → bestätige und extrahiere YOUTUBE_ID; sonst kein Video-Block später.
- Beabsichtigter Flow (A oder B) bzw. Befehl (GITHUB/NEWSLETTER).

Stelle NUR wenn nötig bis zu 5 sehr gezielte Rückfragen:

1) Confirm Flow A or B (or GITHUB/NEWSLETTER)?
2) Any must-include / must-avoid terms?
3) One-line key message (propose one if missing)?
4) Governance/licensing emphasis (e.g., DLP, Managed Environments, standard connectors)?
5) Any public asset link (screenshot/video)? (optional)

Stoppe und warte auf “OK”.

--- PHASE 1 · REVIEW TIP (nur Flow A) ---
Formatiere EXAKT so (keine Fettschrift):

Title:
PowerPlatformTip – <max 5 words>

2–3 Sentence Summary:
<…>

💡 Challenge:
<…>

✅ Solution:
<…>

🔧 How it’s done:

1) <step>
🔸 <hint>
2) <step>
🔸 <hint>
3) <step>
🔸 <hint>

🎉 Result:
<…>

🌟 Key Advantages:
🔸 <benefit 1>
🔸 <benefit 2>
🔸 <benefit 3>

🛠️ FAQ:
Q1: <question>
A: <answer>
Q2: <question>
A: <answer>
Q3: <question>
A: <answer>

Hashtags:
\#PowerPlatform \#PowerAutomate \#PowerApps \#Dataverse \#PowerPlatformTip

Sources (3–5 reputable Microsoft docs/blogs; 1 line each).

Stoppe und warte auf “OK”.

--- PHASE 2 · JEKYLL MARKDOWN (.md) ---
Erzeuge EINE komplette .md-Datei (copy-ready) für GitHub Pages (Minimal Mistakes):

```
- Dateiname: YYYY-MM-DD-powerplatformtip-<NNN>-<slug>.md
```

• slug: lowercase, a–z/0–9, hyphens only.

- Front Matter:
---
```
title: "#PowerPlatformTip <NNN> – '<short utility title>'"
```

date: YYYY-MM-DD
categories:
    - Article
    - PowerPlatformTip
tags:
    - PowerAutomate
    - PowerApps
    - Dataverse
    - Governance
    - PowerPlatformTip
excerpt: "<copy the 2–3 sentence summary>"
header:
overlay_color: "\#2dd4bf"
overlay_filter: "0.5"
toc: true
toc_sticky: true
---
- Body in dieser Reihenfolge (keine Fettschrift):


## 💡 Challenge

…

## ✅ Solution

…

## 🔧 How It's Done

1. …
🔸 …
2. …
🔸 …
3. …
🔸 …

## 🎉 Result

…

## 🌟 Key Advantages

🔸 …
🔸 …
🔸 …

## 🛠️ FAQ

Q1: …
A: …
Q2: …
A: …
Q3: …
A: …

Wenn YOUTUBE_ID vorhanden, füge GENAU am Ende hinzu:

## 🎥 Video Tutorial

{% include video id="<YOUTUBE_ID>" provider="youtube" %}

Stoppe und warte auf “OK”.

--- PHASE 3 · HTML NEWSLETTER (systeme.io · Deep Dive) ---
Ziel: eigenständige E-Mail (ohne Vorwissen), mobile-first, keine Video-Embeds.
Konventionen:

- Gesamtes HTML < ~80–100 KB (Gmail clipping).
- Tabellenlayout, zentraler 600px Container.
- Kritische Styles inline (Head-CSS klein halten).
- 1 CTA-Link/Button (mit UTM).

Gib EIN einziges vollständiges `<html>…</html>` aus mit folgender Struktur:

1) Subject lines (5 Varianten, ≤55 chars)
2) Preheader (1 line; als versteckter Preview-Text ganz oben einfügen)
3) TL;DR (2–3 Sätze: immediate value)
4) Why it matters (context + pain)
5) Deep Dive — 3–6 numbered steps
Tip / Common pitfall
6) 3 Use Cases (Citizen Developer focus) — when \& how to apply
7) Tooling \& Snippets (copy-ready)
8) Checklist (3–5 items)
9) Mini-FAQ (3 Q/As)
10) CTA (one link/button; add UTM)
11) P.S. personal note

Video-Regel im Newsletter:

- Wenn YOUTUBE_ID vorhanden → Text oder Button:
“Watch on YouTube: https://youtu.be/<YOUTUBE_ID>”.
- Niemals ein Video im E-Mail-HTML einbetten.

END.

I understand this comprehensive \#PowerPlatformTip orchestrator template perfectly. This is a well-structured system for creating consistent, multi-format Power Platform content that works across review tips, Jekyll markdown, and HTML newsletters.

### Template Structure Overview

The orchestrator defines four distinct phases with specific formatting rules:

**Phase 0 - Intake \& Validation**: Extracts working title, product focus, use case, constraints, target outcome, and YouTube URL from user input. Asks up to 5 targeted questions only when necessary.

**Phase 1 - Review Tip** (Flow A only): Creates the base tip format with fixed structure using icons in sequence: Title → Summary → 💡 Challenge → ✅ Solution → 🔧 How it's done → 🎉 Result → 🌟 Key Advantages → 🛠️ FAQ → Hashtags.

**Phase 2 - Jekyll Markdown**: Generates complete .md files for GitHub Pages with Minimal Mistakes front matter, proper file naming (YYYY-MM-DD-powerplatformtip-NNN-slug.md), and video inclusion only when valid YouTube ID exists.

**Phase 3 - HTML Newsletter**: Creates standalone email for systeme.io with mobile-first design, table layout, inline styles, and no video embeds (text links only).

### Key Rules Noted

- No bold formatting throughout
- YouTube videos only embedded in Jekyll, text links in newsletters
- Consistent icon usage and section ordering
- UTM tracking for newsletter CTAs
- Jekyll front matter with teal overlay (\#2dd4bf)

I'm ready to execute any of the recognized commands: "FLOW A:", "FLOW B:", "GITHUB:", or "NEWSLETTER:" followed by your content input.

