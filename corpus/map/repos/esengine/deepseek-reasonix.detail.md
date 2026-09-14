# esengine/deepseek-reasonix -- full detail

[Back to orientation](deepseek-reasonix.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/esengine/deepseek-reasonix/8679e1f0b614467ad57aea364b58c478b365e05a/1fb4383a9229e205.json](../../../wiki/dossiers/esengine/deepseek-reasonix/8679e1f0b614467ad57aea364b58c478b365e05a/1fb4383a9229e205.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product ships as a single CGO_ENABLED=0 static Go binary, cross-compilable to six targets (darwin/linux/windows × amd64/arm64) with one command. -- evidence: [README.md#L89-L90](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L89-L90), [README.md#L59-L72](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L59-L72) (`clm_4d145a2382c6e85acbd2fee2d0cfe35c649fbc5b053123a6b15dc51bb09af396`)

## design-choices (2 claim(s))

- [observation/documented] Configuration is declared in reasonix.toml covering providers, the agent, enabled tools, and plugins, with no hardcoded models; DeepSeek ships as a preset and any OpenAI-compatible endpoint is a config entry. -- evidence: [README.md#L59-L72](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L59-L72) (`clm_a45064f0cf2a7e9b1dc3fa3829cff1c3b33fb0d7f0d68672338cbf300d4a2bb7`)
- [observation/documented] MCP servers contribute tools, prompts, and resources, and Extension Protocol v1 sidecars can intercept runtime events and contribute providers and structured UI. -- evidence: [README.md#L59-L72](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L59-L72) (`clm_9215fdb78259aba7db133f138b162abff61b43d56b8ac1e817e2f0840aca51b3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: build from source with `make build` (bin/reasonix) and `make cross` (dist/), and build desktop packages via scripts/desktop-build.sh one platform per run. -- evidence: [README.md#L130-L133](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L130-L133), [README.md#L140-L142](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L140-L142) (`clm_e958c0fbbe5be228c6ca2ed11c36fa5639a2e866096bfc784b7347875f5cce71`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] Reasonix implements Agent Client Protocol v1 as an NDJSON JSON-RPC 2.0 agent over stdin/stdout, launched via `reasonix acp`, with diagnostics sent to stderr. -- evidence: [docs/ACP.md#L36-L39](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L36-L39), [docs/ACP.md#L11-L14](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L11-L14), [docs/ACP.md#L26-L30](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L26-L30) (`clm_21363203e0d16a36e77c20e30ff62c28629db51f56eb9331d3e79c5f67dcc4fe`)
- [observation/documented] ACP exposes session lifecycle methods including session/new, load, resume, prompt, cancel, list, close, and delete, each session owning an isolated controller, workspace root, model, and transcript. -- evidence: [docs/ACP.md#L117-L119](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L117-L119), [docs/ACP.md#L121-L130](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L121-L130) (`clm_30aba16090a5c19f0648f37a29def9e3550668490d5b538de0f1c2ff6eceeebb`)
- [observation/documented] Session controls are split into independent axes: collaboration mode (normal/plan/goal), model, reasoning effort, and permission preset (read-only, workspace-write, danger-full-access), set via session/set_config_option. -- evidence: [docs/ACP.md#L142-L147](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L142-L147), [docs/ACP.md#L149-L151](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L149-L151) (`clm_da8966472920f310d6957f187da3ab5271b2f032c0595a1bd6d17c7cfceae7c6`)
- [observation/documented] A vendor extension `_reasonix.io/session/steer` provides mid-turn guidance, returning steer_accepted or queued_followup after durably committing the guidance. -- evidence: [docs/ACP.md#L273-L278](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L273-L278), [docs/ACP.md#L253-L265](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L253-L265) (`clm_b3568155dda85e633753e0ea9b6c02fdc0302fbd51a590cd9a9e40269d7d4be1`)
- [observation/documented] A durable session inbox extension supports enqueue, list, get, update, delete, move, setPaused, retry, and refresh operations on persisted follow-up work. -- evidence: [docs/ACP.md#L292-L295](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L292-L295), [docs/ACP.md#L297-L305](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L297-L305) (`clm_914cecc3c84bfac1020fca791a18c6320ef4fae15a9104da1016f89375c9057a`)
- [observation/documented] When the ACP client advertises fs.readTextFile, fs.writeTextFile, or terminal capabilities, eligible file operations route through editor unsaved buffers and foreground commands through a client-owned terminal; non-UTF-8 files stay on the local path. -- evidence: [docs/ACP.md#L77-L85](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L77-L85) (`clm_a7426a9beb75edf6263e23d284cbb6a84a1c91ed6488ce8ff01da51d48897d62`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Permission presets are read-only, workspace-write, and danger-full-access; tool-approval changes update the gate in place without rebuilding the session controller. -- evidence: [docs/ACP.md#L142-L147](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L142-L147), [docs/ACP.md#L169-L171](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/docs/ACP.md#L169-L171) (`clm_44183ae25a0abfc887cd7e2b66eebd2e869c60d133b5a891384bd60e3b845b15`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building the CLI requires Go 1.26+ with a pinned toolchain directive; the desktop build additionally requires Node 24+ and pnpm 10 for the frontend and Electron shell. -- evidence: [README.md#L137-L138](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L137-L138), [README.md#L127-L128](https://github.com/esengine/DeepSeek-Reasonix/blob/8679e1f0b614467ad57aea364b58c478b365e05a/README.md#L127-L128) (`clm_107a38b861461958cba9f3aa17a9dde21b799842df31b40e75f5cc4fc6f6b501`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

