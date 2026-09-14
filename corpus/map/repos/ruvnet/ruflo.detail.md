# ruvnet/ruflo -- full detail

[Back to orientation](ruflo.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/ruvnet/ruflo/b02c0cacec225deea01f586b66a9694393369432/43f85fd862fff196.json](../../../wiki/dossiers/ruvnet/ruflo/b02c0cacec225deea01f586b66a9694393369432/43f85fd862fff196.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The README catalogs 35 plugins across categories including core/orchestration, memory, intelligence, testing, security, and domain-specific (e.g. ruflo-swarm, ruflo-rag-memory, ruflo-neural-trader). -- evidence: [README.md#L83-L84](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L83-L84), [README.md#L109-L115](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L109-L115), [README.md#L99-L105](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L99-L105), [README.md#L88-L95](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L88-L95), [README.md#L119-L124](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L119-L124), [README.md#L128-L131](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L128-L131), [README.md#L160-L164](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L160-L164) (`clm_9947260fb2645b1bd1fdd2381a9874cf85a24cec68076dab42bf315c219d9f42`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: CLAUDE.local.md documents maintainer steps for updating the IPFS/Pinata plugin registry (fetch registry, edit entries, pin via Pinata API, update LIVE_REGISTRY_CID) and warns never to hardcode API keys or commit .env. -- evidence: [CLAUDE.local.md#L25-L25](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/CLAUDE.local.md#L25-L25), [CLAUDE.local.md#L19-L23](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/CLAUDE.local.md#L19-L23) (`clm_176eff959fd3209e10242289aba17b70941af137da20ddaf24383bb71e371cbc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Ruflo exposes a CLI (npx ruflo) and an MCP server; the README shows registering it in Claude Code via 'claude mcp add claude-flow -- npx ruflo@latest mcp start'. -- evidence: [README.md#L196-L197](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L196-L197) (`clm_54fbbe540ff43991766b97c2ac9c18b404f51aa3f62b7a746a5573880e71e60e`)
- [observation/documented] Two install paths exist: Claude Code plugins (slash commands, zero workspace files) versus full CLI init which scaffolds .claude/, .claude-flow/, CLAUDE.md, hooks, and an MCP server. -- evidence: [README.md#L60-L66](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L60-L66) (`clm_368cccabb9a6e034c593cb88ac731f155daffe26bf5cd75f1ef9b907ffa747d0`)
- [observation/documented] The ruflo-core plugin registers its own MCP server with namespaced tool names like mcp__plugin_ruflo-core_ruflo__memory_store, differing from the CLI-track bare tool names. -- evidence: [README.md#L81-L81](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L81-L81) (`clm_347620a1aae111431e019ceac8461e9108c8342e4265ddf9a5c493c4136f4b2c`)

## memory-state (1 claim(s))

- [observation/documented] Memory uses an HNSW-indexed AgentDB; the README cites measured ~1.9x faster at N=20k versus brute force with recall@10 near 0.99, noting ANN ties or loses at small N. -- evidence: [README.md#L203-L217](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L203-L217) (`clm_b3ae703a8c3388da567d8631d1e283a97569248acc465fd99f213b3f748dfc78`)

## orchestration (2 claim(s))

- [observation/documented] Swarm coordination supports hierarchical, mesh, and adaptive topologies with consensus, and the architecture diagram shows a Queen-led coordination layer above 100+ specialized agents. -- evidence: [README.md#L352-L374](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L352-L374), [README.md#L203-L217](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L203-L217) (`clm_60db2f3bc01d70d84f90d5ffeced1e6854c758e9968c3b3e75c41094a026e8d7`)
- [observation/documented] Agent federation lets agents on different machines discover, authenticate (mTLS + ed25519), and exchange work, with PII stripped from outbound messages and per-trust-level policies (BLOCK, REDACT, HASH, PASS). -- evidence: [README.md#L284-L284](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L284-L284), [README.md#L293-L299](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L293-L299) (`clm_690fbaed7928b895e91d8b291672cd5aa9ec829d414cdaf04c6d3652f60b3b1d`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A SOTA comparator benchmark suite compares ruflo against LangGraph, AutoGen, and CrewAI on metrics like cold start, single turn, and RSS, with published matrix JSON for darwin and linux. -- evidence: [README.md#L384-L391](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L384-L391), [README.md#L393-L393](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L393-L393) (`clm_fa00bbe48e779308ee42f9c3cbbc11871d6ed4e73d9913eba53a2c1f1e418bec`)

## dependencies (1 claim(s))

- [observation/documented] The runtime supports multiple LLM providers — Claude, GPT, Gemini, Cohere, and Ollama — with smart routing and failover. -- evidence: [README.md#L203-L217](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L203-L217), [README.md#L336-L345](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L336-L345) (`clm_9d9601bbc8c2a3e3ff995385bea59953034b5470c5396c356949ff84c4b3c9f1`)

## limitations (2 claim(s))

- [observation/documented] The roadmap states four CI-skipped integration tests cover real production bugs (HybridBackend persistence, SwarmCoordinator error propagation, scaleAgents direction, workflow resume), and releases since skipping have carried these bugs. -- evidence: [docs/IMPROVEMENT-ROADMAP.md#L15-L15](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/docs/IMPROVEMENT-ROADMAP.md#L15-L15) (`clm_14ee3e56f4074fdf31e5857e2aec10192b52a596949090bb3701e1795cedd821`)
- [observation/documented] Per the roadmap, memory sub-commands hard-code the SQLite path to ~/.swarm/memory.db and ignore 'memory init -p', forcing the DB onto the system drive on Windows and sharing one DB across projects. -- evidence: [docs/IMPROVEMENT-ROADMAP.md#L54-L54](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/docs/IMPROVEMENT-ROADMAP.md#L54-L54) (`clm_117e4d32ff247221b5a8b9d5c93534bc73aa4d48f5103fcf485f027bb07fe331`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

