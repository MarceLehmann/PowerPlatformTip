---
title: "#PowerPlatformTip 107: 'Last Item from SharePointList'"
date: 2024-06-06
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - SharePoint
  - Delegation
  - SortByColumns
  - PowerFx
  - PowerPlatformTip
excerpt: "Efficiently retrieve the latest item from a SharePoint list in PowerApps using delegable sorting and the First function for reliable, scalable data access."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Get the newest SharePoint item in Power Apps with `First(SortByColumns(List, "ID", Descending))`, delegable, unlike `Last()`.

## 💡 Challenge
You need the latest entry from a SharePoint list in PowerApps, but `Last()` isn't delegable, so the direct approach seems out of reach on larger lists.

## ✅ Solution
Sort the SharePoint list by the **ID** column in descending order, then take the top row with **First()**. Both are delegable to SharePoint, so it scales.

## 🔧 How It's Done

🔸 Sort the data source by the **ID** column in descending order so the newest item is on top:

🔸 `SortByColumns('Your List', "ID", Descending)`

🔸 Wrap it in **First()** to grab that top item, the latest entry:

🔸 `First(SortByColumns('Your List', "ID", Descending))`

## 🎉 Result
You reliably access the most recent item from your SharePoint list in PowerApps, sidestepping the delegation limitation of `Last()`.

## 🌟 Key Advantages

🔸 **Simple & efficient:** a straightforward way to get the most recent entry.

🔸 **Versatile:** sort by other columns (Created, Modified…) for different scenarios.

🔸 **Delegable:** works on large lists because sorting happens on the server.

---

## 🎥 Video Tutorial
{% include video id="8fIiREiIBNM" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why can't I use the Last function directly on SharePoint lists?**
`Last()` is not delegable for SharePoint in PowerApps, so it only works on the first 500 (or up to 2000) records. `First(SortByColumns(...))` returns the actual latest item regardless of list size.

**2. Can I sort by columns other than ID?**
Yes, sort by any orderable column such as Created, Modified, or a custom date/number field, e.g. `First(SortByColumns(YourList, "Created", Descending))`.

**3. Will this method work with large SharePoint lists?**
Yes. The approach is delegable, so it works efficiently even on lists with thousands of items because sorting and filtering happen on the SharePoint server.

---