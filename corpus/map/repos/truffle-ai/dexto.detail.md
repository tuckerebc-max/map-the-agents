# truffle-ai/dexto -- full detail

[Back to orientation](dexto.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/truffle-ai/dexto/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/491bca189af9a968.json](../../../wiki/dossiers/truffle-ai/dexto/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/491bca189af9a968.json)

## specifications (1 claim(s))

- [observation/documented] Dexto is described as an agent harness that turns LLMs into reliable, stateful agents able to take actions, remember context, and recover from errors, with agents defined in YAML configuration files. -- evidence: [README.md#L456-L456](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L456-L456), [README.md#L54-L56](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L54-L56), [README.md#L41-L41](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L41-L41) (`clm_3e95222a72fbf753b3aafddb2f48b83666992f303bb7c7ab8d59f847c1d55793`)

## components (2 claim(s))

- [observation/documented] Storage is configurable with cache backends Redis or in-memory and database backends PostgreSQL, SQLite, or in-memory, plus session settings like maxSessions and sessionTTL. -- evidence: [README.md#L420-L423](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L420-L423), [README.md#L412-L418](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L412-L418), [README.md#L425-L427](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L425-L427) (`clm_9d5b6a343b2ec5aeb51a12adb44ec370da15884ea52e178035ff8afd6e99a260`)
- [observation/documented] An MCPManager class in @dexto/core connects to MCP servers, exposes tools, prompts, and resources, executes tools, and disconnects all servers. -- evidence: [README.md#L395-L398](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L395-L398), [README.md#L388-L393](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L388-L393), [README.md#L400-L401](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L400-L401), [README.md#L403-L404](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L403-L404), [README.md#L383-L384](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L383-L384) (`clm_7a4717280e90169f10c53337ceb2cd862d8d1632dc6635871d0202f03da8ba77`)

## design-choices (1 claim(s))

- [observation/documented] Agents are configuration-driven: each YAML file defines a unique agent combining LLM, MCP servers, system prompt, storage, and permissions, and reloading the file updates state, memory, and tools without code changes. -- evidence: [README.md#L456-L456](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L456-L456), [README.md#L482-L484](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L482-L484), [README.md#L54-L56](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L54-L56), [README.md#L460-L463](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L460-L463), [README.md#L471-L472](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L471-L472) (`clm_d88ce3f927fa09209176137e0fbf9e1f528555d0d10ea5170eb83f6a9fa18979`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Dexto offers multiple run modes: Web UI (default), interactive CLI, server mode exposing REST and SSE APIs, and MCP server mode over stdio, with Discord and Telegram example integrations. -- evidence: [README.md#L245-L245](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L245-L245), [README.md#L273-L273](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L273-L273), [README.md#L238-L243](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L238-L243) (`clm_12454d9f914ac15c638edc9d4253761c5e35eebbda588710d1574fff07b8d233`)
- [observation/documented] CLI options include -a/--agent, -m/--model, --auto-approve, --no-elicitation, --mode, and --port, plus commands such as setup, deploy, agents install/list, session management, and search. -- evidence: [README.md#L604-L610](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L604-L610), [README.md#L612-L619](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L612-L619) (`clm_31e8311b2b737c28cba4a2577f43e6685ca21e8d51d38f8dbaaf32af4680c13b`)
- [observation/documented] A TypeScript SDK (@dexto/core) exposes DextoAgent with methods for creating sessions, generating and streaming responses, sending multimodal text/image input, switching LLMs, and listing or deleting sessions. -- evidence: [README.md#L315-L317](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L315-L317), [README.md#L350-L353](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L350-L353), [README.md#L295-L298](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L295-L298), [README.md#L309-L313](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L309-L313), [README.md#L304-L307](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L304-L307), [README.md#L288-L290](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L288-L290) (`clm_73122a7ae74da3d2baf54c4648ec4899885204956f52307e655652c2f4a8392e`)
- [observation/documented] MCP servers are configured in agent YAML with stdio type, command, and args (e.g. filesystem or Puppeteer servers), and servers can be added via an MCP Store in the Web UI or /mcp CLI commands. -- evidence: [README.md#L181-L181](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L181-L181), [README.md#L170-L179](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L170-L179) (`clm_b84f0d65aff22e4d873362a8ab19b96afa2ae464604e295054b57333564329ef`)

## memory-state (2 claim(s))

- [observation/documented] A memory system stores persistent information (preferences, context, facts, learned patterns) across sessions, supports tagging and pinned memories auto-loaded into system prompts, and can be viewed or cleared via the Web UI. -- evidence: [docs/examples/memory.md#L56-L56](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/examples/memory.md#L56-L56), [docs/examples/memory.md#L42-L45](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/examples/memory.md#L42-L45), [docs/docs/guides/configuring-dexto/memory.md#L18-L23](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/docs/guides/configuring-dexto/memory.md#L18-L23), [docs/docs/guides/configuring-dexto/memory.md#L25-L25](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/docs/docs/guides/configuring-dexto/memory.md#L25-L25) (`clm_dcedf559b25d738e64ea1a39fb6d3e1e40d515707d7d347dd9b1adaeef6e7100`)
- [observation/documented] Conversations persist across restarts; the CLI supports continuing the last conversation (-c), resuming a specific session (-r), and searching history, and the SDK exposes session history and message search. -- evidence: [README.md#L205-L205](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L205-L205), [README.md#L208-L208](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L208-L208), [README.md#L350-L353](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L350-L353), [README.md#L201-L201](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L201-L201), [README.md#L355-L357](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L355-L357), [README.md#L211-L212](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L211-L212) (`clm_ed04f38c6759e649d2206f39992cfed8c0801ebfc25c1ce902940988b6d9ed52`)

## orchestration (1 claim(s))

- [observation/documented] Agents can spawn sub-agents via an agent-spawner tool with configurable allowedAgents, maxConcurrentAgents, and timeout; sub-agents run ephemerally, clean up after completion, and forward tool approvals to the parent. -- evidence: [README.md#L220-L225](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L220-L225), [README.md#L232-L232](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L232-L232) (`clm_63bf9a110b9d95ea5ca829f4d44624f3815aa58ca91950c627e7cc0143188cb8`)

## tools-permissions (1 claim(s))

- [observation/documented] Agent YAML supports a permissions block with manual or auto-approve modes and per-tool alwaysAllow policies; approved tools are remembered per session, and MCP mode requires --auto-approve and --no-elicitation since it runs non-interactively. -- evidence: [README.md#L187-L195](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L187-L195), [README.md#L269-L269](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L269-L269), [README.md#L197-L197](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L197-L197) (`clm_0f8d104e68117faceb6469c459ac95d7469566fa06144bc2463915a68841b0d3`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Documented LLM providers include OpenAI, Anthropic, Google, Groq, xAI, and Cohere; local options Ollama and node-llama-cpp (GGUF with GPU detection); plus AWS Bedrock, Vertex AI, OpenRouter, LiteLLM, and Glama gateways. -- evidence: [README.md#L517-L521](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L517-L521), [README.md#L510-L513](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L510-L513), [README.md#L503-L506](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L503-L506), [README.md#L492-L499](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L492-L499) (`clm_f74887bb6cb3adc4575d2e26847ee27c3fc2378ddc7672c76e55ce19a2f40971`)
- [observation/documented] The project is labeled Beta and licensed under Elastic License 2.0; installation is via a curl installer, a PowerShell script, or building from source with pnpm. -- evidence: [README.md#L102-L102](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L102-L102), [README.md#L11-L16](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L11-L16), [README.md#L105-L105](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L105-L105), [README.md#L678-L678](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L678-L678), [README.md#L108-L110](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L108-L110) (`clm_f1ab926ae927fcdbf84a288fc71297c74a8a78d83833725cb36546cd9b878aff`)

## limitations (1 claim(s))

- [observation/documented] The README states anonymous usage telemetry (commands used, execution time, errors, OS/Node info, models used) is collected and can be disabled by setting DEXTO_ANALYTICS_DISABLED=1. -- evidence: [README.md#L640-L644](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L640-L644), [README.md#L648-L648](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L648-L648), [README.md#L638-L638](https://github.com/truffle-ai/dexto/blob/a910e0ef36f2a538c0bb0d4f17e83c4ec8293735/README.md#L638-L638) (`clm_4f2b947c1585d3d53ee5490d9a89c6af08f94c78f7f2be837efa98d6b61912fd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

