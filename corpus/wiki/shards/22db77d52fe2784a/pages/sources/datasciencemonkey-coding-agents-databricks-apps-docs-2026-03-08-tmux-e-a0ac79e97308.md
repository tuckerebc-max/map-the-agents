---
access: public
aliases: []
claim_ids:
- clm_1a15a7eaff68ece1180dfdc7d7c4e15a165ae65350e42953182e55c1bdfbda95
- clm_afcdbfa036754c14af752bdb5baa1070b47a29a4f00430823dfe9c92c28df6eb
- clm_b8f28c94857f46c7e2971994a347516cb7bd99153d681344402100b29d206d6e
maturity: draft
page_id: pg_333543f037e755b5a32fa0ac79e97308
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d34ac7b216ee5d568608a166c0f2a3c1
title: datasciencemonkey/coding-agents-databricks-apps/docs/2026-03-08-tmux-evaluation.md
  @ e4a4b216e439
updated_at: '2026-09-14T03:45:34Z'
---

# datasciencemonkey/coding-agents-databricks-apps/docs/2026-03-08-tmux-evaluation.md @ e4a4b216e439

<!-- rcw:begin owner=source:src_d34ac7b216ee5d568608a166c0f2a3c1 block=evidence -->
- A tmux evaluation concluded tmux should be removed in favor of localStorage-based session recovery, because tmux caused visual artifacts, resize conflicts, and keybinding clashes. [@claim:clm_1a15a7eaff68ece1180dfdc7d7c4e15a165ae65350e42953182e55c1bdfbda95]
- The tmux evaluation acknowledges a remaining gap: if Gunicorn kills a worker, PTY file descriptors are lost and the localStorage recovery approach cannot restore those sessions. [@claim:clm_afcdbfa036754c14af752bdb5baa1070b47a29a4f00430823dfe9c92c28df6eb]
- A state_sync.py process persists Claude Code auto-memory and bash history to /Workspace/Users/{email}/.state/ every 5 minutes, since only /Workspace files survive container restarts. [@claim:clm_b8f28c94857f46c7e2971994a347516cb7bd99153d681344402100b29d206d6e]
<!-- rcw:end owner=source:src_d34ac7b216ee5d568608a166c0f2a3c1 block=evidence -->

## Researcher notes

