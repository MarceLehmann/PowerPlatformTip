# CSS Architecture Documentation

## Overview

The CSS architecture for PowerPlatformTip.com follows a modular, component-based approach with BEM-style naming conventions.

## Structure

```
assets/css/
├── main-components.css          # Main entry point (imports all)
├── _variables.css               # Design tokens & CSS variables
├── custom-components.css        # Legacy combined file (deprecated)
├── performance.css              # Performance optimizations
├── mobile-navigation.css        # Mobile nav styles
├── components/                  # Individual component styles
│   ├── author-bio.css
│   ├── mvp-badge.css
│   ├── newsletter-popup.css
│   ├── newsletter-bar.css
│   ├── after-content-cta.css
│   ├── cookie-consent.css
│   ├── footer-services.css
│   ├── breadcrumbs.css
│   ├── related-posts.css
│   ├── code-blocks.css
│   └── dark-mode-toggle.css
├── utilities/                   # Utility classes
│   ├── animations.css
│   ├── helpers.css
│   └── accessibility.css
└── dist/                        # Build output
    ├── main-components.min.css
    └── main-components.min.css.map
```

## Design Tokens (CSS Variables)

All design tokens are defined in `_variables.css`:

### Colors
```css
--primary-color: #7c4dff
--background-color: #ffffff
--text-color: #333333
```

### Typography
```css
--font-family-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", ...
--font-size-base: 16px
--line-height-base: 1.6
```

### Spacing (8px scale)
```css
--spacing-xs: 0.25rem  /* 4px */
--spacing-sm: 0.5rem   /* 8px */
--spacing-md: 1rem     /* 16px */
--spacing-lg: 1.5rem   /* 24px */
--spacing-xl: 2rem     /* 32px */
```

### Transitions
```css
--transition-fast: 150ms
--transition-base: 250ms
--transition-colors: color 250ms ease-in-out, ...
```

## BEM Naming Convention

We use a BEM-inspired naming convention:

```css
/* Block */
.newsletter-popup { }

/* Element */
.newsletter-popup__header { }
.newsletter-popup__content { }
.newsletter-popup__close { }

/* Modifier */
.newsletter-popup--sticky { }
.newsletter-popup__button--primary { }
```

### Examples

**Author Bio Component:**
```css
.author-bio { }
.author-bio__container { }
.author-bio__photo { }
.author-bio__content { }
.author-bio__actions { }
.author-bio__button--primary { }
```

**Newsletter Popup:**
```css
.newsletter-popup { }
.newsletter-popup--visible { }
.newsletter-popup__overlay { }
.newsletter-popup__modal { }
.newsletter-popup__header { }
.newsletter-popup__close { }
```

## Component Structure

Each component CSS file follows this structure:

```css
/* ============================================
   COMPONENT NAME
   ============================================
   
   Brief description of component
   
   Usage:
   {% include component-name.html %}
   ============================================ */

/* Base styles */
.component { }

/* Elements */
.component__element { }

/* Modifiers */
.component--modifier { }

/* States */
.component.is-active { }
.component.is-loading { }

/* Responsive */
@media (max-width: 768px) { }

/* Dark mode */
.dark-mode .component { }

/* Print */
@media print { }
```

## Responsive Breakpoints

```css
--breakpoint-xs: 480px   /* Mobile */
--breakpoint-sm: 768px   /* Tablet */
--breakpoint-md: 1024px  /* Desktop */
--breakpoint-lg: 1280px  /* Large Desktop */
--breakpoint-xl: 1536px  /* Extra Large */
```

**Usage:**
```css
/* Mobile first approach */
.component {
  /* Mobile styles (default) */
}

@media (min-width: 768px) {
  .component {
    /* Tablet and up */
  }
}

@media (min-width: 1024px) {
  .component {
    /* Desktop and up */
  }
}
```

## Dark Mode Support

All components support dark mode via `.dark-mode` class:

```css
/* Light mode (default) */
.component {
  background: var(--background-color);
  color: var(--text-color);
}

/* Dark mode */
.dark-mode .component {
  background: var(--background-color); /* Auto-updated */
  color: var(--text-color); /* Auto-updated */
}
```

## Build Process

### Development

During development, use individual CSS files:

```html
<link rel="stylesheet" href="/assets/css/custom-components.css">
<link rel="stylesheet" href="/assets/css/mobile-navigation.css">
```

### Production

For production, build minified version:

```bash
npm run build:css
```

