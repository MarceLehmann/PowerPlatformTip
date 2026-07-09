---
title: "#PowerPlatformTip 141 – Text to Array"
date: 2025-08-19
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - Expression
  - Split
  - Array
  - DataProcessing
  - PowerPlatformTip
excerpt: "Convert multiline text into an array in Power Automate using split() — ideal for processing lists from Excel, emails or Power Apps."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Turn a multiline text block into a loopable array in Power Automate with `split(text, separator)`.

## 💡 Challenge
How do you process a copied multiline text block — each line a record (IDs, email addresses, URLs) — in a Power Automate flow without splitting it by hand? Manual steps don't scale and are error-prone.

## ✅ Solution
Use the `split()` expression to turn the multiline string into an array. With a simple separator (a line break, comma, or any character) you get an array you can loop through with "Apply to each".

## 🔧 How It's Done

**1. Capture the text**

🔸 Add a Compose action and paste your multiline text into it. Name it `DataInput`.

**2. Define the separator**

🔸 Add a second Compose containing only a line break (press Enter in the input). Name it `Separator`.

**3. Loop the array**

🔸 Add an Apply to each control and set its input to:

```
split(outputs('DataInput'), outputs('Separator'))
```

**4. Process each line**

🔸 Inside the loop, use `Current item` to trim, validate, call an API, or create records.

## 🎉 Result
Your flow now accepts any multiline text block and processes each line as a separate item. No more copy-paste, no manual cleanup — just reliable automation that scales.

## 🌟 Key Advantages

🔸 Saves time by automating repetitive data preparation

🔸 Flexible: works with lists from Excel, emails, Power Apps, or paste operations

🔸 Reduces human errors from manual handling

🔸 Scales to hundreds or thousands of lines without extra effort

---

## 🎥 Video Tutorial
{% include video id="spDM1XqmwuE" provider="youtube" %}

---

## 🛠️ FAQ
**1. What if my data is comma-separated instead of line breaks?**
Replace the `Separator` Compose content with a comma. The same `split()` expression produces the array.

**2. Can the text originate from a Power App?**
Yes. Pass a multiline text input from Power Apps into the flow; the split logic stays identical.

**3. How do I handle empty lines from accidental extra newlines?**
Add a condition inside the loop to check that `trim(Current item)` is not empty before processing.

---