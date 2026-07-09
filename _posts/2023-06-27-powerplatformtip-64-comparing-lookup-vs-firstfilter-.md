---
title: "#PowerPlatformTip 64 – 'Comparing Lookup vs. First(Filter)'"
date: 2023-06-27
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Apps
  - Lookup
  - First
  - Filter
  - Data Access
  - Performance
  - Optimization
  - App Development
  - PowerPlatformTip
excerpt: "Compare Lookup and First/Filter in Power Apps to choose the best approach for your scenario. Optimize data access, improve performance, and avoid common pitfalls in app development."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

In Power Apps, when you need to retrieve the first record that meets certain criteria, you have two functions—`Lookup()` and `First(Filter())`—which can cause confusion over which to use.

## ✅ Solution

Pick one consistent pattern. Using `First(Filter(Source, Condition))` throughout keeps your code simple, uniform, and maintainable.

## 🔧 How It's Done

**1. Identify your criteria**

🔸 Determine the data source (`Source`) and the filter condition.

🔸 Write `Filter(Source, Condition)` to narrow down records.

**2. Retrieve the first match**

🔸 Wrap the filter in `First()`:

```powerapps
First( Filter( Source, Condition ) )
```

🔸 Use this expression in variables, galleries, or formulas.

**3. Standardize across your app**

🔸 Replace existing `Lookup(Source, Condition)` calls with `First(Filter(...))`.

🔸 Maintaining a single pattern improves readability and eases future updates.

## 🎉 Result

You now have a uniform approach to fetching the first matching record, making your Power Apps formulas more consistent and easier to read—without any performance penalty.

## 🌟 Key Advantages

🔸 Consistent coding pattern throughout your app

🔸 Improved readability and maintainability

🔸 No difference in performance compared to `Lookup()`

## 🎥 Video Tutorial

{% include video id="3-FAa9GZgqQ" provider="youtube" %}

## 🛠️ FAQ

**Q: What's the difference between Lookup() and First(Filter())?**

There is no functional or performance difference; both issue the same query. Using `First(Filter())` aligns with the common Filter pattern.

**Q: When might I still use Lookup()?**

You can use `Lookup()` interchangeably, but for consistency—and to leverage complex filtering scenarios—`First(Filter())` is preferred.

**Q: Does switching to First(Filter()) impact performance?**

No. Both functions generate the same server call, so performance remains identical.
