---
title: "#PowerPlatformTip 7: 'UNION and FilterArray'"
date: 2022-12-16
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerautomate
  - union
  - filterarray
  - data-manipulation
  - efficiency
excerpt: "Merge and filter arrays in Power Automate: Use UNION and FilterArray for efficient data manipulation, deduplication, and smarter workflows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Merge and deduplicate arrays with `union()` (pass the same array twice for DISTINCT), then narrow results with the Filter Array action.

## 💡 Challenge
Data manipulation is a cornerstone of Power Automate, and you often need to merge or filter data sets for various workflows, which quickly gets messy with basic actions alone.

## ✅ Solution
Combine the `union()` function and the 'Filter Array' action. `union()` merges arrays (and deduplicates), while 'Filter Array' returns only the items you're looking for.

## 🔧 How It's Done

**1. Use `union()`**

🔸 `union()` merges two arrays into one. Passing the **same** array twice makes it behave like DISTINCT, removing duplicates.

**2. Use 'Filter Array'**

🔸 Keep only the items that match your condition and drop the rest.

**3. Combine both**

🔸 Merge/deduplicate with `union()`, then narrow the result with 'Filter Array' for precise data sets.

## 🎉 Result
With `union()` and 'Filter Array', you can efficiently merge, deduplicate and filter data sets, fewer actions, cleaner data, faster runs.

## 🌟 Key Advantages

🔸 **Efficiency:** Handle merge/dedupe/filter in just a couple of built-in actions.

🔸 **Flexibility:** Both work with simple values and complex objects.

🔸 **Data Integrity:** `union(x, x)` acts as DISTINCT to remove duplicates automatically.

## 🎥 Video Tutorial
{% include video id="xZxzLlepZcQ" provider="youtube" %}

---

## 🛠️ FAQ

**1. Does UNION automatically remove duplicates?**

Yes, `union()` returns unique values when combining arrays, ensuring no duplicates in the result.

**2. Can I use Filter Array with complex nested objects?**

Absolutely! 'Filter Array' works with complex objects and supports advanced expressions to filter based on nested properties.

**3. What's the performance impact of combining UNION and Filter Array?**

Both are built-in actions and fast, but with very large datasets consider processing in batches to keep run times optimal.
