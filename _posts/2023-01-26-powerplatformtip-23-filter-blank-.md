---
title: "#PowerPlatformTip 23: 'Filter Blank'"
date: 2023-01-26
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerapps
  - gallery
  - filtering
  - isblank
  - user input
excerpt: "Show all gallery items in PowerApps when filter input is blank using IsBlank in your filter logic. Improve user experience and data access."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Add || IsBlank(YourFilterInput) to a gallery's Filter so it shows every item when the search box is empty.

## 💡 Challenge
Filtering galleries in PowerApps based on user input (like text input, dropdown, or combo box) is common, but when the input is empty you usually want to show all items.

## ✅ Solution
Add an `|| IsBlank(YourFilterInput)` condition to your filter formula.

## 🔧 How It's Done

1. Create a gallery and set up your filter inputs (e.g., text input, dropdown, combo box).

2. Apply the following formula to your gallery's Items property:

   ```
   Filter(YourDataSource, Condition || IsBlank(YourFilterInput))
   ```

   🔸 `YourDataSource` is the source of your data.
   🔸 `Condition` is your filtering condition (e.g., `TextInput.Text = ThisItem.Field`).
   🔸 `YourFilterInput` is the input control (e.g., TextInput, Dropdown).

## 🎉 Result
When the filter input is empty, the gallery shows all items. If the input is provided, the gallery filters based on the specified condition.

## 🌟 Key Advantages
🔸 Simplifies gallery filtering logic.

🔸 Enhances user experience by dynamically displaying all or filtered data.

🔸 Reduces the need for multiple filtering conditions.

## 🎥 Video Tutorial
{% include video id="LsgqI7lM4qM" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can I use multiple filter conditions with the IsBlank() check?**

Yes, you can combine multiple conditions using && or || operators while still including the IsBlank() check for each filter input.

**2. Does this technique work with all data sources in PowerApps?**

Yes, this filtering approach works with SharePoint lists, Dataverse tables, SQL databases, and other supported data sources.

**3. How can I handle multiple filter inputs simultaneously?**

Create compound conditions like: `Filter(DataSource, (Condition1 || IsBlank(Input1)) && (Condition2 || IsBlank(Input2)))`.

---