This creates:
- `assets/css/dist/main-components.min.css`
- `assets/css/dist/main-components.min.css.map`

Then update `_includes/head/custom.html`:

```html
<link rel="stylesheet" href="/assets/css/dist/main-components.min.css">
```

### Build Script

The build script (`build-css.js`):
1. Combines all modular CSS files
2. Minifies with clean-css
3. Generates source maps
4. Optimizes for production
5. Reports file size savings

## Component Guidelines

### Creating New Components

1. **Create component file:**
   ```
   assets/css/components/my-component.css
   ```

2. **Follow structure:**
   ```css
   /* Header comment */
   .my-component { }
   .my-component__element { }
   .my-component--modifier { }
   
   /* Responsive */
   @media (max-width: 768px) { }
   
   /* Dark mode */
   .dark-mode .my-component { }
   ```

3. **Use design tokens:**
   ```css
   .my-component {
     padding: var(--spacing-lg);
     color: var(--text-color);
     transition: var(--transition-colors);
   }
   ```

4. **Add to build:**
   - Add to `cssFiles` array in `build-css.js`
   - Import in `main-components.css`

5. **Test:**
   - Light mode
   - Dark mode
   - Mobile responsive
   - Print styles
   - Accessibility (keyboard, screen readers)

### Best Practices

**DO:**
- ✅ Use CSS variables for all values
- ✅ Follow BEM naming
- ✅ Support dark mode
- ✅ Make responsive (mobile-first)
- ✅ Add print styles
- ✅ Include accessibility features
- ✅ Use semantic HTML
- ✅ Optimize performance (contain, will-change)

**DON'T:**
- ❌ Use hard-coded colors
- ❌ Use `!important` (except for utilities)
- ❌ Use IDs for styling
- ❌ Over-nest selectors (max 3 levels)
- ❌ Use browser-specific prefixes (use autoprefixer)
- ❌ Forget dark mode support
- ❌ Ignore mobile users

## Performance

### Critical CSS

Critical above-the-fold CSS is inlined in `<head>`:

```css
/* Critical styles for LCP */
.masthead { }
.page__hero { }
.page__title { }
```

### Non-Critical CSS

All other CSS is loaded with `<link>` and can be deferred:

```html
<link rel="stylesheet" href="/assets/css/main-components.css" media="print" onload="this.media='all'">
```

### CSS Containment

Use `contain` property for performance:

```css
.component {
  contain: layout style paint;
}
```

### GPU Acceleration

Use `transform` and `will-change` for animations:

```css
.animated-element {
  transform: translateZ(0); /* GPU layer */
  will-change: transform;
}
```

## Accessibility

### Focus Styles

All interactive elements have visible focus:

```css
.component:focus {
  outline: 2px solid var(--primary-color);
  outline-offset: 4px;
}
```

### Reduced Motion

Support `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  .animated-element {
    animation: none;
    transition: none;
  }
}
```

### High Contrast

Support `prefers-contrast: high`:

```css
@media (prefers-contrast: high) {
  .component {
    border: 2px solid currentColor;
  }
}
```

### Screen Readers

Use `.visually-hidden` utility:

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## Maintenance

### Updating Components

1. Edit component file in `assets/css/components/`
2. Test locally
3. Run build: `npm run build:css`
4. Commit changes

### Refactoring

When refactoring:
1. Update component file
2. Keep BEM naming consistent
3. Update documentation
4. Test all breakpoints
5. Test dark mode
6. Run build

### Deprecation

To deprecate old CSS:
1. Mark with comment: `/* DEPRECATED: Use .new-class instead */`
2. Leave for 2 versions
3. Remove in next major version

## Migration from Legacy

The old `custom-components.css` file is deprecated. Migration plan:

**Phase 1 (Current):**
- ✅ New modular structure created
- ✅ Build system set up
- ⏳ Both versions coexist

**Phase 2 (Next):**
- Extract all components from `custom-components.css`
- Test thoroughly
- Switch to modular imports

**Phase 3 (Future):**
- Remove `custom-components.css`
- Use only `main-components.min.css`

## Resources

- [BEM Naming Convention](http://getbem.com/)
- [CSS Variables (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [CSS Containment (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Containment)
- [Web Performance (web.dev)](https://web.dev/performance/)
- [WCAG Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

## Questions?

For questions or suggestions, contact:
- Marcel Lehmann
- www.powerplatformtip.com
- GitHub: MarceLehmann/PowerPlatformTip
