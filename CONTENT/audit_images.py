"""
Audits all markdown files in _posts for image URLs pointing to legacy domains.
Outputs a list of unique image URLs and their target local paths.
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")
LEGACY_DOMAINS = ["lehmann.ws", "lehmannws.wordpress.com"]

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    image_links = set()
    
    # regex for markdown images ![alt](url) and html images <img src="url">
    # focusing on legacy domains
    md_pattern = r'!\[.*?\]\((https?://(?:' + '|'.join(re.escape(d) for d in LEGACY_DOMAINS) + r')[^)]+)\)'
    html_pattern = r'<img\s+[^>]*src=["\'](https?://(?:' + '|'.join(re.escape(d) for d in LEGACY_DOMAINS) + r')[^"\']+)["\']'

    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        matches = re.findall(md_pattern, content)
        image_links.update(matches)
        
        matches = re.findall(html_pattern, content)
        image_links.update(matches)

    if not image_links:
        print("No legacy image links found.")
        return

    print(f"Found {len(image_links)} unique legacy image links:")
    for link in sorted(image_links):
        print(link)

if __name__ == "__main__":
    main()
