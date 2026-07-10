---
title: "#PowerPlatformTip 125: 'Convert CSV to JSON'"
date: 2024-09-25
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - CSV
  - JSON
  - DataTransformation
  - PowerPlatformTip
excerpt: "Convert CSV data into JSON in Power Automate using only standard actions without premium connectors or external services."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Convert CSV to JSON in Power Automate with only standard actions, split, Select and Parse JSON, no premium connector.

## 💡 Challenge
You need to convert CSV data into JSON in Power Automate, without premium connectors or external services.

## ✅ Solution
Use standard Power Automate actions to split the CSV and map it into JSON, quickly and directly, with no premium dependency.

## 🔧 How It's Done

**1. Split the CSV into lines**

🔸 Compose: `@split(outputs('CSV_File'), outputs('NewLine'))` to break the content into individual lines.

**2. Extract the field names**

🔸 Compose: `@split(first(outputs('SplitByLines')), ',')` to get the header row.

**3. Map fields to JSON**

🔸 Use a Select action to map each remaining line. Reference field names with `@{outputs('FieldNames')?[0]}` and values with `@split(item(), ',')?[1]`, continuing for each field.

**4. Count the fields**

🔸 Compose: `@length(outputs('FieldNames'))`.

**5. Parse to JSON**

🔸 Feed the mapped data into a Parse JSON action to finish the transformation.

## 🎉 Result
You convert CSV data into JSON entirely within Power Automate using standard actions, no premium connectors or external services required.

## 🌟 Key Advantages

🔸 Uses only standard Power Automate actions

🔸 Fast, direct conversion with no extra cost

🔸 Simplifies data handling and integration

---

## 🛠️ FAQ
**1. Do I need premium connectors to convert CSV to JSON?**
No. This approach uses only built-in Power Automate actions, no premium connectors or external services required.

**2. How can I handle CSV files with different delimiters?**
Adjust the `split` function to use your delimiter, for example `@split(item(), ';')` for semicolon-separated files.

**3. What if header names contain spaces or special characters?**
Use string functions like `replace()` to sanitize header values before mapping, ensuring valid JSON property names.

## 🔗 Related Tips
- [#PowerPlatformTip 124: Recognize Plain Text File Formats](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-124-recognize-plain-text-file-formats/), read CSV and other text files without Base64 decoding.
- [#PowerPlatformTip 104: Efficient JSON Handling](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-104-efficient-json-handling/), work with the resulting JSON efficiently.
