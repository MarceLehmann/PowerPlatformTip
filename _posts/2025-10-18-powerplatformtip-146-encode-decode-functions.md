---
title: "#PowerPlatformTip 146: Encode & Decode Functions"
seo_title: "Encode & Decode in Power Apps & Power Automate"
date: 2025-12-04
last_modified_at: 2026-07-10
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - PowerApps
  - PowerFx
  - HTTPRequests
  - JSONHandling
  - ODataFilters
  - PowerPlatformTip
excerpt: "Passing URLs, JSON data, or text with special characters between systems? Encoding prevents quotes, apostrophes, and special characters from breaking your flows and apps by ensuring they're treated as data, not code."
description: "Stop special characters breaking your flows. Use EncodeUrl, EncodeHTML, encodeUriComponent & decodeUriComponent, plus OData apostrophe escaping, the right way."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
faq:
  - question: >-
      Why do my HTTP requests fail with "invalid JSON" even though the JSON looks correct?
    answer: >-
      The issue is often unescaped double quotes in dynamic values that break JSON syntax. For URL parameters, use encodeUriComponent(). For JSON request bodies, use replace() to escape quotes: `replace(variables('text'), '"', '\"')`. Remember: quotes have special meaning in both JSON and Power Automate expressions.
  - question: >-
      How do I handle text with apostrophes in Power Automate OData filter queries?
    answer: >-
      Use the replace() expression to double apostrophes: `replace(varTitle,'''','''''')`. This escapes the apostrophe so `'Tom's Diner'` becomes `'Tom''s Diner'` in the query. Two apostrophes together are interpreted as a single apostrophe in the data. NEVER use encodeUriComponent() for OData filters as it encodes the filter syntax itself and breaks the query.
  - question: >-
      What's the difference between encodeUriComponent() for URLs vs. JSON escaping for request bodies?
    answer: >-
      Use encodeUriComponent() only for URL parameters and query strings - it converts characters to %XX format. For JSON in HTTP request bodies, use replace() with backslash escaping: `replace(text, '"', '\"')`. URL encoding and JSON escaping serve different purposes and are not interchangeable.
---

> **TL;DR:** Encode special characters in Power Platform, `EncodeUrl`/`EncodeHTML` in Power Apps, `encodeUriComponent`/`decodeUriComponent` in flows, and double apostrophes for OData filters.

## 💡 Challenge

