---
title: "#PowerPlatformTip 122 – 'Track Flow Progress in PowerApps'"
date: 2024-08-28
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - PowerPlatform
  - StateLog
  - FlowProgress
  - Monitoring
  - RealTime
excerpt: "Monitor Power Automate flow progress in PowerApps by creating a StateLog and using a timer to fetch real-time updates."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Monitor Power Automate flow progress in PowerApps by creating a StateLog and using a timer to fetch real-time updates.

## 💡 Challenge
You want to monitor the progress of a flow (Power Automate) that you started from a PowerApp.

## ✅ Solution
You want to monitor the progress of a flow (Power Automate) that you started from a PowerApp. Unfortunately, Power Automate doesn't support updating the status directly in PowerApps using the "Respond to PowerApps" action multiple times. So how can you track the flow's progress within your app?

## 🔧 How It's Done
1. Identify the area in your app or flow where Track Flow Progress in PowerApps is needed.
🔸 Follow established naming conventions for clarity.
2. Configure the properties according to your business requirements.
🔸 Test the implementation with sample data.
3. Verify the output to ensure it matches the expected results.

## 🎉 Result
**

## 🌟 Key Advantages
🔸 Improved Efficiency: Faster development cycles through automation.
🔸 Better Consistency: Standardized approach across all projects.
🔸 Enhanced Reliability: Reduced risk of failure during execution.

## 🎥 Video Tutorial
{% include video id="noscript" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I set up the StateLog table?**  
To set up the StateLog, create a Dataverse (or SharePoint) table with fields like Status, Timestamp, and FlowID. Ensure your flow and app both have permissions to read and write entries.

**2. What polling interval should I use for the timer in PowerApps?**  
A polling interval of 1–5 seconds strikes a good balance between real-time feedback and performance. Adjust based on app complexity to avoid excessive API calls.

**3. Can I monitor multiple flows concurrently?**  
Yes. Include a unique FlowID in each StateLog entry and filter your PowerApp controls by FlowID to track multiple flows in parallel.