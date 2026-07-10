---
title: "#PowerPlatformTip 127 – 'Special User-Informations in PowerApps Studio'"
seo_title: "#PowerPlatformTip 127 – Special User-Informations in PowerApps Studio"
date: 2024-10-17
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerFx
  - StudioMode
  - UserContext
  - AppSecurity
  - PowerPlatformTip
excerpt: "Automatically switch between test and production user emails in PowerApps Studio using environment detection for secure, automated app testing and deployment."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Auto-switch to a test email in Power Apps Studio and the real `User().Email` in production via `StartsWith(Host.Version, "PowerApps-Studio")`.

## 💡 Challenge
While developing apps in Power Apps Studio, you often want to use test values — like a test email address — without risking that they end up in production.

## ✅ Solution
Check whether the app is running in Studio mode. If it is, use a test email for development; in production the app automatically switches to the real user's email address.

## 🔧 How It's Done

Use this formula to detect Studio mode and switch email addresses accordingly:

```powerfx
fxIsStudioMode = StartsWith(Host.Version, "PowerApps-Studio");
fxUserEmail = If(
    fxIsStudioMode,
    "testaccount@company.com",
    User().Email
);
```

🔸 Place these in the **App.OnStart** property so the variables are set when the app initializes.

🔸 You get the test email during development and the correct user email in production — with no manual changes.

## 🎉 Result
No more accidentally shipping apps with hardcoded test emails — the switch is seamless and automatic.

## 🌟 Key Advantages

🔸 Prevents accidental deployment of test data

🔸 Saves time by automating email assignment

🔸 Enhances app security and consistency

Special thanks to [Matthew Devaney](https://www.linkedin.com/in/matthew-devaney) for sharing this fantastic Power Apps tip!

---

## 🎥 Video Tutorial
{% include video id="640i6HAngNU" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I determine if my app is in Studio Mode?**
Use the `StartsWith` function on `Host.Version` to check for "PowerApps-Studio".

**2. Can I apply this pattern to other test values?**
Yes — use the same logic to switch between development and production values for any parameter.

**3. Where should I place these formulas in my app?**
Put them in the App.OnStart property so the variables are set when the app initializes.

## 🔗 Related Tips
- [#PowerPlatformTip 126 – User Context for Automated Tasks](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-126-user-context-for-automated-tasks/) — run tasks in each user's own context.
- [#PowerPlatformTip 73 – Quick Switch to Maker Mode](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-73-quick-switch-to-maker-mode/) — speed up your Studio workflow.
