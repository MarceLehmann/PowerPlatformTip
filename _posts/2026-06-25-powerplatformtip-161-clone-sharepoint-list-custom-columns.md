---
title: "#PowerPlatformTip 161: 'Clone a SharePoint List's Custom Columns to Another Site'"
date: 2026-06-25
categories:
  - Article
  - PowerPlatformTip
tags:
  - SharePoint
  - PowerAutomate
  - REST
  - Consulting
  - SchemaXml
  - PowerPlatformTip
excerpt: "Read every column of a SharePoint list via the REST API, filter down to the custom (user-created) fields, and recreate the exact same columns on another site with createfieldasxml - a portable list blueprint for consultants."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** `GET .../fields` returns each column's `SchemaXml`. Filter to custom fields (`Hidden eq false and ReadOnlyField eq false and CanBeDeleted eq true`), then POST that `SchemaXml` to `.../fields/createfieldasxml` on the target list to clone the columns 1:1.

As a consultant you often build a solution on a dev or demo site and then need to reproduce the **exact same list schema** at the customer. Rebuilding columns by hand is slow and error-prone - a single mismatched internal name breaks your Power Apps and flows. SharePoint already stores every column as XML, so you can read that blueprint from one list and stamp it onto another, fully automated.

## 💡 Challenge
You have a working SharePoint list with a dozen carefully configured columns (choice, lookup, calculated, formatted). You need the identical columns - same internal names, same settings - on a different site or tenant. Manually recreating them is tedious and drifts easily, which later breaks apps and flows that rely on those exact internal names.

## ✅ Solution
Every SharePoint field exposes a `SchemaXml` property - the complete definition of that column. The plan is: **read** all fields of the source list, **filter** to the ones you actually created (excluding built-in/system columns), and **recreate** each one on the target list by posting its `SchemaXml` to `createfieldasxml`. Everything runs through the standard *Send an HTTP request to SharePoint* action - no premium connector.

## 🔧 How it's done

**1. Read all columns of the source list and keep only the custom ones.**

🔸 *Send an HTTP request to SharePoint* (source site) → Method `GET`, Uri:

```
_api/web/lists/getbytitle('Projects')/fields?$select=Title,InternalName,Hidden,ReadOnlyField,CanBeDeleted,FromBaseType,SchemaXml&$filter=Hidden eq false and ReadOnlyField eq false and CanBeDeleted eq true and FromBaseType eq false
```

🔸 Header `Accept: application/json;odata=nometadata`. The `$filter` strips out system columns: built-in fields have `CanBeDeleted = false` and `FromBaseType = true`, while the columns *you* added come back with `CanBeDeleted = true` and `FromBaseType = false`. The response `value` array now holds only your custom columns, each with its full `SchemaXml`.

**2. (Optional) Inspect / store the blueprint.**

🔸 The array of `SchemaXml` strings *is* your portable list definition. Save it to a variable, a file, or a config list so you can redeploy it anytime - this is the reusable asset for the next customer.

**3. Loop the results and recreate each column on the target list.**

🔸 *Apply to each* over the returned `value` array. Inside, add a *Send an HTTP request to SharePoint* (target site) → Method `POST`, Uri:

```
_api/web/lists/getbytitle('Projects')/fields/createfieldasxml
```

🔸 Headers `Accept: application/json;odata=nometadata`, `Content-Type: application/json;odata=verbose`, Body:

```json
{
  "parameters": {
    "__metadata": { "type": "SP.XmlSchemaFieldCreationInformation" },
    "SchemaXml": "@{items('Apply_to_each')?['SchemaXml']}",
    "Options": 24
  }
}
```

🔸 `Options` is a bitwise `AddFieldOptions` value: `AddFieldInternalNameHint (8)` preserves the original internal name carried in the `SchemaXml`, and `AddFieldToDefaultView (16)` adds the column to the default view - `8 + 16 = 24`. Other flags: `AddToDefaultContentType = 1`, `AddToAllContentTypes = 4`, `AddFieldCheckDisplayName = 32`. Use `0` for defaults only.

**4. Create the target list first (if it doesn't exist yet).**

🔸 One-time POST to `_api/web/lists` with a `SP.List` body (`BaseTemplate: 100` for a generic list) before the loop, so the columns have somewhere to land.

## 🎉 Result
The target list ends up with the same custom columns as the source - identical internal names and settings - created automatically. Your Power Apps and flows that reference those internal names keep working unchanged, and you have a reusable schema blueprint to deploy the solution at the next customer in minutes instead of hours.

## 🌟 Key Advantages

🔸 **Portable blueprint:** the `SchemaXml` array is a self-contained list definition you can version, store, and redeploy anywhere.

🔸 **Exact fidelity:** internal names and column settings are cloned 1:1, so downstream apps and flows don't break.

🔸 **Standard action only:** *Send an HTTP request to SharePoint* - no premium connector, fully automatable.

🔸 **Consultant-friendly:** turn a one-off build into a repeatable deployment asset across sites and tenants.

## 🛠️ FAQ

**Q1: How do I reliably tell custom columns from built-in ones?**

Built-in/system columns come back with `CanBeDeleted = false` and usually `FromBaseType = true`. Columns you created have `CanBeDeleted = true` and `FromBaseType = false`. Combine both in the `$filter` (plus `Hidden eq false` and `ReadOnlyField eq false`) to isolate exactly the fields you added.

**Q2: Do lookup columns clone cleanly?**

Lookup fields reference a target list by ID (`List="{GUID}"` inside the `SchemaXml`), and that GUID differs on the new site. Create the referenced list first, then fix up the `List` (and `WebId`) attributes in the `SchemaXml` before posting - or recreate lookups in a dedicated second pass once all base lists exist.

**Q3: What if a column with that internal name already exists on the target?**

`createfieldasxml` will fail on a duplicate internal name. Either target a fresh list, or GET the target's fields first and skip any `InternalName` that already exists so the flow is safely re-runnable.

**Q4: Can I do this without Power Automate?**

Yes - the same REST endpoints work from PnP PowerShell (`Get-PnPField` / `Add-PnPFieldFromXml`) or CSOM (`AddFieldAsXml(schemaXml, addToDefaultView, options)`). The flow approach just keeps it low-code and auth-free.

## 🔗 Related Tips
- [#PowerPlatformTip 47: Batch Requests](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-47-batch-requests/), send many field-creation calls in a single request for faster provisioning.
- [#PowerPlatformTip 95: Optimized SharePoint Queries](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-95-optimized-sharepoint-queries/), get more out of `$select` and `$filter` on the SharePoint REST API.
- [#PowerPlatformTip 123: Work with SharePoint IDs](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-123-sharepoint-ids/), understand the IDs and GUIDs you'll remap when cloning lookups.
