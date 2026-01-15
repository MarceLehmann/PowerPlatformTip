# SEO Content Audit Checklist for PowerPlatformTip

## 📋 Overview

This checklist helps you audit and optimize blog posts for better Google indexing and SEO performance.

## 🎯 Goals
- Reduce "Gefunden - zurzeit nicht indexiert" (Found but not indexed) pages
- Improve CTR from 1.6% to 3%+
- Get 70%+ of pages indexed
- Improve average position from 8.4 to under 6

---

## ✅ Pre-Publish Checklist for New Posts

Use this checklist for every new blog post:

### 1. **Title Optimization** ✍️
- [ ] Title is 50-60 characters (displays fully in search results)
- [ ] Primary keyword appears at the beginning
- [ ] Title is compelling and includes power words
- [ ] Title matches H1 on page
- [ ] Avoid clickbait - be accurate and descriptive

**Good Example**: "Power Apps ComboBox DefaultSelectedItems: Complete Guide"  
**Bad Example**: "How to use DefaultSelectedItems" (too short, no keyword)

### 2. **Meta Description** 📝
- [ ] Description is 150-160 characters
- [ ] Includes primary keyword naturally
- [ ] Has a clear call-to-action or benefit
- [ ] Accurately describes the content
- [ ] Compelling enough to improve CTR

**Format**: `excerpt: "Your 150-160 character description here"`

**Good Example**: "Learn how to set DefaultSelectedItems in Power Apps ComboBox using tables, lookups, and manual records. Complete guide with examples."

### 3. **Content Quality** 📚
- [ ] Minimum 500 words (ideal: 1000-2000 words)
- [ ] Content provides unique value (not rehashing basics)
- [ ] Includes practical examples or code samples
- [ ] Has clear structure with headings (H2, H3)
- [ ] Answers a specific question or solves a problem
- [ ] Includes original screenshots or diagrams
- [ ] No duplicate content from other sources

### 4. **Front Matter SEO** 🏷️
```yaml
---
title: "Your SEO-Optimized Title (50-60 chars)"
date: 2024-01-15
permalink: /article/powerplatform/2024/01/15/your-post-slug/
updated: 2024-01-15  # Update when content changes
categories:
  - Article
  - PowerPlatform
excerpt: "Your compelling meta description (150-160 characters)"
header:
  overlay_color: "#2dd4bf"
  overlay_filter: "0.5"
  teaser: /assets/images/your-image.jpg  # Important for social sharing
toc: true
toc_sticky: true
tags:
  - Power Apps
  - Power Automate
  - Tutorial
---
```

### 5. **Images & Media** 🖼️
- [ ] All images have descriptive file names (power-apps-combobox.jpg, not IMG_1234.jpg)
- [ ] All images have alt text describing the content
- [ ] Featured image (teaser) is 1200x630px (optimal for social)
- [ ] Images are compressed/optimized (WebP preferred)
- [ ] File size under 200KB per image
- [ ] Alt text includes relevant keywords naturally

### 6. **Internal Linking** 🔗
- [ ] Link to 2-3 related posts within content
- [ ] Use descriptive anchor text (not "click here")
- [ ] Link to relevant category/tag pages
- [ ] Include link to homepage or key landing pages
- [ ] Check all links are working

### 7. **Tags & Categories** 🏷️
- [ ] Use 3-7 relevant tags
- [ ] Use consistent tag names (check existing tags first)
- [ ] Tags match actual content topics
- [ ] Primary category is accurate
- [ ] Don't create new categories unnecessarily

### 8. **Structured Data** 🔢
- [ ] Front matter includes all required fields
- [ ] Date format is correct (YYYY-MM-DD)
- [ ] Permalink follows site structure
- [ ] Categories are properly formatted
- [ ] Author information is present (defaults to site author)

### 9. **Readability** 📖
- [ ] Paragraphs are 2-4 sentences max
- [ ] Use bullet points and lists
- [ ] Include code blocks for technical content
- [ ] Use bold/italic for emphasis (sparingly)
- [ ] Break up text with subheadings every 300-400 words
- [ ] TOC enabled for posts over 1000 words

### 10. **Technical SEO** ⚙️
- [ ] URL slug is short and descriptive
- [ ] No special characters in URL (except hyphens)
- [ ] Published date is accurate
- [ ] Last updated date is set if content is updated
- [ ] No noindex tag (unless intentional)

---

## 🔄 Existing Content Audit

For existing posts showing poor performance:

### Identify Problem Posts
Check Google Search Console for:
- [ ] Posts with high impressions but low CTR (<1%)
- [ ] Posts indexed but low position (>15)
- [ ] Posts with "Crawled - currently not indexed"

### Content Refresh Checklist
- [ ] Update the `updated:` date in front matter
- [ ] Add 200-500 words of new content
- [ ] Update outdated information or screenshots
- [ ] Improve title and meta description
- [ ] Add more internal links from other posts
- [ ] Check and fix any broken external links
- [ ] Add relevant new tags
- [ ] Improve image optimization
- [ ] Add FAQ section if applicable
- [ ] Include recent developments (2024-2026 updates)

### Thin Content - Fix or Remove
If post is under 300 words:
- [ ] **Option A**: Expand to 500+ words with more details
- [ ] **Option B**: Merge with related post
- [ ] **Option C**: Add noindex if not valuable

