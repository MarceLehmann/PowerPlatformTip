---
title: "#PowerPlatformTip 151 – 'Manage All Your SharePoint Lists in One Model-Driven App with Virtual Tables'"
date: 2026-02-05
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Dataverse
  - VirtualTables
  - SharePoint
  - ModelDrivenApp
  - PowerPlatformTip
excerpt: "Stop juggling dozens of SharePoint lists across separate views and apps. Dataverse virtual tables expose your production lists in Dataverse without copying data — so you build one model-driven app to manage them all, while SharePoint stays the source of truth."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Surface multiple SharePoint lists as Dataverse virtual tables (no data copied) and manage them all in a single model-driven app — SharePoint stays the source of truth.

Managing lots of productive SharePoint lists means constant tab-hopping: each list has its own view, its own permissions, and building a separate app per list is no fun.
Dataverse **virtual tables** let you surface those lists inside Dataverse **without duplicating data**, so you can build **one model-driven app** to manage them all — with SharePoint still the system of record.

## 💡 Challenge
You run several SharePoint lists in production. Each has a different layout, different permissions, and switching between them feels like tab gymnastics.
Copying everything into Dataverse means data duplication and sync headaches, and building one canvas app per list doesn't scale.

## ✅ Solution
Use the **virtual connector provider for SharePoint** to expose each list as a **virtual table** in Dataverse.
No data is moved — Dataverse connects to the list at runtime — and you get full create, read, update and delete on the records (unless the source forbids it).
Then build a single **model-driven app** on top of those virtual tables to manage everything in one place.

## 🔧 How it's done

**1. Check the prerequisites**

🔸 You need a **Dataverse license** through Power Apps or Dynamics 365 — Microsoft 365 or Teams-only licenses can't create virtual tables.

🔸 The connection must be created by you; connections *shared* with you don't appear in the wizard.

**2. Create the virtual table from a solution**

🔸 In [make.powerapps.com](https://make.powerapps.com), open (or create) an **unmanaged solution**.

🔸 On the command bar choose **New → Table → Virtual table**.

🔸 In the *New table from external data* wizard, add or pick a **SharePoint** connection.

**3. Select your list**

🔸 The provider reads the metadata and lists the available SharePoint lists. Pick the one you want and complete the wizard.

🔸 **One at a time:** bulk creation isn't supported, so repeat step 2–3 for each list you want to manage.

🔸 Each list needs a text column to act as the **Primary Name** column.

**4. Build one model-driven app**

🔸 Create a **model-driven app** and add all your virtual tables to the **site map**, then publish.

🔸 Now every list appears as a normal Dataverse table with grids, forms and views.

**5. Control access with security roles**

🔸 Use Dataverse **security roles** to define who can create, read, update or delete on each virtual table — layered on top of SharePoint permissions.

## 🎉 Result
Instead of hopping between lists or maintaining many apps, you get **one central model-driven app** with a clean Dataverse UI over your existing SharePoint lists.
SharePoint stays the source of truth; you gain the Dataverse experience on top — and when a new list appears, just expose it as another virtual table and it shows up in the app.

## 🌟 Key Advantages

🔸 **No duplication:** data stays in SharePoint, connected at runtime — no sync jobs.

🔸 **One app for many lists:** central management instead of app sprawl.

🔸 **Consistent UX:** uniform grids and forms even if the lists look nothing alike in SharePoint.

🔸 **Governed access:** Dataverse security roles control CRUD per table.

🔸 **Extensible:** add a new list as a virtual table and it instantly appears in the app.

## 🔗 Related Tips
- [#PowerPlatformTip 41 – Standard tables in Dataverse](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-41-standard-tables-in-dataverse/) — when native Dataverse tables are the better fit than virtual ones.
- [#PowerPlatformTip 52 – DV4T: Budget-Friendly Choice](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-52-dv4t-budget-friendly-choice/) — the alternative: actually migrating SharePoint data into Dataverse.

## 🛠️ FAQ

**Q1: Do virtual tables copy my SharePoint data into Dataverse?**

No. Virtual tables connect to the external source at runtime and represent the data as Dataverse records — there's no replication, so SharePoint stays the source of truth.

**Q2: Can I create all my list virtual tables in one go?**

No — bulk creation isn't supported. You create one virtual table per SharePoint list. Once created, they all live in the same model-driven app.

**Q3: Why can't I create a virtual table with my Microsoft 365 license?**

Virtual tables require a Dataverse license via Power Apps or Dynamics 365. Microsoft 365 or Teams licenses can't be used to create them.

**Q4: Do I get full edit rights on the records?**

Yes — virtual tables support full create, read, update and delete unless the underlying source restricts it. You govern who can do what with Dataverse security roles.
