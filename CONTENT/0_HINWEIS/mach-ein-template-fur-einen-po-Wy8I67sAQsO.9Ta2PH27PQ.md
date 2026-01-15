<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# mach ein template für einen powerplatformtip newsletter in systeme.io.

diese formatierung bitte einhalten:

```
<div style="font-family:Inter, 'Segoe UI', Roboto, Arial, sans-serif; color:#0f172a; line-height:1.45; max-width:700px; margin:0 auto; padding:20px;"> <p style="margin:0 0 18px 0;">Hey Power Platform friend!</p> <h2 style="color:#0f766e;margin-top:0;">1. 💰 TL;DR - Cut AI Costs by 80%</h2> <ul style="margin-top:8px;padding-left:20px;"> <li>AI Builder credits end November 1, 2025. New Copilot Credits cost 5-10x more.</li> <li>Process only document thumbnails (first page) instead of entire PDFs with <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</code>.</li> <li>Works with Azure AI, OpenAI Vision, Google Document AI - save 70-95% processing costs.</li> <li>Smart fallback: if thumbnail extraction fails, process full document. Zero data loss.</li> </ul> <p style="margin:10px 0 18px 0;">📖 [https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-143-reduce-ai-costs/](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-143-reduce-ai-costs/)</p> <h2 style="color:#0f766e;">2. 💸 Why This Matters Right Now</h2> <p style="margin-top:8px;">Microsoft is killing AI Builder credits on November 1, 2025. The replacement? Copilot Credits that cost significantly more.</p> <p>Here's the problem: Most business documents (invoices, contracts, receipts) have 15-30 pages. But the important data is usually on page 1. The rest? Terms and conditions, legal text, appendices - stuff that costs you money but gives you zero business value.</p> <p><strong>Real numbers:</strong> Processing a 15-page invoice with Azure AI Document Intelligence costs $0.45. Processing just the first page? $0.03. That's 93% savings right there.</p> <h2 style="color:#0f766e;">3. 🔧 Build it in 15 minutes — Recipe</h2> <ol style="padding-left:20px;"> <li><strong>Save Document to SharePoint First:</strong> Whether Power Apps upload or email attachment - save to SharePoint library first. Thumbnails only exist AFTER saving.</li> <li><strong>Get File Properties:</strong> Add "Get file properties" action right after saving. This gives you access to the thumbnail.</li> <li><strong>Extract Thumbnail:</strong> <div style="margin:8px 0;"> <pre style="background:#f6f8fa;padding:10px;border-radius:6px;display:inline-block;">@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</pre> </div> </li> <li><strong>Send to AI Provider:</strong> Works with Azure AI, OpenAI GPT-4o Vision, Google Document AI, or AI Builder. Any AI that accepts images.</li> <li><strong>Validate Results:</strong> Check if you got invoice number, amount, date, vendor name. Is confidence score above 85%? Great, you're done!</li> <li><strong>Smart Fallback:</strong> If something's missing or confidence is low, then process the full PDF. This happens only 5-15% of the time for invoices.</li> </ol> <h2 style="color:#0f766e;">4. 📊 Real Examples</h2> <ul style="margin-top:8px;padding-left:20px;"> <li><strong>Invoice Processing:</strong> 1,000 invoices × 15 pages × $30/1,000 pages = $450/month vs 1,000 invoices × 1 page = $30/month. Savings: $420/month (93% reduction)</li> <li><strong>Email Attachments:</strong> Email arrives → Save to SharePoint → Get thumbnail → Extract data → Done in 5 seconds instead of 30</li> <li><strong>Power Apps Upload:</strong> User uploads expense report → Thumbnail processing extracts amount, date, category → Automatic approval workflow starts</li> </ul> <h2 style="color:#0f766e;">5. 🛠️ Copy These Expressions</h2> <p><strong>Large thumbnail (best quality):</strong><br> <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</code></p> <p><strong>Medium thumbnail (faster):</strong><br> <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Medium']}</code></p> <p><strong>Validation check:</strong><br> <code>and(not(empty(outputs('AI_Processing')?['body/invoice_number'])), greater(outputs('AI_Processing')?['body/confidence'], 0.85))</code></p> <h2 style="color:#0f766e;">6. 🔥 Pro Tips & Pitfalls</h2> <ul style="margin-top:8px;padding-left:20px;"> <li><strong>Save to SharePoint first</strong> - thumbnails only exist after files are saved to the library</li> <li><strong>Use Large thumbnails</strong> for best accuracy (95-98%), switch to Medium if you need faster processing</li> <li><strong>Monitor fallback rates</strong> - over 15% usually means documents have small fonts or poor quality</li> <li><strong>Works with any AI provider</strong> that accepts images - perfect for avoiding vendor lock-in</li> <li><strong>Standard connectors only</strong> - suitable for enterprise environments with strict governance</li> </ul> <hr style="border:none;border-top:1px solid #eee;margin:22px 0;" /> <p style="margin-top:8px;font-style:italic;font-size:15px;color:#0f766e;"> Cheers,<br>
```

