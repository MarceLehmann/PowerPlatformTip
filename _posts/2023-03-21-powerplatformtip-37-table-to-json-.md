---
title: "#PowerPlatformTip 37 – 'Table to JSON'"
date: 2023-03-21
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - power automate
  - table to json
  - parsejson
  - data transformation
  - automation
excerpt: "Convert two-column tables to JSON in Power Automate for easier data access. Use Parse JSON for efficient data transformation and automation."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Convert a two-column Name/Value table to a JSON record and run it through Parse JSON so you can access each entry directly.

## 💡 Challenge
Working with two-column tables – specifically 'Name' and 'Value' pairs – in Power Automate can be tedious when trying to access individual entries efficiently.

## ✅ Solution
Streamline the selection of individual entries by converting the table into a JSON record and using the "Parse JSON" action.

## 🔧 How It's Done

1. Convert your 'Name' and 'Value' table into a JSON record. This transformation allows more flexible data manipulation.

2. Use the "Parse JSON" action in Power Automate to structure the data, enabling straightforward access to any entry within your flow.

## 🎉 Result
Accessing and selecting data from two-column tables becomes seamless, saving time and reducing complexity.

## 🌟 Key Advantages
🔸 **Efficiency:** Quickly convert tabular data into a manipulable format.

🔸 **Simplicity:** Access individual data points without complex expressions.

🔸 **Flexibility:** Adapt the method for various data structures beyond simple name-value pairs.

## 🎥 Video Tutorial
{% include video id="Oxf1mnN6k0M" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can this method handle tables with multiple columns beyond name-value pairs?**

Yes, but you'll need to modify the JSON structure to accommodate additional columns, creating more complex object structures.

**2. What happens if my table contains special characters or spaces in the names?**

Special characters may need escaping in JSON. Consider using the replace() function to sanitize field names before conversion.

**3. Is there a size limit for tables when converting to JSON?**

While there's no strict limit, very large tables may impact flow performance. Consider batch processing for tables with thousands of rows.

---
