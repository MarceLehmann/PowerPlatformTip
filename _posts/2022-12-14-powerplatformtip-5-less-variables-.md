---
title: "#PowerPlatformTip 5 – 'Less Variables'"
date: 2022-12-14
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - power automate
  - parse json
  - flow optimization
  - variables
  - best practices
excerpt: "Reduce variables in Power Automate by using Parse JSON or Compose for static parameters. Keep flows readable and loop concurrency intact—reserve variables for values that actually change."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Hold static parameters in Parse JSON or Compose instead of Initialize Variable to keep flows readable and preserve loop concurrency.

## 💡 Challenge
In many Power Automate flows, you might find yourself using the 'Initialize Variable' action to store a parameter that never changes throughout the flow. It's like carrying a heavy toolbox when all you need is a single screwdriver!

## ✅ Solution
Use 'Parse JSON' (or 'Compose') to hold static parameters instead of 'Initialize Variable'. You avoid variables entirely—which keeps your flow readable and, importantly, doesn't block parallelism inside loops.

## 🔧 How It's Done

**1. Replace 'Initialize Variable'**

🔸 Swap out the 'Initialize Variable' action for 'Parse JSON' or 'Compose'.

**2. Set the JSON schema**

🔸 Define the JSON schema to match the parameter you want to set.

**3. Use in Flow**

🔸 Reference the parsed object wherever you would have used the variable.

## 🎉 Result
By using 'Parse JSON' for static parameters, your flow stays clean and its intent is clearer—and you keep the option to run 'Apply to each' loops with concurrency enabled.

## 🌟 Key Advantages

🔸 **Clarity:** Makes it obvious the parameter is static and won't change, improving readability.

🔸 **Concurrency-friendly:** Unlike variables, Parse JSON / Compose don't force 'Apply to each' loops to run sequentially—you can keep parallelism on.

🔸 **Best Practices:** Reserves variables for values that genuinely change during the run.

## 🎥 Video Tutorial
{% include video id="5sVpg6yT-5I" provider="youtube" %}

## 🛠️ FAQ

**1. When should I use Parse JSON instead of Initialize Variable?**

Use Parse JSON (or Compose) for static values that don't change during execution. Use Initialize Variable only for values you'll modify while the flow runs.

**2. Does Parse JSON reduce my action / API count compared to Initialize Variable?**

No. Both are built-in actions and each counts as one Power Platform request. The real benefit is readability and keeping loop concurrency—not fewer API calls.

**3. Can I use complex objects with Parse JSON?**

Absolutely! Parse JSON excels at handling complex nested objects and arrays, making it perfect for structured static data.
