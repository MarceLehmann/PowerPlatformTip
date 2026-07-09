---
title: "#PowerPlatformTip 29 – 'ParseJSON Description'"
date: 2023-02-15
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - power automate
  - parsejson
  - dynamic content
  - json schema
  - automation
excerpt: "Add custom descriptions in Power Automate's Parse JSON action to organize and distinguish similar Dynamic Content entries. Improve flow clarity."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge
When using the Parse JSON action in Power Automate, distinguishing between multiple occurrences of the same name in Dynamic Content can be difficult, leading to confusion about which value corresponds to which name.

## ✅ Solution
Add a custom `Description` inside the Parse JSON schema. This description appears under the Dynamic Content entry, letting you tell similar entries apart.

## 🔧 How It's Done

1. In your Parse JSON action, add a `"Description"` property to an element in the schema, after its `type`:

   ```json
   {
     "properties": {
       "FieldName": {
         "type": "string",
         "Description": "This is the description for FieldName"
       }
     }
   }
   ```

2. The description you added now appears beneath the corresponding Dynamic Content in Power Automate, guiding you to the right value.

## 🎉 Result
A more intuitive way to work with Dynamic Content in Power Automate, reducing the risk of errors when dealing with multiple occurrences of the same name.

## 🌟 Key Advantages
🔸 **Improved Clarity:** Custom descriptions explain the context and purpose of each Dynamic Content entry.

🔸 **Enhanced Organization:** Keeps your flow design tidy and well-documented.

🔸 **Increased Accuracy:** Minimizes confusion by clearly identifying each data element.

## 🎥 Video Tutorial
{% include video id="sh2QDZouFU0" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can I add descriptions to all field types in Parse JSON schema?**

Yes, descriptions can be added to any field type (string, number, boolean, array, object) in your JSON schema.

**2. Do these descriptions affect the actual JSON parsing process?**

No, descriptions are metadata that only affect the Power Automate interface and don't impact the parsing functionality.

**3. Is there a character limit for field descriptions?**

While there's no strict limit, keep descriptions concise for better readability in the Dynamic Content pane.

---
