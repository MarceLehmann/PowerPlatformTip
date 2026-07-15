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

> **TL;DR:** A single Power Automate message is limited to **100 MB**. Enable **Allow chunking** under an action's **Settings → Content transfer** and supported actions handle files up to **1 GB**.

Uploading or copying a large document in a flow suddenly fails with a size or timeout error? You have hit the **100 MB message size limit** that applies to a single HTTP call in Power Automate. For actions that support it, switching on **Allow chunking** raises the ceiling to **1 GB** by splitting the payload into smaller pieces automatically.

## 💡 Challenge
Your flow moves, uploads or downloads a file — a big PDF, video or backup — and the run fails or times out once the file grows past roughly 100 MB.
That is expected: the limit on a single message in an automated, scheduled or instant flow is **100 MB**, and when you send a file through a connector the **whole payload** (headers, metadata and file) must stay under that limit — not just the file itself.

## ✅ Solution
Many file actions can transfer larger content in pieces instead of one block. Turning on **Allow chunking** in the action's **Content transfer** settings lets supported actions process files **up to 1 GB**. The chunking protocol is handled for you — you do not split anything manually.

## 🔧 How it's done

**1. Open the action's settings.**

🔸 On the file action (e.g. *Create file*, *Get file content*, *HTTP*), open the **… menu → Settings**.

**2. Enable Allow chunking.**

🔸 Scroll to **Content transfer** and set **Allow chunking** to **On**. Save the action.

🔸 With chunking on, supported actions handle payloads up to **1 GB** instead of 100 MB.

**3. Don't feed chunked actions from the trigger or a variable directly.**

🔸 Chunking is **not supported on triggers**. If you reference `triggerBody()`, a variable or an inline expression as the content, chunking is disabled.

🔸 Store the content in a **Compose** action first, then point the chunking-enabled action at that Compose output.

**4. Confirm the connector actually supports chunking.**

🔸 Not every connector or API supports chunking — some don't even honor the default 100 MB. If an action doesn't expose the toggle or still fails, the underlying connector doesn't support it.

**5. For files well beyond 1 GB, copy server-side.**

🔸 Skip downloading and re-uploading the bytes through the flow. Use a **server-side copy** — e.g. Azure Blob **Copy Blob From URL** with a Microsoft Graph `@microsoft.graph.downloadUrl` — so the file never passes through Power Automate's size limits.

## 🎉 Result
Large-file actions that used to fail at ~100 MB now transfer content up to **1 GB** with a single settings toggle — no premium connector, no restructuring, and no manual splitting.

## 🌟 Key Advantages

🔸 **One toggle:** Allow chunking is a per-action setting, not a redesign.

🔸 **10x headroom:** 100 MB → 1 GB on supported actions.

🔸 **Built-in:** works with standard HTTP and many standard file actions — no premium licence required.

## 🛠️ FAQ

**Q1: What exactly is the limit — 100 MB or 1 GB?**

A single message is **100 MB** by default. With **Allow chunking** enabled on a supporting action, the limit rises to **1 GB**.

**Q2: Why does my flow still fail after enabling chunking?**

Either the connector doesn't support chunking, or the content comes straight from a trigger/variable/expression (which disables it). Route the content through a **Compose** action and verify the connector supports chunking.

**Q3: Does chunking work on triggers?**

No. Chunking applies to **actions** only. A trigger can't deliver more than the default limit, so pull large content with a separate action after the trigger.

**Q4: The file is 3 GB — what now?**

Chunking tops out at **1 GB**. For larger files, use a **server-side copy** (e.g. Azure Blob *Copy Blob From URL* with a direct download URL) so the bytes never flow through Power Automate.

**Q5: Enabling chunking removed my Overwrite option — is that related?**

Yes. Some SharePoint actions hide **Overwrite** when chunking is on. See #PowerPlatformTip 27 for the reverse trade-off.

## 🔗 Related Tips
- [#PowerPlatformTip 27: Overwrite Existing Files in Power Automate](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-27-overwrite-existing-files/) — the reverse trade-off: turn *Allow Chunking* **off** to unlock the Overwrite toggle.
- [#PowerPlatformTip 58: HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/) — HTTP actions are the main chunking candidates for custom API calls.
- [#PowerPlatformTip 18: Download & Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/) — choosing the right action for public vs. authenticated file handling.
