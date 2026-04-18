---
title: "#PowerPlatformTip NNN – 'Limit Apply to Each with take()'"
date: 2026-01-08
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - PowerPlatformTip
  - Expression
  - ApplyToEach
  - Testing
excerpt: "Stop burning hundreds of flow runs while testing loops. The take() expression lets you limit your Apply to Each loop to exactly the first X items from any array — no code changes needed, just swap the input expression and swap it back when done."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

When building flows with large SharePoint lists or Dataverse tables, testing an "Apply to each" loop on the full dataset wastes run quota and time.
The `take()` expression is a one-line fix that limits the loop to exactly the records you need for a confident test.
Remove it when you're done — no restructuring required.

## 💡 Challenge

Your "Apply to each" loop is connected to a Select action that returns hundreds or thousands of items.
Every test run processes every single item, burns flow run quota, and takes minutes to complete.
You need a way to test just the first 5 items without rebuilding the entire flow structure.

## ✅ Solution

Replace the array input of your "Apply to each" action with a `take()` expression.
`take(array, count)` returns only the first X elements of any array and discards the rest.
This keeps the full flow structure intact — you simply swap the expression in and out.

## 🔧 How It's Done

1. Open your "Apply to each" action and clear the current input field.
🔸 Make sure you are in the Expression tab, not the Dynamic content tab.

2. Enter the `take()` expression pointing to your previous action's output:
take(outputs('Select'), 5)

🔸 If your flow uses a German interface and the action is named "Auswählen", use:
`take(outputs('Auswählen'), 5)`

🔸 If you used a different action name, replace `'Select'` with your exact action name as it appears in the flow.

3. Save and run your test — the loop executes exactly 5 times regardless of array size.
   
🔸 Confirm your "Create item" logic and matching conditions behave correctly on the 5 test records.

4. Once satisfied, remove the `take()` wrapper and restore the original dynamic content or expression.
   
🔸 Simply re-open the input field and select the original output from your Select/Filter action.

## 🎉 Result

Your test runs complete in seconds instead of minutes, use only 5 flow run iterations instead of hundreds, and your logic is fully validated before you unleash it on the full dataset.
No parallel branches, no condition hacks, no duplicate flows needed.

## 🌟 Key Advantages

🔸 Zero structural changes to your flow — one expression swap in, one swap out

🔸 Works with any array source: Select, Filter Array, List Rows, Get Items, and more

🔸 No premium connectors or custom code required — pure built-in expression

## 🛠️ FAQ

Q1: Does take() throw an error if the array has fewer items than the number I specify?
A: No. If the array contains fewer elements than X, take() simply returns all available items without throwing an error.

Q2: Can I use take() with the output of a "Filter Array" action instead of a "Select" action?
A: Yes. Any array-type output works. Use `take(body('Filter_Array'), 5)` or the equivalent outputs() reference for your action name.

Q3: Is there a risk of accidentally leaving take() in a production flow?
A: Yes — always double-check before promoting to production. A best practice is to add a flow note or a comment action as a visible reminder that take() is active.
