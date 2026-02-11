"""
Final-final localization script.
Handles encoding/spaces in URLs more robustly.
"""
import os, re, glob, urllib.request, hashlib, urllib.parse

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")
IMAGES_ROOT = os.path.join(BASE, "assets", "images", "posts")

def get_local_path(url):
    # Unquote URL to handle encoding issues like %20
    unquoted_url = urllib.parse.unquote(url)
    
    # WordPress pattern
    wp_match = re.search(r'wp-content/uploads/(\d{4})/(\d{2})/(.+?)(?:[?#]|$)', unquoted_url)
    if wp_match:
        year, month, filename = wp_match.groups()
        rel_path = f"{year}/{month}/{filename}"
        full_path = os.path.join(IMAGES_ROOT, year, month, filename)
    else:
        # Generic external pattern
        ext = ".png"
        for e in [".jpg", ".jpeg", ".gif", ".webp", ".png"]:
            if e in unquoted_url.lower():
                ext = e
                break
        
        url_hash = hashlib.md5(url.encode()).hexdigest()
        filename = f"ext_{url_hash}{ext}"
        rel_path = f"external/{filename}"
        full_path = os.path.join(IMAGES_ROOT, "external", filename)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    if not os.path.exists(full_path):
        try:
            print(f"  Downloading: {url}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response, open(local_full_path := full_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"    SUCCESS -> {rel_path}")
        except Exception as e:
            # Try with legacy domain if it's a normalized one
            if "powerplatformtip.com/wp-content/uploads" in url:
                legacy_url = url.replace("powerplatformtip.com", "lehmannws.wordpress.com")
                try:
                    req = urllib.request.Request(legacy_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=10) as response, open(full_path, 'wb') as out_file:
                        out_file.write(response.read())
                    print(f"    SUCCESS -> {rel_path} (legacy)")
                except:
                    return None
            return None
                
    return f"/assets/images/posts/{rel_path}"

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        original_content = content
        
        # Find everything that looks like a URL in an image context
        # 1. Markdown ![alt](url)
        # 2. HTML <img src="url">
        # 3. YAML teaser: url
        
        urls = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
        urls += re.findall(r'<img\s+[^>]*src=["\'](https?://[^"\']+)["\']', content)
        urls += re.findall(r'teaser:\s*(https?://[^"\s\n]+)', content)
        
        for url in set(urls):
            if "/assets/" in url or "powerplatformtip.com/assets/" in url:
                continue
            
            local_path = get_local_path(url)
            if local_path:
                # Use escaped replacement to avoid issues with special characters in the URL
                content = content.replace(url, local_path)
                
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f"  Fixed: {os.path.basename(f)}")

if __name__ == "__main__":
    main()
