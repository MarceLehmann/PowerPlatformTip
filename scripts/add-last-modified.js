#!/usr/bin/env node

/**
 * Add last_modified_at to all posts from git history
 * This script updates the frontmatter of all posts to include last_modified_at
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const REPO_ROOT = path.join(__dirname, '..');
const POSTS_DIR = path.join(REPO_ROOT, '_posts');

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
    console.error(`Error getting git lastmod for ${filePath}:`, error.message);
    return null;
  }
}

/**
 * Parse frontmatter from markdown file
 */
function parseFrontmatter(content) {
  // Remove BOM if present
  content = content.replace(/^\uFEFF/, '');
  
  // Match frontmatter with flexible spacing
  const frontmatterRegex = /^---\r?\n([\s\S]*?)\r?\n---/;
  const match = content.match(frontmatterRegex);
  
  if (!match) return null;
  
  return {
    raw: match[0],
    content: content.substring(match[0].length),
    fullContent: content
  };
}

/**
 * Check if frontmatter has last_modified_at
 */
function hasLastModifiedAt(frontmatter) {
  return /^last_modified_at:/m.test(frontmatter);
}

/**
 * Add last_modified_at to frontmatter
 */
function addLastModifiedAt(frontmatterRaw, lastModDate) {
  // Remove trailing --- and add last_modified_at before it
  const lines = frontmatterRaw.split('\n');
  const lastLineIndex = lines.findIndex((line, idx) => idx > 0 && line.trim() === '---');
  
  if (lastLineIndex === -1) {
    // Malformed frontmatter, skip
    return frontmatterRaw;
  }
  
  // Add last_modified_at before the closing ---
  lines.splice(lastLineIndex, 0, `last_modified_at: ${lastModDate}`);
  
  return lines.join('\n');
}

/**
 * Process all posts
 */
function processAllPosts() {
  console.log('Processing posts to add last_modified_at...\n');
  
  const files = fs.readdirSync(POSTS_DIR).filter(f => 
    f.endsWith('.md') || f.endsWith('.markdown')
  );
  
  let updated = 0;
  let skipped = 0;
  let errors = 0;
  
  files.forEach(filename => {
    const filePath = path.join(POSTS_DIR, filename);
    
    try {
      const content = fs.readFileSync(filePath, 'utf8');
      const parsed = parseFrontmatter(content);
      
      if (!parsed) {
        console.log(`⚠ ${filename}: No frontmatter found, skipping`);
        skipped++;
        return;
      }
      
      // Check if already has last_modified_at
      if (hasLastModifiedAt(parsed.raw)) {
        skipped++;
        return;
      }
      
      // Get git last modified date
      const lastModDate = getGitLastModified(filePath);
      
      if (!lastModDate) {
        console.log(`⚠ ${filename}: Could not get git lastmod date, skipping`);
        skipped++;
        return;
      }
      
      // Add last_modified_at to frontmatter
      const updatedFrontmatter = addLastModifiedAt(parsed.raw, lastModDate);
      const newContent = updatedFrontmatter + parsed.content;
      
      // Write back to file
      fs.writeFileSync(filePath, newContent, 'utf8');
      console.log(`✓ ${filename}: Added last_modified_at: ${lastModDate}`);
      updated++;
      
    } catch (error) {
      console.error(`✗ ${filename}: Error - ${error.message}`);
      errors++;
    }
  });
  
  console.log(`\n=== Summary ===`);
  console.log(`Total files: ${files.length}`);
  console.log(`Updated: ${updated}`);
  console.log(`Skipped: ${skipped}`);
  console.log(`Errors: ${errors}`);
}

if (require.main === module) {
  processAllPosts();
}

module.exports = { processAllPosts };
