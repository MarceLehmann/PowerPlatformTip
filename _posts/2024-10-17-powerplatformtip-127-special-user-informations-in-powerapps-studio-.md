---

title: "#PowerPlatformTip 127 – 'Special User-Informations in PowerApps Studio'"
seo_title: "#PowerPlatformTip 127 – 'Special User-Informations in"
date: 2024-10-17
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerPlatformTip
  - PowerPlatform
  - TestEnvironment
  - StudioMode
  - Email
  - UserContext
  - Development
  - Production
  - AppSecurity
  - Environment Switching
  - Security
excerpt: "Automatically switch between test and production user emails in PowerApps Studio using environment detection for secure, automated app testing and deployment."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true

---

## 📝 TL;DR
Automatically switch between test and production user emails in PowerApps Studio using environment detection for secure, automated app testing and deployment.

## 💡 Challenge
While developing apps in Power Apps Studio mode, we often use test values like a test email address.

## ✅ Solution
You can implement a check to see if your app is running in Studio Mode. If it is, use a test email account for development. When the app is in the Production-Mode, it will automatically switch to using the user's email address.

## 🔧 How It's Done
Use this formula to detect if your app is in Studio Mode and switch email addresses accordingly:
fxIsStudioMode = StartsWith(Host.Version, "PowerApps-Studio");
fxUserEmail = If(
fxIsStudioMode,
"testaccount@company.com",
User().Email
);
This way, you'll use a test email during development and the correct user email in production without manual changes.

## 🎉 Result
No more accidentally deploying apps with hardcoded test emails! This approach makes the switch seamless and automatic.

## 🌟 Key Advantages
🔸 Prevents accidental deployment of test data
🔸 Saves time by automating email assignment
🔸 Enhances app security and consistency
Special thanks to [Matthew Devaney](https://www.linkedin.com/in/matthew-devaney) for sharing this fantastic PowerApps tip!

## 🎥 Video Tutorial
{% include video id="640i6HAngNU" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I determine if my app is in Studio Mode?**  
Use the StartsWith function on Host.Version to check for "PowerApps-Studio".

**2. Can I apply this pattern to other test values?**  
Yes, you can use similar logic to switch between development and production values for any parameter.

**3. Where should I place these formulas in my app?**  
Include them in the App.OnStart property so that the variables are set when the app initializes.