---
title: "#PowerPlatformTip 114 – 'Send Approvals to External Recipients'"
date: 2024-05-17
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - Approvals
  - AdaptiveCards
  - ExternalApprovals
  - Outlook
  - PowerPlatformTip
excerpt: "Send Power Automate approval requests to external recipients using Adaptive Cards or email, enabling secure, flexible workflows beyond your organization."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Send Power Automate approvals to external recipients via 'Send email with options' or Adaptive Cards in Outlook.

## 💡 Challenge
The standard approval process in Power Automate doesn't support external recipients out of the box.

## ✅ Solution
Use the **Send email with options** action for a quick approach, or combine **Approvals + Adaptive Cards + Outlook** for a richer, interactive experience.

## 🔧 How It's Done

**Simple method**

🔸 Add the **Send email with options** action to your flow.

🔸 Define the options (e.g. "Approve", "Reject").

🔸 Send the email to the external recipients.

🔸 Process the response in your flow.

**Advanced method**

🔸 Start an approval process in your flow.

🔸 Create an Adaptive Card with approval options.

🔸 Send the card via the Outlook action to external recipients.

🔸 Process the response from the card in your flow.

🔸 Step-by-step walkthrough: [Approvals with Adaptive Cards in Outlook (Yash Agarwal)](https://powerplatformtip.com/Article/power-automate-tutorial-approvals-adaptive-cards-outlook-awesome-from-yash-agarwal/)

## 🎉 Result
External stakeholders can now take part in your approval processes — either by email response or interactively via an Adaptive Card in Outlook.

## 🌟 Key Advantages

🔸 Includes external stakeholders in approval processes.

🔸 Flexibility in designing the approval experience.

🔸 Better collaboration across organizational boundaries.

---

## 🎥 Video Tutorial
{% include video id="rQSWzLiPRec" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can I send approval requests to recipients outside my Microsoft 365 tenant?**
Yes. Using the **Send email with options** action or Adaptive Cards via Outlook, you can send to any valid external address.

**2. Are responses from the "Send email with options" action secure and trackable?**
Responses are tracked in your flow run history. However, they offer only basic text options and aren't managed in the Approvals center.

**3. When should I use the Adaptive Card method?**
Use the advanced method with Adaptive Cards when you need a richer, interactive experience in Outlook and want to track approvals within Microsoft 365.

---