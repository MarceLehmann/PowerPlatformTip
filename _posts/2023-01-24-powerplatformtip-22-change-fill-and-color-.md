---
title: "#PowerPlatformTip 22 – 'Change Fill & Color'"
date: 2023-01-24
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerapps
  - canvas apps
  - themes
  - ui customization
  - color
excerpt: "Change fill and color across a PowerApps Canvas App by centralizing colors in a theme variable and using the formula editor's Find & Replace."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge
Changing the colors and fill of a Canvas App when using the default template can be cumbersome, as there is no straightforward UI for overriding the theme, and colors are often hardcoded across many controls.

## ✅ Solution
Centralize your colors in a theme variable and reference it everywhere, so a single change updates the whole app. For values that are already hardcoded, use the formula editor's built-in Find & Replace.

## 🔧 How It's Done
Here's how to do it:

1. Use the built-in Theme settings.
   🔸 Go to **App > Theme** and pick a predefined theme or customize one.
   🔸 Adjust primary, secondary, and accent colors directly in the theme editor.

2. Centralize colors in `App.OnStart`.
   🔸 Define your palette once as a record:

   ```
   Set(
       varTheme,
       {
           Primary: ColorValue("#2dd4bf"),
           Accent:  ColorValue("#0f766e"),
           Text:    ColorValue("#1f2937")
       }
   )
   ```

   🔸 Reference `varTheme.Primary` in your controls instead of hardcoding colors – changing one line updates the whole app.

3. Replace existing hardcoded colors.
   🔸 Use the formula editor's **Find & Replace** to swap hardcoded color values or `RGBA(...)` calls with your `varTheme` references.

> ℹ️ Note: Power Fx does not have a `ReplaceAll` function. For replacing text inside a string you would use `Substitute(text, old, new)` (all matches) or `Replace(text, start, count, new)` (by position) – but for swapping colors across controls, the theme variable plus Find & Replace approach above is the reliable way.

## 🎉 Result
You can update the color scheme across all screens and controls in your app from a single place, ensuring a consistent and branded UI without manual per-control edits.

## 🌟 Key Advantages
🔸 Fast, centralized color updates across the entire app.

🔸 No need to rebuild or apply a separate custom template.

🔸 Easily maintain consistency when adding new controls or screens.

---

## 🛠️ FAQ
**1. Is there a `ReplaceAll` function to swap all colors at once?**

No. Power Fx offers `Substitute` and `Replace` for text, but not a global color swap. Centralize colors in a variable (e.g. `varTheme`) and reference it everywhere so one change updates the app.

**2. Can I apply custom themes to existing apps without losing my current design?**

Yes, but test the theme changes carefully as some custom formatting may be overridden by the new theme settings.

**3. Can I save my palette for use in other apps?**

Yes – keep your `App.OnStart` theme record in a shared component or snippet and reuse it across Canvas Apps to ensure brand consistency.

---

## 🎥 Video Tutorial
{% include video id="5P722KclIsk" provider="youtube" %}
