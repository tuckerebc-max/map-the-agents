# githpriyanshu23/clawde_code -- full detail

[Back to orientation](clawde_code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/githpriyanshu23/clawde_code/00e3585ae83aabff740880f9dd464a31e3c06325/425f298bc7ee3322.json](../../../wiki/dossiers/githpriyanshu23/clawde_code/00e3585ae83aabff740880f9dd464a31e3c06325/425f298bc7ee3322.json)

## specifications (2 claim(s))

- [observation/documented] The archived project is Claude Code, a CLI for interacting with Claude from the terminal for software engineering tasks such as editing files, running commands, and searching codebases. -- evidence: [README.md#L19-L19](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L19-L19) (`clm_1728ea3db4094e58b11c82656664ab7696dcaa9bb481c0f169102c74fdfc6cf2`)
- [observation/documented] Per the README, the codebase is TypeScript running on Bun with a React+Ink terminal UI, spanning roughly 1,900 files and over 512,000 lines. -- evidence: [README.md#L23-L27](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L23-L27) (`clm_f14e575aa0159e3a1edddb618ff827c84718c4d960a836b7a4a036fec081dce7`)

## components (2 claim(s))

- [observation/documented] The src tree includes a tool registry, command registry, QueryEngine for LLM API calls, cost tracking, and directories for tools, commands, components, services, bridge, coordinator, plugins, skills, and memory. -- evidence: [README.md#L31-L71](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L31-L71) (`clm_6c2531827790da29924f532dcc4ac2a195c667f735ac427a0da7ca9f0fc6418a`)
- [observation/documented] Documented agent tools include BashTool, file read/write/edit tools, GlobTool, ripgrep-based GrepTool, web fetch/search, AgentTool for sub-agents, MCPTool, LSPTool, and task/team management tools. -- evidence: [README.md#L79-L103](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L79-L103) (`clm_b6f64d34c14158a148303763c19fc27adb7789c8cce6276381083d82c1ba9532`)

## design-choices (2 claim(s))

- [observation/documented] Startup is optimized by prefetching MDM settings, keychain reads, and API preconnect in parallel before heavy module evaluation, and heavy modules like OpenTelemetry and gRPC are lazily loaded via dynamic import. -- evidence: [README.md#L227-L227](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L227-L227), [README.md#L217-L217](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L217-L217) (`clm_ea420dac74b611bae7947126209c6043905ce9c95c24bc8d12b1ccf5a713bc16`)
- [observation/documented] Feature flags via Bun's bundler strip inactive code at build time; notable flags include PROACTIVE, KAIROS, BRIDGE_MODE, DAEMON, VOICE_MODE, AGENT_TRIGGERS, and MONITOR_TOOL. -- evidence: [README.md#L177-L177](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L177-L177), [README.md#L171-L175](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L171-L175), [README.md#L166-L166](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L166-L166) (`clm_1c549665298a49b06df249bce848ef7262c370e667c9ad56cb67f1085c8fe194`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the README instructs running bash ./gitpretty-apply.sh to apply per-file emoji commit formatting, optionally with --hooks to install hooks for future commits. -- evidence: [README.md#L255-L255](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L255-L255), [README.md#L245-L247](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L245-L247), [README.md#L257-L259](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L257-L259), [README.md#L243-L243](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L243-L243) (`clm_fe9255c9e6b19e360517bf30d2b9df42303349ab4fbaa9bbf7fd0120951695d8`)
- [observation/documented] Repository development practice: to use the bundled source-explorer MCP server, clone the repo, run npm install && npm run build in mcp-server, then register it with claude mcp add claude-code-explorer. -- evidence: [README.md#L269-L269](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L269-L269), [README.md#L282-L283](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L282-L283), [README.md#L279-L279](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L279-L279) (`clm_8543255ace77b7fed19a81b787775d5a2650f5589f85a222349d98dd8e3998d7`)

## skills-patterns (1 claim(s))

- [observation/documented] Reusable workflows live in the skills directory and execute through SkillTool, and users can add custom skills. -- evidence: [README.md#L235-L235](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L235-L235) (`clm_765bc653fd707091c4e9bb86db71f73efab5cf7a736c8adea49869ab9a3d47b2`)

## interfaces (2 claim(s))

- [observation/documented] Users invoke slash commands with a / prefix, including /commit, /review, /compact, /mcp, /doctor, /login, /memory, /resume, and /cost, among about 50 commands. -- evidence: [README.md#L109-L130](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L109-L130), [README.md#L107-L107](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L107-L107) (`clm_5b3aaa32e4e0657cf96125e0a09f55449a52914d192454216945e8052beb6fe0`)
- [observation/documented] The bundled MCP server exposes tools such as list_tools, get_tool_source, read_source_file, search_source, and get_architecture, plus prompts like explain_tool and architecture_overview. -- evidence: [README.md#L313-L317](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L313-L317), [README.md#L300-L309](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L300-L309) (`clm_1ea3a459667dc18a6d74c315ff58e762162bcf5acfb60dae00e463b48c1239dc`)

## memory-state (1 claim(s))

- [observation/documented] The product includes persistent memory: a memdir memory directory, a /memory command, and services for automatic memory extraction and team memory synchronization. -- evidence: [README.md#L134-L147](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L134-L147), [README.md#L31-L71](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L31-L71), [README.md#L109-L130](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L109-L130) (`clm_1e72b9416476270bc997a4a9b296bdef797084b200a6b135b2fbe497d44d6fa1`)

## orchestration (1 claim(s))

- [observation/documented] Sub-agents are spawned via AgentTool, a coordinator directory handles multi-agent orchestration, and TeamCreateTool enables team-level parallel work. -- evidence: [README.md#L231-L231](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L231-L231) (`clm_a7c757d70d69c3b82747b8eeec58b449d95a1e8c07fd1c3af641ea4c48fec520`)

## tools-permissions (1 claim(s))

- [observation/documented] Permissions are checked on every tool invocation; the system prompts the user or auto-resolves based on the configured permission mode such as default, plan, bypassPermissions, or auto. -- evidence: [README.md#L162-L162](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L162-L162) (`clm_2b75816bb367aadbb7a5497e13eda59a4bf045f3106ec2df1cd1a60c8625dda1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The documented stack uses Bun, strict TypeScript, React+Ink, Commander.js, Zod v4, ripgrep, MCP and LSP SDKs, the Anthropic SDK, OpenTelemetry with gRPC, GrowthBook, and OAuth 2.0/JWT/Keychain auth. -- evidence: [README.md#L199-L211](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L199-L211) (`clm_c09b7f64d9dc55f31f497850e8e09567748aa663b8f23a566dfb6c67710c2d46`)

## limitations (1 claim(s))

- [observation/documented] The README states the archived source was leaked from Anthropic's npm registry on 2026-03-31 and that all original code remains Anthropic's property. -- evidence: [README.md#L5-L5](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L5-L5), [README.md#L344-L344](https://github.com/GitHpriyanshu23/Clawde_Code/blob/00e3585ae83aabff740880f9dd464a31e3c06325/README.md#L344-L344) (`clm_d2303804704ecf80ccfe6c00d32bf6321855fa4807602ba50cbed175ad3ce3c0`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

