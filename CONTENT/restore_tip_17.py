import os
import re

# Hardcoded for Tip 17 Example
TIP_NUMBER = 17
OLD_HTML_PATH = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\CONTENT\3_OLD\#PowerPlatformTip 17 – ‘Format data by example’.html"
NEW_MD_PATH = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\_posts\2023-01-05-powerplatformtip-17-format-data-by-example-.md"

# Updated to use NEWOPTIMIZEDPOSTS - fixed path construction
BASE_DIR = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
OUTPUT_DIR = os.path.join(BASE_DIR, "NEWOPTIMIZEDPOSTS")

# Ensure output dir exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_frontmatter(md_content):
    """Extracts front matter from existing markdown."""
    pattern = r"^(---\s+.*?\s+---)"
    match = re.search(pattern, md_content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def get_faq(md_content):
    """Extracts FAQ section from existing markdown."""
    pattern = r"## 🛠️ FAQ\s+(.*)"
    match = re.search(pattern, md_content, re.DOTALL)
    if match:
        return match.group(0) # Include header
    return ""

def clean_html_to_md(html_text):
    """Converts HTML snippet to clean Markdown."""
    if not html_text: return ""
    
    # 1. Lists
    # Convert lists to markdown syntax
    html_text = re.sub(r'<li>\s*(.*?)\s*</li>', r'* \1\n', html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r'</?ul>', '\n', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'</?ol>', '\n', html_text, flags=re.IGNORECASE)
    
    # 2. Paragraphs / Breaks
    html_text = re.sub(r'<p[^>]*>', '', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'</p>', '\n\n', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'<br\s*/?>', '\n', html_text, flags=re.IGNORECASE)
    
    # 3. Bold / Italic
    html_text = re.sub(r'<(strong|b)[^>]*>\s*(.*?)\s*</\1>', r'**\2**', html_text, flags=re.IGNORECASE)
    html_text = re.sub(r'<(em|i)[^>]*>\s*(.*?)\s*</\1>', r'*\2*', html_text, flags=re.IGNORECASE)
    
    # 4. Links
    html_text = re.sub(r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_text, flags=re.IGNORECASE)
    
    # 5. Headers (if any remained)
    html_text = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'### \1\n\n', html_text, flags=re.IGNORECASE)
    
    # 6. Clean Tags
    html_text = re.sub(r'<[^>]+>', '', html_text)
    
    # 7. Decode Entities
    html_text = html_text.replace('&nbsp;', ' ').replace('&#8217;', "'").replace('&#8216;', "'")
    html_text = re.sub(r'\n{3,}', '\n\n', html_text)
    
    return html_text.strip()

def extract_block(html_content, label_emoji, label_text):
    """Extracts a section starting with specific Emoji/Text."""
    # Pattern: <p>{emoji} <strong>{text}</strong>: <br />(.*?)</p>
    # Note: HTML might vary slightly, so be flexible with whitespace
    
    # Try finding the header match first
    # Regex for the start
    # We look for the label text, optionally preceded by emoji
    pattern_start = r"(?:" + re.escape(label_emoji) + r")?\s*(?:<strong>|<b>)\s*" + re.escape(label_text) + r"\s*(?:</strong>|</b>).*?(?:<br\s*/>|:)"
    
    # Find where it starts
    match = re.search(pattern_start, html_content, re.IGNORECASE)
    if not match:
        return ""
        
    start_pos = match.end()
    
    # Capture until the NEXT known section header
    # Strategy: Slice from start_pos
    remainder = html_content[start_pos:]
    
    # Known headers to stop at
    next_headers = ["💡", "✅", "🔧", "🎉", "🌟", "📌", "id=\"jp-post-flair\"", "class=\"entry-footer\"", "class=\"sharedaddy"]
    
    end_pos = len(remainder)
    
    for h in next_headers:
        idx = remainder.find(h)
        if idx != -1 and idx < end_pos:
            end_pos = idx
            
    # Also check if we hit the end of entry-content div (heuristic)
    
    raw_content = remainder[:end_pos]
    return clean_html_to_md(raw_content)

def process_tip_17():
    print(f"Processing Tip {TIP_NUMBER} -> NEWOPTIMIZEDPOSTS...")
    
    # 1. Read Files
    with open(OLD_HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    with open(NEW_MD_PATH, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 2. Extract Video ID (Regex)
    video_id = ""
    match = re.search(r'src=["\'].*?(?:embed/|v=|youtu.be/)([\w-]+)', html_content)
    if match:
        video_id = match.group(1)
    
    # 3. Extract Sections
    # We pass the full HTML content to the extractor.
    challenge_html = extract_block(html_content, "💡", "Challenge")
    solution_html = extract_block(html_content, "✅", "Solution")
    how_html = extract_block(html_content, "🔧", "How It’s Done")
    result_html = extract_block(html_content, "🎉", "Result")
    advantages_html = extract_block(html_content, "🌟", "Key Advantages")

    # 4. Extract Metadata / FAQ from Markdown
    front_matter = get_frontmatter(md_content)
    faq_section = get_faq(md_content)

    # 5. Generate TL;DR (First sentence of Challenge)
    tldr_text = "TL;DR not found."
    if challenge_html:
        # simplistic: split by dot
        parts = challenge_html.split('.')
        if len(parts) > 0:
            tldr_text = parts[0].strip() + "."
    elif solution_html:
        parts = solution_html.split('.')
        if len(parts) > 0:
            tldr_text = parts[0].strip() + "."

    # 6. Construct New Content
    new_content = front_matter + "\n\n"
    new_content += f"## 📝 TL;DR\n{tldr_text}\n\n"
    
    if challenge_html: new_content += "## 💡 Challenge\n" + challenge_html + "\n\n"
    if solution_html: new_content += "## ✅ Solution\n" + solution_html + "\n\n"
    if how_html: new_content += "## 🔧 How It's Done\n" + how_html + "\n\n"
    if result_html: new_content += "## 🎉 Result\n" + result_html + "\n\n"
    if advantages_html: new_content += "## 🌟 Key Advantages\n" + advantages_html + "\n\n"
    
    if video_id:
        new_content += f"## 🎥 Video Tutorial\n{{% include video id=\"{video_id}\" provider=\"youtube\" %}}\n\n"
    
    if faq_section:
        new_content += "---\n\n" + faq_section + "\n"
        
    # 7. Write Output to NEWOPTIMIZEDPOSTS
    filename = os.path.basename(NEW_MD_PATH)
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Restored content written to: {output_path}")

if __name__ == "__main__":
    process_tip_17()
