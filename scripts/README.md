# SEO Optimization Scripts

This directory contains automation scripts for maintaining and optimizing the SEO health of the PowerPlatformTip Jekyll site.

## Available Scripts

### 1. seo-audit.js

Comprehensive SEO audit script that analyzes the entire site structure.

**Purpose:**
- Scans all posts and pages
- Validates internal links
- Checks sitemap integrity
- Generates detailed findings report

**Usage:**
```bash
node scripts/seo-audit.js
```

**Output:**
- `report.json` - Detailed audit results including:
  - Post and page inventory
  - Broken internal links
  - Sitemap validation
  - SEO recommendations

**When to run:**
- After adding new posts
- Before major deployments
- Monthly for regular health checks
- When troubleshooting indexing issues

### 2. add-last-modified.js

Automatically adds `last_modified_at` field to post frontmatter based on git history.

**Purpose:**
- Extracts last commit date from git history for each post
- Adds or updates `last_modified_at` field in post frontmatter
- Signals content freshness to search engines

**Usage:**
```bash
node scripts/add-last-modified.js
```

**Output:**
- Updates post files directly with modification dates
- Displays summary of updated, skipped, and errored files

**When to run:**
- After significant content updates
- When posts are edited or updated
- Before requesting re-indexing in Google Search Console
- One-time: Already run for all existing posts

### 3. generate-report.js

Generates comprehensive SEO optimization report.

**Purpose:**
- Creates detailed documentation of all SEO improvements
- Provides metrics and expected outcomes
- Documents next steps and monitoring actions

**Usage:**
```bash
node scripts/generate-report.js
```

**Output:**
- `SEO-OPTIMIZATION-REPORT.md` - Human-readable report
- `seo-optimization-report.json` - Machine-readable data

**When to run:**
- After completing SEO optimization work
- Before presenting results to stakeholders
- For documentation purposes

## Requirements

All scripts require Node.js and use only built-in modules:
- `fs` - File system operations
- `path` - Path handling
- `child_process` - Git command execution

No additional npm packages required.

## Workflow

### Regular Maintenance

1. **After Content Updates:**
   ```bash
   # Update modification dates
   node scripts/add-last-modified.js
   
   # Run audit to verify
   node scripts/seo-audit.js
   ```

2. **Monthly Health Check:**
   ```bash
   # Full SEO audit
   node scripts/seo-audit.js
   
   # Review report.json for issues
   ```

3. **Before Major Deployment:**
   ```bash
   # Complete audit
   node scripts/seo-audit.js
   
   # Fix any issues found
   # Generate final report
   node scripts/generate-report.js
   ```

## Understanding the Reports

### report.json Structure

```json
{
  "summary": {
    "totalPosts": 164,
    "publishedPosts": 146,
    "totalPages": 8,
    "brokenLinks": 0
  },
  "posts": [...],  // Detailed post information
  "pages": [...],  // Detailed page information
  "brokenLinks": [...],  // Any broken links found
  "recommendations": [...]  // Actionable recommendations
}
```

### Key Metrics to Monitor

1. **Published Posts** - Should match total posts (no unpublished posts)
2. **Broken Links** - Should be 0 for page links
3. **Posts with last_modified_at** - Should be 100%
4. **Recommendations** - Address high-priority items first

## Troubleshooting

### Script Errors

**"No frontmatter found"**
- Post is missing YAML frontmatter
- Check file starts with `---`
- Verify frontmatter format

**"Could not get git lastmod date"**
- File not in git history
- Git not available in environment
- Run `git add` and `git commit` for the file

### False Positives

**Broken image links reported**
- Images may exist but use different URL structure
- External images are skipped
- Review manually if images display correctly on site

## Best Practices

1. **Run audits regularly** - Monthly at minimum
2. **Fix high-priority issues first** - Focus on broken page links
3. **Keep last_modified_at current** - Run after content updates
4. **Monitor Google Search Console** - Compare script results with real data
5. **Document changes** - Use generate-report.js for major updates

## Integration with CI/CD

These scripts can be integrated into GitHub Actions or other CI/CD pipelines:

```yaml
# Example GitHub Actions step
- name: SEO Audit
  run: |
    node scripts/seo-audit.js
    # Optionally fail build if critical issues found
```

## Contributing

When adding new scripts:
1. Follow the existing naming convention
2. Include comprehensive JSDoc comments
3. Add usage documentation to this README
4. Test with the existing site structure
5. Handle errors gracefully

## Support

For issues or questions:
- Check the script comments for detailed documentation
- Review the generated reports for insights
- Consult Google Search Console for real-world SEO data
- Open an issue in the repository

---

**Last Updated:** January 2026
**Maintained by:** PowerPlatformTip Team
