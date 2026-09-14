# halfwhey/claudraband -- full detail

[Back to orientation](claudraband.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/halfwhey/claudraband/d2b6a7d1836ff55d77367ba55c0a175752105e0c/4c0e8208ff0b9c40.json](../../../wiki/dossiers/halfwhey/claudraband/d2b6a7d1836ff55d77367ba55c0a175752105e0c/4c0e8208ff0b9c40.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project provides resumable non-interactive workflows, an HTTP daemon for remote or headless session control, an ACP server for editor integration, and a TypeScript library for building custom tools. -- evidence: [README.md#L23-L26](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L23-L26) (`clm_6248154111f65c677675a3ddc13a16e7e6b48fde8fad797e12892503c1ff0bd8`)

## design-choices (1 claim(s))

- [observation/documented] The tool wraps the official Claude Code TUI in a controlled terminal rather than replacing it; it does not touch OAuth, and every interaction runs through a real Claude Code session with authentication via Claude Code. -- evidence: [README.md#L19-L19](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L19-L19), [README.md#L30-L31](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L30-L31) (`clm_63b640d92add1000117cdb2530236ce74657f5c002214bc4993b8cfc68705c73`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI offers prompt, send, watch, interrupt, status, last, attach, sessions (with close), serve, and acp commands, with flags such as --session, --select, --model, --permission-mode, --backend, and --connect. -- evidence: [docs/cli.md#L115-L115](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L115-L115), [README.md#L93-L98](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L93-L98), [docs/cli.md#L129-L129](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L129-L129), [docs/cli.md#L133-L144](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L133-L144), [README.md#L82-L89](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L82-L89) (`clm_cd6613998a07343aedc784d43582ad4524a9058a26287cb7fa7955b368ce15df`)
- [observation/documented] The daemon exposes an HTTP API mirroring CLI verbs: POST /sessions, /prompt, /send, /interrupt, GET /sessions/:id/status, /last, and an SSE /watch endpoint, with JSON error bodies and 400/404/409/500 statuses. -- evidence: [docs/daemon-api.md#L17-L17](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L17-L17), [docs/daemon-api.md#L276-L276](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L276-L276), [docs/daemon-api.md#L282-L287](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L282-L287), [docs/daemon-api.md#L19-L27](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L19-L27) (`clm_6d9665f090b2c247f9936ab72b25265b23363cbdc18d2c9b4ad7a749efdc45c9`)
- [observation/documented] The SSE watch stream sends a ready event, then JSON events with monotonically increasing seq values; kinds include user_message, assistant_text, assistant_thinking, tool_call, tool_result, turn_end, system, and error, plus permission_request events. -- evidence: [docs/daemon-api.md#L238-L238](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L238-L238), [docs/daemon-api.md#L266-L266](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L266-L266), [docs/daemon-api.md#L255-L262](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L255-L262), [docs/daemon-api.md#L244-L244](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L244-L244) (`clm_b66cb0c76f0df4396995fb17655289c3576156910a1254b20e646a8955b36732`)
- [observation/documented] The --select flag answers pending AskUserQuestion or permission prompts using Claude's raw option numbers (the bypass-permissions warning is option 2); prompt --select waits for the following turn while send --select is fire-and-forget. -- evidence: [docs/cli.md#L28-L32](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L28-L32), [docs/cli.md#L214-L217](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L214-L217) (`clm_25625fcc2fee98b48d6ce5c43514c0b1adae142e47bd124fe765b4e4adf498b3`)

## memory-state (1 claim(s))

- [observation/documented] Live sessions are tracked in ~/.claudraband/; the sessions command lists only live entries, while prompt or send with --session auto-resume saved sessions even when no longer live. -- evidence: [README.md#L123-L127](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L123-L127), [README.md#L121-L121](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L121-L121), [docs/cli.md#L12-L12](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L12-L12) (`clm_1994a38214d3ac14c93e344c135617c9cd90e713ee0c3db67fa8eddaa4e301b4`)

## orchestration (1 claim(s))

- [observation/documented] Sessions run inside tmux by default both locally and in the daemon; an experimental, slower headless xterm backend exists as a fallback, and the auto backend prefers tmux then xterm. -- evidence: [docs/cli.md#L117-L117](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L117-L117), [docs/cli.md#L195-L199](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L195-L199), [README.md#L104-L104](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L104-L104), [README.md#L100-L100](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L100-L100) (`clm_2d4690e8a4fb811178d51adfe17e5d2a0053ec2459e03cdc5304b7a4408b62ad`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The package bundles Claude Code @anthropic-ai/claude-code@2.1.96, and the CLAUDRABAND_CLAUDE_PATH environment variable can override the binary path. -- evidence: [docs/cli.md#L14-L14](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L14-L14), [README.md#L53-L53](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L53-L53) (`clm_87b62e767427d1031de95864644fb992ad7f3d919ec509c36e0ea92afaf119c0`)
- [observation/documented] Runtime requirements are Node.js or Bun, an already-authenticated Claude Code, and tmux for the first-class local and daemon-backed workflow. -- evidence: [README.md#L38-L40](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L38-L40) (`clm_55afbbcbf562191b1161845d4c711601b71ea07acf2250a10ce06bb87f23a909`)

## limitations (1 claim(s))

- [observation/documented] The project is explicitly experimental and geared toward personal, ad-hoc usage rather than replacing the Claude SDK; attach only works on live sessions and does not restart dead ones. -- evidence: [README.md#L9-L9](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L9-L9), [docs/cli.md#L93-L93](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L93-L93), [README.md#L123-L127](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L123-L127), [README.md#L30-L31](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L30-L31) (`clm_58f61386aa9b2856f068b87dc4cef410fecf5f78dbed43e20b5c8cf5f8e8c015`)

## relevance (1 claim(s))

- [observation/documented] ACP support lets external frontends such as Toad and Zed drive Claude Code through claudraband, with session follow and resume supported while a real Claude Code pane remains underneath. -- evidence: [README.md#L117-L117](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L117-L117), [README.md#L139-L139](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L139-L139), [README.md#L143-L143](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L143-L143), [README.md#L149-L149](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L149-L149) (`clm_ee9d8bd75283c9a5b79f7174b9e3a64fdbcb7158f8f948ce0a1c6e885e46d27c`)

