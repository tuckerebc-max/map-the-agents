# junkyard22/orca -- full detail

[Back to orientation](orca.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/junkyard22/orca/115d36b6cf5108b834cb24377ee5aea2a8a2c835/91cfee230c8891fa.json](../../../wiki/dossiers/junkyard22/orca/115d36b6cf5108b834cb24377ee5aea2a8a2c835/91cfee230c8891fa.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The runtime is organized as packages: benson-core (intent parsing), orca-core (runtime, event bus, SQLite persistence), maestro-core (role routing), pappy-core (QC verdicts), miranda-core (compliance gate), workbench-core (tool execution), and dewey-core (context store). -- evidence: [ARCHITECTURE.md#L32-L45](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L32-L45), [README.md#L88-L95](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L88-L95) (`clm_db101c06b220ca423ece0da336cf784530718a49b4604c5ad283184a3281a9b5`)

## design-choices (1 claim(s))

- [observation/documented] Roles include brain (decompose/route), strong_model, cheap_model, reviewer, narrator, planner_deep, debugger, reader, and vision; several roles are optional with documented fallbacks (e.g. planner_deep falls back to brain). -- evidence: [ARCHITECTURE.md#L11-L28](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L11-L28) (`clm_be3a0061485e4445bf9f578396e641edf67870d25d0fc6ef14f1bc3a95162984`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: ARCHITECTURE.md directs contributors to run a contract-check checklist before coding tasks touching orchestration, LLM paths, gates, QC, or role contracts, and mandates that agent-loop changes go only in packages/agent-loop-core. -- evidence: [ARCHITECTURE.md#L3-L7](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L3-L7), [ARCHITECTURE.md#L150-L157](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L150-L157) (`clm_961c74e6d9aced6bca3ea111c029bbc38b7782e70c1c09d365ce0b800b7b0811`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] MCP servers are declared in orca-settings.json under mcpServers[] with stdio transport; by default each server's tools are namespaced with a ${id}_ prefix to avoid collisions. -- evidence: [ARCHITECTURE.md#L120-L120](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L120-L120), [ARCHITECTURE.md#L114-L116](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L114-L116), [ARCHITECTURE.md#L174-L175](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L174-L175) (`clm_8aa0e30eb1b671167cefb24112324b8f7a2653d7e081512d05752e8e8b51fc0d`)
- [observation/documented] The desktop composer's Cargo tray accepts /repo, /file, /task, /connect, /context, /status commands plus @repo/@file/@task/@connector references, storing resources as typed references rather than raw contents. -- evidence: [ARCHITECTURE.md#L56-L59](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L56-L59), [README.md#L37-L42](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L37-L42), [ARCHITECTURE.md#L63-L73](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L63-L73) (`clm_535e1bfb1eab9bace3ae8c248b38fb7a67f3e9f44a911fe520ad1305fce40421`)
- [observation/documented] The product ships two frontends: an Electron desktop GUI (settings UI, chat view, session history) and a CLI runner that accepts prompts as arguments or via stdin piping. -- evidence: [ARCHITECTURE.md#L49-L52](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L49-L52), [README.md#L46-L50](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L46-L50), [README.md#L54-L56](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L54-L56) (`clm_694d6565274dc346fd837da59454ac7a77ec868ab0c740616abdab1ca043a6b7`)

## memory-state (1 claim(s))

- [observation/documented] Dewey persists a session-independent typed ContextManifest in ~/.orca/userContext.json storing resource locators and labels, never raw file or connector contents; raw contents load only via explicitly permitted tool calls. -- evidence: [ARCHITECTURE.md#L63-L73](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L63-L73), [ARCHITECTURE.md#L75-L77](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L75-L77) (`clm_801c52babd80e87168e314d0880b38a03cac435dd4c3decaff5f09a3a29f609c`)

## orchestration (1 claim(s))

- [observation/documented] The pipeline routes user input through Benson (intent parsing) to an Orca Runtime that orchestrates Maestro role routing, Pappy QC (PASS/WARN/FAIL), and Miranda compliance with a repair loop. -- evidence: [README.md#L7-L23](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L7-L23), [ARCHITECTURE.md#L11-L28](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L11-L28) (`clm_faaffa4602291bda137cbc7b1805486c72599f759b38ee556bebde40da8255c8`)

## tools-permissions (3 claim(s))

- [observation/documented] Role tool access is capability-scoped: tools resolve into named groups (filesystem-read/write, shell, github-read/write, web, documentation), and unclassifiable tool names are excluded from every role with no allow-by-default fallback. -- evidence: [ARCHITECTURE.md#L179-L182](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L179-L182), [ARCHITECTURE.md#L184-L193](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L184-L193) (`clm_fb09015479d39d329ec53cea10d07167f66958c77d25402e26aacec6bd385943`)
- [observation/documented] Task permissions can only add filesystem-write or shell capabilities, and when both fileWrite and shellExec are false the runtime removes write, shell, and github-write groups regardless of role baseline. -- evidence: [ARCHITECTURE.md#L215-L220](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L215-L220) (`clm_15fa2933e27c06a6d714e47105d6b91de091d2898f5d847455d8a4f98e0e28cb`)
- [observation/documented] Miranda's before_tool_run gate checks calls against allowedTools and the runtime enforces taskSpec.permissions.toolsAllowed uniformly for MCP tools; filtered tools' schemas are never serialized into prompts. -- evidence: [ARCHITECTURE.md#L233-L239](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L233-L239), [ARCHITECTURE.md#L258-L260](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L258-L260) (`clm_c0717e38f5552f9a7e4dd2b615590b307cc5dcc7008916ef9e81e914cdcdfa19`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] LLM providers are configurable via env: OpenRouter (OPENROUTER_API_KEY) or local Ollama (base URL and model), with role-to-model mappings in orca-settings.json. -- evidence: [README.md#L71-L71](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L71-L71), [README.md#L75-L79](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L75-L79), [README.md#L64-L69](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/README.md#L64-L69) (`clm_7aefcefb2fb27703cfa27afeb5109acce9b9c2443bf02780a24db51691efd7a0`)

## limitations (1 claim(s))

- [observation/documented] The desktop adapter still retains an inline agent loop as its primary path pending full unification with the shared agent-loop-core package, per the architecture doc's stated current state. -- evidence: [ARCHITECTURE.md#L159-L160](https://github.com/junkyard22/Orca/blob/115d36b6cf5108b834cb24377ee5aea2a8a2c835/ARCHITECTURE.md#L159-L160) (`clm_19d82156d2fc3d870135b0b41cd29afb4535b3a1ef4fbd842e133e3376dc68bb`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

