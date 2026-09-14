---
access: public
aliases: []
claim_ids:
- clm_2387c9da7ef7a5914910e8d0c01e00943c2cbc4a3aa2ae4493cf9949d38d593a
- clm_d2ca4f0502aeaff82bcc5cbed1c85b86a3ce0b5b710717b7df24e017e49142c7
maturity: draft
page_id: pg_4074c402fda15b8e9070987d653e02ce
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8228fcd4f2dd5d8da7dbe4c6e915c127
title: feiskyer/koder/docs/agents-and-teams.md @ 55f553326039
updated_at: '2026-09-14T02:01:03Z'
---

# feiskyer/koder/docs/agents-and-teams.md @ 55f553326039

<!-- rcw:begin owner=source:src_8228fcd4f2dd5d8da7dbe4c6e915c127 block=evidence -->
- Koder supports background subagents via /fork and task_delegate with isolated default context, plus local teams via /peers with mailbox routing, task records, and team memory; teammates run in-process (default) or in tmux panes. [@claim:clm_2387c9da7ef7a5914910e8d0c01e00943c2cbc4a3aa2ae4493cf9949d38d593a]
- Agents with isolation: worktree frontmatter run in their own git worktree under .koder/worktrees/; empty worktrees are auto-removed and ones with uncommitted work are kept, with SubagentStart/Stop and WorktreeCreate/Remove hook events. [@claim:clm_d2ca4f0502aeaff82bcc5cbed1c85b86a3ce0b5b710717b7df24e017e49142c7]
<!-- rcw:end owner=source:src_8228fcd4f2dd5d8da7dbe4c6e915c127 block=evidence -->

## Researcher notes

