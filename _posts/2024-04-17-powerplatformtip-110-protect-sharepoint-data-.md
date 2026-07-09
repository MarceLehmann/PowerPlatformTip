---
title: "#PowerPlatformTip 110 – 'Protect SharePoint Data'"
date: 2024-04-17
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - SharePoint
  - PowerApps
  - Security
  - Permissions
  - PowerPlatformTip
excerpt: "Use a SharePoint custom permission level to block direct access to lists and enforce interactions through Power Apps for improved data security."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Create a custom SharePoint permission level without 'View Application Pages' to force users through your Power App and block direct list access.

## 💡 Challenge
How do you make sure users work with SharePoint data strictly through Power Apps, preventing direct access and the data-integrity issues that come with it?

## ✅ Solution
Create a custom SharePoint permission level that removes **View Application Pages**. Users in that group can still read and write data through Power Apps, but can't open the SharePoint lists directly.

## 🔧 How It's Done

**1. Create a custom permission level**

🔸 Go to **Site Permissions → Permission Levels**.

🔸 Open the **Contribute** level and click **Copy Permission Level**.

🔸 Name it “Power Apps – Custom Permission” and add a description.

🔸 Under **List Permissions**, uncheck **View Application Pages**.

🔸 Click **Create**.

**2. Assign it to a new group**

🔸 In **Site Permissions**, click **Create Group**.

🔸 Name it (e.g. “Power App Users”) and set an owner if desired.

🔸 Select the custom permission level you just created, then click **Create**.

**3. Add users**

🔸 Add users to the “Power App Users” group. They now work with the data through your Power App, without direct GUI access to the SharePoint lists or application pages.

## 🎉 Result
Power Apps users' access is deliberately limited: interactions are routed through the app, and users can't open SharePoint lists via the GUI — aligning with best practices for data integrity and security.

## 🌟 Key Advantages

🔸 **Data security:** restricts direct access to SharePoint data, routing it through Power Apps.

🔸 **Controlled access:** administrators fine-tune permissions to fit operational needs.

🔸 **Flexibility:** keep SharePoint as the data source while enforcing strict access control.

---

## 🎥 Video Tutorial
{% include video id="rcdSfqokvXk" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I remove or modify the custom permission level?**
Go to **Site Permissions → Permission Levels**, select “Power Apps – Custom Permission,” and edit or delete it as needed.

**2. Will this affect other users' access to application pages?**
Only users in the custom group lose the **View Application Pages** right. Users with default or elevated permissions are unaffected.

**3. Can this approach be applied to document libraries and other list types?**
Yes — assign the custom permission level to any SharePoint list or library to extend the same protection.

---