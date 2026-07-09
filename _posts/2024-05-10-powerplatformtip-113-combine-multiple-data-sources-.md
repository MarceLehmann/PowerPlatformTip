---
title: "#PowerPlatformTip 113 – 'Combine Multiple Data Sources'"
date: 2024-05-10
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerFx
  - Ungroup
  - DataIntegration
  - Collections
  - PowerPlatformTip
excerpt: "Simplify merging static and dynamic data in Power Apps by ungrouping mixed data sources into a single flat table for improved management."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Merge static and dynamic data in Power Apps into one flat table using the `Ungroup` function.

## 💡 Challenge
Combining multiple data sources — including hard-coded static data — into a single Power Apps structure adds real complexity to your app's data management.

## ✅ Solution
Use the `Ungroup` function to flatten different data types into one unified table, making the data easier to interact with and use.

## 🔧 How It's Done

**1. Combine the sources** into an array mixing static and dynamic data.

🔸 Build an array of objects containing local static entries and tables from your data sources.

🔸 Use a common property name (e.g. `locItem`) across all objects.

**2. Flatten with `Ungroup`.**

🔸 Specify the common nested property (`locItem`) as the one to ungroup.

🔸 The result is a single flat table containing all items.

```powerapps
Ungroup(
   [
      // Object 1
      {locItem:[{Date: Today(), ID:0}]},

      // Object 2
      {locItem: DelegationPlayground}
   ],
   // The 'locItem' property is the common property to ungroup
   locItem
)
```

## 🎉 Result
A streamlined, efficient data structure that's easier to manage and query — boosting app performance and the user experience.

## 🌟 Key Advantages

🔸 Integrates disparate data sources into one structure.

🔸 Simplifies querying and data manipulation in the app.

🔸 Improves overall efficiency and maintainability.

---

## 🎥 Video Tutorial
{% include video id="DAWOoWicDH8" provider="youtube" %}

---

## 🛠️ FAQ
**1. What is the main purpose of the Ungroup function in Power Apps?**
It flattens nested tables or collections into a single level by ungrouping a specific nested property, making mixed data sources easier to work with.

**2. Can I use other functions to merge static and dynamic data?**
Yes, you can also use the `Table` function, but `Ungroup` gives more flexibility when combining different sources into one structure.

**3. Is Ungroup delegable with large data sets?**
Ungroup itself isn't delegable, but it works well on locally loaded collections or static data after the data has been retrieved from delegable sources.

---