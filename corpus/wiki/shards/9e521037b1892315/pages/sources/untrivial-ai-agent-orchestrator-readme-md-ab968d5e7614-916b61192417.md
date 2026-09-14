---
access: public
aliases: []
claim_ids:
- clm_0f5e16ef79b24897be70caca500bbb08f107c45fd3d8d64dab462de53bc615c8
- clm_3ed626fe47f66e8f81668920ffa6602fe8f4c36ff6363abc00e07b4cbfa00908
- clm_3ef25d32d49392879a2fbfbe85a600b49a5b46dc188d9ed015fe8b58a73fafba
- clm_f870a9b0d41c80f59633913f4d9addaf93b11e1bece277f4f9a4d090540a1fcd
maturity: draft
page_id: pg_9d7a2ea9ff0152ba8471916b61192417
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_441e7576210f5250ae415a9c53def15f
title: Untrivial-ai/agent-orchestrator/README.md @ ab968d5e7614
updated_at: '2026-09-14T03:21:42Z'
---

# Untrivial-ai/agent-orchestrator/README.md @ ab968d5e7614

<!-- rcw:begin owner=source:src_441e7576210f5250ae415a9c53def15f block=evidence -->
- The orchestrator keeps a project-scoped conversation preserving goals, decisions, and constraints, and combines it with repository context and live AO state like active workers, PRs, CI, and reviews. [@claim:clm_0f5e16ef79b24897be70caca500bbb08f107c45fd3d8d64dab462de53bc615c8]
- Git-backed workers each get their own branch and worktree, while Scratch workers get AO-managed branchless directories, to keep parallel work isolated. [@claim:clm_3ed626fe47f66e8f81668920ffa6602fe8f4c36ff6363abc00e07b4cbfa00908]
- The product advertises support for 27 coding agents through one supervised workflow, with named examples including Claude Code, Codex, Cursor, Aider, and GitHub Copilot. [@claim:clm_3ef25d32d49392879a2fbfbe85a600b49a5b46dc188d9ed015fe8b58a73fafba]
- A project orchestrator agent handles planning and delegation: it breaks plans into tasks, spawns or redirects workers, passes context, and tracks progress, while workers own implementation and PRs. [@claim:clm_f870a9b0d41c80f59633913f4d9addaf93b11e1bece277f4f9a4d090540a1fcd]
<!-- rcw:end owner=source:src_441e7576210f5250ae415a9c53def15f block=evidence -->

## Researcher notes

