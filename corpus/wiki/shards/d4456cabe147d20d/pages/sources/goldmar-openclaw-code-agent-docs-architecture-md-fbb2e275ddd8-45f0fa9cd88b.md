---
access: public
aliases: []
claim_ids:
- clm_1a572e56a112ad70cbab6e87a17eb229b4c9c7c44937361e63adc28f6c9d57af
- clm_ef1082d228791e2d303f5560357f30046ec54340b1de0b9314bbd27c9349f21d
- clm_ff1926c3b87746d10ff10c1cf06282f20fe1d54516e43f1c33c4c4b2ccfcda41
maturity: draft
page_id: pg_347ce6fec518566f9d9c45f0fa9cd88b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1ed538f7580f55b49b89b929e8082046
title: goldmar/openclaw-code-agent/docs/ARCHITECTURE.md @ fbb2e275ddd8
updated_at: '2026-09-14T01:52:24Z'
---

# goldmar/openclaw-code-agent/docs/ARCHITECTURE.md @ fbb2e275ddd8

<!-- rcw:begin owner=source:src_1ed538f7580f55b49b89b929e8082046 block=evidence -->
- src/session-manager.ts is the control plane: it enforces maxSessions, spawns and tracks sessions, resolves resume/fork requests, persists runtime metadata and output, and composes notification, interaction, and worktree-controller services. [@claim:clm_1a572e56a112ad70cbab6e87a17eb229b4c9c7c44937361e63adc28f6c9d57af]
- Sessions support suspend, resume, fork, interrupt, and recovery across restarts with persisted metadata and output; persisted records stay resumable even after runtime sessions are garbage-collected at sessionGcAgeMinutes. [@claim:clm_ef1082d228791e2d303f5560357f30046ec54340b1de0b9314bbd27c9349f21d]
- The OpenCode harness is explicitly experimental: it runs a per-session local 'opencode serve' process, uses classic session lifecycle routes because v2 session wait is unavailable, and does not forward the reasoning-effort option. [@claim:clm_ff1926c3b87746d10ff10c1cf06282f20fe1d54516e43f1c33c4c4b2ccfcda41]
<!-- rcw:end owner=source:src_1ed538f7580f55b49b89b929e8082046 block=evidence -->

## Researcher notes

