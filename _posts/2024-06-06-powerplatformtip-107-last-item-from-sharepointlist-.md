---
title: "#PowerPlatformTip 107 – 'Last Item from SharePointList'"
date: 2024-06-06
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - SharePoint
  - Data Retrieval
  - Delegation
  - List Sorting
  - Latest Item
  - PowerPlatform
  - Marcel Lehmann
excerpt: "Efficiently retrieve the latest item from a SharePoint list in PowerApps using delegable sorting and the First function for reliable, scalable data access."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
You need the latest entry from a SharePoint list in PowerApps, but the direct approach seems out of reach.

## 💡 Challenge
You need the latest entry from a SharePoint list in PowerApps, but the direct approach seems out of reach.

## ✅ Solution
Employ SortByColumns to sort the SharePoint list by the ID column in descending order, then pluck out the first item with the First function.

## 🔧 How It's Done
* Utilize SortByColumns on the SharePoint data source, targeting the ID column with a descending sort order. This method arranges the items such that the latest entry is at the top.

* Apply the First function around the SortByColumns to grab now top-most item, effectively retrieving the last entry in your list.

## 🎉 Result
This method ensures you access the most recent item from your SharePoint list in PowerApps, bypassing the limitation with the Last function elegantly.

## 🌟 Key Advantages
* **Simplicity and Efficiency**: A straightforward approach to accessing the most recent list entries.

* **Versatility**: Can be adapted to sort by other columns for different scenarios.

* **PowerApps Integration**: Seamlessly integrates within your PowerApps logic, enhancing functionality without complex workarounds.

## 🎥 Video Tutorial
{% include video id="8fIiREiIBNM" provider="youtube" %}

---

## 🛠️ FAQ
**Q: Why can't I use the Last function directly on SharePoint lists?**
The Last function is not delegable for SharePoint data sources in PowerApps, which means it can only work with the first 500 records. Using SortByColumns with First ensures you get the actual latest item regardless of list size.

**Q: Can I use this approach with columns other than ID for sorting?**
Yes, you can sort by any column that supports ordering, such as Created, Modified, or custom date/number fields. For example: `First(SortByColumns(YourList, "Created", Descending))`.

**Q: Will this method work with large SharePoint lists?**
Yes, this approach is delegable to SharePoint, meaning it will work efficiently even with lists containing thousands of items, as the sorting and filtering happen on the SharePoint server.

---

## 🎥 Video Tutorial
{% include video id="8fIiREiIBNM" provider="youtube" %}

---