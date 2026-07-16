---
title: "#PowerPlatformTip 156: 'Handle Files up to 1 GB with Chunking in Power Automate'"
date: 2026-07-16
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - HTTP
  - Performance
  - Files
  - Limits
  - PowerPlatformTip
excerpt: "Power Automate caps a single message at 100 MB. Turn on 'Allow chunking' in the action's Content transfer settings and supported actions push large files up to 1 GB — no premium connector, no rebuild."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** A single Power Automate message is limited to **100 MB**. Enable **Allow chunking** under an action's **Settings → Content transfer** and supported actions handle files up to **1 GB** — but only when the content flows **directly by reference** from one chunk-capable action to the next. The moment a variable, expression **or a Compose** materialises it, you are back to the 100 MB ceiling. Beyond 1 GB, copy **server-side** (e.g. a SharePoint copy job).

Uploading or copying a large document in a flow suddenly fails with a size or timeout error? You have hit the **100 MB message size limit** that applies to a single HTTP call in Power Automate. For actions that support it, switching on **Allow chunking** raises the ceiling to **1 GB** by splitting the payload into smaller pieces automatically.

## 💡 Challenge
Your flow moves, uploads or downloads a file — a big PDF, video or backup — and the run fails or times out once the file grows past roughly 100 MB.
That is expected: the limit on a single message in an automated, scheduled or instant flow is **100 MB**, and when you send a file through a connector the **whole payload** (headers, metadata and file) must stay under that limit — not just the file itself.

## ✅ Solution
Many file actions can transfer larger content in pieces instead of one block. Turning on **Allow chunking** in the action's **Content transfer** settings lets supported actions process files **up to 1 GB**. The chunking protocol is handled for you — you do not split anything manually. The catch: a chunked output **larger than 100 MB can only be read by another chunk-capable action**. The moment an ordinary action (a variable, an expression, or even a **Compose**) touches it, the run hits the 100 MB message limit.

## 🔧 How it's done

**1. Open the action's settings.**

🔸 On the file action (e.g. *Create file*, *Get file content*, *HTTP*), open the **… menu → Settings**.

**2. Enable Allow chunking.**

🔸 Scroll to **Content transfer** and set **Allow chunking** to **On**. Save the action.

🔸 With chunking on, supported actions handle payloads up to **1 GB** instead of 100 MB.

**3. For real >100 MB, stream chunk-capable action → chunk-capable action *directly*.**

🔸 Chunking is **not supported on triggers**.

🔸 A chunked output **larger than 100 MB can only be accessed by another chunk-capable action** (one that natively supports chunking or has it enabled in its runtime config). Reference the source action's body **directly**, e.g. `"body": "@body('HTTP_GET_Download')"`, in the chunk-enabled destination action.

🔸 **Do not route it through a variable or a Compose.** Those are ordinary actions bound by the 100 MB message limit — accessing a larger chunked output throws a runtime error. In other words: **Compose does not lift the ceiling to 1 GB.**

**4. When Compose *does* help (≤100 MB only).**

🔸 If your content is **≤100 MB** but comes from a `triggerBody()`, a variable or an inline expression, those inputs **disable chunking**. Wrap the content in a **Compose** action and reference it with `@body('Compose')` so a chunk-enabled action can activate chunking — useful when the destination connector's own limit is *below* 100 MB (for example a connector that already treats 30 MB as "large"). Compose only fixes the reference form; it never raises the 100 MB cap.

**5. Confirm the connector actually supports chunking.**

🔸 Not every connector or API supports chunking — some don't even honor the default 100 MB. If an action doesn't expose the toggle or still fails, the underlying connector doesn't support it.

🔸 For **HTTP** actions specifically, the external endpoint must implement the **Logic Apps chunking protocol** (`206 Partial Content` for downloads, `x-ms-transfer-mode: chunked` + PATCH for uploads). A generic web server that only speaks standard HTTP chunking will **not** work.

**6. For files well beyond 1 GB, copy server-side (never move the bytes through the flow).**

🔸 **Azure Blob:** *Copy Blob From URL* with a Microsoft Graph `@microsoft.graph.downloadUrl`.

🔸 **SharePoint → SharePoint:** the **Copy file** action copies within the same tenant server-side. For large or bulk moves, call the **`CreateCopyJobs` REST API** via *Send an HTTP request to SharePoint* (`POST /_api/site/CreateCopyJobs`) — it copies/moves files server-side up to SharePoint's own file-size limit (**250 GB**), and the payload never enters Power Automate.

> 💡 **Extra tip — beyond 1 GB in SharePoint:** Don't try to force a multi-GB file through chunking. Use a **SharePoint copy job**. The simplest option is the standard **Copy file** action (same tenant). For heavier scenarios — very large files, whole folders, or many files at once — POST to `/_api/site/CreateCopyJobs` with a *Send an HTTP request to SharePoint* action. SharePoint performs the copy/move entirely on the server, so neither the 100 MB nor the 1 GB flow limit applies. You only pass the source and destination URLs, not the bytes.

## 🔁 Reference vs. value: the part that trips everyone up
Chunking lives on **references**, not on evaluated **values**:

🔸 **Reference (streamable):** `@body('ChunkCapableAction')` is a *pointer* to a content body. Another chunk-capable action can consume it chunk by chunk without ever loading the whole thing into memory. → up to 1 GB works.

