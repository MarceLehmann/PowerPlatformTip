---
title: "#PowerPlatformTip 20 – 'Change Flow-Owner'"
date: 2023-01-17
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - flow-owner
  - permissions
  - solutions
  - automation
  - PowerPlatformTip
excerpt: "Change a Power Automate flow owner in place by making it solution-aware. Avoid export/import and keep all connections and run history intact."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

You can't change the owner of a plain (non-solution) cloud flow in place — the owner is part of the flow's identity, so you'd normally have to export and re-import.
The clean way is to make the flow **solution-aware**, then reassign the owner directly from its **Details**.

## 💡 Challenge
For a non-solution flow there's no in-place "change owner" option. Working around it with export, permission changes and re-import is slow and error-prone.

## ✅ Solution
Add the flow to a **solution** (in a Dataverse-enabled environment), which unlocks in-place ownership changes via **Details → Edit → Owner**.

## 🔧 How it's done

**1. Make the flow solution-aware**

🔸 In [make.powerautomate.com](https://make.powerautomate.com), add the flow to a solution (or create it inside one).

**2. Open the flow details**

🔸 Select the flow, then in the **Details** section choose **Edit**.

**3. Set the new owner**

🔸 In the **Owner** section, add the new owner. The original owner and the new owner become **co-owners**, so nothing breaks.

**4. Refresh the license (if needed)**

🔸 For scheduled or automated flows, the new owner's license takes effect within about 7 days — edit and re-save the flow to apply it immediately.

## 🎉 Result
Ownership transfers without export/import, and all connection references and run history stay intact — no downtime.

## 🌟 Key Advantages

🔸 **In-place change:** no export/import round trip.

🔸 **History preserved:** connections and run history carry over.

🔸 **Business continuity:** owner and new owner become co-owners, avoiding permission gaps.

---

## 🛠️ FAQ

**Q1: Can I change ownership of flows that use premium connectors?**

Yes, but the new owner needs the appropriate licenses for any premium connectors. Without a premium license, the flow keeps running for a grace period before being turned off.

**Q2: What happens to the flow's run history when ownership changes?**

The complete run history stays intact and accessible to the new owner.

**Q3: Do I need special permissions to change flow ownership?**

Yes — you must be the current owner, a co-owner, or an environment admin.
