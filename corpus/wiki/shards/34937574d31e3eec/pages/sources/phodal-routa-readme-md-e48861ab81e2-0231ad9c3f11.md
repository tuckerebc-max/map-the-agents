---
access: public
aliases: []
claim_ids:
- clm_22916abf5c50d08ac92b0f56e6f60002200e80c9147cdda686877440656a4818
- clm_38a6d9c7056885d8526445cbb1fb0b6aafbaa10f2cc8c884805403277a8bbfeb
- clm_57d083d4ae653f8acbbbe7de9eaa2400a2a87243c6aee1c97555ee073279f11d
- clm_5ee473c51bfe5e67818cdde7ebbe30a87126f3433c6b2d4e37c533a57556b84c
- clm_6490c16d69edc7484e597dc3cf3403030a9a20783b848c953a1669955b758e5d
- clm_cac67e64e405953ff060de1a04427ac8c3a78ae6608a1d73bd2708a48ef0f881
- clm_cd8623e22d4b5467b9d32111b6fb11424b31d8a09601ae0199645abfff5ddc2b
- clm_d11b0ec7559c88ef159c25f0445fa0562d4e978d624bdc1668358fac7f975d08
- clm_df0add6a4692c86d54c96c19f328dd61f4469d558a075367d6c3ec3c471980df
- clm_ee5e3b746d38d78181ea6990be01595949421d4a1d729363f5cd049499a23f54
maturity: draft
page_id: pg_3c0e366c0272504ba5270231ad9c3f11
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_780a01174d315d5284553833bdc171eb
title: phodal/routa/README.md @ e48861ab81e2
updated_at: '2026-09-14T02:31:09Z'
---

# phodal/routa/README.md @ e48861ab81e2

<!-- rcw:begin owner=source:src_780a01174d315d5284553833bdc171eb block=evidence -->
- The CLI is distributed as routa-cli on npm and crates.io, with commands such as routa --help, routa acp list, and routa workspace list. [@claim:clm_22916abf5c50d08ac92b0f56e6f60002200e80c9147cdda686877440656a4818]
- The implementation is intentionally dual-backend: a Next.js web app in src/, a Tauri desktop shell backed by an Axum server in crates/routa-server, sharing semantics defined by api-contract.yaml. [@claim:clm_38a6d9c7056885d8526445cbb1fb0b6aafbaa10f2cc8c884805403277a8bbfeb]
- Built-in lane prompts live under resources/specialists/workflows/kanban/*.yaml, and core role prompts (routa, crafter, gate) under resources/specialists/core/. [@claim:clm_57d083d4ae653f8acbbbe7de9eaa2400a2a87243c6aee1c97555ee073279f11d]
- Routa is described as a workspace-first multi-agent coordination platform for software delivery, keeping goals, tasks, sessions, traces, evidence, and review state visible on a board rather than in one chat thread. [@claim:clm_5ee473c51bfe5e67818cdde7ebbe30a87126f3433c6b2d4e37c533a57556b84c]
- Work flows through Kanban lanes Backlog, Todo, Dev, Review, Done, each backed by a specialist prompt (Backlog Refiner, Todo Orchestrator, Dev Crafter, Review Guard, Done Reporter), with a Blocked Resolver for blocked work. [@claim:clm_6490c16d69edc7484e597dc3cf3403030a9a20783b848c953a1669955b758e5d]
- Each downstream lane is deliberately stricter than the previous one; cards accumulate artifacts (story YAML, execution brief, dev evidence, review verdict, completion summary) as they move forward. [@claim:clm_cac67e64e405953ff060de1a04427ac8c3a78ae6608a1d73bd2708a48ef0f881]
- Repository map includes crates/routa-core (shared Rust runtime foundation), crates/routa-cli (CLI entrypoints and ACP serving), and crates/harness-monitor (run observation and operator-facing harness monitor). [@claim:clm_cd8623e22d4b5467b9d32111b6fb11424b31d8a09601ae0199645abfff5ddc2b]
- Integration surfaces listed include ACP, MCP, A2A, AG-UI, A2UI, REST, and SSE. [@claim:clm_d11b0ec7559c88ef159c25f0445fa0562d4e978d624bdc1668358fac7f975d08]
- Badges indicate TypeScript 5.9, Next.js 16.2, and Rust with Axum; the project is MIT licensed. [@claim:clm_df0add6a4692c86d54c96c19f328dd61f4469d558a075367d6c3ec3c471980df]
- The review gate is a stacked decision path with three layers: Harness Monitor (what happened), Entrix Fitness (what should be true, hard gates and evidence requirements), and Gate Specialist (whether the card can move). [@claim:clm_ee5e3b746d38d78181ea6990be01595949421d4a1d729363f5cd049499a23f54]
<!-- rcw:end owner=source:src_780a01174d315d5284553833bdc171eb block=evidence -->

## Researcher notes

