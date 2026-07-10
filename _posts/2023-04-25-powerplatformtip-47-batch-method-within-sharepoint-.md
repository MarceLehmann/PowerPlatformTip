---
title: "#PowerPlatformTip 47: 'Batch-Method within SharePoint'"
date: 2023-04-25
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - SharePoint
  - Power Automate
  - Batch Processing
  - REST API
  - Performance
  - Automation
  - Bulk Operations
  - Workflow Optimization
  - PowerPlatformTip
excerpt: "Accelerate bulk SharePoint list operations in Power Automate using the SharePoint REST batch method. Create, update, or delete up to 1,000 items per call to maximize performance, minimize API usage, and streamline automation workflows."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Bundle up to 1,000 SharePoint list create/update/delete operations into a single HTTP $batch call for a massive performance boost.

## 💡 Challenge
Creating SharePoint list items one by one in Power Automate can be slow and consumes many API actions, especially when dealing with hundreds of items.

## ✅ Solution
Leverage the SharePoint REST batch endpoint to bundle up to 1,000 create-item requests into a single HTTP call.

## 🔧 How It's Done
Here's how to do it:

1. Add an HTTP request action in Power Automate.
   🔸 Site Address: Your SharePoint site URL.
   🔸 Method: POST
   🔸 URL: `_api/$batch`

2. Configure headers and body.
   🔸 Headers:
     - Accept: `application/json;odata=verbose`
     - Content-Type: `multipart/mixed; boundary="batch_12345"`
   🔸 Body: Construct a batch payload with multiple subrequests for creating items. Writes (create/update/delete) must be wrapped in a changeset boundary inside the batch.

3. Parse the response.
   🔸 The HTTP action returns a multipart response containing each subresponse.
   🔸 Use a “Parse JSON” action to read success or failure for each item.

4. Handle errors and logging.
   🔸 Loop through responses to identify and retry failed creations.
   🔸 Log results or send notifications as needed.

## 🎉 Result
By batching requests, you can create up to 1,000 SharePoint list items in a single operation, dramatically improving flow performance and reducing the number of API calls.

## 🌟 Key Advantages
🔸 Massive performance boost for bulk operations.

🔸 Fewer API calls, reducing risk of throttling.

🔸 Easier error handling and logging for large data sets.

---

## 🛠️ FAQ
**1. What's the maximum number of items I can batch create in SharePoint?**

SharePoint REST API supports up to 1,000 operations per batch request, making it highly efficient for bulk operations.

**2. How do I handle partial failures when some items in the batch fail?**

Parse the batch response to identify failed items by their status codes, then retry those specific items or log them for manual review.

**3. Can I use batch operations for updating and deleting items too?**

Yes, the batch method supports CREATE, UPDATE, and DELETE operations, allowing you to mix different operations in a single batch request.

---
