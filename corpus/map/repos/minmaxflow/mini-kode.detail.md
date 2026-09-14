# minmaxflow/mini-kode -- full detail

[Back to orientation](mini-kode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/minmaxflow/mini-kode/4e7f9767e5ca320ce4866a4743d2cc633a6952da/270e8b959f6026a5.json](../../../wiki/dossiers/minmaxflow/mini-kode/4e7f9767e5ca320ce4866a4743d2cc633a6952da/270e8b959f6026a5.json)

## specifications (1 claim(s))

- [observation/documented] Mini-Kode is an educational project to help developers understand modern coding-agent architecture, described as a complete yet manageable implementation of about 14K lines of production code. -- evidence: [README.md#L9-L9](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L9-L9), [README.md#L3-L3](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L3-L3) (`clm_a197315229be7f96ae0ed94d5d88c1fcb4a9fec023d54b3288d0dcc9b2d90f40`)

## components (1 claim(s))

- [observation/documented] The source tree is organized into modules for tools, Ink-based UI, LLM client, permissions, config, CLI, agent logic, sessions, and shared utilities. -- evidence: [README.md#L104-L115](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L104-L115) (`clm_3aaaea4b807d6829794feefd46d3307d895f33cc04947fcab1c8980a585b4c59`)

## design-choices (1 claim(s))

- [observation/documented] The architecture is layered: a terminal UI layer, an agent layer coordinating the LLM-plus-tool loop, an LLM layer with streaming and tool parsing, a tool layer, and an infrastructure layer for config and permissions. -- evidence: [docs/architecture.md#L5-L5](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/architecture.md#L5-L5), [docs/architecture.md#L11-L47](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/architecture.md#L11-L47) (`clm_da860c0c35da3e3d9e1bc39de4d9a5d0bedc5456881e125e886b19be87792936`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors need Bun and pnpm, install with pnpm install, and use pnpm run dev, pnpm run build, and pnpm run test for development, building, and testing. -- evidence: [README.md#L83-L84](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L83-L84), [README.md#L77-L77](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L77-L77), [README.md#L64-L65](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L64-L65), [README.md#L80-L80](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L80-L80), [README.md#L69-L71](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L69-L71) (`clm_d696de5cdfec1c7f0ba4c5e8e7aee777e5371c59338095e8c10424bcdcb100fb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is invoked as the mini-kode command; it supports an interactive mode (bare command) and a non-interactive mode that executes a task supplied as a quoted argument. -- evidence: [README.md#L57-L58](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L57-L58), [README.md#L52-L52](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L52-L52), [README.md#L54-L54](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L54-L54) (`clm_c61821c4f771d452eace373afe4c8cd1a79f36c8cea2dbbeba779dc514c41634`)
- [observation/documented] MCP servers are configured via .mini-kode/mcp.json with stdio and http transports; tools from connected servers are auto-registered, and ${ENV_VAR} references in args and headers are resolved from the environment. -- evidence: [docs/config.md#L140-L141](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L140-L141), [docs/tools.md#L129-L129](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L129-L129), [docs/config.md#L166-L169](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L166-L169), [docs/tools.md#L133-L136](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L133-L136), [docs/config.md#L136-L136](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L136-L136), [docs/config.md#L145-L145](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/config.md#L145-L145) (`clm_006251e8c615219542ada5fe0d94d139066eb8ec73a2104309346dab373758bb`)

## memory-state (1 claim(s))

- [observation/documented] The system reads an AGENTS.md file from the project root and includes it in system prompts, providing persistent project context across sessions that users can edit. -- evidence: [README.md#L96-L96](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L96-L96), [docs/llm-tool-integration.md#L80-L83](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L80-L83), [README.md#L98-L100](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L98-L100), [docs/llm-tool-integration.md#L78-L78](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L78-L78) (`clm_6bebbfd61415de1e5ffd3c2b8c85679817ce5c32aa9a46770d4ed7966a45bcf7`)

## orchestration (1 claim(s))

- [observation/documented] The agent executor runs a loop: build context, send the request with tool descriptions to the LLM, parse text or tool calls, execute tools, feed results back, and repeat until a final response; conversation length is managed via auto-compaction. -- evidence: [docs/llm-tool-integration.md#L87-L87](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L87-L87), [docs/llm-tool-integration.md#L70-L74](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L70-L74), [docs/llm-tool-integration.md#L47-L50](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/llm-tool-integration.md#L47-L50), [docs/architecture.md#L79-L83](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/architecture.md#L79-L83) (`clm_34c3bc6abd899a6c14329edbc25af68353be686c6b0b49df0a9c775fe72b2686`)

## tools-permissions (2 claim(s))

- [observation/documented] Tools implement a shared Tool<Input, Output> interface with a readonly flag; read-only tools run concurrently while writing tools run sequentially, and writing tools check permissions, pausing until the user approves. -- evidence: [docs/tools.md#L25-L25](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L25-L25), [docs/tools.md#L27-L28](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L27-L28), [docs/tools.md#L13-L21](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L13-L21), [docs/tools.md#L90-L92](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L90-L92) (`clm_d288e5546590be60c259addfee056fb21dbb12611d1a4e5acf584cb807fdc5ed`)
- [observation/documented] Built-in tools include fileRead, fileEdit, listFiles, grep, glob, bash, architect, todo_read, todo_write, and fetch, plus dynamically registered MCP tools; fileEdit, bash, fetch, and MCP tools are marked as requiring permission. -- evidence: [docs/tools.md#L34-L46](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/docs/tools.md#L34-L46) (`clm_270198b2b776df947f08acd01cb1e60efeae5f9e8ca94e259d8ee91105451e5e`)

## evaluation (1 claim(s))

- [inference/documented] No agent-performance evaluation or benchmark harness appears in the provided evidence; the only test-related material is the repository's own Vitest test command, so evaluation capability remains unknown. -- evidence: [README.md#L83-L84](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L83-L84), [README.md#L119-L125](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L119-L125) (`clm_c3649298ba9da2533f28f9ede6f9978cea6b396827167b5ebe57d8d496e91b0a`)

## dependencies (2 claim(s))

- [observation/documented] The documented tech stack includes TypeScript, pnpm, Ink for the terminal UI, OpenAI SDK for LLM integration, Vitest for testing, Zod for runtime validation, and Commander for the CLI. -- evidence: [README.md#L119-L125](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L119-L125) (`clm_6d075132f9e58ed6762d8b91f0ac3e3ed32c316667dd24b1ebb803328d36e951`)
- [observation/documented] LLM access is configured via environment variables including DEEPSEEK_API_KEY, GLM_API_KEY, OPENAI_API_KEY, and generic MINIKODE_API_KEY/BASE_URL/MODEL variables; DeepSeek and GLM are noted as tested and verified. -- evidence: [README.md#L42-L43](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L42-L43), [README.md#L30-L32](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L30-L32), [README.md#L40-L40](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L40-L40), [README.md#L45-L48](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L45-L48), [README.md#L36-L38](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L36-L38), [README.md#L28-L28](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L28-L28), [README.md#L34-L34](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/README.md#L34-L34) (`clm_467610794cd570914ad7fa3d29a8b0b9a7858bbf3e12a63e16003682ebe666d1`)

## limitations (1 claim(s))

- [observation/documented] A known issue documents that resizing the terminal during CLI operation can cause some UI elements to render multiple times, producing duplicate components and visual clutter. -- evidence: [KNOWN_ISSUES.md#L7-L7](https://github.com/minmaxflow/mini-kode/blob/4e7f9767e5ca320ce4866a4743d2cc633a6952da/KNOWN_ISSUES.md#L7-L7) (`clm_c1f1e54968c8a11c7a3b03d49ce9ddd31a93534000851b6c4fc6955bb2d23456`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

