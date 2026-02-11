"""
Audits all markdown files in _posts for any external image URLs.
Excludes local paths starting with /assets/ and the new canonical domain.
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    external_images = set()
    
    # regex for markdown images ![alt](url) and html images <img src="url">
    md_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    html_pattern = r'<img\s+[^>]*src=["\'](https?://[^"\']+)["\']'

    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        matches = re.findall(md_pattern, content)
        for m in matches:
            if "powerplatformtip.com" not in m and "/assets/" not in m:
                external_images.add(m)
        
        matches = re.findall(html_pattern, content)
        for m in matches:
            if "powerplatformtip.com" not in m and "/assets/" not in m:
                external_images.add(m)

    if not external_images:
        print("No other external image links found.")
        return

    print(f"Found {len(external_images)} unique external image links:")
    for link in sorted(external_images):
        print(link)

if __name__ == "__main__":
    main()
