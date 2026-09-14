# podiom/podiom -- full detail

[Back to orientation](podiom.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/podiom/podiom/78025f74007775e4e161ab5632ee6a19f616fbc1/a58c745d296cbf3b.json](../../../wiki/dossiers/podiom/podiom/78025f74007775e4e161ab5632ee6a19f616fbc1/a58c745d296cbf3b.json)

## specifications (1 claim(s))

- [observation/documented] The repository points to docs/requirements/foundation.md as the authoritative foundation specification, at version v1.6. -- evidence: [README.md#L216-L235](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L216-L235) (`clm_ddf17bd31007bce13bf48a694c7530e45d25b953694cec5b3261ded43d03c321`)

## components (2 claim(s))

- [observation/documented] The podiomd daemon embeds the web SPA and uses pure-Go SQLite, so it needs no external web assets or cgo at runtime. -- evidence: [README.md#L182-L183](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L182-L183) (`clm_a93c12d1c4874d76db8dd80f5a75b5ca0fb7015820cb0ceee237d2f625173ee7`)
- [observation/documented] The layout includes a thin CLI client (cmd/podiom), a daemon combining web server, scheduler, and core (cmd/podiomd), internal packages, and a Svelte/Vite/TypeScript/Tailwind web UI built into podiomd. -- evidence: [README.md#L204-L210](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L204-L210) (`clm_4fdf498203856b650c8e8c6c71458f9585a556b079b559c5b904387b1cf8196c`)

## design-choices (1 claim(s))

- [observation/documented] Podiom is local-first: all runtime state lives under one overridable root ($PODIOM_HOME, defaulting to ~/.podiom/), and provider CLIs keep their native authentication and policy controls. -- evidence: [README.md#L212-L212](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L212-L212), [README.md#L190-L192](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L190-L192), [README.md#L110-L115](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L110-L115) (`clm_c7978f1f3f7cee387ead86ac6a5fc25a82c330faea9d2540c15615fc2ecab7fc`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md gives coding-agent guidelines—state assumptions before implementing, keep changes minimal and surgical, and turn tasks into verifiable, test-driven goals. -- evidence: [AGENTS.md#L21-L25](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L21-L25), [AGENTS.md#L49-L52](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L49-L52), [AGENTS.md#L11-L15](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L11-L15) (`clm_d951608442a7fa4b659a80ca9180397e52a05031934f3677b0430157672d26a7`)
- [observation/documented] Repository development practice: provider-specific logic must stay in registries and per-layer tables rather than branching on provider names, with a drift test (TestProviderKnowledgeStaysInRegistry) enforcing this boundary. -- evidence: [AGENTS.md#L67-L67](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L67-L67), [AGENTS.md#L71-L77](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L71-L77), [AGENTS.md#L91-L95](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L91-L95) (`clm_6c512f6c94e14bf7939ee8a362cc21b6597c9b0a21d07b62cc04e3c88651d819`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Podiom does not replace the provider runtime; it shells out to the native claude and codex CLIs and reuses their models, MCP servers, tools, skills, and authentication. -- evidence: [README.md#L41-L43](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L41-L43) (`clm_fb975e63c4deff15c7cbd8230e1d99226cd9ed3b8423ea3a2c574c84df73bd52`)
- [observation/documented] The web UI defaults to 127.0.0.1:8787, with bind address and port configurable via server.bind and server.port in config.yaml; a browser-native WebSocket endpoint at /api/ws is also documented. -- evidence: [README.md#L198-L200](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L198-L200), [README.md#L216-L235](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L216-L235) (`clm_66d8978da7faff08f30f285bd52810e420214e5d3982b88a2cf7b8d7e74aec09`)
- [observation/documented] Native iOS and Android mobile apps can connect to standalone daemons or an opt-in, API-only Home Assistant LAN endpoint, and the same core can run as a Home Assistant add-on or in a container. -- evidence: [README.md#L110-L115](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L110-L115) (`clm_c08851172ef66a32e702defd2c6498a685fa13b306492abbd9b6f965034fc58a`)

## memory-state (1 claim(s))

- [observation/documented] Podiom stores a canonical history for every session and can replay that history onto a fresh backing CLI session when the provider or profile changes. -- evidence: [README.md#L83-L86](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L83-L86) (`clm_5e8e3a9635acf947cdc2955879fa04f99cb272a4b432ede53b7e636e4efa1d5c`)

## orchestration (1 claim(s))

- [observation/documented] A goal gives one lead agent an outcome to own over days or weeks; the agent turns it into roadmap tasks and schedules, delegates work, and records periodic reviews with progress, evidence, and next steps. -- evidence: [README.md#L52-L59](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L52-L59), [README.md#L47-L50](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L47-L50) (`clm_fbd6e12dc15f991c4eadb946711ba4e393557d97a47701d38f23e4d0c5d1eeb8`)

## tools-permissions (1 claim(s))

- [observation/documented] Goals run deliberately autonomously: the lead agent and linked tasks or schedules run with full access and no per-action approval prompts, while tool activity is recorded on the goal timeline. -- evidence: [README.md#L61-L65](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L61-L65) (`clm_0464bd7c1caae66a132c5829bca2041f41dd5249ed25e236212e939ee8b18f60`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets developers already using Claude Code or OpenAI Codex locally who want persistent, reviewable agent work, recurring jobs, project context, and an audit trail in one workspace. -- evidence: [README.md#L119-L125](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L119-L125) (`clm_8040fb01daba8a75b63cd13f5668dd58ccb3ab9b1192368a0c4adbe336e8d767`)

