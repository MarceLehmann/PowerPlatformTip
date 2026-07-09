---
title: "#PowerPlatformTip 129 – 'Case-sensitive SharePoint Filtering'"
date: 2024-11-06
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - SharePoint
  - OData
  - FilterArray
  - CaseSensitivity
  - DataFiltering
excerpt: "Combine OData filtering with Filter array in Power Automate for precise, case-sensitive SharePoint queries."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Get case-sensitive SharePoint results in Power Automate by pre-filtering with OData, then refining with a 'Filter array' action.

## 💡 Challenge
SharePoint OData filtering does not differentiate between uppercase and lowercase letters.

## ✅ Solution
Use OData filtering for an initial, quick query. Then, refine the data using the "Filter array" action, which does distinguish between uppercase and lowercase characters.

## 🔧 How It's Done
Apply OData filtering in your SharePoint query for the first selection (e.g., based on a specific field value).
Follow it up with the "Filter array" action to perform a case-sensitive check by filtering the text again in the array.

## 🎉 Result
You get fast and efficient filtering with OData, combined with precise, case-sensitive verification using "Filter array." This ensures you retrieve exactly the data you're looking for.

## 🌟 Key Advantages
🔸 Fast queries with OData
🔸 Accurate filtering with "Filter array"
🔸 Combined efficiency and precision

## 🎥 Video Tutorial
{% include video id="a7Hendredjs" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why is OData filtering case-insensitive?**  
SharePoint’s OData endpoint applies string comparisons without distinguishing letter casing.

**2. Can I perform case-sensitive filtering directly in OData?**  
No, SharePoint OData does not support native case-sensitive comparisons in the query.

**3. Does using Filter array impact performance?**  
When used after OData pre-filtering, Filter array processes a smaller set in-memory, maintaining good performance.