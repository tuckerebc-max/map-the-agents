## Data scope (preparation for Tailwind v4)

This document introduces the minimal guide and a file scaffold for future `data-scope` based styling. This PR does not apply scopes yet.

### Purpose
- Prepare isolated styling scopes (e.g., dark sections, embedded widgets) without global side effects.

### Minimal scaffold
Create a scope file and wrap target areas with a `data-scope` attribute later.

```css
/* styles/scope/example-scope.css */
@layer utilities {
  [data-scope="example"] {
    /* put scope-specific semantic mappings here */
  }
}
```

### Usage (later)
- Wrap a section: `<section data-scope="example">...` and rely on scoped semantic rules.

Notes: This is a scaffold only; no runtime impact in this PR.

