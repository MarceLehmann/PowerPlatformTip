---
title: "#PowerPlatformTip 13 – 'PowerApps4Teams in make.powerapps.com'"
date: 2022-12-22
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Teams
  - url-hack
  - productivity
  - powerapps4teams
  - PowerPlatformTip
excerpt: "Edit PowerApps4Teams apps directly in make.powerapps.com using a URL hack. Save time and boost productivity by bypassing the standard Teams creation process."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Open a PowerApps for Teams app directly in the make.powerapps.com studio by swapping its environment and app IDs into a standard edit URL.

Editing a PowerApps for Teams app normally means going through the Teams creation flow every time.
With a small URL trick you can open the same app directly in edit mode in the Power Apps studio at make.powerapps.com — by swapping the environment and app IDs into a known edit URL.

## 💡 Challenge
If you build with PowerApps for Teams, reaching the edit screen through the Teams interface is slow and repetitive. A shortcut straight into the studio would save real time.

## ✅ Solution
Copy the environment ID and app ID, paste them into a standard Power Apps edit URL, and open your Teams app directly in edit mode in the studio.

## 🔧 How it's done

**1. Copy the IDs**

🔸 Get the **environment ID** and **app ID** from your PowerApps for Teams app details.

**2. Open any app in edit mode**

🔸 In make.powerapps.com, edit any app and copy the URL from the browser's address bar as a template.

**3. Swap the IDs**

🔸 Replace the environment ID and the app ID segments in the URL with your Teams app's values.

**4. Load the URL**

🔸 Press Enter — the studio opens your Teams app for editing like any other canvas app.

## 🎉 Result
You jump straight into editing your Teams app in the familiar Power Apps studio, skipping the Teams navigation entirely.

## 🌟 Key Advantages

🔸 **Time-saving:** bypass the Teams creation process and edit directly.

🔸 **Familiar environment:** work in the full Power Apps studio.

🔸 **Quick edits:** make small changes without navigating through Teams.

## 🎥 Video Tutorial
{% include video id="FuzWFysCg5g" provider="youtube" %}

---

## 🛠️ FAQ

**Q1: How do I find the environment and app IDs for my Teams app?**

Open your Teams app, click **Edit** to launch the studio, and read both IDs from the browser URL or the app settings.

**Q2: Can I use this hack for any PowerApps for Teams app?**

Yes. As long as the app exists in the environment, you can swap the IDs in an edit URL to open that app directly in the studio.

**Q3: Is this supported by Microsoft or just a workaround?**

It's an unofficial workaround. It uses the standard studio, but it isn't documented by Microsoft, so it may change with future updates.
