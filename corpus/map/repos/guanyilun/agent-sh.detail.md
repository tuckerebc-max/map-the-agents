# guanyilun/agent-sh -- full detail

[Back to orientation](agent-sh.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/guanyilun/agent-sh/8038ae7730eb2978a43887fb9e1a7da7b409791d/a723232a0e326851.json](../../../wiki/dossiers/guanyilun/agent-sh/8038ae7730eb2978a43887fb9e1a7da7b409791d/a723232a0e326851.json)

## specifications (2 claim(s))

- [observation/documented] agent-sh is published as an npm package (`agent-sh`) with a license badge, installable globally via `npm install -g agent-sh`. -- evidence: [README.md#L32-L34](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L32-L34), [README.md#L3-L4](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L3-L4) (`clm_72ec5a38ad78b754541f1918afeae0ce3353e1c2f73dae817cca9e70248b941b`)
- [observation/documented] The runtime requires Node.js 18+ and supports bash, zsh, and fish as host shells; other shells such as nushell are not yet wired up. -- evidence: [README.md#L48-L48](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L48-L48) (`clm_c797267ff84e977963f684ad537fbf8a3b9a0d6a495cfec039f3491ce57f49ef`)

## components (2 claim(s))

- [observation/documented] The architecture is a pure kernel (`createCore()`) providing EventBus, HandlerRegistry, Compositor, multi-backend coordination, and a default cwd handler, with agent, shell, TUI, and providers all loaded as extensions. -- evidence: [docs/architecture.md#L9-L43](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/architecture.md#L9-L43), [docs/architecture.md#L7-L7](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/architecture.md#L7-L7) (`clm_753604f7f83b0d94d5fdeff1e2a2572d13c6e276b53336223acda03ba53113b5`)
- [observation/documented] The default backend `ash` resolves providers, configures an LlmClient, calls any OpenAI-compatible API directly, and executes tools in a loop until the LLM finishes; it only activates once an apiKey and model are resolved. -- evidence: [docs/agent.md#L5-L5](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L5-L5) (`clm_5792c66312ba36d97aaf6feb35e6458f98eac19d66c140ce8970b00519f94949`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Skills follow the Agent Skills standard: directories with a SKILL.md containing YAML frontmatter (required name and description); only metadata enters the system prompt, and the agent loads full content via read_file when needed. -- evidence: [docs/agent.md#L104-L104](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L104-L104), [docs/agent.md#L122-L124](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L122-L124), [docs/agent.md#L120-L120](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L120-L120), [docs/agent.md#L82-L82](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L82-L82) (`clm_5153fe7e95e306e1ea78fea87d7fdc04b96c6cb12bf9b20409fccd6c616e5f20`)

## interfaces (2 claim(s))

- [observation/documented] Tools implement a `ToolDefinition` interface with name, description, JSON Schema input_schema, an execute function with optional streaming onChunk callback, and flags like modifiesFiles, readOnly, and showOutput. -- evidence: [docs/agent.md#L280-L285](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L280-L285), [docs/agent.md#L287-L290](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L287-L290), [docs/agent.md#L292-L294](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L292-L294) (`clm_24353849ad0ed947a8ad3f4840c791e69c33d4cc228fc4d3dae90461387469b5`)
- [observation/documented] Core tools include bash, read_file, write_file, edit_file, grep (via ripgrep), glob, ls, and list_skills; conversation_recall is registered by the rolling-history extension rather than being a core tool. -- evidence: [docs/agent.md#L177-L187](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L177-L187), [docs/agent.md#L189-L189](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L189-L189) (`clm_067578336e57aff5da169d9072c7647040d46ad411072e438f50e541efb240a8`)

## memory-state (1 claim(s))

- [observation/documented] Conversation state is an OpenAI-compatible messages array; ash auto-compacts when estimated prompt tokens cross autoCompactThreshold (default 0.5) of the model's context window, and older turns are evicted to a persistent rolling-history store browsable via conversation_recall. -- evidence: [docs/agent.md#L356-L356](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L356-L356), [docs/agent.md#L37-L38](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L37-L38), [docs/agent.md#L350-L350](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L350-L350), [docs/agent.md#L341-L341](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L341-L341) (`clm_0f3235d2e61cb0fcd90c541c743035609fc5f0683eb1477a21907406edde1be6`)

## orchestration (1 claim(s))

- [observation/documented] The agent runs a tool loop with no hard iteration limit; side-effect-free tools run in parallel via Promise.all while side-effecting tools run sequentially, and results over maxResultBytes (default 100KB) are head+tail truncated. -- evidence: [docs/agent.md#L223-L223](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L223-L223), [docs/agent.md#L154-L154](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L154-L154), [docs/agent.md#L221-L221](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L221-L221) (`clm_255fef59932579011fbb349995b5c32192b222fe37186815f0789074119438aa`)

## tools-permissions (1 claim(s))

- [observation/documented] By default every tool runs without gating ('yolo mode'); the kernel has no permission opinion, and gating extensions can interpose confirmation or policy checks via tool advisors. -- evidence: [docs/agent.md#L158-L163](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L158-L163) (`clm_3b0a98f1549298b6ec64e89cb797ebfcfa19117dca8e14c2482e1a2ee22f2fe4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The bundled frontend is a shell on top of node-pty, and the grep tool searches file contents via ripgrep; ash works with any OpenAI-compatible API including built-in providers openrouter, openai, deepseek, ollama, zai-coding-plan, and opencode. -- evidence: [docs/agent.md#L177-L187](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/docs/agent.md#L177-L187), [README.md#L62-L62](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L62-L62), [README.md#L10-L10](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L10-L10) (`clm_308942903fd7f609a53ce97e769f5c6d0f4e5f9994ea5876403db915cd756216`)

## limitations (1 claim(s))

- [observation/documented] Native Windows (cmd.exe/PowerShell) is not supported as the host shell; the README recommends running inside WSL for the full interactive experience, while headless/library/ACP-bridge usage may work. -- evidence: [README.md#L50-L50](https://github.com/guanyilun/agent-sh/blob/8038ae7730eb2978a43887fb9e1a7da7b409791d/README.md#L50-L50) (`clm_761f9deeee81908f0ec6f7fdf178d4bd8daedaa8f19c8e542e1eba3b9e5a6c66`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

