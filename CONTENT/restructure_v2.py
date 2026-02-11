"""
Restructure v2: Re-build all NEWOPTIMIZEDPOSTS from HTML sources again
with improved inline section detection.

Key improvements:
- Detect non-bold inline headers: "💡 Challenge:" (not just **Challenge:**)
- Better paragraph splitting for unstructured content
- For very short tips: use 'The Tip' as combined Challenge+Solution
- Always generate all required sections
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
OLD_DIR = os.path.join(BASE, "CONTENT", "3_OLD")
READY_DIR = os.path.join(OLD_DIR, "ready")
NEW_DIR = os.path.join(BASE, "NEWOPTIMIZEDPOSTS")

# Section markers - both bold and non-bold
SECTION_MARKERS = [
    # (pattern_to_find, section_key)
    # Bold inline: 💡 **Challenge:** or ✅ **Solution:**
    (r'[\U0001f4a1]\s*\*\*Challenge:?\*\*\s*:?\s*', 'challenge'),
    (r'[\u2705]\s*\*\*Solution:?\*\*\s*:?\s*', 'solution'),
    (r'[\U0001f527]\s*\*\*How [Ii]t.s [Dd]one:?\*\*\s*:?\s*', 'how'),
    (r'[\U0001f389]\s*\*\*Result:?\*\*\s*:?\s*', 'result'),
    (r'[\U0001f31f]\s*\*\*(?:Key )?Advantages:?\*\*\s*:?\s*', 'advantages'),
    # Non-bold inline: 💡 Challenge: or ✅ Solution:
    (r'[\U0001f4a1]\s*Challenge:?\s*', 'challenge'),
    (r'[\u2705]\s*Solution:?\s*', 'solution'),
    (r'[\U0001f527]\s*How [Ii]t.s [Dd]one:?\s*', 'how'),
    (r'[\U0001f389]\s*Result:?\s*', 'result'),
    (r'[\U0001f31f]\s*(?:Key )?Advantages:?\s*', 'advantages'),
    # Also detect: 📌 Pro Tips:
    (r'[\U0001f4cc]\s*Pro Tips?:?\s*', 'pro_tips'),
]

def extract_sections_from_text(text):
    """Split text into sections by detecting inline section markers."""
    sections = {}
    
    # Find all marker positions
    markers = []
    for pattern, key in SECTION_MARKERS:
        for m in re.finditer(pattern, text):
            markers.append((m.start(), m.end(), key))
    
    # Sort by position
    markers.sort(key=lambda x: x[0])
    
    if not markers:
        return sections
    
    # Extract content between markers
    for i, (start, end, key) in enumerate(markers):
        if key in sections:
            continue  # First occurrence wins
        
        # Content goes from end of this marker to start of next marker
        if i + 1 < len(markers):
            content = text[end:markers[i+1][0]]
        else:
            content = text[end:]
        
        content = content.strip()
        if content:
            sections[key] = content
    
    # Merge pro_tips into advantages if no advantages
    if 'pro_tips' in sections and 'advantages' not in sections:
        sections['advantages'] = sections.pop('pro_tips')
    elif 'pro_tips' in sections:
        del sections['pro_tips']
    
    return sections


def restructure_from_current(filepath):
    """Read current NEWOPTIMIZEDPOSTS file and restructure using improved parsing."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    fm_match = re.match(r'^(---\s*\n.*?\n---)\s*\n', content, re.DOTALL)
    frontmatter = fm_match.group(1) if fm_match else ""
    
    # Get body (strip frontmatter)
    body = re.sub(r'^---.*?---\s*\n', '', content, flags=re.DOTALL)
    
    # Extract Video section
    video = ""
    vm = re.search(r'(## \U0001f3a5 Video Tutorial\s*\n.*?\n)', body, re.DOTALL)
    if vm:
        video = vm.group(0).strip()
    # Also check for just {% include video %} without header
    elif re.search(r'\{%\s*include video', body):
        vid_match = re.search(r'(\{%\s*include video.*?%\})', body)
        if vid_match:
            video = f"## \U0001f3a5 Video Tutorial\n{vid_match.group(1)}"
    
    # Extract FAQ section
    faq = ""
    faq_match = re.search(r'(---\s*\n\s*## \U0001f6e0\ufe0f FAQ.*)', body, re.DOTALL)
    if not faq_match:
        faq_match = re.search(r'(## \U0001f6e0\ufe0f FAQ.*)', body, re.DOTALL)
    if faq_match:
        faq = faq_match.group(0)
    
    # Get content body (remove existing ## headers, video, faq)
    content_body = body
    content_body = re.sub(r'## \U0001f4dd TL;DR\s*\n', '', content_body)
    content_body = re.sub(r'## \U0001f4a1 Challenge\s*\n', '', content_body)
    content_body = re.sub(r'## \u2705 Solution\s*\n', '', content_body)
    content_body = re.sub(r'## \U0001f527 How It\'s Done\s*\n', '', content_body)
    content_body = re.sub(r'## \U0001f389 Result\s*\n', '', content_body)
    content_body = re.sub(r'## \U0001f31f Key Advantages\s*\n', '', content_body)
    content_body = re.sub(r'## \U0001f4a1 The Tip\s*\n', '', content_body)
    content_body = re.sub(r'## \U0001f3a5 Video Tutorial\s*\n.*?\n', '', content_body, flags=re.DOTALL)
    content_body = re.sub(r'---\s*\n\s*## \U0001f6e0\ufe0f FAQ.*', '', content_body, flags=re.DOTALL)
    content_body = re.sub(r'## \U0001f6e0\ufe0f FAQ.*', '', content_body, flags=re.DOTALL)
    content_body = re.sub(r'\{%\s*include video.*?%\}', '', content_body)
    content_body = content_body.strip()
    
    # Try to detect inline section markers
    sections = extract_sections_from_text(content_body)
    
    # If inline detection found sections, great. Otherwise, heuristic split.
    if not sections.get('challenge'):
        # Heuristic: split into paragraphs
        paragraphs = re.split(r'\n\s*\n', content_body)
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        
        # Classify paragraphs
        numbered = [p for p in paragraphs if re.match(r'^\s*\d+[\.\)️⃣]', p)]
        bullets = [p for p in paragraphs if re.match(r'^\s*[\*\-]\s', p) and not re.match(r'^\s*\*\*', p)]
        star_items = [p for p in paragraphs if p.strip().startswith('\U0001f538') or p.strip().startswith('🔸')]
        regular = [p for p in paragraphs if p not in numbered and p not in bullets and p not in star_items]
        
        if regular:
            sections['challenge'] = regular[0]
            if len(regular) >= 2:
                sections['solution'] = regular[1]
            if len(regular) >= 3:
                sections['result'] = '\n\n'.join(regular[2:])
        
        if numbered or bullets:
            sections['how'] = '\n'.join(numbered + bullets)
        
        if star_items:
            sections['advantages'] = '\n'.join(star_items)
    
    # Build the new file
    new_content = frontmatter + '\n\n'
    
    # TL;DR: Use excerpt from frontmatter
    excerpt = ""
    em = re.search(r'excerpt:\s*"([^"]*)"', frontmatter)
    if em:
        excerpt = em.group(1)
    
    if excerpt:
        new_content += f'## \U0001f4dd TL;DR\n\n{excerpt}\n\n'
    
    if sections.get('challenge'):
        new_content += f'## \U0001f4a1 Challenge\n\n{sections["challenge"]}\n\n'
    
    if sections.get('solution'):
        new_content += f'## \u2705 Solution\n\n{sections["solution"]}\n\n'
    
    if sections.get('how'):
        new_content += f'## \U0001f527 How It\'s Done\n\n{sections["how"]}\n\n'
    
    if sections.get('result'):
        new_content += f'## \U0001f389 Result\n\n{sections["result"]}\n\n'
    
    if sections.get('advantages'):
        new_content += f'## \U0001f31f Key Advantages\n\n{sections["advantages"]}\n\n'
    
    if video:
        new_content += video + '\n\n'
    
    if faq:
        new_content += faq + '\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return sections


