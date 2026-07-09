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
  - PowerPlatformTip
excerpt: "Combine OData filtering with Filter array in Power Automate for precise, case-sensitive SharePoint queries."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Get case-sensitive SharePoint results in Power Automate by pre-filtering with OData, then refining with a 'Filter array' action.

## 💡 Challenge
SharePoint's OData filtering doesn't distinguish between uppercase and lowercase letters, so a query for `ABC` also returns `abc`.

## ✅ Solution
Use OData for a fast initial query, then refine the results with the "Filter array" action — which *does* distinguish uppercase from lowercase.

## 🔧 How It's Done

**1. Pre-filter with OData**

🔸 Apply an OData filter in your SharePoint query for the first, coarse selection (e.g. based on a field value).

**2. Refine with "Filter array"**

🔸 Add a "Filter array" action and compare the text again — this check is case-sensitive, so only exact-case matches remain.

## 🎉 Result
You combine fast OData querying with precise, case-sensitive verification via "Filter array," so you retrieve exactly the data you're looking for.

## 🌟 Key Advantages

🔸 Fast queries with OData

🔸 Accurate filtering with "Filter array"

🔸 Combined efficiency and precision

---

## 🎥 Video Tutorial
{% include video id="a7Hendredjs" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why is OData filtering case-insensitive?**
SharePoint's OData endpoint applies string comparisons without distinguishing letter casing.

**2. Can I perform case-sensitive filtering directly in OData?**
No. SharePoint OData does not support native case-sensitive comparisons in the query.

**3. Does using Filter array impact performance?**
When used after OData pre-filtering, Filter array processes a smaller set in-memory, keeping performance good.

---