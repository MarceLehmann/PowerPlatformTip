# SOCIALMEDIA Content Management

This folder manages the workflow for creating PowerPlatformTip content across different channels.

## Folder Structure

```
SOCIALMEDIA/
├── 1_INPUT/          # Place combined content files here
├── BLOG/             # Processed blog posts (Markdown)
├── NEWSLETTER/       # Processed newsletter content (Markdown)
└── process-tip.sh    # Automation script
```

## Workflow

### 1. Input Format

Place your combined PowerPlatformTip file in `1_INPUT/` folder with this structure:

```markdown
---
title: "Your Tip Title"
tip_number: 123
date: 2025-12-01
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
---

<!-- BLOG START -->
# Blog Content

Your detailed blog post content here...
This section will become the blog post.

## Section 1
Content...

## Section 2
More content...

<!-- BLOG END -->

<!-- NEWSLETTER START -->
# Newsletter Version

Shorter, concise version for newsletter...
Quick tips and highlights.

## Quick Takeaways
- Point 1
- Point 2
- Point 3

<!-- NEWSLETTER END -->
```

### 2. Processing

Run the processing script:
```bash
./SOCIALMEDIA/process-tip.sh
```

Or using the GitHub Copilot command:
```
Process the PowerPlatformTip in SOCIALMEDIA/1_INPUT folder
```

### 3. Output

The script will:
- Extract BLOG content → `BLOG/YYYY-MM-DD-tip-number-slug.md`
- Extract NEWSLETTER content → `NEWSLETTER/YYYY-MM-DD-tip-number.md`
- Keep proper frontmatter for Jekyll
- Archive processed input file

## File Naming Convention

**Blog posts:**
- Format: `YYYY-MM-DD-powerplatformtip-{number}-{slug}.md`
- Example: `2025-12-01-powerplatformtip-150-power-apps-tips.md`

**Newsletters:**
- Format: `YYYY-MM-DD-tip-{number}.md`
- Example: `2025-12-01-tip-150.md`

## Markers

Use these HTML comments to separate content:
- `<!-- BLOG START -->` and `<!-- BLOG END -->` for blog content
- `<!-- NEWSLETTER START -->` and `<!-- NEWSLETTER END -->` for newsletter content

## Notes

- Ensure all required frontmatter fields are present in the input file
- The script preserves all frontmatter metadata
- Processed files are automatically moved to an `_PROCESSED` subfolder in INPUT
- Blog posts will automatically appear on the website after processing
- Newsletter content is ready for email distribution
