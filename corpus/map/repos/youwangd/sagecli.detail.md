# youwangd/sagecli -- full detail

[Back to orientation](sagecli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/youwangd/sagecli/c167712ddb6929dee36a534ae128ac6600adf5c7/03c45df43acaed22.json](../../../wiki/dossiers/youwangd/sagecli/c167712ddb6929dee36a534ae128ac6600adf5c7/03c45df43acaed22.json)

## specifications (1 claim(s))

- [observation/documented] Sage is a vendor-neutral, Unix-native control plane for agent CLIs implemented as one bash script (~8,500 lines) under an MIT license. -- evidence: [README.md#L21-L22](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L21-L22), [README.md#L50-L52](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L50-L52), [README.md#L24-L28](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L24-L28), [README.md#L249-L249](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L249-L249), [README.md#L56-L63](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L56-L63) (`clm_3697de9d8cc9981387434cd62f011ffeb3ffd46a5d5896dc9b317ee16137ca52`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Design emphasizes vendor neutrality: 8 runtimes plus any ACP agent behind one command surface, backends swappable with a flag, and a --fallback chain that auto-routes to healthy runtimes after a pre-flight health check. -- evidence: [README.md#L122-L125](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L122-L125), [README.md#L50-L52](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L50-L52), [README.md#L130-L130](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L130-L130), [README.md#L116-L116](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L116-L116) (`clm_3b96fa9b1d0200ff0d3963e64cd337d35281296a7c9a821a006898f3e9dd5f46`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes 53 commands across 12 domains (e.g. create, send, call, tasks, bench, mcp, skill, memory, trace, dashboard, doctor), with inline help via sage help and per-command --help. -- evidence: [README.md#L211-L211](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L211-L211), [README.md#L209-L209](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L209-L209), [CAPABILITIES.md#L4-L56](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/CAPABILITIES.md#L4-L56) (`clm_983ae5355d6d7250d3a9ac89780b9119725e08db33a9a546f1b5f71d329cf14c`)
- [observation/documented] The acp runtime speaks JSON-RPC 2.0 over stdio and maintains persistent sessions across tasks, unlike one-shot runtimes such as cline/claude-code which spawn a fresh process per task. -- evidence: [README.md#L179-L179](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L179-L179), [DEVELOPMENT.md#L167-L167](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L167-L167), [DEVELOPMENT.md#L187-L193](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L187-L193) (`clm_08672c9775ef7d74f49ecb31ee13ca1e12433055fa3e2a1c12ed5808ba8928c1`)
- [observation/documented] Every runtime implements exactly two shell functions, runtime_start() for one-time setup and runtime_inject() for each incoming message, so a new runtime is a single bridge file. -- evidence: [DEVELOPMENT.md#L289-L293](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L289-L293), [DEVELOPMENT.md#L295-L300](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L295-L300), [DEVELOPMENT.md#L287-L287](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L287-L287) (`clm_439c76c1b7b3d0e78111622c5890b642fffa350aad6e4b59675c313bb8356978`)

## memory-state (2 claim(s))

- [observation/documented] All state lives under ~/.sage/ as files: per-agent inbox/replies/results/workspace/state, runtime.json, instructions.md, steer.md, plus shared runtimes/, tools/, tasks/, plans/, and trace.jsonl. -- evidence: [DEVELOPMENT.md#L22-L60](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L22-L60), [README.md#L203-L203](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L203-L203) (`clm_c435c521b6ac7cef7b486d41fcabd687e01a893b4bca2de3677ab5b2caf4f2f5`)
- [observation/documented] Sage provides per-agent persistent memory (memory set/get/ls/rm/clear with auto-injection into prompts) and a shared context store (context set/get/ls/rm/clear with auto-inject). -- evidence: [CAPABILITIES.md#L69-L180](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/CAPABILITIES.md#L69-L180) (`clm_56bcbc236e10b8e328c13d2f48d0765a592ee6384706f9bc15513e8b11c6b600`)

## orchestration (2 claim(s))

- [observation/documented] Each agent runs a runner.sh process in a tmux window that polls its inbox directory every 300ms, sources the runtime script, and calls runtime_inject() per message. -- evidence: [README.md#L189-L201](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L189-L201), [DEVELOPMENT.md#L5-L18](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L5-L18) (`clm_8b04a8aec629f51f9157d99c14f442b007cd4f88fd8bddf49e72efe170d29a93`)
- [observation/documented] sage send is asynchronous (writes JSON to the inbox, returns a task ID immediately, auto-starts the agent), while sage call is synchronous, polling a reply directory up to a specified timeout. -- evidence: [DEVELOPMENT.md#L244-L255](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L244-L255), [DEVELOPMENT.md#L258-L268](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L258-L268) (`clm_54372bbec87d251009dc5a09ab32858e33e047b213b2b6ef519456ff0ea57eae`)

## tools-permissions (1 claim(s))

- [observation/documented] In the ACP runtime, when an agent requests a permission (e.g. file write), the Claude Code adapter's session/request_permission is auto-approved by the runtime; Cline handles tools internally. -- evidence: [DEVELOPMENT.md#L219-L221](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L219-L221) (`clm_4559474154f34c584dbe731865a6ad480319d6a74cbb22d5a0b8904c5d877e76`)

## evaluation (1 claim(s))

- [observation/documented] Sage includes bench-as-code: sage bench run executes real tasks through multiple agents' CLIs and sage bench report emits metrics such as success rate and median wall time per agent. -- evidence: [README.md#L143-L147](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L143-L147), [README.md#L136-L139](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L136-L139) (`clm_e88b9ed6edd31b30e578db8576bc3950d228fb3ff65ede97a82ac0679c5735e6`)

## dependencies (1 claim(s))

- [observation/documented] Required dependencies are bash 4.0+, jq 1.6+, and tmux 3.0+; agent CLIs such as Claude Code, Gemini CLI, Codex, Cline, and ACP agents are optional per-runtime. -- evidence: [DEVELOPMENT.md#L537-L539](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L537-L539), [DEVELOPMENT.md#L542-L546](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/DEVELOPMENT.md#L542-L546), [README.md#L83-L83](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L83-L83) (`clm_bb585b6e0036113098b66907c0ac2654f666f2ef97436eddf6e14600e16d16b8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Sage positions itself as glue for orchestrating existing coding agents rather than a coding assistant, targeting users who already run Claude Code, Codex, or Gemini CLI and want them to interoperate. -- evidence: [README.md#L65-L65](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L65-L65), [README.md#L24-L28](https://github.com/youwangd/SageCLI/blob/c167712ddb6929dee36a534ae128ac6600adf5c7/README.md#L24-L28) (`clm_e3556cc2f423dbbcc5c2f54c106615e9321bab1064708bf955127d45fbba1936`)

