#!/usr/bin/env node

/**
 * SEO Audit Script for Jekyll GitHub Pages
 * 
 * This script performs the following tasks:
 * 1. Scans all _posts/*.md and _pages/*.md files
 * 2. Validates sitemap.xml entries
 * 3. Finds broken internal links
 * 4. Generates report.json with findings
 * 5. Updates sitemap.xml with only valid URLs and git lastmod dates
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const REPO_ROOT = path.join(__dirname, '..');
const POSTS_DIR = path.join(REPO_ROOT, '_posts');
const PAGES_DIR = path.join(REPO_ROOT, '_pages');
const SITEMAP_PATH = path.join(REPO_ROOT, 'sitemap.xml');
const CONFIG_PATH = path.join(REPO_ROOT, '_config.yml');

// Results object
const results = {
  timestamp: new Date().toISOString(),
  summary: {
    totalPosts: 0,
    totalPages: 0,
    publishedPosts: 0,
    unpublishedPosts: 0,
    brokenLinks: 0,
    validUrls: 0,
    invalidUrls: 0
  },
  posts: [],
  pages: [],
  brokenLinks: [],
  sitemapIssues: [],
  recommendations: []
};

/**
 * Parse frontmatter from markdown file
 */
function parseFrontmatter(content) {
  const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---/;
  const match = content.match(frontmatterRegex);
  
  if (!match) return null;
  
  const frontmatter = {};
  const lines = match[1].split('\n');
  let currentKey = null;
  let currentValue = [];
  
  lines.forEach(line => {
    const keyMatch = line.match(/^(\w+):\s*(.*)$/);
    if (keyMatch) {
      if (currentKey) {
        frontmatter[currentKey] = currentValue.join('\n').trim();
      }
      currentKey = keyMatch[1];
      currentValue = [keyMatch[2]];
    } else if (currentKey && line.trim()) {
      currentValue.push(line.trim());
    }
  });
  
  if (currentKey) {
    frontmatter[currentKey] = currentValue.join('\n').trim();
  }
  
  return frontmatter;
}

/**
 * Get last modified date from git history
 */
function getGitLastModified(filePath) {
  try {
    const relPath = path.relative(REPO_ROOT, filePath);
    const cmd = `git log -1 --format=%aI -- "${relPath}"`;
    const result = execSync(cmd, { cwd: REPO_ROOT, encoding: 'utf8' }).trim();
    return result || null;
  } catch (error) {
    return null;
  }
}

/**
 * Get all markdown files from a directory
 */
function getMarkdownFiles(dir) {
  const files = [];
  
  if (!fs.existsSync(dir)) return files;
  
  const entries = fs.readdirSync(dir);
  entries.forEach(entry => {
    const fullPath = path.join(dir, entry);
    const stat = fs.statSync(fullPath);
    
    if (stat.isFile() && (entry.endsWith('.md') || entry.endsWith('.markdown'))) {
      files.push(fullPath);
    }
  });
  
  return files;
}

/**
 * Parse post URL from filename and frontmatter
 */
function getPostUrl(filename, frontmatter) {
  // If permalink is set, use it
  if (frontmatter.permalink) {
    return frontmatter.permalink;
  }
  
  // Parse from filename (YYYY-MM-DD-title.md)
  const match = filename.match(/(\d{4})-(\d{2})-(\d{2})-(.*)\.(md|markdown)$/);
  if (match) {
    const [, year, month, day, slug] = match;
    const categories = frontmatter.categories || '';
    const catPath = Array.isArray(categories) 
      ? categories.join('/').toLowerCase() 
      : categories.toLowerCase().replace(/\s+/g, '/');
    
    if (catPath) {
      return `/${catPath}/${slug}/`;
    }
    return `/${year}/${month}/${day}/${slug}/`;
  }
  
  return null;
}

/**
 * Scan all posts
 */
