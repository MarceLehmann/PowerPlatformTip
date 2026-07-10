---
title: "#PowerPlatformTip 132 – 'Office Files Viewer in PowerApps'"
date: 2025-01-16
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - SharePoint
  - OfficeFiles
  - FileViewer
  - Component
  - NoCode
  - PowerPlatformTip
excerpt: "Display Office files like PDFs or Word documents directly in PowerApps without external workflows or third-party tools."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Show PDFs, Word and Excel files straight from SharePoint inside Power Apps with the Office Files Viewer component – no Power Automate.

## 💡 Challenge
Viewing Office files directly in Power Apps is often a hassle — you end up wiring in complex integrations or extra tools like Power Automate, which is time-consuming and usually unnecessary.

## ✅ Solution
Use the Office Files Viewer component to display Office files directly from SharePoint inside Power Apps — no Power Automate required.

## 🔧 How It's Done

**1. Prepare the SharePoint library**

🔸 Create a hyperlink column in your SharePoint list.

🔸 Convert it into an image column and add the file URLs.

**2. Import the component**

🔸 Download and import the Office Files Viewer component into your app.

🔸 Find the component and instructions on GitHub.

**3. Configure the inputs**

🔸 Set your SharePoint URL as the component's data source.

🔸 Follow the instructions to display your files directly in Power Apps.

**4. Test and optimize**

🔸 Verify that files display as expected.

🔸 Adjust the view and integration to your needs.

## 🎉 Result
You get a user-friendly, integrated way to display Office files directly within Power Apps — no unnecessary tools, just an efficient, seamless solution.

## 🌟 Key Advantages

🔸 **Native integration:** fully built into Power Apps — no Power Automate.

🔸 **Multiple file types:** view PDFs, Word documents, Excel files, and more.

🔸 **Time saver:** streamlines file viewing so you focus on the important work.

---

## 🛠️ FAQ
**1. Can I view other file formats besides PDF?**
Yes — you can display PDFs, Word documents, Excel spreadsheets, images and more directly from SharePoint using the component.

**2. Do I need Power Automate to get this working?**
No. The Office Files Viewer component works natively in Power Apps — no external workflows required.

**3. How do I update file URLs after setup?**
Update the SharePoint hyperlink/image column with new URLs, or adjust the component's data source settings in Power Apps.

## 🔗 Related Tips
- [#PowerPlatformTip 92 – Free PDF Tools in Power Automate](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-92-free-pdf-tools-in-powerautomate/) — generate and manipulate PDFs for viewing.
- [#PowerPlatformTip 18 – Download and Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/) — handle file downloads in your apps.
