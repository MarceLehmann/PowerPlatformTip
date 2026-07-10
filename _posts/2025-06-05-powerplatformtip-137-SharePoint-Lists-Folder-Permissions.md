---
title: "#PowerPlatformTip 137: 'SharePoint Lists Folder Permissions'"
date: 2025-06-05
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - SharePoint
  - FolderPermissions
  - Permissions
  - ListSettings
  - Security
  - PowerPlatformTip
excerpt: "Enable folder-based permissions in SharePoint lists to streamline access control without building item-by-item Power Automate flows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Enable folders in your SharePoint list's Advanced Settings, create one folder per department, and set permissions at the folder level, every item inside inherits them automatically, with no per-item Power Automate flow needed.

## 💡 Challenge
Teams often need granular, department-specific permissions on list items and end up building elaborate Power Automate flows to assign rights per item, time-consuming and hard to maintain.

## ✅ Solution
Activate the folder feature in your list's Advanced Settings, create one folder per department, and set unique permissions at the folder level so that all contained items inherit them automatically.

## 🔧 How It's Done

**1. Open the list settings**

🔸 In your SharePoint list, click the gear icon → List settings.

**2. Enable folders**

🔸 Select Advanced settings → under Folder, enable "Make 'New Folder' command available" → OK.

**3. Create department folders**

🔸 Back in the list, use **New → Folder** to create one folder per department.

**4. Break inheritance on a folder**

🔸 Click the folder's "…" → Details pane → Manage access → Stop inheriting permissions.

**5. Assign the right access**

🔸 Remove the existing groups and grant the supervisor or department group the appropriate rights.

## 🎉 Result
You now have a folder-based structure where each department's items automatically inherit the correct permissions, no additional flows required, saving setup and maintenance time and improving list performance.

## 🌟 Key Advantages

🔸 Quick setup using built-in list settings (no extra tools needed)

🔸 Automatic inheritance cuts down on manual effort and errors

🔸 Clear separation of access by department

🔸 Scales well for lists up to 100,000 items (beyond that, folder-level breaks in inheritance aren't supported)

---

## 🛠️ FAQ

**Q1: How do I enable folders in a SharePoint list?**

Go to **List settings → Advanced settings**, turn on "Make 'New Folder' command available", and save.

**Q2: Do items inherit folder permissions by default?**

Yes. List items automatically inherit whatever permissions are set on their parent folder.

**Q3: Are there any limits to using folder-based permissions?**

If a folder or list exceeds 100,000 items, you can't break permission inheritance for that folder.

## 🔗 Related Tips
- [#PowerPlatformTip 110: Protect SharePoint Data](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-110-protect-sharepoint-data/), more ways to lock down list and library access.
- [#PowerPlatformTip 74: Elevated Permissions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-74-elevated-permissions/), grant access from a flow when native inheritance isn't enough.
