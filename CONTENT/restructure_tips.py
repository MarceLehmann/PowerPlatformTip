"""
Restructure NEWOPTIMIZEDPOSTS files that use 'The Tip' fallback
into the standard structure: TL;DR, Challenge, Solution, How, Result, Advantages.

Strategy for unstructured fallback content:
- If content already has inline bold headers like **Challenge:**, split on those
- If content has numbered lists, put those under 'How It's Done'
- First paragraph -> Challenge, next paragraph -> Solution
- Numbered/bulleted content -> How It's Done
- Any remaining -> Result
- Emoji bullets (star items) -> Key Advantages
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
NEW_DIR = os.path.join(BASE, "NEWOPTIMIZEDPOSTS")

def get_frontmatter(content):
    m = re.match(r'^(---\s*\n.*?\n---)\s*\n', content, re.DOTALL)
    return m.group(1) if m else ""

def get_faq(content):
    m = re.search(r'(---\s*\n\s*## \U0001f6e0\ufe0f FAQ.*)', content, re.DOTALL)
    if not m:
        m = re.search(r'(## \U0001f6e0\ufe0f FAQ.*)', content, re.DOTALL)
    return m.group(0) if m else ""

def get_video(content):
    m = re.search(r'(## \U0001f3a5 Video Tutorial\s*\n.*?\n)', content, re.DOTALL)
    return m.group(0).strip() if m else ""

def get_body(content):
    """Get body between frontmatter and video/FAQ sections."""
    body = re.sub(r'^---.*?---\s*\n', '', content, flags=re.DOTALL)
    body = re.sub(r'## \U0001f3a5 Video Tutorial.*', '', body, flags=re.DOTALL)
    body = re.sub(r'---\s*\n\s*## \U0001f6e0\ufe0f FAQ.*', '', body, flags=re.DOTALL)
    body = re.sub(r'## \U0001f6e0\ufe0f FAQ.*', '', body, flags=re.DOTALL)
    # Remove existing TL;DR section
    body = re.sub(r'## \U0001f4dd TL;DR\s*\n.*?\n(?=##|\Z)', '', body, flags=re.DOTALL)
    # Remove "The Tip" header
    body = re.sub(r'## \U0001f4a1 The Tip\s*\n', '', body)
    return body.strip()

def split_inline_sections(body):
    """Try to split body that has inline bold headers like **Challenge:** etc."""
    sections = {}
    
    # Check for inline bold headers
    patterns = [
        (r'\U0001f4a1\s*\*\*Challenge:?\*\*\s*:?\s*\n?(.*?)(?=\u2705|\U0001f527|\U0001f389|\U0001f31f|\Z)', 'challenge'),
        (r'\u2705\s*\*\*Solution:?\*\*\s*:?\s*\n?(.*?)(?=\U0001f527|\U0001f389|\U0001f31f|\Z)', 'solution'),
        (r'\U0001f527\s*\*\*How [Ii]t.s [Dd]one:?\*\*\s*:?\s*\n?(.*?)(?=\U0001f389|\U0001f31f|\Z)', 'how'),
        (r'\U0001f389\s*\*\*Result:?\*\*\s*:?\s*\n?(.*?)(?=\U0001f31f|\Z)', 'result'),
        (r'\U0001f31f\s*\*\*(?:Key )?Advantages:?\*\*\s*:?\s*\n?(.*?)(?=\Z)', 'advantages'),
    ]
    
    for pattern, key in patterns:
        m = re.search(pattern, body, re.DOTALL)
        if m:
            sections[key] = m.group(1).strip()
    
    return sections

def heuristic_split(body):
    """Split unstructured body into sections using heuristics."""
    sections = {}
    
    # Clean up whitespace-only lines
    lines = body.split('\n')
    lines = [l for l in lines if l.strip()]
    
    if not lines:
        return sections
    
    # Group into paragraphs (separated by empty content)
    paragraphs = []
    current = []
    for line in lines:
        if line.strip():
            current.append(line)
        else:
            if current:
                paragraphs.append('\n'.join(current))
                current = []
    if current:
        paragraphs.append('\n'.join(current))
    
    if not paragraphs:
        return sections
    
    # Find numbered list items and bullet points
    numbered_items = []
    bullet_items = []
    star_items = []
    regular_text = []
    
    for p in paragraphs:
        if re.match(r'^\s*\d+[\.\)️⃣]', p) or re.match(r'^\s*\*\s+\*\*\d+', p):
            numbered_items.append(p)
        elif p.strip().startswith('\U0001f538') or p.strip().startswith('🔸'):
            star_items.append(p)
        elif re.match(r'^\s*[\*\-]\s', p):
            bullet_items.append(p)
        else:
            regular_text.append(p)
    
    # Assign to sections
    if len(regular_text) >= 2:
        sections['challenge'] = regular_text[0]
        sections['solution'] = regular_text[1]
        if len(regular_text) >= 3:
            sections['result'] = regular_text[2]
        if len(regular_text) >= 4:
            extra = '\n\n'.join(regular_text[3:])
            sections['result'] = sections.get('result', '') + '\n\n' + extra
    elif len(regular_text) == 1:
        sections['challenge'] = regular_text[0]
    
    if numbered_items or bullet_items:
        sections['how'] = '\n\n'.join(numbered_items + bullet_items)
    
    if star_items:
        sections['advantages'] = '\n\n'.join(star_items)
    
    return sections

def restructure_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter = get_frontmatter(content)
    video = get_video(content)
    faq = get_faq(content)
    body = get_body(content)
    
    if not body.strip():
        return False, "Empty body"
    
    # Try inline section extraction first
    sections = split_inline_sections(body)
    
    # If that didn't work well, use heuristic split
    if not sections.get('challenge') and not sections.get('solution'):
        sections = heuristic_split(body)
    
    # Generate TL;DR from challenge or first text
    tldr = ""
    if sections.get('challenge'):
        first_sent = sections['challenge'].split('.')[0]
        if len(first_sent) > 20:
            tldr = first_sent.strip() + '.'
    
    # Build new content
    new = frontmatter + '\n\n'
    
    if tldr:
        new += f'## \U0001f4dd TL;DR\n\n{tldr}\n\n'
    
    if sections.get('challenge'):
        new += f'## \U0001f4a1 Challenge\n\n{sections["challenge"]}\n\n'
    
    if sections.get('solution'):
        new += f'## \u2705 Solution\n\n{sections["solution"]}\n\n'
    
    if sections.get('how'):
        new += f'## \U0001f527 How It\'s Done\n\n{sections["how"]}\n\n'
    
    if sections.get('result'):
        new += f'## \U0001f389 Result\n\n{sections["result"]}\n\n'
    
    if sections.get('advantages'):
        new += f'## \U0001f31f Key Advantages\n\n{sections["advantages"]}\n\n'
    
    if video:
        new += video + '\n\n'
    
    if faq:
        new += faq + '\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new)
    
    return True, sections.keys()

def main():
    files = sorted(glob.glob(os.path.join(NEW_DIR, "*.md")))
    files = [f for f in files if "VERIFICATION" not in os.path.basename(f)]
    
    restructured = 0
    skipped = 0
    errors = []
    
    for f in files:
        fname = os.path.basename(f)
        
        with open(f, 'r', encoding='utf-8') as fh:
            body = re.sub(r'^---.*?---\s*', '', fh.read(), flags=re.DOTALL)
        
        # Check if already compliant
        has_challenge = bool(re.search(r'## .* Challenge', body))
        has_solution = bool(re.search(r'## .* Solution', body))
        has_how = bool(re.search(r'## .* How', body))
        has_the_tip = bool(re.search(r'## .* The Tip', body))
        
        # Skip if already properly structured (has at least Challenge+Solution+How)
        if has_challenge and has_solution and has_how and not has_the_tip:
            skipped += 1
            continue
        
        tip = re.search(r'powerplatformtip-(\d+)', fname)
        num = tip.group(1) if tip else '?'
        
        ok, info = restructure_file(f)
        if ok:
            restructured += 1
            print(f"  Restructured Tip {num}: {list(info)}")
        else:
            errors.append(f"Tip {num}: {info}")
            print(f"  ERROR Tip {num}: {info}")
    
    print(f"\nDone: {restructured} restructured, {skipped} already OK, {len(errors)} errors")

if __name__ == "__main__":
    main()
