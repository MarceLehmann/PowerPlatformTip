---
title: "#PowerPlatformTip 001 – 'Infinite Approvals beyond 30 days'"
date: 2025-10-15
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

## 💡 Challenge

Standard Power Automate approval actions time out after 30 days, which breaks long-running processes like legal reviews, complex HR cases, or multi-level management approvals. When the approval action times out, the flow run stops and you cannot continue to wait for the decision or automatically resume the process.

## ✅ Solution

Use a SharePoint list with two helper columns to control when the flow is allowed to trigger and, for the advanced pattern, to store the current Approval ID. On top of this, implement one of two patterns: either create a brand-new approval whenever the previous one times out or restart the flow and keep waiting on the same approval task by reusing its Approval ID.

## 🔧 How It's Done

1. Prepare SharePoint and the trigger  
🔸 Add a Yes/No column TriggerFlow with default Yes and a Single line of text column ApprovalID to your SharePoint list, then use the trigger When an item is created or modified with the trigger condition `@equals(triggerOutputs()?['body/TriggerFlow'], true)` so the flow only runs when TriggerFlow is set to Yes.  
🔸 Make the very first action after the trigger an Update item that sets TriggerFlow to No so any further edits during the run cannot re-trigger the flow and create infinite loops.

2. Method 1: Everytime NEW Approval  
🔸 Add Start and wait for an approval, configure Title and Assigned to as usual, and optionally set a Timeout value (for example 29 days) in the action settings to control when the timeout should be raised.  
🔸 After the approval action, add Update item that sets TriggerFlow back to Yes and configure its run after settings so it runs only when the approval action has timed out, which flips the list item and starts a new run that sends a fresh approval email and creates a new task.

3. Method 2: Start and Wait for the SAME Approval  
🔸 Add a Condition that checks if the ApprovalID column in the SharePoint item is empty and, if it is, use Create an approval to build a new approval and then Update item to write the Approval ID into the ApprovalID column, otherwise use a Compose action to read the existing ApprovalID so it can be reused.  
🔸 Under the condition, add Wait for an approval and supply the Approval ID value so the action always waits on the correct approval, then add an Update item with run after set only to has timed out that sets TriggerFlow to Yes to restart the flow when the wait action times out.  
🔸 Add a separate success branch for Wait for an approval configured to run on is successful, place your real post-approval business logic there, and finish with an Update item that clears ApprovalID and keeps TriggerFlow as No so the loop ends cleanly and the item stops retriggering.

## 🎥 Video Tutorial

{% include video id="iTGwT58amFs" provider="youtube" %}

## 🎉 Result

Your approval flows can now effectively run without a hard time limit, because each timeout simply restarts the flow instead of killing the business process. Depending on which method you choose, approvers either receive a new reminder email and a fresh task each cycle or work with a single persistent approval that remains valid while the flow quietly restarts in the background.

## 🌟 Key Advantages

🔸 Handles the 30-day approval timeout explicitly, avoiding broken runs and hanging approval tasks in long-running business processes.  
🔸 Lets you choose between stronger visibility via repeated reminder emails or a cleaner user experience with one stable approval in the Approvals center.  
🔸 Uses only standard SharePoint and Approvals capabilities so it works in typical Power Automate environments without special licenses or custom connectors.

## 🛠️ FAQ

Q1: Why can approvals not simply run longer than 30 days?  
A: Approvals are subject to Power Automate action limits and long-running actions time out after 30 days, so you need restartable patterns like these to keep your business process alive.

Q2: Why does method 2 split Create an approval and Wait for an approval?  
A: Splitting the actions exposes the Approval ID, which is stored in SharePoint and reused by later runs so the same approval task is tracked across restarts instead of creating new tasks every time.

Q3: How does TriggerFlow prevent the flow from retriggering endlessly?  
A: The trigger condition only fires when TriggerFlow is Yes and the first Update item immediately sets it to No, so only the dedicated timeout branch that sets TriggerFlow back to Yes can start a new run.
