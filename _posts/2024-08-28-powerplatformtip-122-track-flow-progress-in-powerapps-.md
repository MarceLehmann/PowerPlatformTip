---
title: "#PowerPlatformTip 122 – 'Track Flow Progress in PowerApps'"
date: 2024-08-28
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - StateLog
  - FlowProgress
  - Monitoring
  - PowerPlatformTip
excerpt: "Monitor Power Automate flow progress in PowerApps by creating a StateLog and using a timer to fetch real-time updates."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Track a running Power Automate flow inside Power Apps by logging status to a StateLog table and polling it with a timer.

## 💡 Challenge
You started a Power Automate flow from a Power App and want to show its live progress back in the app. But "Respond to a PowerApp or flow" can only return once — so you can't push multiple status updates back while the flow keeps running.

## ✅ Solution
Log the flow's progress to a StateLog table (Dataverse or SharePoint) as it runs, then use a Timer control in Power Apps to poll that table and display the latest status in real time.

## 🔧 How It's Done

**1. Create a StateLog table**

🔸 Add a Dataverse or SharePoint table with columns like `Status`, `Timestamp` and `FlowID`.

**2. Write progress from the flow**

🔸 At each meaningful step, add or update a StateLog row with the current status and the run's unique `FlowID`.

**3. Poll from Power Apps with a Timer**

🔸 Add a Timer control (e.g. a 1–5 second interval) that refreshes the StateLog and reads the latest entry for the current `FlowID`.

**4. Show the status in the UI**

🔸 Bind a label or progress indicator to the latest status so users see live updates while the flow runs.

## 🎉 Result
Users watch the flow's progress update live inside the Power App — from "Started" through to "Completed" — instead of waiting blindly for a single response.

## 🌟 Key Advantages

🔸 Real-time visibility into long-running flows

🔸 Works for multiple concurrent flows via a unique FlowID

🔸 Uses standard Dataverse/SharePoint plus a Timer — no premium requirement

---

## 🛠️ FAQ
**1. How do I set up the StateLog table?**
Create a Dataverse (or SharePoint) table with fields like Status, Timestamp, and FlowID. Make sure your flow and app both have permissions to read and write entries.

**2. What polling interval should I use for the timer in PowerApps?**
A 1–5 second interval strikes a good balance between real-time feedback and performance. Adjust based on app complexity to avoid excessive API calls.

**3. Can I monitor multiple flows concurrently?**
Yes. Include a unique FlowID in each StateLog entry and filter your Power Apps controls by FlowID to track multiple flows in parallel.

---