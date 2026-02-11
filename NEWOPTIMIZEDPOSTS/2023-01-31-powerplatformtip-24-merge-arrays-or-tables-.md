---
title: "#PowerPlatformTip 24 – 'Merge arrays or tables'"
date: 2023-01-31
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

## 📝 TL;DR
Ever find yourself wanting to merge two arrays in Power Automate, but you hit a snag because you need to keep those pesky duplicates? If you've tried the union function, you know it's a neat trick for merging arrays, but alas, it leaves behind any duplicates, aiming for uniqueness like it's going out of style.

## 💡 Challenge
Ever find yourself wanting to merge two arrays in Power Automate, but you hit a snag because you need to keep those pesky duplicates? If you've tried the union function, you know it's a neat trick for merging arrays, but alas, it leaves behind any duplicates, aiming for uniqueness like it's going out of style.

## ✅ Solution
Fear not! There's a workaround that's not just a workaround, but a magic trick waiting to be performed. It involves a bit of array alchemy—concatenating the arrays and then pulling a "now you see me, now you don't" with the duplicates.

## 🔧 How It's Done
Let’s break down the spell:

* **Conjure Your Arrays Together:** Use the concat function to merge your two arrays into one. Think of it as inviting all the elements to a grand ball, duplicates included.

* **The Secret Sauce – '||':** To keep track of where one array ends and the other begins, we use a unique delimiter, '||'. This is like giving each guest at the ball a unique mask.

* **Split to Reveal:** Now, the grand finale. Use the split function to turn this merged string back into an array, using the same '||' delimiter to remove the masks and reveal the identities of all your elements, duplicates proudly standing.

Here's the incantation:

split(
concat(
join(outputs('Compose_-_2_arrays')?['array1′],'||'),
'||',
join(outputs('Compose_-_2_arrays')?['array2'],'||')),
'||')

## 🎉 Result
Voilà! You’ve mastered the art of merging arrays while honoring the presence of duplicates. This isn't just merging; it's merging with style and intelligence.

## 🌟 Key Advantages
* **Inclusivity:** Every element gets to join the party, duplicates don’t get left out in the cold.

* **Flexibility:** Adjust the formula to fit your specific scenario, whether it's for simple lists or complex data structures.

* **Power:** Empowers you to manipulate data in ways that standard functions don’t directly allow.

Merge arrays, keep the duplicates, and do it all with a flourish. This tip isn't just a solution; it's a performance. Enjoy the show!

## 🎥 Video Tutorial
{% include video id="noscript" provider="youtube" %}

---

## 🛠️ FAQ
**1. What happens if my array contains values that include the delimiter '||'?**  
Choose a unique delimiter that doesn't appear in your data, or use a more complex delimiter like '###DELIMITER###'.

**2. Can this method handle arrays with different data types?**  
Yes, but ensure all values can be converted to strings for the join operation, then convert back to appropriate types if needed.

**3. Is there a performance impact when merging large arrays?**  
For very large arrays, consider using the union() function for simple merging without duplicates, or batch processing for better performance.

---