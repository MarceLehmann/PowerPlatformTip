---
title: "#PowerPlatformTip 153 – 'Rename a SharePoint File with Power Automate'"
date: 2026-03-05
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - SharePoint
  - REST
  - FileLeafRef
  - HTTP
  - PowerPlatformTip
excerpt: "The SharePoint connector has no 'Rename file' action — but you don't need one. A single 'Send an HTTP request to SharePoint' call that MERGEs the FileLeafRef field renames any document in place, keeping its ID, version history and metadata intact."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

There's no native "Rename file" action in the SharePoint connector, so people copy-and-delete files — losing the item ID, version history and metadata in the process.
The clean way is a single REST call: update the item's **`FileLeafRef`** field with a **MERGE** request via *Send an HTTP request to SharePoint*. The file keeps its ID, versions and permissions — only the name changes.

## 💡 Challenge
You need to rename a document in a SharePoint library from a flow — for example to enforce a naming convention or add a reference number.
The standard connector only offers *Copy file* / *Delete file*, which breaks the item ID, resets version history and drops metadata. You want a true in-place rename.

## ✅ Solution
`FileLeafRef` is the internal field that holds the **file name including its extension**. Updating it renames the file in place.
Use the **Send an HTTP request to SharePoint** action with a **MERGE** request against the list item. The item ID, versions, permissions and all other metadata stay untouched.

## 🔧 How it's done

**1. Get the item's ID and the library's entity type.**

🔸 You need the numeric list item **ID** (from *Get files (properties)*, a trigger, or *Get item*).

🔸 Get the exact `__metadata` type once with a GET request:

```
_api/web/lists/getbytitle('Draft Standards')?$select=ListItemEntityTypeFullName
```

🔸 For a library named "Draft Standards" the value is `SP.Data.Draft_x0020_StandardsItem` (spaces become `_x0020_`).

**2. Add the *Send an HTTP request to SharePoint* action.**

🔸 **Site Address:** your target site.

🔸 **Method:** `POST`

🔸 **Uri:**

```
_api/web/lists/getbytitle('Draft Standards')/items(ID)
```

(replace `ID` with the item's ID).

**3. Set the headers** for a MERGE update:

```
Accept: application/json;odata=verbose
Content-Type: application/json;odata=verbose
IF-MATCH: *
X-HTTP-Method: MERGE
```

🔸 `X-HTTP-Method: MERGE` turns the POST into an update; `IF-MATCH: *` updates regardless of the current version (eTag).

**4. Set the Body** — write the new name to `FileLeafRef` (keep the extension!):

```json
{
  "__metadata": { "type": "SP.Data.Draft_x0020_StandardsItem" },
  "FileLeafRef": "Framework-Agreement-2026.pdf"
}
```

🔸 The `type` value MUST match your library's `ListItemEntityTypeFullName` from step 1 — it is different for every library.

**5. Run the flow.** A `204 No Content` response means the rename succeeded.

🔸 Build the new name dynamically with expressions (e.g. `concat('Invoice-', triggerBody()?['RefNo'], '.pdf')`) — just make sure the result is a valid SharePoint file name.

## 🎉 Result
The file is renamed in place. Its item ID, version history, permissions and metadata are all preserved — no copy, no delete, no broken links or lost history.

## 🌟 Key Advantages

🔸 **True in-place rename:** ID, versions and metadata survive — unlike copy-and-delete.

🔸 **No premium needed:** the SharePoint connector's *Send an HTTP request to SharePoint* action is standard.

🔸 **Fully dynamic:** compute the new file name from any flow data with expressions.

## 🛠️ FAQ

**Q1: Why not just use *Copy file* and *Delete file*?**

That creates a new item with a new ID and wipes version history and metadata. Updating `FileLeafRef` renames the existing item, so everything is preserved.

**Q2: Where do I find the correct `__metadata` type?**

Send a GET to `_api/web/lists/getbytitle('YourLibrary')?$select=ListItemEntityTypeFullName`. Use that exact value — spaces in the library name are encoded as `_x0020_`.

**Q3: Do I have to include the file extension in `FileLeafRef`?**

Yes. `FileLeafRef` is the leaf name *including* the extension. Omit it and you'll break the file type — always append `.pdf`, `.docx`, etc.

**Q4: Can I rename a folder the same way?**

Yes. Folders are also list items, so updating `FileLeafRef` on the folder's item renames the folder in place.

## 🔗 Related Tips
- [#PowerPlatformTip 121 – Filtering SharePoint File Fields with OData](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-121-filtering-sharepoint-file-fields-with-odata/) — how `FileLeafRef`, `FileRef` and `FileDirRef` work.
- [#PowerPlatformTip 58 – HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/) — the basics of HTTP requests in Power Automate.
- [#PowerPlatformTip 47 – Batch-Method within SharePoint](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-47-batch-method-within-sharepoint/) — bulk REST operations against SharePoint.
