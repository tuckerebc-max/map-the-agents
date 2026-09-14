---
access: public
aliases: []
claim_ids:
- clm_2ba14b166d28f5a00d26af2ceef2efe4ff1a2a37afed8f5951009e7b5e50f760
- clm_8947b8ae6060580fcb721a23c2b3096d92c301c22542e1f9f59c66e268e0cf3e
maturity: draft
page_id: pg_c4a25c1d74d5588facc4ea96a88fa204
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_35567bae24cc5af0ad133d7616335a0b
title: roberto-mello/lavra/site/src/content/docs/AUTONOMOUS_EXECUTION.md @ 2e7e512eb90b
updated_at: '2026-09-14T04:18:53Z'
---

# roberto-mello/lavra/site/src/content/docs/AUTONOMOUS_EXECUTION.md @ 2e7e512eb90b

<!-- rcw:begin owner=source:src_35567bae24cc5af0ad133d7616335a0b block=evidence -->
- The docs acknowledge autonomous-mode trade-offs: bash runs without review, file writes are unapproved with only advisory ownership enforcement, and there is no human checkpoint; mitigations include feature branches, low retry budgets, and worktree/container isolation. [@claim:clm_2ba14b166d28f5a00d26af2ceef2efe4ff1a2a37afed8f5951009e7b5e50f760]
- For autonomous modes (/lavra-work-ralph, /lavra-work-teams), the docs recommend a granular allow list in .claude/settings.json (git, bd, test runners, Read/Write/Edit/Grep/Glob) rather than --dangerously-skip-permissions, which bypasses all approval prompts globally. [@claim:clm_8947b8ae6060580fcb721a23c2b3096d92c301c22542e1f9f59c66e268e0cf3e]
<!-- rcw:end owner=source:src_35567bae24cc5af0ad133d7616335a0b block=evidence -->

## Researcher notes

