#!/bin/bash

# PowerPlatformTip Content Processor
# Splits combined INPUT files into BLOG and NEWSLETTER content

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT_DIR="$SCRIPT_DIR/1_INPUT"
BLOG_DIR="$SCRIPT_DIR/BLOG"
NEWSLETTER_DIR="$SCRIPT_DIR/NEWSLETTER"
PROCESSED_DIR="$INPUT_DIR/_PROCESSED"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}  PowerPlatformTip Content Processor${NC}"
echo -e "${BLUE}================================================${NC}\n"

# Create processed directory if it doesn't exist
mkdir -p "$PROCESSED_DIR"

# Check if there are any files to process
shopt -s nullglob
input_files=("$INPUT_DIR"/*.md)
shopt -u nullglob

if [ ${#input_files[@]} -eq 0 ]; then
    echo -e "${YELLOW}No markdown files found in INPUT folder.${NC}"
    exit 0
fi

# Process each file
for input_file in "${input_files[@]}"; do
    filename=$(basename "$input_file")
    echo -e "${GREEN}Processing: ${filename}${NC}\n"
    
    # Extract frontmatter
    frontmatter=$(awk '/^---$/,/^---$/ {print; if (++count==2) exit}' "$input_file")
    
    # Extract metadata from frontmatter
    title=$(echo "$frontmatter" | grep "^title:" | sed 's/title: *//; s/"//g; s/'\''//g')
    tip_number=$(echo "$frontmatter" | grep "^tip_number:" | sed 's/tip_number: *//')
    date=$(echo "$frontmatter" | grep "^date:" | sed 's/date: *//')
    
    # Create slug from title
    slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g; s/--*/-/g; s/^-//; s/-$//')
    
    # Generate filenames
    blog_filename="${date}-powerplatformtip-${tip_number}-${slug}.md"
    newsletter_filename="${date}-tip-${tip_number}.md"
    
    # Extract BLOG content
    if grep -q "<!-- BLOG START -->" "$input_file" && grep -q "<!-- BLOG END -->" "$input_file"; then
        echo -e "${BLUE}  → Extracting BLOG content...${NC}"
        
        # Get frontmatter and blog content
        {
            echo "$frontmatter"
            echo ""
            awk '/<!-- BLOG START -->/,/<!-- BLOG END -->/' "$input_file" | \
                sed '/<!-- BLOG START -->/d; /<!-- BLOG END -->/d'
        } > "$BLOG_DIR/$blog_filename"
        
        echo -e "${GREEN}  ✓ Created: BLOG/$blog_filename${NC}"
    else
        echo -e "${YELLOW}  ⚠ No BLOG markers found${NC}"
    fi
    
    # Extract NEWSLETTER content
    if grep -q "<!-- NEWSLETTER START -->" "$input_file" && grep -q "<!-- NEWSLETTER END -->" "$input_file"; then
        echo -e "${BLUE}  → Extracting NEWSLETTER content...${NC}"
        
        # Get frontmatter and newsletter content
        {
            echo "$frontmatter"
            echo ""
            awk '/<!-- NEWSLETTER START -->/,/<!-- NEWSLETTER END -->/' "$input_file" | \
                sed '/<!-- NEWSLETTER START -->/d; /<!-- NEWSLETTER END -->/d'
        } > "$NEWSLETTER_DIR/$newsletter_filename"
        
        echo -e "${GREEN}  ✓ Created: NEWSLETTER/$newsletter_filename${NC}"
    else
        echo -e "${YELLOW}  ⚠ No NEWSLETTER markers found${NC}"
    fi
    
    # Move processed file
    mv "$input_file" "$PROCESSED_DIR/"
    echo -e "${GREEN}  ✓ Moved to: _PROCESSED/$filename${NC}\n"
done

echo -e "\n${GREEN}================================================${NC}"
echo -e "${GREEN}  Processing Complete!${NC}"
echo -e "${GREEN}================================================${NC}"
echo -e "\nProcessed ${#input_files[@]} file(s)"
echo -e "Check ${BLUE}BLOG/${NC} and ${BLUE}NEWSLETTER/${NC} folders for output\n"
