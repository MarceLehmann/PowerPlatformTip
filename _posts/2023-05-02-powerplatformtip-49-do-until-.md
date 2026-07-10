---
title: "#PowerPlatformTip 49: 'Do-Until'"
date: 2023-05-02
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - Marcel Lehmann
  - Power Automate
  - Do Until
  - Loop
  - Automation
  - Workflow
  - Retry Logic
  - Dynamic Processes
  - Flow Control
  - PowerPlatformTip
excerpt: "Automate repetitive tasks in Power Automate with the Do Until loop. Learn how to build robust flows that wait for conditions, retry actions, and handle dynamic processes efficiently."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Put the failure-prone action directly in a Do Until loop's condition to retry until it succeeds, no extra boolean variable needed.

## 💡 Challenge
In Power Automate, using a boolean variable to control a "Do Until" loop adds extra overhead and complexity when handling transient failures like locked or unavailable files.

## ✅ Solution
Directly evaluate the action that might fail in the loop's condition, eliminating the need for an additional true/false variable.

## 🔧 How It's Done
Here's how to do it:

1. Add a "Do Until" control to your flow.
   🔸 In the loop's condition, insert the action you expect may fail (e.g., "Get file content") directly.
   🔸 Use the action's success status or output expression as the loop condition.

2. Configure loop settings.
   🔸 Set the maximum number of iterations or timeout under "Timeout" and "Count."
   🔸 Optionally add a delay between retries to allow external resources to become available.

3. Handle errors after the loop.
   🔸 After the loop completes, add your next action or error-handling steps.
   🔸 Apply additional controls or notifications if all retries fail.

## 🎉 Result
Your flow retries the action until it succeeds without managing extra variables, simplifying logic and reliably handling locked or unavailable resources.

## 🌟 Key Advantages
🔸 Simplifies loop conditions by removing extra variables.

🔸 Improves flow readability and maintenance.

🔸 Handles transient failures automatically with built-in retry logic.

---

## 🛠️ FAQ
**Q: What happens if the Do Until loop reaches its maximum iteration count before the action succeeds?**

The loop will exit and continue with the next action in your flow. You should add error handling after the loop to check if the action ultimately succeeded and take appropriate action if it didn't.

**Q: How do I set appropriate timeout and retry count values for file operations?**

For file operations, start with a 2-3 minute timeout and 5-10 retry attempts. Add a 10-30 second delay between retries to allow locked files to become available. Adjust based on your specific use case and file system behavior.

**Q: Can I use this approach with any type of action that might fail?**

Yes, this works with any action that can have transient failures - file operations, API calls, database connections, etc. The key is that the failure should be temporary and likely to succeed on retry, not a permanent configuration issue.

---