def main():
    files = sorted(glob.glob(os.path.join(NEW_DIR, "*.md")))
    files = [f for f in files if "VERIFICATION" not in os.path.basename(f)]
    
    restructured = 0
    already_ok = 0
    
    for f in files:
        fname = os.path.basename(f)
        tip = re.search(r'powerplatformtip-(\d+)', fname)
        num = tip.group(1) if tip else '?'
        
        with open(f, 'r', encoding='utf-8') as fh:
            body = re.sub(r'^---.*?---\s*', '', fh.read(), flags=re.DOTALL)
        
        has_challenge = bool(re.search(r'## \U0001f4a1 Challenge', body))
        has_solution = bool(re.search(r'## \u2705 Solution', body))
        has_how = bool(re.search(r'## \U0001f527 How', body))
        has_result = bool(re.search(r'## \U0001f389 Result', body))
        has_advantages = bool(re.search(r'## \U0001f31f Key Advantages', body))
        
        all_ok = all([has_challenge, has_solution, has_how, has_result, has_advantages])
        
        if all_ok:
            already_ok += 1
            continue
        
        sections = restructure_from_current(f)
        restructured += 1
        keys = list(sections.keys())
        print(f"  Tip {num}: {keys}")
    
    print(f"\nDone: {restructured} restructured, {already_ok} already OK")

if __name__ == "__main__":
    main()
