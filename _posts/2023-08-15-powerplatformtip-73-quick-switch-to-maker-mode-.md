---
title: "#PowerPlatformTip 73 – 'Quick Switch to Maker Mode'"
date: 2023-08-15
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Maker Mode
  - Productivity
  - Bookmarklet
  - App Editing
  - Low Code
  - Power Platform
excerpt: "Instantly switch from play mode to maker mode in Power Apps using a bookmarklet—speed up app editing, boost productivity, and streamline your development workflow."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

You're using a Power App in play mode and realize you need to make some adjustments. Normally you'd navigate back to the environment, locate the app, and click **Edit** – a time-consuming detour that disrupts your workflow.

## ✅ Solution

Use a simple bookmarklet (a small JavaScript snippet) that lets you switch from play mode to maker mode instantly, without closing the app.

## 🔧 How It's Done

**1. Create the bookmarklet**

🔸 Grab the JavaScript code from [PowerAppsPlayToMake.js](https://github.com/MarceLehmann/CodeSnippets/blob/main/PowerAppsPlayToMake.js).

🔸 Create a new browser bookmark and paste the code into the URL field.

**2. Activate it in play mode**

🔸 While viewing an app in play mode, click the bookmarklet.

**3. Land in maker mode**

🔸 You transition instantly to maker mode, with the app open and ready for edits.

## 🎉 Result

You've streamlined the switch between play and maker modes in Power Apps, enabling rapid iterations and a smoother development experience.

## 🌟 Key Advantages

🔸 Time-Saving: No more navigating through multiple steps to edit your app

🔸 Seamless Workflow: Stay in the zone by switching modes without disruptions

🔸 Faster Iterations: A smoother development experience for quick edits

## 🎥 Video Tutorial

{% include video id="vfciorDH6bM" provider="youtube" %}

## 🛠️ FAQ

**Q: How do I add this bookmarklet to my browser?**

Open your browser's bookmark manager, create a new bookmark, and paste the JavaScript code from the GitHub link into the URL field. Save it and you're ready to use it.

**Q: Which browsers support this bookmarklet?**

Most modern desktop browsers support bookmarklets, including Chrome, Edge, Firefox, and Safari. Mobile browsers may have limitations executing custom scripts.

**Q: Is this an official Microsoft feature?**

No. This is a user-created workaround using a bookmarklet. It's not officially supported by Microsoft, so use it at your own discretion.
