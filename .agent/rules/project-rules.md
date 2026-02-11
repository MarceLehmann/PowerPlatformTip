---
trigger: always_on
description: Global rules for PowerPlatformTip generation
---

# PowerPlatformTip Rules

These rules must be followed for all content generation related to PowerPlatformTip.

## Formatting & Style
- **No Bold Text**: Do not use bold text in the tip content bodies.
- **Line Breaks**: Start a new line after every colon `:`.
- **Sentences**: Use short, clear sentences.
- **Sources**: No numbers/statistics without a verified source.
- **Language**: German (unless specified otherwise).

## Standard Structure & Icons
All tips must follow this sequence:
1.  **Title**
2.  **📝 TL;DR** (2–3 Sentence Summary)
3.  **💡 Challenge**
4.  **✅ Solution**
5.  **🔧 How it's done** (numbered list + `🔸` bullets for hints)
6.  **🎉 Result**
7.  **🌟 Key Advantages** (`🔸` bullets)
8.  **🎥 Video** (YouTube embed, if available)
9. **🛠️ FAQ** (3 Q/As)
10. **Hashtags**

## Channel Specifics

### Markdown (Jekyll / GitHub Pages)
- **Filename**: `YYYY-MM-DD-powerplatformtip-<NNN>-<slug>.md`
- **Front Matter**:
  ```yaml
  layout: single
  title: "#PowerPlatformTip <NNN> – '<short utility title>'"
  date: YYYY-MM-DD
  categories:
    - Article
    - PowerPlatformTip
  tags:
    - PowerAutomate # etc.
  excerpt: "Short SEO description (max 160 chars)"
  header:
    overlay_color: "#2dd4bf"
    overlay_filter: "0.5"
  toc: true
  toc_sticky: true
  ```
- **Video**: Include `{% include video id="<YOUTUBE_ID>" provider="youtube" %}` ONLY if a valid ID exists, at the very end.

### HTML Newsletter
- **Template**: Use the template at `.agent/templates/newsletter_template.html`.
- **Styling**: Strict adherence to the template's inline styles. Links must use `color:inherit; text-decoration:none;`.
- **No Embeds**: Email best practice - no video embeds. Use text link `Watch on YouTube: ...`.
- **Structure**:
  1.  Introduction
  2.  TL;DR (Section 1)
  3.  Article Link
  4.  Why This Matters (Section 2)
  5.  Recipe (Section 3 - Numbered List)
  6.  Real Examples (Section 4)
  7.  Expressions (Section 5)
  8.  Pro Tips (Section 6)
  9.  Footer (unsubscribe, social)