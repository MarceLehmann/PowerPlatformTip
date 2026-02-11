"""
Targeted fix for the remaining Microsoft blog images in Tip 2022-05-23.
"""
import os, urllib.request, hashlib

BASE = r"c:\Users\marcel.lehmann\OneDrive - thepoweraddicts.ch\Projekte\PowerPlatformTip"
FILE = os.path.join(BASE, "_posts", "2022-05-23-return-an-array-from-powerautomate-to-powerapps-split-method.md")
IMAGES_ROOT = os.path.join(BASE, "assets", "images", "posts", "external")

URLS = [
    "https://acomblogimages.blob.core.windows.net/media/PowerApps/Audrie/blog%20-%20stored%20proc%207.png",
    "https://acomblogimages.blob.core.windows.net/media/PowerApps/Audrie/blog%20-%20stored%20proc%204.png",
    "https://acomblogimages.blob.core.windows.net/media/PowerApps/Audrie/blog%20-%20stored%20proc%205.png"
]

def main():
    os.makedirs(IMAGES_ROOT, exist_ok=True)
    
    with open(FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for url in URLS:
        url_hash = hashlib.md5(url.encode()).hexdigest()
        filename = f"msblob_{url_hash}.png"
        local_full = os.path.join(IMAGES_ROOT, filename)
        local_rel = f"/assets/images/posts/external/{filename}"
        
        try:
            print(f"Downloading: {url}")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                with open(local_full, 'wb') as out:
                    out.write(resp.read())
            
            content = content.replace(url, local_rel)
            print(f"  Replaced in file: {url} -> {local_rel}")
        except Exception as e:
            print(f"  Failed: {e}")

    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
