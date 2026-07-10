---
title: "#PowerPlatformTip 126 – 'User Context for Automated Tasks'"
date: 2024-10-08
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - Outlook
  - Teams
  - ScheduledFlow
  - UserContext
  - PowerPlatformTip
excerpt: "Automate user-specific tasks like setting OOO replies and Teams notifications centrally while allowing users to customize messages before scheduled flows run."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Run user-context tasks like Outlook auto-replies from one central Power App + scheduled flow instead of per-user flows.

## 💡 Challenge
You want to automate tasks like setting an out-of-office reply in Outlook or sending Teams notifications, but these must run in each user's own context. Users should also be able to customize the details — such as the auto-reply text — before the flow runs. Ideally the whole thing runs on a schedule from a single, centrally managed flow rather than one flow per user.

## ✅ Solution
Build a Power App that collects the extra user input (like an out-of-office message) and passes it to a Power Automate flow that runs the task in the user's context. You can even send the app link on a schedule — e.g. every morning — asking users whether they want to set their auto-reply for the day.

## 🔧 How It's Done

**1. Build a Power App for user input**

🔸 Collect user-specific inputs like the auto-reply text or a Teams message.

🔸 Use form controls to capture text and options.

**2. Connect it to a flow that runs in the user's context**

🔸 Pass the user's authentication context to the flow.

🔸 Trigger actions like setting the auto-reply or sending notifications.

**3. Schedule a reminder to the app**

🔸 Configure recurrence (e.g. every morning).

🔸 Send an email or Teams message with the app link.

**4. Pre-fill and submit**

🔸 Retrieve previous settings or defaults with the OnStart property.

🔸 Users review, adjust and submit to trigger the flow.

## 🎉 Result
Each user gets a scheduled message with a link to the Power App. They decide whether to set their auto-reply or send a message, adjust the text or other settings, and click "Submit." The flow runs under their credentials, completing the task in their context — centrally managed, yet personalized per user.

## 🌟 Key Advantages

🔸 Personalized automation running in the user's context

🔸 Reduced admin overhead through one centrally managed flow

🔸 No need to create and manage individual flows for every user

---

## 🎥 Video Tutorial
{% include video id="QYrqT-K3E58" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I ensure the flow runs with the user's permissions?**
Use the Power Apps connector to pass the authenticated user's context to Power Automate, so all actions execute under their credentials.

**2. Can this be fully automated without user input?**
Yes. You can trigger the flow via the OnStart property of the Power App to run automatically when the app opens, but having users confirm maintains transparency and GDPR compliance.

**3. How do I pre-fill user details in the Power App?**
Use the OnStart property together with Office 365 Users or other connectors to retrieve the user's profile and defaults, populating form fields before display.

## 🔗 Related Tips
- [#PowerPlatformTip 135 – One Flow, Many Users](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-135-One-Flow-Many-Users/) — the central-app pattern for user-context flows.
- [#PowerPlatformTip 127 – Special User-Informations in PowerApps Studio](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-127-special-user-informations-in-powerapps-studio/) — handle user identity in dev vs. production.
