---
title: "#PowerPlatformTip 144: Infinite Approvals beyond 30 days"
seo_title: "Power Automate Approvals Beyond 30 Days"
date: 2025-10-15
last_modified_at: 2026-07-10
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - PowerApps
  - Dataverse
  - Approvals
  - Governance
  - PowerPlatformTip
excerpt: "Infinite Approvals lets you build Power Automate approval flows that survive beyond the 30-day timeout limit by safely restarting themselves. You can either send a fresh approval request after each timeout or restart the flow while still waiting on the original approval so the first email link and task remain valid."
description: "Power Automate approvals time out after 30 days, killing long HR, legal & multi-level sign-offs. Two patterns to run approvals indefinitely, no premium needed."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Beat the 30-day Power Automate approval timeout by having the flow restart itself via a SharePoint `TriggerFlow` flag, either send a fresh approval each cycle, or keep waiting on the *same* approval by storing its Approval ID.

Approvals that run longer than 30 days are far more common than most makers expect. Contract sign-offs, budget and procurement requests, legal reviews, complex HR cases, or multi-level management chains routinely sit in someone's queue for weeks. Then, quietly, the flow run just **times out at day 30**, the approval task goes stale, nobody gets notified, and the whole process silently dies in the run history. This tip gives you two reliable patterns to keep those approvals alive for as long as you need.

## 💡 Challenge
Standard Power Automate approval actions ("Start and wait for an approval" / "Wait for an approval") have a hard **30-day action timeout**. When that limit is hit:

🔸 The flow run stops and is marked as timed out in the history.

🔸 The approval task and email link go stale, approvers who finally react get nothing back.

🔸 There's no built-in way to "keep waiting" or automatically resume the process.

For any business process where a decision legitimately takes longer than a month, this is a showstopper.

## ✅ Solution
Let the flow **restart itself** before or after the timeout, using a small SharePoint list as a control table. Two helper columns drive everything:

🔸 `TriggerFlow` (Yes/No), controls *when* a new run may start.

🔸 `ApprovalID` (single line of text), stores the current approval so a later run can keep waiting on it (only needed for Method 2).

From there, pick the pattern that fits your process:

🔸 **Method 1, New approval each cycle:** every timeout starts a fresh approval (new email + new task). Best when you *want* a recurring reminder.

🔸 **Method 2, Same approval, silent restart:** the flow restarts in the background but keeps waiting on the original approval task, so the first email link stays valid. Best for a clean approver experience.

## 🔧 How It's Done

**1. Prepare SharePoint and the trigger**

🔸 Add a Yes/No column `TriggerFlow` (default **Yes**) and a single-line-of-text column `ApprovalID` to your SharePoint list.

🔸 Use the trigger **"When an item is created or modified"** with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when `TriggerFlow` is Yes.

🔸 Make the **very first action** after the trigger an **Update item** that sets `TriggerFlow` to **No**. This prevents edits during the run from re-triggering the flow and creating infinite loops.

**2. Method 1, a new approval each time**

🔸 Add **"Start and wait for an approval"**, configure Title and Assigned to as usual, and set a **Timeout** (e.g. `P29D` = 29 days) in the action settings so you restart *before* the hard 30-day limit.

🔸 After it, add an **Update item** that sets `TriggerFlow` back to **Yes**, with **Configure run after** set to run only when the approval **has timed out**. Flipping the item starts a new run that sends a fresh approval email and task.

🔸 On the **is successful** path, put your real post-approval business logic and leave `TriggerFlow` at No so the loop ends.

**3. Method 2, keep waiting on the same approval**

🔸 Add a **Condition** checking whether `ApprovalID` is empty. If empty → use **"Create an approval"**, then **Update item** to write the returned Approval ID into `ApprovalID`. If not empty → use **Compose** to read the existing `ApprovalID` so it can be reused.

🔸 Below the condition, add **"Wait for an approval"** and supply the Approval ID, so every run waits on the *correct*, original approval task.

🔸 Add an **Update item** with **run after: has timed out** that sets `TriggerFlow` to Yes, this restarts the flow silently while the original approval email/link stays valid.

🔸 Add a separate **is successful** branch on "Wait for an approval" with your post-approval logic, and finish with an **Update item** that clears `ApprovalID` and keeps `TriggerFlow` at No so the loop ends cleanly.

**4. Test the restart cycle**

🔸 Temporarily set the Timeout very short (e.g. `PT5M`) to prove the timeout → restart handoff works before going live with `P29D`.

## 🤔 Which method should I choose?

| | **Method 1, New approval** | **Method 2, Same approval** |
|---|---|---|
| Approver gets | A fresh email + task each cycle | One persistent task; no new emails |
| Feels like | A recurring reminder | A single, uninterrupted approval |
| Extra column | `TriggerFlow` only | `TriggerFlow` **+** `ApprovalID` |
| Best for | Chasing slow approvers | Clean UX, audit-friendly processes |
| Approvals center | Multiple entries over time | One stable entry |

## 🎉 Result
Your approval flows now run **without a hard time limit**, each timeout simply restarts the flow instead of killing the process. Depending on the method, approvers either get a fresh nudge every cycle, or work with a single persistent approval that stays valid while the flow quietly restarts in the background. No more decisions lost at day 30.

## 🌟 Key Advantages

🔸 Removes the 30-day approval timeout as a failure point in long-running processes.

🔸 Two patterns: stronger visibility (repeated reminders) *or* a cleaner single-approval experience.

🔸 Uses only **standard** SharePoint and Approvals capabilities, no premium licenses or custom connectors.

🔸 The `TriggerFlow` guard prevents runaway/infinite loops by design.

---

## 🎥 Video Tutorial
{% include video id="iTGwT58amFs" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why can't approvals simply run longer than 30 days?**
Approvals are subject to Power Automate action limits, and long-running actions time out after 30 days. That's a platform limit you can't raise, so you need a restartable pattern to keep the process alive.

**2. Why does Method 2 split "Create an approval" and "Wait for an approval"?**
Splitting the actions exposes the **Approval ID**. Storing it in SharePoint lets later runs reuse it, so the *same* approval task is tracked across restarts instead of creating a new task each time.

**3. How does TriggerFlow prevent endless retriggering?**
The trigger condition only fires when `TriggerFlow` is Yes, and the first Update item immediately sets it to No. Only the dedicated timeout branch that sets `TriggerFlow` back to Yes can start a new run, so exactly one controlled restart happens per cycle.

**4. Won't the run history fill up with timed-out runs?**
Each cycle is a separate run, so yes, you'll see periodic entries. That's expected and harmless. Set the Timeout close to the limit (e.g. `P29D`) to minimize the number of restarts, and use the item's status column to track where the approval stands.

**5. Can I use Dataverse instead of SharePoint?**
Yes. Any data source with an "on create/modify" trigger and update action works, replace the SharePoint list with a Dataverse table and use the equivalent trigger condition on your `TriggerFlow` column.

**6. Does the approver get spammed with emails?**
Only with Method 1, and only once per cycle (e.g. every ~29 days), which is usually the *desired* reminder. Method 2 sends no new emails on restart; the original approval task and its link stay valid.

## 🔗 Related Tips
- [#PowerPlatformTip 109: Use Timeout](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-109-use-timeout/), set ISO 8601 timeouts and run-after handling on any action.
- [#PowerPlatformTip 114: Send Approvals to External Recipients](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-114-send-approvals-to-external-recipients/), extend approvals beyond your tenant.
- [#PowerPlatformTip 149: Approvals to a Shared Mailbox](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-149-approvals-to-a-shared-mailbox/), route approval tasks to shared inboxes.
