---
title: "#PowerPlatformTip 126 – 'User Context for Automated Tasks'"
date: 2024-10-08
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Power Automate
  - Power Platform
  - Outlook
  - Teams
  - Automation
  - Scheduled Flow
  - User Context
excerpt: "Automate user-specific tasks like setting OOO replies and Teams notifications centrally while allowing users to customize messages before scheduled flows run."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Run user-context tasks like Outlook auto-replies from one central Power App + scheduled flow instead of per-user flows.

## 💡 Challenge
You want to automate tasks like setting an out-of-office reply in Outlook or sending Teams notifications, but these need to run in the user’s own context. At the same time, users should be able to customize information—such as modifying the auto-reply text—before the flow is triggered. Ideally, this process runs on a schedule and uses a single centrally managed flow rather than one per user.

## ✅ Solution
Create a Power App that collects additional user input (like an out-of-office message) and passes it to a Power Automate flow, which runs the task in the user’s context. You can even send the link to this Power App on a schedule—such as every morning—asking users whether they want to set their auto-reply for the day.

## 🔧 How It's Done
Here's how to do it:
1. Build a Power App that prompts the user for details like the auto-reply text or a Teams message.  
   🔸 Collect user-specific inputs.  
   🔸 Use form controls to capture text and options.  
2. Connect the Power App to a Power Automate flow that performs the action in the user’s context.  
   🔸 Pass the user’s authentication context to the flow.  
   🔸 Trigger actions like setting the auto-reply or sending notifications.  
3. Set up a scheduled flow to send a link to the Power App.  
   🔸 Configure recurrence (e.g., every morning).  
   🔸 Use email or Teams message with the app link.  
4. Pre-fill the app with existing user details and have users submit to trigger the flow.  
   🔸 Retrieve previous settings or defaults.  
   🔸 Use the OnStart property to auto-populate fields.

## 🎉 Result
Each user receives a scheduled message with a link to the Power App. They can decide whether to set their auto-reply or send a message, adjust the text or other settings, and then click “Submit.” The flow runs under their credentials, completing the task in their context. The process is centrally managed yet personalized for each user.

## 🌟 Key Advantages
🔸 Personalized automation running in the user’s context  
🔸 Reduced admin overhead by centrally managing the flow  
🔸 No need to create and manage individual flows for every user  

---

## 🎥 Video Tutorial
{% include video id="QYrqT-K3E58" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I ensure the flow runs with the user’s permissions?**  
Use the Power Apps connector to pass the authenticated user’s context to Power Automate, so all actions execute under their credentials.

**2. Can this be fully automated without user input?**  
Yes. You can trigger the flow via the OnStart property of the Power App to run automatically when the app opens, but having users confirm maintains GDPR compliance and transparency.

**3. How do I pre-fill user details in the Power App?**  
Use the OnStart property along with Office 365 Users or other connectors to retrieve the user’s profile and default values, populating form fields before display.
