---
title: "#PowerPlatformTip 131 – 'ForAll & Patch Optimization in PowerApps'"
date: 2025-01-08
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerPlatform
  - SharePoint
  - ForAll
  - Patch
  - Optimization
  - Performance
  - BatchProcessing
  - Bulk Update
excerpt: "Optimize Power Apps performance by using ForAll and Patch for bulk updates—reduce API calls, speed up batch processing, and handle missing IDs efficiently."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Speed up bulk updates in Power Apps by putting `ForAll` inside `Patch` so records update in one batched call.

## 💡 Challenge
Your Power App becomes slow when updating multiple records in SharePoint or other data sources. This often happens when combining `ForAll` and `Patch`, resulting in a high number of API calls. Additionally, if some IDs from the source (e.g., a collection) do not exist in the target data source, **Patch** will create new records for these missing IDs, while updating the existing ones.

## ✅ Solution
Rearrange the logic: swap the position of `ForAll` and `Patch` to enable batch updates. Be aware of the behavior with missing IDs and handle it accordingly if necessary.

## 🔧 How It's Done
Here's how to do it:
1. Review the original formula:  
   🔸 Using `ForAll` wrapped around `Patch`:  
   powerapps
   ForAll(
     GalleryName.AllItems,
     Patch(
       SharePointList,
       LookUp(SharePointList, ID = ThisRecord.ID),
       { Column1: ThisRecord.Column1Input.Text }
     )
   )
   
2. Rearrange for batch updates:  
   🔸 Use `Patch` outside `ForAll`:  
   powerapps
   Patch(
     SharePointList,
     ForAll(
       GalleryName.AllItems,
       {
         ID: ThisRecord.ID,
         Column1: ThisRecord.Column1Input.Text
       }
     )
   )
   
3. Handle missing IDs:  
   🔸 `Patch` creates new records if IDs don’t exist.  
   🔸 Filter out invalid IDs before running `Patch` if you want to avoid unintended creations.

## 🎉 Result
– Faster: updates are processed in a single batch.  
– Handles missing IDs: you can choose to update only existing records or create new ones.  
– Cleaner code: easier to read and maintain.

## 🌟 Key Advantages
🔸 Up to 50% faster updates for large datasets.  
🔸 Flexible handling of missing IDs based on your scenario.  
🔸 Reduced API calls and improved scalability.

---

## 🎥 Video Tutorial
{% include video id="" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why did my Power App become slow when updating multiple records?**  
When combining `ForAll` with `Patch`, each iteration triggers a separate API call. Wrapping `Patch` inside `ForAll` generates many calls, slowing down performance.

**2. How does swapping `ForAll` and `Patch` improve performance?**  
By moving `ForAll` inside `Patch`, Power Apps batches all record updates into a single call, reducing the total number of API calls and speeding up execution.

**3. How can I prevent unintended record creation during `Patch`?**  
Filter your items to only include IDs already in the target data source (e.g., `Filter(GalleryName.AllItems, ID in SharePointList.ID)`) so `Patch` updates existing records only.
