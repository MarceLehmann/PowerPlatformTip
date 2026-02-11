"""
Localize images from WordPress uploads to local assets.
1. Downloads images from https://powerplatformtip.com/wp-content/uploads/...
2. Saves them locally in assets/images/posts/YYYY/MM/...
3. Updates all markdown files in _posts to use local paths.
"""
import os, re, glob, urllib.request

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
POSTS_DIR = os.path.join(BASE, "_posts")
IMAGES_ROOT = os.path.join(BASE, "assets", "images", "posts")

def download_image(url):
    """Download image and return local relative path."""
    # Pattern: https://powerplatformtip.com/wp-content/uploads/2023/01/img1.png
    match = re.search(r'wp-content/uploads/(\d{4})/(\d{2})/(.+)$', url)
    if not match:
        return None
    
    year, month, filename = match.groups()
    local_rel_path = f"{year}/{month}/{filename}"
    local_full_path = os.path.join(IMAGES_ROOT, year, month, filename)
    
    # Create directory
    os.makedirs(os.path.dirname(local_full_path), exist_ok=True)
    
    # Download if not exists
    if not os.path.exists(local_full_path):
        try:
            print(f"  Downloading: {url} -> {local_rel_path}")
            urllib.request.urlretrieve(url, local_full_path)
        except Exception as e:
            print(f"  ERROR downloading {url}: {e}")
            return None
            
    return f"/assets/images/posts/{local_rel_path}"

def main():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    
    updated_files_count = 0
    total_images_localized = 0
    
    # Patterns to match
    patterns = [
        r'(https?://[^)\s\n]+wp-content/uploads/[^)\s\n]+)'
    ]

    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
            
        original_content = content
        
        # Find all URLs
        urls = set()
        for p in patterns:
            matches = re.findall(p, content)
            urls.update(matches)
            
        for url in urls:
            local_path = download_image(url)
            if local_path:
                content = content.replace(url, local_path)
                total_images_localized += 1
                
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(content)
            updated_files_count += 1
            print(f"  Updated links in: {os.path.basename(f)}")
            
    print(f"\nDone: {updated_files_count} files updated, {total_images_localized} images handled.")

if __name__ == "__main__":
    main()
