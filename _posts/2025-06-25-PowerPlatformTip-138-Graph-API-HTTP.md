---
title: "#PowerPlatformTip 138: 'Graph API via HTTP with Microsoft Entra ID'"
seo_title: "Microsoft Graph API in Power Automate via HTTP"
date: 2025-06-25
last_modified_at: 2026-07-10
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - GraphAPI
  - HTTP
  - MicrosoftEntraID
  - PowerPlatformTip
excerpt: "Use the preauthorized 'HTTP with Microsoft Entra ID' connector in Power Automate to call Microsoft Graph without a custom app registration."
description: "Call Microsoft Graph in Power Automate without app registrations or secrets, use the preauthorized 'HTTP with Microsoft Entra ID' action. No OAuth setup."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Skip app registrations and secrets, the preauthorized "HTTP with Microsoft Entra ID" action calls Microsoft Graph directly. Point both the Base Resource URL and the Resource URI to `https://graph.microsoft.com`.

## 💡 Challenge
Calling Graph APIs in Power Automate traditionally meant registering a Microsoft Entra ID (formerly Azure AD) app, setting up client secrets or certificates, and configuring complicated OAuth flows, slow to set up and easy to break.

## ✅ Solution
Use the built-in "HTTP with Microsoft Entra ID (preauthorized)" action, sign in once, and point both the Base Resource URL and the Application ID URI to `https://graph.microsoft.com`.

## 🔧 How It's Done

**1. Add the action**

🔸 Insert "HTTP with Microsoft Entra ID (preauthorized)", authentication is already set to "Log in with Microsoft Entra ID".

**2. Set the Base Resource URL**

🔸 `https://graph.microsoft.com`

**3. Set the Microsoft Entra ID Resource URI**

🔸 `https://graph.microsoft.com`

**4. Pick the method and endpoint**

🔸 e.g. `GET https://graph.microsoft.com/v1.0/me`

**5. Run the flow**

🔸 The connector fetches and injects the token for you, no manual token handling.

## 🎉 Result
You get JSON responses from Graph in seconds, no app registration, no secrets, and no manual token handling.

## 🌟 Key Advantages

🔸 Zero custom app setup in Microsoft Entra ID

🔸 Automatic token acquisition and renewal

🔸 Easily extended to any Graph endpoint

---

## 🛠️ FAQ

**Q1: What permissions does it use?**

It leverages your own delegated permissions (e.g. `User.Read`).

**Q2: Can I use POST or PATCH methods?**

Yes, just pick the method and supply your body and headers as usual.

**Q3: How do I fetch Teams data?**

Change the endpoint to `/v1.0/teams/{team-id}`; the base URL stays the same.

## 🔗 Related Tips
- [#PowerPlatformTip 58: HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/), the fundamentals of building HTTP requests in Power Automate.
- [#PowerPlatformTip 96: Scraping Web Data with Standard Connectors](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-96-scraping-web-data-with-standard-connectors/), more no-premium HTTP patterns.
