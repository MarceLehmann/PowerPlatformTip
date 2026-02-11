import os
import re
import glob

# Paths
BASE_DIR = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
OLD_DIR = os.path.join(BASE_DIR, "CONTENT", "3_OLD")
READY_DIR = os.path.join(OLD_DIR, "ready")
POSTS_DIR = os.path.join(BASE_DIR, "_posts")
OUTPUT_DIR = os.path.join(BASE_DIR, "NEWOPTIMIZEDPOSTS")

# Ensure output dir exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

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
            tip_num = get_tip_info_from_filename(basename)
            if tip_num:
                posts_map[tip_num] = {
                    "path": f,
                    "filename": basename
                }
    return posts_map

def get_frontmatter(md_content):
    pattern = r"^(---\s+.*?\s+---)"
    match = re.search(pattern, md_content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def get_faq(md_content):
    pattern = r"## 🛠️ FAQ\s+(.*)"
    match = re.search(pattern, md_content, re.DOTALL)
    if match:
        return match.group(0)
    return ""

def clean_html_to_md(html_text):
    if not html_text: return ""
    
    # Lists
    html_text = re.sub(r'<li>\s*(.*?)\s*</li>', r'* \1\n', html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r'</?ul>', '\n', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'</?ol>', '\n', html_text, flags=re.IGNORECASE)
    
    # Paragraphs / Breaks
    html_text = re.sub(r'<p[^>]*>', '', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'</p>', '\n\n', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'<br\s*/?>', '\n', html_text, flags=re.IGNORECASE)
    
    # Bold / Italic
    html_text = re.sub(r'<(strong|b)[^>]*>\s*(.*?)\s*</\1>', r'**\2**', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'<(em|i)[^>]*>\s*(.*?)\s*</\1>', r'*\2*', html_text, flags=re.IGNORECASE)
    
    # Links
    html_text = re.sub(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_text, flags=re.IGNORECASE)
    
    # Headers
    html_text = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'### \1\n\n', html_text, flags=re.IGNORECASE)
    
    # Clean Tags
    html_text = re.sub(r'<[^>]+>', '', html_text)
    
    # Decode Entities
    html_text = html_text.replace('&nbsp;', ' ')
    html_text = html_text.replace('&#8217;', "'").replace('&#8216;', "'")
    html_text = html_text.replace('&#8220;', '"').replace('&#8221;', '"')
    html_text = html_text.replace('&#8211;', '–').replace('&#8212;', '—')
    html_text = html_text.replace('&#039;', "'").replace('&amp;', '&').replace('&quot;', '"')
    html_text = html_text.replace('&lt;', '<').replace('&gt;', '>')
    html_text = re.sub(r'\n{3,}', '\n\n', html_text)
    
    return html_text.strip()

def clean_footer_text(text):
    """Removes specific footer text requested by the user."""
    if not text: return ""
    
    # Pattern 1: Overview link (various formats: bold, italic, linked)
    text = re.sub(r'\*{0,3}If you want to see the overview above all #PowerPlatformTip[^\n]*(?:click here|here)[^\n]*\*{0,3}', '', text, flags=re.IGNORECASE)
    # Pattern 1b: Broken link remnants like "*](https://lehmannws...)"
    text = re.sub(r'\*?\]\(https?://lehmannws\.wordpress\.com[^)]*\)\*{0,3}', '', text)
    # Pattern 2: Coaching/Training text
    text = re.sub(r'Interested in training or personalized coaching[^\n]*(?:success|skills|strategies)[^\n]*\.?\s*💡?', '', text, flags=re.IGNORECASE)
    # Pattern 3: Stray bold/italic markers left over
    text = re.sub(r'^\s*\*{1,3}\s*$', '', text, flags=re.MULTILINE)
    
    return text.strip()

def extract_block(html_content, label_emoji, label_text):
    pattern_start = r"(?:" + re.escape(label_emoji) + r")?\s*(?:<strong>|<b>)\s*" + re.escape(label_text) + r"\s*(?:</strong>|</b>).*?(?:<br\s*/>|:)"
    match = re.search(pattern_start, html_content, re.IGNORECASE)
    if not match: return ""
        
    start_pos = match.end()
    remainder = html_content[start_pos:]
    next_headers = ["💡", "✅", "🔧", "🎉", "🌟", "📌", "id=\"jp-post-flair\"", "class=\"entry-footer\"", "class=\"sharedaddy", "<div class=\"embed-youtube"]
    
    end_pos = len(remainder)
    for h in next_headers:
        idx = remainder.find(h)
        if idx != -1 and idx < end_pos:
            end_pos = idx
            
    raw_content = remainder[:end_pos]
    return clean_html_to_md(raw_content)

