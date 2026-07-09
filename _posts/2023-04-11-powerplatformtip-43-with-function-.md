---
title: "#PowerPlatformTip 43 – 'With function'"
date: 2023-04-11
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerapps
  - with function
  - code readability
  - maintainability
  - formulas
excerpt: "Use the With function in PowerApps to group variable declarations and simplify complex formulas for improved code readability and maintainability."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Use the With function to declare local variables in one block and keep complex formulas like Haversine readable and maintainable.

## 💡 Challenge
Complex calculations and expressions in PowerApps can lead to code that's hard to read and maintain. For example, calculating the distance between two points using the Haversine formula can clutter your code with repetitive variable declarations.

## ✅ Solution
The "With" function enhances code readability and maintainability. By defining multiple variables within a single block, it streamlines complex expressions like the Haversine formula.

## 🔧 How It's Done

* **Step 1:** Use the "With" function to define all necessary variables for the calculation – for example the radius of Earth, the differences in latitude and longitude, and the formula terms.

* **Step 2:** Refer to these variables directly within your formula, avoiding repetition and keeping the code clean.

* **Example:**

  ```
  With({var1: value1, var2: value2}, YourFormulaHere)
  ```

## 🎉 Result
A more concise, organized approach to complex formulas. The "With" function encapsulates variable declarations, making the code easier to read and maintain.

## 🌟 Key Advantages
* **Improved Readability:** Reduces clutter by grouping variable declarations.

* **Ease of Maintenance:** Updates to variables or logic require changes in only one place.

* **Enhanced Performance:** Can optimize your app by streamlining expressions.

> ℹ️ Tip: Use With judiciously – over-abstracting can hurt readability for others unfamiliar with your logic.

## 🎥 Video Tutorial
{% include video id="GlCfiZD8YQk" provider="youtube" %}

---

## 🛠️ FAQ
**1. Can I nest multiple With functions within each other?**

Yes, you can nest With functions, but for better readability, consider using a single With function with multiple variables instead.

**2. What's the difference between With function and Set function for variables?**

With creates local variables within its scope only, while Set creates global variables accessible throughout the app. Use With for temporary calculations.

**3. Can I use With function with complex data types like collections or records?**

Yes, With works with all data types including collections, records, and tables, making it versatile for complex calculations and data manipulations.

---
