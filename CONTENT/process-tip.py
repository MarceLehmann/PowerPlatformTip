#!/usr/bin/env python3
"""
PowerPlatformTip Content Processor v2.0
Intelligente Verarbeitung von KI-generierten Chat-Protokollen
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
import io

# Force UTF-8 output for Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Farben für Terminal-Output
    
    # Farben für Terminal-Output
class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def print_header():
    print(f"{Colors.BLUE}╔════════════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.BLUE}║  PowerPlatformTip Content Processor v2.1      ║{Colors.NC}")
    print(f"{Colors.BLUE}║  KI-Chat-Protokoll → Output Folder            ║{Colors.NC}")
    print(f"{Colors.BLUE}╚════════════════════════════════════════════════╝{Colors.NC}\n")

def extract_phase_block(content, phase_name, code_type="markdown"):
    """Extrahiert den letzten PHASE-Block (Rückwärtskompatibilität)."""
    blocks = extract_phase_blocks(content, phase_name, code_type)
    return blocks[-1] if blocks else None

def extract_phase_blocks(content, phase_name, code_type="markdown"):
    """Extrahiert alle PHASE-Blöcke als Liste (Erscheinungsreihenfolge)."""
    pattern = rf'###\s*{phase_name}\s*[^\n]*\n\n```{code_type}\n(.*?)```'
    matches = list(re.finditer(pattern, content, re.DOTALL | re.IGNORECASE))
    return [m.group(1).strip() for m in matches]

def extract_metadata(markdown_content):
    """Extrahiert Metadaten aus dem Jekyll Frontmatter"""
    metadata = {}
    
    # Tip Nummer
    tip_match = re.search(r'#PowerPlatformTip\s+(\d+)', markdown_content)
    if tip_match:
        metadata['tip_number'] = tip_match.group(1)
    
    # Datum
    date_match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', markdown_content, re.MULTILINE)
    if date_match:
        metadata['date'] = date_match.group(1)
    
    # Titel (ohne Tip-Nummer)
    title_match = re.search(r'^title:\s*["\']?#PowerPlatformTip\s+\d+\s*[–-]\s*["\']?([^"\']+)["\']?', markdown_content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        # Entferne führende/nachfolgende Quotes
        title = re.sub(r'^["\']|["\']$', '', title)
        metadata['title'] = title
    
    return metadata

def create_slug(title):
    """Erstellt einen URL-freundlichen Slug aus dem Titel"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug

