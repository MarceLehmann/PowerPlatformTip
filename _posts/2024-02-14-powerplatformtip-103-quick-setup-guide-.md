---
title: "#PowerPlatformTip 103 – 'Quick Setup Guide'"
date: 2024-02-14
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerApps
  - SharePoint
  - Dataverse
  - ComboBox
  - Choices
  - PowerPlatformTip
excerpt: "Quickly configure dropdowns and ComboBoxes in PowerApps using SharePoint or Dataverse Lookup and Choice columns for rapid, reliable data selection."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Populate Power Apps dropdowns and ComboBoxes fast by pointing their `Items` at SharePoint/Dataverse Lookup or Choice columns via `Choices()`.

## 💡 Challenge
You need a dropdown or ComboBox populated quickly — under time pressure or as a temporary solution — without building and maintaining a separate data table.

## ✅ Solution
Point the control's `Items` at an existing **Lookup** or **Choice** column in SharePoint or Dataverse using `Choices()`. The valid values come straight from the column definition.

## 🔧 How It's Done

**1. Prepare your data source**

🔸 Create a **Lookup** column (Dataverse or SharePoint) for relational data, or a **Choice** column for simple picklists.

**2. Configure the control**

🔸 Add a Dropdown or ComboBox to the canvas.

🔸 Point its `Items` at the column with `Choices()`:

🔸 Dataverse: `Choices([@Tests].cr0a0_LookupAccount)` — `[@Tests]` is the table, `cr0a0_LookupAccount` the lookup/choice column.

🔸 SharePoint: `Choices('Your List'.YourChoiceColumn)`

## 🎉 Result
A swift, reliable way to feed user inputs in PowerApps, balancing speed and data integrity — ideal for projects that need immediate results or tight deadlines.

## 🌟 Key Advantages

🔸 **Speed:** rapid app development and deployment.

🔸 **Efficiency:** streamlines integrating data into PowerApps.

🔸 **Practicality:** a viable solution when time or resources are limited.

---

## 🎥 Video Tutorial
{% include video id="1w8ifafAQus" provider="youtube" %}

---

## 🛠️ FAQ
**1. What is this fast-setup approach in PowerApps?**
Pointing a Dropdown/ComboBox `Items` at a SharePoint or Dataverse Lookup/Choice column via `Choices()` populates it instantly, without a separate data table.

**2. Can this method be used with both SharePoint and Dataverse?**
Yes. Use SharePoint Lookup/Choice columns or Dataverse Lookup columns to source the control's values.

**3. Are there any limitations when using the `Choices()` function?**
`Choices()` returns all values from a Lookup or Choice column but may not support advanced filtering or custom formatting. Watch delegation limits and test performance on large datasets.

---
