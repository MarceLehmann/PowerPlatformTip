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
excerpt: "Clicking a SharePoint file link in Power Apps usually opens a preview instead of saving the file. Appending &download=1 to the URL inside Launch() often makes SharePoint return the file as a real download - a handy (if unofficial) trick, no Power Automate and no custom connector."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** `Launch(FileURL & "&download=1")` often turns a SharePoint file link into a real download instead of a browser preview. It's a widely used but **unofficial** SharePoint behavior (only `web=1` is officially documented), so test it in your tenant - no flow, no premium connector.

Opening a document from a canvas app with `Launch()` normally hands the URL to the browser, which happily shows a **preview** of the PDF, image or Office file. Users then have to hunt for a download button inside the viewer. Appending `&download=1` to the SharePoint URL has long been a community trick to make SharePoint serve the file as an attachment, so the browser downloads it straight away. It's not officially documented - and modern SharePoint doesn't honor it everywhere - but where it works, it's a one-liner.

## 💡 Challenge
You store files in SharePoint and surface their links in a gallery or button. Calling `Launch(ThisItem.FileURL)` opens the file in the browser's built-in viewer (preview mode). For a quick look that's fine, but when users actually need the file on their device, the extra "download from the viewer" step is annoying and, on mobile, sometimes impossible.

## ✅ Solution
`download=1` is a **SharePoint URL parameter** (not a Power Fx feature) that many makers use to make SharePoint respond with `Content-Disposition: attachment`, which forces the browser to download the file instead of rendering it. Because `Launch()` simply appends parameters to the query string, you can add it right in the formula.

> ⚠️ **Reality check:** Microsoft only officially documents `web=1` (force *open in browser*). `download=1` is an **undocumented** behavior: it works in many classic file URLs, but **modern SharePoint may rewrite or ignore it** in some contexts (for example the Quick Links web part). Always test it against your own tenant and file URLs, and keep the `Download()` alternative below in mind.

## 🔧 How it's done

**1. Get the file URL** from your data source.

🔸 In a SharePoint document library, the file's absolute URL (`FileRef`-based) works, for example:

```
https://contoso.sharepoint.com/sites/Team/Shared Documents/Report.pdf
```

**2. Append the download parameter inside Launch.** Use the conventional **lowercase** `download=1`.

🔸 If the URL already has a query string (contains `?`), add `&download=1`:

```power
Launch( ThisItem.FileURL & "&download=1" )
```

🔸 If the raw URL has **no** `?` yet, start the query string with `?download=1` instead:

```power
Launch( ThisItem.FileURL & "?download=1" )
```

**3. Make it robust for both cases** so you don't have to guess:

```power
Launch(
    ThisItem.FileURL &
    If( IsMatch( ThisItem.FileURL, "\?" ), "&", "?" ) &
    "download=1"
)
```

🔸 This checks whether a `?` is already present and picks `&` or `?` automatically.

**4. Put it on a button or gallery item** `OnSelect`. Where the parameter is honored, the file downloads immediately on the web; in the mobile player the user is prompted to save it.

🔸 Allow pop-ups if your app is embedded (Teams, SharePoint, Power BI), otherwise the browser may block the new window that `Launch()` opens.

## 🎉 Result
Where SharePoint honors the parameter, a single click saves the file to the user's device instead of opening a preview they then have to download manually. No Power Automate flow, no custom connector, no extra component - just one parameter on the URL.

## 🌟 Key Advantages

🔸 **One-liner:** no flow, no premium connector, no component to import.

🔸 **Real download (when honored):** SharePoint returns the file as an attachment via `Content-Disposition`, so browsers save instead of preview.

🔸 **Works with what you have:** any absolute SharePoint file URL already in your gallery or list.

## 🛠️ FAQ

**Q1: Is `download=1` an official, guaranteed feature?**

No. It's an **undocumented SharePoint URL behavior**, not a Power Apps / `Launch()` feature. `Launch()` only appends it to the query string; SharePoint decides what to do. The only officially documented sibling parameter is `web=1` (force *open in the browser*). Modern SharePoint may rewrite or ignore `download=1` in some contexts, so treat it as a best-effort trick and test it.

**Q2: What's the difference to the native `Download()` function?**

`Download(Address)` is a documented Power Fx function that downloads a file to the device. In native players (Windows/Android/iOS) the user is prompted for a save location, but in the browser its behavior depends on browser settings - PDFs, images and videos often just open in a new tab. Per Microsoft, `Download()` also **can't authenticate** protected SharePoint links in the mobile player. So `Download()` is the officially supported route, while `&download=1` is an unofficial trick that can force a save more reliably for library files where it's honored.

**Q3: The file still opens in a preview - what's wrong?**

First, remember `download=1` isn't guaranteed. Then check that you appended it with the correct separator (`?` for the first parameter, `&` afterwards, lowercase) and that the link is a direct file URL. Some sharing links open a viewer page rather than the file; use the file's absolute path (`FileRef`) instead. If it's simply being ignored by your tenant, fall back to `Download()`, a document library web part, or a Power Automate flow that streams the file.

**Q4: Does the user need permission to the file?**

Yes. The download runs in the user's browser session, so they must have at least read access to the file in SharePoint, just like opening it normally.

## 🔗 Related Tips
- [#PowerPlatformTip 53: Launch function](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-53-launch-function/), the all-round guide to opening URLs, apps and deep links with `Launch()`.
- [#PowerPlatformTip 132: Office Files Viewer in PowerApps](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-132-office-files-viewer-in-powerapps/), the opposite use case - viewing files inside the app instead of downloading them.
- [#PowerPlatformTip 18: Download & Save Files](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-18-download-and-save-files/), downloading and storing files server-side with Power Automate.
