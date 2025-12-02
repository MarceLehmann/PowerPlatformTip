#!/bin/bash

# Build Script for PowerPlatformTip
# Optimizes CSS and JS files for production

echo "🚀 Starting build process..."

# Check if required tools are installed
command -v npm >/dev/null 2>&1 || { echo "❌ npm is required but not installed. Aborting." >&2; exit 1; }

# Install dependencies if not already installed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install --save-dev clean-css-cli uglify-js
fi

# Create build directory
mkdir -p _site/assets/css
mkdir -p _site/assets/js

echo "🎨 Minifying CSS files..."

# Minify custom CSS
if [ -f "assets/css/custom-components.css" ]; then
    npx cleancss -o _site/assets/css/custom-components.min.css assets/css/custom-components.css
    echo "✅ custom-components.css minified"
fi

if [ -f "assets/css/performance.css" ]; then
    npx cleancss -o _site/assets/css/performance.min.css assets/css/performance.css
    echo "✅ performance.css minified"
fi

echo "⚙️ Minifying JS files..."

# Minify custom JS
if [ -f "assets/js/performance.js" ]; then
    npx uglifyjs assets/js/performance.js -o _site/assets/js/performance.min.js -c -m
    echo "✅ performance.js minified"
fi

echo "🎉 Build complete!"
echo ""
echo "📊 File sizes:"
echo "----------------------------------------"

# Show file sizes
if [ -f "_site/assets/css/custom-components.min.css" ]; then
    SIZE=$(wc -c < "_site/assets/css/custom-components.min.css")
    echo "custom-components.min.css: ${SIZE} bytes"
fi

if [ -f "_site/assets/css/performance.min.css" ]; then
    SIZE=$(wc -c < "_site/assets/css/performance.min.css")
    echo "performance.min.css: ${SIZE} bytes"
fi

if [ -f "_site/assets/js/performance.min.js" ]; then
    SIZE=$(wc -c < "_site/assets/js/performance.min.js")
    echo "performance.min.js: ${SIZE} bytes"
fi

echo "----------------------------------------"
echo ""
echo "💡 Tip: Update your HTML to reference .min.css and .min.js files"
echo "💡 Tip: Enable Gzip/Brotli compression on your server (.htaccess provided)"
