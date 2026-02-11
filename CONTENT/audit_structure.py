"""
Structural compliance audit: Check which NEWOPTIMIZEDPOSTS files
follow the required header structure and which deviate.
"""
import os, re, glob

NEW_DIR = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip\NEWOPTIMIZEDPOSTS"

REQUIRED_SECTIONS = [
    ("📝 TL;DR", True),       # optional per user's latest rules
    ("💡 Challenge", True),    # REQUIRED
    ("✅ Solution", True),     # REQUIRED  
    ("🔧 How", True),          # REQUIRED (How It's Done / How it's done)
    ("🎉 Result", True),       # REQUIRED
    ("🌟 Key Advantages", True), # REQUIRED
    ("🛠️ FAQ", True),          # REQUIRED
]

BAD_SECTIONS = ["💡 The Tip"]  # Fallback header - should not exist

def audit_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip frontmatter
    body = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    
    results = {}
    for label, _ in REQUIRED_SECTIONS:
        results[label] = bool(re.search(r'##\s*' + re.escape(label), body))
    
    issues = []
    for bad in BAD_SECTIONS:
        if re.search(r'##\s*' + re.escape(bad), body):
            issues.append(f"Has non-standard section: '{bad}'")
    
    missing = [label for label, req in REQUIRED_SECTIONS if req and not results.get(label)]
    
    return results, missing, issues

def main():
    files = sorted(glob.glob(os.path.join(NEW_DIR, "*.md")))
    files = [f for f in files if "VERIFICATION" not in os.path.basename(f)]
    
    compliant = []
    non_compliant = []
    
    for f in files:
        fname = os.path.basename(f)
        results, missing, issues = audit_file(f)
        
        tip_match = re.search(r'powerplatformtip-(\d+)', fname)
        tip_num = tip_match.group(1) if tip_match else "?"
        
        if not missing and not issues:
            compliant.append(tip_num)
        else:
            non_compliant.append({
                'tip': tip_num,
                'file': fname,
                'missing': missing,
                'issues': issues,
                'has': [k for k, v in results.items() if v]
            })
    
    print(f"=== STRUCTURAL COMPLIANCE AUDIT ===")
    print(f"Compliant: {len(compliant)}")
    print(f"Non-compliant: {len(non_compliant)}")
    print()
    
    # Group non-compliant by issue type
    has_fallback = [t for t in non_compliant if any("The Tip" in i for i in t['issues'])]
    missing_sections = [t for t in non_compliant if t['missing'] and t not in has_fallback]
    
    print(f"--- Uses 'The Tip' fallback ({len(has_fallback)}) ---")
    for t in has_fallback:
        print(f"  Tip {t['tip']}: missing {t['missing']}")
    
    print(f"\n--- Missing sections but no fallback ({len(missing_sections)}) ---")
    for t in missing_sections:
        print(f"  Tip {t['tip']}: missing {t['missing']}, has {t['has']}")
    
    print(f"\n--- Compliant ({len(compliant)}) ---")
    print(f"  Tips: {', '.join(compliant)}")

if __name__ == "__main__":
    main()
