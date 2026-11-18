## Semantic tokens (Phase 1.5 scaffold)

Minimal usage guide for semantic utilities. These map to primitives via `internal-packages/ui/styles/semantic.css` (scaffold). Not applied globally yet.

- Text
  - `text-text`: Regular content text
  - `text-inverse`: High-contrast text on dark surfaces
- Focus / Ring
  - `ring-focused`: Tailwind v3 ring color hook for the focused color token
  - `outline-focused`: Outline color mapped to the focused token

Notes
- Keep using the v3 bridge in `aliases.css`. Add minimal aliases only when needed during migration.
- Avoid raw colors; prefer tokens and semantic utilities.

