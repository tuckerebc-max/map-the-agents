---
access: public
aliases: []
claim_ids:
- clm_17cc819bca8d21cf6c9d191bbaab9e041a0d2fd832e754877e069354c13d7d63
- clm_9d32a63b513f4fb1a0e259c3c83652f5b387e7273575008d9457a5f65a52c0f4
maturity: draft
page_id: pg_08ba1e7c604d5087861e1b1114f2fb2b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_920519ec9b785ec6bc45078970c48b81
title: andyrewlee/amux/AGENTS.md @ f94362f6c25f
updated_at: '2026-09-14T01:33:26Z'
---

# andyrewlee/amux/AGENTS.md @ f94362f6c25f

<!-- rcw:begin owner=source:src_920519ec9b785ec6bc45078970c48b81 block=evidence -->
- The amux-harness binary appears to support deterministic perf and render testing of the UI itself (headless frame dumps), suggesting an internal render/perf evaluation path rather than agent-task benchmarking. [@claim:clm_17cc819bca8d21cf6c9d191bbaab9e041a0d2fd832e754877e069354c13d7d63]
- Repository development practice: AGENTS.md instructs validating changes with make devcheck, using the harness with -dump-frame for headless render verification, and running make verify-loop for input/send/tmux changes to prove end-to-end keystroke delivery. [@claim:clm_9d32a63b513f4fb1a0e259c3c83652f5b387e7273575008d9457a5f65a52c0f4]
<!-- rcw:end owner=source:src_920519ec9b785ec6bc45078970c48b81 block=evidence -->

## Researcher notes

