---
access: public
aliases: []
claim_ids:
- clm_801d1a7de3c9093fa3d5dc2857605f65e439d2856b962b96f5f81e603f76439d
- clm_83cd58f2a34483b2f8c557ce05f0c1d819ec98f33ba11c394c355e8823c67526
- clm_b8e736c78a091225ca6f5ec0caf31190ab3acb491641e0786abfcc237d32f060
- clm_c6fe0744f03e81c52accf3c047284a1720707030b557ba38f6d1e5a3bb11ea92
- clm_cd44f61b7d1232ecee8acc0671a1f022c219fbc0d9fb2936a49ef67494275bca
- clm_e248fed1616b582fa63f6bcefac6f56e9cedade7d0bb0afbe22af57814afac4f
- clm_f7623ff1a657804b23de4140cfd0613403ef9063d2b6551373647c6fbb6130a1
maturity: draft
page_id: pg_fd797560abc6565eb8099154dd6941af
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7320b6928fe75e6a8700e61610bae1b7
title: griddynamics/rosetta/docs/ARCHITECTURE.md @ 785054e925aa
updated_at: '2026-09-14T03:54:35Z'
---

# griddynamics/rosetta/docs/ARCHITECTURE.md @ 785054e925aa

<!-- rcw:begin owner=source:src_7320b6928fe75e6a8700e61610bae1b7 block=evidence -->
- rosettify-prompts is a dev-only prompt A/B/N benchmark against the Anthropic API, comparing tokens, cost, latency, and stability across concurrent conversation variants; it is not shipped to end users. [@claim:clm_801d1a7de3c9093fa3d5dc2857605f65e439d2856b962b96f5f81e603f76439d]
- The MCP server is built on FastMCP v3 with Streamable HTTP + OAuth 2.1 and STDIO transports, and the MCP pipeline involves Redis schema migrations and RAGFlow datasets. [@claim:clm_83cd58f2a34483b2f8c557ce05f0c1d819ec98f33ba11c394c355e8823c67526]
- Rosettify is a local CLI/MCP utility providing deterministic workflow execution with zero network calls; it includes plan management, specs management, an atomic write cycle with a backup chain, and sequential phase enforcement. [@claim:clm_b8e736c78a091225ca6f5ec0caf31190ab3acb491641e0786abfcc237d32f060]
- The curiocity harness drives coding-agent CLIs (Claude Code, Codex) through a real PTY, reads native on-disk transcripts, auto-answers agent questions via LLM, and scores runs with deterministic checks plus an LLM judge, gating CI on the aggregate. [@claim:clm_c6fe0744f03e81c52accf3c047284a1720707030b557ba38f6d1e5a3bb11ea92]
- Rosetta defines typed command aliases (e.g. USE SKILL, APPLY PHASE, INVOKE SUBAGENT) that work across IDEs instead of calling MCP tools directly, for portability, decoupling, and authoring. [@claim:clm_cd44f61b7d1232ecee8acc0671a1f022c219fbc0d9fb2936a49ef67494275bca]
- The rosettify tool is published on npm and invoked via npx, or run as a local MCP server over stdio with a --mcp flag; it offers plan and specs subcommands operating on local JSON files. [@claim:clm_e248fed1616b582fa63f6bcefac6f56e9cedade7d0bb0afbe22af57814afac4f]
- The architecture follows inversion of control: Rosetta does not see or process source code; it exposes guardrails and a menu of instructions, and the coding agent selects only what it needs. [@claim:clm_f7623ff1a657804b23de4140cfd0613403ef9063d2b6551373647c6fbb6130a1]
<!-- rcw:end owner=source:src_7320b6928fe75e6a8700e61610bae1b7 block=evidence -->

## Researcher notes