def html_to_systeme_markdown(html_content):
    """
    Converts HTML content to systeme.io compatible markdown.
    Supported: **bold**, *italic*, lists, [links](url).
    Headers are converted to **bold**.
    """
    # Normalize newlines
    text = html_content.replace('\r\n', '\n').replace('\r', '\n')
    
    # 0. Remove Head, Style, Script blocks entirely
    text = re.sub(r'<(head|style|script)[^>]*>.*?</\1>', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 1. SPECIAL: Handle Template-Specific Classes (Before generic tag stripping)
    
    # .section-title -> **Title**
    text = re.sub(r'<div class="section-title">\s*(.*?)\s*</div>', r'\n\n**\1**\n\n', text, flags=re.IGNORECASE)
    
    # .step -> 1. **Title**: Content
    text = re.sub(
        r'<div class="step">.*?<span class="step-number">(\d+)</span>\s*<b>(.*?)</b>\s*<br>\s*(.*?)</div>', 
        r'\n\n\1. **\2**: \3', 
        text, flags=re.IGNORECASE | re.DOTALL
    )

    # .use-case -> **Title**\nContent
    text = re.sub(
        r'<div class="use-case">\s*<div class="use-case-title">\s*(.*?)\s*</div>\s*(.*?)</div>', 
        r'\n\n**\1**\n\2', 
        text, flags=re.IGNORECASE | re.DOTALL
    )

    # .faq-item -> **Q: ...**\nA: ...
    text = re.sub(
        r'<div class="faq-item">\s*<div class="faq-question">\s*(.*?)\s*</div>\s*(.*?)</div>', 
        r'\n\n**\1**\n\2', 
        text, flags=re.IGNORECASE | re.DOTALL
    )
    
    # 2. Links: <a href="url">text</a> -> [text](url)
    text = re.sub(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Lists
    text = re.sub(r'</?[uo]l[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<li[^>]*>\s*(.*?)\s*</li>', r'- \1\n', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 4. Bold/Headers -> **text**
    header_pattern = r'<(h[1-6]|b|strong)[^>]*>\s*(.*?)\s*</\1>'
    def header_replacer(match):
        tag = match.group(1).lower()
        content = match.group(2)
        if tag.startswith('h'): return f'\n\n**{content}**\n\n'
        return f'**{content}**'

    text = re.sub(header_pattern, header_replacer, text, flags=re.IGNORECASE | re.DOTALL)
    
    # 5. Italic -> *text*
    text = re.sub(r'<(i|em)[^>]*>\s*(.*?)\s*</\1>', r'*\2*', text, flags=re.IGNORECASE | re.DOTALL)
    
    # 5. Paragraphs and breaks
    text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    
    # 6. Remove all other tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # 7. Clean up multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()

def generate_systeme_io_content(metadata, block_content, is_html=False):
    """Generates systeme.io compatible markdown content."""
    
    title_line = f"# PowerPlatformTip #{metadata.get('tip_number', 'XXX')}: {metadata.get('title', 'Title')}\n\n"
    footer = f"\n\n---\n[Mehr erfahren](https://www.powerplatformtip.com)"

    if is_html:
        # Use HTML conversion
        converted_body = html_to_systeme_markdown(block_content)
        return title_line + converted_body + footer
    else:
        # Fallback: Extract from Markdown
        challenge = extract_section(block_content, '💡 Challenge')
        solution = extract_section(block_content, '✅ Solution')
        advantages = extract_section(block_content, '🌟 Key Advantages')

        # Parse advantages to ensure clean list format
        adv_items = []
        for raw_line in advantages.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith('🔸') or line.startswith('-'):
                cleaned = re.sub(r'^(🔸\s*|-\s*)', '', line).strip()
                adv_items.append(cleaned)
        
        systeme_content = f"""{title_line}**💡 Challenge**

{challenge}

**✅ Solution**

{solution}

**🌟 Key Advantages**

"""
        for item in adv_items:
            systeme_content += f"- {item}\n"

        return systeme_content + footer

def generate_newsletter_from_markdown(metadata, markdown_content):
    """Erzeuge einfachen HTML Newsletter aus dem Markdown (Fallback) mit sauberer Bullet-Liste."""
    challenge = extract_section(markdown_content, '💡 Challenge')
    solution = extract_section(markdown_content, '✅ Solution')
    advantages = extract_section(markdown_content, '🌟 Key Advantages')

    # Vorteile Zeilenweise parsen (Originalzeilen erhalten)
    adv_items = []
    for raw_line in advantages.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith('🔸') or line.startswith('-'):
            cleaned = re.sub(r'^(🔸\s*|-\s*)', '', line).strip()
            adv_items.append(cleaned)
    advantages_html = ''.join(f'<li>{item}</li>' for item in adv_items)

    title = metadata.get('title', 'PowerPlatformTip')
    tip_number = metadata.get('tip_number', 'XXX')
    date = metadata.get('date', '')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>PowerPlatformTip {tip_number}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height:1.5; max-width:640px; margin:0 auto; padding:24px; }}
        h1 {{ color:#0d9488; }}
        .section {{ margin-bottom:20px; }}
        ul {{ padding-left:20px; }}
        .footer {{ font-size:12px; color:#666; margin-top:40px; }}
        .cta a {{ display:inline-block; background:#0d9488; color:#fff; padding:10px 16px; text-decoration:none; border-radius:6px; }}
    </style>
</head>
<body>
    <h1>PowerPlatformTip #{tip_number}: {title}</h1>
    <p><em>{date}</em></p>
    <div class="section">
        <h2>Challenge</h2>
        <p>{challenge}</p>
    </div>
    <div class="section">
        <h2>Solution</h2>
        <p>{solution}</p>
    </div>
    <div class="section">
        <h2>Key Advantages</h2>
        <ul>{advantages_html}</ul>
    </div>
    <div class="section cta">
        <a href="https://www.powerplatformtip.com" target="_blank" rel="noopener">Mehr erfahren</a>
    </div>
    <div class="footer">Generated automatically from PowerPlatformTip Markdown fallback. © 2026</div>
</body>
</html>"""
    return html

def extract_section(markdown_content, heading):
    """Extrahiert Text unter einer Abschnittsüberschrift bis zur nächsten Überschrift (Zeilen erhalten)."""
    lines = markdown_content.splitlines()
    capture = False
    buffer = []
    for line in lines:
        if line.strip().startswith('##') and heading in line:
            capture = True
            continue
        if capture:
            if line.strip().startswith('## '):  # nächste Überschrift beginnt
                break
            buffer.append(line)
    return '\n'.join(buffer).strip()

def process_file(input_file, output_base_dir):
    """Verarbeitet eine Input-Datei und erzeugt Output-Ordner pro Tip."""
    print(f"{Colors.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.NC}")
    print(f"{Colors.GREEN}📄 {input_file.name}{Colors.NC}\n")

    content = input_file.read_text(encoding='utf-8')

    print(f"{Colors.BLUE}  → Suche PHASE 2 Varianten (Jekyll Markdown)...{Colors.NC}")
    phase2_blocks = extract_phase_blocks(content, "PHASE 2.*JEKYLL MARKDOWN", "markdown")

    if not phase2_blocks:
        print(f"{Colors.YELLOW}  ⚠ Kein PHASE 2 Block gefunden{Colors.NC}")
        return 0

    processed_variants = 0
    for idx, phase2_content in enumerate(phase2_blocks, start=1):
        metadata = extract_metadata(phase2_content)
        if not (metadata.get('tip_number') and metadata.get('date') and metadata.get('title')):
            print(f"{Colors.YELLOW}  ⚠ Variante {idx}: Metadaten unvollständig – übersprungen{Colors.NC}")
            continue

        phase2_content = re.sub(r'toc_sticky:\s*true', 'toc_sticky: false', phase2_content)
        slug = create_slug(metadata['title'])
        
        # Erstelle Tip-spezifischen Ordner in 2_OUTPUT
        tip_folder_name = f"{metadata['date']}-tip-{metadata['tip_number']}-{slug}"
        tip_dir = output_base_dir / tip_folder_name
        tip_dir.mkdir(parents=True, exist_ok=True)

        # 1. Blog Post
        blog_filename = f"{metadata['date']}-powerplatformtip-{metadata['tip_number']}-{slug}.md"
        blog_file = tip_dir / blog_filename
        blog_file.write_text(phase2_content, encoding='utf-8')
        print(f"{Colors.GREEN}  ✓ Blog Variante {idx} erstellt: {tip_folder_name}/{blog_filename}{Colors.NC}")

        # 2. Newsletter HTML (PHASE 3 oder Fallback)
        phase3_html = extract_phase_block(content, "PHASE 3", "html")
        newsletter_filename = f"{metadata['date']}-tip-{metadata['tip_number']}-{slug}.html"
        
        if phase3_html:
            (tip_dir / newsletter_filename).write_text(phase3_html, encoding='utf-8')
            print(f"{Colors.GREEN}    → Newsletter (PHASE 3) erstellt: {newsletter_filename}{Colors.NC}")
            
            # 3a. Systeme.io from HTML
            systeme_content = generate_systeme_io_content(metadata, phase3_html, is_html=True)
        else:
            fallback_html = generate_newsletter_from_markdown(metadata, phase2_content)
            (tip_dir / newsletter_filename).write_text(fallback_html, encoding='utf-8')
            print(f"{Colors.YELLOW}    ⚠ Kein PHASE 3 → Fallback Newsletter erstellt: {newsletter_filename}{Colors.NC}")
            
            # 3b. Systeme.io from Markdown Fallback
            systeme_content = generate_systeme_io_content(metadata, phase2_content, is_html=False)
            
        # Write Systeme.io content
        systeme_filename = "newsletter-systeme.md"
        (tip_dir / systeme_filename).write_text(systeme_content, encoding='utf-8')
        print(f"{Colors.GREEN}    → Systeme.io Newsletter erstellt: {systeme_filename}{Colors.NC}")

        processed_variants += 1

    return processed_variants

def main():
    script_dir = Path(__file__).parent
    input_dir = script_dir / "1_INPUT"
    output_base_dir = script_dir / "2_OUTPUT"
    processed_dir = input_dir / "_PROCESSED"
    
    # Erstelle Verzeichnisse
    output_base_dir.mkdir(exist_ok=True)
    processed_dir.mkdir(exist_ok=True)
    
    print_header()
    
    # Suche Input-Dateien
    input_files = [f for f in input_dir.glob("*.md") if not f.name.startswith("EXAMPLE")]
    
    if not input_files:
        print(f"{Colors.YELLOW}⚠  Keine Markdown-Dateien im INPUT-Ordner gefunden.{Colors.NC}")
        print(f"   Lege KI-Chat-Protokolle in {Colors.BLUE}1_INPUT/{Colors.NC} ab.\n")
        return
    
    print(f"{Colors.GREEN}✓ {len(input_files)} Datei(en) gefunden{Colors.NC}\n")
    
    processed_count = 0
    
    for input_file in input_files:
        count_created = process_file(input_file, output_base_dir)

        # Archiviere Input-Datei
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archived_name = f"{timestamp}_{input_file.name}"
        input_file.rename(processed_dir / archived_name)
        
        print(f"\n{Colors.GREEN}  ✓ Archiviert: _PROCESSED/{archived_name}{Colors.NC}\n")
        
        if count_created:
            processed_count += 1
    
    print(f"{Colors.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.NC}")
    print(f"{Colors.GREEN}✓ Verarbeitung abgeschlossen!{Colors.NC}\n")
    print(f"📊 Statistik:")
    print(f"   {Colors.GREEN}{processed_count}{Colors.NC} von {len(input_files)} Datei(en) mit mind. einer Variante verarbeitet")
    print(f"   {Colors.BLUE}2_OUTPUT/{Colors.NC} enthält nun die generierten Ordner")
    print(f"\n{Colors.YELLOW}💡 Nächster Schritt:{Colors.NC} Blog-Posts nach {Colors.BLUE}_posts/{Colors.NC} kopieren\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Abgebrochen{Colors.NC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Fehler: {e}{Colors.NC}")
        sys.exit(1)
