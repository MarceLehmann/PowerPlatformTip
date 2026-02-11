"""
Localize images from WordPress uploads to local assets.
Correctly targets the legacy WordPress domain to fetch images.
1. Searches for images with 'wp-content/uploads' in their path.
2. Tries to download from lehmannws.wordpress.com.
3. Saves to assets/images/posts/YYYY/MM/...
4. Updates all markdown files in _posts to use local paths.
"""
import os, re, glob, urllib.request

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")
IMAGES_ROOT = os.path.join(BASE, "assets", "images", "posts")

# Try these domains for fetching
SOURCE_DOMAINS = [
    "lehmannws.wordpress.com",
    "lehmann.ws"
]

def download_image(original_url):
    """Download image from legacy source and return local relative path."""
    # The URL might already be normalized to powerplatformtip.com or still be lehmann.ws
    match = re.search(r'wp-content/uploads/(\d{4})/(\d{2})/(.+)$', original_url)
    if not match:
        return None
    
    year, month, filename = match.groups()
    # Strip potential markdown resizing/alignment at the end of the filename if captured
    filename = filename.split(')')[0].split('"')[0].split("'")[0]
    
    local_rel_path = f"{year}/{month}/{filename}"
    local_full_path = os.path.join(IMAGES_ROOT, year, month, filename)
    
    # Create directory
    os.makedirs(os.path.dirname(local_full_path), exist_ok=True)
    
    # Try downloading from source domains
    success = False
    if not os.path.exists(local_full_path):
        for domain in SOURCE_DOMAINS:
            try:
                # Construct target download URL
                download_url = f"https://{domain}/wp-content/uploads/{year}/{month}/{filename}"
                print(f"  Attempting: {download_url}")
                
                # Use a User-Agent to avoid being blocked
                req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(local_full_path, 'wb') as out_file:
                    out_file.write(response.read())
                
                print(f"    SUCCESS: Saved to {local_rel_path}")
                success = True
                break
            except Exception as e:
                print(f"    Failed for {domain}: {e}")
    else:
        success = True # Already exists
            
    return f"/assets/images/posts/{local_rel_path}" if success else None

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    
    updated_files_count = 0
    total_images_handled = 0
    
    # Pattern to find any URL with wp-content/uploads
    url_pattern = r'(https?://[^)\s\n"\']+wp-content/uploads/[^)\s\n"\']+)'

    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        original_content = content
        urls = re.findall(url_pattern, content)
        unique_urls = set(urls)
        
        for url in unique_urls:
            local_path = download_image(url)
            if local_path:
                content = content.replace(url, local_path)
                total_images_handled += 1
                
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(content)
            updated_files_count += 1
            print(f"  Updated images in: {os.path.basename(f)}")
            
    print(f"\nSummary: {updated_files_count} files updated, {total_images_handled} image instances localized.")

if __name__ == "__main__":
    main()
