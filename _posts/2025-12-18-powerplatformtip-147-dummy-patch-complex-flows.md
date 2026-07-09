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

**When direct Patch fails**: Use Power Automate for advanced scenarios – conditional data, external API calls, error fallbacks, multi-record lookups, tracking.  
Flow finishes → Respond to PowerApps → but your Gallery or EditForm still shows *pre-Flow* data.  
Why not use Refresh? Downloads 500-2000 records (delegation limit), wasting bandwidth even if filtered.

**The fix**: Add *RefreshHack* column → Dummy Patch on `GalleryExample.selected` → single-record cache refresh.

## 💡 Challenge
Canvas Patch handles simple updates automatically. Complex logic requires Flows.  
Real scenario: User submits form → Flow validates/approves → updates SharePoint → App cache blind = stale display in Gallery.

## ✅ Solution
Create RefreshHack (hidden Single line of text column). Patch it with Blank() on the selected record post-Flow.

## 🔧 How it’s done

1) **Setup RefreshHack column**:  
   - In SharePoint/Dataverse list: New column "RefreshHack" (Single line of text).  
   - Hide from all views/forms (no user impact).  
   - Purpose: Safe dummy field for cache invalidation (never used in formulas).

2) **App flow**: Gallery → EditForm/Button OnSelect.

- a) Trigger complex Flow  
  Set(varFlowID, ComplexFlow.Run(GalleryExample.selected.ID));

- b) Wait for success + Dummy Patch  
  If(
    varFlowID.Success,
    Patch(
      MySharePointList,
      GalleryExample.Selected,
      { RefreshHack: Blank() }
    );
    Notify("Update complete!", NotificationType.Success)
  )

3) **What happens**:  
   - Flow runs full logic (Switch conditions, HTTP fallback, etc.).  
   - Patch signals "this record changed" → PowerApps invalidates *only* that cache entry.  
   - Gallery/Form reloads fresh data from source.  
   *Test*: Browser F12 > Network – see ~1KB payload vs Refresh's 50KB+.

## 🎉 Result
Complex enterprise Flows → precise, instant sync without app slowdown or delegation warnings. Scales to 50k+ lists.

## 🌟 Key Advantages
🔸 **Precise targeting**: GalleryExample.selected ensures right record.  
🔸 **No bulk data**: Beats Refresh performance by 500x on large lists.  
🔸 **Delegation-proof**: Single Patch, no warnings.  
🔸 **Mobile-friendly**: Low bandwidth critical for field users.

## 🎥 Video Tutorial
{% include video id="Rj6Q_oF7jLw" provider="youtube" %}

## 🛠️ FAQ
Q1: Why RefreshHack column specifically?  
A: Single-line text = lightweight. Blank() forces revalidation without business impact.

Q2: Direct Patch enough for simple cases?  
A: Yes – auto-caches. Flows only for complex/enterprise logic.

Q3: Does it work mid-Gallery scroll?  
A: Yes – selected record refreshes in place.
