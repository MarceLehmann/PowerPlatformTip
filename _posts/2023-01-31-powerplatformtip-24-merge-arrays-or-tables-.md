---
title: "#PowerPlatformTip 24 – 'Merge arrays or tables'"
date: 2023-01-31
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - power automate
  - arrays
  - tables
  - data manipulation
  - concat
excerpt: "Merge arrays or tables in Power Automate while preserving duplicates using concat and split functions. Simplify data manipulation workflows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Merge two arrays and keep duplicates by joining each with a delimiter, concatenating, then splitting back — instead of union which drops duplicates.

## 💡 Challenge
You need to merge two arrays in Power Automate but keep the duplicates. The `union` function merges arrays, but it removes duplicates and returns only unique values.

## ✅ Solution
Instead of `union`, concatenate the arrays with a unique delimiter and then split the result back into an array. This preserves every element, including duplicates.

## 🔧 How It's Done

1. **Join each array** into a string using a unique delimiter (`||`).

2. **Concatenate** both strings, keeping the delimiter between them.

3. **Split** the combined string back into an array using the same delimiter – all elements, duplicates included, are restored.

Here's the expression:

```
split(
  concat(
    join(outputs('Compose_-_2_arrays')?['array1'], '||'),
    '||',
    join(outputs('Compose_-_2_arrays')?['array2'], '||')
  ),
  '||'
)
```

## 🎉 Result
You merge both arrays while keeping all duplicate values – something the standard `union` function does not allow.

## 🌟 Key Advantages
🔸 Inclusivity: every element is kept, duplicates included.

🔸 Flexibility: adjust the formula for simple lists or more complex data structures.

🔸 Power: manipulate data in ways the standard functions don't directly allow.

---

## 🛠️ FAQ
**1. What happens if my array contains values that include the delimiter '||'?**

Choose a unique delimiter that doesn't appear in your data, or use a more complex delimiter like '###DELIMITER###'.

**2. Can this method handle arrays with different data types?**

Yes, but ensure all values can be converted to strings for the join operation, then convert back to appropriate types if needed.

**3. Is there a performance impact when merging large arrays?**

For very large arrays, consider using the union() function for simple merging without duplicates, or batch processing for better performance.

---
