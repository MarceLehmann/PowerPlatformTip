---
title: "#PowerPlatformTip 18 – 'Download & Save Files'"
date: 2023-01-10
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - file-download
  - file-management
  - http-request
  - automation
  - PowerPlatformTip
excerpt: "Download and save public or password-protected files in Power Automate using HTTP requests and file management actions. Ensure secure, automated file handling."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Download files in a flow with 'Upload file from URL' for public files, or an authenticated HTTP request plus 'Create file' for protected ones.

Downloading files in a flow works differently depending on whether the file is openly accessible or behind authentication.
Use the right action for each case: a simple URL action for public files, and an authenticated HTTP request for protected ones.

## 💡 Challenge
Public and password-protected files need different handling — one approach doesn't cover both accessibility and security.

## ✅ Solution
Use two methods depending on the source: **Upload file from URL** for public files, and **HTTP request + Create file** for files that require authentication.

## 🔧 How it's done

**1. Public files**

🔸 Use the **Upload file from URL** action — straightforward for files that are openly accessible online.

**2. Password-protected files**

🔸 Use an **HTTP** request with the correct authentication headers to fetch the file, then a **Create file** action to save the returned content.

## 🎉 Result
A reliable, secure process for downloading and saving files regardless of whether they're public or protected.

## 🌟 Key Advantages

🔸 **Secure handling** of sensitive, authenticated files.

🔸 **Simple path** for public files with a single action.

🔸 **Streamlined file management** in your Power Platform solutions.

---

## 🛠️ FAQ

**Q1: What file types can I download and save?**

Many formats work — documents (PDF, Word, Excel), images (JPG, PNG) and others supported by Power Automate.

**Q2: How do I handle authentication for protected files?**

Use the **HTTP** action with the appropriate authentication (Basic, Bearer token or OAuth) for the source's security requirements.

**Q3: Are there size limits when downloading files?**

Yes. Power Automate has file-size and execution-time limits. For large files, consider chunking or premium connectors.
