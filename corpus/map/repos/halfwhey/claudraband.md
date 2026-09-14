# halfwhey/claudraband

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d2b6a7d1836f @ 4c0e8208ff0b9c40

## Summary (orientation draft, not independently verified)

Claudraband is a documented CLI/daemon/library wrapper that runs the official Claude Code TUI inside controlled tmux (or experimental xterm) terminals, exposing resumable sessions via CLI commands, an HTTP daemon API with SSE streaming, and an ACP server for editor frontends.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project provides resumable non-interactive workflows, an HTTP daemon for remote or headless session control, an ACP server for editor integration, and a TypeScript library for building custom tools. -- evidence: [README.md#L23-L26](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L23-L26)
- design-choices (1 claim(s)):
  - [observation/documented] The tool wraps the official Claude Code TUI in a controlled terminal rather than replacing it; it does not touch OAuth, and every interaction runs through a real Claude Code session with authentication via Claude Code. -- evidence: [README.md#L19-L19](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L19-L19), [README.md#L30-L31](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L30-L31)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI offers prompt, send, watch, interrupt, status, last, attach, sessions (with close), serve, and acp commands, with flags such as --session, --select, --model, --permission-mode, --backend, and --connect. -- evidence: [docs/cli.md#L115-L115](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L115-L115), [README.md#L93-L98](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L93-L98), [docs/cli.md#L129-L129](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L129-L129), [docs/cli.md#L133-L144](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L133-L144), [README.md#L82-L89](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L82-L89)
  - [observation/documented] The daemon exposes an HTTP API mirroring CLI verbs: POST /sessions, /prompt, /send, /interrupt, GET /sessions/:id/status, /last, and an SSE /watch endpoint, with JSON error bodies and 400/404/409/500 statuses. -- evidence: [docs/daemon-api.md#L17-L17](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L17-L17), [docs/daemon-api.md#L276-L276](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L276-L276), [docs/daemon-api.md#L282-L287](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L282-L287), [docs/daemon-api.md#L19-L27](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/daemon-api.md#L19-L27)
- memory-state (1 claim(s)):
  - [observation/documented] Live sessions are tracked in ~/.claudraband/; the sessions command lists only live entries, while prompt or send with --session auto-resume saved sessions even when no longer live. -- evidence: [README.md#L123-L127](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L123-L127), [README.md#L121-L121](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L121-L121), [docs/cli.md#L12-L12](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L12-L12)
- orchestration (1 claim(s)):
  - [observation/documented] Sessions run inside tmux by default both locally and in the daemon; an experimental, slower headless xterm backend exists as a fallback, and the auto backend prefers tmux then xterm. -- evidence: [docs/cli.md#L117-L117](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L117-L117), [docs/cli.md#L195-L199](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L195-L199), [README.md#L104-L104](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L104-L104), [README.md#L100-L100](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L100-L100)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The package bundles Claude Code @anthropic-ai/claude-code@2.1.96, and the CLAUDRABAND_CLAUDE_PATH environment variable can override the binary path. -- evidence: [docs/cli.md#L14-L14](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/docs/cli.md#L14-L14), [README.md#L53-L53](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L53-L53)
  - [observation/documented] Runtime requirements are Node.js or Bun, an already-authenticated Claude Code, and tmux for the first-class local and daemon-backed workflow. -- evidence: [README.md#L38-L40](https://github.com/halfwhey/claudraband/blob/d2b6a7d1836ff55d77367ba55c0a175752105e0c/README.md#L38-L40)
- limitations (1 claim(s)):
More evidence: [full detail](claudraband.detail.md)

Metadata and full claim list: [full detail](claudraband.detail.md)
Human notes ([notes](claudraband.notes.md), never overwritten by build)

[Back to map index](../../index.md)
