---
title: "#PowerPlatformTip 75 – 'Boost Efficiency with Concurrency Control'"
date: 2023-08-29
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Automate
  - Concurrency Control
  - Parallelism
  - Flow Optimization
  - Child Flows
  - Efficiency
  - Power Platform
  - Automation
excerpt: "Enable Concurrency Control in Power Automate to process 'For Each' loops in parallel, dramatically improving flow speed, scalability, and automation efficiency."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Enable Concurrency Control in Power Automate to process 'For Each' loops in parallel, dramatically improving flow speed, scalability, and automation efficiency.

## 💡 Challenge
If you don't want to miss out on any future #PowerPlatformTip posts, be sure to subscribe to my newsletter – you'll be the first to know whenever I publish a new tip!
								Type your email…							
								Subscribe							
💡 **The Challenge:** By default, "For each" loops in Power Automate execute actions sequentially, which can be time-consuming when dealing with a large number of items.

## ✅ Solution
If you don't want to miss out on any future #PowerPlatformTip posts, be sure to subscribe to my newsletter – you'll be the first to know whenever I publish a new tip!
								Type your email…							
								Subscribe							
💡 **The Challenge:** By default, "For each" loops in Power Automate execute actions sequentially, which can be time-consuming when dealing with a large number of items.
✅ **The Solution:** Use the "Concurrency Control" feature in Power Automate to customize the degree of parallelism, allowing multiple actions to run simultaneously.
🔧 **How It's Done:**
1️⃣ Navigate to the "Settings" of the "For each" loop.
2️⃣ Enable "Concurrency Control" and set the desired degree of parallelism (up to 50).
3️⃣ If you need to process more than 50 items in parallel, consider setting the degree to 50 and offloading the actions to a child flow. This way, each user (e.g., when sending an adaptive card) can have a dedicated flow, ensuring individual responses.
🎉 **Result:** You've optimized the execution of your flow, allowing for faster processing of items!
**Key Advantages:**
1️⃣ **Speed & Efficiency:** Parallel processing reduces the overall execution time, especially for large data sets.
2️⃣ **Scalability:** By offloading to child flows, you can handle a larger number of parallel tasks without hitting the limit.
3️⃣ **Individual Responses:** Using child flows for each user ensures personalized processing and responses.
⚠️ **Note:** Be cautious when using actions that might lead to throttling within an "Apply to each" loop. Excessive parallelism can cause exponential delays, making your flow even slower. Always test and monitor your flows to find the optimal balance.

## 🔧 How It's Done
1️⃣ Navigate to the "Settings" of the "For each" loop.
2️⃣ Enable "Concurrency Control" and set the desired degree of parallelism (up to 50).
3️⃣ If you need to process more than 50 items in parallel, consider setting the degree to 50 and offloading the actions to a child flow. This way, each user (e.g., when sending an adaptive card) can have a dedicated flow, ensuring individual responses.

## 🎉 Result
You've optimized the execution of your flow, allowing for faster processing of items!
**Key Advantages:**
1️⃣ **Speed & Efficiency:** Parallel processing reduces the overall execution time, especially for large data sets.
2️⃣ **Scalability:** By offloading to child flows, you can handle a larger number of parallel tasks without hitting the limit.
3️⃣ **Individual Responses:** Using child flows for each user ensures personalized processing and responses.
⚠️ **Note:** Be cautious when using actions that might lead to throttling within an "Apply to each" loop. Excessive parallelism can cause exponential delays, making your flow even slower. Always test and monitor your flows to find the optimal balance.

## 🌟 Key Advantages
🔸 Improved Efficiency: Faster development cycles through automation.
🔸 Better Consistency: Standardized approach across all projects.
🔸 Enhanced Reliability: Reduced risk of failure during execution.

## 🎥 Video Tutorial
{% include video id="qyFAtpnek-w" provider="youtube" %}

---

## 🛠️ FAQ
**1. What is Concurrency Control in Power Automate?**  
Concurrency Control is a feature that lets you configure the number of parallel threads for a loop, so multiple iterations run simultaneously instead of sequentially.

**2. What is the maximum degree of parallelism I can set?**  
You can set up to 50 parallel threads in a For each loop. For processing more items in parallel, use a child flow and set the parent to 50.

**3. Will setting a high degree of parallelism cause throttling?**  
Excessive parallelism can lead to throttling by connectors or the Power Platform, potentially slowing down your flow. Test different settings to find the optimal balance.