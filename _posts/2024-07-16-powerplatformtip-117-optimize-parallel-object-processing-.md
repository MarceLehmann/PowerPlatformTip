---
title: "#PowerPlatformTip 117 – 'Optimize Parallel Object Processing'"
date: 2024-07-16
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Marcel Lehmann
  - PowerAutomate
  - PowerPlatform
  - PowerPlatformTip
  - concurrency
  - parallel-processing
  - child-flow
  - database
  - performance
excerpt: "Speed up large-item processing in Power Automate by leveraging child flows, database triggers, and strategic 'Respond to a PowerApp or flow' placement."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Break past the 50-item Apply to Each limit in Power Automate using child flows or database triggers for true parallel processing.

## 💡 Challenge
Managing a large number of items in Power Automate’s “Apply to Each” action can be slow. By default, items are processed sequentially (up to 50 in parallel), causing delays as subsequent items wait for slots to free up.

## ✅ Solution
Trigger child flows or write data to a database to handle items individually, and place the “Respond to a PowerApp or flow” action before lengthy operations to free up the main flow quickly.

## 🔧 How It's Done
Here's how to do it:
1. Triggering a Child Flow  
   🔸 Advantage: Enables parallel execution of over 50 items, improving efficiency.  
   🔸 Steps:  
     - Create a child flow to manage individual items.  
     - In your main flow, loop through items and trigger the child flow for each.  
2. Writing to a Database  
   🔸 Advantage: Ensures data integrity and allows for controlled, structured data processing.  
   🔸 Steps:  
     - Write data to a database within the “Apply to Each” action.  
     - Set up another flow to trigger based on database entries, processing each entry individually.  
3. Strategic Placement of “Respond to a PowerApp or flow”  
   🔸 Advantage: Allows the flow to complete quickly and frees up the system for more requests.  
   🔸 Steps:  
     - Place the “Respond to a PowerApp or flow” action before time-intensive actions.  
     - Resubmit failed flows later, ensuring completion without impacting main flow performance.

## 🎉 Result
Processing of large item sets becomes significantly faster and more efficient, bypassing the default 50-item concurrency limit and improving overall flow responsiveness.

## 🌟 Key Advantages
🔸 Speed: Significantly reduces time to process large item numbers.  
🔸 Efficiency: Allows parallel processing beyond the 50-item limit.  
🔸 Flexibility: Provides more control over structured data processing using child flows or databases.

---

## 🎥 Video Tutorial
{% include video id="p6iVVVzgD5A" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I set concurrency in Apply to Each?**  
You can adjust the concurrency control in the settings of the “Apply to Each” action up to a maximum of 50 parallel runs, but beyond that you need child flows or database triggers.

**2. What are child flows and why use them?**  
Child flows are separate Power Automate flows invoked from a parent flow. They allow you to process items independently and in parallel, bypassing concurrency limits of the main flow.

**3. How do I handle errors in child flows?**  
Implement error handling within the child flow using scopes and configure run-after settings. Log failures to a database or send notifications, and optionally retry or resubmit failed runs later.