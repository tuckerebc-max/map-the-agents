---
access: public
aliases: []
claim_ids:
- clm_56c607444c13efd343b0bad148f8bc59a3b2d415ff33771ad4336ba85174f0fb
- clm_84f50bcfa158291569bb36ecc49a79c45a363138c7f4c0be527e1a6b45424978
- clm_a6a5efcc5808fe6a36c25c6229123d0476708f62ab97bbaed7456427b64c46ee
maturity: draft
page_id: pg_7c5858da3174580aa479578fbcd0c2ee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_68cc8ede07735d0abfe372fbca986f46
title: alpbahadur/49-IDE/AGENTS.md @ c8bfb5c0a355
updated_at: '2026-09-14T03:34:09Z'
---

# alpbahadur/49-IDE/AGENTS.md @ c8bfb5c0a355

<!-- rcw:begin owner=source:src_68cc8ede07735d0abfe372fbca986f46 block=evidence -->
- Repository development practice: AGENTS.md documents a development-only multi-instance mode where each worktree runs its own stack, keyed by cloud URL, with per-instance database, config dir, ttyd port block, and tmux socket. [@claim:clm_56c607444c13efd343b0bad148f8bc59a3b2d415ff33771ad4336ba85174f0fb]
- Repository development practice: AGENTS.md mandates using the bd (beads) CLI for all issue tracking (bd ready/claim/close, --json flags, discovered-from links) and forbids markdown TODO lists or external trackers. [@claim:clm_84f50bcfa158291569bb36ecc49a79c45a363138c7f4c0be527e1a6b45424978]
- The product integrates Beads (steveyegge/beads) for interactive issue tables on the canvas; the agent runs via node agent/bin/49-agent.js and the cloud server via node cloud/src/index.js. [@claim:clm_a6a5efcc5808fe6a36c25c6229123d0476708f62ab97bbaed7456427b64c46ee]
<!-- rcw:end owner=source:src_68cc8ede07735d0abfe372fbca986f46 block=evidence -->

## Researcher notes

