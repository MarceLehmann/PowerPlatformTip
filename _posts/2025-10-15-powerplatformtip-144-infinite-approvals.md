---
title: "#PowerPlatformTip 144 – Infinite Approvals beyond 30 days"
date: 2025-10-15
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - PowerApps
  - Dataverse
  - Governance
  - PowerPlatformTip
excerpt: "Infinite Approvals lets you build Power Automate approval flows that survive beyond the 30-day timeout limit by safely restarting themselves. You can either send a fresh approval request after each timeout or restart the flow while still waiting on the original approval so the first email link and task remain valid."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Beat the 30-day Power Automate approval timeout by having the flow restart itself via a SharePoint TriggerFlow flag – new or same approval.

## 💡 Challenge
Standard Power Automate approval actions time out after 30 days, which breaks long-running processes like legal reviews, complex HR cases, or multi-level management approvals. When the approval action times out, the flow run stops — you can't keep waiting for the decision or automatically resume the process.

## ✅ Solution
Use a SharePoint list with two helper columns to control when the flow may trigger and, for the advanced pattern, to store the current Approval ID. On top of that, pick one of two patterns: create a brand-new approval whenever the previous one times out, or restart the flow and keep waiting on the same approval task by reusing its Approval ID.

## 🔧 How It's Done

**1. Prepare SharePoint and the trigger**

🔸 Add a Yes/No column `TriggerFlow` (default Yes) and a single-line-of-text column `ApprovalID` to your SharePoint list. Use the trigger "When an item is created or modified" with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is Yes.

🔸 Make the very first action after the trigger an Update item that sets TriggerFlow to No, so further edits during the run can't re-trigger the flow and cause infinite loops.

**2. Method 1 — a new approval each time**

🔸 Add "Start and wait for an approval", configure Title and Assigned to as usual, and optionally set a Timeout (e.g. 29 days) in the action settings.

🔸 After it, add an Update item that sets TriggerFlow back to Yes, with run-after configured to run only when the approval has timed out — this flips the item and starts a new run that sends a fresh approval email and task.

**3. Method 2 — keep waiting on the same approval**

🔸 Add a Condition checking whether `ApprovalID` is empty. If empty, use "Create an approval" then Update item to write the Approval ID into `ApprovalID`; otherwise use Compose to read the existing `ApprovalID` so it can be reused.

🔸 Under the condition, add "Wait for an approval" and supply the Approval ID so it always waits on the correct approval, then add an Update item (run-after: has timed out) that sets TriggerFlow to Yes to restart the flow.

🔸 Add a separate success branch on "Wait for an approval" (run-after: is successful), place your real post-approval business logic there, and finish with an Update item that clears `ApprovalID` and keeps TriggerFlow No so the loop ends cleanly.

## 🎉 Result
Your approval flows can now run without a hard time limit, because each timeout simply restarts the flow instead of killing the process. Depending on the method, approvers either receive a fresh reminder email and task each cycle, or work with a single persistent approval that stays valid while the flow quietly restarts in the background.

## 🌟 Key Advantages

🔸 Handles the 30-day approval timeout explicitly, avoiding broken runs and hanging approval tasks in long-running processes.

🔸 Lets you choose between stronger visibility via repeated reminder emails or a cleaner experience with one stable approval in the Approvals center.

🔸 Uses only standard SharePoint and Approvals capabilities, so it works in typical Power Automate environments without special licenses or custom connectors.

---

## 🎥 Video Tutorial
{% include video id="iTGwT58amFs" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why can't approvals simply run longer than 30 days?**
Approvals are subject to Power Automate action limits, and long-running actions time out after 30 days — so you need restartable patterns like these to keep the process alive.

**2. Why does Method 2 split "Create an approval" and "Wait for an approval"?**
Splitting the actions exposes the Approval ID, which is stored in SharePoint and reused by later runs, so the same approval task is tracked across restarts instead of creating new tasks each time.

**3. How does TriggerFlow prevent endless retriggering?**
The trigger condition only fires when TriggerFlow is Yes, and the first Update item immediately sets it to No — so only the dedicated timeout branch that sets TriggerFlow back to Yes can start a new run.

## 🔗 Related Tips
- [#PowerPlatformTip 114 – Send Approvals to External Recipients](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-114-send-approvals-to-external-recipients/) — extend approvals beyond your tenant.
- [#PowerPlatformTip 149 – Approvals to a Shared Mailbox](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-149-approvals-to-a-shared-mailbox/) — route approval tasks to shared inboxes.
