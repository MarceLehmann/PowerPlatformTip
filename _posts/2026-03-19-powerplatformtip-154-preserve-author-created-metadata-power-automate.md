---
title: "#PowerPlatformTip 154 – 'Preserve Author, Editor & Dates on Copied SharePoint Files'"
date: 2026-03-19
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - SharePoint
  - REST
  - Metadata
  - HTTP
  - PowerPlatformTip
excerpt: "When you have to copy-and-delete a SharePoint file, it loses its original Created By, Modified By and timestamps. One 'Send an HTTP request to SharePoint' MERGE call restores AuthorId, EditorId, Created and Modified — so the migrated file looks exactly like the original."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

Sometimes a straight *Copy file* isn't possible and you have to recreate a document with *Create file* + *Delete file*. The problem: the new file gets **you** as author, **today** as the created date, and loses the original history.
With a single REST MERGE call you can write the original **AuthorId**, **EditorId**, **Created** and **Modified** values back onto the new item — so the migrated file is indistinguishable from the source.

## 💡 Challenge
You migrate or rebuild files across libraries where *Copy file* won't work (different site, content type change, etc.), so you use *Create file* + *Delete file*.
The recreated item now shows the **flow's identity** as Created By / Modified By and the **current timestamp** as Created / Modified. Audit trails, "sort by newest" and compliance views are all broken.

## ✅ Solution
`Author` and `Editor` are person fields you set via their ID columns **`AuthorId`** and **`EditorId`**; `Created` and `Modified` are date fields you set directly.
Read these values from the source item before deleting it, then write them onto the new item with a **MERGE** request via *Send an HTTP request to SharePoint*. `MERGE` only touches the fields you send, so nothing else changes.

## 🔧 How it's done

1) **Capture the original metadata** before deleting the source.
   🔸 From *Get files (properties)* / *Get item* keep: `Author` (Claims/Email), `Editor`, `Created`, `Modified`.

2) **Resolve the user to a numeric ID.** `AuthorId`/`EditorId` need the site user ID, not the email.
   🔸 *Send an HTTP request to SharePoint* → Method `POST`, Uri:
   ```
   _api/web/ensureuser
   ```
   Header `Content-Type: application/json;odata=verbose`, Body:
   ```json
   { "logonName": "i:0#.f|membership|jane.doe@contoso.com" }
   ```
   🔸 Read the returned `Id` (e.g. `body('Ensure_Author')?['d']?['Id']`). Repeat for the editor.

3) **Get the target library's entity type** once:
   ```
   _api/web/lists/getbytitle('Documents')?$select=ListItemEntityTypeFullName
   ```
   🔸 e.g. `SP.Data.DocumentsItem`.

4) **Add the MERGE request** on the new item.
   🔸 Method `POST`, Uri `_api/web/lists/getbytitle('Documents')/items(ID)`
   🔸 Headers:
   ```
   Accept: application/json;odata=verbose
   Content-Type: application/json;odata=verbose
   IF-MATCH: *
   X-HTTP-Method: MERGE
   ```
   🔸 Body — dates in ISO 8601 UTC:
   ```json
   {
     "__metadata": { "type": "SP.Data.DocumentsItem" },
     "AuthorId": 12,
     "EditorId": 15,
     "Created": "2022-03-14T08:15:00Z",
     "Modified": "2022-06-01T10:42:00Z"
   }
   ```

5) **Run this MERGE last.** Any later write to the item resets `Modified`/`Editor` to now.
   🔸 A `204 No Content` response means the metadata was applied. Verify in the library's *Created* / *Modified* columns.

## 🎉 Result
The recreated file shows the **original** Created By, Modified By, Created and Modified — exactly like the source. Audit trails stay intact, chronological sorting is correct, and compliance views remain trustworthy, even though the file was rebuilt via create-and-delete.

## 🌟 Key Advantages
🔸 **Faithful migration:** original author, editor and timestamps are preserved.
🔸 **Standard action only:** *Send an HTTP request to SharePoint* — no premium connector.
🔸 **Selective by design:** `MERGE` writes only the four metadata fields, leaving everything else untouched.

## 🛠️ FAQ
Q1: Why `AuthorId` instead of `Author`?
A: `Author` and `Editor` are person/lookup fields. Via REST you set them with the numeric site user ID on the `AuthorId` / `EditorId` columns, which you get from `_api/web/ensureuser`.

Q2: What date format do `Created` and `Modified` expect?
A: ISO 8601 in UTC, e.g. `2022-03-14T08:15:00Z`. Convert your source values with `formatDateTime(..., 'yyyy-MM-ddTHH:mm:ssZ')` if needed.

Q3: My Modified date keeps resetting to today — why?
A: Any subsequent update to the item overwrites `Modified` and `Editor`. Make this MERGE the **last** write to the item so your values stick.

Q4: Does this need special permissions?
A: The connection must have permission to write to the library. Setting `Author`/`Editor` requires the account to be able to update those fields (site member/owner-level access).

## 🔗 Related Tips
- [#PowerPlatformTip 153 – Rename a SharePoint File with Power Automate](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-153-rename-sharepoint-file-power-automate/) — the companion rename trick using `FileLeafRef`.
- [#PowerPlatformTip 133 – SharePoint Updates with Power Automate](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-133-sharepoint-updates-with-power-automate-no-required-fields-needed/) — updating only the fields you need.
- [#PowerPlatformTip 47 – Batch-Method within SharePoint](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-47-batch-method-within-sharepoint/) — bulk REST operations for large migrations.
