---
title: "#PowerPlatformTip 142 – Automate Outlook Categories"
date: 2025-08-26
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - Outlook
  - MicrosoftGraph
  - Automation
  - Productivity
  - PowerPlatformTip
excerpt: "Learn how to automatically set categories for Outlook meetings using a standard, non-premium Power Automate action. Save time and stay organized with this simple tip."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Auto-categorize Outlook meetings with a standard Power Automate flow that PATCHes events via the Office 365 Outlook 'Send an HTTP request' action – no premium.

Tired of manually categorizing your Outlook meetings? This tip shows how to use Power Automate to set categories for calendar events automatically — keeping you organized with almost no effort.

## 💡 Challenge
How do you make sure all important meetings in your Outlook calendar are consistently categorized without doing it by hand? Adding categories manually takes time and is easy to forget on a busy schedule, which leaves your calendar disorganized.

## ✅ Solution
Use a Power Automate flow with the standard Office 365 Outlook connector to find and update your calendar events automatically. Trigger it on a schedule or with a button; it loops through your meetings and applies a category — keeping everything organized without you thinking about it.

## 🔧 How It's Done

**1. Add a trigger**

🔸 Start the flow with a manual button or a schedule.

**2. Define the category**

🔸 Use a Compose action for the new category (e.g. "NewCategory").

**3. Get the events**

🔸 Add "Get calendar view of events (V3)" to fetch meetings within a date range.

**4. Loop the events**

🔸 Insert a "For each" loop to process every event found.

**5. Send the PATCH request**

🔸 Inside the loop, add "Send an HTTP request" (Office 365 Outlook connector), set the Method to `PATCH` and the URI to:

```
https://graph.microsoft.com/v1.0/me/events/@{items('For_each')?['id']}
```

🔸 In the Body, set the category:

```json
{
  "categories": @{outputs('Compose_-_New_Category')}
}
```

**6. Save and test**

🔸 Run the flow and watch your meeting categories update automatically.

## 🎉 Result
Your flow now runs in the background, applying your category to all relevant meetings. Your calendar is instantly more organized and easier to filter — you can find specific types of meetings with a click, all without a premium license.

## 🌟 Key Advantages

🔸 **Accessibility:** uses only standard connectors — no premium Power Automate license required.

🔸 **Time-saving:** frees you from manually updating calendar entries.

🔸 **Powerful customization:** the Graph API through this action allows more advanced updates than standard actions permit.

---

## 🎥 Video Tutorial
{% include video id="2Xj99XQK-5A" provider="youtube" %}

---

## 🛠️ FAQ
**1. Is this really not a premium feature?**
Correct. While the general "HTTP" connector is premium, the "Send an HTTP request" action inside the Office 365 Outlook connector is included with standard M365 licenses and is designed to call the Microsoft Graph API for Outlook.

**2. How can I add a category without removing existing ones?**
Before your PATCH, add another "Send an HTTP request" (Outlook connector) with the GET method to the same URI to read the event's current categories. Then combine the existing categories with your new one and use that result in the PATCH request.

**3. Can I update other details besides the category?**
Yes. The `PATCH` method can update many event properties — for example, change the 'showAs' status (Free to Busy), modify the body, or update the subject by including those fields in the JSON body.

---