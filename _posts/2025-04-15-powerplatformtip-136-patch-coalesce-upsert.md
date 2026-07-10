---
title: "#PowerPlatformTip 136: 'Patch Coalesce Upsert'"
date: 2025-04-15
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Patch
  - Coalesce
  - Upsert
  - BestPractices
  - PowerPlatformTip
excerpt: "Learn how to use Patch() with Coalesce() in Power Apps to perform creates and updates in a single call, simplifying your code."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Do upsert in Power Apps with one `Patch(Source, Coalesce(LookUp(...), Defaults(Source)), {...})`, update or create in a single call.

## 💡 Challenge
In Power Apps, keeping separate logic branches for "Create" and "Update" bloats your formulas and invites bugs. How can you fold this into a single operation?

## ✅ Solution
Use a single `Patch()` call combined with `Coalesce()`. If `LookUp()` finds no record, `Coalesce()` falls back to `Defaults(DataSource)`, so the same call either updates an existing record or creates a new one.

## 🔧 How It's Done

**1. Define your data source**

🔸 Make sure you have a table or collection connection, e.g. `Contacts`.

**2. Retrieve any existing record**

🔸 `varRecord = LookUp(Contacts, Email = varEmail)`, returns the record if it exists, otherwise Blank.

**3. Patch with Coalesce**

🔸 Combine `Patch()` and `Coalesce()`:

```powerapps
Patch(
    Contacts,
    Coalesce(
        varRecord,
        Defaults(Contacts)
    ),
    {
        Email: varEmail,
        FullName: txtName.Text,
        Phone: txtPhone.Text
    }
)
```

🔸 `Coalesce(varRecord, Defaults(Contacts))` uses the Defaults template when `varRecord` is Blank, creating a new record.

**4. Publish and test**

🔸 If a matching record exists it's updated; otherwise a new record is created with your field values.

## 🎉 Result
You've consolidated two code paths into one: cleaner form logic, easier to maintain and less error-prone. "Upsert" (update or insert) now happens seamlessly with a single `Patch()`.

## 🌟 Key Advantages

🔸 One unified call instead of separate Create/Update branches

🔸 No extra variables or `If()` checks needed

🔸 Cleaner maintenance and improved performance

🔸 Consistent behavior across SharePoint, Dataverse, or any Power Apps data source

---

## 🛠️ FAQ
**1. Do I still need `If()` conditions to check for existing records?**
`Coalesce()` handles the check for you. If `LookUp()` returns Blank, it automatically uses `Defaults()`, so `If()` is unnecessary.

**2. Will this approach work with Dataverse tables?**
Yes. Both `Patch()` and `Coalesce()` behave identically in Dataverse. Just replace `Contacts` with your table name (e.g. `Accounts`).

**3. What if `LookUp()` returns more than one record?**
Make your lookup criteria unique (for example, a primary key or unique field). Otherwise `LookUp()` returns the first match and may lead to unexpected updates.

## 🔗 Related Tips
- [#PowerPlatformTip 131: ForAll & Patch Optimization in PowerApps](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-131-forall-patch-optimization-in-powerapps/), batch bulk updates efficiently.
- [#PowerPlatformTip 57: Mastering Patch](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-57-mastering-patch/), the core Patch patterns.
