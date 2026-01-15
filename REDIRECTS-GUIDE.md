# 301 Redirects Guide for PowerPlatformTip

## How to Use jekyll-redirect-from Plugin

The `jekyll-redirect-from` plugin is now enabled in this Jekyll site. It allows you to easily handle 301 redirects for broken URLs.

## Setup Complete ✅
- Plugin added to `_config.yml`
- Plugin added to `Gemfile`
- Ready to use in front matter

## How to Add Redirects

### Method 1: In Post/Page Front Matter

Add old URLs to any post or page using the `redirect_from` front matter:

```yaml
---
title: "My Post Title"
date: 2023-01-01
redirect_from:
  - /old-url/
  - /another-old-url/
  - /yet-another-url/
---
```

### Method 2: Redirect TO a Different Page

Use `redirect_to` to send users from this page to another:

```yaml
---
title: "Old Page"
redirect_to: /new-page/
---
```

## Fixing the 42 × 404 Errors

### Steps to Implement

1. **Identify the broken URLs** from Google Search Console
   - Export the list of 42 URLs returning 404 errors

2. **Find the correct target page** for each broken URL
   - Determine where each URL should redirect to

3. **Add redirects** using one of these methods:

   **Option A: Add to target page front matter**
   ```yaml
   ---
   title: "Correct Page Title"
   redirect_from:
     - /broken-url-1/
     - /broken-url-2/
   ---
   ```

   **Option B: Create a redirect page** in `_pages/` directory
   ```yaml
   ---
   permalink: /broken-url/
   redirect_to: /correct-page/
   sitemap: false
   ---
   ```

## Common 404 Error Patterns to Check

Based on common Jekyll issues, check for these patterns:

### 1. Trailing Slash Issues
```
/article/post-name  → should redirect to → /article/post-name/
```

### 2. Date Format Changes
```
/2023/01/post-name/  → should redirect to → /article/category/2023/01/01/post-name/
```

### 3. Category Changes
```
/old-category/post-name/  → should redirect to → /new-category/post-name/
```

### 4. Renamed Posts
```
/old-post-title/  → should redirect to → /new-post-title/
```

### 5. Feed URLs
```
/category/feed.xml  → should redirect to → /feed.xml
```

## Example Redirect Implementations

### Example 1: Single Post with Multiple Old URLs
```yaml
---
title: "Power Apps Guide"
date: 2023-06-15
permalink: /article/powerplatform/2023/06/15/power-apps-guide/
redirect_from:
  - /powerapps-guide/
  - /2023/power-apps/
  - /articles/power-apps-guide/
---
```

### Example 2: Consolidated Content
If you merged multiple posts into one:
```yaml
---
title: "Complete Power Automate Guide"
redirect_from:
  - /power-automate-basics/
  - /power-automate-advanced/
  - /power-automate-tips/
---
```

### Example 3: Renamed Category
Create a page in `_pages/redirects/`:
```yaml
---
permalink: /old-category/post-name/
redirect_to: /new-category/post-name/
sitemap: false
---
```

## Testing Redirects

After adding redirects:

1. **Build the site locally**:
   ```bash
   bundle exec jekyll build
   ```

2. **Check the `_site` folder** for generated redirect pages

3. **Test locally**:
   ```bash
   bundle exec jekyll serve
   # Visit http://localhost:4000/old-url/ and verify redirect
   ```

4. **After deployment**, test each redirect:
   ```bash
   curl -I https://powerplatformtip.com/old-url/
   # Should return: HTTP/1.1 301 Moved Permanently
   # Location: https://powerplatformtip.com/new-url/
   ```

## Bulk Redirect Implementation

For the 42 × 404 errors, create a checklist:

- [ ] Export 404 URLs from Google Search Console
- [ ] Match each URL to correct destination
- [ ] Add `redirect_from` to target posts/pages
- [ ] Test locally
- [ ] Deploy and verify
- [ ] Monitor Search Console for improvements

## Monitoring

After implementing redirects:

1. **Google Search Console**: 
   - Check "Coverage" report
   - 404 errors should decrease over 2-4 weeks

2. **Server Logs** (if accessible):
   - Monitor 404 responses
   - Look for patterns in broken URLs

3. **Analytics**:
   - Check if redirected pages show traffic
   - Verify no redirect loops

## Additional Resources

- [jekyll-redirect-from Documentation](https://github.com/jekyll/jekyll-redirect-from)
- [Google Search Console](https://search.google.com/search-console)
- [HTTP Status Code 301](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301)

## Notes

- Redirects are implemented as HTML meta refresh with 0-second delay
- GitHub Pages supports jekyll-redirect-from natively
- Redirects are permanent (301) and preserve SEO value
- Multiple redirects can point to the same destination
- Redirects work for both posts and pages
