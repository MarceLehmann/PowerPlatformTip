---
title: "#PowerPlatformTip 121 – 'Filtering SharePoint File Fields with OData'"
date: 2024-08-21
modified: 2025-10-15
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - SharePoint
  - OData
  - FileLeafRef
  - FileRef
  - FileDirRef
  - PowerPlatformTip
excerpt: "Quickly and efficiently filter SharePoint files in Power Automate by using FileLeafRef (file name), FileRef (full path), and FileDirRef (folder) fields with simple OData filter expressions – even if you don’t know how these fields work yet."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Quickly and efficiently filter SharePoint files in Power Automate by using FileLeafRef (file name), FileRef (full path), and FileDirRef (folder) fields with simple OData filter expressions – even if you don’t know how these fields work yet.

## 💡 Challenge
Managing complex workflows in Power Platform can be difficult without the right approach to Filtering SharePoint File Fields with OData. Many developers find themselves struggling with efficiency and manual configuration.

## ✅ Solution
By implementing Filtering SharePoint File Fields with OData, you can automate repetitive tasks and simplify your application logic. This feature provides a native way to handle data more effectively.

## 🔧 How It's Done
* **FileLeafRef**: Filter by specific file names without the path.
* **FileLeafRef**: Filter by specific file names without the path.
* **FileRef**: Filter by the full path to a file.
* **FileDirRef**: Filter by files within a specific directory.
This approach is particularly useful for optimizing your SharePoint queries, as discussed in my other tip [#PowerPlatformTip 95 – ‘Optimized SharePoint Queries’, which focused on efficient query design.

## 🎉 Result
Your workflows become more robust and easier to maintain. Implementing Filtering SharePoint File Fields with OData reduces the time spent on manual adjustments and minimizes potential for errors.

## 🌟 Key Advantages
🔸 Improved Efficiency: Faster development cycles through automation.
🔸 Better Consistency: Standardized approach across all projects.
🔸 Enhanced Reliability: Reduced risk of failure during execution.

## 🎥 Video Tutorial
{% include video id="2DmwfItne0Q" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I apply these OData filters in Power Automate?**  
In the "Get files (properties only)" action, enter your OData filter expression into the **Filter Query** field to limit results based on FileLeafRef, FileRef, or FileDirRef.

**2. Can I combine multiple OData filter conditions?**  
Yes. Use logical operators like `and` or `or` in your filter query, for example:  
`FileLeafRef eq 'document.pdf' and startswith(FileDirRef, '/sites/demo/Shared Documents')`.

**3. Are these fields supported in SharePoint on-premises?**  
OData filtering with FileLeafRef, FileRef, and FileDirRef works in SharePoint Online and on-premises (2013+). Ensure your environment and connector version support OData queries.

**4: What does FileLeafRef mean?**  
It's the file name itself – for example, 'Invoice.pdf'.

**5: What does FileRef mean?**  
It's the full path of a file, including folders – for example, '/sites/demo/Shared Documents/Invoice.pdf'.

**6: What does FileDirRef mean?**  
It refers to a folder path only. Example: '/sites/demo/Shared Documents/'.