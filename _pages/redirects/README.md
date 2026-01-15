# Example Redirect Pages

This directory contains example redirect pages showing how to use `jekyll-redirect-from` plugin.

## Usage

1. Copy one of the example files
2. Rename it to match your redirect purpose
3. Update the `permalink:` to the old/broken URL
4. Update the `redirect_to:` to the correct destination URL
5. Keep `sitemap: false` and `robots: "noindex, follow"`

## Important Notes

- Always include trailing slashes in URLs to match Jekyll's URL structure
- Test redirects locally before deploying
- Keep these example files for reference (they won't be deployed if permalink is changed)
- See REDIRECTS-GUIDE.md in the root directory for comprehensive documentation

## Examples Included

- **example-feed-redirect.md**: Redirect old feed URLs to main feed
- **example-url-change.md**: Redirect when URL structure changes
- **example-consolidated-content.md**: Redirect merged content to consolidated post
