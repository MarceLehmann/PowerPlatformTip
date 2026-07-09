---
title: "#PowerPlatformTip 115 – 'AI OCR Models'"
date: 2024-06-22
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - AIBuilder
  - AzureDocumentIntelligence
  - OCR
  - PowerAutomate
  - DocumentProcessing
  - CostSavings
  - PowerPlatformTip
excerpt: "Compare AI Builder and Azure Document Intelligence in Power Platform for cost-effective, flexible AI OCR document processing."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

> **TL;DR:** Choose Azure Document Intelligence over AI Builder for OCR – same prebuilt models at ~1¢/page and ~40% cheaper.

## 💡 Challenge
Efficient document processing matters, and the AI OCR tool you pick in Power Platform makes a real difference in cost and flexibility.

## ✅ Solution
Power Platform gives you two main AI OCR options for document processing:

🔸 **AI Builder**

🔸 **Azure Document Intelligence**

Both support a range of prebuilt models for different document types.

## 🔧 How It's Done

**1. AI Builder**

🔸 **Setup:** in make.powerapps.com, pick a prebuilt model (invoice, receipt, business card, ID, or form processing).

🔸 **Test & deploy:** try it with sample documents, then call it from a Power Automate flow.

🔸 **Cost:** requires AI Builder credits, roughly 1.6 cents per page.

**2. Azure Document Intelligence**

🔸 **Setup:** provision the service in Azure and choose a prebuilt or custom model (invoices, receipts, business cards, and more).

🔸 **Integration:** grab the API key and endpoint for Power Automate.

🔸 **Usage:** call the API to process documents with more control and flexibility.

🔸 **Cost:** about $10 per 1,000 pages (~1 cent/page) — roughly 40% cheaper than AI Builder.

## 🎉 Result
Azure Document Intelligence delivers significant cost savings, a wide range of prebuilt models, and greater control — making it the stronger choice for most document-processing needs.

## 🌟 Key Advantages

🔸 **AI Builder:** quick, easy setup, tightly integrated with Power Automate.

🔸 **Azure Document Intelligence:** cost-effective and flexible, ideal for high-volume processing.

**Recommendation:** AI Builder is simpler to start with, but Azure Document Intelligence usually wins on cost efficiency and flexibility.

Special thanks to Damien Bird for the great overview!

---

## 🎥 Video Tutorial
{% include video id="fLHmEwcg8Jo" provider="youtube" %}

---

## 🛠️ FAQ
**1. What is the main difference between AI Builder and Azure Document Intelligence?**
AI Builder is tightly integrated into Power Platform with an easy setup, while Azure Document Intelligence offers more flexibility, a wider range of models, and lower per-page costs.

**2. How do I choose the right prebuilt model for my documents?**
Pick a model based on your document type — invoices, receipts, business cards — and test it with sample files to confirm accuracy before integrating.

**3. What are the cost implications of each service?**
AI Builder costs around 1.6 cents per page, whereas Azure Document Intelligence is about 1 cent per page ($10 per 1,000 pages), roughly 40% savings.

---