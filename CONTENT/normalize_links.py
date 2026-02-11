"""
Normalize legacy links in _posts.
Replaces:
- lehmann.ws -> powerplatformtip.com
- lehmannws.wordpress.com -> powerplatformtip.com
- Removes /YYYY/MM/DD/ from WordPress style URLs if possible, 
  but the safest is just domain replacement and letting Jersy handle redirects if needed.
  However, Jekyll permalink is /:categories/:title/.
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")

def normalize_content(content):
    # 1. Replace domains
    content = content.replace("lehmann.ws", "powerplatformtip.com")
    content = content.replace("lehmannws.wordpress.com", "powerplatformtip.com")
    
    # 2. Cleanup double slashes (often happens after replacements)
    content = content.replace("https://powerplatformtip.com//", "https://powerplatformtip.com/")
    
    # 3. Optional: Try to convert WP date-links to Jekyll style
    # WP: https://powerplatformtip.com/2021/03/19/slug/
    # Target: https://powerplatformtip.com/Article/slug/ (typical category for tips is Article)
    # We'll just do a regex replace for the date pattern.
    content = re.sub(r'https?://powerplatformtip\.com/\d{4}/\d{2}/\d{2}/([^/\s\)]+)', r'https://powerplatformtip.com/Article/\1', content)
    
    return content

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    
    updated_count = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            original = fh.read()
            
        normalized = normalize_content(original)
        
        if normalized != original:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(normalized)
            updated_count += 1
            print(f"  Normalized links in: {os.path.basename(f)}")
            
    print(f"\nDone: {updated_count} files normalized.")

if __name__ == "__main__":
    main()
