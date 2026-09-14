---
access: public
aliases: []
claim_ids:
- clm_4b0c04c68b0b3663363980086499526722e0b608797c34729b7dcd0b62314c27
- clm_d7537b2c88ec5bfdb16c8b73c39c243c7eb6238b84151fa60e4b0e0b31c1a060
maturity: draft
page_id: pg_271fe2ae1d52576da37052639e896339
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_daa8306a64875810a02f47980fdc9366
title: OpenBMB/ChatDev/docs/user_guide/en/modules/memory.md @ 4fb2db0ea903
updated_at: '2026-09-14T02:26:10Z'
---

# OpenBMB/ChatDev/docs/user_guide/en/modules/memory.md @ 4fb2db0ea903

<!-- rcw:begin owner=source:src_daa8306a64875810a02f47980fdc9366 block=evidence -->
- Agent nodes attach memories via MemoryAttachmentConfig with fields for store name, retrieve_stage, top_k (default 3), similarity_threshold, and read/write flags; retrieved items are injected into the agent context and writes occur after node completion. [@claim:clm_4b0c04c68b0b3663363980086499526722e0b608797c34729b7dcd0b62314c27]
- The memory system offers four built-in store types: simple (FAISS plus semantic rerank, read/write), file (read-only vector index over documents), blackboard (append-only recency log), and mem0 (cloud-managed, requires the mem0ai package). [@claim:clm_d7537b2c88ec5bfdb16c8b73c39c243c7eb6238b84151fa60e4b0e0b31c1a060]
<!-- rcw:end owner=source:src_daa8306a64875810a02f47980fdc9366 block=evidence -->

## Researcher notes

