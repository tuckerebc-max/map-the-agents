---
access: public
aliases: []
claim_ids:
- clm_12d51da79cca6258d6bdcead0501445207a230da1473ff296b1658fc725cadfb
- clm_5b755d2d5c4dfc5642a3599e739e4b79e063d95f4e0e5639d93e6ff5937931eb
- clm_7339f8d9961d29657d3a874ee10528a3ccee764aa73bc3f3561efb95c4fd9cea
- clm_8220283b6f24daf8fa48bee41bdffcb9db8036298ee3188d63201bfaf39d9bbc
- clm_b39b57cee49e9ff1b17db2ac48e16e7a2b3d66fd2da8d38db51a63fe42cb2f02
- clm_d790359331b940c57cec521de6257da3d43a38b8feff8d4d171fe6f4e74db636
maturity: draft
page_id: pg_7ae9b7d087f9569a801b270806f32526
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_51f3220a2ed759aeba46239e52e7d750
title: catatafishen/agentbridge/docs/ARCHITECTURE.md @ 124f7c082dc3
updated_at: '2026-09-14T03:40:39Z'
---

# catatafishen/agentbridge/docs/ARCHITECTURE.md @ 124f7c082dc3

<!-- rcw:begin owner=source:src_51f3220a2ed759aeba46239e52e7d750 block=evidence -->
- The plugin communicates with agent CLIs over the Agent Client Protocol (JSON-RPC 2.0 via stdin/stdout); the MCP server JAR receives tool calls via stdio and forwards them to the PSI bridge over HTTP POST on localhost. [@claim:clm_12d51da79cca6258d6bdcead0501445207a230da1473ff296b1658fc725cadfb]
- The bridge port is shared via a file at ~/.copilot/psi-bridge.json, which the MCP server reads to reach the in-IDE HTTP service. [@claim:clm_5b755d2d5c4dfc5642a3599e739e4b79e063d95f4e0e5639d93e6ff5937931eb]
- ActiveAgentManager is a project-level service that stores the active AgentProfile, owns the AbstractAgentClient, and handles client start/stop/restart/dispose. [@claim:clm_7339f8d9961d29657d3a874ee10528a3ccee764aa73bc3f3561efb95c4fd9cea]
- Agent clients extend AbstractAgentClient, which provides session management (create, prompt, cancel), model selection, event streaming, and connection lifecycle; ACP clients include CopilotClient, JunieClient, KiroClient, and OpenCodeClient. [@claim:clm_8220283b6f24daf8fa48bee41bdffcb9db8036298ee3188d63201bfaf39d9bbc]
- PsiBridgeService is a project-level HTTP server exposing 92 IntelliJ-native MCP tools; it starts on a dynamic localhost port and accesses PSI, VFS, Document API, and Git4Idea. [@claim:clm_b39b57cee49e9ff1b17db2ac48e16e7a2b3d66fd2da8d38db51a63fe42cb2f02]
- Tool permissions support three modes: deny (never execute), ask (prompt user for approval), and allow (execute without prompt); sensitive operations like force git push, shell commands, file deletions, and out-of-root operations always require approval. [@claim:clm_d790359331b940c57cec521de6257da3d43a38b8feff8d4d171fe6f4e74db636]
<!-- rcw:end owner=source:src_51f3220a2ed759aeba46239e52e7d750 block=evidence -->

## Researcher notes

