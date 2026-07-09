---
title: "#PowerPlatformTip 111 – 'Adaptive Cards for Dynamic Approvals'"
date: 2024-04-24
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Adaptive Cards
  - Power Automate
  - Approvals
  - Dynamic Approvals
  - Office 365
  - User Search
  - Workflow
excerpt: "Use Adaptive Cards and Office 365 User Search in Power Automate to dynamically select the next approver, enhancing approval process flexibility."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Replace static Power Automate approvals with Adaptive Cards + Office 365 User Search so each approver picks the next one dynamically.

## 💡 Challenge
In many workflows, Power Automate's standard approval function is limited as it doesn't allow for the dynamic selection of the next approver after an approval. Users are looking for a solution that makes it possible to manage approvals more flexibly, choosing the next approver individually after each approval.

## ✅ Solution
The solution is to use Adaptive Cards within Power Automate flows instead of standard approval mechanisms. By leveraging Adaptive Cards combined with the Office 365 User Search, users can dynamically select the next approver, significantly enhancing the flexibility of the process.

## 🔧 How It's Done
* Create a Power Automate Flow that sends an Adaptive Card to the first approver as soon as an approval request is initiated.

* Incorporate an Office 365 User Search field into the Adaptive Card, allowing the current approver to select the next approver.

* After approval by the current user, the Adaptive Card is automatically sent to the next approver based on the selection.

* Repeat this process until the approval chain is complete. Each step is logged for tracking and transparency.

* At the end of the process, a summary is generated showing who has seen, approved, or forwarded the approval request.

## 🎉 Result
A versatile and dynamic approval process that transcends the limitations of the standard approval function, allowing users to customize the approval flow according to their needs.

## 🌟 Key Advantages
🔸 Unmatched flexibility in choosing approvers.
🔸 Enables sequential and conditional approvals.
🔸 Improved oversight and transparency of the approval history.
🔸 Optimizes user experience through integration with Office 365.

## 🎥 Video Tutorial
{% include video id="KoTyWm7Qg4M" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I implement Office 365 User Search in Adaptive Cards?**  
You can add a people picker input in the Adaptive Card JSON schema, which connects to Azure AD and allows approvers to search and select users dynamically.

**2. What happens if an approver doesn’t respond to the Adaptive Card?**  
You can configure timeouts or parallel branches in your flow to handle non-responses, such as escalating to a fallback approver or sending reminders automatically.

**3. Can I include conditional logic within the approval flow?**  
Yes, use conditional actions in Power Automate based on the approver’s selection or other variables, enabling complex approval scenarios and branching logic.

---