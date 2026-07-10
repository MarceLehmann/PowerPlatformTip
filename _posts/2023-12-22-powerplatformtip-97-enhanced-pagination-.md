---
title: "#PowerPlatformTip 97: 'Enhanced Pagination'"
date: 2023-12-22
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Automate
  - Pagination
  - Excel
  - SharePoint
  - Data Retrieval
  - Performance
  - Integration
excerpt: "Overcome default item limits in Power Automate by enabling enhanced pagination for Excel and SharePoint, retrieve more data, improve performance, and streamline integrations."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Raise the default item limits (Excel 256, SharePoint 100) by enabling Pagination and setting a higher threshold in the Get items action settings.

## 💡 Challenge
In Power Automate, the default "Get items" action settings limit the number of items returned from Excel and SharePoint sources. Excel is capped at 256 items, while SharePoint defaults to 100.

## ✅ Solution
Adjusting the pagination settings is crucial for Excel and SharePoint integrations. It ensures that you retrieve more than the default number of items, enhancing data handling capabilities.

## 🔧 How It's Done
Here's how to do it:
1. In Power Automate, open your flow and locate the "Get items" action.  
2. Click the three dots (…) on the action and open **Settings**.  
3. Turn on **Pagination** and set the **Threshold** to the number of items you need.  
   🔸 For Excel: increase the limit beyond the default 256.  
   🔸 For SharePoint: raise it above the default 100.  
4. Carefully balance performance and data retrieval needs.

## 🎉 Result
Efficient and complete data retrieval from Excel and SharePoint, overcoming the default item limit constraints.

## 🌟 Key Advantages
🔸 Comprehensive data access for larger datasets.  
🔸 Customizable settings to match specific project requirements.  
🔸 Improved data handling and performance in complex workflows.

## 🎥 Video Tutorial
{% include video id="KIINmSQyj1w" provider="youtube" %}

## 🛠️ FAQ
**1. What are the default item limits for Excel and SharePoint in the 'Get items' action?**

By default, the Excel connector returns up to 256 items, while the SharePoint connector returns up to 100 items.

**2. How can I increase the pagination threshold in my flow?**

Open the 'Get items' action, click on the three dots to access **Settings**, enable **Pagination**, and set the **Threshold** to the desired value.

**3. Will increasing the pagination limit slow down my flow?**

Raising the item limit can impact performance and run time. Test different threshold values to find a balance between data retrieval needs and performance.