🔸 **Value (materialised):** `@variables(…)`, `@triggerBody()` or a composed expression (`concat(…)`, `@{…}`) forces the engine to **evaluate** the content into a finished string/JSON in memory. A materialised value is not streamable → the 100 MB limit applies.

🔸 **Compose is materialising too.** It is an ordinary Data Operation, not a chunk-capable action, so it is bound by the 100 MB limit and **cannot carry a >100 MB chunked payload** — it throws a runtime error. Compose only earns its place for **≤100 MB** content that needs a valid `@body()` reference to switch chunking on toward a smaller-limit connector.

### ❌ Wrong — a variable (or Compose) in the >100 MB path
```json
"Set_variable": {
  "type": "SetVariable",
  "inputs": { "name": "Big", "value": "@body('HTTP_GET_Download')" }
},
"Create_file": {
  "type": "ApiConnection",
  "runtimeConfiguration": { "contentTransfer": { "transferMode": "Chunked" } },
  "inputs": { "body": "@variables('Big')" }
}
```
Writing the large download body into a **variable** (or a **Compose**) materialises it → 100 MB cap / runtime error → the run fails. The intermediate action kills chunking.

### ✅ Right — reference the chunk-capable source body directly
```json
"HTTP_GET_Download": {
  "type": "Http",
  "inputs": { "method": "GET", "uri": "https://big.example.com/file.zip" }
},
"Create_file": {
  "type": "ApiConnection",
  "runtimeConfiguration": { "contentTransfer": { "transferMode": "Chunked" } },
  "inputs": {
    "body": "@body('HTTP_GET_Download')",
    "host": { "connection": { "name": "@parameters('$connections')['sharepointonline']['connectionId']" } },
    "method": "post",
    "path": "/datasets/.../files"
  },
  "runAfter": { "HTTP_GET_Download": ["Succeeded"] }
}
```
The content stays a chunked reference the whole way — chunk-capable download → chunk-capable *Create file* — so the chain streams up to 1 GB. **No variable, no Compose, no expression touches the bytes.**

> ⚠️ **Heads-up:** When chunking is enabled, the action's output contains **only** the `body` property — `statusCode` and `headers` are gone. Tracked properties that reference `outputs['statusCode']` or `outputs['headers']` fail with `TrackedPropertiesEvaluationFailed`, even though the download/upload actually succeeded. Remove those references.

## 🎉 Result
Large-file actions that used to fail at ~100 MB now transfer content up to **1 GB** — provided the payload stays a chunked reference from one chunk-capable action to the next. Above 1 GB, a **server-side copy** (Azure Blob or a SharePoint copy job) moves the file without ever touching Power Automate's size limits. No premium connector, no restructuring, and no manual splitting.

## 🌟 Key Advantages

🔸 **One toggle:** Allow chunking is a per-action setting, not a redesign.

🔸 **10x headroom:** 100 MB → 1 GB on supported actions.

🔸 **Built-in:** works with standard HTTP (endpoint must implement the Logic Apps chunking protocol) and many standard file actions — no premium licence required.

## 🛠️ FAQ

**Q1: What exactly is the limit — 100 MB or 1 GB?**

A single message is **100 MB** by default. With **Allow chunking** enabled and the content streamed directly between chunk-capable actions, the limit rises to **1 GB**.

**Q2: Why does my flow still fail after enabling chunking?**

Usually one of these: the connector doesn't support chunking, the HTTP endpoint doesn't speak the Logic Apps chunking protocol, or an **ordinary action in the middle** (a variable, expression or **Compose**) materialises the content and hits the 100 MB limit. Reference the chunk-capable source action's body **directly** in the chunk-enabled destination action.

**Q3: Can I route the >100 MB content through a Compose to reach 1 GB?**

No — that is the classic trap. **Compose is bound by the 100 MB message limit** and cannot access a chunked output larger than that (you get a runtime error). Compose only helps for **≤100 MB** content that needs a valid `@body('Compose')` reference to activate chunking toward a connector with a smaller-than-100 MB limit. For genuine >100 MB, reference the chunk-capable source action's body directly — no Compose, no variable.

**Q4: Does chunking work on triggers?**

No. Chunking applies to **actions** only. A trigger can't deliver more than the default limit, so pull large content with a separate action after the trigger.

**Q5: The file is 3 GB — what now?**

Chunking tops out at **1 GB**, so copy **server-side**. Within SharePoint, use the **Copy file** action or the **`CreateCopyJobs` REST API** (`POST /_api/site/CreateCopyJobs` via *Send an HTTP request to SharePoint*) — SharePoint copies/moves the file on the server up to its 250 GB file limit, bytes never entering the flow. For blob storage, use Azure Blob *Copy Blob From URL* with a direct download URL.

**Q6: Enabling chunking removed my Overwrite option — is that related?**

Yes. Some SharePoint actions hide **Overwrite** when chunking is on. See #PowerPlatformTip 27 for the reverse trade-off.

## 🔗 Related Tips
- [#PowerPlatformTip 27: Overwrite Existing Files in Power Automate](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-27-overwrite-existing-files/) — the reverse trade-off: turn *Allow Chunking* **off** to unlock the Overwrite toggle.
- [#PowerPlatformTip 58: HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/) — HTTP actions are the main chunking candidates for custom API calls.
- [#PowerPlatformTip 18: Download & Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/) — choosing the right action for public vs. authenticated file handling.
