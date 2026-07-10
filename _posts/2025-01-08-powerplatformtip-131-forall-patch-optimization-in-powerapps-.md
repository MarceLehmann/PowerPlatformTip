---
title: "#PowerPlatformTip 131: 'ForAll & Patch Optimization in PowerApps'"
seo_title: "Power Apps ForAll + Patch: Faster Bulk Updates"
date: 2025-01-08
last_modified_at: 2026-07-10
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - SharePoint
  - ForAll
  - Patch
  - Performance
  - BatchProcessing
  - PowerPlatformTip
excerpt: "Optimize Power Apps performance by using ForAll and Patch for bulk updates, reduce API calls, speed up batch processing, and handle missing IDs efficiently."
description: "Speed up bulk updates in Power Apps by nesting ForAll inside Patch, cut API calls, batch record updates, and handle missing IDs. Up to 50% faster."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
faq:
  - question: "Why did my Power App become slow when updating multiple records?"
    answer: "When you wrap Patch inside ForAll, each iteration triggers a separate API call. Many records means many calls, which slows performance."
  - question: "How does swapping ForAll and Patch improve performance?"
    answer: "Moving ForAll inside Patch batches all record updates into a single call, reducing the total number of API calls and speeding up execution."
  - question: "How can I prevent unintended record creation during Patch?"
    answer: "Filter your items to only include IDs already in the target data source (e.g. Filter(GalleryName.AllItems, ID in SharePointList.ID)) so Patch updates existing records only."
howto:
  name: "How to optimize bulk updates with ForAll and Patch in Power Apps"
  steps:
    - name: "Review the original formula"
      text: "ForAll wrapped around Patch, one call per record."
    - name: "Rearrange for batch updates"
      text: "Put ForAll inside a single Patch."
    - name: "Handle missing IDs"
      text: "Patch creates new records if IDs don't exist. Filter out invalid IDs before running Patch if you want to avoid unintended creations."
---

> **TL;DR:** Speed up bulk updates in Power Apps by putting `ForAll` inside `Patch` so records update in one batched call.

## 💡 Challenge
Your Power App slows down when updating many records in SharePoint or another data source. This usually happens when you wrap `Patch` inside `ForAll`, producing one API call per record. And if some source IDs don't exist in the target, `Patch` creates new records for them while updating the existing ones.

## ✅ Solution
Rearrange the logic: move `ForAll` *inside* `Patch` to enable a batched update. Just be aware of the missing-ID behavior and handle it if needed.

## 🔧 How It's Done

**1. Review the original formula**

🔸 `ForAll` wrapped around `Patch`, one call per record:

```powerapps
ForAll(
    GalleryName.AllItems,
    Patch(
        SharePointList,
        LookUp(SharePointList, ID = ThisRecord.ID),
        { Column1: ThisRecord.Column1Input.Text }
    )
)
```

**2. Rearrange for batch updates**

🔸 Put `ForAll` inside a single `Patch`:

```powerapps
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
```

**3. Handle missing IDs**

🔸 `Patch` creates new records if IDs don't exist.

🔸 Filter out invalid IDs before running `Patch` if you want to avoid unintended creations.

## 🎉 Result

🔸 **Faster:** updates are processed in a single batch.

🔸 **Handles missing IDs:** update only existing records, or create new ones, your choice.

🔸 **Cleaner code:** easier to read and maintain.

## 🌟 Key Advantages

🔸 Up to 50% faster updates for large datasets.

🔸 Flexible handling of missing IDs based on your scenario.

🔸 Reduced API calls and improved scalability.

---

## 🛠️ FAQ
**1. Why did my Power App become slow when updating multiple records?**
When you wrap `Patch` inside `ForAll`, each iteration triggers a separate API call. Many records means many calls, which slows performance.

**2. How does swapping `ForAll` and `Patch` improve performance?**
Moving `ForAll` inside `Patch` batches all record updates into a single call, reducing the total number of API calls and speeding up execution.

**3. How can I prevent unintended record creation during `Patch`?**
Filter your items to only include IDs already in the target data source (e.g. `Filter(GalleryName.AllItems, ID in SharePointList.ID)`) so `Patch` updates existing records only.

## 🔗 Related Tips
- [#PowerPlatformTip 57: Mastering Patch](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-57-mastering-patch/), the fundamentals behind bulk Patch operations.
- [#PowerPlatformTip 81: Fast DataSource Updates](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-81-fast-datasource-updates/), more ways to speed up data writes.
