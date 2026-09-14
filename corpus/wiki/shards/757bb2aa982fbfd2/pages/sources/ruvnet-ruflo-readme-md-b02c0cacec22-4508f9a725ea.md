---
access: public
aliases: []
claim_ids:
- clm_347620a1aae111431e019ceac8461e9108c8342e4265ddf9a5c493c4136f4b2c
- clm_368cccabb9a6e034c593cb88ac731f155daffe26bf5cd75f1ef9b907ffa747d0
- clm_54fbbe540ff43991766b97c2ac9c18b404f51aa3f62b7a746a5573880e71e60e
- clm_60db2f3bc01d70d84f90d5ffeced1e6854c758e9968c3b3e75c41094a026e8d7
- clm_690fbaed7928b895e91d8b291672cd5aa9ec829d414cdaf04c6d3652f60b3b1d
- clm_9947260fb2645b1bd1fdd2381a9874cf85a24cec68076dab42bf315c219d9f42
- clm_9d9601bbc8c2a3e3ff995385bea59953034b5470c5396c356949ff84c4b3c9f1
- clm_b3ae703a8c3388da567d8631d1e283a97569248acc465fd99f213b3f748dfc78
- clm_fa00bbe48e779308ee42f9c3cbbc11871d6ed4e73d9913eba53a2c1f1e418bec
maturity: draft
page_id: pg_4e77bad0aaed54dbb2934508f9a725ea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f029307c6c885aa18a3f5ee2b376a1d4
title: ruvnet/ruflo/README.md @ b02c0cacec22
updated_at: '2026-09-14T04:18:44Z'
---

# ruvnet/ruflo/README.md @ b02c0cacec22

<!-- rcw:begin owner=source:src_f029307c6c885aa18a3f5ee2b376a1d4 block=evidence -->
- The ruflo-core plugin registers its own MCP server with namespaced tool names like mcp__plugin_ruflo-core_ruflo__memory_store, differing from the CLI-track bare tool names. [@claim:clm_347620a1aae111431e019ceac8461e9108c8342e4265ddf9a5c493c4136f4b2c]
- Two install paths exist: Claude Code plugins (slash commands, zero workspace files) versus full CLI init which scaffolds .claude/, .claude-flow/, CLAUDE.md, hooks, and an MCP server. [@claim:clm_368cccabb9a6e034c593cb88ac731f155daffe26bf5cd75f1ef9b907ffa747d0]
- Ruflo exposes a CLI (npx ruflo) and an MCP server; the README shows registering it in Claude Code via 'claude mcp add claude-flow -- npx ruflo@latest mcp start'. [@claim:clm_54fbbe540ff43991766b97c2ac9c18b404f51aa3f62b7a746a5573880e71e60e]
- Swarm coordination supports hierarchical, mesh, and adaptive topologies with consensus, and the architecture diagram shows a Queen-led coordination layer above 100+ specialized agents. [@claim:clm_60db2f3bc01d70d84f90d5ffeced1e6854c758e9968c3b3e75c41094a026e8d7]
- Agent federation lets agents on different machines discover, authenticate (mTLS + ed25519), and exchange work, with PII stripped from outbound messages and per-trust-level policies (BLOCK, REDACT, HASH, PASS). [@claim:clm_690fbaed7928b895e91d8b291672cd5aa9ec829d414cdaf04c6d3652f60b3b1d]
- The README catalogs 35 plugins across categories including core/orchestration, memory, intelligence, testing, security, and domain-specific (e.g. ruflo-swarm, ruflo-rag-memory, ruflo-neural-trader). [@claim:clm_9947260fb2645b1bd1fdd2381a9874cf85a24cec68076dab42bf315c219d9f42]
- The runtime supports multiple LLM providers — Claude, GPT, Gemini, Cohere, and Ollama — with smart routing and failover. [@claim:clm_9d9601bbc8c2a3e3ff995385bea59953034b5470c5396c356949ff84c4b3c9f1]
- Memory uses an HNSW-indexed AgentDB; the README cites measured ~1.9x faster at N=20k versus brute force with recall@10 near 0.99, noting ANN ties or loses at small N. [@claim:clm_b3ae703a8c3388da567d8631d1e283a97569248acc465fd99f213b3f748dfc78]
- A SOTA comparator benchmark suite compares ruflo against LangGraph, AutoGen, and CrewAI on metrics like cold start, single turn, and RSS, with published matrix JSON for darwin and linux. [@claim:clm_fa00bbe48e779308ee42f9c3cbbc11871d6ed4e73d9913eba53a2c1f1e418bec]
<!-- rcw:end owner=source:src_f029307c6c885aa18a3f5ee2b376a1d4 block=evidence -->

## Researcher notes