### Duplicate/Similar Content
- [ ] Identify posts covering same topic
- [ ] Consolidate into one comprehensive post
- [ ] Add redirects from old URLs to consolidated post
- [ ] Update all internal links

---

## 🔍 Monthly SEO Audit Tasks

Perform these checks monthly:

### 1. Google Search Console Review
- [ ] Check indexing status
- [ ] Review coverage issues
- [ ] Identify new 404 errors
- [ ] Check mobile usability issues
- [ ] Review performance trends

### 2. Content Performance
- [ ] Identify top 10 performing posts (traffic, rankings)
- [ ] Identify bottom 10 posts for improvement
- [ ] Update posts older than 1 year
- [ ] Check for seasonal content opportunities

### 3. Technical Checks
- [ ] Verify sitemap.xml is updating
- [ ] Check robots.txt is correct
- [ ] Test canonical URLs
- [ ] Verify schema.org markup
- [ ] Check page load speed (Lighthouse)

### 4. Link Building
- [ ] Review internal linking opportunities
- [ ] Check for broken internal links
- [ ] Review external backlinks
- [ ] Identify link building opportunities

---

## 🚨 Common SEO Mistakes to Avoid

❌ **Don't Do This**:
1. Duplicate title tags across posts
2. Missing or duplicate meta descriptions
3. Images without alt text
4. Thin content (under 300 words)
5. Keyword stuffing in content
6. Ignoring mobile optimization
7. Slow page load times
8. Broken internal/external links
9. No internal linking between posts
10. Forgetting to update old content

✅ **Do This Instead**:
1. Unique, descriptive titles for every post
2. Compelling, unique descriptions for each post
3. Descriptive alt text for all images
4. Comprehensive content (500+ words)
5. Natural keyword usage
6. Mobile-first approach
7. Optimize images and code
8. Regular link audits
9. Strategic internal linking
10. Regular content updates

---

## 📊 Priority Framework

### High Priority (Fix Immediately)
- Posts with 404 errors
- Duplicate titles/descriptions
- Missing meta descriptions
- Images without alt text
- Broken links

### Medium Priority (Fix This Month)
- Thin content (under 500 words)
- Poor titles (under 40 chars)
- Missing internal links
- Old content (over 2 years, no updates)
- Posts with poor CTR

### Low Priority (Schedule for Later)
- Minor wording improvements
- Additional internal links
- Enhanced images
- FAQ additions
- Related posts optimization

---

## 🎓 SEO Best Practices for Power Platform Content

### Keyword Research
- Use Google Search Console to find queries people use
- Include product names: "Power Apps", "Power Automate", "Dataverse"
- Add modifiers: "how to", "tutorial", "guide", "tip", "fix", "error"
- Include version/year: "2024", "2025", "latest"
- Use long-tail keywords: "power apps combobox default selected items"

### Content Types That Rank Well
1. **How-to Guides**: Step-by-step tutorials
2. **Error Solutions**: "How to fix [error]"
3. **Comparison Posts**: "X vs Y in Power Platform"
4. **Lists**: "10 Power Apps Tips"
5. **Complete Guides**: "Ultimate Guide to [topic]"
6. **Case Studies**: Real-world examples
7. **Updates**: "What's new in [feature]"

### Power Platform Specific Keywords
- Power Apps (Canvas, Model-driven)
- Power Automate (Cloud flows, Desktop flows)
- Power BI
- Dataverse
- Power Pages
- Copilot Studio
- PowerFx
- Connectors
- SharePoint integration
- Common Data Service (legacy term)

---

## 📈 Success Metrics

Track these monthly:

- [ ] Pages indexed (target: 70%+)
- [ ] Average CTR (target: 3%+)
- [ ] Average position (target: under 6)
- [ ] Organic traffic growth
- [ ] Pages with impressions
- [ ] 404 errors (target: under 5)
- [ ] Page load speed (target: under 3s)
- [ ] Core Web Vitals (all green)

---

## 🛠️ Tools & Resources

- **Google Search Console**: Monitor indexing and performance
- **Google Analytics**: Track traffic and user behavior
- **Lighthouse**: Performance and SEO audits
- **Screaming Frog**: Site crawling and analysis
- **Yoast SEO**: Content optimization (WordPress, but principles apply)
- **Jekyll SEO Tag**: Plugin documentation
- **Schema.org**: Structured data reference

---

## 📝 Quick Reference: Ideal Post Structure

```markdown
---
[Front matter with SEO fields]
---

# Main Title (H1) - Matches page title

Brief introduction (2-3 sentences) explaining what the post covers.

## What You'll Learn (H2)
- Bullet point 1
- Bullet point 2
- Bullet point 3

## Main Content Section 1 (H2)

Content with images, code samples, and examples.

### Subsection (H3)

More detailed content.

## Main Content Section 2 (H2)

Continue with structured content.

## Common Issues and Solutions (H2)

Address common problems readers face.

## Conclusion (H2)

Summarize key points and next steps.

## Related Posts (Auto-generated)

[Internal links to related content - already implemented]
```

---

**Last Updated**: 2026-01-15  
**Version**: 1.0  
**Maintained By**: PowerPlatformTip SEO Team