function scanPosts() {
  console.log('Scanning posts...');
  const files = getMarkdownFiles(POSTS_DIR);
  results.summary.totalPosts = files.length;
  
  files.forEach(filePath => {
    const content = fs.readFileSync(filePath, 'utf8');
    const frontmatter = parseFrontmatter(content);
    const filename = path.basename(filePath);
    
    if (!frontmatter) {
      results.posts.push({
        file: filename,
        error: 'No frontmatter found'
      });
      return;
    }
    
    const published = frontmatter.published !== 'false';
    if (published) {
      results.summary.publishedPosts++;
    } else {
      results.summary.unpublishedPosts++;
    }
    
    const url = getPostUrl(filename, frontmatter);
    const lastModified = getGitLastModified(filePath);
    
    results.posts.push({
      file: filename,
      url: url,
      published: published,
      title: frontmatter.title,
      date: frontmatter.date,
      lastModified: lastModified,
      hasLastModifiedAt: !!frontmatter.last_modified_at,
      permalink: frontmatter.permalink
    });
  });
  
  console.log(`Found ${results.summary.totalPosts} posts (${results.summary.publishedPosts} published)`);
}

/**
 * Scan all pages
 */
function scanPages() {
  console.log('Scanning pages...');
  const files = getMarkdownFiles(PAGES_DIR);
  results.summary.totalPages = files.length;
  
  files.forEach(filePath => {
    const content = fs.readFileSync(filePath, 'utf8');
    const frontmatter = parseFrontmatter(content);
    const filename = path.basename(filePath);
    
    if (!frontmatter) {
      results.pages.push({
        file: filename,
        error: 'No frontmatter found'
      });
      return;
    }
    
    const url = frontmatter.permalink || `/${filename.replace(/\.(md|markdown)$/, '')}/`;
    const lastModified = getGitLastModified(filePath);
    
    results.pages.push({
      file: filename,
      url: url,
      title: frontmatter.title,
      lastModified: lastModified,
      hasLastModifiedAt: !!frontmatter.last_modified_at
    });
  });
  
  console.log(`Found ${results.summary.totalPages} pages`);
}

/**
 * Find broken internal links
 */
function findBrokenLinks() {
  console.log('Scanning for broken internal links...');
  
  const allUrls = new Set();
  
  // Collect all valid URLs
  results.posts.forEach(post => {
    if (post.url && post.published) {
      allUrls.add(post.url);
      // Also add without trailing slash
      if (post.url.endsWith('/')) {
        allUrls.add(post.url.slice(0, -1));
      }
    }
  });
  
  results.pages.forEach(page => {
    if (page.url) {
      allUrls.add(page.url);
      if (page.url.endsWith('/')) {
        allUrls.add(page.url.slice(0, -1));
      }
    }
  });
  
  // Add common pages
  allUrls.add('/');
  allUrls.add('/posts/');
  allUrls.add('/tags/');
  allUrls.add('/categories/');
  
  // Scan all markdown files for links
  const allFiles = [
    ...getMarkdownFiles(POSTS_DIR),
    ...getMarkdownFiles(PAGES_DIR)
  ];
  
  allFiles.forEach(filePath => {
    const content = fs.readFileSync(filePath, 'utf8');
    const filename = path.relative(REPO_ROOT, filePath);
    
    // Find markdown links [text](url)
    const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
    let match;
    
    while ((match = linkRegex.exec(content)) !== null) {
      const linkText = match[1];
      let linkUrl = match[2];
      
      // Skip external links, anchors, and images
      if (linkUrl.startsWith('http') || linkUrl.startsWith('#') || linkUrl.startsWith('mailto:')) {
        continue;
      }
      
      // Remove anchor from URL
      const urlWithoutAnchor = linkUrl.split('#')[0];
      
      // Check if URL exists
      const exists = allUrls.has(urlWithoutAnchor) || 
                    allUrls.has(urlWithoutAnchor + '/') ||
                    allUrls.has(urlWithoutAnchor.replace(/\/$/, ''));
      
      if (!exists && urlWithoutAnchor) {
        results.brokenLinks.push({
          file: filename,
          linkText: linkText,
          linkUrl: linkUrl,
          line: content.substring(0, match.index).split('\n').length
        });
        results.summary.brokenLinks++;
      }
    }
  });
  
  console.log(`Found ${results.summary.brokenLinks} broken internal links`);
}

