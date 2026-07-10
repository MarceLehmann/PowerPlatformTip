---
title: "#PowerPlatformTip 124 – 'Recognize Plain Text File Formats'"
date: 2024-09-18
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - JSON
  - CSV
  - PlainText
  - OneDriveForBusiness
  - PowerPlatformTip
excerpt: "Learn how to use plain text file formats in Power Automate's Get File Content action to simplify processing by avoiding Base64 decoding."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Skip Base64 decoding in Power Automate – plain-text formats like JSON, CSV, XML and Markdown return content directly from 'Get File Content'.

## 💡 Challenge
The "Get File Content" action in Power Automate often returns file contents as Base64, which complicates further processing. Yet some formats return their content directly as plain text — making things much simpler.

## ✅ Solution
Use plain-text formats such as JSON, HTML, CSV, TXT, XML, Markdown, YAML, CSS, JavaScript, and log files to get content directly, without any Base64 decoding.

## 🔧 How It's Done

**1. Retrieve the file with "Get File Content"**

🔸 Configure the connector (OneDrive for Business, SharePoint, etc.).

🔸 Select the target file in your flow.

**2. Identify plain-text formats**

🔸 JSON, HTML, CSV, TXT, XML, Markdown (.md), YAML (.yaml/.yml), CSS, JavaScript (.js), and .log files.

🔸 Make sure the file has the correct extension for plain text.

**3. Process the content directly**

🔸 Use variables, Compose actions, or expressions on the plain text.

🔸 Skip any Base64-decoding actions.

**4. Validate with a CSV on OneDrive for Business**

🔸 Test a CSV retrieval to confirm plain-text output.

🔸 Adjust your flow logic based on the direct CSV content.

## 🎉 Result
Using plain-text formats saves time and cuts complexity in your automations. You work directly with the content, making your flow more efficient and straightforward.

## 🌟 Key Advantages

🔸 No Base64 decoding needed — immediate use of file contents

🔸 Simplifies and speeds up further processing

🔸 Ideal for common automation and data tasks

---

## 🎥 Video Tutorial
{% include video id="ZUywICtR4Vo" provider="youtube" %}

---

## 🛠️ FAQ
**1. Which file formats are recognized as plain text in Power Automate?**
JSON, HTML, CSV, TXT, XML, Markdown (.md), YAML (.yaml/.yml), CSS, JavaScript (.js), and .log files are output as plain text by "Get File Content."

**2. Do all connectors support plain text output?**
Plain-text output depends on the connector and the file type. "Get File Content" in OneDrive for Business and SharePoint supports these text formats directly.

**3. How do I handle formats that output as Base64?**
For Base64 outputs, use a "Compose" action or the `base64ToString()` expression to decode the content before processing.

## 🔗 Related Tips
- [#PowerPlatformTip 125 – Convert CSV to JSON](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-125-convert-csv-to-json/) — turn plain-text CSV into JSON with standard actions.
- [#PowerPlatformTip 104 – Efficient JSON Handling](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-104-efficient-json-handling/) — process JSON payloads cleanly in flows.
