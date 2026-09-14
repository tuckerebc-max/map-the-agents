---
access: public
aliases: []
claim_ids:
- clm_1f1dc01c0820dba305326130bbf571201bdaadab1e6d52f74cd6bec1699931f9
- clm_30baedf91f92c1f02efc97178cb0e217e8876fe0cc41365e146b423d57b5bc55
- clm_587f4e0bee99f1d4a569b68b5914f1ab5d931735e118a675b35b9b3bbdc01b6c
- clm_5d1e66f623075314a51fcf11be130f3b3b8a31bfd9796e1654645e763070de4f
- clm_86720398fff7f344e1d1b38cfcd51aed69ca2788453df3828eba6e18d87da653
- clm_f6f971e5b4d98701fbd3d303301d5dde08acb83da7ac3bfefdce9a5f55675b4c
maturity: draft
page_id: pg_35defd83afe85bd5b82c1d8a36c10376
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d9afc24621755158bfc599654af39cac
title: sipyourdrink-ltd/bernstein/docs/architecture/ARCHITECTURE.md @ ce5c5217c1dc
updated_at: '2026-09-14T04:21:54Z'
---

# sipyourdrink-ltd/bernstein/docs/architecture/ARCHITECTURE.md @ ce5c5217c1dc

<!-- rcw:begin owner=source:src_d9afc24621755158bfc599654af39cac block=evidence -->
- The Task Server is a FastAPI REST application on port 8052 exposing /tasks, /status, and /metrics, with routes split across roughly 70 modules in core/routes/ and state checkpointed to .sdd/runtime/tasks.jsonl. [@claim:clm_1f1dc01c0820dba305326130bbf571201bdaadab1e6d52f74cd6bec1699931f9]
- A LineageSpine provides an always-on Merkle+HMAC provenance chain; every adapter artifact write routes through LineageSpine.record at a single write boundary, appending hash-chained rows to .sdd/lineage/<run_id>/spine.jsonl. [@claim:clm_30baedf91f92c1f02efc97178cb0e217e8876fe0cc41365e146b423d57b5bc55]
- A janitor verifies task completion via concrete signals (files exist, tests pass, content matches) and moves tasks to done/ or failed/ without trusting agent claims; a separate LLM reviewer runs afterward and can push corrections back into the queue. [@claim:clm_587f4e0bee99f1d4a569b68b5914f1ab5d931735e118a675b35b9b3bbdc01b6c]
- All state is stored as files under .sdd/ with no databases or hidden memory, chosen for inspectability, recoverability, auditability, and git-friendliness; runtime state under .sdd/runtime/ is ephemeral. [@claim:clm_5d1e66f623075314a51fcf11be130f3b3b8a31bfd9796e1654645e763070de4f]
- The orchestrator is deterministic Python with no model in the coordination loop; only one planning LLM call happens up front, and the same plan replays to a byte-identical task graph. [@claim:clm_86720398fff7f344e1d1b38cfcd51aed69ca2788453df3828eba6e18d87da653]
- Pluggable sandbox backends implement a SandboxBackend/SandboxSession protocol; first-party options are worktree (default), docker, e2b Firecracker microVMs, and modal serverless containers, with third parties registering via an entry-point group. [@claim:clm_f6f971e5b4d98701fbd3d303301d5dde08acb83da7ac3bfefdce9a5f55675b4c]
<!-- rcw:end owner=source:src_d9afc24621755158bfc599654af39cac block=evidence -->

## Researcher notes

