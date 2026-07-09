---
title: "#PowerPlatformTip 19 – 'Resize files'"
date: 2023-01-12
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - SharePoint
  - image-resizing
  - file-management
  - automation
  - PowerPlatformTip
excerpt: "Easily resize large images in Power Automate using SharePoint thumbnails and file management actions. Streamline image processing and automation."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Resize an image for free by storing it on SharePoint and using the 'Upload file from URL' action's thumbnail output — no image editor needed.

Need a smaller version of an image inside a flow — without a premium image-processing connector or external editor?
SharePoint automatically generates **thumbnails** for images stored in a library. Combine the **Upload file from URL** action with that thumbnail output to get a resized copy.

## 💡 Challenge
Handling large images is cumbersome when you only need them in a smaller size, and full image-editing usually means extra tooling.

## ✅ Solution
Use the **Upload file from URL** action together with the **thumbnail output** for image files stored on SharePoint.

## 🔧 How it's done

**1. Store the image on SharePoint**

🔸 Upload (or already have) the large image file in a SharePoint document library.

**2. Use Upload file from URL**

🔸 Add the **Upload file from URL** action for the stored image.

**3. Access the thumbnail output**

🔸 Use the action's **thumbnail** output — a smaller, resized version of the original image.

## 🎉 Result
You get a smaller version of your image without any complex processing or external editor.

## 🌟 Key Advantages

🔸 **Simple:** SharePoint does the resizing for you.

🔸 **Built-in:** uses SharePoint's storage and thumbnail feature.

🔸 **No editor needed:** avoids external image-editing tools.

## 🎥 Video Tutorial
{% include video id="Tvs99nvb2L0" provider="youtube" %}

---

## 🛠️ FAQ

**Q1: Which image formats does this work with?**

Common web image formats such as JPEG, PNG and GIF render reliably through SharePoint's thumbnail service.

**Q2: Can I resize multiple images in one run?**

Yes. Loop with **Apply to each** over your images, mindful of the flow's execution-time limits.

**Q3: Does resizing affect image quality?**

The thumbnail preserves the aspect ratio at a smaller size. Avoid upscaling beyond the original dimensions for the best result.
