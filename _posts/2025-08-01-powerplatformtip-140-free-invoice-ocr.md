---
title: "#PowerPlatformTip 140: Free Invoice OCR (Process 500 PDFs/Month for €0)"
seo_title: "#PowerPlatformTip 140: Free Invoice OCR for 500 PDFs a Month"
date: 2025-08-01
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - OCR
  - AzureAI
  - AdobePDF
  - Cloudmersive
  - Invoices
  - PowerPlatformTip
excerpt: "Build a Power Automate flow that reads and summarises up to 500 PDF invoices every month - completely free with Adobe, Cloudmersive, or Azure plus Azure AI Language."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Read and summarize up to 500 PDF invoices/month for free with a free-tier OCR connector plus Azure AI Language summarization.

## 💡 Challenge
Accounts-payable still receives hundreds of PDF invoices, reminders, and receipts every month. Manual keying of amounts, due dates, and suppliers is slow, costly, and error-prone.

## ✅ Solution
Combine any **free-tier OCR connector** (Adobe PDF Services, Cloudmersive PDF/OCR, or Azure Document Intelligence Read F0) with **Azure AI Language, Abstractive Summarization F0**. One Power Automate flow extracts text from each PDF and returns a clear, three-bullet summary, at zero cost up to **500 pages per month**.

## 🔧 How It's Done

**1. Trigger**

🔸 *When a file is created* (SharePoint / OneDrive → folder **Incoming Invoices**).

**2. OCR action, pick one connector**

🔸 Adobe PDF Services (standard)

🔸 Cloudmersive PDF (premium)

🔸 Azure Read F0 (standard)

**3. Compose**

🔸 Capture the plain OCR text (`content` or `text` field).

**4. HTTP**

🔸 Call **Azure AI Language** `/language:analyze-text` with `kind=AbstractiveSummarization` and `summaryLength=short`.

**5. Post-process**

🔸 Send a Teams/Outlook summary, store it in the Dataverse table **InvoiceSummaries**, then move the PDF to an **Archive** folder.

## 🎉 Result
Every new invoice now triggers an automated pipeline, OCR → AI summary → messaging/storage. Finance receives the key facts (total, due date, supplier) within seconds and can focus on approvals instead of data entry.

## 🌟 Key Advantages

🔸 **€0 budget** for up to 500 pages per month

🔸 100% Power Platform, no external servers or scripts

🔸 Swappable OCR connectors; keep the same summarization step

🔸 Handles multilingual invoices and receipts

🔸 Seamless upgrade path when your volume grows

---

## 🛠️ FAQ
**1. Do I need a premium licence?**
Only if you choose **Cloudmersive** (premium connector). Adobe PDF Services and Azure Read F0 use standard or HTTP actions.

**2. What about multi-page PDFs with Azure Read F0?**
The free tier processes only the **first two pages**. Split longer invoices or upgrade to S0 (€0.01 / page).

**3. How do I avoid hitting Azure AI token limits?**
F0 allows 16,384 characters per request, trim or chunk OCR text for very long invoices.

## 🔗 Related Tips
- [#PowerPlatformTip 115: AI OCR Models](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-115-ai-ocr-models/), OCR options for reading documents.
- [#PowerPlatformTip 143: Reduce AI Costs with Thumbnail-First Document Processing](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-143-reduce-ai-costs/), cut AI spend on document pipelines.
