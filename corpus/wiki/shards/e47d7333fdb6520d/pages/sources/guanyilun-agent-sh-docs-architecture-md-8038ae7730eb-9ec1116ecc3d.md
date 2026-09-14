---
access: public
aliases: []
claim_ids:
- clm_753604f7f83b0d94d5fdeff1e2a2572d13c6e276b53336223acda03ba53113b5
maturity: draft
page_id: pg_1a7bee5c4fe65e7080a59ec1116ecc3d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ee863c2c0bed58b5a9cae73a397c8980
title: guanyilun/agent-sh/docs/architecture.md @ 8038ae7730eb
updated_at: '2026-09-14T01:52:03Z'
---

# guanyilun/agent-sh/docs/architecture.md @ 8038ae7730eb

<!-- rcw:begin owner=source:src_ee863c2c0bed58b5a9cae73a397c8980 block=evidence -->
- The architecture is a pure kernel (`createCore()`) providing EventBus, HandlerRegistry, Compositor, multi-backend coordination, and a default cwd handler, with agent, shell, TUI, and providers all loaded as extensions. [@claim:clm_753604f7f83b0d94d5fdeff1e2a2572d13c6e276b53336223acda03ba53113b5]
<!-- rcw:end owner=source:src_ee863c2c0bed58b5a9cae73a397c8980 block=evidence -->

## Researcher notes

