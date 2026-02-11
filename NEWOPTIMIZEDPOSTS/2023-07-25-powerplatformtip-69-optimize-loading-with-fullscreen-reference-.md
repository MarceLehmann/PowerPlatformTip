---
title: "#PowerPlatformTip 69 – 'Optimize Loading with Fullscreen Reference'"
date: 2023-07-25
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
excerpt: "Speed up Power Apps loading by using App.width and App.height for fullscreen dimensions—improve performance, user experience, and deliver faster app startup times."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Speed up Power Apps loading by using App.width and App.height for fullscreen dimensions—improve performance, user experience, and deliver faster app startup times.

## 💡 Challenge
If you don't want to miss out on any future #PowerPlatformTip posts, be sure to subscribe to my newsletter – you'll be the first to know whenever I publish a new tip!
								Type your email…							
								Subscribe							
💡 **The Challenge:** In a world where every second counts, speeding up your Power Apps loading process can be a real game-changer.

## ✅ Solution
If you don't want to miss out on any future #PowerPlatformTip posts, be sure to subscribe to my newsletter – you'll be the first to know whenever I publish a new tip!
								Type your email…							
								Subscribe							
💡 **The Challenge:** In a world where every second counts, speeding up your Power Apps loading process can be a real game-changer. You're looking for ways to make your Power Apps load faster.
✅ **The Solution:** When building your Power Apps, make sure to reference App.width and App.height for fullscreen dimensions rather than using Parent.width and Parent.height. Why? Because 'App' loads immediately, whereas 'Parent' follows a sequential loading process. By referencing 'App', you're ensuring that your app's dimensions are available right away, leading to a faster loading time.
🔧 **How It's Done:**
1️⃣ **Use 'App':** Instead of 'Parent', use 'App' to reference dimensions. This ensures immediate loading and faster app performance.
2️⃣ **Optimize Loading Time:** By ensuring your app's dimensions are available right away, you significantly reduce your Power App's loading time.
🎉 **Result:** You've significantly reduced your Power App's loading time, delivering a seamless and efficient user experience!
**Key Advantages:**
1️⃣ **Performance Boost:** By using 'App' to reference dimensions, you can improve your app's performance and reduce loading time.
2️⃣ **User Experience:** Faster loading times lead to a smoother and more efficient user experience.
3️⃣ **Efficiency:** This simple change can make a big difference in your app's efficiency, saving valuable time for your users.

## 🔧 How It's Done
1️⃣ **Use 'App':** Instead of 'Parent', use 'App' to reference dimensions. This ensures immediate loading and faster app performance.
2️⃣ **Optimize Loading Time:** By ensuring your app's dimensions are available right away, you significantly reduce your Power App's loading time.

## 🎉 Result
You've significantly reduced your Power App's loading time, delivering a seamless and efficient user experience!
**Key Advantages:**
1️⃣ **Performance Boost:** By using 'App' to reference dimensions, you can improve your app's performance and reduce loading time.
2️⃣ **User Experience:** Faster loading times lead to a smoother and more efficient user experience.
3️⃣ **Efficiency:** This simple change can make a big difference in your app's efficiency, saving valuable time for your users.

## 🌟 Key Advantages
🔸 Improved Efficiency: Faster development cycles through automation.
🔸 Better Consistency: Standardized approach across all projects.
🔸 Enhanced Reliability: Reduced risk of failure during execution.

## 🎥 Video Tutorial
{% include video id="noscript" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why should I use App.width and App.height instead of Parent.width and Parent.height?**  
Because 'App' loads immediately, making dimensions available faster, whereas 'Parent' relies on a sequential loading process.

**2. Will this change affect my existing app layouts?**  
No, switching the reference to 'App' only changes how dimensions are retrieved; your layout remains the same but loads faster.

**3. Can I use this optimization for other components in Power Apps?**  
Yes, referencing 'App' properties can be applied whenever you need immediate global app context to improve performance.