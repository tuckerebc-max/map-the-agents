# matteraiorg/orbital-extension -- full detail

[Back to orientation](orbital-extension.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/matteraiorg/orbital-extension/ac82a92110acff133f618853b5a2318a3be858c8/9ba36631393dad88.json](../../../wiki/dossiers/matteraiorg/orbital-extension/ac82a92110acff133f618853b5a2318a3be858c8/9ba36631393dad88.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The product exposes agentic tools including fileEdit, executeCommand, read_multi_file, writeToFile, searchFiles, web_search, web_fetch, newTask, updateTodoList, and code-structure analysis tools. -- evidence: [README.md#L71-L73](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L71-L73), [README.md#L66-L67](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L66-L67), [README.md#L54-L54](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L54-L54), [README.md#L77-L78](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L77-L78), [README.md#L58-L62](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L58-L62) (`clm_30d6db484c0d1dfe20f3fb86ed7b3215778b9223972086e987c4769f31dfd047`)
- [observation/documented] A generate_file native tool produces file artifacts (PDF, DOCX, PPTX, XLSX, CSV, MD, TXT, HTML) via the MatterAI backend, holding binaries in memory until the user explicitly saves to the Downloads folder. -- evidence: [CHANGELOG.md#L69-L69](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L69-L69) (`clm_48b917c6e30b3d5d9bca9f7730e80d83ca628f6b0092b16634f5e37ba31cf7f0`)

## design-choices (3 claim(s))

- [observation/documented] Models are fetched from the backend /v1/models endpoint and registered into the client registry, refreshing on window focus, via a refresh button, and through a 10-minute background poller. -- evidence: [CHANGELOG.md#L23-L23](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L23-L23) (`clm_5c41c45eff133494a955862ad2a3fcc3b5c05073676bd61a8287a4614a9f5524`)
- [observation/documented] File-edit tools require old_string to match exactly one location copied verbatim from a current read, and replace_all must be set intentionally after verifying all occurrences should change. -- evidence: [CHANGELOG.md#L108-L111](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L108-L111) (`clm_b97dcb4745b89dc4e389bb8187538b90c523817ba4a56b4c74f72b7e1ea422f5`)
- [observation/documented] search_files is ripgrep-first with FFF as fallback, one-shot with no cursor parameter, and results capped at 100 with pages telling the model to refine the pattern instead of paginating. -- evidence: [CHANGELOG.md#L125-L133](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L125-L133), [CHANGELOG.md#L40-L45](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L40-L45) (`clm_20e3e817d292ded8844cc4ba33bfb41d055ac7cbeb21295d6a5470f08ec7094e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the axon-code repository and run pnpm install to set up the development environment, and the README points to a CONTRIBUTING.md guide. -- evidence: [README.md#L168-L168](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L168-L168), [README.md#L174-L174](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L174-L174), [README.md#L177-L178](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L177-L178) (`clm_9651deec57cd27f2ecd21bb4046a33f2ae3c47e527471a4333b0eba385fef461`)

## skills-patterns (1 claim(s))

- [observation/documented] A /create-skill command lets users describe a workflow in plain language and creates or updates a reusable skill under .orb/skills/<skill-name>/ with supporting scripts and assets. -- evidence: [CHANGELOG.md#L201-L201](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L201-L201) (`clm_4a6639708a628936ef72a8b27396a72bb4fe2813e0887b9352946354e110d577`)

## interfaces (1 claim(s))

- [observation/documented] Orbital ships as a dedicated AI-first IDE plus extensions for VS Code, Cursor, and Windsurf; JetBrains IDEs and a CLI are listed as coming soon. -- evidence: [README.md#L45-L50](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L45-L50) (`clm_121f0f46667a72276e0c3450521179690c97553c2e15f35680fe7549075d5d04`)

## memory-state (1 claim(s))

- [observation/documented] AGENTS.md project memory is loaded from the repo-level .orb/ directory (alongside project root and legacy .orbital/), shared between the IDE extension and the OrbCode CLI. -- evidence: [CHANGELOG.md#L209-L212](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L209-L212) (`clm_57396ddeffff09e57df546c57b442ba66a1e5bc0b40e1bc5eff2bd86df3eb00f`)

## orchestration (1 claim(s))

- [observation/documented] Independent read-only tools (read_file, search_files, list_files, list_code_definition_names, codebase_search, lsp) run concurrently up to 4 at a time, with results committed in model order; mutating and interactive tools stay serialized. -- evidence: [CHANGELOG.md#L36-L36](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/CHANGELOG.md#L36-L36) (`clm_b5262fbb4f45509d498fda953b33db229247b4f4756b6c0fcb5ba7e1fecdfa35`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The model catalog is served dynamically from the MatterAI backend, so new models appear in the selector without an extension update. -- evidence: [README.md#L88-L88](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L88-L88) (`clm_779ba9109098addc5feddbe48774ce9bc99d5f80a51c570ca4ac5eae3acf85cc`)

## limitations (1 claim(s))

- [observation/documented] Per the README, JetBrains IDE support and a command-line interface are marked 'Coming Soon', and tab auto-complete is listed as coming soon. -- evidence: [README.md#L45-L50](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L45-L50), [README.md#L29-L37](https://github.com/MatterAIOrg/Orbital-Extension/blob/ac82a92110acff133f618853b5a2318a3be858c8/README.md#L29-L37) (`clm_4a0d8cf616c8bbc8f4df42be4c90555bc136d49635583e21121fae4aa47e5272`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

