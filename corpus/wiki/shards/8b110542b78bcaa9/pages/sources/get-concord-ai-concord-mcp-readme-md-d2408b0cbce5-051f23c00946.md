---
access: public
aliases: []
claim_ids:
- clm_0adb3cce0386055f7816236bb303e9b2e02dccb065ab5ab5d597dabbfc81df6f
- clm_3be86c5d68e9296651c8470c1b9d8d231f1ef0dbdcb7231c0692eead852bd82d
- clm_3d576647722fe4ebafc08002ae00258134af940f394b5814e0d6bc8496883b09
- clm_67bb37c8a7515cbbf62772910001b991f80b70438b022c63a59069dcd1ebe5ad
- clm_730768a1bf06d275b6d25698b32d44a78ca7e25a39de167902d3e44676d794cf
- clm_791d497129e7081ea5165b5dc4bb0574e5e1e7f24cf5af61968f5e1aa7a1be6e
- clm_89aa6cdd2162c79a7f25bb0eed3b0c9b53dd2c6fb088d412a5f2f7edddf8c75e
- clm_9082783e8004127566c87c8d7ee790f38f890473fec3b6becb81e9fc8cd2f5a4
- clm_b1c6343914e410896c5e4ee6937a85cd6088beb07fe5867e77596b452c52c445
- clm_d8fe9d7f0184b63d76ae218922c599b68898b559ede3d386a4c8d3d91837fb23
- clm_dd3337486c17d78b768c84b25445f138775744bf0bcfe8bad4686c4d37ee7a94
- clm_f2153a3de9b07a225994ed0018bec4e003653fcd097d5f65a7b5f7cff4406b82
maturity: draft
page_id: pg_22a60e41f1495b6fabf6051f23c00946
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f1a20d2129ba54bda19c895e73341f2b
title: Get-Concord-AI/concord-mcp/README.md @ d2408b0cbce5
updated_at: '2026-09-14T03:53:39Z'
---

# Get-Concord-AI/concord-mcp/README.md @ d2408b0cbce5

<!-- rcw:begin owner=source:src_f1a20d2129ba54bda19c895e73341f2b block=evidence -->
- Repository development practice: releases publish to npm via OIDC trusted publishing from a v* tag-triggered GitHub Actions workflow, with an optional maintainer-approval environment gate; contributing guidance points to CONTRIBUTING.md and CLAUDE.md and notes strict typing with no 'any' or typecasts. [@claim:clm_0adb3cce0386055f7816236bb303e9b2e02dccb065ab5ab5d597dabbfc81df6f]
- There is no universal /concord slash command; integration is via MCP tools plus installed per-client instructions, and live delivery depends on the receiving harness and session state. [@claim:clm_3be86c5d68e9296651c8470c1b9d8d231f1ef0dbdcb7231c0692eead852bd82d]
- The package is distributed as @concord-ai/concord-mcp on npm, installed globally, and the release workflow requires Node 24 and npm >= 11.5.1. [@claim:clm_3d576647722fe4ebafc08002ae00258134af940f394b5814e0d6bc8496883b09]
- Delivery fails immediately when the named agent has no reachable endpoint rather than silently rerouting; hook-only integrations leave a durable pull message and state that limitation in the result. [@claim:clm_67bb37c8a7515cbbf62772910001b991f80b70438b022c63a59069dcd1ebe5ad]
- Besides MCP tools, Concord offers a CLI (setup, status, dashboard, who, tasks, handoff, review-packet, export, doctor, adapters status) operating on the same shared workspace. [@claim:clm_730768a1bf06d275b6d25698b32d44a78ca7e25a39de167902d3e44676d794cf]
- Telemetry is sent to getconcord.ai but excludes code, paths, identifiers, and message content; CONCORD_TELEMETRY_DISABLED=1 or DO_NOT_TRACK=1 disables it, and delivery is best-effort so it can never fail an operation. [@claim:clm_791d497129e7081ea5165b5dc4bb0574e5e1e7f24cf5af61968f5e1aa7a1be6e]
- Lifecycle-changing operations use the task's monotonic version as expected_version, so of two agents acting on the same version only the first transition succeeds; ownership changes are kept in an append-only audit history. [@claim:clm_89aa6cdd2162c79a7f25bb0eed3b0c9b53dd2c6fb088d412a5f2f7edddf8c75e]
- SQLite in the repo-root .concord/ directory is the local source of truth; the root is resolved from CONCORD_REPO_ROOT, then CLAUDE_PROJECT_DIR, then the working directory, so agents in one repo share one store. [@claim:clm_9082783e8004127566c87c8d7ee790f38f890473fec3b6becb81e9fc8cd2f5a4]
- Agent-to-agent prompts use update_work with operation "prompt", a to_agent_id, content, and idempotency_key; replies use operation "reply" with reply_to_message_id. [@claim:clm_b1c6343914e410896c5e4ee6937a85cd6088beb07fe5867e77596b452c52c445]
- The product exposes five MCP tools: start_work, inspect_work, update_work, transfer_work, and finish_work, covering presence/claims, state reads, prompts, ownership changes, and completion evidence. [@claim:clm_d8fe9d7f0184b63d76ae218922c599b68898b559ede3d386a4c8d3d91837fb23]
- The .concord/ workspace holds concord.db, HANDOFF.md, REVIEW_PACKET.md, and an optional WORK_STATE.json export; setup gitignores the directory so it stays local by default. [@claim:clm_dd3337486c17d78b768c84b25445f138775744bf0bcfe8bad4686c4d37ee7a94]
- The README states Concord is not an orchestrator, code reviewer, hosted sync service, memory vector DB, or autonomous coding agent — it is a shared work-state layer for agents in the same local checkout. [@claim:clm_f2153a3de9b07a225994ed0018bec4e003653fcd097d5f65a7b5f7cff4406b82]
<!-- rcw:end owner=source:src_f1a20d2129ba54bda19c895e73341f2b block=evidence -->

## Researcher notes

