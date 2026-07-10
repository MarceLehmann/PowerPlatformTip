---
title: "#PowerPlatformTip 89: 'Code View (Peek Code)'"
date: 2023-11-30
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Automate
  - Code View
  - Expressions
  - Debugging
  - Flow Logic
  - Troubleshooting
  - Productivity
excerpt: "Use Code View in Power Automate to inspect action expressions in a read-only format, gain insight, debug flows, and understand logic for more effective troubleshooting."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Use Code View (formerly Peek code) in Power Automate to inspect an action's underlying expressions in read-only form for faster debugging.

## 💡 Challenge
While working with Power Automate, you might come across situations where you want to understand or utilize expressions used in different actions more effectively. However, finding and understanding these expressions can sometimes be challenging.

## ✅ Solution
Use the Code View feature (formerly Peek code) in Power Automate to view the expressions used in actions in a read-only format, providing insight into the underlying logic of your flows.

## 🔧 How It's Done
Here's how to do it:
1. In your flow, find the action you are interested in.  
2. Click the three dots (…) in the top-right corner of the action to open its menu.  
3. From the menu, select “Peek code” (also labeled “Code view”).  
4. A window opens displaying the expressions and JSON used in that action in a read-only format.

## 🎉 Result
You gain insight into the expressions used in different actions in Power Automate, which aids understanding of flow logic and supports more effective debugging.

## 🌟 Key Advantages
🔸 Insight into expressions: Get a deeper understanding of the expressions used in different actions.  
🔸 Learning tool: Understand how actions work at the code level.  
🔸 Debugging: View and analyze expressions to troubleshoot flow issues.

## 🎥 Video Tutorial
{% include video id="3ksHSpyog-8" provider="youtube" %}

## 🛠️ FAQ
**1. What is the Code View feature?**

Code View (Peek code) shows the underlying JSON and expressions of a selected action in Power Automate in a read-only format.

**2. Can I edit expressions directly in Code View?**

No, Code View is strictly read-only. To modify expressions, use the action designer or the expression editor in the flow designer.

**3. How does Code View help with debugging?**

By exposing the exact expressions and property names, Code View allows you to troubleshoot and understand flow logic more effectively.
