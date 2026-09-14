---
access: public
aliases: []
claim_ids:
- clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26
- clm_151be13f17087c676c76c50fa013810f91a0db8e8fd85e1e01d7c53462f871c4
- clm_27d771a4615fbcfb0f831dc6ebc3d807780d2876177289fb5125954e43a0c26f
- clm_58dec173115ed2b423be7154e433283dda251967e8fda2d4f71ff19d60f81761
maturity: draft
page_id: pg_8a00673dd9a55fb7821d518c4f6e7819
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e361bf4545be5159945eb84b83b5c0a7
title: sondera-ai/sondera-coding-agent-hooks/docs/development.md @ 9efefedd249e
updated_at: '2026-09-14T04:22:24Z'
---

# sondera-ai/sondera-coding-agent-hooks/docs/development.md @ 9efefedd249e

<!-- rcw:begin owner=source:src_e361bf4545be5159945eb84b83b5c0a7 block=evidence -->
- Trajectories persist in a Turso (SQLite) store defaulting to ~/.sondera/trajectories/trajectories.db, overridable via --db; the console reads agents and trajectories from the same store. [@claim:clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26]
- Repository development practice: integration tests needing a reachable model provider are #[ignore]d by default and run explicitly with `cargo test -- --ignored` once the configured provider is up. [@claim:clm_151be13f17087c676c76c50fa013810f91a0db8e8fd85e1e01d7c53462f871c4]
- Repository development practice: CI runs cargo fmt --check, clippy with -D warnings, cargo doc, cargo test --locked --workspace, cargo deny check, and buf lint/format from crates/schema/proto; working conventions live in AGENTS.md. [@claim:clm_27d771a4615fbcfb0f831dc6ebc3d807780d2876177289fb5125954e43a0c26f]
- Every hook adapter depends on the harness crate as sondera-harness-client with default-features off and only the client feature, linking the gRPC client but not the policy engine. [@claim:clm_58dec173115ed2b423be7154e433283dda251967e8fda2d4f71ff19d60f81761]
<!-- rcw:end owner=source:src_e361bf4545be5159945eb84b83b5c0a7 block=evidence -->

## Researcher notes

