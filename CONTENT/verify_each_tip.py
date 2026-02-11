"""
Per-file verification: Compare each NEWOPTIMIZEDPOSTS markdown
against its original HTML source in 3_OLD or 3_OLD/ready.
Checks: video ID, content length, footer remnants, HTML entities, sections.
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
NEW_DIR = os.path.join(BASE, "NEWOPTIMIZEDPOSTS")
OLD_DIR = os.path.join(BASE, "CONTENT", "3_OLD")
READY_DIR = os.path.join(OLD_DIR, "ready")

def get_tip_num(filename):
    m = re.search(r'(?:Tip|PlatformTip)[\s-]*(\d+)', filename, re.IGNORECASE)
    return int(m.group(1)) if m else None

def build_old_map():
    """Map tip number -> html file path."""
    m = {}
    for f in glob.glob(os.path.join(OLD_DIR, "*.html")) + glob.glob(os.path.join(READY_DIR, "*.html")):
        num = get_tip_num(os.path.basename(f))
        if num:
            m[num] = f
    return m

# IDs to ignore (WordPress tracking pixels, not real videos)
IGNORE_VIDEO_IDS = {'wpcom-no-pv', 'videoseries'}

def extract_video_ids(text):
    """Extract all YouTube video IDs from text."""
    ids = set()
    for m in re.finditer(r'(?:embed/|v=|youtu\.be/|video\s+id=["\'])([\w-]{11})', text):
        vid = m.group(1)
        if vid not in IGNORE_VIDEO_IDS:
            ids.add(vid)
    return ids

def extract_text_from_html(html):
    """Strip tags to get approximate plain text length."""
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Get entry-content only
    start = text.find('class="entry-content">')
    if start != -1:
        text = text[start:]
        # End before footer
        for marker in ['id="jp-post-flair"', 'class="sharedaddy', 'class="entry-footer"']:
            idx = text.find(marker)
            if idx != -1:
                text = text[:idx]
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def check_footer_remnants(md_text):
    """Check for known footer text that should have been removed."""
    issues = []
    if re.search(r'overview above all.*PowerPlatformTip', md_text, re.IGNORECASE):
        issues.append("Footer: 'overview above all' text found")
    if re.search(r'Interested in training or personalized coaching', md_text, re.IGNORECASE):
        issues.append("Footer: 'training/coaching' text found")
    if re.search(r'lehmannws\.wordpress\.com', md_text):
        issues.append("Footer: WordPress link remnant found")
    return issues

def check_html_entities(md_text):
    """Check for unresolved HTML entities."""
    issues = []
    entities = re.findall(r'&(?:#\d+|[a-zA-Z]+);', md_text)
    # Filter out legitimate ones like &amp; in code blocks
    bad = [e for e in entities if e not in ['&amp;', '&lt;', '&gt;']]
    if bad:
        unique = list(set(bad))[:5]
        issues.append(f"HTML entities not decoded: {', '.join(unique)}")
    return issues

def check_sections(md_text):
    """Check which sections exist."""
    sections = {}
    for label in ['TL;DR', 'Challenge', 'Solution', "How It's Done", 'Result', 'Key Advantages', 'The Tip', 'Video Tutorial', 'FAQ']:
        sections[label] = bool(re.search(r'##.*' + re.escape(label), md_text))
    return sections

def check_frontmatter(md_text):
    """Check frontmatter completeness."""
    issues = []
    fm = re.search(r'^---\s+(.*?)\s+---', md_text, re.DOTALL)
    if not fm:
        issues.append("MISSING frontmatter!")
        return issues
    fm_text = fm.group(1)
    for field in ['title', 'date', 'categories', 'tags', 'excerpt']:
        if field + ':' not in fm_text:
            issues.append(f"Frontmatter missing: {field}")
    return issues

def main():
    old_map = build_old_map()
    new_files = sorted(glob.glob(os.path.join(NEW_DIR, "*.md")))
    
    report_lines = []
    report_lines.append("# Per-File Verification Report\n")
    report_lines.append(f"Total files in NEWOPTIMIZEDPOSTS: {len(new_files)}\n")
    
    issues_count = 0
    ok_count = 0
    
    for nf in new_files:
        fname = os.path.basename(nf)
        tip_num = get_tip_num(fname)
        
        with open(nf, 'r', encoding='utf-8') as f:
            md_text = f.read()
        
        tip_issues = []
        
        # 1. Find matching HTML
        html_file = old_map.get(tip_num)
        if not html_file:
            tip_issues.append("NO matching HTML source found in 3_OLD!")
        else:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_text = f.read()
            
            # 2. Compare video IDs
            html_vids = extract_video_ids(html_text)
            md_vids = extract_video_ids(md_text)
            
            if html_vids and not md_vids:
                tip_issues.append(f"MISSING video! HTML has: {html_vids}")
            elif html_vids and md_vids and html_vids != md_vids:
                tip_issues.append(f"Video mismatch! HTML={html_vids}, MD={md_vids}")
            
            # 3. Content length comparison
            html_plain = extract_text_from_html(html_text)
            # Strip frontmatter and FAQ for fair comparison
            md_body = re.sub(r'^---.*?---\s*', '', md_text, flags=re.DOTALL)
            md_body = re.sub(r'## 🛠️ FAQ.*', '', md_body, flags=re.DOTALL)
            md_body = re.sub(r'\s+', ' ', md_body).strip()
            
            html_len = len(html_plain)
            md_len = len(md_body)
            
            if html_len > 0:
                ratio = md_len / html_len
                if ratio < 0.3:
                    tip_issues.append(f"LOW content ratio: {ratio:.0%} (HTML={html_len}, MD={md_len})")
        
        # 4. Footer remnants
        tip_issues.extend(check_footer_remnants(md_text))
        
        # 5. HTML entities
        tip_issues.extend(check_html_entities(md_text))
        
        # 6. Frontmatter
        tip_issues.extend(check_frontmatter(md_text))
        
        # 7. Sections
        sections = check_sections(md_text)
        has_content = sections.get('Challenge') or sections.get('The Tip')
        if not has_content:
            tip_issues.append("NO content section found (neither Challenge nor The Tip)")
        
        has_tldr = sections.get('TL;DR')
        has_faq = sections.get('FAQ')
        
        # 8. Build report entry
        if tip_issues:
            issues_count += 1
            status = "⚠️"
        else:
            ok_count += 1
            status = "✅"
        
        mode = "structured" if sections.get('Challenge') else ("fallback" if sections.get('The Tip') else "unknown")
        video_str = "🎥" if extract_video_ids(md_text) else "—"
        tldr_str = "📝" if has_tldr else "—"
        faq_str = "🛠️" if has_faq else "—"
        
        report_lines.append(f"\n## {status} Tip {tip_num} – `{fname}`")
        report_lines.append(f"Mode: {mode} | Video: {video_str} | TL;DR: {tldr_str} | FAQ: {faq_str}")
        
        if tip_issues:
            for issue in tip_issues:
                report_lines.append(f"- ❌ {issue}")
        else:
            report_lines.append("- Alle Checks bestanden.")
    
    # Summary
    summary = f"\n---\n## Zusammenfassung\n- ✅ OK: {ok_count}\n- ⚠️ Probleme: {issues_count}\n- Total: {len(new_files)}\n"
    report_lines.insert(2, summary)
    
    report_path = os.path.join(BASE, "NEWOPTIMIZEDPOSTS", "VERIFICATION_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"Report saved: {report_path}")
    print(f"OK: {ok_count} | Issues: {issues_count} | Total: {len(new_files)}")

if __name__ == "__main__":
    main()
