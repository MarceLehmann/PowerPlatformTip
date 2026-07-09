---
title: "#PowerPlatformTip 56 – 'Empowering Tools in CoE'"
date: 2023-05-30
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Power Platform
  - Center of Excellence
  - CoE
  - Governance
  - Administration
  - Monitoring
  - Security
  - Best Practices
  - PowerPlatformTip
excerpt: "Empower your Power Platform Center of Excellence (CoE) with essential tools. Discover how to streamline governance, monitoring, and administration for scalable, secure, and efficient Power Platform adoption."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Use the CoE Kit's Set Flow/Apps Permissions tools and orphan detection to see who has access and auto-handle ownerless flows and apps.

## 💡 Challenge

Managing permissions and ownership in the Center of Excellence (CoE) Kit can be difficult. It's hard to know who has access to flows and apps, and orphaned resources get left behind when people leave the company.

## ✅ Solution

Leverage the CoE Kit's built-in tools—'Set Flow Permissions', 'Set Apps Permissions' and the orphan detection flow—to gain clear visibility, manage access, and automatically handle orphaned flows and apps.

## 🔧 How It's Done

**1. Use the Set Flow Permissions tool**

🔸 View which users have access to each flow.

🔸 Assign new flow permissions directly within the tool.

**2. Use the Set Apps Permissions tool**

🔸 View which users have access to each app.

🔸 Assign new app permissions quickly and securely.

**3. Enable orphan detection under Governance Components**

🔸 Identify flows and apps without an owner.

🔸 Automatically alert the departed user's manager to reassign permissions.

## 🎉 Result

You gain comprehensive visibility into who can access your resources, streamline permission management, and ensure no flow or app remains orphaned—improving security and operational efficiency.

## 🌟 Key Advantages

🔸 Complete visibility of user permissions for flows and apps

🔸 Simplified management of access rights directly from the CoE Kit

🔸 Automated detection and handling of orphaned flows and apps

## 🛠️ FAQ

**Q: What is the CoE Kit?**

The Center of Excellence (CoE) Kit is a collection of Power Platform components designed to help organizations govern, monitor, and manage their Power Apps and flows at scale.

**Q: How do I use the Set Flow Permissions tool?**

Open the CoE Kit and navigate to the 'Set Flow Permissions' tool to view current permissions and assign or revoke access for individual users.

**Q: How does the orphan detection flow work?**

The orphan detection flow scans for flows and apps without active owners and automatically notifies the departed user's manager, enabling timely reassignment of permissions.
