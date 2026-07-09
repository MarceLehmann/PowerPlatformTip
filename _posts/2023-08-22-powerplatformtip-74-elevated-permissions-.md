---
title: "#PowerPlatformTip 74 – 'Elevated Permissions'"
date: 2023-08-22
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - Power Automate
  - Elevated Permissions
  - Security
  - Impersonation
  - Data Connections
  - SharePoint
  - Flow
excerpt: "Run PowerApps data connections with elevated permissions using Power Automate flows—enable secure actions beyond user rights, leveraging impersonation and advanced security."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge

You want to run data connections in PowerApps with elevated permissions, allowing users with limited access to perform actions they normally couldn't—like creating items in a SharePoint list they only have read access to.

## ✅ Solution

Use Power Automate flows to run data connections with elevated permissions. This lets you act as an admin or service account, similar to the Impersonation Step action in SharePoint Designer workflows.

## 🔧 How It's Done

**1. Understand PowerApps security**

🔸 Learn how PowerApps security works with data connections and sharing.

🔸 Ensure connectors and app sharing roles are configured correctly.

**2. Integrate Power Automate**

🔸 Call a Power Automate flow from Power Apps using the V2 connector.

🔸 Build the flow to connect to data sources with elevated permissions.

**3. Configure impersonation**

🔸 Use the "Run-only users" setting to specify an admin or service account.

🔸 Grant only the intended users permission to trigger the flow.

## 🎉 Result

You've set up PowerApps to run data connections with elevated permissions, allowing users to perform actions beyond their normal permissions—securely and in a controlled way.

## 🌟 Key Advantages

🔸 Enhanced User Experience: Users can perform actions beyond their normal permissions

🔸 Security & Flexibility: Maintain security while controlling how data connections run

🔸 Seamless Integration: PowerApps and Power Automate work together to extend functionality

## 🎥 Video Tutorial

{% include video id="ts-ggDAy7IQ" provider="youtube" %}

## 🛠️ FAQ

**Q: How do I grant elevated permissions without exposing credentials?**

Use the 'Run-only users' setting in Power Automate: the flow runs under its owner's credentials, so app users don't need to know service account details.

**Q: Can any user trigger the flow with elevated rights?**

Only users explicitly added as run-only users can trigger the flow; the Power Apps V2 connector enforces this access control.

**Q: Are there any licensing requirements for elevated flow execution?**

The flow executes under the owner's license; ensure the owner has the required connector and premium licenses so the flow can run with elevated permissions for all users.
