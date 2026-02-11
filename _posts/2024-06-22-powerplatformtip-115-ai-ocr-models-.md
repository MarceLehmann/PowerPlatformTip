---
title: "#PowerPlatformTip 115 – 'AI OCR Models'"
date: 2024-06-22
categories:
  - Article
  - PowerPlatformTip
tags:
  - ai
  - ai-ocr
  - ai-builder
  - azure-document-intelligence
  - power-automate
  - cost-savings
  - document-processing
  - prebuilt-models
excerpt: "Compare AI Builder and Azure Document Intelligence in Power Platform for cost-effective, flexible AI OCR document processing."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

## 📝 TL;DR
Automating document processing efficiently is crucial for handling various types of documents.

## 💡 Challenge
Automating document processing efficiently is crucial for handling various types of documents. Choosing the right AI OCR tool within Power Platform can make a significant difference.

## ✅ Solution
Power Platform offers two main AI OCR tools for document processing:

* AI Builder

* Azure Document Intelligence Service

Both tools support various prebuilt models to handle different document types.

## 🔧 How It's Done
**1. AI Builder Approach**

* **Setup**: Access make.powerapps.com, select prebuilt models like invoice processing, receipt processing, business card reader, and form processing.

* **Testing & Deployment**: Use sample documents to test and integrate into a Power Automate flow.

* **Costs**: Requires purchasing AI Builder credits, costing around 1.6 cents per page.

**2. Azure Document Intelligence Service**

* **Setup**: Configure the service in Azure, selecting from prebuilt models such as invoices, receipts, business cards, and custom documents.

* **Integration**: Obtain API keys and endpoints for Power Automate.

* **Usage**: Send requests to the API and process documents with greater control and flexibility.

* **Costs**: $10 for 1,000 pages (1 cent per page), offering about 40% cost savings compared to AI Builder.

## 🎉 Result
Azure Document Intelligence offers significant cost savings, a wide range of prebuilt models, and greater control, making it the superior choice for most document processing needs.

## 🌟 Key Advantages
* **AI Builder**: Easy, quick setup, integrated with Power Automate.

* **Azure Document Intelligence**: Cost-effective, flexible, supports various document types, ideal for high-volume processing.

Recommendation: Although AI Builder is simpler to start with, Azure Document Intelligence is typically the better option for its cost efficiency and flexibility.

Special thanks to Damien Bird for the great overview! Watch the full video below

## 🎥 Video Tutorial
{% include video id="fLHmEwcg8Jo" provider="youtube" %}

---

## 🛠️ FAQ
**1. What is the main difference between AI Builder and Azure Document Intelligence?**  
AI Builder is tightly integrated into Power Platform with an easy setup, while Azure Document Intelligence offers more flexibility, a wider range of models, and lower per-page costs.

**2. How do I choose the right prebuilt model for my documents?**  
Select a model based on your document type—such as invoices, receipts, or business cards—and test it with sample files to ensure accuracy before integration.

**3. What are the cost implications of each service?**  
AI Builder costs around 1.6 cents per page, whereas Azure Document Intelligence costs about 1 cent per page (with $10 per 1,000 pages), providing roughly 40% savings.