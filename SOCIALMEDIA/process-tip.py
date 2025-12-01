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

# Farben für Terminal-Output
class Colors:
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def print_header():
    print(f"{Colors.BLUE}╔════════════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.BLUE}║  PowerPlatformTip Content Processor v2.0      ║{Colors.NC}")
    print(f"{Colors.BLUE}║  KI-Chat-Protokoll → Blog + Newsletter        ║{Colors.NC}")
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
    slug = slug.strip('-')
    return slug

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
    <div class="footer">Generated automatically from PowerPlatformTip Markdown fallback.</div>
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

def process_file(input_file, blog_dir, newsletter_dir):
    """Verarbeitet eine Input-Datei und erzeugt für alle PHASE 2 Varianten jeweils Blog+Newsletter."""
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

        blog_filename = f"{metadata['date']}-powerplatformtip-{metadata['tip_number']}-{slug}.md"
        blog_file = blog_dir / blog_filename
        blog_file.write_text(phase2_content, encoding='utf-8')
        print(f"{Colors.GREEN}  ✓ Blog Variante {idx} erstellt: {blog_filename}{Colors.NC}")

        # PHASE 3 einmal global extrahieren (falls vorhanden nur für erste Variante verwenden?)
        phase3_html = extract_phase_block(content, "PHASE 3", "html")
        if phase3_html:
            newsletter_filename = f"{metadata['date']}-tip-{metadata['tip_number']}-{slug}.html"
            (newsletter_dir / newsletter_filename).write_text(phase3_html, encoding='utf-8')
            print(f"{Colors.GREEN}    → Newsletter (PHASE 3) erstellt: {newsletter_filename}{Colors.NC}")
        else:
            fallback_html = generate_newsletter_from_markdown(metadata, phase2_content)
            newsletter_filename = f"{metadata['date']}-tip-{metadata['tip_number']}-{slug}.html"
            (newsletter_dir / newsletter_filename).write_text(fallback_html, encoding='utf-8')
            print(f"{Colors.YELLOW}    ⚠ Kein PHASE 3 → Fallback Newsletter erstellt: {newsletter_filename}{Colors.NC}")

        processed_variants += 1

    return processed_variants

def main():
    script_dir = Path(__file__).parent
    input_dir = script_dir / "1_INPUT"
    blog_dir = script_dir / "BLOG"
    newsletter_dir = script_dir / "NEWSLETTER"
    processed_dir = input_dir / "_PROCESSED"
    
    # Erstelle Verzeichnisse
    blog_dir.mkdir(exist_ok=True)
    newsletter_dir.mkdir(exist_ok=True)
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
        count_created = process_file(input_file, blog_dir, newsletter_dir)

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
    print(f"   {Colors.BLUE}BLOG/{Colors.NC} & {Colors.BLUE}NEWSLETTER/{Colors.NC} enthalten nun alle Varianten")
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
