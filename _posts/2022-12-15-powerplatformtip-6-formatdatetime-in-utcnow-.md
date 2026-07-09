---
title: "#PowerPlatformTip 6 – 'formatDateTime in utcNow'"
date: 2022-12-15
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - powerautomate
  - date-formatting
  - utcnow
  - flow-optimization
  - productivity
excerpt: "Format dates in Power Automate with utcNow: Skip extra functions, simplify flows, and boost efficiency with direct date formatting."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 💡 Challenge
Working with dates and times often requires using formatDateTime with utcNow to format values, adding unnecessary complexity and extra steps in your flow.

## ✅ Solution
Format the date directly within utcNow by passing your desired format string, eliminating the separate formatDateTime function.

## 🔧 How It's Done

**1. Use utcNow with format parameter**

🔸 Instead of using `formatDateTime(utcNow(), 'your-format')`, call `utcNow('your-format')`.

**2. Apply your date-time format**

🔸 Use the same format string you need directly inside `utcNow`.

**3. Test your flow**

🔸 Run and verify your flow in a non-production environment to ensure it works as expected.

## 🎉 Result
By directly formatting dates within utcNow, you simplify and streamline your flows, reducing steps and improving readability and performance.

## 🌟 Key Advantages

🔸 **Simplicity:** Eliminates the need for an additional `formatDateTime` function.

🔸 **Efficiency:** Reduces the number of expressions in your flow.

🔸 **Clarity:** Makes your flow easier to read and maintain.

---

## 🛠️ FAQ

**1. What format strings can I use with utcNow()?**

You can use standard .NET DateTime format strings like 'yyyy-MM-dd', 'HH:mm:ss', or custom combinations to format the date and time as needed.

**2. Is utcNow() always in UTC timezone?**

Yes, utcNow() always returns the current time in UTC. If you need local time, consider using the convertTimeZone() function.

**3. Can I combine utcNow() formatting with other functions?**

Absolutely! You can chain utcNow() with other functions like addDays(), addHours(), or use it within expressions for complex date calculations.
