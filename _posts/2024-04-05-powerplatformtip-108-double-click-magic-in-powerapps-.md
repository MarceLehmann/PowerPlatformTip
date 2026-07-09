---
title: "#PowerPlatformTip 108 – 'Double-Click Magic in PowerApps'"
date: 2024-04-05
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerFx
  - DoubleClick
  - Timer
  - UserExperience
  - PowerPlatformTip
excerpt: "Distinguish single and double clicks in PowerApps to trigger different functionalities, bringing desktop-like efficiency without clutter."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Detect single vs. double clicks on one Power Apps button using a click counter plus a 1-second timer to trigger different actions.

## 💡 Challenge
How can you handle both single and double clicks on the same button in PowerApps to perform separate actions, reflecting the user's intent more accurately?

## ✅ Solution
Combine a **click counter** with a **timer** to tell single and double clicks apart, then run the matching action.

## 🔧 How It's Done

**1. Track clicks** with a counter variable.

🔸 In the button's `OnSelect`:

```powerapps
UpdateContext({locPopUp: locPopUp + 1})
```

**2. Start the timer** on the same click.

🔸 Also in `OnSelect`:

```powerapps
UpdateContext({locPopUpTimer: true})
```

**3. Configure the timer control.**

🔸 Set its `Duration` to `1000` (milliseconds) and enable `AutoStart`.

**4. Decide the action when the timer ends.**

🔸 In the timer's `OnTimerEnd`, check the `locPopUp` count, then reset the timer:

```powerapps
UpdateContext({locPopUpTimer: false})
```

**5. Show the popup and reset.**

🔸 Display popups based on `locPopUp` when `locPopUpTimer` is false. On closing, reset the counter:

```powerapps
UpdateContext({locPopUp: 0})
```

## 🎉 Result
The app cleanly distinguishes single from double clicks and runs contextually relevant actions based on interaction speed — mimicking familiar desktop behavior and improving the user experience.

## 🌟 Key Advantages

🔸 **Versatile interactions:** complex behavior within a simple UI.

🔸 **Familiar UX:** interaction patterns users know from the desktop.

🔸 **Efficient design:** fewer buttons for different actions, keeping the UI clean.

---

## 🎥 Video Tutorial
{% include video id="T1iQMEw5V4s" provider="youtube" %}

---

## 🛠️ FAQ
**1. How does the method distinguish between a single and double click?**
It uses a click counter (`locPopUp`) and a timer (`locPopUpTimer`). On each click the counter increments and the timer starts. If a second click arrives before the timer ends, it's a double click; otherwise it's a single click.

**2. Can I adjust the interval used to detect a double click?**
Yes. Change the timer's `Duration` (e.g. 500ms or 1000ms) to match the expected speed of interaction in your app.

**3. How can I apply this pattern for a double-click-only action?**
Compare the current time to the last click time (e.g. with `Now()` and `DateAdd`) and set a variable to true when two clicks occur within the defined interval.

---