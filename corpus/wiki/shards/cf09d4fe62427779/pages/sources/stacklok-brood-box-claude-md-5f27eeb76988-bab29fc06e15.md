---
access: public
aliases: []
claim_ids:
- clm_8008fbafa15bc55a7f8c0ab1be53cfd09640010748e31a598d0605dc81226881
- clm_b7fcc5c1ad3a89004acda19fee5016125a8b4ef5dd8eb7eb3f715ede62262b20
- clm_b8de62be6f9bf9952a4806e1599889fd995a1335b1f94f45901501b498b0eaaa
maturity: draft
page_id: pg_625391cc4a72562888c8bab29fc06e15
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4d6b6a18d36250c28c9a2dc17d99e90c
title: stacklok/brood-box/CLAUDE.md @ 5f27eeb76988
updated_at: '2026-09-14T02:42:31Z'
---

# stacklok/brood-box/CLAUDE.md @ 5f27eeb76988

<!-- rcw:begin owner=source:src_4d6b6a18d36250c28c9a2dc17d99e90c block=evidence -->
- Repository development practice: the project enforces strict DDD layer boundaries with dependency injection, and code that violates layer boundaries is treated as a blocking merge issue. [@claim:clm_8008fbafa15bc55a7f8c0ab1be53cfd09640010748e31a598d0605dc81226881]
- Repository development practice: contributors must always use `task` targets (build, test, lint, fmt, verify) rather than raw go/docker commands, because the Taskfile sets critical flags, ldflags, and environment variables. [@claim:clm_b7fcc5c1ad3a89004acda19fee5016125a8b4ef5dd8eb7eb3f715ede62262b20]
- Built-in agents (claude-code, codex, opencode, hermes, gemini) each ship as a per-agent client package pairing an Agent value with a Plugin for MCP config injection and credential seeding, and custom agents can be defined in config. [@claim:clm_b8de62be6f9bf9952a4806e1599889fd995a1335b1f94f45901501b498b0eaaa]
<!-- rcw:end owner=source:src_4d6b6a18d36250c28c9a2dc17d99e90c block=evidence -->

## Researcher notes

