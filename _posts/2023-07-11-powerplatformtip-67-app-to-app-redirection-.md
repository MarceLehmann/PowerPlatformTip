---
title: "#PowerPlatformTip 67 – 'App-to-App Redirection'"
date: 2023-07-11
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - App Redirection
  - Launch Function
  - User Experience
  - Migration
  - App Transition
  - Power Platform
excerpt: "Seamlessly redirect users from old to new Power Apps using the Launch function—improve user experience, manage migrations, and ensure smooth app transitions across environments."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Put a `Launch` to the new app's URL in the old app's `OnStart`/`OnVisible` to auto-redirect users while the old link keeps working.

## 💡 Challenge

Managing multiple apps across different environments can be a daunting task. When you move users from an older app to a revamped one hosted elsewhere, you want the transition to feel seamless.

## ✅ Solution

The `Launch` function in Power Apps comes to the rescue. Use it to redirect users automatically from the old app to the new one, ensuring a smooth transition while the old link keeps working.

## 🔧 How It's Done

**1. Add the redirection**

🔸 In the old app, use the `Launch` function pointing to the new app's URL.

🔸 Place it in the `OnStart` property or in an `OnVisible` event on the first screen.

**2. Communicate the change**

🔸 Inform users they're now in a new app with a fresh URL.

🔸 Let them request or bookmark the new URL (for example via Teams).

## 🎉 Result

You've ensured a seamless transition for users to the new app version or environment, while the older app links keep working during the changeover.

## 🌟 Key Advantages

🔸 User Experience: A smooth transition minimizes disruption

🔸 Efficiency: The old link keeps working, avoiding broken links elsewhere

🔸 Control: You manage a planned, organized shift to the new app

## 🛠️ FAQ

**Q: How do I trigger the redirection?**

Use the `Launch` function in Power Apps and set it in the `OnStart` or `OnVisible` property with the new app URL.

**Q: Can I still access the old app?**

Yes. The redirection allows the old URL to continue working while users move to the new app.

**Q: How should I inform users about the new URL?**

Communicate via Teams or in-app notifications, providing the new link and guidance on the change.
