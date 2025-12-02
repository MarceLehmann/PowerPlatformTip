# Giscus Setup Guide for PowerPlatformTip

## Overview

Giscus is a comments system powered by GitHub Discussions. It's lightweight, privacy-friendly, and perfect for technical blogs.

## Setup Instructions

### 1. Enable GitHub Discussions

1. Go to your repository: https://github.com/MarceLehmann/PowerPlatformTip
2. Click **Settings** tab
3. Scroll down to **Features** section
4. Check ✅ **Discussions**
5. Click **Set up discussions**

### 2. Configure Discussions Categories

Create these categories for better organization:

- **General** - General discussions (already exists)
- **Blog Comments** - For blog post comments (create this)
- **Q&A** - Questions and answers
- **Ideas** - Feature requests and ideas

### 3. Get Giscus Configuration

1. Visit https://giscus.app/
2. Fill in the configuration:

   **Repository:**
   ```
   MarceLehmann/PowerPlatformTip
   ```

   **Discussion Category:**
   - Choose "Blog Comments" (or "General")
   
   **Features:**
   - ✅ Enable reactions for the main post
   - ✅ Emit discussion metadata
   - ✅ Lazy load comments

   **Theme:**
   - Light: `light`
   - Dark: `dark` (or `preferred_color_scheme` for auto)

3. Copy the generated values:
   - `data-repo-id` → Copy this value
   - `data-category-id` → Copy this value

### 4. Update _config.yml

Replace the giscus section in `_config.yml`:

```yaml
comments:
  provider               : "giscus"
  giscus:
    repo_id              : "YOUR_REPO_ID_HERE"  # From giscus.app
    category_name        : "Blog Comments"       # Or "General"
    category_id          : "YOUR_CATEGORY_ID_HERE"  # From giscus.app
    discussion_term      : "pathname"
    reactions_enabled    : "1"
    theme                : "preferred_color_scheme"  # Auto dark/light mode
    strict               : "0"
    input_position       : "bottom"
    emit_metadata        : "0"
    lang                 : "en"
    lazy                 : true
```

### 5. Install Giscus App (Important!)

1. Visit https://github.com/apps/giscus
2. Click **Install**
3. Select **Only select repositories**
4. Choose `PowerPlatformTip`
5. Click **Install**

This gives Giscus permission to create discussions on your behalf.

### 6. Test Comments

1. Build and deploy your site
2. Visit any blog post
3. Scroll to the bottom
4. You should see the Giscus comments section
5. Try posting a test comment

## Features

### Automatic Features

✅ **Dark Mode Support** - Automatically switches with your site theme  
✅ **GitHub Login** - Readers authenticate with GitHub  
✅ **Reactions** - Emoji reactions on posts  
✅ **Markdown Support** - Full GitHub-flavored markdown  
✅ **Notifications** - Authors get notified of new comments  
✅ **Moderation** - Edit/delete through GitHub Discussions  

### Advanced Configuration

**Pathname Mapping:**
- Each post creates a unique discussion based on its URL
- Comments are tied to the post URL

**Lazy Loading:**
- Comments load only when user scrolls to them
- Improves page performance

**Metadata:**
- Discussion URLs are emitted for tracking
- Useful for analytics

## Dark Mode Integration

Our dark mode toggle automatically updates Giscus theme:

```javascript
// Add to dark-mode-toggle.html
function updateGiscusTheme(isDark) {
  const iframe = document.querySelector('iframe.giscus-frame');
  if (iframe) {
    const theme = isDark ? 'dark' : 'light';
    iframe.contentWindow.postMessage(
      { giscus: { setConfig: { theme } } },
      'https://giscus.app'
    );
  }
}
```

## Moderation

### How to Moderate Comments

1. Go to https://github.com/MarceLehmann/PowerPlatformTip/discussions
2. Find the discussion (named after post title)
3. You can:
   - Edit comments (as repo owner)
   - Delete spam
   - Lock discussions
   - Pin important discussions
   - Mark answers (for Q&A categories)

### Spam Protection

- Requires GitHub account (reduces spam significantly)
- You can lock/close discussions anytime
- Block users through GitHub settings
- Delete spam comments instantly

## Troubleshooting

### Comments Not Showing

**Check:**
1. Is Giscus app installed on the repo?
2. Are Discussions enabled?
3. Is `repo_id` and `category_id` correct?
4. Is the page deployed (doesn't work on localhost)?
5. Check browser console for errors

### Wrong Category

Edit in `_config.yml`:
```yaml
category_name: "Blog Comments"  # Must match exactly
```

### Theme Not Switching

Use `preferred_color_scheme` theme:
```yaml
theme: "preferred_color_scheme"
```

## Privacy & GDPR

### What Giscus Collects

- GitHub username (public)
- Comment content
- Timestamps
- IP address (GitHub servers, not stored by us)

### Privacy Policy Update

Add to your privacy policy:

> **Comments (Giscus)**
> 
> Our blog uses Giscus, a comments system powered by GitHub Discussions. When you comment:
> 
> - You authenticate with your GitHub account
> - Your GitHub username and avatar are displayed publicly
> - Comments are stored on GitHub's servers
> - GitHub's Privacy Policy applies: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
> 
> You can delete your comments anytime through GitHub Discussions.

## Customization

### Custom CSS for Dark Mode

Already included in `dark-mode-toggle.html`:

```css
.dark-mode .giscus,
.dark-mode .giscus-frame {
  color-scheme: dark;
}
```

### Hide Comments on Specific Posts

Add to post front matter:
```yaml
comments: false
```

## Analytics

### Track Comment Engagement

1. Enable metadata in `_config.yml`:
   ```yaml
   emit_metadata: "1"
   ```

2. Listen for events:
   ```javascript
   window.addEventListener('message', (event) => {
     if (event.origin !== 'https://giscus.app') return;
     // Track comment events
     console.log(event.data);
   });
   ```

## Benefits

✅ **Free & Open Source**  
✅ **No Database Required**  
✅ **GitHub Integration**  
✅ **Spam Protection**  
✅ **Markdown Support**  
✅ **Dark Mode Ready**  
✅ **Privacy Friendly**  
✅ **No Tracking**  

## Resources

- Giscus Website: https://giscus.app/
- Giscus GitHub: https://github.com/giscus/giscus
- Documentation: https://github.com/giscus/giscus/blob/main/ADVANCED-USAGE.md

---

**Next Steps:**
1. Enable Discussions on your repo
2. Get repo_id and category_id from giscus.app
3. Update _config.yml
4. Install Giscus app
5. Test on a blog post
6. Update privacy policy

**Status:** Ready to implement  
**Estimated Time:** 10 minutes