<br> Marcel Lehmann
<br>BizzApps MVP

```
<br>Im Feldacher 16, 8320 Fehraltorf, Switzerland<br>
```

```
<br>[Follow me on LinkedIn](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=marcelehmann)<br>
```

<br>You're receiving this because you might be interested in Power Platform. You can unsubscribe at any time.
</p> </div>

Here is the **Systeme.io** HTML newsletter template based on your design.

I have converted the Markdown links (e.g., `[Link](url)`) into standard HTML `<a>` tags so they function correctly in email clients. You can copy and paste this directly into a **Raw HTML** element in the Systeme.io email editor.

### 📧 Systeme.io HTML Template

```html
<div style="font-family:Inter, 'Segoe UI', Roboto, Arial, sans-serif; color:#0f172a; line-height:1.45; max-width:700px; margin:0 auto; padding:20px;">
    
    <!-- Introduction -->
    <p style="margin:0 0 18px 0;">Hey Power Platform friend!</p>
    
    <!-- Section 1 -->
    <h2 style="color:#0f766e;margin-top:0;">1. 💰 TL;DR - Cut AI Costs by 80%</h2>
    <ul style="margin-top:8px;padding-left:20px;">
        <li>AI Builder credits end November 1, 2025. New Copilot Credits cost 5-10x more.</li>
        <li>Process only document thumbnails (first page) instead of entire PDFs with <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</code>.</li>
        <li>Works with Azure AI, OpenAI Vision, Google Document AI - save 70-95% processing costs.</li>
        <li>Smart fallback: if thumbnail extraction fails, process full document. Zero data loss.</li>
    </ul>
    
    <!-- Link / Article Reference -->
    <p style="margin:10px 0 18px 0;">📖 <a href="https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-143-reduce-ai-costs/" style="color:#0f766e; text-decoration:underline;">Read the full article here</a></p>
    
    <!-- Section 2 -->
    <h2 style="color:#0f766e;">2. 💸 Why This Matters Right Now</h2>
    <p style="margin-top:8px;">Microsoft is killing AI Builder credits on November 1, 2025. The replacement? Copilot Credits that cost significantly more.</p>
    <p>Here's the problem: Most business documents (invoices, contracts, receipts) have 15-30 pages. But the important data is usually on page 1. The rest? Terms and conditions, legal text, appendices - stuff that costs you money but gives you zero business value.</p>
    <p><strong>Real numbers:</strong> Processing a 15-page invoice with Azure AI Document Intelligence costs $0.45. Processing just the first page? $0.03. That's 93% savings right there.</p>
    
    <!-- Section 3 -->
    <h2 style="color:#0f766e;">3. 🔧 Build it in 15 minutes — Recipe</h2>
    <ol style="padding-left:20px;">
        <li><strong>Save Document to SharePoint First:</strong> Whether Power Apps upload or email attachment - save to SharePoint library first. Thumbnails only exist AFTER saving.</li>
        <li><strong>Get File Properties:</strong> Add "Get file properties" action right after saving. This gives you access to the thumbnail.</li>
        <li><strong>Extract Thumbnail:</strong>
            <div style="margin:8px 0;">
                <pre style="background:#f6f8fa;padding:10px;border-radius:6px;display:inline-block;font-family:monospace;overflow-x:auto;max-width:100%;">@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</pre>
            </div>
        </li>
        <li><strong>Send to AI Provider:</strong> Works with Azure AI, OpenAI GPT-4o Vision, Google Document AI, or AI Builder. Any AI that accepts images.</li>
        <li><strong>Validate Results:</strong> Check if you got invoice number, amount, date, vendor name. Is confidence score above 85%? Great, you're done!</li>
        <li><strong>Smart Fallback:</strong> If something's missing or confidence is low, then process the full PDF. This happens only 5-15% of the time for invoices.</li>
    </ol>
    
    <!-- Section 4 -->
    <h2 style="color:#0f766e;">4. 📊 Real Examples</h2>
    <ul style="margin-top:8px;padding-left:20px;">
        <li><strong>Invoice Processing:</strong> 1,000 invoices × 15 pages × $30/1,000 pages = $450/month vs 1,000 invoices × 1 page = $30/month. Savings: $420/month (93% reduction)</li>
        <li><strong>Email Attachments:</strong> Email arrives → Save to SharePoint → Get thumbnail → Extract data → Done in 5 seconds instead of 30</li>
        <li><strong>Power Apps Upload:</strong> User uploads expense report → Thumbnail processing extracts amount, date, category → Automatic approval workflow starts</li>
    </ul>
    
    <!-- Section 5 -->
    <h2 style="color:#0f766e;">5. 🛠️ Copy These Expressions</h2>
    <p><strong>Large thumbnail (best quality):</strong><br>
    <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</code></p>
    
    <p><strong>Medium thumbnail (faster):</strong><br>
    <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Medium']}</code></p>
    
    <p><strong>Validation check:</strong><br>
    <code>and(not(empty(outputs('AI_Processing')?['body/invoice_number'])), greater(outputs('AI_Processing')?['body/confidence'], 0.85))</code></p>
    
    <!-- Section 6 -->
    <h2 style="color:#0f766e;">6. 🔥 Pro Tips & Pitfalls</h2>
    <ul style="margin-top:8px;padding-left:20px;">
        <li><strong>Save to SharePoint first</strong> - thumbnails only exist after files are saved to the library</li>
        <li><strong>Use Large thumbnails</strong> for best accuracy (95-98%), switch to Medium if you need faster processing</li>
        <li><strong>Monitor fallback rates</strong> - over 15% usually means documents have small fonts or poor quality</li>
        <li><strong>Works with any AI provider</strong> that accepts images - perfect for avoiding vendor lock-in</li>
        <li><strong>Standard connectors only</strong> - suitable for enterprise environments with strict governance</li>
    </ul>
    
    <!-- Footer -->
    <hr style="border:none;border-top:1px solid #eee;margin:22px 0;" />
    <p style="margin-top:8px;font-style:italic;font-size:15px;color:#0f766e;">
        Cheers,<br><br>
        Marcel Lehmann<br>
        BizzApps MVP<br>
        Im Feldacher 16, 8320 Fehraltorf, Switzerland<br><br>
        <a href="https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=marcelehmann" style="color:#0f766e; text-decoration:underline;">Follow me on LinkedIn</a><br><br>
        You're receiving this because you might be interested in Power Platform. <a href="{{ unsubscribe_url }}" style="color:#0f766e; text-decoration:underline;">Unsubscribe</a> at any time.
    </p>
</div>
```

