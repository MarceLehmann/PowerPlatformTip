import os
import re
import glob
import shutil
import urllib.request
import urllib.parse
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime

# Paths
BASE_DIR = r"c:\Users\ML Office\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
OLD_DIR = os.path.join(BASE_DIR, "CONTENT", "3_OLD")
READY_DIR = os.path.join(OLD_DIR, "ready")
POSTS_DIR = os.path.join(BASE_DIR, "_posts")
OUTPUT_BASE_DIR = os.path.join(BASE_DIR, "CONTENT", "2_OUTPUT")

def get_tip_info_from_filename(filename):
    match = re.search(r'(?:Tip|PlatformTip)[\s-]*(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def build_posts_map():
    posts_map = {}
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    for f in files:
        basename = os.path.basename(f)
        parts = basename.split('-')
        if len(parts) > 3:
            date_str = "-".join(parts[0:3])
            tip_num = get_tip_info_from_filename(basename)
            if tip_num:
                slug = "-".join(parts[3:]).replace(".md", "")
                posts_map[tip_num] = {
                    "date": date_str,
                    "slug": slug,
                    "filename": basename
                }
    return posts_map

def clean_text(text):
    if not text: return ""
    return text.strip()

def normalize_string(s):
    # Replace curly quotes with straight quotes for comparison
    return s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')

# HTML to Markdown conversion helper
def convert_html_to_markdown(element):
    if element is None:
        return ""
    
    markdown_text = ""
    
    # Handle text nodes
    if isinstance(element, str):
        return element
        
    for child in element.children:
        # Recursive call for children
        if child.name:
            if child.name == 'p':
                markdown_text += convert_html_to_markdown(child) + "\n\n"
            elif child.name == 'br':
                markdown_text += "\n"
            elif child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(child.name[1])
                markdown_text += '#' * level + " " + convert_html_to_markdown(child) + "\n\n"
            elif child.name == 'ul':
                for li in child.find_all('li', recursive=False):
                    content = convert_html_to_markdown(li).strip()
                    if content: markdown_text += f"* {content}\n"
                markdown_text += "\n"
            elif child.name == 'ol':
                for i, li in enumerate(child.find_all('li', recursive=False), 1):
                    content = convert_html_to_markdown(li).strip()
                    if content: markdown_text += f"{i}. {content}\n"
                markdown_text += "\n"
            elif child.name == 'img':
                src = child.get('src', '')
                alt = child.get('alt', '')
                if src:
                    markdown_text += f"\n![{alt}]({src})\n"
            elif child.name == 'a':
                href = child.get('href', '')
                text = convert_html_to_markdown(child).strip()
                if href and text:
                    markdown_text += f"[{text}]({href})"
                elif href:
                    markdown_text += f"<{href}>"
                elif text:
                    markdown_text += text
            elif child.name in ['strong', 'b']:
                text = convert_html_to_markdown(child).strip()
                if text: markdown_text += f"**{text}**"
            elif child.name in ['em', 'i']:
                text = convert_html_to_markdown(child).strip()
                if text: markdown_text += f"*{text}*"
            elif child.name == 'iframe':
                src = child.get('src', '')
                if src:
                    # Check if it's already a clean youtube link or needs processing
                    if "youtube" in src or "youtu.be" in src:
                         # We'll let the main parser handle the special video tag if needed, 
                         # but keeping it as a link or raw iframe is also okay. 
                         # For now, let's just keep the src so we don't lose it.
                         markdown_text += f"\nVideo: {src}\n"
                    else:
                         markdown_text += f"\n[Embedded Content]({src})\n"
            elif child.name == 'div':
                 # Skip useless divs (like share daddy if missed by filter) but process content
                 classes = child.get('class') or []
                 if 'sharedaddy' in classes or 'jp-relatedposts' in classes:
                     continue
                 markdown_text += convert_html_to_markdown(child)
            elif child.name == 'figure':
                 markdown_text += convert_html_to_markdown(child) + "\n"
            else:
                # Default: process children
                markdown_text += convert_html_to_markdown(child)
        else:
            # NavigableString
            text = str(child)
            # Basic cleanup of excessive whitespace in text nodes but keep needed spaces
            markdown_text += text
            
    return markdown_text

def parse_html_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    title_tag = soup.find('h1', class_='entry-title')
    title = title_tag.get_text(strip=True) if title_tag else "Unknown Title"
    
    entry_content = soup.find('div', class_='entry-content')
    if not entry_content:
        return None

    data = {
        "title": title,
        "challenge": "",
        "solution": "",
        "how": "",
        "result": "",
        "advantages": "",
        "video": "",
        "link": ""
    }

    current_section = None
    buffer = []
    
    # Track if we found ANY structured sections
    found_structured_sections = False
    fallback_buffer = []

    # First pass: Identify video iframes globally in content to populate metadata
    video_iframe = entry_content.find('iframe')
    if video_iframe:
        data['video'] = video_iframe.get('src', '')

    for element in entry_content.children:
        if element.name is None: 
            text = str(element).strip()
            if not text: continue
        
        # Ignore share daddy - check class list safely
        if element.name == 'div':
             classes = element.get('class') or []
             if 'sharedaddy' in classes or 'jp-relatedposts' in classes:
                 continue
        
        # Determine if this element STARTS a new section
        # We look at the TEXT content to decide, but we capture the MARKDOWN content
        raw_text = element.get_text(separator=" ", strip=True) 
        norm_text = normalize_string(raw_text)
        
        is_header = False
        
        if "💡" in norm_text and ("Challenge" in norm_text or "Problem" in norm_text or "The Challenge" in norm_text):
            if current_section and buffer: data[current_section] = "\n".join(buffer)
            current_section = "challenge"
            buffer = []
            found_structured_sections = True
            is_header = True
            # Remove the header label from the content ??
            # Actually, convert_html_to_markdown will keep it. 
            # We might want to strip it if matches exactly.
            # For now, let's clean the buffer specifically if it's just the header line.
            
        elif "✅" in norm_text and ("Solution" in norm_text or "The Solution" in norm_text):
             if current_section and buffer: data[current_section] = "\n".join(buffer)
             current_section = "solution"
             buffer = []
             found_structured_sections = True
             is_header = True

        elif "🔧" in norm_text and ("How It's Done" in norm_text or "How Its Done" in norm_text):
             if current_section and buffer: data[current_section] = "\n".join(buffer)
             current_section = "how"
             buffer = []
             found_structured_sections = True
             is_header = True
        
        elif "🎉" in norm_text and ("Result" in norm_text or "The Result" in norm_text):
             if current_section and buffer: data[current_section] = "\n".join(buffer)
             current_section = "result"
             buffer = []
             found_structured_sections = True
             is_header = True

        elif "🌟" in norm_text and ("Advantages" in norm_text or "Key Advantages" in norm_text):
             if current_section and buffer: data[current_section] = "\n".join(buffer)
             current_section = "advantages"
             buffer = []
             found_structured_sections = True
             is_header = True
        
        elif "📌" in norm_text and ("Pro Tips" in norm_text):
             if current_section and buffer: data[current_section] = "\n".join(buffer)
             current_section = "advantages" 
             buffer = ["\n**Pro Tips:**"]
             found_structured_sections = True
             is_header = True
        
        # Convert this element to markdown
        md_content = convert_html_to_markdown(element)
        
        # If it was a header line, we might want to strip the actual header text "💡 Challenge:" from md_content
        # but keep the rest (if any).
        if is_header:
            # Simple regex to remove the header prefix from the markdown line
            md_content = re.sub(r'^[#\*_\s]*[🔧✅💡🎉🌟📌].*?(?:Challenge|Solution|Done|Result|Advantages|Tips)[\s:]*', '', md_content, flags=re.IGNORECASE).strip()
        
        # Universal cleanup of residual/empty markdown artifacts
        cleaned_md = md_content.strip()
        # Aggressive check for just bold/italic markers possibly with spaces
        if re.match(r'^[\s\*_]+$', cleaned_md):
             md_content = ""
        
        if not md_content.strip(): continue

        if current_section:
            # Filter out "Share" rubbish text if it somehow survived
            if "Share" in raw_text and "Twitter" in raw_text and "LinkedIn" in raw_text: continue
            buffer.append(md_content)
        else:
             # Capture content for fallback
             if "Share" in raw_text and "Twitter" in raw_text: continue
             fallback_buffer.append(md_content)

    if current_section and buffer: 
        data[current_section] = "\n".join(buffer)
    
    # If no structured sections were found, use the fallback buffer
    if not found_structured_sections and fallback_buffer:
        data['challenge'] = "\n\n".join(fallback_buffer)

    link_tag = soup.find('link', rel='canonical')
    if link_tag:
        data['link'] = link_tag['href']

    return data

def generate_newsletter_md(data):
    sections = []
    
    sections.append(f"# {data['title']}\n")
    
    if data['challenge']:
        sections.append(f"## 💡 The Challenge\n{data['challenge']}\n")
    
    if data['solution']:
        sections.append(f"## ✅ The Solution\n{data['solution']}\n")
    
    if data['how']:
        sections.append(f"## 🔧 How It's Done\n{data['how']}\n")
        
    if data['result']:
        sections.append(f"## 🎉 Result\n{data['result']}\n")
        
    if data['advantages']:
        sections.append(f"## 🌟 Key Advantages\n{data['advantages']}\n")

    sections.append("---\n")

def main():
    print("--- Starting Batch Process & Audit ---")
    posts_map = build_posts_map()
    print(f"Loaded {len(posts_map)} posts from _posts directory.")

    # Gather all HTML files from both OLD and Ready directories
    # We want to audit ALL of them.
    all_html_files = []
    
    # Check OLD_DIR
    old_files = glob.glob(os.path.join(OLD_DIR, "*.html"))
    print(f"Found {len(old_files)} files in 3_OLD")
    all_html_files.extend(old_files)
    
    # Check READY_DIR
    ready_files = glob.glob(os.path.join(READY_DIR, "*.html"))
    print(f"Found {len(ready_files)} files in 3_OLD/ready")
    all_html_files.extend(ready_files)
    
    # Remove duplicates if any (though paths are different)
    all_html_files = list(set(all_html_files))
    
    print(f"Total HTML files to process: {len(all_html_files)}")
    print("-" * 30)

    # Audit Phase
    files_to_process = []
    missing_posts = []
    skipped_files = []

    for html_file in all_html_files:
        filename = os.path.basename(html_file)
        tip_num = get_tip_info_from_filename(filename)
        
        if not tip_num:
            print(f"[SKIP] No Tip Number found in filename: {filename}")
            skipped_files.append(filename)
            continue
            
        post_info = posts_map.get(tip_num)
        if not post_info:
            print(f"[MISSING POST] Tip {tip_num} found in OLD ({filename}) but NOT found in _posts!")
            missing_posts.append((tip_num, filename))
            continue
            
        # If we have both, add to processing list
        files_to_process.append((html_file, tip_num, post_info))

    print("-" * 30)
    print(f"Audit Complete.")
    print(f"Valid Pairs (HTML + Post): {len(files_to_process)}")
    print(f"Missing Posts: {len(missing_posts)}")
    print(f"Skipped Files: {len(skipped_files)}")
    print("-" * 30)

    # Processing Phase
    print("--- Beginning Processing & Asset Downloading ---")
    
    for html_file, tip_num, post_info in files_to_process:
        filename = os.path.basename(html_file)
        
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parsed_data = parse_html_content(content)
        if not parsed_data: 
            print(f"[ERROR] Failed to parse content for Tip {tip_num} ({filename})")
            continue
            
        clean_slug = re.sub(r'^powerplatformtip-\d+-?', '', post_info['slug']).strip('-')
        dir_name = f"{post_info['date']}-tip-{tip_num}-{clean_slug}"
        output_dir = os.path.join(OUTPUT_BASE_DIR, dir_name)
        
        # Create Output Dir
        os.makedirs(get_long_path(output_dir), exist_ok=True)
        
        # Create Assets Dir
        assets_dir = os.path.join(output_dir, "assets")
        os.makedirs(get_long_path(assets_dir), exist_ok=True)

        # Process Assets (Download & Update Links) in parsed_data
        for key in ['challenge', 'solution', 'how', 'result', 'advantages']:
            parsed_data[key] = process_content_assets(parsed_data[key], assets_dir)
        
        # --- Domain Replacement for Final Output ---
        # Now that assets are safe (downloaded), point all remaining lehmann.ws links to powerplatformtip.com
        for key, value in parsed_data.items():
            if isinstance(value, str) and 'lehmann.ws' in value:
                 parsed_data[key] = value.replace('lehmann.ws', 'powerplatformtip.com')
        
        # --- Generate Blog Post (The Post) ---
        post_path = os.path.join(POSTS_DIR, post_info["filename"])
        frontmatter = ""
        if os.path.exists(post_path):
            with open(post_path, 'r', encoding='utf-8') as pf:
                post_content = pf.read()
                if post_content.startswith('---'):
                    parts = post_content.split('---', 2)
                    if len(parts) >= 2:
                        frontmatter = f"---{parts[1]}---\n\n"
        
        # Construct full article content from parsed data (OLD source)
        full_article = frontmatter
        
        if parsed_data['challenge']:
            full_article += f"## 💡 Challenge\n{parsed_data['challenge']}\n\n"
            
        if parsed_data['solution']:
            full_article += f"## ✅ Solution\n{parsed_data['solution']}\n\n"
            
        if parsed_data['how']:
            full_article += f"## 🔧 How It's Done\n\n{parsed_data['how']}\n\n"
            
        if parsed_data['result']:
            full_article += f"## 🎉 Result\n{parsed_data['result']}\n\n"
            
        if parsed_data['advantages']:
            full_article += f"## 🌟 Key Advantages\n{parsed_data['advantages']}\n\n"
        
        if parsed_data['video']:
             vid_url = parsed_data['video']
             if "embed/" in vid_url:
                 vid_id = vid_url.split("embed/")[1].split("?")[0]
                 full_article += f"## 🎥 Video Tutorial\n{{% include video id=\"{vid_id}\" provider=\"youtube\" %}}\n\n"
             else:
                 full_article += f"## 🎥 Video Tutorial\n[Watch Video]({vid_url})\n\n"
        
        # Save the full post in the output directory
        # Use long path for writing
        with open(get_long_path(os.path.join(output_dir, post_info["filename"])), 'w', encoding='utf-8') as f:
            f.write(full_article)

        # -------------------------------------
        
        with open(get_long_path(os.path.join(output_dir, 'newsletter-systeme.md')), 'w', encoding='utf-8') as f:
            f.write(generate_newsletter_md(parsed_data))
            
        with open(get_long_path(os.path.join(output_dir, 'linkedin.md')), 'w', encoding='utf-8') as f:
            f.write(generate_social_md(parsed_data, 'linkedin'))

        with open(get_long_path(os.path.join(output_dir, 'twitter.md')), 'w', encoding='utf-8') as f:
            f.write(generate_social_md(parsed_data, 'twitter'))
            
        print(f"Re-Processed Tip {tip_num} -> {dir_name} (Included Post & Assets)")
        
        # Ensure it is in ready dir (if picked from OLD_DIR)
        if os.path.dirname(html_file) == OLD_DIR:
             shutil.move(html_file, os.path.join(READY_DIR, filename))

if __name__ == "__main__":
    main()
