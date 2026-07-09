---
title: "#PowerPlatformTip 150 – 'JSON & HTML to Markdown with Office Scripts'"
date: 2026-01-22
last_modified_at: 2026-07-09
categories:
  - Article
  - PowerPlatformTip
tags:
  - PowerAutomate
  - OfficeScripts
  - JSON
  - HTML
  - Markdown
  - PowerPlatformTip
excerpt: "Turn JSON arrays and HTML into clean Markdown right inside a flow — with pure code, no AI. Two small Office Scripts do the formatting, Power Automate passes the data in and writes the Markdown to SharePoint, Teams or a file."
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
toc: true
toc_sticky: true
---

You get structured JSON from an API or SharePoint, or raw HTML from an email or web source, and you need clean Markdown for documentation, a Teams post or a wiki page.
No need for AI Builder or Copilot: two small Office Scripts convert both formats deterministically, every single time.
Power Automate stays the orchestrator; the scripts do the formatting.

## 💡 Challenge
Building Markdown inside a flow usually means nested `Apply to each` loops and fragile string concatenation — for JSON tables and even more so for HTML, where you'd otherwise reach for an AI action that is non-deterministic and can cost premium capacity.
You want reusable steps that take JSON or HTML in and return valid Markdown out, with predictable results.

## ✅ Solution
Use Office Scripts as pure formatting engines. One script turns a JSON array into a Markdown table; a second turns HTML into Markdown using deterministic string processing.
Power Automate passes the input via the **Run script** action and receives the Markdown as the dynamic content named `result` — no AI involved.

## 🔧 How it's done

1) **Create Script A – JSON to Markdown table**
   - In Excel on the web, open **Automate > New Script**, paste the code below and save it as `JsonToMarkdown`.
   🔸 The `object[]` parameter makes the JSON show up as an input in Power Automate.
   🔸 The `: string` return type surfaces the Markdown as the `result` dynamic content.

   ```typescript
   function main(workbook: ExcelScript.Workbook, jsonData: object[]): string {
     if (!jsonData || jsonData.length === 0) {
       return "_No data_";
     }

     const rows = jsonData as Record<string, string | number | boolean>[];
     const headers = Object.keys(rows[0]);

     // Header + separator row
     let markdown = `| ${headers.join(" | ")} |\n`;
     markdown += `| ${headers.map(() => "---").join(" | ")} |\n`;

     // Data rows (escape pipe characters so the table stays valid)
     for (const row of rows) {
       const cells = headers.map(h => (row[h] ?? "").toString().replace(/\|/g, "\\|"));
       markdown += `| ${cells.join(" | ")} |\n`;
     }

     return markdown;
   }
   ```

