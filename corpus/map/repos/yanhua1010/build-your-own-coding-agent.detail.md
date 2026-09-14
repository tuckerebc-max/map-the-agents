# yanhua1010/build-your-own-coding-agent -- full detail

[Back to orientation](build-your-own-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yanhua1010/build-your-own-coding-agent/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/f0cb08e3c2e0dca7.json](../../../wiki/dossiers/yanhua1010/build-your-own-coding-agent/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/f0cb08e3c2e0dca7.json)

## specifications (1 claim(s))

- [observation/documented] The repository is a tutorial series that dissects the internals of coding agents layer by layer while building a runnable mini-agent, using three open-source coding agent projects as references. -- evidence: [README.md#L3-L3](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L3-L3) (`clm_64928a2bb42f68b8759f757088018a623622d77883003b4f345b7a2aaab973d4`)

## components (2 claim(s))

- [observation/documented] Six published articles cover the agent loop, unified LLM API and error contracts, tool calling, context compaction and session persistence, and permission/security philosophy, each linked to notes and runnable code. -- evidence: [README.md#L13-L20](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L13-L20) (`clm_bd0249cf9595c292e704a3b2f10b7b0adfb47460bd4e3724a046a87ebc39c83d`)
- [observation/documented] Each article maps to an independently runnable stage under steps/, starting from a ~100-line minimal loop and progressively adding tool execution, context management, and a TUI. -- evidence: [README.md#L26-L26](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L26-L26) (`clm_b6fe8d95a9225345d04da83f13c9dfe92ed6bef7abb28678c2cbf0681013678b`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] A step can be run by exporting DEEPSEEK_API_KEY and executing 'cd steps/01-minimal-loop && npm install && npm start'. -- evidence: [README.md#L30-L32](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L30-L32) (`clm_fbfbc55506c3fcfbd5e825f61177e82e5fd819f48623321b8855bb0d9ee6c595`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [inference/documented] The mini-agent likely exposes a terminal/TUI interface, since a TUI is listed among the capabilities progressively added in later steps. -- evidence: [README.md#L26-L26](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L26-L26) (`clm_82d2db532e160c6d10531ca68f5ac597cda6c776478eb6426caa8f2ebc2f3da0`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The series uses domestic Chinese model APIs (DeepSeek, GLM, Kimi), and the code is stated to run directly locally. -- evidence: [README.md#L9-L9](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L9-L9) (`clm_9b381d0a85d3702e1ef45d0da39de55edc64335af7d8b33f7c4d4e436f122294`)
- [observation/documented] The repository code is MIT licensed; quoted third-party snippets follow their original licenses (pi: MIT; codex and grok-build: Apache-2.0), with copyright retained by the original authors. -- evidence: [README.md#L36-L36](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L36-L36) (`clm_57f3791bdbb4242ee1c2fb1d66cf8b7b6b01494e3fce24c6380526f3e5c0f06d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The series uses pi (TypeScript, MIT, ~78k stars) as the main teaching text, with codex (Rust, ~101k stars) and grok-build (Rust, ~23k stars) used for architecture comparison. -- evidence: [README.md#L5-L7](https://github.com/yanhua1010/build-your-own-coding-agent/blob/1e607dbb2f0819eda93d3d26d2dbb0b7089a3a2a/README.md#L5-L7) (`clm_214b475617afe5ab5a8a10dd6bacc31f783e10bea3da90ccb87d15e32be4f071`)

