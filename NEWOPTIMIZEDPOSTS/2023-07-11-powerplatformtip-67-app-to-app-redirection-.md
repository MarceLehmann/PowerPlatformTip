---
title: "#PowerPlatformTip 67 – 'App-to-App Redirection'"
date: 2023-07-11
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

## 📝 TL;DR
Seamlessly redirect users from old to new Power Apps using the Launch function—improve user experience, manage migrations, and ensure smooth app transitions across environments.

## 💡 Challenge
💡 **The Challenge:** Managing multiple apps on different environments can be a daunting task.

## ✅ Solution
💡 **The Challenge:** Managing multiple apps on different environments can be a daunting task. You want to ensure a seamless user transition from an older app to a revamped one hosted elsewhere.
✅ **The Solution:** The 'Launch' function in Power Apps comes to your rescue! By using the 'Launch' function, you can create a redirection from the old app to the new one, ensuring a smooth transition for users.
🔧 **How It's Done:**
1️⃣ **Launch Function:** Use the 'Launch' function to create a redirection from the old app to the new one. This can be done in the OnStart property or an OnVisible event on a screen.
2️⃣ **User Communication:** Inform users about the change, emphasizing that they're in a new app with a fresh URL. Users can request this new URL via Teams.
🎉 **Result:** You've ensured a seamless transition for users to the new app version or environment, while maintaining the older apps.
**Key Advantages:**
1️⃣ **User Experience:** By ensuring a smooth transition, you enhance the user experience and minimize disruption.
2️⃣ **Efficiency:** This approach allows users to continue using the old link for a while, helping you avoid broken links in various locations.
3️⃣ **Control:** You maintain control over the transition process, allowing for a planned and organized shift to the new app.

## 🔧 How It's Done
1️⃣ **Launch Function:** Use the 'Launch' function to create a redirection from the old app to the new one. This can be done in the OnStart property or an OnVisible event on a screen.
2️⃣ **User Communication:** Inform users about the change, emphasizing that they're in a new app with a fresh URL. Users can request this new URL via Teams.

## 🎉 Result
You've ensured a seamless transition for users to the new app version or environment, while maintaining the older apps.
**Key Advantages:**
1️⃣ **User Experience:** By ensuring a smooth transition, you enhance the user experience and minimize disruption.
2️⃣ **Efficiency:** This approach allows users to continue using the old link for a while, helping you avoid broken links in various locations.
3️⃣ **Control:** You maintain control over the transition process, allowing for a planned and organized shift to the new app.

## 🌟 Key Advantages
🔸 Improved Efficiency: Faster development cycles through automation.
🔸 Better Consistency: Standardized approach across all projects.
🔸 Enhanced Reliability: Reduced risk of failure during execution.

## 🎥 Video Tutorial
{% include video id="noscript" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I trigger the redirection?**  
Use the `Launch` function in Power Apps and set it in the `OnStart` or `OnVisible` property with the new app URL.

**2. Can I still access the old app?**  
Yes. The redirection allows the old URL to continue working while users move to the new app.

**3. How should I inform users about the new URL?**  
Communicate via Teams or in-app notifications, providing the new link and guidance on the change.