### Design tokens and scopes (developer guide)

This guide outlines the minimal, safe rules for introducing color design tokens and using scopes. Replace incrementally with no visual changes.

### Layers and files

- tokens: `internal-packages/ui/styles/tokens.css`
  - Define primitives with Tailwind v4 `@theme` (gray/brand/status, etc.) and temporary compat tokens (e.g., white-900)
- semantic: `internal-packages/ui/styles/semantic.css`
  - Map semantic tokens (text/bg/border/focused, etc.) to primitives (light defaults)
- aliases (bridge): `internal-packages/ui/styles/aliases.css`
  - Thin v3-compat utilities for migration. To be removed later
- scopes: `internal-packages/ui/styles/scopes/*.css`
  - Optional overrides per `:root[data-scope="stage"|"settings-apps"|"workspaces"]`

Load order (example)
1) tokens → 2) semantic → 3) scopes (when needed) → 4) aliases

### What to use (v4-style naming)

- Text: `text-text`, `text-text/70`, `text-inverse`, `text-muted`
- Background/surface: `bg-bg`, `bg-surface`, `bg-surface-muted`
- Border: `border-border`, `border-border-muted`, `border-border-focused`
- Focus: `ring-focused`, `outline-focused`
- SVG: `fill-text`, `stroke-border`
- Gradients: `from-brand-500`, `to-brand-700`

Prefer `/20` `/40` `/60` `/70` `/80` for opacity (equivalent to color-mix).

### Scopes

- Attach `data-scope="stage"` (etc.) to root; override semantic tokens in `scopes/*.css`.
- Example: `:root[data-scope="stage"] { --color-brand-500: ...; --color-text: ...; }`

### Migration policy

- Prioritize “no visual change” (exclude glass areas)
- Start with safe replacements, e.g.:
  - `text-black-600/20 → text-text/20`
  - `color-border-focused → ring-focused` (in focus context) / `border-border` (otherwise)
  - `text-white-900 → text-inverse` (only when dark background is explicit)
- Phase out compat utilities/tokens: no new usage; reduce existing

### Lint/CI

- Disallow raw colors (hex/rgba/hsla/oklch) except in `tokens.css`
- Phase out direct Tailwind scales (e.g., `text-white-900`)
- CI runs non-blocking reports (increase-fail will be added later)

### Codemods (safe-pass)

- Dry-run: `pnpm codemod:safe-pass-1`
- Apply: `pnpm codemod:safe-pass-1:apply`
- Only minimal safe set; ambiguous cases are skipped and reported

### Notes

- In v3, a bridge utility allows early adoption of new naming; in v4, `@theme` resolves directly
- Eventually remove `aliases.css` and compat tokens; converge on primitives + semantics + scopes


