# startuphakk/openmonoagent.ai -- full detail

[Back to orientation](openmonoagent.ai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/startuphakk/openmonoagent.ai/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/1b092f398ae5cb57.json](../../../wiki/dossiers/startuphakk/openmonoagent.ai/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/1b092f398ae5cb57.json)

## specifications (1 claim(s))

- [observation/documented] OpenMono is described as a .NET 10 CLI coding agent that runs entirely on local hardware, pairing with its own llama.cpp inference server and Docker sandboxing. -- evidence: [docs/ARCHITECTURE.md#L3-L3](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L3-L3), [README.md#L42-L42](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L42-L42) (`clm_0641fe9b019de1a567b881f65e66b01d468320fa0ca6994975e16440f63d19de`)

## components (2 claim(s))

- [observation/documented] Every tool call passes a 12-step pipeline including schema validation, plan-mode guard, capability check, caching, pre/post hooks, and artifact storage for results over 10 KB. -- evidence: [docs/ARCHITECTURE.md#L204-L220](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L204-L220), [README.md#L133-L134](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L133-L134) (`clm_bd1f76a5e424e225aeb6281413f4302e4609191b2b4469fdb688e1acfec55465`)
- [observation/documented] A Roslyn tool loads .cs files into an in-memory AdhocWorkspace with a 5-minute compilation cache, exposing actions like find-references, callers, diagnostics, type-hierarchy, and blast-radius. -- evidence: [docs/ARCHITECTURE.md#L296-L305](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L296-L305), [docs/ARCHITECTURE.md#L292-L292](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L292-L292) (`clm_ce440f9177eeff87dbaa5d83320db4d29bcdce56b314bdf711fc8df3160559da`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README directs contributors to read CONTRIBUTING.md before opening a PR and welcomes contributions of tools, providers, LSP servers, playbooks, bug fixes, and docs. -- evidence: [README.md#L304-L311](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L304-L311) (`clm_138fbf0c21b79c0f1041154cdba3d948fef9a5d54d90d113577c3c8f43c6dbad`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI offers TUI mode by default and a classic scrolling terminal via `openmono agent --classic`; renderer selection falls back to classic when I/O is redirected. -- evidence: [docs/ARCHITECTURE.md#L354-L357](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L354-L357), [README.md#L67-L70](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L67-L70) (`clm_ffbe4ca569205d7d9363b00f7fea62b96266c27d72fe2611eabbae0c14e4837c`)
- [observation/documented] A VS Code/Cursor extension connects to the agent over ACP on port 7475, started with `--acp-only --acp-port 7475`, sharing the same agent core as the CLI. -- evidence: [README.md#L211-L212](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L211-L212), [docs/ARCHITECTURE.md#L45-L45](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L45-L45) (`clm_ac1f29675af26284103b979753bafc0c9300278dea75d3e2dda2aef9cb6b2143`)

## memory-state (2 claim(s))

- [observation/documented] Context management checkpoints at 65% context fill with an LLM summary and compacts at 80% as a fallback; thresholds track the real window read from llama.cpp `/props`. -- evidence: [docs/ARCHITECTURE.md#L234-L237](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L234-L237), [docs/ARCHITECTURE.md#L239-L239](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L239-L239) (`clm_65a58eb902cf36160e7f11c5f13f02ba063b96d5c28d01e314c257eb55702126`)
- [observation/documented] Sessions persist as JSONL under `~/.openmono/sessions/` with a header record plus messages, and checkpoints are stored in a sibling `.checkpoints.json` file. -- evidence: [docs/ARCHITECTURE.md#L228-L230](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L228-L230) (`clm_420740377277fcfd902da187e2b896d3017d2f97b1c5aa4c3896e6a86890e142`)

## orchestration (2 claim(s))

- [observation/documented] The agentic loop runs up to 25 iterations per turn, aborts on three identical repeated tool sequences (doom-loop detection), and ends when the LLM emits text with no tool calls. -- evidence: [README.md#L125-L126](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L125-L126), [docs/ARCHITECTURE.md#L194-L194](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L194-L194), [docs/ARCHITECTURE.md#L196-L196](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L196-L196) (`clm_5d6b7f2fbc595d4a3d5260fc241bc5236a6ad105e115dc98b06deb64dba57551`)
- [observation/documented] Five specialist sub-agents (Explore, Plan, Coder, Verify, general-purpose) run in isolated sessions with restricted tool allow-lists and per-agent turn budgets from 10 to 30. -- evidence: [README.md#L139-L140](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L139-L140), [README.md#L142-L146](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L142-L146), [docs/ARCHITECTURE.md#L247-L253](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L247-L253) (`clm_b59c11f6e8329cdfd91d8a2cbdf570822d56f42f5e5a7ddbceb2f017ab823969`)

## tools-permissions (1 claim(s))

- [observation/documented] A PermissionEngine uses a capability system (file read/write, process exec, network egress, VCS mutation, agent spawn) with decision order: deny-all, deny patterns, allow-all, allow patterns, then interactive prompt. -- evidence: [docs/ARCHITECTURE.md#L311-L311](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L311-L311), [docs/ARCHITECTURE.md#L313-L320](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L313-L320), [docs/ARCHITECTURE.md#L322-L322](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L322-L322) (`clm_c7a625b02570aa55c43c9fab0a3f618bf92abde3de835a94c6a28ead5d73e3de`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] Web search and scraping rely on self-hosted SearXNG and Scrapling+Camoufox behind a Caddy gateway, with automatic fallback to DuckDuckGo or direct HTTP fetch when services are absent. -- evidence: [README.md#L201-L202](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L201-L202), [docs/ARCHITECTURE.md#L53-L57](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L53-L57), [docs/ARCHITECTURE.md#L87-L98](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L87-L98) (`clm_ca66c7cac0c064bd0110c4bf071f24bc7f75c3b685c69cab52e7a9d5eaafd1a1`)
- [observation/documented] LSP servers for C#, TypeScript, Python, Go, and Rust start lazily on first use, and MCP servers are spawned as subprocesses with a JSON-RPC 2.0 handshake over stdin/stdout. -- evidence: [docs/ARCHITECTURE.md#L263-L266](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L263-L266), [docs/ARCHITECTURE.md#L278-L284](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L278-L284), [docs/ARCHITECTURE.md#L276-L276](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L276-L276) (`clm_938f517c21119d7d155b05ff723df8702b6db1b85aefc3d59e837e44d05b8c14`)
- [observation/documented] Local llama.cpp is the default and fully supported provider; OpenAI, Anthropic, and Ollama providers are documented as available but work-in-progress. -- evidence: [README.md#L175-L176](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L175-L176) (`clm_fd6c150a9cb6312fde2ad8251bcfad84b788b37823367c30cdf71f9575b43f27`)

## limitations (1 claim(s))

- [observation/documented] The Docker sandbox mounts the project as /workspace, and the documentation states nothing outside that mount is visible or reachable from the agent. -- evidence: [docs/ARCHITECTURE.md#L3-L3](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/docs/ARCHITECTURE.md#L3-L3), [README.md#L153-L154](https://github.com/StartupHakk/OpenMonoAgent.ai/blob/f3f001dd5b33f79e90c3571ce8bd00664c49ed0b/README.md#L153-L154) (`clm_f6e27268dee23c4d465b7cb710fe710338cdcd030baf73f05c1ffcd21ce6cf07`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