2) **Create Script B – HTML to Markdown**
   - Add a second script, paste the code below and save it as `HtmlToMarkdown`.
   🔸 This is a deterministic string converter (Office Scripts have no DOM parser). It handles headings, bold/italic, links, images, lists, code, blockquotes and paragraphs.

   ```typescript
   function main(workbook: ExcelScript.Workbook, htmlInput: string): string {
     if (!htmlInput) {
       return "";
     }

     let md = htmlInput;

     // 1. Drop script, style and comment blocks
     md = md.replace(/<script[\s\S]*?<\/script>/gi, "");
     md = md.replace(/<style[\s\S]*?<\/style>/gi, "");
     md = md.replace(/<!--[\s\S]*?-->/g, "");

     // 2. Headings h1–h6
     for (let level = 1; level <= 6; level++) {
       const re = new RegExp(`<h${level}[^>]*>([\\s\\S]*?)<\\/h${level}>`, "gi");
       md = md.replace(re, (_m, inner: string) => `\n\n${"#".repeat(level)} ${inner.trim()}\n\n`);
     }

     // 3. Bold and italic
     md = md.replace(/<(strong|b)[^>]*>([\s\S]*?)<\/\1>/gi, (_m, _t, inner: string) => `**${inner.trim()}**`);
     md = md.replace(/<(em|i)[^>]*>([\s\S]*?)<\/\1>/gi, (_m, _t, inner: string) => `*${inner.trim()}*`);

     // 4. Preformatted blocks and inline code
     md = md.replace(/<pre[^>]*>([\s\S]*?)<\/pre>/gi, (_m, inner: string) => `\n\n\`\`\`\n${inner.trim()}\n\`\`\`\n\n`);
     md = md.replace(/<code[^>]*>([\s\S]*?)<\/code>/gi, (_m, inner: string) => `\`${inner.trim()}\``);

     // 5. Images (with and without alt) and links
     md = md.replace(/<img[^>]*alt=["']([^"']*)["'][^>]*src=["']([^"']*)["'][^>]*>/gi, (_m, alt: string, src: string) => `![${alt}](${src})`);
     md = md.replace(/<img[^>]*src=["']([^"']*)["'][^>]*>/gi, (_m, src: string) => `![](${src})`);
     md = md.replace(/<a[^>]*href=["']([^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi, (_m, href: string, text: string) => `[${text.trim()}](${href})`);

     // 6. List items and list wrappers
     md = md.replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, (_m, inner: string) => `- ${inner.trim()}\n`);
     md = md.replace(/<\/?(ul|ol)[^>]*>/gi, "\n");

     // 7. Blockquotes
     md = md.replace(/<blockquote[^>]*>([\s\S]*?)<\/blockquote>/gi, (_m, inner: string) => `\n> ${inner.trim()}\n`);

     // 8. Paragraphs and line breaks
     md = md.replace(/<br\s*\/?>/gi, "\n");
     md = md.replace(/<\/p>/gi, "\n\n");
     md = md.replace(/<p[^>]*>/gi, "");

     // 9. Strip any remaining tags
     md = md.replace(/<[^>]+>/g, "");

     // 10. Decode the most common HTML entities
     const entities: Record<string, string> = {
       "&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">",
       "&quot;": "\"", "&#39;": "'", "&apos;": "'"
     };
     md = md.replace(/&nbsp;|&amp;|&lt;|&gt;|&quot;|&#39;|&apos;/g, m => entities[m]);

     // 11. Tidy up whitespace
     md = md.replace(/[ \t]+\n/g, "\n").replace(/\n{3,}/g, "\n\n").trim();

     return md;
   }
   ```

3) **Add the Run script action**
   - In your flow add **Excel Online (Business) > Run script** and pick the workbook, then choose `JsonToMarkdown` or `HtmlToMarkdown`.

4) **Pass the input**
   🔸 **JSON**: map your array to `jsonData` and click **Switch to input entire array**, otherwise Power Automate sends single elements instead of the full array.
   🔸 **HTML**: map your HTML string (e.g. an email body) to `htmlInput`.

5) **Use the Markdown output**
   - Reference the dynamic content named **`result`** in the next action.
   🔸 Write it to a `.md` file (Create file), post it to a **Teams** channel, or add it to a SharePoint page.

## 🎉 Result
JSON arrays and HTML both become clean, valid Markdown in a single reusable flow step — deterministically, with no AI action and no premium capacity.
Run it a hundred times and you get the exact same output every time.

## 🌟 Key Advantages

🔸 **No AI, fully deterministic**: pure TypeScript, identical output on every run — nothing to review or hallucinate.

🔸 **Two formats, one pattern**: JSON tables and HTML content handled by the same Run script mechanism.

🔸 **No premium**: standard Excel Online (Business) connector — no AI Builder, no Copilot licence.

🔸 **Reusable**: drop the scripts into any flow for docs, Teams posts or wiki pages.

## 🔗 Related Tips
- [#PowerPlatformTip 37 – Table to JSON](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-37-table-to-json/) — the reverse direction: turn a two-column table into a JSON record before you format it.
- [#PowerPlatformTip 124 – Recognize Plain Text File Formats](https://www.powerplatformtip.com/article/powerplatformtip/powerplatformtip-124-recognize-plain-text-file-formats/) — read `.md` and `.json` files directly with Get File Content, without Base64 decoding.

## 🛠️ FAQ

**Q1: Why does my JSON arrive as single items instead of one array in the Run script action?**

Power Automate passes arrays element by element by default. Click **Switch to input entire array** on the `jsonData` field to send the complete array as one object.

**Q2: Where is the converted Markdown in my flow?**

The return value appears as dynamic content named **`result`**. Ensure your `main` function declares a return type (`: string`); if you change the signature later, recreate the Run script action so the connector picks up the new output.

**Q3: How complete is the HTML converter?**

It's a deterministic string converter that covers common tags (headings, bold/italic, links, images, lists, code, blockquotes, paragraphs). Office Scripts have no DOM parser, so for deeply nested or malformed HTML, extend the regex rules or pre-clean the source. Note that some web APIs such as `TextEncoder` and `Crypto` are not available when Office Scripts run in Power Automate.
