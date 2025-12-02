/* ============================================
   BUILD SCRIPT FOR CSS OPTIMIZATION
   ============================================
   
   This script:
   1. Combines modular CSS files
   2. Minifies the output
   3. Generates source maps
   4. Optimizes for production
   
   Usage:
   npm run build:css
   ============================================ */

const fs = require('fs');
const path = require('path');
const CleanCSS = require('clean-css');

// Configuration
const config = {
  sourceDir: 'assets/css',
  outputDir: 'assets/css/dist',
  mainFile: 'main-components.css',
  outputFile: 'main-components.min.css',
  sourceMap: true,
  minify: true
};

// Files to process (in order)
const cssFiles = [
  '_variables.css',
  'components/author-bio.css',
  'components/mvp-badge.css',
  'components/newsletter-popup.css',
  'components/newsletter-bar.css',
  'components/after-content-cta.css',
  'components/cookie-consent.css',
  'components/footer-services.css',
  'components/mobile-navigation.css',
  'components/breadcrumbs.css',
  'components/related-posts.css',
  'components/code-blocks.css',
  'components/dark-mode-toggle.css',
  'utilities/animations.css',
  'utilities/helpers.css',
  'utilities/accessibility.css'
];

/**
 * Extract CSS from large combined file
 */
function extractComponentCSS() {
  console.log('📦 Extracting CSS components from custom-components.css...');
  
  const sourceFile = path.join(config.sourceDir, 'custom-components.css');
  
  if (!fs.existsSync(sourceFile)) {
    console.error('❌ custom-components.css not found!');
    return;
  }
  
  const content = fs.readFileSync(sourceFile, 'utf8');
  
  // Split by major comment headers
  const sections = content.split(/\/\*\s*={40,}\s*/);
  
  const componentMap = {
    'AUTHOR BIO': 'components/author-bio.css',
    'MVP BADGE': 'components/mvp-badge.css',
    'NEWSLETTER POPUP': 'components/newsletter-popup.css',
    'NEWSLETTER BAR': 'components/newsletter-bar.css',
    'AFTER-CONTENT CTA': 'components/after-content-cta.css',
    'COOKIE CONSENT': 'components/cookie-consent.css',
    'FOOTER SERVICES': 'components/footer-services.css',
    'RELATED POSTS': 'components/related-posts.css',
    'CODE BLOCKS': 'components/code-blocks.css'
  };
  
  sections.forEach(section => {
    const lines = section.split('\n');
    const header = lines[0]?.trim();
    
    Object.entries(componentMap).forEach(([keyword, filename]) => {
      if (header.includes(keyword)) {
        const componentDir = path.join(config.sourceDir, path.dirname(filename));
        if (!fs.existsSync(componentDir)) {
          fs.mkdirSync(componentDir, { recursive: true });
        }
        
        const outputPath = path.join(config.sourceDir, filename);
        const componentContent = '/*' + section;
        
        fs.writeFileSync(outputPath, componentContent, 'utf8');
        console.log(`  ✅ Created ${filename}`);
      }
    });
  });
  
  console.log('✨ Component extraction complete!\n');
}

/**
 * Combine CSS files
 */
function combineCSS() {
  console.log('🔨 Combining CSS files...');
  
  let combined = '';
  let filesProcessed = 0;
  
  cssFiles.forEach(file => {
    const filePath = path.join(config.sourceDir, file);
    
    if (fs.existsSync(filePath)) {
      const content = fs.readFileSync(filePath, 'utf8');
      combined += `\n/* ${file} */\n${content}\n`;
      filesProcessed++;
      console.log(`  ✅ Added ${file}`);
    } else {
      console.log(`  ⚠️  Skipped ${file} (not found)`);
    }
  });
  
  console.log(`\n📊 Combined ${filesProcessed}/${cssFiles.length} files\n`);
  
  return combined;
}

/**
 * Minify CSS
 */
function minifyCSS(css) {
  console.log('⚡ Minifying CSS...');
  
  const options = {
    level: 2,
    sourceMap: config.sourceMap,
    sourceMapInlineSources: true,
    compatibility: 'ie11',
    format: {
      breaks: {
        afterAtRule: false,
        afterBlockBegins: false,
        afterBlockEnds: false,
        afterComment: false,
        afterProperty: false,
        afterRuleBegins: false,
        afterRuleEnds: false,
        beforeBlockEnds: false,
        betweenSelectors: false
      },
      spaces: {
        aroundSelectorRelation: false,
        beforeBlockBegins: false,
        beforeValue: false
      },
      semicolonAfterLastProperty: false
    }
  };
  
  const result = new CleanCSS(options).minify(css);
  
  if (result.errors.length > 0) {
    console.error('❌ Minification errors:', result.errors);
    return null;
  }
  
  if (result.warnings.length > 0) {
    console.warn('⚠️  Minification warnings:', result.warnings);
  }
  
  // Stats
  const originalSize = Buffer.byteLength(css, 'utf8');
  const minifiedSize = Buffer.byteLength(result.styles, 'utf8');
  const savings = ((1 - minifiedSize / originalSize) * 100).toFixed(2);
  
  console.log(`  📉 Original: ${(originalSize / 1024).toFixed(2)} KB`);
  console.log(`  📦 Minified: ${(minifiedSize / 1024).toFixed(2)} KB`);
  console.log(`  💰 Savings: ${savings}%\n`);
  
  return {
    css: result.styles,
    sourceMap: result.sourceMap?.toString()
  };
}

/**
 * Write output files
 */
function writeOutput(result) {
  console.log('💾 Writing output files...');
  
  // Create output directory
  if (!fs.existsSync(config.outputDir)) {
    fs.mkdirSync(config.outputDir, { recursive: true });
  }
  
  // Write minified CSS
  const cssPath = path.join(config.outputDir, config.outputFile);
  fs.writeFileSync(cssPath, result.css, 'utf8');
  console.log(`  ✅ ${config.outputFile}`);
  
  // Write source map
  if (result.sourceMap) {
    const mapPath = cssPath + '.map';
    fs.writeFileSync(mapPath, result.sourceMap, 'utf8');
    console.log(`  ✅ ${config.outputFile}.map`);
  }
  
  console.log('\n✨ Build complete!\n');
}

/**
 * Main build process
 */
function build() {
  console.log('\n🚀 Starting CSS build process...\n');
  
  try {
    // Step 1: Extract components (only if needed)
    // extractComponentCSS();
    
    // Step 2: Combine CSS files
    const combined = combineCSS();
    
    // Step 3: Minify (if enabled)
    if (config.minify) {
      const result = minifyCSS(combined);
      if (result) {
        writeOutput(result);
      }
    } else {
      writeOutput({ css: combined });
    }
    
    console.log('🎉 Success! CSS build completed.\n');
  } catch (error) {
    console.error('❌ Build failed:', error);
    process.exit(1);
  }
}

// Run build
build();
