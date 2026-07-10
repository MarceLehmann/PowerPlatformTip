---
title: "#PowerPlatformTip 123 – 'Get Lowest / Highest SharePoint ID & TotalCount'"
seo_title: "#PowerPlatformTip 123 – 'Get Lowest / Highest SharePoint ID'"
date: 2024-09-11
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - SharePoint
  - ListAnalytics
  - REST
  - PowerPlatformTip
excerpt: "Efficiently retrieve the highest, lowest, and total item IDs from a SharePoint list in Power Automate for advanced list analytics and data management."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Get the lowest ID, highest ID and total count of a SharePoint list in Power Automate with three simple `$orderby`/`ItemCount` REST calls.

## 💡 Challenge
You need the highest, lowest, and total count of item IDs in a SharePoint list — to build reports, paginate, or manage data more efficiently — without scanning the whole list.

## ✅ Solution
Use three small HTTP requests against the SharePoint REST API to fetch the lowest ID, the highest ID and the total item count directly.

## 🔧 How It's Done

**1. Get the lowest ID**

🔸 Send an HTTP GET to the SharePoint API:
`/_api/Web/Lists/GetByTitle('YourListName')/Items?$select=ID&$filter=ID gt 0&$top=1&$orderby=ID asc`

🔸 Set the method to GET and the header `accept: application/json; odata=nometadata`.

**2. Get the highest ID**

🔸 Same request, ordered descending:
`/_api/Web/Lists/GetByTitle('YourListName')/Items?$select=ID&$filter=ID gt 0&$top=1&$orderby=ID desc`

🔸 Use the same method and headers.

**3. Get the total item count**

🔸 Call the ItemCount endpoint:
`/_api/Web/Lists/GetByTitle('YourListName')/ItemCount`

🔸 Again use GET with the same headers.

## 🎉 Result
You get the lowest, highest, and total count of IDs in your SharePoint list in seconds – perfect for reports and data analysis.

## 🌟 Key Advantages

🔸 Automated and fast data retrieval

🔸 Simplifies management of large lists

🔸 No manual searching required

---

## 🎥 Video Tutorial
{% include video id="ITOWKQI8B_Q" provider="youtube" %}

---

## 🛠️ FAQ
**1. Do I need any special permissions to run these HTTP requests?**
You need at least read permissions on the SharePoint list to retrieve IDs and item counts via the API. Ensure your connection in Power Automate has the appropriate access.

**2. Can this approach handle large lists with more than 5,000 items?**
Yes. Retrieving the lowest or highest ID with `$top=1` is efficient, but be aware of list view thresholds when filtering larger datasets. For total count, the `ItemCount` endpoint stays performant.

**3. How can I adapt this to retrieve other columns or values?**
Adjust the `$select` and `$orderby` query parameters to include the desired fields (e.g., `Title`) and order by those columns as needed.

## 🔗 Related Tips
- [#PowerPlatformTip 97 – Enhanced Pagination](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-97-enhanced-pagination/) — handle large SharePoint result sets efficiently.
- [#PowerPlatformTip 95 – Optimized SharePoint Queries](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-95-optimized-sharepoint-queries/) — build fast, delegable list queries.
