---
access: public
aliases: []
claim_ids:
- clm_2018c6219dfb72dfd0acb9ebefb027838218775f1c7f0a1ab9d19730b0b678e7
- clm_250b88293dd96367dea437f48198c698874a270823a7a6962d13fd8789b0a5ff
- clm_42ed3a22da230600e92df9644d8e4aba2d18ddd7d1c987171fb7a92c244a3810
- clm_69d3be32c32edff26ad8273753fad67457672887423e022e93b204dd645802f2
- clm_9b4a532ad64f09b6efaea344345be7a19e1f23f3ecb4fac7021de4079306b1bd
- clm_9eed03bd4cd462e36b284541bccf52cd447c1b05748aa80c398525f2dc3d9d32
- clm_a703d06855b41af1fde2da0f877a5009fd53ed865795dc0dde14b0712c1c7e12
- clm_b059a7d7ed3b4f852742f9ebbdf01aa4d84bd33e8a7826e6df65d85c24f2f250
- clm_ba79378d9de5b1295aa6257570eb695a44253e321db25d1227ec501fa61aa929
- clm_de5e41cb55dc06640216ad9b756eed5fce68c429f99802f8d765a5da1578f526
- clm_e83bc772c0ce2638c050d92f148cd129ffa3c080779829852e69977d23911b75
- clm_f1ff934219c8c2b10fde5cb3797cd1c5909e737680e6e3d7a51a33eda92a447f
- clm_f89df1ec02466e948c27e6ae512cda5579b82e707546d9a13546668e5ab43656
maturity: draft
page_id: pg_19a517fba4a85d87956c56eabdae3c0b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_090e08ca26395818abfe77ae9f3d5f49
title: DimitriGeelen/agentic-engineering-framework/README.md @ 35aaaaedc1c3
updated_at: '2026-09-14T02:00:39Z'
---

# DimitriGeelen/agentic-engineering-framework/README.md @ 35aaaaedc1c3

<!-- rcw:begin owner=source:src_090e08ca26395818abfe77ae9f3d5f49 block=evidence -->
- Prerequisites are bash 4.4+, git 2.20+, and python3 3.8+; PyYAML is optional (needed for fw serve and some helpers), and Node.js is optional with Python as fallback for TypeScript hooks. [@claim:clm_2018c6219dfb72dfd0acb9ebefb027838218775f1c7f0a1ab9d19730b0b678e7]
- Approval verbs such as fw inception decide, fw arc close, and fw bvp confirm refuse to run under agent control and route to a human via the Watchtower dashboard. [@claim:clm_250b88293dd96367dea437f48198c698874a270823a7a6962d13fd8789b0a5ff]
- Three memory layers persist across sessions: working memory in .context/working/, project memory in .context/project/, and episodic memory of completed tasks in .context/episodic/. [@claim:clm_42ed3a22da230600e92df9644d8e4aba2d18ddd7d1c987171fb7a92c244a3810]
- A Framework MCP server exposes 22 capabilities (16 read-only, 6 agent-authority) to external agents; five sovereignty-bound verbs are deliberately never registered, and agent-authority tools shell out through bin/fw so the same gates fire. [@claim:clm_69d3be32c32edff26ad8273753fad67457672887423e022e93b204dd645802f2]
- The framework's core principle is traceability: nothing gets done without a task, with conversations, decisions, and artefacts captured in a record called the Context Fabric. [@claim:clm_9b4a532ad64f09b6efaea344345be7a19e1f23f3ecb4fac7021de4079306b1bd]
- `fw recall` searches learnings, patterns, decisions, and episodics by meaning rather than keyword, and `fw handover --commit` writes a structured handover the next session reads on start. [@claim:clm_9eed03bd4cd462e36b284541bccf52cd447c1b05748aa80c398525f2dc3d9d32]
- The README states this is alpha software; multi-provider validation for Cursor, Aider, and Devin is designed but not validated, with Claude Code as the tested provider, and Watchtower auto-start is not yet shipped. [@claim:clm_a703d06855b41af1fde2da0f877a5009fd53ed865795dc0dde14b0712c1c7e12]
- A PreToolUse hook intercepts file modifications and refuses edits when no active task is set; build tasks with placeholder acceptance criteria are blocked (policy G-020). [@claim:clm_b059a7d7ed3b4f852742f9ebbdf01aa4d84bd33e8a7826e6df65d85c24f2f250]
- The product exposes a `fw` CLI (about 60 verbs across 11 sections) including work-on, audit, recall, fabric blast-radius, handover, serve, tier0 approve, and mcp lifecycle commands. [@claim:clm_ba79378d9de5b1295aa6257570eb695a44253e321db25d1227ec501fa61aa929]
- A Component Fabric maps how code pieces relate, making a change's blast radius visible before the change rather than after. [@claim:clm_de5e41cb55dc06640216ad9b756eed5fce68c429f99802f8d765a5da1578f526]
- A tiered authority model: Tier 0 destructive commands need human approval via `fw tier0 approve`, Tier 1 edits need an active task, Tier 2 exceptions are single-use and logged, Tier 3 read-only is pre-approved. [@claim:clm_e83bc772c0ce2638c050d92f148cd129ffa3c080779829852e69977d23911b75]
- The framework wraps an external TermLink binary for cross-terminal, cross-host worker sessions, with bus manifest/read, dispatch send over SSH, and pickup verbs for coordination. [@claim:clm_f1ff934219c8c2b10fde5cb3797cd1c5909e737680e6e3d7a51a33eda92a447f]
- The framework coordinates agents but does not execute them; it is not an agent runtime or multi-agent pipeline, and the model lives in the user's CLI agent while governance lives here. [@claim:clm_f89df1ec02466e948c27e6ae512cda5579b82e707546d9a13546668e5ab43656]
<!-- rcw:end owner=source:src_090e08ca26395818abfe77ae9f3d5f49 block=evidence -->

## Researcher notes

