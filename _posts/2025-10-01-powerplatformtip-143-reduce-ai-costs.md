---
title: "#PowerPlatformTip 143: Reduce AI Costs with Thumbnail-First Document Processing"
seo_title: "#PowerPlatformTip 143: Reduce AI Costs with Thumbnail-First Processing"
date: 2025-10-01
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - AIBuilder
  - CopilotCredits
  - SharePoint
  - CostOptimization
  - DocumentProcessing
  - PowerPlatformTip
excerpt: "With AI Builder credits ending November 1, 2025, and Copilot Credits costing significantly more, organizations need smarter AI processing strategies. Process only the SharePoint thumbnail of documents first using Get File Properties action, extract required data, and fall back to full PDF processing only when necessary."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Cut AI document-processing costs 70-95% by extracting data from the SharePoint thumbnail first and only processing the full PDF as a fallback.

## 💡 Challenge
AI document-processing costs rose sharply with the move from AI Builder credits to Copilot Credits (effective November 1, 2025). Most business documents like invoices run 15-30 pages, but the critical information sits on the first page only. Processing entire PDFs with Azure AI Document Intelligence ($30 per 1,000 pages), OpenAI Vision API ($0.01275 per image), or AI Builder wastes 80-95% of AI capacity on terms, legal disclaimers, and appendices that hold no extractable business data.

## ✅ Solution
Implement a thumbnail-first strategy in Power Automate. Whether documents arrive via Power Apps upload or email attachment, save them to SharePoint first, use Get File Properties to access the thumbnail, send it to your AI provider for extraction, validate the results, and only process the full document if required fields are missing or confidence is too low. This platform-agnostic approach works with any AI service that accepts image input and ensures zero data loss through intelligent fallback logic.

## 🔧 How It's Done

**1. Configure document intake and save to SharePoint**

🔸 Power Apps: user uploads a document → Create file to save it in a SharePoint library.

🔸 Email: when a new email arrives (with attachments) → Apply to each attachment → Get attachment content → Create file in SharePoint.

🔸 Both paths must save the document to SharePoint first, before accessing thumbnails.

**2. Get file properties to access thumbnail metadata**

🔸 Add "Get file properties" immediately after file creation.

🔸 Reference the file ID from the previous "Create file" action.

🔸 This exposes all file metadata, including thumbnail URLs.

🔸 The thumbnail is only available after the file is saved to SharePoint, not during upload.

**3. Extract the thumbnail URL**

🔸 Use the expression `@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}`.

🔸 Available sizes: Small, Medium, Large (Large gives the best quality for AI).

🔸 No Parse JSON needed, direct access to the thumbnail URL.

**4. Convert the thumbnail and send it to your AI provider**

🔸 HTTP GET the thumbnail URL with SharePoint authentication headers.

🔸 Send the base64 image to Azure AI Document Intelligence, OpenAI Vision (GPT-4o), Google Document AI, or AI Builder.

**5. Validate completeness and confidence**

🔸 Check that all required fields are populated (invoice number, date, total, vendor).

🔸 Verify confidence scores (e.g. Azure AI > 85%).

🔸 If validation passes → stop here and save 70-95% of the cost.

**6. Add a conditional fallback**

🔸 Condition: IF required fields missing OR confidence < 85% → process the full PDF with the same provider (Get file content on the original).

🔸 ELSE proceed with the thumbnail-extracted data.

🔸 Log the success/fallback ratio for ongoing optimization.

**7. Monitor savings and success rates**

🔸 Track the thumbnail-only success rate (target 85-95% for invoices).

🔸 Compare monthly cost: thumbnail-first vs. full processing.

🔸 Typical result: $450/month → $30-90/month for 1,000 invoices (15 pages average).

## 🎉 Result
Organizations processing 1,000 invoices monthly (15 pages average with T&Cs) reduce Azure AI Document Intelligence costs from $450/month to $30-90/month. Thumbnail-first extraction achieves a 92-98% success rate for standard invoice formats, with intelligent fallback ensuring zero data loss. Flow execution time drops 60-80% thanks to smaller payloads. The platform-agnostic approach protects against vendor-specific licensing changes while staying governance-compliant (standard connectors only, suitable for Managed Environments).

## 🌟 Key Advantages

🔸 **Universal intake:** works with Power Apps uploads, email attachments, or any source, just save to SharePoint first.

🔸 **Cost optimization:** 70-95% reduction across all providers (Azure AI, OpenAI, Google Document AI, AI Builder).

🔸 **Zero data loss:** intelligent fallback processes full documents only when thumbnail extraction is insufficient.

🔸 **Simple syntax:** direct thumbnail access via `@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}`, no complex JSON parsing.

🔸 **Platform agnostic:** works with any AI service accepting image input, protecting against vendor lock-in.

🔸 **Performance:** 60-80% faster flow execution thanks to smaller payloads.

🔸 **Standard connectors only:** no premium connectors, suitable for DLP policies and Managed Environments.

---

## 🛠️ FAQ
**Q1: Why must I save to SharePoint first instead of processing uploads directly?**
SharePoint generates thumbnails automatically when files are saved to document libraries. The thumbnail isn't available during upload, only after SharePoint processes and stores the file. That's why Get File Properties must run after Create File, not during the upload trigger. Power Apps uploads and email attachments both need this two-step process: save first, then access thumbnail metadata.

**Q2: What's the difference between Small, Medium, and Large thumbnail sizes for AI processing?**
SharePoint generates three sizes automatically: Small (96x96px, basic OCR), Medium (400x400px, optimal for structured documents like invoices), Large (800x800px, best for complex documents with small fonts). Large gives the highest accuracy (95-98%) but uses slightly more bandwidth. Use `@{outputs('Get_file_properties')?['body/{Thumbnail}/Medium']}` for cost-optimized processing or Large for maximum accuracy.

**Q3: How do I handle different document sources (Power Apps, email, manual upload) in one flow?**
Create a child flow that handles the thumbnail-processing logic, then call it from multiple parent flows. Each parent handles its specific trigger (Power Apps button, email arrival, manual trigger), saves the document to SharePoint, and calls the child flow with the file ID. This modular approach keeps intake methods consistent while maintaining separation of concerns.

## 🔗 Related Tips
- [#PowerPlatformTip 140: Free Invoice OCR](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-140-free-invoice-ocr/), build the OCR pipeline this optimizes.
- [#PowerPlatformTip 115: AI OCR Models](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-115-ai-ocr-models/), choose the right OCR model for your documents.
