---
access: public
aliases: []
claim_ids:
- clm_127700f585034991b356ad29b60fb4c5895d73b34dd7612bc3079255ac3fa1d1
- clm_17e893c41e08af7032f8429ea4bd27f5d49e1eadecccd169cf969de4641d44f2
- clm_1b1b31071df892a96289d4ceea6529af9dfbc096aebc5b9ab78c8f4bd5d28b3a
- clm_9270cb5fb29fcc0e467df944eaf2122c6462a339e160c1ca1c563f431779964d
- clm_aea05da35046246c2f721a51cfbfed5efbe066c3dfdaaafa8ea41e8e5870ce7d
- clm_b686b3f033fa59ad286a091b7f01439da009f9f762b38a1b64351dfb3983a6bb
- clm_d4ad4cd1b94c3012733955d99dd82a21f8f0875fef20ad80790583fe909b6e8d
- clm_e74f931c9a6d1e62e1f81d1f23405e40d74d5db5b40e912dd38203a1e69203b9
- clm_f203f68e90f4b4e15d9f4120e9fd13c032dd65ca1f96adce5796f4aee8eb7f12
maturity: draft
page_id: pg_ea6d7d1331075ba4876cab9833543edb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b191ee00f9ea50ad8fbb33b99f1d1721
title: Kimi-K2-7/kimi-K2.7/llms.txt @ eb185473ccb4
updated_at: '2026-09-14T04:03:27Z'
---

# Kimi-K2-7/kimi-K2.7/llms.txt @ eb185473ccb4

<!-- rcw:begin owner=source:src_b191ee00f9ea50ad8fbb33b99f1d1721 block=evidence -->
- Documented features include a Hyper-Parallel Browser, MCP Hive toolsets per agent, Swarm Bridge backend integration, ThoughtStream reasoning visualization, Local Token Optimizer, Data Fusion Engine, and Multimodal Swarm Vision. [@claim:clm_127700f585034991b356ad29b60fb4c5895d73b34dd7612bc3079255ac3fa1d1]
- The Swarm Bridge exposes an Anthropic/OpenAI-compatible API so the swarm can serve as a backend for Claude Code, Cursor, or OpenClaw, per the documentation. [@claim:clm_17e893c41e08af7032f8429ea4bd27f5d49e1eadecccd169cf969de4641d44f2]
- The product is described as a native Windows and macOS desktop app coordinating up to 300 parallel AI sub-agents, powered by Moonshot AI's Kimi K2.7 Code model. [@claim:clm_1b1b31071df892a96289d4ceea6529af9dfbc096aebc5b9ab78c8f4bd5d28b3a]
- The documentation cites benchmark figures for the underlying model: 81.1% on MCPMark Verified versus Claude Opus 4.8's 76.4%, and 62.0 on Kimi Code Bench v2, up from K2.6's 50.9. [@claim:clm_9270cb5fb29fcc0e467df944eaf2122c6462a339e160c1ca1c563f431779964d]
- Repository development practice: the docs suggest building from source to verify release integrity, and the repository is MIT-licensed with source, releases, and issues hosted on GitHub. [@claim:clm_aea05da35046246c2f721a51cfbfed5efbe066c3dfdaaafa8ea41e8e5870ce7d]
- The docs describe a proprietary 'PARL' coordination layer for sub-agent synergy and 'Critical Steps' routing that auto-detects critical task nodes and allocates compute there, reportedly cutting runtime up to 80%. [@claim:clm_b686b3f033fa59ad286a091b7f01439da009f9f762b38a1b64351dfb3983a6bb]
- Target audiences named are developers doing whole-repo agentic coding, researchers and marketers needing parallel data gathering, investors, and users of Claude Code/Cursor/OpenClaw seeking a cheaper backend. [@claim:clm_d4ad4cd1b94c3012733955d99dd82a21f8f0875fef20ad80790583fe909b6e8d]
- The app depends on Moonshot AI's Kimi K2.7 Code model (1T-parameter MoE, ~32B active per token, 256K context, open weights on Hugging Face), and Swarm mode routes requests through a built-in proxy pool. [@claim:clm_e74f931c9a6d1e62e1f81d1f23405e40d74d5db5b40e912dd38203a1e69203b9]
- The app is positioned as a one-click installer requiring no terminal, with heavy computation on a cloud cluster while the desktop acts as orchestrator (8GB RAM stated as sufficient). [@claim:clm_f203f68e90f4b4e15d9f4120e9fd13c032dd65ca1f96adce5796f4aee8eb7f12]
<!-- rcw:end owner=source:src_b191ee00f9ea50ad8fbb33b99f1d1721 block=evidence -->

## Researcher notes

