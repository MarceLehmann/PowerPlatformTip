---
title: "#PowerPlatformTip 111: 'Adaptive Cards for Dynamic Approvals'"
date: 2024-04-24
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - AdaptiveCards
  - PowerAutomate
  - Approvals
  - Microsoft365
  - Workflow
  - PowerPlatformTip
excerpt: "Use Adaptive Cards and Office 365 User Search in Power Automate to dynamically select the next approver, enhancing approval process flexibility."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Replace static Power Automate approvals with Adaptive Cards + Office 365 User Search so each approver picks the next one dynamically.

## 💡 Challenge
Power Automate's standard approval action doesn't let an approver choose the *next* approver on the fly. For flexible, ad-hoc chains you need a way to pick the next person after each approval.

## ✅ Solution
Use Adaptive Cards with a Microsoft 365 user picker instead of the standard approval. Each approver selects who should approve next, so the chain builds itself dynamically.

## 🔧 How It's Done

🔸 Create a flow that sends an Adaptive Card to the first approver when a request is initiated.

🔸 Add an **Office 365 User Search** input to the card so the current approver can pick the next approver.

🔸 After the current approval, send the card automatically to the selected next approver.

🔸 Repeat until the chain is complete, logging each step for tracking and transparency.

🔸 At the end, generate a summary of who saw, approved, or forwarded the request.

## 🎉 Result
A versatile, dynamic approval process that goes beyond the standard approval action, letting users shape the approval flow to fit their needs.

## 🌟 Key Advantages

🔸 Unmatched flexibility in choosing approvers.

🔸 Enables sequential and conditional approvals.

🔸 Better oversight and transparency of the approval history.

🔸 Smooth user experience through Microsoft 365 integration.

---

## 🎥 Video Tutorial
{% include video id="KoTyWm7Qg4M" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I implement Office 365 User Search in Adaptive Cards?**
Add a people-picker input to the Adaptive Card JSON schema. It connects to Microsoft Entra ID and lets approvers search and select users dynamically.

**2. What happens if an approver doesn't respond to the Adaptive Card?**
Configure timeouts or parallel branches in your flow to handle non-responses, escalate to a fallback approver or send automatic reminders.

**3. Can I include conditional logic within the approval flow?**
Yes. Use conditional actions in Power Automate based on the approver's selection or other variables to build branching approval scenarios.

---