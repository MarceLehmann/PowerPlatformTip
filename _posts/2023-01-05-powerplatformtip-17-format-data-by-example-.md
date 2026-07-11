---
title: "#PowerPlatformTip 17: 'Format data by example'"
date: 2023-01-05
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - data-formatting
  - expressions
  - copilot
  - productivity
  - PowerPlatformTip
excerpt: "Master data formatting in Power Automate! Use 'Format data by example', or its Copilot successor, the expression assistant, to generate accurate expressions for dates, strings and numbers."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Let Power Automate write the formatting expression for you, give an example (or describe it to the Copilot expression assistant) and it generates the syntax for dates, strings and numbers.

Writing expressions to format dates, strings and numbers by hand is fiddly and error-prone.
Power Automate can generate the expression for you from an example of the output you want, no need to know the exact functions or syntax.

> **Note (2025+):** The classic **Format data by examples** feature has been deprecated and hidden in the Power Automate designer. Its successor is the **Copilot expression assistant** in the expression editor, which does the same job using natural language. The workflow below applies to both, you describe or exemplify the output, and Power Automate builds the expression.

## 💡 Challenge
Creating complex expressions for formatting dates, strings and numbers is time-consuming and easy to get wrong in Power Automate.

## ✅ Solution
Let Power Automate generate the expression for you. Provide an example of the desired output (classic *Format data by example*) or describe it in natural language (the newer **Copilot expression assistant**), and it returns the matching expression.

## 🔧 How it's done

**1. Open the expression editor**

🔸 In an action's text field, open **Expression**, then choose the expression assistant (or, on older tenants, *Format data by examples*).

**2. Provide an example or description**

🔸 Give a sample of the source value and how you want it formatted, or simply describe the target format in words.

**3. Get and test the expression**

🔸 Power Automate suggests an expression. Test it with another value to confirm it produces what you expect.

**4. Apply it**

🔸 Insert the expression into your flow for consistent, accurate formatting.

## 🎉 Result
You build correct formatting expressions in seconds instead of hand-writing syntax, accurate and consistent across your flows.

## 🌟 Key Advantages

🔸 **Simplifies complex expressions:** no need to memorise function syntax.

🔸 **Saves time and reduces errors** for dates, strings and numbers alike.

🔸 **Consistent formatting** across your Power Automate projects.

## 🎥 Video Tutorial
{% include video id="wKTVzcU7KnA" provider="youtube" %}

---

## 🛠️ FAQ

**Q1: What types of data formatting does this support?**

Dates, numbers and text patterns, for example reformatting a date, adding thousands separators, or building a combined string from several fields.

**Q2: Can I use it for multi-column formatting?**

Yes. You can combine values from multiple fields into a single formatted output string.

**Q3: I can't find 'Format data by example' anymore, where did it go?**

Microsoft deprecated and hid the classic feature (from around August 2025). Use the **Copilot expression assistant** in the expression editor instead, it replaces it and generates expressions from natural-language descriptions.
