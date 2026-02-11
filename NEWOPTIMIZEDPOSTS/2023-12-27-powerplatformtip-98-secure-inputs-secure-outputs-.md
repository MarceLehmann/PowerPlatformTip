---
title: "#PowerPlatformTip 98 – 'Secure Inputs / Secure Outputs'"
date: 2023-12-27
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
excerpt: "Protect sensitive data in Power Automate by enabling Secure Inputs and Secure Outputs—mask confidential information in flow logs, enhance compliance, and secure workflows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Protect sensitive data in Power Automate by enabling Secure Inputs and Secure Outputs—mask confidential information in flow logs, enhance compliance, and secure workflows.

## 💡 Challenge
Managing complex workflows in Power Platform can be difficult without the right approach to Secure Inputs / Secure Outputs. Many developers find themselves struggling with efficiency and manual configuration.

## ✅ Solution
By implementing Secure Inputs / Secure Outputs, you can automate repetitive tasks and simplify your application logic. This feature provides a native way to handle data more effectively.

## 🔧 How It's Done
* Go to the action you want to secure in your Flow.
* Go to the action you want to secure in your Flow.
* In the new designer select 'Settings'.
* Toggle on 'Secure Inputs' and/or 'Secure Outputs' to mask the data in logs.
* Save your changes to ensure these settings are applied.
By enabling these features, your Flow's sensitive data, such as personal details or confidential information, will be hidden in run history. This means if someone is reviewing the Flow logs, they won't see the actual data that was processed, significantly reducing the risk of data leakage or unauthorized access.
🔸 **Enhanced Security**: Ensures sensitive data is not visible in Flow logs, protecting against unauthorized access. 
🔸 **Compliance Friendly**: Helps in maintaining compliance with data protection regulations by safeguarding personal and confidential information. 
🔸 **Peace of Mind**: Adds an extra layer of security to your automated processes, allowing you to focus on building efficient workflows without compromising data integrity.
Remember, while "Secure Inputs" and "Secure Outputs" are powerful, they are just one aspect of a comprehensive data security strategy. Always consider the full context of your data processing and adhere to best practices for maximum protection.

## 🎉 Result
Your workflows become more robust and easier to maintain. Implementing Secure Inputs / Secure Outputs reduces the time spent on manual adjustments and minimizes potential for errors.

## 🌟 Key Advantages
🔸 Improved Efficiency: Faster development cycles through automation.
🔸 Better Consistency: Standardized approach across all projects.
🔸 Enhanced Reliability: Reduced risk of failure during execution.

## 🎥 Video Tutorial
{% include video id="xEmk4Ka5SlE" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why should I use Secure Inputs and Secure Outputs?**  
They hide sensitive data in the Flow run history and logs, preventing unauthorized access to confidential information.

**2. Will enabling Secure Inputs/Outputs affect my Flow's performance?**  
It has minimal impact on execution speed; it only changes how data is logged, not how it’s processed.

**3. Can I toggle Secure Inputs and Secure Outputs individually?**  
Yes, you can enable Secure Inputs, Secure Outputs, or both for each action based on your security needs.