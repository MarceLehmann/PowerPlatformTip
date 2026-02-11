import os
import re
import glob

def get_tip_number(filename):
    match = re.search(r'Tip\s*(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    match = re.search(r'platformtip-?(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return ""

def clean_html(html_content):
    # Remove script and style elements
    html_content = re.sub(r'<(script|style).*?</\1>', '', html_content, flags=re.DOTALL)
    # Remove tags
    text = re.sub(r'<[^>]+>', ' ', html_content)
    # Collapse whitespace
    return re.sub(r'\s+', ' ', text).strip() 

def clean_markdown(md_content):
    # Remove frontmatter
    if md_content.startswith('---'):
        parts = md_content.split('---', 2)
        if len(parts) > 2:
            return parts[2].strip()
    return md_content

old_dir = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\CONTENT\3_OLD"
posts_dir = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\_posts"

old_files = glob.glob(os.path.join(old_dir, "*.html"))
post_files = glob.glob(os.path.join(posts_dir, "*.md"))

old_map = {}
for f in old_files:
    num = get_tip_number(os.path.basename(f))
    if num:
        old_map[num] = f

post_map = {}
for f in post_files:
    num = get_tip_number(os.path.basename(f))
    if num:
        post_map[num] = f

print(f"{'Tip':<5} | {'OLD Len':<8} | {'POST Len':<8} | {'Diff':<6} | {'Issues'}")
print("-" * 100)

common_tips = sorted(list(set(old_map.keys()) & set(post_map.keys())))

# Keywords/Sections to check
required_sections = ["Challenge", "Solution", "How", "Result", "Key Advantages"]

for tip in common_tips:
    old_path = old_map[tip]
    post_path = post_map[tip]
    
    old_text = clean_html(read_file(old_path))
    post_text = clean_markdown(read_file(post_path))
    
    issues = []
    
    # Check for significant length reduction (e.g., > 20% loss)
    if len(old_text) > 0:
        ratio = len(post_text) / len(old_text)
        if ratio < 0.6:
            issues.append(f"Major Content Loss ({int(ratio*100)}%)")
        elif ratio < 0.8:
            issues.append(f"Content Loss ({int(ratio*100)}%)")
            
    # Check for missing sections in NEW content that represent structure
    # Note: Old content might not have these keywords exactly, so we focus on structure in the NEW content
    # But if the user says "structurally fine but content wrong", we should look for sections present in new but empty?
    # Or comparing count of code blocks?
    
    old_code_blocks = old_text.count('{') + old_text.count('}') # Rough proxy for code
    post_code_blocks = post_text.count('```')
    
    # Check for specific missing content if we can identify it in Old
    
    if len(issues) > 0 or len(post_text) < 500: # detailed report for problematic ones
        print(f"{tip:<5} | {len(old_text):<8} | {len(post_text):<8} | {len(old_text)-len(post_text):<6} | {', '.join(issues)}")

