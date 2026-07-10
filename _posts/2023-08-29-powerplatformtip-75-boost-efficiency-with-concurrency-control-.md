---
title: "#PowerPlatformTip 75: 'Boost Efficiency with Concurrency Control'"
date: 2023-08-29
last_modified_at: 2026-07-09
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

> **TL;DR:** Turn on Concurrency Control on a 'For each' loop to run up to 50 iterations in parallel, and offload to a child flow to scale beyond 50.

## 💡 Challenge

By default, "For each" loops in Power Automate execute actions sequentially, which can be time-consuming when dealing with a large number of items.

## ✅ Solution

Use the "Concurrency Control" feature in Power Automate to customize the degree of parallelism, allowing multiple iterations to run simultaneously.

## 🔧 How It's Done

**1. Open the loop settings**

🔸 Navigate to the **Settings** of the "For each" loop.

**2. Enable Concurrency Control**

🔸 Turn on "Concurrency Control" and set the desired degree of parallelism (up to 50).

**3. Scale beyond 50 with child flows**

🔸 To process more than 50 items in parallel, set the degree to 50 and offload the actions to a child flow.

🔸 This way each user (e.g., when sending an adaptive card) can have a dedicated flow, ensuring individual responses.

## 🎉 Result

You've optimized the execution of your flow, allowing for much faster processing of items.

## 🌟 Key Advantages

🔸 Speed & Efficiency: Parallel processing reduces overall execution time, especially for large data sets

🔸 Scalability: Offloading to child flows lets you handle more parallel tasks without hitting the limit

🔸 Individual Responses: Child flows per user ensure personalized processing and responses

> ⚠️ **Note:** Be cautious with actions that might lead to throttling inside an "Apply to each" loop. Excessive parallelism can cause exponential delays, making your flow even slower. Always test and monitor to find the optimal balance.

## 🎥 Video Tutorial

{% include video id="qyFAtpnek-w" provider="youtube" %}

## 🛠️ FAQ

**Q: What is Concurrency Control in Power Automate?**

Concurrency Control lets you configure the number of parallel threads for a loop, so multiple iterations run simultaneously instead of sequentially.

**Q: What is the maximum degree of parallelism I can set?**

You can set up to 50 parallel threads in a For each loop. For processing more items in parallel, use a child flow and set the parent to 50.

**Q: Will setting a high degree of parallelism cause throttling?**

Excessive parallelism can lead to throttling by connectors or the Power Platform, potentially slowing down your flow. Test different settings to find the optimal balance.
