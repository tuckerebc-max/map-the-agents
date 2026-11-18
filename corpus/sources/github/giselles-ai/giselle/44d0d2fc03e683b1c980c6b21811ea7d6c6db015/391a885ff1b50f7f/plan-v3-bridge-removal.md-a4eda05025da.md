### Plan: Staged removal of v3 bridge (aliases and compat tokens)

Scope
- Targets: `internal-packages/ui/styles/aliases.css` (compat utilities) and temporary compat tokens in `tokens.css` (e.g., --color-white-900, --color-black-600)
- Non-goal: semantic/scopes themselves are not removed

Milestones
1) Freeze new usage
   - CI guard: fail on newly introduced alias utilities and compat tokens outside tokens.css
   - Docs: new code MUST use semantic utilities (text-text, bg-surface, border-border, ring-focused)
2) Reduce usage to zero
   - Run codemod safe-pass (batch) and follow-ups for ambiguous spots
   - Visual checks for glass areas; skip where visual parity risks exist
3) Promote guards to error
   - stylelint/eslint: warn → error for raw colors and alias utilities
4) Remove bridge
   - Delete `aliases.css`
   - Remove compat tokens from `tokens.css`
   - Update docs and PR template

Acceptance
- repo-wide usage of alias utilities = 0
- repo-wide usage of compat tokens (outside tokens.css) = 0
- CI: increase-fail enabled and passing

Risks / Mitigation
- Visual drift in glass areas → keep excluded; handle in dedicated PRs
- Third-party components with hardcoded colors → wrap via semantic classes or add minimal tokens

Timeline
- Week N: freeze + codemod pass 1 (safe)
- Week N+1: manual fixes + codemod pass 2
- Week N+2: promote guards to error + remove bridge
