---
title: "#PowerPlatformTip 98: 'Secure Inputs / Secure Outputs'"
date: 2023-12-27
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Automate
  - Secure Inputs
  - Secure Outputs
  - Data Security
  - Compliance
  - Workflow Security
  - Flow Logs
excerpt: "Protect sensitive data in Power Automate by enabling Secure Inputs and Secure Outputs, mask confidential information in flow logs, enhance compliance, and secure workflows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Toggle Secure Inputs and Secure Outputs in an action's settings to mask sensitive data in Power Automate run history and logs.

## 💡 Challenge
By default, the data processed by an action, passwords, tokens, or personal details, appears in plain text in the flow's run history. Anyone who can open the run can see this confidential information.

## ✅ Solution
Enable **Secure Inputs** and/or **Secure Outputs** on the relevant action. This masks the action's data in the run history so it is no longer visible to anyone reviewing the logs.

## 🔧 How It's Done
Here's how to do it:
1. Open the action you want to secure in your flow.  
2. Select **Settings** (in the new designer, the settings pane of the action).  
3. Toggle on **Secure Inputs** and/or **Secure Outputs** to mask the data in logs.  
4. Save your changes so the settings are applied.

## 🎉 Result
Your flow's sensitive data is hidden in the run history. If someone reviews the flow logs, they won't see the actual data that was processed, significantly reducing the risk of data leakage or unauthorized access.

⚠️ **Important Note:** Secure Inputs and Secure Outputs are one part of a broader data-security strategy. Always consider the full context of your data processing and follow best practices for maximum protection.

## 🌟 Key Advantages
🔸 **Enhanced Security:** Sensitive data is not visible in flow logs, protecting against unauthorized access.

🔸 **Compliance Friendly:** Helps maintain compliance with data-protection regulations by safeguarding personal and confidential information.

🔸 **Peace of Mind:** Adds an extra layer of security so you can focus on building efficient workflows without compromising data integrity.

## 🎥 Video Tutorial
{% include video id="xEmk4Ka5SlE" provider="youtube" %}

## 🛠️ FAQ
**1. Why should I use Secure Inputs and Secure Outputs?**

They hide sensitive data in the flow run history and logs, preventing unauthorized access to confidential information.

**2. Will enabling Secure Inputs/Outputs affect my flow's performance?**

It has minimal impact on execution speed; it only changes how data is logged, not how it's processed.

**3. Can I toggle Secure Inputs and Secure Outputs individually?**

Yes, you can enable Secure Inputs, Secure Outputs, or both for each action based on your security needs.
