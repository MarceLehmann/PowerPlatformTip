---
title: "#PowerPlatformTip 147 – Dummy Patch After Complex Flows"
date: 2025-12-18
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - PowerAutomate
  - Dataverse
  - SharePoint
  - Performance
  - PowerPlatformTip
excerpt: "Complex Flows with approvals/fallbacks updating lists? Use Dummy Patch on GalleryExample.selected + RefreshHack column for precise single-record refresh – skips Refresh bulk loads."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Force a single-record cache refresh in Power Apps after a complex flow by dummy-patching a hidden RefreshHack column on the selected record.

Some scenarios need Power Automate for advanced logic – conditional data, external API calls, error fallbacks, multi-record lookups, tracking. The flow finishes and responds to Power Apps, but your Gallery or EditForm still shows *pre-flow* data. A full `Refresh` would download 500-2000 records (delegation limit), wasting bandwidth even when filtered. The fix: a hidden *RefreshHack* column plus a Dummy Patch on the selected record for a single-record cache refresh.

## 💡 Challenge
Canvas `Patch` handles simple updates automatically, but complex logic needs flows. Real scenario: user submits a form → flow validates/approves → updates SharePoint → the app's cache is blind, so the Gallery shows stale data.

## ✅ Solution
Create a hidden `RefreshHack` (single line of text) column and `Patch` it with `Blank()` on the selected record right after the flow completes.

## 🔧 How It's Done

**1. Set up the RefreshHack column**

🔸 In your SharePoint/Dataverse list, add a new "RefreshHack" column (single line of text).

🔸 Hide it from all views and forms (no user impact).

🔸 It's a safe dummy field for cache invalidation — never used in formulas.

**2. Trigger the flow, then dummy-patch**

🔸 On your Gallery → EditForm/Button OnSelect, run the complex flow:

```powerapps
Set(varFlowID, ComplexFlow.Run(GalleryExample.Selected.ID))
```

🔸 On success, patch the hidden column on the selected record:

```powerapps
If(
    varFlowID.Success,
    Patch(
        MySharePointList,
        GalleryExample.Selected,
        { RefreshHack: Blank() }
    );
    Notify("Update complete!", NotificationType.Success)
)
```

**3. What happens**

🔸 The flow runs its full logic (Switch conditions, HTTP fallback, etc.).

🔸 The Patch signals "this record changed" → Power Apps invalidates *only* that cache entry.

🔸 The Gallery/Form reloads fresh data for that record. Check F12 > Network: ~1KB payload vs. Refresh's 50KB+.

## 🎉 Result
Complex enterprise flows get precise, instant sync without app slowdown or delegation warnings — and it scales to 50k+ lists.

## 🌟 Key Advantages

🔸 **Precise targeting:** `GalleryExample.Selected` hits the right record.

🔸 **No bulk data:** beats Refresh performance dramatically on large lists.

🔸 **Delegation-proof:** a single Patch, no warnings.

🔸 **Mobile-friendly:** low bandwidth, critical for field users.

---

## 🎥 Video Tutorial
{% include video id="Rj6Q_oF7jLw" provider="youtube" %}

---

## 🛠️ FAQ
**1. Why the RefreshHack column specifically?**
A single-line text column is lightweight. Patching it with `Blank()` forces revalidation without any business impact.

**2. Is direct Patch enough for simple cases?**
Yes — it auto-caches. Use flows only for complex/enterprise logic.

**3. Does it work mid-Gallery scroll?**
Yes — the selected record refreshes in place.

---