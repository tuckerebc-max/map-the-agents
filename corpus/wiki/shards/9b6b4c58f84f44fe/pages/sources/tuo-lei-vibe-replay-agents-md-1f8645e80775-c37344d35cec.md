---
access: public
aliases: []
claim_ids:
- clm_b140e9b755925363aefbba99dd95546395b462c30d0f4f5373e7c89bb72ea838
- clm_f6920e88e359fe8570f0f995113b7a5b07dc46e41557bf58e6bc802487af3101
maturity: draft
page_id: pg_85e69f7d7c67511cb4c0c37344d35cec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6b2e7765935d5d48b906f8a618b8c80f
title: tuo-lei/vibe-replay/AGENTS.md @ 1f8645e80775
updated_at: '2026-09-14T04:27:41Z'
---

# tuo-lei/vibe-replay/AGENTS.md @ 1f8645e80775

<!-- rcw:begin owner=source:src_6b2e7765935d5d48b906f8a618b8c80f block=evidence -->
- Generated replays are self-contained HTML files that make no automatic external requests; remote HTTP(S) images load only after an explicit per-image click, and data URLs render immediately. [@claim:clm_b140e9b755925363aefbba99dd95546395b462c30d0f4f5373e7c89bb72ea838]
- Repository development practice: AGENTS.md is the single source of truth for coding agents (CLAUDE.md is an @AGENTS.md shim), with pnpm-only tooling, oxlint/oxfmt via lefthook pre-commit, `pnpm verify` as the pre-PR gate, and a guard test enforcing the agent-instruction wiring and a 32 KiB AGENTS.md size limit. [@claim:clm_f6920e88e359fe8570f0f995113b7a5b07dc46e41557bf58e6bc802487af3101]
<!-- rcw:end owner=source:src_6b2e7765935d5d48b906f8a618b8c80f block=evidence -->

## Researcher notes

