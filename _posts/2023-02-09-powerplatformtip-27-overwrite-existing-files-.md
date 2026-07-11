---
title: "#PowerPlatformTip 27: 'Overwrite existing files' (The Settings Hack)"
seo_title: "Overwrite Existing Files in Power Automate (SharePoint)"
date: 2023-02-09
last_modified_at: 2026-07-10
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
excerpt: "Enable file overwriting in SharePoint by disabling 'Allow Chunking', a simple settings tweak that unlocks the hidden overwrite toggle in Power Automate."
description: "Overwrite toggle missing in Power Automate's Create File action? Turn off Allow Chunking to unlock it and replace SharePoint files, no delete-and-recreate."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
faq:
  - question: "Why is the Overwrite option hidden by default?"
    answer: "Microsoft enables chunking by default to support large file uploads. Since chunked uploads can't overwrite, the toggle is hidden until you disable chunking."
  - question: "What happens if my file is too large with chunking off?"
    answer: "The flow can fail with a size limit error. For large files, keep chunking enabled and use a delete-then-create pattern instead."
  - question: "Does overwriting preserve sharing permissions?"
    answer: "Yes, overwriting maintains existing sharing links, permissions, and metadata. The file ID stays the same."
  - question: "Can I use this for OneDrive too?"
    answer: "OneDrive for Business has the Overwrite toggle available by default, no settings hack needed there!"
howto:
  name: "How to overwrite existing files in SharePoint with Power Automate"
  steps:
    - text: "Open your Create File action in Power Automate."
    - text: "Click Settings (top right of the action)."
    - text: "Scroll to the Content Transfer section."
    - text: "Set Allow Chunking to Off."
    - text: "Close Settings, the Overwrite toggle now appears in your action!"
---

> **TL;DR:** Turn off 'Allow Chunking' in the SharePoint Create File action's settings to unlock the hidden Overwrite toggle.

## 💡 Challenge
You want to overwrite existing files in SharePoint using Power Automate's **Create File** action, but the **Overwrite** toggle is missing or greyed out!

## ✅ Solution
Disable the **Allow Chunking** setting in your SharePoint connector, this instantly unlocks the **Overwrite** option.

## 🔧 How It's Done

![SharePoint Create File Settings - Allow Chunking disabled to enable Overwrite](/assets/images/posts/powerplatformtip-27-overwrite.jpg "Disable Allow Chunking to unlock Overwrite")

1. Open your **Create File** action in Power Automate.
2. Click **Settings** (top right of the action).
3. Scroll to the **Content Transfer** section.
4. Set **Allow Chunking** to **Off**.
5. Close Settings, the **Overwrite** toggle now appears in your action!

## ⚠️ Trade-offs
🔸 **Size limit**: With chunking disabled, very large files can fail. Keep chunking enabled for large file scenarios.

🔸 **Version History**: Overwriting replaces the file entirely. Enable SharePoint versioning if you need rollback capability.

## 🎉 Result
Your files get cleanly replaced without duplicates, no delete-then-create workarounds needed.

## 🌟 Key Advantages
🔸 **One-Click Fix**: A simple settings toggle, no extra actions in your flow.

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

OneDrive for Business has the Overwrite toggle available by default, no settings hack needed there!

## 🔗 Related Tips
- [#PowerPlatformTip 121: Filtering SharePoint File Fields with OData](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-121-filtering-sharepoint-file-fields-with-odata/), target the exact file before you overwrite it.
- [#PowerPlatformTip 18: Download and Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/), more file-handling patterns in flows.
