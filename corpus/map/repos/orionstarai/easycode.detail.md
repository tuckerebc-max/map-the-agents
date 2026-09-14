# orionstarai/easycode -- full detail

[Back to orientation](easycode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/orionstarai/easycode/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/a79807b5d6c7fa03.json](../../../wiki/dossiers/orionstarai/easycode/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/a79807b5d6c7fa03.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project is a monorepo with a CLI package (React Ink terminal UI, commands, services, auth) and a core package containing tools, MCP engine, prompts, hooks, skills, and config modules. -- evidence: [README.md#L503-L513](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L503-L513), [README.md#L430-L499](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L430-L499), [README.md#L426-L426](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L426-L426) (`clm_1af3e42696c05fccdfa99268a4af63ac2972d7171715e003f77280383261a0a3`)

## design-choices (1 claim(s))

- [observation/documented] MCP servers can be configured in .easycode/settings.json either as local processes (command/args/env) or via Streamable HTTP endpoints with headers, including trust and include/exclude tool options. -- evidence: [README.md#L674-L674](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L674-L674), [README.md#L680-L696](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L680-L696), [README.md#L740-L746](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L740-L746), [README.md#L712-L730](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L712-L730), [README.md#L698-L706](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L698-L706), [README.md#L732-L736](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L732-L736) (`clm_258ef96da80b6c6352ae080d1315060b07eee0b08004d7ca55ab874dc27c5ab1`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm install, build with npm run build, test with npm run test, and run lint and typecheck before committing. -- evidence: [README.md#L1140-L1144](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1140-L1144), [README.md#L1115-L1116](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1115-L1116), [README.md#L1124-L1136](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1124-L1136), [README.md#L1119-L1120](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1119-L1120) (`clm_6221f6421c04067d701ebafb07996313accfc5149883d434fb72831811e7c143`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product is a CLI launched with the `easycode` command, supporting options such as --model, --prompt, --sandbox, --yolo, --continue, --session, --workdir, and --list-sessions. -- evidence: [README.md#L282-L284](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L282-L284), [README.md#L228-L230](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L228-L230), [README.md#L286-L300](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L286-L300) (`clm_95beccbc791540fd0fd9123255ef231bbb859a3247c8e507291cbfa0f411dfda`)
- [observation/documented] Interactive mode provides slash commands including /help, /session, /model, /compress, /tools, /mcp, /memory, /plan, /yolo, /restore, /theme, /auth, and /init. -- evidence: [README.md#L384-L389](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L384-L389), [README.md#L375-L380](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L375-L380), [README.md#L409-L412](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L409-L412), [README.md#L416-L420](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L416-L420), [README.md#L359-L363](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L359-L363), [README.md#L350-L355](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L350-L355), [README.md#L367-L371](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L367-L371), [README.md#L341-L346](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L341-L346) (`clm_29b4858e0d0eefae73f70f7a4467bbc382696be3d86309f2db4f95709bd2d1f0`)
- [observation/documented] Custom models can be configured in OpenAI-compatible or Anthropic Claude formats via a /model management wizard or ~/.easycode-user/custom-models.json, with fields like provider, baseUrl, apiKey, modelId, and optional enableThinking. -- evidence: [README.md#L768-L768](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L768-L768), [README.md#L800-L823](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L800-L823), [README.md#L897-L903](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L897-L903), [README.md#L907-L913](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L907-L913), [README.md#L787-L794](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L787-L794), [README.md#L798-L798](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L798-L798), [README.md#L882-L891](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L882-L891) (`clm_4901f1c505d637f4e6956a7eebaac6b49bfa0e796543717cffe2b4343c7512bb`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are persisted with automatic history saving, resumable via --continue or --session, with history compression to save tokens and checkpoint-based file rollback via /restore. -- evidence: [README.md#L375-L380](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L375-L380), [README.md#L166-L169](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L166-L169), [README.md#L350-L355](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L350-L355), [README.md#L286-L300](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L286-L300) (`clm_cb44563caa89b28ec5cac1985238874c07d3b6bbd8320994de254b5ef691effb`)

## orchestration (2 claim(s))

- [observation/documented] Easy Code can act as an ACP orchestrator, delegating coding tasks to locally installed Claude Code or Codex via pinned ACP bridge packages, triggered by the model, @cc/@codex prefixes, or /bind in Feishu. -- evidence: [README.md#L975-L978](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L975-L978), [README.md#L971-L971](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L971-L971), [README.md#L982-L986](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L982-L986) (`clm_b0a4759fd6bd63a9976c8ef484059174c72692dfa690240cf4a38292bf2a79cd`)
- [observation/documented] Delegated external-agent sessions can be resumed with a resume sub-syntax that reloads full session history via session/load, and task records persist under ~/.easycode-user/delegate-tasks/. -- evidence: [README.md#L997-L997](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L997-L997), [README.md#L1008-L1008](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1008-L1008), [README.md#L1003-L1006](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1003-L1006), [README.md#L1001-L1001](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1001-L1001) (`clm_1ee1daa61620bc82731565db57c7be45f1416011a633a7ca0609e6b5f8d7019c`)

## tools-permissions (2 claim(s))

- [observation/documented] Built-in tools include file operations (read_file, write_file, replace, delete_file), search (glob, grep via ripgrep), shell execution, web_fetch/web_search, task sub-agent, todo_write, and memory. -- evidence: [README.md#L638-L641](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L638-L641), [README.md#L632-L634](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L632-L634), [README.md#L614-L620](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L614-L620), [README.md#L645-L650](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L645-L650), [README.md#L624-L628](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L624-L628), [README.md#L142-L151](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L142-L151) (`clm_092f123927b7cfb9727fdd1cdab77ee6dc3865665412f6acb13b3368d1f290f6`)
- [observation/documented] Tools carry documented safety levels: read-only tools like read_file and grep, confirmation-required tools like write_file, replace, and shell, with a --yolo mode that auto-executes all operations without confirmation. -- evidence: [README.md#L632-L634](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L632-L634), [README.md#L614-L620](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L614-L620), [README.md#L318-L318](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L318-L318), [README.md#L286-L300](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L286-L300) (`clm_6e375d19dfd95015fbd811ba9fbe2e5b8ac87a5e1e9b3d1039c0ae6103bd16a1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack uses TypeScript 5.x on Node.js 20+, React+Ink for CLI UI, esbuild for building, Vitest for tests, @google/genai for Gemini, and @modelcontextprotocol/sdk for MCP. -- evidence: [README.md#L14-L18](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L14-L18), [README.md#L503-L513](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L503-L513) (`clm_32d45750f01cadabf9ea7caaae1c3930e0d65ec8fc22ebb1740590a643003c44`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

