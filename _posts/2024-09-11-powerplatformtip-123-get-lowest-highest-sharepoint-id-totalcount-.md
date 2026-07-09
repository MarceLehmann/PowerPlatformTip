---

title: "#PowerPlatformTip 123 – 'Get Lowest / Highest SharePoint ID & TotalCount'"
seo_title: "#PowerPlatformTip 123 – 'Get Lowest / Highest SharePoint ID"
date: 2024-09-11
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Marcel Lehmann
  - PowerAutomate
  - PowerPlatform
  - PowerPlatformTip
  - SharePoint
  - List Analytics
excerpt: "Efficiently retrieve the highest, lowest, and total item IDs from a SharePoint list in Power Automate for advanced list analytics and data management."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true

---

> **TL;DR:** Get the lowest ID, highest ID and total count of a SharePoint list in Power Automate with three simple `$orderby`/`ItemCount` REST calls.

## 💡 Challenge
Need to fetch the highest, lowest, and total count of IDs in a SharePoint list to manage your data more efficiently?

## ✅ Solution
Use Power Automate to quickly retrieve the highest, lowest, and total count of IDs in your SharePoint list without having to perform manual queries.

## 🔧 How It's Done
Here's how to do it:
1. Get Lowest ID  
   🔸 Use an HTTP GET request to the SharePoint API with the URL:  
     `/_api/Web/Lists/GetByTitle('YourListName')/Items?$select=ID&$filter=ID gt 0&$top=1&$orderby=ID asc`  
   🔸 Set the method to "GET" and the headers to `accept: application/json; odata=nometadata`.
2. Get Highest ID  
   🔸 Use an HTTP GET request to the SharePoint API with the URL:  
     `/_api/Web/Lists/GetByTitle('YourListName')/Items?$select=ID&$filter=ID gt 0&$top=1&$orderby=ID desc`  
   🔸 Use the same method and headers as for the lowest ID.
3. Get Total Item Count  
   🔸 Use an HTTP GET request to the SharePoint API with the URL:  
     `/_api/Web/Lists/GetByTitle('YourListName')/ItemCount`  
   🔸 Again, set the method to "GET" and use the same headers.

## 🎉 Result
These steps will provide you with the lowest, highest, and total count of IDs in your SharePoint list quickly – perfect for reports and data analysis!

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
Yes. Retrieving the lowest or highest ID with `$top=1` is efficient, but be aware of list view thresholds when filtering larger datasets. For total count, the `ItemCount` endpoint remains performant.

**3. How can I adapt this to retrieve other columns or values?**  
Simply adjust the `$select` and `$orderby` query parameters to include the desired fields (e.g., `Title`) and order by those columns as needed.
