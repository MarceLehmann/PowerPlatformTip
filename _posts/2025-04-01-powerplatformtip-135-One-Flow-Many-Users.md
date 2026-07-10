---
title: "#PowerPlatformTip 135: 'One Flow, Many Users'"
date: 2025-04-01
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - AdaptiveCards
  - Flow
  - Automation
  - UserContext
  - PowerPlatformTip
excerpt: "Use Power Apps and Adaptive Cards to let everyone in your company trigger flows in their own context, without Outlook permission chaos or flow duplication."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Make one Power App the trigger hub for your shared flows and send Adaptive Cards that link to it, every user runs the flow in their own context, with no per-user permissions or duplicate flows.

## 💡 Challenge
You've built an awesome flow, but now everyone should use it. The problem: Outlook-based flows need permission setups or even a duplicate per user. That's messy, slow, and hard to maintain.

## ✅ Solution
Make one Power App the trigger hub for your shared flows, then send Adaptive Cards (e.g. every morning) with a link to the app. Users click the card and trigger the flow in **their own user context**, no extra permissions needed.

## 🔧 How It's Done

**1. Create a Power App**

🔸 Add a simple button or menu to trigger your flow(s).

**2. Build a scheduled flow**

🔸 Use a recurrence trigger to send an Adaptive Card via Teams or Outlook at 7:00 AM.

**3. Link the Power App**

🔸 Include a deep link or app URL inside the Adaptive Card.

**4. User clicks = flow starts**

🔸 The flow runs in the context of the signed-in user, not the maker.

**5. (Optional) Add guardrails**

🔸 Add confirmation screens or multiple flow triggers inside the app.

## 🎉 Result
You've got one centralized setup, and everyone can use it without breaking permissions or duplicating logic. Each employee triggers their flow when needed, all clean and compliant.

## 🌟 Key Advantages

🔸 One flow, multiple users, clean and efficient

🔸 Runs in the secure context of the signed-in user

🔸 Avoids Outlook or shared-mailbox headaches

🔸 Centralized but flexible execution

🔸 Easily extendable with more flows

---

## 🛠️ FAQ

**Q1: Can I still use this if I don't send Adaptive Cards?**

Yes! You can share the Power App through Teams, SharePoint, or email, the Adaptive Card just makes it smoother.

**Q2: What if the user needs to confirm something first?**

Build a confirmation screen into the app, you have full control over the experience.

**Q3: Can I trigger more than one flow?**

Absolutely, add multiple buttons or logic in the app to handle different scenarios.

## 🔗 Related Tips
- [#PowerPlatformTip 111: Adaptive Cards for Dynamic Approvals](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-111-adaptive-cards-for-dynamic-approvals/), build richer, interactive Adaptive Cards for your triggers.
- [#PowerPlatformTip 68: Power Apps and Power Apps for Teams](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-68-utilize-the-best-of-both-worlds-power-apps-and-power-apps-4-teams/), choose the best home for your trigger-hub app.
