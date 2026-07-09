---
title: "#PowerPlatformTip 118 – 'Copy Actions in Switch/Condition'"
date: 2024-07-23
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - Switch
  - Condition
  - CopyActions
  - DynamicContent
  - Workflow
  - PowerPlatformTip
excerpt: "Copy actions or scopes into a Switch or Condition in Power Automate without the errors caused by unresolved dynamic-content references."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Copying an action inside a Switch or Condition can break its dynamic-content references — paste it outside first, drag it into the branch, then re-point the references.

## 💡 Challenge
In Power Automate, copying actions or scopes directly within a Switch or Condition often fails, because the copied element still depends on outputs that aren't reachable inside the target branch.

## ✅ Solution
Copy the action or scope to a higher level in the flow first, move it into the desired branch, and then update the dynamic-content references so they point to elements that are accessible in the new location.

## 🔧 How It's Done

**1. Identify the action or scope to copy**

🔸 Errors when copying inside a Switch/Condition usually come from dependencies on outputs that aren't available in the target branch.

**2. Copy and paste it outside the Switch/Condition**

🔸 Paste the action or scope at a higher level in the flow first — somewhere its references still resolve.

**3. Move it into the desired branch**

🔸 Drag and drop the action or scope into the exact case or branch inside the Switch or Condition where you need it.

**4. Update the dynamic content references**

🔸 Re-point every dynamic value to an output that is accessible in the new location. This is what prevents the save error.

## 🎉 Result
You can place actions or scopes inside Switches and Conditions without unresolved-dependency errors, keeping your flow structure clean and saveable.

## 🌟 Key Advantages

🔸 Avoid errors when copying elements into complex branch structures

🔸 Keep dynamic-content references correct after moving actions

🔸 Streamline the organization and structure of your flows

---

## 🎥 Video Tutorial
{% include video id="9lMRvMHqR0g" provider="youtube" %}

---

## 🛠️ FAQ

**Q1: Why does copying an action directly within a Switch or Condition cause errors?**

Copying directly often breaks internal references, because the copied action keeps dependencies on elements that aren't yet available in the new context.

**Q2: Can I copy multiple actions or scopes at once with this method?**

Yes. Group multiple actions or a scope and follow the same process: copy outside, paste at a higher level, move them together into the branch, then update references.

**Q3: What happens if I forget to update dynamic content references?**

You'll hit save or runtime errors, because the action can't resolve references to variables or outputs in the new location.

## 🔗 Related Tips
- [#PowerPlatformTip 45 – Use Scopes](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-45-use-scopes/) — group actions into scopes to move and manage them as one block.
- [#PowerPlatformTip 11 – Trigger Condition](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-11-trigger-condition/) — control when logic runs instead of nesting more conditions.
