---
title: "#PowerPlatformTip 29 – 'ParseJSON Description'"
date: 2023-02-15
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

## 📝 TL;DR
When utilizing the Parse JSON action in Power Automate, distinguishing between multiple occurrences of the same name in Dynamic Content can be challenging, leading to confusion about which value corresponds to which name.

## 💡 Challenge
When utilizing the Parse JSON action in Power Automate, distinguishing between multiple occurrences of the same name in Dynamic Content can be challenging, leading to confusion about which value corresponds to which name.

## ✅ Solution
Enhance clarity and organization of Dynamic Content by incorporating a custom description within the Parse JSON schema. This simple adjustment allows you to differentiate between similar entries more effectively.

## 🔧 How It's Done
* In your Parse JSON action, after specifying the type for an element, add an additional line with "Description": "YOURDESCRIPTION". This custom description should provide clarity on the purpose or origin of the data.

* Example Schema Adjustment:

{

  "properties": 
{

    "FieldName": 
{

      "type": "string",

      "Description": "This is the description for FieldName"

    }}}

* Upon implementing this change, the description you've added will appear beneath the corresponding Dynamic Content in Power Automate, guiding you to accurately select the right value for your flow operations.

## 🎉 Result
A more intuitive and manageable way to work with Dynamic Content in Power Automate, significantly reducing the risk of errors when dealing with multiple occurrences of the same name.

## 🌟 Key Advantages
🔸 **Improved Clarity:** Custom descriptions make it easier to understand the context and purpose of each piece of Dynamic Content. 
🔸 **Enhanced Organization:** Keeps your flow design tidy and well-documented, facilitating easier maintenance and updates. 
🔸 **Increased Accuracy:** Minimizes confusion and improves the accuracy of your flow's logic by clearly identifying each data element.

This approach not only simplifies the process of working with complex JSON structures but also enhances the overall reliability and effectiveness of your automated workflows.

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