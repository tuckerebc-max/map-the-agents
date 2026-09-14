---
access: public
aliases: []
claim_ids:
- clm_06f4228bb952599dbd759e294fcf575aad6e909b9e285be969fba93d634a9a21
- clm_259d5738952c044e6d62eb05076b3cb496f5f5074538b22c426de2e9939724d6
- clm_51939f3e0ab35c2240d6fbd7ca403c16c7400d8aa61742866f5d9de88b95365c
- clm_6c5954b537d41eb74d6d9fae0c51a418d72da816264d745e43ded2facae57883
- clm_7c7b381fa6f40cdf53fb0762e308f25144a875960519f212a18e78b787a2873d
- clm_99c766990a956f80d84f6e9a94579da166d052fe3c0f83715ed932e8bc0e1f96
- clm_9a43e031744baf7f41efecd557529d3510fe04ef902fa22b76dd03a752d11c6b
- clm_a21cb760f77cdf377656f6df7fb6c870c2a5ac597fc0e9ee5735a8837521aa16
- clm_a2c4be17e1ec17fd42aec0f2457c1802da1b4606e364f6a1a9ad8b0374109dfb
- clm_b059bd89bafae3c4faf876bae440748168ab533584db7412cc64054d43773065
- clm_f8fa920e10027f871240ab9bc5cfcdf64ba8763a63c7b89c23d9523498455dc1
- clm_fce70803312adb0ffbb1d477af132890972a30ef4725ca58b2ad07c16f118bfd
maturity: draft
page_id: pg_5f10871c316c51beb22b8d9091007910
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_20082b2e6b1b5933ab279e89d6c92ac2
title: pacifio/cersei/README.md @ 708c5055845b
updated_at: '2026-09-14T02:29:01Z'
---

# pacifio/cersei/README.md @ 708c5055845b

<!-- rcw:begin owner=source:src_20082b2e6b1b5933ab279e89d6c92ac2 block=evidence -->
- MCP integration connects stdio and SSE servers via McpManager and exposes their tool definitions to the agent builder; the MCP client uses JSON-RPC 2.0 over stdio transport. [@claim:clm_06f4228bb952599dbd759e294fcf575aad6e909b9e285be969fba93d634a9a21]
- Skills auto-discover from .claude/commands/*.md, .claude/skills/*/SKILL.md, user-level ~/.claude/commands, and bundled skills; a SkillTool lists skills and expands $ARGUMENTS templates. [@claim:clm_259d5738952c044e6d62eb05076b3cb496f5f5074538b22c426de2e9939724d6]
- Repository development practice: the README instructs running the workspace test suite with 'cargo test --workspace', optionally with '--features graph', or per-crate with 'cargo test -p cersei-tools' and similar. [@claim:clm_51939f3e0ab35c2240d6fbd7ca403c16c7400d8aa61742866f5d9de88b95365c]
- Using the SDK requires adding cersei (via git), tokio with the 'full' feature, and anyhow; the #[derive(Tool)] macro additionally needs async-trait and a cersei-tools dependency. [@claim:clm_6c5954b537d41eb74d6d9fae0c51a418d72da816264d745e43ded2facae57883]
- Sessions persist as append-only JSONL with tombstone soft-delete, and messages can be written and reloaded per session id. [@claim:clm_7c7b381fa6f40cdf53fb0762e308f25144a875960519f212a18e78b787a2873d]
- Memory is three-tier: flat markdown files scanned with frontmatter, a CLAUDE.md hierarchy merged into context, and an optional Grafeo graph layer supporting tagged store/recall queries with text fallback. [@claim:clm_99c766990a956f80d84f6e9a94579da166d052fe3c0f83715ed932e8bc0e1f96]
- The SDK exposes a runtime permission model with selectable policies including AllowAll, AllowReadOnly, DenyAll, RuleBased, and Interactive, plus interactive permissions with session caching in the CLI. [@claim:clm_9a43e031744baf7f41efecd557529d3510fe04ef902fa22b76dd03a752d11c6b]
- The workspace is organized into crates including cersei-types, cersei-provider, cersei-tools, cersei-tools-derive, cersei-agent, cersei-memory, cersei-hooks, cersei-mcp, a cersei facade crate, and abstract-cli. [@claim:clm_a21cb760f77cdf377656f6df7fb6c870c2a5ac597fc0e9ee5735a8837521aa16]
- Cersei is described as a Rust SDK exposing the building blocks of a coding agent — tool execution, LLM streaming, sub-agent orchestration, persistent memory, skills, and MCP integration — as composable library functions. [@claim:clm_a2c4be17e1ec17fd42aec0f2457c1802da1b4606e364f6a1a9ad8b0374109dfb]
- The repo ships agent-performance benchmarks: Terminal Bench 2.0 end-to-end coding tasks in Daytona sandboxes, LongMemEval recall accuracy vs Mastra/Zep/Supermemory with LLM-as-judge, and general-agent framework comparisons. [@claim:clm_b059bd89bafae3c4faf876bae440748168ab533584db7412cc64054d43773065]
- Agents are constructed via a builder API supporting provider, tools, model/temperature/max_tokens, system prompt, working directory, permission policy, memory, hooks, and context-management options. [@claim:clm_f8fa920e10027f871240ab9bc5cfcdf64ba8763a63c7b89c23d9523498455dc1]
- Sub-agent orchestration includes an AgentTool the model can spawn autonomously, a coordinator mode with parallel workers whose tools are filtered to prevent recursion, and a task system (TaskCreate through TaskOutput). [@claim:clm_fce70803312adb0ffbb1d477af132890972a30ef4725ca58b2ad07c16f118bfd]
<!-- rcw:end owner=source:src_20082b2e6b1b5933ab279e89d6c92ac2 block=evidence -->

## Researcher notes

