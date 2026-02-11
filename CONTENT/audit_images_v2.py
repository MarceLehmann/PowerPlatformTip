"""
Audits all markdown files in _posts for image URLs pointing to WordPress uploads.
Replaces legacy domains with the target pattern and collects unique URLs.
"""
import os, re, glob

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    image_links = set()
    
    # regex for markdown images ![alt](url) and html images <img src="url">
    # looking for wp-content/uploads in any domain or relative path
    patterns = [
        r'!\[.*?\]\((https?://[^)]+wp-content/uploads/[^)]+)\)',
        r'<img\s+[^>]*src=["\'](https?://[^"\']+wp-content/uploads/[^"\']+)["\']',
        r'teaser:\s*(https?://[^"\s\n]+wp-content/uploads/[^"\s\n]+)'
    ]

    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        for pattern in patterns:
            matches = re.findall(pattern, content)
            image_links.update(matches)

    if not image_links:
        print("No WordPress image links found.")
        return

    print(f"Found {len(image_links)} unique WordPress image links.")
    # Sort these for orderly downloading
    for link in sorted(image_links):
        print(link)

if __name__ == "__main__":
    main()
