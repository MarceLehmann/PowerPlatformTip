---
title: "#PowerPlatformTip 15 – 'try-catch-finally'"
date: 2022-12-24
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - error-handling
  - flow-reliability
  - automation
  - logging
  - PowerPlatformTip
excerpt: "Implement the try-catch-finally pattern in Power Automate for robust error handling, improved flow reliability, and automated cleanup."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Wrap your flow in Try, Catch and Finally Scope actions and use 'Configure run after' so Catch runs on failure and Finally always runs cleanup.

Flows that fail silently are painful to troubleshoot.
Borrow the **try-catch-finally** pattern from programming: run your main logic in a Try scope, handle failures in a Catch scope, and always run cleanup in a Finally scope — driven by each scope's **Configure run after** settings.

## 💡 Challenge
Without explicit error handling, flows fail silently and give you little to work with when something breaks.

## ✅ Solution
Structure your flow into three **Scope** actions — Try, Catch and Finally — and use **Configure run after** so the Catch runs only on failure and the Finally always runs.

## 🔧 How it's done

**1. Add a Try scope**

🔸 Put your core logic inside a **Scope** named *Try* — include every critical action.

**2. Add a Catch scope**

🔸 Add a second scope set to **run after** the Try *has failed / timed out*. Put your error handling here — notifications and logging.

**3. Add a Finally scope**

🔸 Add a third scope configured to run after both Try and Catch, whatever their result, for cleanup like deleting temporary data.

**Extra tip:** build a direct link to the current run with this expression:

```
concat('https://unitedkingdom.flow.microsoft.com/manage/environments/', workflow()?['tags']['environmentName'], '/flows/', workflow()?['name'], '/runs/', workflow()?['run']['name'])
```

🔸 Adjust the regional host (e.g. `emea`, `unitedstates`) to match your tenant's Power Automate URL.

## 🎉 Result
Failures surface clearly, cleanup always runs, and your flows behave predictably when things go wrong.

## 🌟 Key Advantages

🔸 **Surface failures:** no more silent errors — you know what went wrong and where.

🔸 **Isolated cleanup:** a dedicated Finally scope keeps post-processing tidy.

🔸 **Reliability:** structured handling makes flows more robust and dependable.

---

## 🛠️ FAQ

**Q1: When should I use try-catch-finally in Power Automate?**

Use it for critical flows where error handling matters — external API calls, file operations, and complex business processes.

**Q2: Can I nest Try-Catch scopes?**

Yes, you can nest scopes, but keep the error handling simple and clear so the flow stays readable.

**Q3: What error information is available in the Catch scope?**

Use the `result()` expression on the Try scope to read each action's status, error code and message (there's no stack trace in Power Automate). Feed those values into your logging or notification actions.
