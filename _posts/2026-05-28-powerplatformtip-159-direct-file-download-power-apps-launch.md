---
title: "#PowerPlatformTip 159: 'Force a Direct File Download in Power Apps with Launch'"
date: 2026-05-28
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - SharePoint
  - Launch
  - FileDownload
  - CanvasApps
  - PowerPlatformTip
excerpt: "Clicking a SharePoint file link in Power Apps usually opens a preview instead of saving the file. Append &Download=1 to the URL inside Launch() and SharePoint returns the file as a real download - no Power Automate, no custom connector."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** `Launch(FileURL & "&Download=1")` turns a SharePoint file link into a real download instead of a browser preview. One string, no flow, no premium connector.

Opening a document from a canvas app with `Launch()` normally hands the URL to the browser, which happily shows a **preview** of the PDF, image or Office file. Users then have to hunt for a download button inside the viewer. By appending `&Download=1` to the SharePoint URL, you tell SharePoint to serve the file as an attachment, so the browser downloads it straight away.

## 💡 Challenge
You store files in SharePoint and surface their links in a gallery or button. Calling `Launch(ThisItem.FileURL)` opens the file in the browser's built-in viewer (preview mode). For a quick look that's fine, but when users actually need the file on their device, the extra "download from the viewer" step is annoying and, on mobile, sometimes impossible.

## ✅ Solution
`Download=1` is a **SharePoint URL parameter**, not a Power Fx feature. When SharePoint sees it, it responds with `Content-Disposition: attachment`, which forces the browser to download the file instead of rendering it. Because `Launch()` simply appends extra parameters to the end of the query string, you can add it right in the formula.

## 🔧 How it's done

**1. Get the file URL** from your data source.

🔸 In a SharePoint document library, the *Link to item* / *FileRef*-based absolute URL of the file works, for example:

```
https://contoso.sharepoint.com/sites/Team/Shared Documents/Report.pdf
```

**2. Append the download parameter inside Launch.**

🔸 If the URL already has a query string (contains `?`), add `&Download=1`:

```power
Launch( ThisItem.FileURL & "&Download=1" )
```

🔸 If the raw URL has **no** `?` yet, start the query string with `?Download=1` instead:

```power
Launch( ThisItem.FileURL & "?Download=1" )
```

**3. Make it robust for both cases** so you don't have to guess:

```power
Launch(
    ThisItem.FileURL &
    If( IsMatch( ThisItem.FileURL, "\?" ), "&", "?" ) &
    "Download=1"
)
```

🔸 This checks whether a `?` is already present and picks `&` or `?` automatically.

**4. Put it on a button or gallery item** `OnSelect`. On the web the file downloads immediately; in the mobile player the user is prompted to save it.

🔸 Allow pop-ups if your app is embedded (Teams, SharePoint, Power BI), otherwise the browser may block the new window that `Launch()` opens.

## 🎉 Result
A single click saves the file to the user's device instead of opening a preview they then have to download manually. No Power Automate flow, no custom connector, no extra component, just one parameter on the URL.

## 🌟 Key Advantages

🔸 **One-liner:** no flow, no premium connector, no component to import.

🔸 **Real download:** SharePoint returns the file as an attachment via `Content-Disposition`, so browsers save instead of preview.

🔸 **Works with what you have:** any absolute SharePoint file URL already in your gallery or list.

## 🛠️ FAQ

**Q1: Is `Download=1` a Power Apps / Launch function feature?**

No. It's a **SharePoint** URL behavior. `Launch()` only appends it to the query string; SharePoint interprets it and returns the file as a download.

**Q2: What's the difference to the native `Download()` function?**

`Download(Address)` is a Power Fx function that downloads a file to the device, but in the browser its behavior depends on the browser settings - PDFs, images and videos often just open in a new tab. It also can't authenticate protected SharePoint links in the mobile player. The `&Download=1` trick relies on SharePoint's own attachment response, which forces a save more reliably for library files.

**Q3: The file still opens in a preview - what's wrong?**

Check that you actually appended the parameter with the correct separator (`?` for the first parameter, `&` afterwards) and that the link is a direct file URL. Some sharing links open a viewer page rather than the file; use the file's absolute path (`FileRef`) instead.

**Q4: Does the user need permission to the file?**

Yes. The download runs in the user's browser session, so they must have at least read access to the file in SharePoint, just like opening it normally.

## 🔗 Related Tips
- [#PowerPlatformTip 53: Launch function](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-53-launch-function/), the all-round guide to opening URLs, apps and deep links with `Launch()`.
- [#PowerPlatformTip 132: Office Files Viewer in PowerApps](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-132-office-files-viewer-in-powerapps/), the opposite use case - viewing files inside the app instead of downloading them.
- [#PowerPlatformTip 18: Download & Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/), downloading and storing files server-side with Power Automate.
