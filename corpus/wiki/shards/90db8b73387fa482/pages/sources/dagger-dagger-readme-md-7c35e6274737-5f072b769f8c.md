---
access: public
aliases: []
claim_ids:
- clm_086248ef5f19a63b47e04a84c1bdf7b482a6b01858d7ed067ab46c332d36ab37
- clm_1e6f3b614732ff6c7ae3f62b98bccd4113ba50e3ae08c6b9e851f393fe9a7985
- clm_59b369010545209ec952eeffada33e1ff4e0d3e43186baf6c143b19a121b7b97
- clm_84814ade7823a272e5849b4b71a5f5426530ab84b13a38cd66b762f21df7fd8a
- clm_d7651630f5ed41c4ce88358af829f17a99056ade0591290c15a1edbd1c8c5b3f
- clm_e9e4b4e91c4aef35598f73a1b5cd9aa5f8585b9b0c0b9d2e664fefccce4272e7
maturity: draft
page_id: pg_a2a1e3a1b0105295b4855f072b769f8c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0dd6a995a7795d778e18c2546d47c995
title: dagger/dagger/README.md @ 7c35e6274737
updated_at: '2026-09-14T05:10:24Z'
---

# dagger/dagger/README.md @ 7c35e6274737

<!-- rcw:begin owner=source:src_0dd6a995a7795d778e18c2546d47c995 block=evidence -->
- Every operation emits OpenTelemetry spans enriched with logs and metrics; the CLI includes a live TUI and traces can be exported to Jaeger, Honeycomb, or any OTel-compatible backend. [@claim:clm_086248ef5f19a63b47e04a84c1bdf7b482a6b01858d7ed067ab46c332d36ab37]
- The product ships SDKs in eight languages (Go, Python, TypeScript, PHP, Java, .NET, Elixir, Rust), each generated from the API schema, plus an interactive REPL. [@claim:clm_1e6f3b614732ff6c7ae3f62b98bccd4113ba50e3ae08c6b9e851f393fe9a7985]
- Custom object types are content-addressed and can cross SDK and module boundaries without serialization; every operation is keyed by its inputs so only affected operations re-run, with content-addressed caching across local runs and CI. [@claim:clm_59b369010545209ec952eeffada33e1ff4e0d3e43186baf6c143b19a121b7b97]
- The CLI can be installed via Homebrew with `brew install dagger/tap/dagger`, and the product runs locally, in CI servers, or in the cloud. [@claim:clm_84814ade7823a272e5849b4b71a5f5426530ab84b13a38cd66b762f21df7fd8a]
- Dagger is documented as a platform for automating software delivery, providing an execution engine and a system API for orchestrating containers, filesystems, secrets, git repositories, and network tunnels. [@claim:clm_d7651630f5ed41c4ce88358af829f17a99056ade0591290c15a1edbd1c8c5b3f]
- The only runtime requirement is a Linux container runtime such as Docker; it runs natively on Linux and via Docker Desktop or similar on macOS and Windows, with identical local and CI behavior. [@claim:clm_e9e4b4e91c4aef35598f73a1b5cd9aa5f8585b9b0c0b9d2e664fefccce4272e7]
<!-- rcw:end owner=source:src_0dd6a995a7795d778e18c2546d47c995 block=evidence -->

## Researcher notes

