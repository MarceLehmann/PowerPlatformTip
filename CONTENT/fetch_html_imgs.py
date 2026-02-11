import urllib.request, re

url = "https://powerapps.microsoft.com/en-us/blog/return-an-array-from-a-sql-stored-procedure-to-powerapps-split-method/"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        # Find all img src tags
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
        for img in imgs:
            if "blob.core.windows.net" in img or "wp-content" in img or "media" in img or ".png" in img or ".jpg" in img:
                print(img)
except Exception as e:
    print(f"Error: {e}")