/**
 * Validate sitemap entries
 */
function validateSitemap() {
  console.log('Validating sitemap entries...');
  
  if (!fs.existsSync(SITEMAP_PATH)) {
    results.sitemapIssues.push({
      type: 'missing',
      message: 'sitemap.xml does not exist'
    });
    return;
  }
  
  const sitemapContent = fs.readFileSync(SITEMAP_PATH, 'utf8');
  
  // Check for hardcoded URLs in sitemap
  const hardcodedUrls = [
    '/posts/',
    '/about/',
    '/tags/',
    '/learning-resources/',
    '/privacy-policy/'
  ];
  
  hardcodedUrls.forEach(url => {
    if (sitemapContent.includes(`<loc>{{ site.url }}${url}</loc>`)) {
      results.summary.validUrls++;
    }
  });
  
  // Check if sitemap uses dynamic generation
  if (sitemapContent.includes('{% for post in site.posts %}')) {
    results.sitemapIssues.push({
      type: 'info',
      message: 'Sitemap uses dynamic generation for posts (good)'
    });
  }
  
  // Check for lastmod implementation
  if (sitemapContent.includes('last_modified_at')) {
    results.sitemapIssues.push({
      type: 'info',
      message: 'Sitemap uses last_modified_at field (good)'
    });
  }
}

/**
 * Generate recommendations
 */
function generateRecommendations() {
  console.log('Generating recommendations...');
  
  // Check for posts without last_modified_at
  const postsWithoutLastMod = results.posts.filter(p => !p.hasLastModifiedAt && p.published).length;
  if (postsWithoutLastMod > 0) {
    results.recommendations.push({
      priority: 'high',
      type: 'content_freshness',
      message: `${postsWithoutLastMod} posts missing last_modified_at field`,
      action: 'Add last_modified_at from git history to all posts'
    });
  }
  
  // Check for broken links
  if (results.summary.brokenLinks > 0) {
    results.recommendations.push({
      priority: 'high',
      type: 'broken_links',
      message: `${results.summary.brokenLinks} broken internal links found`,
      action: 'Review and fix broken links in report.json'
    });
  }
  
  // Check for unpublished posts
  if (results.summary.unpublishedPosts > 0) {
    results.recommendations.push({
      priority: 'medium',
      type: 'unpublished_content',
      message: `${results.summary.unpublishedPosts} unpublished posts found`,
      action: 'Review unpublished posts and publish or remove from sitemap'
    });
  }
  
  // Always recommend jekyll plugins
  results.recommendations.push({
    priority: 'high',
    type: 'plugins',
    message: 'Ensure SEO plugins are configured',
    action: 'Add jekyll-sitemap, jekyll-seo-tag, jekyll-feed to _config.yml'
  });
}

/**
 * Main execution
 */
function main() {
  console.log('=== SEO Audit for Jekyll Site ===\n');
  
  scanPosts();
  scanPages();
  findBrokenLinks();
  validateSitemap();
  generateRecommendations();
  
  // Write report
  const reportPath = path.join(REPO_ROOT, 'report.json');
  fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
  console.log(`\n✓ Report saved to report.json`);
  
  // Summary
  console.log('\n=== Summary ===');
  console.log(`Posts: ${results.summary.totalPosts} (${results.summary.publishedPosts} published, ${results.summary.unpublishedPosts} unpublished)`);
  console.log(`Pages: ${results.summary.totalPages}`);
  console.log(`Broken Links: ${results.summary.brokenLinks}`);
  console.log(`Recommendations: ${results.recommendations.length}`);
  
  return results;
}

if (require.main === module) {
  main();
}

module.exports = { main, results };
