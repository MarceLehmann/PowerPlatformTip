---
title: "#PowerPlatformTip 108 – 'Double-Click Magic in PowerApps'"
date: 2024-04-05
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Marcel Lehmann
  - PowerApps
  - PowerPlatform
  - PowerPlatformTip
  - DoubleClick
  - UserExperience
  - Timer
  - Popup
excerpt: "Distinguish single and double clicks in PowerApps to trigger different functionalities, bringing desktop-like efficiency without clutter."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Detect single vs. double clicks on one Power Apps button using a click counter plus a 1-second timer to trigger different actions.

## 💡 Challenge
How can we utilize both single and double clicks on the same button in PowerApps to perform separate actions, reflecting the state of interaction more accurately?

## ✅ Solution
Implement a method that leverages a combination of a click counter and a timer to differentiate between single and double clicks, executing actions accordingly.

## 🔧 How It's Done
Here's how to do it:
1. Click Tracking  
   🔸 Increment `locPopUp` variable to count clicks.  
   🔸 Use in OnSelect:  
   powerapps
   UpdateContext({locPopUp: locPopUp + 1})
   
2. Timer Initiation  
   🔸 Start the timer by setting `locPopUpTimer` to true.  
   🔸 Use in OnSelect:  
   powerapps
   UpdateContext({locPopUpTimer: true});
   
3. Timer Configuration  
   🔸 Set the timer’s Duration to 1000 (milliseconds).  
   🔸 Enable AutoStart on the timer control.  
4. Action Determination  
   🔸 In the timer’s OnTimerEnd, check the `locPopUp` count.  
   🔸 Reset `locPopUpTimer` to false:  
   powerapps
   UpdateContext({locPopUpTimer: false})
   
5. Popup Visibility and Reset  
   🔸 Display popups based on `locPopUp` value when `locPopUpTimer` is false.  
   🔸 On closing the popup, reset `locPopUp` to 0:  
   powerapps
   UpdateContext({locPopUp: 0});
   

## 🎉 Result
This setup effectively differentiates between single and double clicks, allowing PowerApps to execute contextually relevant actions based on user interaction speed. It mimics traditional desktop application behavior, enhancing the user experience within PowerApps.

## 🌟 Key Advantages
🔸 Versatile Interactions: Enables complex user interactions within a simple UI framework.  
🔸 User Experience: Offers intuitive operational modes that users are familiar with from desktop environments.  
🔸 Efficient Design: Reduces the need for multiple buttons for different actions, keeping the UI clean and user-friendly.

---

## 🎥 Video Tutorial
{% include video id="T1iQMEw5V4s" provider="youtube" %}

---

## 🛠️ FAQ
**1. How does the method distinguish between a single and double click?**  
It uses a click counter (`locPopUp`) and a timer (`locPopUpTimer`). When the button is clicked, the counter increments and the timer starts. If a second click occurs before the timer ends, it’s treated as a double click; otherwise, it’s a single click action.

**2. Can I adjust the interval used to detect a double click?**  
Yes. You can modify the timer’s Duration property (e.g., set it to 500ms or 1000ms) to suit the expected speed of user interaction in your app.

**3. How can I apply this pattern for a double-click-only action?**  
Use a formula that compares the current time to the last click time (e.g., with `Now()` and `DateAdd`) and set a variable (like `locDobble`) to true when two clicks occur within the defined interval.

---