Developers face critical issues when special characters like quotes ("), apostrophes ('), or JSON brackets ({}) are interpreted as code syntax instead of data content. This causes broken HTTP requests, failed API calls, invalid JSON errors, and runtime failures in both Power Apps and Power Automate. Without proper encoding, URLs with query parameters break, filter queries fail, and data transmission produces unpredictable results.

## ✅ Solution

Use native encode/decode functions to convert special characters into safe escape sequences (%XX format). Power Apps offers EncodeUrl() and EncodeHTML() for encoding output, but lacks native decoding. Power Automate provides full bidirectional support through encodeUriComponent() and decodeUriComponent(), essential for HTTP requests and JSON payloads. Important: OData filter queries require different escaping techniques.

## 🔧 How It's Done

### Power Apps Functions

**1. EncodeUrl(), encode URLs and query parameters safely**

🔸 Expression: `EncodeUrl("https://example.com/search?q=hello world")`

🔸 Returns: `"https://example.com/search?q=hello%20world"`

🔸 Special characters: Space→%20, ?→%3F, &→%26, #→%23

🔸 Use case: `Launch(EncodeUrl("https://wa.me/?text=Check O'Neill's offer!"))`

**2. EncodeHTML(), prevent HTML injection and display issues**

🔸 Expression: `EncodeHTML("<script>alert('test')</script>")`

🔸 Returns: `"&lt;script&gt;alert('test')&lt;/script&gt;"`

🔸 Converts: < → &lt;, > → &gt;, & → &amp;, " → &quot;

🔸 Use case: Display user comments safely in HTML Text controls without XSS vulnerability

**3. PlainText(), strip HTML tags and decode entities**

🔸 Expression: `PlainText("<p>Hello &nbsp; &quot;World&quot;</p>")`

🔸 Returns: `"Hello   "World""`

🔸 Removes all HTML/XML tags and converts entities to readable text

🔸 Use case: Clean SharePoint rich text fields for plain text display or search

**4. DecodeUrl() limitation**

🔸 No native function exists in Power Apps

🔸 Solution: Call a Power Automate flow with the decodeUriComponent() expression

### Power Automate Expressions

**5. encodeUriComponent(), critical for URL parameters**

🔸 Expression: `encodeUriComponent('How are you?')`

🔸 Returns: `'How%20are%20you%3F'`

🔸 Special characters: Space→%20, ?→%3F, '→%27, "→%22, {→%7B, }→%7D

🔸 Use case 1: Encode JSON as URL parameter: `encodeUriComponent('{"name":"John"}')`

🔸 Use case 2: Prepare query string parameters for HTTP GET requests

**6. decodeUriComponent(), convert encoded data back to readable format**

🔸 Expression: `decodeUriComponent('https%3A%2F%2Fexample.com%2Fsearch%3Fq%3Dhello%20world')`

🔸 Returns: `'https://example.com/search?q=hello world'`

🔸 Decode apostrophes: `decodeUriComponent('Tom%27s%20Diner')` returns `'Tom's Diner'`

🔸 Use case: Process encoded webhook data or query string parameters from external systems

**7. JSON escaping for HTTP request body**

🔸 Problem: Double quotes in JSON break HTTP request syntax

🔸 Use case (Request Body): Use proper JSON escaping with replace()

🔸 Expression: `replace(string(variables('jsonData')), '"', '\"')`

🔸 Result: Escapes double quotes with backslash so JSON remains valid

🔸 Alternative: Use backslash escape: `replace(body('Get_item')?['Title'],'"','\"')`

**8. OData filter query with apostrophes**

🔸 Problem: Filter query fails with `Title eq 'Tom's Diner'`

🔸 Solution: Use replace() to double apostrophes: `replace(Title,'''','''''')`

🔸 How it works: Two apostrophes (`''`) represent one apostrophe in the data

🔸 Result: `'Tom's Diner'` becomes `'Tom''s Diner'` in the OData query

🔸 Important: Do NOT use encodeUriComponent() for OData filters - it breaks the query syntax

## 🎉 Result

Developers can safely transmit data containing quotes, apostrophes, JSON structures, and special characters without syntax errors or runtime failures. HTTP requests work reliably, OData queries process correctly with proper apostrophe escaping, and the distinction between code and content is preserved across Power Platform solutions.

## 🌟 Key Advantages

🔸 Prevents "invalid JSON" errors in HTTP actions through proper quote escaping

🔸 Enables safe transmission of JSON objects as URL parameters with encodeUriComponent()

🔸 Solves OData filter query failures when values contain apostrophes using replace()

🔸 Distinguishes between syntax characters and data content in Power Fx and expressions

🔸 No premium connectors required, works with standard HTTP and SharePoint actions

---

## 🛠️ FAQ

**Q1: Why do my HTTP requests fail with "invalid JSON" even though the JSON looks correct?**

The issue is often unescaped double quotes in dynamic values that break JSON syntax. For URL parameters, use encodeUriComponent(). For JSON request bodies, use replace() to escape quotes: `replace(variables('text'), '"', '\"')`. Remember: quotes have special meaning in both JSON and Power Automate expressions.

**Q2: How do I handle text with apostrophes in Power Automate OData filter queries?**

Use the replace() expression to double apostrophes: `replace(varTitle,'''','''''')`. This escapes the apostrophe so `'Tom's Diner'` becomes `'Tom''s Diner'` in the query. Two apostrophes together are interpreted as a single apostrophe in the data. NEVER use encodeUriComponent() for OData filters as it encodes the filter syntax itself and breaks the query.

**Q3: What's the difference between encodeUriComponent() for URLs vs. JSON escaping for request bodies?**

Use encodeUriComponent() only for URL parameters and query strings - it converts characters to %XX format. For JSON in HTTP request bodies, use replace() with backslash escaping: `replace(text, '"', '\"')`. URL encoding and JSON escaping serve different purposes and are not interchangeable.

## 🔗 Related Tips
- [#PowerPlatformTip 58: HTTP Actions](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-58-http-actions/), where proper encoding keeps requests valid.
- [#PowerPlatformTip 121: Filtering SharePoint File Fields with OData](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-121-filtering-sharepoint-file-fields-with-odata/), apply apostrophe escaping in real filters.
