---
title: "#PowerPlatformTip 128 – 'Dynamic Data Retrieval'"
date: 2024-10-31
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - JSON
  - ParseJSON
  - DynamicDataRetrieval
  - PowerPlatformTip
excerpt: "Use Parse JSON with dynamic keys in Power Automate to flexibly retrieve data without complex conditions."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Pull values from JSON dynamically in Power Automate using Parse JSON with variable keys – no Switch or If cascades.

## 💡 Challenge
Handling dynamic data in Power Automate often pushes you toward sprawling Switch or If structures — one branch per language, user role or message type. That gets hard to maintain fast.

## ✅ Solution
Use the **Parse JSON** action together with a dynamic key expression to pull values straight from a JSON structure. You reference the property by a variable instead of hardcoding it, so the same expression returns different content (greetings, settings, user data) based on need.

## 🔧 How It's Done

**1. Parse your JSON**

🔸 Add a Parse JSON action and generate the schema from a sample payload.

**2. Reference a value by dynamic key**

🔸 Instead of hardcoding, build the property path from a variable, e.g. `body('Parse_JSON')?[variables('key')]`.

**3. Drive the key from context**

🔸 Set the key from the language, user role or message type so one expression returns the right content.

**4. Handle missing keys**

🔸 Wrap it with `coalesce(body('Parse_JSON')?[variables('key')], 'default')` to fall back gracefully.

## 🎉 Result
You get an agile, scalable flow that retrieves and processes data in real time — no cascade of conditions to maintain as new data variations appear.

## 🌟 Key Advantages

🔸 No complex Switch/If conditions

🔸 Quick to adapt for new data variations

🔸 Flexible across many use cases

---

## 🎥 Video Tutorial
{% include video id="NuFd6myyUio" provider="youtube" %}

---

## 🛠️ FAQ
**1. How do I generate the JSON schema for the Parse JSON action?**
Copy a sample JSON payload and use the "Use sample payload to generate schema" button in the action to create the schema automatically.

**2. What happens if a key doesn't exist in the JSON?**
The Parse JSON action still runs but returns null for missing keys. Use expressions like `coalesce()` or conditional steps to provide default values.

**3. Can I use this approach for nested JSON objects?**
Yes. Access nested objects by chaining property names, for example `body('Parse_JSON')?['data']?['key']`.

## 🔗 Related Tips
- [#PowerPlatformTip 104 – Efficient JSON Handling](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-104-efficient-json-handling/) — more techniques for working with JSON in flows.
- [#PowerPlatformTip 33 – Coalesce](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-33-coalesce/) — provide clean fallbacks for missing values.
