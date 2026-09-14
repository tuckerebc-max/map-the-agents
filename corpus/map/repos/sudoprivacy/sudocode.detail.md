# sudoprivacy/sudocode -- full detail

[Back to orientation](sudocode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sudoprivacy/sudocode/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/8fb393471e10b339.json](../../../wiki/dossiers/sudoprivacy/sudocode/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/8fb393471e10b339.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] One scode binary serves copilot, worker, or standalone roles depending on the FsBackend implementation: StdFsBackend (host std::fs), NexusVfsFsBackend (gRPC to remote kernel), or KernelFsBackend (in-process syscalls). -- evidence: [README.md#L170-L171](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L170-L171), [README.md#L192-L195](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L192-L195), [README.md#L188-L190](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L188-L190) (`clm_c70c1ca32d78f554c24a1a2ad80cb4101849d6686668fe0a8ad47c9895a27d56`)

## design-choices (1 claim(s))

- [observation/documented] The project commits to inline-only terminal output (no alternate-screen TUI, no ratatui), local-first operation with zero telemetry by default, and semver stability with no forced auto-updates. -- evidence: [README.md#L92-L104](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L92-L104), [README.md#L108-L119](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L108-L119) (`clm_f7c23209a3ab0f22735ca3e247b046d219f653cb2cd8c0dadf75f4ba8787cd7d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] scode speaks the Agent Communication Protocol natively over two transports sharing one handler chain: `scode acp` over stdio and `scode acp serve --port N` over WebSocket. -- evidence: [docs/acp.md#L3-L4](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L3-L4), [docs/acp.md#L10-L10](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L10-L10), [docs/acp.md#L13-L14](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L13-L14) (`clm_04d08ece3e59789e2123736bd0be72b93e3aa34ff53d91a6b01a689cfe1e4ad7`)
- [observation/documented] The WebSocket server exposes JSON-RPC at ws://localhost:8080/ws plus an embedded interactive Web UI at http://localhost:8080/; both transports share streaming, tool use, elicitation and permission prompting. -- evidence: [docs/acp.md#L21-L22](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L21-L22), [docs/acp.md#L18-L19](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L18-L19) (`clm_2ccf0cc1810d8b21b293ba31acfef57dc1cd325ffc4097959cfd7e39aed03dca`)
- [observation/documented] ACP sessions accept `_meta.sudocode.systemPrompt` (replaces built-in static system-prompt blocks) and `appendSystemPrompt` (appended after them); non-string or empty values are rejected with invalid_params (-32602). -- evidence: [docs/acp.md#L92-L106](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L92-L106), [docs/acp.md#L79-L82](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L79-L82) (`clm_c12ebc788c4fab2c9191876d5b65f2fdd3723ad1837703a063e03cbc4c81d403`)
- [observation/documented] A session/prompt starting with `/` runs as a slash command (e.g. /help, /status, /cost, /model, /compact, /diff, /doctor), and the agent advertises the command table via a session/update notification after session/new or session/load. -- evidence: [docs/acp.md#L166-L175](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L166-L175), [docs/acp.md#L161-L164](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L161-L164), [docs/acp.md#L180-L182](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L180-L182) (`clm_417cdff9cb1fb7401495ead4fb2d106bb82922ce1beaf903f85af3be8fbe5b6d`)
- [observation/documented] Automatic compaction trims oversized tool text (over 8,192 code points) to a head/tail with marker before running a checkpoint pipeline; successful replacement archives the original transcript as `<transcript>.before-compact-<timestamp>`. -- evidence: [docs/acp.md#L236-L245](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L236-L245), [docs/acp.md#L258-L263](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L258-L263) (`clm_2b6ad02d2676386c1605fc8e4caefab386d742f10aa740c46abf7fe901633200`)

## memory-state (3 claim(s))

- [observation/documented] Sessions persist as JSONL under `<cwd>/.scode/sessions/<workspace-fingerprint>/`; session/load restores transcript, model, compaction state and fork lineage, but not permission-mode overrides, background commands, or MCP servers not passed in the request. -- evidence: [docs/acp.md#L274-L279](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L274-L279), [docs/acp.md#L267-L272](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L267-L272) (`clm_08645cf940261c73a8ca3456e070460e7304f72a72951d88369390f182ee166f`)
- [observation/documented] Per-session memory is controlled via `_meta.sudocode.memory`; 'disabled' means the session neither reads nor writes the persistent memory directory, and disabling never deletes existing entries. -- evidence: [docs/acp.md#L135-L157](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L135-L157), [docs/acp.md#L110-L113](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L110-L113), [docs/acp.md#L127-L131](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L127-L131) (`clm_691a52f2580adc08639655701c876431c5dfc948220c486c9175eb04fba15791`)
- [observation/documented] Forking via `session/new` with `_meta.sudocode.forkFrom` copies the source transcript into a new first-class session under the new cwd; the source is read, never modified, and the initialize response advertises sessionFork for feature detection. -- evidence: [docs/acp.md#L325-L330](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L325-L330), [docs/acp.md#L291-L297](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L291-L297) (`clm_b502023c83300e2516d2a13d7084bab111158fc3a64c1a2a1e6ac27308de8618`)

## orchestration (1 claim(s))

- [observation/documented] Sudo Code positions itself as an agent unit, not an orchestrator: it plugs into a nexus-VFS `chat-with-me` mailbox primitive so humans, orchestrators, or peer agents over ACP can drive it. -- evidence: [README.md#L125-L133](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L125-L133), [README.md#L165-L166](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L165-L166) (`clm_6c84ee8add798f08a7ed95ba56f65344fd49176ca2362cb12c366dbcadea80c4`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Authentication supports three modes — subscription (CLAUDE_CODE_OAUTH_TOKEN), proxy (PROXY_AUTH_TOKEN + PROXY_BASE_URL), and api-key (Anthropic, OpenAI, xAI, Gemini, DashScope keys) — with auto-detection in that order. -- evidence: [docs/authentication.md#L6-L10](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/authentication.md#L6-L10), [docs/authentication.md#L3-L4](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/authentication.md#L3-L4), [docs/authentication.md#L14-L18](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/authentication.md#L14-L18) (`clm_80a98ef88606fed64048f87c211ad90e4cd57298bde92d2733167287334378b1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

