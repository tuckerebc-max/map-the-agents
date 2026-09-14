---
access: public
aliases: []
claim_ids:
- clm_0f8d104e68117faceb6469c459ac95d7469566fa06144bc2463915a68841b0d3
- clm_12454d9f914ac15c638edc9d4253761c5e35eebbda588710d1574fff07b8d233
- clm_31e8311b2b737c28cba4a2577f43e6685ca21e8d51d38f8dbaaf32af4680c13b
- clm_3e95222a72fbf753b3aafddb2f48b83666992f303bb7c7ab8d59f847c1d55793
- clm_4f2b947c1585d3d53ee5490d9a89c6af08f94c78f7f2be837efa98d6b61912fd
- clm_63bf9a110b9d95ea5ca829f4d44624f3815aa58ca91950c627e7cc0143188cb8
- clm_73122a7ae74da3d2baf54c4648ec4899885204956f52307e655652c2f4a8392e
- clm_7a4717280e90169f10c53337ceb2cd862d8d1632dc6635871d0202f03da8ba77
- clm_9d5b6a343b2ec5aeb51a12adb44ec370da15884ea52e178035ff8afd6e99a260
- clm_b84f0d65aff22e4d873362a8ab19b96afa2ae464604e295054b57333564329ef
- clm_d88ce3f927fa09209176137e0fbf9e1f528555d0d10ea5170eb83f6a9fa18979
- clm_ed04f38c6759e649d2206f39992cfed8c0801ebfc25c1ce902940988b6d9ed52
- clm_f1ab926ae927fcdbf84a288fc71297c74a8a78d83833725cb36546cd9b878aff
- clm_f74887bb6cb3adc4575d2e26847ee27c3fc2378ddc7672c76e55ce19a2f40971
maturity: draft
page_id: pg_cf66289ea6c059edaf6c9ea96f217814
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fcf32ae43a5657cab30fb11696cfa004
title: truffle-ai/dexto/README.md @ a910e0ef36f2
updated_at: '2026-09-14T03:20:56Z'
---

# truffle-ai/dexto/README.md @ a910e0ef36f2

<!-- rcw:begin owner=source:src_fcf32ae43a5657cab30fb11696cfa004 block=evidence -->
- Agent YAML supports a permissions block with manual or auto-approve modes and per-tool alwaysAllow policies; approved tools are remembered per session, and MCP mode requires --auto-approve and --no-elicitation since it runs non-interactively. [@claim:clm_0f8d104e68117faceb6469c459ac95d7469566fa06144bc2463915a68841b0d3]
- Dexto offers multiple run modes: Web UI (default), interactive CLI, server mode exposing REST and SSE APIs, and MCP server mode over stdio, with Discord and Telegram example integrations. [@claim:clm_12454d9f914ac15c638edc9d4253761c5e35eebbda588710d1574fff07b8d233]
- CLI options include -a/--agent, -m/--model, --auto-approve, --no-elicitation, --mode, and --port, plus commands such as setup, deploy, agents install/list, session management, and search. [@claim:clm_31e8311b2b737c28cba4a2577f43e6685ca21e8d51d38f8dbaaf32af4680c13b]
- Dexto is described as an agent harness that turns LLMs into reliable, stateful agents able to take actions, remember context, and recover from errors, with agents defined in YAML configuration files. [@claim:clm_3e95222a72fbf753b3aafddb2f48b83666992f303bb7c7ab8d59f847c1d55793]
- The README states anonymous usage telemetry (commands used, execution time, errors, OS/Node info, models used) is collected and can be disabled by setting DEXTO_ANALYTICS_DISABLED=1. [@claim:clm_4f2b947c1585d3d53ee5490d9a89c6af08f94c78f7f2be837efa98d6b61912fd]
- Agents can spawn sub-agents via an agent-spawner tool with configurable allowedAgents, maxConcurrentAgents, and timeout; sub-agents run ephemerally, clean up after completion, and forward tool approvals to the parent. [@claim:clm_63bf9a110b9d95ea5ca829f4d44624f3815aa58ca91950c627e7cc0143188cb8]
- A TypeScript SDK (@dexto/core) exposes DextoAgent with methods for creating sessions, generating and streaming responses, sending multimodal text/image input, switching LLMs, and listing or deleting sessions. [@claim:clm_73122a7ae74da3d2baf54c4648ec4899885204956f52307e655652c2f4a8392e]
- An MCPManager class in @dexto/core connects to MCP servers, exposes tools, prompts, and resources, executes tools, and disconnects all servers. [@claim:clm_7a4717280e90169f10c53337ceb2cd862d8d1632dc6635871d0202f03da8ba77]
- Storage is configurable with cache backends Redis or in-memory and database backends PostgreSQL, SQLite, or in-memory, plus session settings like maxSessions and sessionTTL. [@claim:clm_9d5b6a343b2ec5aeb51a12adb44ec370da15884ea52e178035ff8afd6e99a260]
- MCP servers are configured in agent YAML with stdio type, command, and args (e.g. filesystem or Puppeteer servers), and servers can be added via an MCP Store in the Web UI or /mcp CLI commands. [@claim:clm_b84f0d65aff22e4d873362a8ab19b96afa2ae464604e295054b57333564329ef]
- Agents are configuration-driven: each YAML file defines a unique agent combining LLM, MCP servers, system prompt, storage, and permissions, and reloading the file updates state, memory, and tools without code changes. [@claim:clm_d88ce3f927fa09209176137e0fbf9e1f528555d0d10ea5170eb83f6a9fa18979]
- Conversations persist across restarts; the CLI supports continuing the last conversation (-c), resuming a specific session (-r), and searching history, and the SDK exposes session history and message search. [@claim:clm_ed04f38c6759e649d2206f39992cfed8c0801ebfc25c1ce902940988b6d9ed52]
- The project is labeled Beta and licensed under Elastic License 2.0; installation is via a curl installer, a PowerShell script, or building from source with pnpm. [@claim:clm_f1ab926ae927fcdbf84a288fc71297c74a8a78d83833725cb36546cd9b878aff]
- Documented LLM providers include OpenAI, Anthropic, Google, Groq, xAI, and Cohere; local options Ollama and node-llama-cpp (GGUF with GPU detection); plus AWS Bedrock, Vertex AI, OpenRouter, LiteLLM, and Glama gateways. [@claim:clm_f74887bb6cb3adc4575d2e26847ee27c3fc2378ddc7672c76e55ce19a2f40971]
<!-- rcw:end owner=source:src_fcf32ae43a5657cab30fb11696cfa004 block=evidence -->

## Researcher notes

