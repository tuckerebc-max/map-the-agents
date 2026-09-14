# dinoanderson/qwen_cli_coder -- full detail

[Back to orientation](qwen_cli_coder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dinoanderson/qwen_cli_coder/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/6cb863d3cc58a3c7.json](../../../wiki/dossiers/dinoanderson/qwen_cli_coder/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/6cb863d3cc58a3c7.json)

## specifications (2 claim(s))

- [observation/documented] The project is a community-maintained fork of Google's Gemini CLI, modified to work with Qwen models from Alibaba Cloud, under Apache License 2.0. -- evidence: [README.md#L13-L13](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L13-L13), [README.md#L15-L17](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L15-L17), [README.md#L485-L488](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L485-L488), [README.md#L5-L5](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L5-L5) (`clm_28430d8cb72ff365311fcfa9ae73ccb9a5c856b8e88266acef4ae085f54ae318`)
- [observation/documented] Supported models include qwen-turbo-latest (1M context), qwen3-235b-a22b (131k context), and qwen-vl-plus-latest (32k context, vision). -- evidence: [README.md#L134-L137](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L134-L137) (`clm_d06dfa68b325af753709850eeda2cef7e9b67ba7491afc6559bdda0b7b68d2ca`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Architecture splits a user-facing CLI package (packages/cli) from a backend core package (packages/core) that handles API calls, prompt construction, and tool execution. -- evidence: [docs/architecture.md#L9-L9](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L9-L9), [docs/architecture.md#L21-L27](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L21-L27), [docs/architecture.md#L29-L31](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L29-L31) (`clm_da2338b44673550ad1b62d8095e5089bcd522cc178bc0a8b2cdb0fd18c5afe46`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md for guidelines specific to this community fork. -- evidence: [README.md#L494-L494](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L494-L494) (`clm_8cd86934207a9f1854c5fa293eb105640d825bed31e9df9b9ea13ed39fa0f262`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI provides slash commands including /model for interactive model switching, /lang for English/Chinese localization, /theme, /auth, /mcp, and /tools. -- evidence: [README.md#L151-L155](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L151-L155), [README.md#L158-L162](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L158-L162), [README.md#L144-L148](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L144-L148), [README.md#L192-L195](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L192-L195) (`clm_f3b6c8a65fb217e01956562fe6c38e7035c5121894fffd7b25adf4bd6fb43767`)
- [observation/documented] An Assistant Mode launched via 'node bundle/qwen.js --assistant' opens a browser chat interface with file upload, session-based storage, and dark mode detection. -- evidence: [README.md#L40-L41](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L40-L41), [README.md#L45-L51](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L45-L51) (`clm_d45d54c32dc5b65f44055756fcb7b91ce880cfdf2a82f5bd33f7e1ce2465918e`)
- [observation/documented] MCP servers are configured via mcpServers settings; same-named tools from multiple servers are prefixed with the server alias to avoid conflicts. -- evidence: [docs/cli/configuration.md#L117-L149](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L117-L149) (`clm_2e5de9ecaf5b2e1081e5fc58deca443b55b93e3f6ae545a826150b128686b37e`)

## memory-state (2 claim(s))

- [observation/documented] Configuration uses ~/.qwen/settings.json (user) and .qwen/settings.json (project, overriding user), with a five-layer precedence ending in command-line arguments. -- evidence: [docs/cli/configuration.md#L9-L13](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L9-L13), [docs/cli/configuration.md#L19-L24](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L19-L24) (`clm_4c76e9b1001fa64c9bca01293770aa7eb012d21325439fe7f8873bd98b62e68d`)
- [observation/documented] A checkpointing feature (disabled by default) can save and restore conversation and file states, enabling a /restore command when enabled. -- evidence: [docs/cli/configuration.md#L153-L156](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L153-L156) (`clm_6cd3834602276491824aa1eae9a8d624e08eaf935b24e454b46271236679968e`)

## orchestration (1 claim(s))

- [observation/documented] Multi-agent tools (spawn_sub_agent, delegate_task, aggregate_results) support up to 5 concurrent agents with priority-based scheduling and multiple aggregation formats. -- evidence: [README.md#L263-L266](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L263-L266), [README.md#L268-L272](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L268-L272) (`clm_f20e44e77791b3083b5444559fb2aee65000939a8937166362bd2459da26d5e1`)

## tools-permissions (3 claim(s))

- [observation/documented] Tools that modify the filesystem or run shell commands require user approval before execution; read-only operations may proceed without confirmation. -- evidence: [docs/architecture.md#L37-L50](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L37-L50) (`clm_1613ed4107f98da202d1486a05090d0d29a4bffaae3d06ccd4a0de860d7dbcba`)
- [observation/documented] Settings support coreTools and excludeTools lists to restrict which built-in tools the model can use, plus an autoAccept option to skip confirmation for safe tools. -- evidence: [docs/cli/configuration.md#L78-L80](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L78-L80), [docs/cli/configuration.md#L84-L86](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L84-L86), [docs/cli/configuration.md#L72-L74](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L72-L74) (`clm_4ae8bc2bf1ebacf4a76ea5354c118c460b99f65b67ea6ee2b91b989d19fb2016`)
- [observation/documented] A sandbox setting (default false) enables tool execution inside a pre-built Qwen-cli-sandbox Docker image, and MCP server configs can set a trust flag bypassing tool confirmations. -- evidence: [docs/cli/configuration.md#L117-L149](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L117-L149), [docs/cli/configuration.md#L96-L98](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L96-L98) (`clm_5b3a2e05f63d08c11182108e4872e10ebfcdae7df1395e0b3e0e421fc3f3cfa5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requires Node.js 18 or higher; authentication uses a DashScope API key via DASHSCOPE_API_KEY or QWEN_API_KEY with region-specific QWEN_BASE_URL endpoints. -- evidence: [README.md#L107-L109](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L107-L109), [README.md#L101-L105](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L101-L105), [README.md#L85-L85](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L85-L85), [README.md#L111-L113](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L111-L113) (`clm_df4e9ba854adec92754593aace44cb45803b46cbd65f141bd1f67cf2fcc4cfe8`)
- [observation/documented] The fork is not published to npm registries, so installation requires cloning and building from source with npm install, build, and bundle steps. -- evidence: [README.md#L83-L83](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L83-L83), [README.md#L87-L94](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L87-L94) (`clm_2b3c2494f21bce0938a752fef934ee454339ef2f371e0e7e1ffea15ab4f81087`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

