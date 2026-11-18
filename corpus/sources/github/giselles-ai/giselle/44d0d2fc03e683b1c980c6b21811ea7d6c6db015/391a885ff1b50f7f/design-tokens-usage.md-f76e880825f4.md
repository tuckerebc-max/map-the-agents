### Design tokens usage (required guide)

This is a minimal policy. New code must prefer semantic tokens and avoid raw colors.

### Load order
1) `internal-packages/ui/styles/tokens.css` (@theme primitives + compat tokens)
2) `internal-packages/ui/styles/semantic.css` (semantic → primitive mapping)
3) `internal-packages/ui/styles/scopes/*.css` (only when needed)
4) `internal-packages/ui/styles/aliases.css` (bridge; to be removed)

### Recommended utilities (v4-style)
- Text: `text-text`, `text-text/70`, `text-inverse`, `text-muted`
- Background: `bg-bg`, `bg-surface`, `bg-surface-muted`, `hover:bg-surface-hover`
- Border: `border-border`, `border-border-muted`, `border-border-focused`
- Focus: `ring-focused`, `outline-focused`
- SVG: `fill-text`, `stroke-border`
- Gradient: `from-brand-500`, `to-brand-700`

### Exceptions (during migration)
- Glass effects (backdrop-blur/translucency/shadows) may stay as-is to avoid visual drift
- If a 3rd-party requires raw colors, add tokens in `tokens.css` first

### Migration checklist (safe replacements)
- Do not add raw colors (hex/rgba/hsla/oklch); reduce existing
- `text-black-600/20 → text-text/20`
- `color-border-focused → ring-focused` (focus) / `border-border` (otherwise)
- `text-white-900 → text-inverse` (only when background is clearly dark)
- For SVG `#000/#fff`, use `currentColor` with parent `text-*`, or `fill-text`/`stroke-border`

See `docs/plan-v3-bridge-removal.md` for the staged removal plan.


