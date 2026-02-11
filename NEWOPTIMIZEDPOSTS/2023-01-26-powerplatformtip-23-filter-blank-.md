---
title: "#PowerPlatformTip 23 – 'Filter Blank'"
date: 2023-01-26
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerapps
  - gallery
  - filtering
  - isblank
  - user input
excerpt: "Show all gallery items in PowerApps when filter input is blank using isblank in your filter logic. Improve user experience and data access."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Show all gallery items in PowerApps when filter input is blank using isblank in your filter logic. Improve user experience and data access.

## 💡 Challenge
Filtering galleries in PowerApps based on user input (like text input, dropdown, or combo box) is common.

## ✅ Solution
Use the "|| isblank(YOUR FILTERINPUT)" condition in your filter formula.

## 🔧 How It's Done
* Create a gallery and set up your filter inputs (e.g., text input, dropdown, combo box).
* Apply the following formula to your gallery's Items property:
Filter(YourDataSource, Condition || isblank(YOUR FILTERINPUT))
🔸 YourDataSource is the source of your data.
🔸 Condition is your filtering condition (e.g., TextInput.Text = ThisItem.Field).
🔸 YOUR FILTERINPUT is the input control (e.g., TextInput, Dropdown).

## 🎉 Result
When the filter input is empty, the gallery will show all items. If the input is provided, the gallery will filter based on the specified condition.

## 🌟 Key Advantages
🔸 Simplifies gallery filtering logic.
🔸 Enhances user experience by dynamically displaying all or filtered data.
🔸 Reduces the need for multiple filtering conditions.

## 🎥 Video Tutorial
{% include video id="LsgqI7lM4qM" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can I use multiple filter conditions with the isblank() check?**  
Yes, you can combine multiple conditions using && or || operators while still including the isblank() check for each filter input.

**2. Does this technique work with all data sources in PowerApps?**  
Yes, this filtering approach works with SharePoint lists, Dataverse tables, SQL databases, and other supported data sources.

**3. How can I handle multiple filter inputs simultaneously?**  
Create compound conditions like: `Filter(DataSource, (Condition1 || IsBlank(Input1)) && (Condition2 || IsBlank(Input2)))`