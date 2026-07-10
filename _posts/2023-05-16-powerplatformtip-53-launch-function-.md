---
title: "#PowerPlatformTip 53: 'Launch function'"
date: 2023-05-16
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Apps
  - Launch Function
  - App Integration
  - Deep Linking
  - Navigation
  - User Experience
  - Teams Integration
  - SharePoint Integration
  - PowerPlatformTip
excerpt: "Open URLs, launch apps, and integrate Power Apps with Teams, SharePoint, and more using the Launch function. Enhance user experience with seamless navigation, deep linking, and personalized app flows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Use the Launch function to open URLs, emails, phone calls, Teams/OneNote/SharePoint deep links, and role-based dashboards straight from your Power App.

## 💡 Challenge

In Power Apps, guiding users to external websites, emails, phone calls, collaborations, or personalized dashboards can require custom connectors or manual prompts.

## ✅ Solution

Leverage the Launch function to open URLs, start emails or calls, integrate with other apps, and direct users to customized content.

## 🔧 How It's Done

**1. Open essential external resources using Launch**

🔸 `Launch("https://www.example.com")`

🔸 `Launch("mailto:info@example.com")`

🔸 `Launch("tel:+1234567890")`

**2. Seamlessly integrate with other applications**

🔸 `Launch("msteams://teams.microsoft.com/l/channel/...")`

🔸 `Launch("onenote:https://example-my.sharepoint.com/personal/...")`

🔸 `Launch("https://example.sharepoint.com/sites/...")`

**3. Personalize the experience based on user roles**

🔸 Example:

```powerapps
If(User().Email = "manager@example.com",
    Launch("https://www.example.com/manager-dashboard"),
    Launch("https://www.example.com/employee-dashboard"))
```

## 🎉 Result

Users can instantly access relevant external resources, collaborate seamlessly, and receive a personalized in-app experience without additional configuration.

## 🌟 Key Advantages

🔸 Immediate access to websites, email and phone calls

🔸 Seamless integration with Teams, OneNote, and SharePoint

🔸 Personalized navigation based on user roles

## 🛠️ FAQ

**Q: Does the Launch function work on both web and mobile versions of Power Apps?**

Yes, on both platforms, but behavior may vary. On mobile it can open native apps directly (like the phone app for `tel:` links), while on web it typically opens in the browser or prompts to open the associated application.

**Q: Can I use Launch to open other Power Apps or Power BI reports?**

Yes. Launch other apps using their web URLs, or use deep links for Power BI reports. For Power Apps use: `Launch("https://apps.powerapps.com/play/[app-id]?tenantId=[tenant-id]")`.

**Q: Are there any security considerations when using Launch with external URLs?**

Yes. Always validate URLs before using Launch, especially from user input. Consider a whitelist of approved domains and avoid launching URLs that could redirect to malicious sites.
