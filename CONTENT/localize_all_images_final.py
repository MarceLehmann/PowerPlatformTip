"""
Final localization script for ALL external images.
1. Searches for any http(s) image links that aren't local /assets/.
2. Handles both WordPress uploads and generic external images.
3. Saves WordPress images to assets/images/posts/YYYY/MM/...
4. Saves other external images to assets/images/posts/external/ [hash-of-url].
5. Updates all markdown files in _posts to use local paths.
"""
import os, re, glob, urllib.request, hashlib

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")
IMAGES_ROOT = os.path.join(BASE, "assets", "images", "posts")

def get_local_path(url):
    """Determine local path and download if necessary."""
    # WordPress pattern
    wp_match = re.search(r'wp-content/uploads/(\d{4})/(\d{2})/(.+?)(?:[?#]|$)', url)
    if wp_match:
        year, month, filename = wp_match.groups()
        # Cleanup filename from query params
        filename = filename.split('?')[0].split('#')[0]
        rel_path = f"{year}/{month}/{filename}"
        full_path = os.path.join(IMAGES_ROOT, year, month, filename)
    else:
        # Generic external pattern
        # Use MD5 hash of URL to avoid filename collisions and long paths
        ext = ".png" # default
        if ".jpg" in url.lower() or ".jpeg" in url.lower(): ext = ".jpg"
        elif ".gif" in url.lower(): ext = ".gif"
        elif ".webp" in url.lower(): ext = ".webp"
        
        url_hash = hashlib.md5(url.encode()).hexdigest()
        filename = f"ext_{url_hash}{ext}"
        rel_path = f"external/{filename}"
        full_path = os.path.join(IMAGES_ROOT, "external", filename)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    if not os.path.exists(full_path):
        try:
            print(f"  Downloading: {url}")
            # Try original URL first
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response, open(full_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"    SUCCESS -> {rel_path}")
        except Exception as e:
            # If it failed and looks like a normalized WP URL, try legacy domain
            if "powerplatformtip.com/wp-content/uploads" in url:
                legacy_url = url.replace("powerplatformtip.com", "lehmannws.wordpress.com")
                try:
                    print(f"    Retrying with legacy: {legacy_url}")
                    req = urllib.request.Request(legacy_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=10) as response, open(full_path, 'wb') as out_file:
                        out_file.write(response.read())
                    print(f"    SUCCESS -> {rel_path} (via legacy)")
                except Exception as e2:
                    print(f"    FAILED: {e2}")
                    return None
            else:
                print(f"    FAILED: {e}")
                return None
                
    return f"/assets/images/posts/{rel_path}"

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    
    total_files_updated = 0
    total_images_localized = 0
    
    # Generic regex for markdown and html images
    md_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    html_pattern = r'<img\s+[^>]*src=["\'](https?://[^"\']+)["\']'
    teaser_pattern = r'teaser:\s*(https?://[^"\s\n]+)'

    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        original_content = content
        
        urls = set()
        urls.update(re.findall(md_pattern, content))
        urls.update(re.findall(html_pattern, content))
        urls.update(re.findall(teaser_pattern, content))
        
        for url in urls:
            # Skip local or already handled
            if "/assets/" in url or url.startswith("/") or url.startswith("."):
                continue
            
            local_path = get_local_path(url)
            if local_path:
                content = content.replace(url, local_path)
                total_images_localized += 1
                
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(content)
            total_files_updated += 1
            print(f"  Processed: {os.path.basename(f)}")
            
    print(f"\nSummary: {total_files_updated} files updated, {total_images_localized} image instances localized.")

if __name__ == "__main__":
    main()