def extract_fallback_body(html_content):
    """Extracts body content when no structured headers are found."""
    # Start after entry-content div or title
    # We can try to just grab everything inside <div class="entry-content">...</div>
    # But using regex for that on full file is tricky.
    # Let's find start of entry-content
    start_marker = "class=\"entry-content\">"
    start_idx = html_content.find(start_marker)
    if start_idx == -1: return ""
    start_idx += len(start_marker)
    
    remainder = html_content[start_idx:]
    
    # End before sharedaddy or footer or youtube embed
    end_markers = ["<div id=\"jp-post-flair\"", "class=\"sharedaddy", "<div class=\"embed-youtube", "class=\"entry-footer\""]
    end_pos = len(remainder)
    for m in end_markers:
        idx = remainder.find(m)
        if idx != -1 and idx < end_pos:
            end_pos = idx
            
    raw_body = remainder[:end_pos]
    return clean_html_to_md(raw_body)

def process_single_tip(html_file, tip_num, md_file_path):
    print(f"Propcessing Tip {tip_num}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 1. Video ID
    video_id = ""
    match = re.search(r'src=["\'].*?(?:embed/|v=|youtu.be/)([\w-]+)', html_content)
    if match:
        video_id = match.group(1)
    
    # 2. Extract Sections (Strict)
    challenge = extract_block(html_content, "💡", "Challenge")
    solution = extract_block(html_content, "✅", "Solution")
    how = extract_block(html_content, "🔧", "How It’s Done")
    result = extract_block(html_content, "🎉", "Result")
    advantages = extract_block(html_content, "🌟", "Key Advantages")
    if not advantages: advantages = extract_block(html_content, "🌟", "Advantages")

    # 3. Clean Footer for Strict Sections
    challenge = clean_footer_text(challenge)
    solution = clean_footer_text(solution)
    how = clean_footer_text(how)
    result = clean_footer_text(result)
    advantages = clean_footer_text(advantages)

    # 4. Fallback Extraction
    fallback_body = ""
    used_fallback = False
    
    if not (challenge or solution or how):
        # No structure found. Use fallback.
        print(f"  [INFO] No structure for Tip {tip_num}. Using fallback.")
        fallback_body = extract_fallback_body(html_content)
        fallback_body = clean_footer_text(fallback_body)
        used_fallback = True

    # 5. Metadata / FAQ
    front_matter = get_frontmatter(md_content)
    faq_section = get_faq(md_content)

    # 6. Generate TL;DR
    tldr_text = ""
    if challenge:
        parts = challenge.split('.')
        if len(parts) > 0: tldr_text = parts[0].strip() + "."
    elif fallback_body:
         # First sentence of fallback
         parts = fallback_body.split('.')
         if len(parts) > 0: tldr_text = parts[0].strip() + "."
    
    # 7. Construct New Content
    new_content = front_matter + "\n\n"
    if tldr_text:
        new_content += f"## 📝 TL;DR\n{tldr_text}\n\n"
    
    if used_fallback:
        # Put everything under "Challenge" or a generic header?
        # Or just "## Details"
        # Strategy: Intro/Challenge -> How -> Result
        # Since we don't know, let's put it as "## 💡 Challenge & Solution" just to have a header
        # Or split by paragraphs? Too risky.
        # Let's use "## 💡 The Tip" as a generic header for fallback
        new_content += "## 💡 The Tip\n" + fallback_body + "\n\n"
    else:
        if challenge: new_content += "## 💡 Challenge\n" + challenge + "\n\n"
        if solution: new_content += "## ✅ Solution\n" + solution + "\n\n"
        if how: new_content += "## 🔧 How It's Done\n" + how + "\n\n"
        if result: new_content += "## 🎉 Result\n" + result + "\n\n"
        if advantages: new_content += "## 🌟 Key Advantages\n" + advantages + "\n\n"
    
    if video_id:
        new_content += f"## 🎥 Video Tutorial\n{{% include video id=\"{video_id}\" provider=\"youtube\" %}}\n\n"
    
    if faq_section:
        new_content += "---\n\n" + faq_section + "\n"
        
    # Check for meaningful content
    # total_len = len(challenge) + len(solution) + len(how) + len(fallback_body)
    # if total_len < 50:
    #     print(f"  [WARNING] Low content length ({total_len} chars) for Tip {tip_num}")

    # Output
    filename = os.path.basename(md_file_path)
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("--- Starting Batch Restoration ---")
    posts_map = build_posts_map()
    
    all_html_files = []
    all_html_files.extend(glob.glob(os.path.join(OLD_DIR, "*.html")))
    all_html_files.extend(glob.glob(os.path.join(READY_DIR, "*.html")))
    all_html_files = list(set(all_html_files)) 
    
    processed_count = 0
    
    for html_file in all_html_files:
        filename = os.path.basename(html_file)
        tip_num = get_tip_info_from_filename(filename)
        
        if not tip_num: continue
            
        if tip_num in posts_map:
            md_path = posts_map[tip_num]["path"]
            process_single_tip(html_file, tip_num, md_path)
            processed_count += 1
            
    print(f"Processed: {processed_count}")
    print(f"Output Directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
