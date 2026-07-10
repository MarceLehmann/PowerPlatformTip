---
title: "#PowerPlatformTip 109 – 'Use TimeOut'"
seo_title: "Power Automate Timeout: Extend Action Limits"
date: 2024-04-11
last_modified_at: 2026-07-10
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - Timeout
  - Approval
  - ErrorHandling
  - LongRunningTasks
  - PowerPlatformTip
excerpt: "Extend action timeouts and add error handling to ensure long-running Power Automate tasks complete without disruption."
description: "Long approvals timing out in Power Automate? Extend action timeouts with ISO 8601 durations (P2W, P1D) and add run-after error handling so flows never fail."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
faq:
  - question: "How do I specify custom timeout values in Power Automate?"
    answer: "Use ISO 8601 duration format (e.g. P2W, P1D, PT2H, PT30M, PT45S) in the Timeout field of the action's settings."
  - question: "Will my flow still fail if an action times out?"
    answer: "If you don't configure error handling, a timeout fails the run. Use Configure run after to catch timeouts and continue."
  - question: "Can I use timeouts with all actions in Power Automate?"
    answer: "Most built-in actions allow timeout configuration. For unsupported actions, wrap them in scopes or alternative logic."
howto:
  name: "Extend action timeouts in Power Automate"
  steps:
    - name: "Raise the action's Timeout"
      text: "In the settings of your approval (or any long-running action), set Timeout to an ISO 8601 duration that covers the expected delay (e.g. P2W = two weeks, P1D = one day, PT2H = two hours, PT30M = 30 minutes, PT45S = 45 seconds)."
    - name: "Add error handling"
      text: "Use Configure run after to define what happens if the action times out — e.g. start an alternative branch, send a notification, or kick off a new approval."
    - name: "Test and refine"
      text: "Run the flow under different conditions to fine-tune the timeout and the run-after logic."
---

> **TL;DR:** Raise an action's Timeout (ISO 8601, e.g. `P2W`) and add 'Configure run after' handling so long approvals finish without failing the flow.

## 💡 Challenge
Approvals and other long-running tasks can take longer than an action's default timeout, risking interruptions and unintended cancellations.

## ✅ Solution
Raise the timeout on the specific action so it has room to finish, and add error handling so the flow continues gracefully even if a timeout does occur.

## 🔧 How It's Done

**1. Raise the action's Timeout.**

🔸 In the settings of your approval (or any long-running action), set **Timeout** to an ISO 8601 duration that covers the expected delay:

🔸 `P2W` = two weeks · `P1D` = one day · `PT2H` = two hours · `PT30M` = 30 minutes · `PT45S` = 45 seconds

**2. Add error handling.**

🔸 Use **Configure run after** to define what happens if the action times out — e.g. start an alternative branch, send a notification, or kick off a new approval.

**3. Test and refine.**

🔸 Run the flow under different conditions to fine-tune the timeout and the run-after logic.

## 🎉 Result
Your flows stay operational and adaptable, handling long-running tasks without falling victim to unnecessary timeouts or disruptions.

## 🌟 Key Advantages

🔸 **Reliability:** flows survive tasks that take longer than expected.

🔸 **Flexibility:** choose how to proceed if a long-running task times out.

🔸 **Efficiency:** automation keeps moving by handling hiccups automatically.

---

## 🎥 Video Tutorial
{% include video id="VKWl_LJfLTE" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I specify custom timeout values in Power Automate?**
Use ISO 8601 duration format (e.g. P2W, P1D, PT2H, PT30M, PT45S) in the **Timeout** field of the action's settings.

**2. Will my flow still fail if an action times out?**
If you don't configure error handling, a timeout fails the run. Use **Configure run after** to catch timeouts and continue.

**3. Can I use timeouts with all actions in Power Automate?**
Most built-in actions allow timeout configuration. For unsupported actions, wrap them in scopes or alternative logic.

## 🔗 Related Tips
- [#PowerPlatformTip 144 – Infinite Approvals beyond 30 days](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-144-infinite-approvals/) — keep approvals alive past the 30-day limit.
- [#PowerPlatformTip 98 – Secure Inputs & Secure Outputs](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-98-secure-inputs-secure-outputs/) — more action-setting tricks in flows.
