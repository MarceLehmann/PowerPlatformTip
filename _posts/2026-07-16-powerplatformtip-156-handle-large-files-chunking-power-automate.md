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

> **TL;DR:** A single Power Automate message is limited to **100 MB**. Enable **Allow chunking** under an action's **Settings → Content transfer** and supported actions handle files up to **1 GB** — but only when the content stays a **reference** (`@body('…')`) and never gets materialised by a variable or expression.

Uploading or copying a large document in a flow suddenly fails with a size or timeout error? You have hit the **100 MB message size limit** that applies to a single HTTP call in Power Automate. For actions that support it, switching on **Allow chunking** raises the ceiling to **1 GB** by splitting the payload into smaller pieces automatically.

## 💡 Challenge
Your flow moves, uploads or downloads a file — a big PDF, video or backup — and the run fails or times out once the file grows past roughly 100 MB.
That is expected: the limit on a single message in an automated, scheduled or instant flow is **100 MB**, and when you send a file through a connector the **whole payload** (headers, metadata and file) must stay under that limit — not just the file itself.

## ✅ Solution
Many file actions can transfer larger content in pieces instead of one block. Turning on **Allow chunking** in the action's **Content transfer** settings lets supported actions process files **up to 1 GB**. The chunking protocol is handled for you — you do not split anything manually. The catch: the large content must flow **by reference** from one chunk-capable action to the next; the moment a variable or expression evaluates it, you drop back to the 100 MB cap.

## 🔧 How it's done

**1. Open the action's settings.**

🔸 On the file action (e.g. *Create file*, *Get file content*, *HTTP*), open the **… menu → Settings**.

**2. Enable Allow chunking.**

🔸 Scroll to **Content transfer** and set **Allow chunking** to **On**. Save the action.

🔸 With chunking on, supported actions handle payloads up to **1 GB** instead of 100 MB.

**3. Feed chunked actions by reference — never from a trigger, variable or expression.**

🔸 Chunking is **not supported on triggers**. A chunking-enabled action only streams when its input is a content **reference** like `@body('…')`. If you pass `triggerBody()`, `@variables(…)` or an inline expression, the engine **materialises** the whole content as a value — chunking silently switches off and you fall back to the 100 MB cap.

🔸 Wrap the content in a **Compose** action and reference it with `@body('Compose')`. **Compose does not raise the limit** — it only gives the action a valid `body` reference so chunking can activate. The real >100 MB transfer only happens when the **source itself is chunk-capable** (e.g. a chunked HTTP GET download), not a variable.

**4. Confirm the connector actually supports chunking.**

🔸 Not every connector or API supports chunking — some don't even honor the default 100 MB. If an action doesn't expose the toggle or still fails, the underlying connector doesn't support it.

🔸 For **HTTP** actions specifically, the external endpoint must implement the **Logic Apps chunking protocol** (`206 Partial Content` for downloads, `x-ms-transfer-mode: chunked` + PATCH for uploads). A generic web server that only speaks standard HTTP chunking will **not** work.

**5. For files well beyond 1 GB, copy server-side.**

🔸 Skip downloading and re-uploading the bytes through the flow. Use a **server-side copy** — e.g. Azure Blob **Copy Blob From URL** with a Microsoft Graph `@microsoft.graph.downloadUrl` — so the file never passes through Power Automate's size limits.

## 🔁 Reference vs. value: the part that trips everyone up
Chunking lives on **references**, not on evaluated **values**:

🔸 **Reference (streamable):** `@body('…')` is a *pointer* to a content body. The engine can hand it to the next action chunk by chunk without ever loading the whole thing into memory. → chunking works.

🔸 **Value (materialised):** `@variables(…)`, `@triggerBody()` or a composed expression (`concat(…)`, `@{…}`) forces the engine to **evaluate** the content into a finished string/JSON in memory. A materialised value is not streamable → chunking is disabled and the 100 MB limit applies.

**Compose** is the exception: its output is a plain `body` field, so `@body('Compose')` is a reference again — exactly what a chunk-capable action needs. It fixes the *reference form*, it does **not** lift the size ceiling.

