---
title: "#PowerPlatformTip 27 – 'Overwrite existing files' (The Settings Hack)"
date: 2023-02-09
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - power automate
  - sharepoint
  - file overwrite
  - file management
  - chunking
  - settings hack
excerpt: "Enable file overwriting in SharePoint by disabling 'Allow Chunking' – a simple settings tweak that unlocks the hidden overwrite toggle in Power Automate."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge
You want to overwrite existing files in SharePoint using Power Automate's **Create File** action – but the **Overwrite** toggle is missing or greyed out!

## ✅ Solution
Disable the **Allow Chunking** setting in your SharePoint connector – this instantly unlocks the **Overwrite** option.

## 🔧 How It's Done

![SharePoint Create File Settings - Allow Chunking disabled to enable Overwrite](/assets/images/posts/powerplatformtip-27-overwrite.jpg "Disable Allow Chunking to unlock Overwrite")

1. Open your **Create File** action in Power Automate.
2. Click **Settings** (top right of the action).
3. Scroll to the **Content Transfer** section.
4. Set **Allow Chunking** to **Off**.
5. Close Settings – the **Overwrite** toggle now appears in your action!

## ⚠️ Trade-offs
🔸 **Size limit**: With chunking disabled, very large files can fail. Keep chunking enabled for large file scenarios.

🔸 **Version History**: Overwriting replaces the file entirely. Enable SharePoint versioning if you need rollback capability.

## 🎉 Result
Your files get cleanly replaced without duplicates – no delete-then-create workarounds needed.

## 🌟 Key Advantages
🔸 **One-Click Fix**: A simple settings toggle – no extra actions in your flow.

🔸 **Faster Flows**: Skip the "check if exists → delete → create" dance.

🔸 **Cleaner Libraries**: No more `filename(1).docx` clutter.

---

## 🛠️ FAQ
**1. Why is the Overwrite option hidden by default?**

Microsoft enables chunking by default to support large file uploads. Since chunked uploads can't overwrite, the toggle is hidden until you disable chunking.

**2. What happens if my file is too large with chunking off?**

The flow can fail with a size limit error. For large files, keep chunking enabled and use a delete-then-create pattern instead.

**3. Does overwriting preserve sharing permissions?**

Yes, overwriting maintains existing sharing links, permissions, and metadata. The file ID stays the same.

**4. Can I use this for OneDrive too?**

OneDrive for Business has the Overwrite toggle available by default – no settings hack needed there!

---