<span style="display:none">[^1_1]</span>

<div align="center">⁂</div>

[^1_1]: template-powerplatformtip-orch-xRC4Id1wSKScXYVQNiwVlA.md


---

# E-Mail sieht dann aber so aus, bitte keine linkstylings

Verstanden! Hier ist das angepasste Template **ohne Link-Stylings** (keine Unterstreichungen, keine besonderen Farben - Links sehen aus wie normaler Text):

```html
<div style="font-family:Inter, 'Segoe UI', Roboto, Arial, sans-serif; color:#0f172a; line-height:1.45; max-width:700px; margin:0 auto; padding:20px;">
    
    <!-- Introduction -->
    <p style="margin:0 0 18px 0;">Hey Power Platform friend!</p>
    
    <!-- Section 1 -->
    <h2 style="color:#0f766e;margin-top:0;">1. 💰 TL;DR - Cut AI Costs by 80%</h2>
    <ul style="margin-top:8px;padding-left:20px;">
        <li>AI Builder credits end November 1, 2025. New Copilot Credits cost 5-10x more.</li>
        <li>Process only document thumbnails (first page) instead of entire PDFs with <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</code>.</li>
        <li>Works with Azure AI, OpenAI Vision, Google Document AI - save 70-95% processing costs.</li>
        <li>Smart fallback: if thumbnail extraction fails, process full document. Zero data loss.</li>
    </ul>
    
    <!-- Link / Article Reference -->
    <p style="margin:10px 0 18px 0;">📖 <a href="https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-143-reduce-ai-costs/" style="color:inherit; text-decoration:none;">https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-143-reduce-ai-costs/</a></p>
    
    <!-- Section 2 -->
    <h2 style="color:#0f766e;">2. 💸 Why This Matters Right Now</h2>
    <p style="margin-top:8px;">Microsoft is killing AI Builder credits on November 1, 2025. The replacement? Copilot Credits that cost significantly more.</p>
    <p>Here's the problem: Most business documents (invoices, contracts, receipts) have 15-30 pages. But the important data is usually on page 1. The rest? Terms and conditions, legal text, appendices - stuff that costs you money but gives you zero business value.</p>
    <p><strong>Real numbers:</strong> Processing a 15-page invoice with Azure AI Document Intelligence costs $0.45. Processing just the first page? $0.03. That's 93% savings right there.</p>
    
    <!-- Section 3 -->
    <h2 style="color:#0f766e;">3. 🔧 Build it in 15 minutes — Recipe</h2>
    <ol style="padding-left:20px;">
        <li><strong>Save Document to SharePoint First:</strong> Whether Power Apps upload or email attachment - save to SharePoint library first. Thumbnails only exist AFTER saving.</li>
        <li><strong>Get File Properties:</strong> Add "Get file properties" action right after saving. This gives you access to the thumbnail.</li>
        <li><strong>Extract Thumbnail:</strong>
            <div style="margin:8px 0;">
                <pre style="background:#f6f8fa;padding:10px;border-radius:6px;display:inline-block;font-family:monospace;overflow-x:auto;max-width:100%;">@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</pre>
            </div>
        </li>
        <li><strong>Send to AI Provider:</strong> Works with Azure AI, OpenAI GPT-4o Vision, Google Document AI, or AI Builder. Any AI that accepts images.</li>
        <li><strong>Validate Results:</strong> Check if you got invoice number, amount, date, vendor name. Is confidence score above 85%? Great, you're done!</li>
        <li><strong>Smart Fallback:</strong> If something's missing or confidence is low, then process the full PDF. This happens only 5-15% of the time for invoices.</li>
    </ol>
    
    <!-- Section 4 -->
    <h2 style="color:#0f766e;">4. 📊 Real Examples</h2>
    <ul style="margin-top:8px;padding-left:20px;">
        <li><strong>Invoice Processing:</strong> 1,000 invoices × 15 pages × $30/1,000 pages = $450/month vs 1,000 invoices × 1 page = $30/month. Savings: $420/month (93% reduction)</li>
        <li><strong>Email Attachments:</strong> Email arrives → Save to SharePoint → Get thumbnail → Extract data → Done in 5 seconds instead of 30</li>
        <li><strong>Power Apps Upload:</strong> User uploads expense report → Thumbnail processing extracts amount, date, category → Automatic approval workflow starts</li>
    </ul>
    
    <!-- Section 5 -->
    <h2 style="color:#0f766e;">5. 🛠️ Copy These Expressions</h2>
    <p><strong>Large thumbnail (best quality):</strong><br>
    <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Large']}</code></p>
    
    <p><strong>Medium thumbnail (faster):</strong><br>
    <code>@{outputs('Get_file_properties')?['body/{Thumbnail}/Medium']}</code></p>
    
    <p><strong>Validation check:</strong><br>
    <code>and(not(empty(outputs('AI_Processing')?['body/invoice_number'])), greater(outputs('AI_Processing')?['body/confidence'], 0.85))</code></p>
    
    <!-- Section 6 -->
    <h2 style="color:#0f766e;">6. 🔥 Pro Tips & Pitfalls</h2>
    <ul style="margin-top:8px;padding-left:20px;">
        <li><strong>Save to SharePoint first</strong> - thumbnails only exist after files are saved to the library</li>
        <li><strong>Use Large thumbnails</strong> for best accuracy (95-98%), switch to Medium if you need faster processing</li>
        <li><strong>Monitor fallback rates</strong> - over 15% usually means documents have small fonts or poor quality</li>
        <li><strong>Works with any AI provider</strong> that accepts images - perfect for avoiding vendor lock-in</li>
        <li><strong>Standard connectors only</strong> - suitable for enterprise environments with strict governance</li>
    </ul>
    
    <!-- Footer -->
    <hr style="border:none;border-top:1px solid #eee;margin:22px 0;" />
    <p style="margin-top:8px;font-style:italic;font-size:15px;color:#0f766e;">
        Cheers,<br><br>
        Marcel Lehmann<br>
        BizzApps MVP<br>
        Im Feldacher 16, 8320 Fehraltorf, Switzerland<br><br>
        <a href="https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=marcelehmann" style="color:inherit; text-decoration:none;">Follow me on LinkedIn</a><br><br>
        You're receiving this because you might be interested in Power Platform. <a href="{{ unsubscribe_url }}" style="color:inherit; text-decoration:none;">Unsubscribe</a> at any time.
    </p>
</div>
```

**Änderungen:**

- Alle Links haben jetzt `color:inherit; text-decoration:none;`
- Links sehen aus wie normaler Text (keine Unterstreichung, keine spezielle Farbe)
- Der Link bleibt klickbar, ist aber optisch nicht mehr hervorgehoben
<span style="display:none">[^2_1]</span>

<div align="center">⁂</div>

[^2_1]: 16723.jpg

