---
access: public
aliases: []
claim_ids:
- clm_205c2433ea579e7fdd152e073ee906bd80488a22dae6f41e58df9f1ac39e20a9
- clm_920f6343a022061b8b5d9f07fe91db7fb124b9af002631696878221a63b251e4
maturity: draft
page_id: pg_ee11239710d958439abde34a7c9cec9b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8752b9de84da595dbe9084b9f5b960fc
title: openai/codex/codex-rs/core/src/agent/control/user_authorization.rs @ 6f39a47bb3b0
updated_at: '2026-09-14T02:25:53Z'
---

# openai/codex/codex-rs/core/src/agent/control/user_authorization.rs @ 6f39a47bb3b0

<!-- rcw:begin owner=source:src_8752b9de84da595dbe9084b9f5b960fc block=evidence -->
- The Rust core includes an AgentControl method that returns bounded root conversation and authorization state for MultiAgent V2 worker threads, skipping when the thread is the root itself or not V2. [@claim:clm_205c2433ea579e7fdd152e073ee906bd80488a22dae6f41e58df9f1ac39e20a9]
- Root evidence projection filters the root thread's retained history, excluding summary messages and user messages starting with <user_action>, and caps root messages at 8. [@claim:clm_920f6343a022061b8b5d9f07fe91db7fb124b9af002631696878221a63b251e4]
<!-- rcw:end owner=source:src_8752b9de84da595dbe9084b9f5b960fc block=evidence -->

## Researcher notes

