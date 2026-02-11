"""
Replace legacy _posts with optimized versions from NEWOPTIMIZEDPOSTS.
Matching is done via Tip Number (e.g. powerplatformtip-129).
"""
import os, re, glob, shutil

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
NEW_DIR = os.path.join(BASE, "NEWOPTIMIZEDPOSTS")
POSTS_DIR = os.path.join(BASE, "_posts")

def get_tip_num(filename):
    m = re.search(r'powerplatformtip-(\d+)', filename)
    return m.group(1) if m else None

def main():
    new_files = glob.glob(os.path.join(NEW_DIR, "*.md"))
    new_files = [f for f in new_files if "VERIFICATION" not in os.path.basename(f)]
    
    posts_files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    
    # Create map for current posts
    posts_map = {}
    for pf in posts_files:
        num = get_tip_num(os.path.basename(pf))
        if num:
            posts_map[num] = pf

    replaced = 0
    errors = []
    
    for nf in new_files:
        fname = os.path.basename(nf)
        num = get_tip_num(fname)
        
        if not num:
            continue
            
        if num in posts_map:
            target = posts_map[num]
            try:
                # Copy optimized content to the existing filename in _posts
                # Using shutil.copy2 to preserve metadata if possible
                shutil.copy2(nf, target)
                replaced += 1
                print(f"  Replaced Tip {num}: {os.path.basename(target)}")
            except Exception as e:
                errors.append(f"Tip {num}: {str(e)}")
        else:
            # If it's a new tip or the naming pattern in _posts is totally different
            # we might want to copy it as a new file, but for now let's just log it.
            print(f"  Tip {num} not found in _posts. Skipping replacement.")

    print(f"\nDone: {replaced} replaced, {len(errors)} errors.")

if __name__ == "__main__":
    main()
