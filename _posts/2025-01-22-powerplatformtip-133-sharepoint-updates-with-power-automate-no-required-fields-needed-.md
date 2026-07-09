---
title: "#PowerPlatformTip 133 – 'SharePoint Updates with Power Automate – No Required Fields Needed'"
seo_title: "#PowerPlatformTip 133 – SharePoint Updates without Required Fields"
date: 2025-01-22
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - SharePoint
  - PowerAutomate
  - JSON
  - UpdateItem
  - FieldMapping
  - PowerPlatformTip
excerpt: "Update specific SharePoint fields in Power Automate without HTTP requests or required fields."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Update only specific SharePoint fields in Power Automate by passing a JSON variable to 'Update item' – no HTTP, no required-field hassle.

## 💡 Challenge
Updating only specific fields in SharePoint items can be tricky. It often feels like you're forced to fill unnecessary required fields or fall back to raw HTTP requests. Wouldn't it be easier to just update the fields you need?

## ✅ Solution
Use dynamic JSON from a variable to update only the necessary fields in a SharePoint item — quickly and efficiently, without extra overhead.

## 🔧 How It's Done

**1. Define the trigger**

🔸 Choose a suitable trigger, e.g. "When an item is created or modified" in SharePoint.

**2. Prepare the JSON data**

🔸 Initialize a variable or Compose action (e.g. `UpdateData`) with a JSON object containing only the fields to update:

```json
{
    "Status": "Completed"
}
```

**3. Update the item with dynamic data**

🔸 Add the "Update item" action.

🔸 Set the Site URL as usual; for the list, use the display name via `string('List Name')`.

🔸 For the fields, embed the JSON variable `UpdateData` to apply all updates in one step.

**4. Test the flow**

🔸 Confirm that only the specified fields update and that required fields cause no issues.

## 🎉 Result
Your flow is streamlined and flexible — it updates only the fields you need, saving time and reducing manual effort.

## 🌟 Key Advantages

🔸 No hassle with unnecessary required fields

🔸 Flexible updates using dynamic JSON data

🔸 Clean and maintainable flow structure

---

## 🎥 Video Tutorial
{% include video id="Nco3uk7q7yY" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can I update multiple fields simultaneously?**
Yes. Include multiple key-value pairs in the JSON variable to update several fields at once.

**2. What happens to required fields not included in the JSON?**
Required fields not included remain unchanged; the flow won't prompt for them when using dynamic JSON updates.

**3. Can this approach be used for other data sources?**
While designed for SharePoint, the dynamic-JSON update concept can be adapted to other connectors that accept JSON payloads.

---