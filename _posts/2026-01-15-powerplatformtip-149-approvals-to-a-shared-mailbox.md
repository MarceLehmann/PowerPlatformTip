---
title: "#PowerPlatformTip 149 – 'Approvals to a Shared Mailbox'"
date: 2026-01-15
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - Approvals
  - Outlook
  - SharedMailbox
  - UserContext
  - PowerPlatformTip
excerpt: "Sending a Power Automate approval to a shared mailbox looks fine – until someone clicks. The 'Start and wait for an approval' task is bound to a single identity, so a delegated user tries to complete it in their own context and it fails. The fix: use 'Send email with options' so any member of the shared mailbox can respond."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Send Power Automate approvals to a shared mailbox with 'Send email with options' so any delegated member can respond via `SelectedOption`.

**The trap:** You assign a *Start and wait for an approval* action to a shared mailbox so the whole team can decide. The email arrives, everyone sees it – but when a delegated user clicks **Approve**, nothing sticks. The approval task belongs to one identity and the clicking user isn't the assigned approver, so the action tries to complete in the wrong context.

**The fix:** Replace the standard approval with the **Send email with options** action from Office 365 Outlook. The actionable email lands in the shared mailbox and any member can respond – you capture the answer with the `SelectedOption` token.

## 💡 Challenge
The standard **Start and wait for an approval** action creates an approval task bound to the identity in the **Assigned to** field, surfacing in that identity's Approvals center and Outlook actionable card. Assign it to a shared mailbox and the task ties to the mailbox identity – but the people who work the mailbox are *delegated* users with their own accounts. When one clicks **Approve** or **Reject**, the response is attempted in their personal context, which was never the assigned approver, so the decision doesn't register. Reassigning is possible, but only manually from the Approvals center and per task – not something a shared mailbox can do cleanly at scale.

## ✅ Solution
Swap the Approvals action for the **Send email with options** action (Office 365 Outlook). It sends a normal actionable email with voting buttons defined in the **User Options** field (for example `Approve, Reject`) straight into the shared mailbox. Any team member with access can click a button, and the flow reads the answer from the **SelectedOption** dynamic value – no identity-bound approval task, no user-context mismatch.

## 🔧 How It's Done

**1. Configure the Outlook connection**

🔸 Use a connection whose account has *Send As* / *Send on Behalf* on the shared mailbox, or set the **From (Send as)** field of the action to the shared mailbox address.

**2. Add the "Send email with options" action**

🔸 In the **Add an action** search box type `send email` and pick **Office 365 Outlook – Send email with options**.

**3. Fill in the fields**

🔸 **To:** the shared mailbox address (or individual approvers, semicolon separated).

🔸 **Subject:** a clear decision title, e.g. `Approval needed: Invoice #12345`.

🔸 **User Options:** your decision buttons as a comma-separated list, e.g. `Approve,Reject`.

**4. Add a Condition**

🔸 Left side: the **SelectedOption** dynamic value. Operator: `is equal to`. Right side: `Approve`.

**5. Build the branches**

🔸 In **If yes / If no**, add your follow-up logic (update SharePoint, notify the requester, etc.). The clicked answer lives in **SelectedOption** – always persist or act on it, otherwise the decision is lost.

**6. (Optional) Log who responded**

🔸 Because the mailbox is shared, add a comment step or capture the responder to keep an audit trail of the actual decision-maker.

## 🎉 Result
The decision request reaches the whole team through the shared mailbox, and **any** member can approve or reject with a single click that the flow reliably captures. No identity-bound approval task, no "it worked for me but not for my colleague" context errors, and no per-user flow duplication.

## 🌟 Key Advantages

🔸 **Context-proof:** no approval task tied to one identity – every delegated mailbox user can respond.

🔸 **Team-friendly:** perfect for support, finance, or dispatch mailboxes where whoever is available decides.

🔸 **Simple & standard:** uses only the native Office 365 Outlook action, no premium approval task, no Adaptive Card JSON.

---

## 🛠️ FAQ
**1. Why does assigning a standard approval to a shared mailbox fail?**
The *Start and wait for an approval* task is bound to the identity in the **Assigned to** field. A delegated user clicking the actionable card acts in their own personal context, which isn't the assigned approver, so the decision doesn't complete against the task.

**2. How do I read the decision from Send email with options?**
The action returns the clicked value in the **SelectedOption** dynamic token. Add a Condition (or Switch) on **SelectedOption** to branch your flow, and always store or act on the value.

**3. Do I lose the Approvals center history with this approach?**
Yes – Send email with options doesn't create an entry in the Approvals center. If you need a tracked decision log, write the responder and outcome to a SharePoint list or Dataverse table yourself.

---

## 🔗 Related Tips

🔸 [#PowerPlatformTip 114 – Send Approvals to External Recipients](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-114-send-approvals-to-external-recipients/)