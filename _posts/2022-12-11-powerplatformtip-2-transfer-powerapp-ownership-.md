---
title: "#PowerPlatformTip 2: 'Transfer PowerApp Ownership'"
date: 2022-12-11
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerapps
  - ownership
  - admin
  - governance
  - coe-toolkit
excerpt: "Transfer Power Apps ownership after a maker leaves, using the CoE Starter Kit admin apps or the Set-AdminPowerAppOwner PowerShell cmdlet. Keep apps governed and running."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Reassign a departed maker's Power Apps via the CoE Starter Kit admin apps or the `Set-AdminPowerAppOwner` PowerShell cmdlet for clean, bulk ownership transfer.

## 💡 Challenge
When a maker leaves the company, the apps they own can become orphaned, and reassigning ownership through the maker UI one by one is slow and easy to miss. You need a reliable, admin-friendly way to hand over Power Apps ownership.

## ✅ Solution
Use an admin approach instead of the maker UI: either the **CoE Starter Kit** admin apps (for a governed, low-code experience) or the **`Set-AdminPowerAppOwner`** cmdlet from the *Microsoft.PowerApps.Administration.PowerShell* module for scripted, bulk changes.

## 🔧 How It's Done

**1. Choose your tool**

🔸 For a UI: deploy the [CoE Starter Kit](https://aka.ms/CoEStarterKitRepo) and use its admin apps to inventory and manage app ownership.

🔸 For scripting / bulk: install the `Microsoft.PowerApps.Administration.PowerShell` module.

**2. Set the new owner via PowerShell**

🔸 Run `Set-AdminPowerAppOwner -AppName <AppId> -EnvironmentName <EnvId> -AppOwner <UserObjectId>`.

🔸 Loop over multiple apps to reassign them in bulk.

**3. Verify the result**

🔸 Confirm the new owner in the Power Platform admin center or maker portal.

## 🎉 Result
Ownership is reassigned cleanly, no orphaned apps, no manual clicking through each app. Admins keep full control and governance stays intact.

## 🌟 Key Advantages

🔸 **Admin-grade:** Works even when you're not the current owner, using admin permissions.

🔸 **Scales:** Script bulk reassignments across many apps at once.

🔸 **Governed:** Fits into a CoE / governance process for departing makers.

---

## 🛠️ FAQ

**1. Can I reassign ownership of multiple apps at once?**

Yes, wrap `Set-AdminPowerAppOwner` in a PowerShell loop to reassign many apps programmatically.

**2. Do I need admin privileges?**

Yes. You need a Power Platform / environment admin (or Global admin) role to change ownership for apps you don't own.

**3. What happens to the previous owner?**

`Set-AdminPowerAppOwner` sets the new owner and changes the previous owner to the "Can View" role, they keep read access but no longer own the app. App data and connections remain intact.