### ❌ Wrong — variable input, chunking never activates
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
Writing the large download body into a **variable** materialises it → 100 MB cap → the run fails. The variable kills chunking.

### ✅ Right — keep it a reference (via Compose)
```json
"HTTP_GET_Download": {
  "type": "Http",
  "inputs": { "method": "GET", "uri": "https://big.example.com/file.zip" }
},
"Compose": {
  "type": "Compose",
  "inputs": { "body": "@body('HTTP_GET_Download')" },
  "runAfter": { "HTTP_GET_Download": ["Succeeded"] }
},
"Create_file": {
  "type": "ApiConnection",
  "runtimeConfiguration": { "contentTransfer": { "transferMode": "Chunked" } },
  "inputs": {
    "body": "@body('Compose')",
    "host": { "connection": { "name": "@parameters('$connections')['sharepointonline']['connectionId']" } },
    "method": "post",
    "path": "/datasets/.../files"
  },
  "runAfter": { "Compose": ["Succeeded"] }
}
```
The content stays a reference the whole way — chunk-capable download → `@body('Compose')` → chunk-capable *Create file* — so the chain streams up to 1 GB. No `SetVariable`, no expression touches the bytes.

> ⚠️ **Heads-up:** When chunking is enabled, the action's output contains **only** the `body` property — `statusCode` and `headers` are gone. Tracked properties that reference `outputs['statusCode']` or `outputs['headers']` fail with `TrackedPropertiesEvaluationFailed`, even though the download/upload actually succeeded. Remove those references.

## 🎉 Result
Large-file actions that used to fail at ~100 MB now transfer content up to **1 GB** — provided the payload stays a reference from one chunk-capable action to the next. No premium connector, no restructuring, and no manual splitting.

## 🌟 Key Advantages

🔸 **One toggle:** Allow chunking is a per-action setting, not a redesign.

🔸 **10x headroom:** 100 MB → 1 GB on supported actions.

🔸 **Built-in:** works with standard HTTP (endpoint must implement the Logic Apps chunking protocol) and many standard file actions — no premium licence required.

## 🛠️ FAQ

**Q1: What exactly is the limit — 100 MB or 1 GB?**

A single message is **100 MB** by default. With **Allow chunking** enabled on a supporting action, the limit rises to **1 GB**.

**Q2: Why does my flow still fail after enabling chunking?**

Usually one of three reasons: the connector doesn't support chunking, the endpoint (for HTTP) doesn't speak the Logic Apps chunking protocol, or the content comes from a **trigger/variable/expression** and gets materialised. Route the content through a **Compose** action and reference it with `@body('Compose')`.

**Q3: Does putting the content in a Compose raise the limit to 1 GB?**

No. Compose is a **reference/syntax trick**, not a size booster. It only gives the chunk-capable action a valid `body` reference so chunking activates. The actual >100 MB only flows when the **source** is chunk-capable (e.g. a chunked HTTP GET), and no variable or expression evaluates the content in between.

**Q4: Does chunking work on triggers?**

No. Chunking applies to **actions** only. A trigger can't deliver more than the default limit, so pull large content with a separate action after the trigger.

**Q5: The file is 3 GB — what now?**

Chunking tops out at **1 GB**. For larger files, use a **server-side copy** (e.g. Azure Blob *Copy Blob From URL* with a direct download URL) so the bytes never flow through Power Automate.

**Q6: Enabling chunking removed my Overwrite option — is that related?**

Yes. Some SharePoint actions hide **Overwrite** when chunking is on. See #PowerPlatformTip 27 for the reverse trade-off.

## 🔗 Related Tips
- [#PowerPlatformTip 27: Overwrite Existing Files in Power Automate](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-27-overwrite-existing-files/) — the reverse trade-off: turn *Allow Chunking* **off** to unlock the Overwrite toggle.
- [#PowerPlatformTip 58: HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/) — HTTP actions are the main chunking candidates for custom API calls.
- [#PowerPlatformTip 18: Download & Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/) — choosing the right action for public vs. authenticated file handling.
