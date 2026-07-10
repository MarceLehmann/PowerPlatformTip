---
title: "#PowerPlatformTip 69: 'Optimize Loading with Fullscreen Reference'"
date: 2023-07-25
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Fullscreen
  - App Loading
  - Performance
  - Canvas Apps
  - App.width
  - App.height
  - Optimization
excerpt: "Speed up Power Apps loading by using App.width and App.height for fullscreen dimensions, improve performance, user experience, and deliver faster app startup times."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Reference `App.Width`/`App.Height` instead of `Parent.Width`/`Parent.Height` for fullscreen layouts so dimensions are available instantly and apps load faster.

## 💡 Challenge

In a world where every second counts, speeding up your Power Apps loading process can be a real game-changer. You're looking for ways to make your apps load faster.

## ✅ Solution

When building fullscreen layouts, reference `App.Width` and `App.Height` instead of `Parent.Width` and `Parent.Height`. `App` loads immediately, whereas `Parent` follows a sequential loading process, so referencing `App` makes your dimensions available right away and speeds up loading.

## 🔧 How It's Done

**1. Use App instead of Parent**

🔸 Replace `Parent.Width` / `Parent.Height` with `App.Width` / `App.Height` for fullscreen dimensions.

🔸 This ensures the dimensions are available immediately on load.

**2. Apply it to your root containers**

🔸 Set the Width/Height of your top-level screen containers to the `App` references.

🔸 Child controls sized relative to those containers benefit automatically.

## 🎉 Result

You've reduced your Power App's loading time, delivering a smoother and more efficient user experience, with the same layout, just faster.

## 🌟 Key Advantages

🔸 Performance Boost: `App` dimensions are available immediately

🔸 Better User Experience: Faster, smoother startup

🔸 Simple Change: A tiny formula tweak with a real impact

## 🛠️ FAQ

**Q: Why should I use App.Width and App.Height instead of Parent.Width and Parent.Height?**

Because `App` loads immediately, making dimensions available faster, whereas `Parent` relies on a sequential loading process.

**Q: Will this change affect my existing app layouts?**

No. Switching the reference to `App` only changes how dimensions are retrieved; your layout stays the same but loads faster.

**Q: Can I use this optimization for other components in Power Apps?**

Yes. Referencing `App` properties helps whenever you need immediate global app context to improve performance.
