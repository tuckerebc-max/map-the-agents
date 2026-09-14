# sudoprivacy/sudocode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a67bb90f5c4b @ 8fb393471e10b339

## Summary (orientation draft, not independently verified)

Sudo Code (scode) is a Rust CLI coding agent speaking ACP over stdio and WebSocket, with three auth modes, JSONL session persistence, per-session system-prompt/memory controls, and a stated inline-only, model-agnostic, local-first design. The nexus-VFS mailbox integration and FsBackend deployment modes are described as design/architecture in README docs. Evidence coverage: 133 of 300 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 30 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] One scode binary serves copilot, worker, or standalone roles depending on the FsBackend implementation: StdFsBackend (host std::fs), NexusVfsFsBackend (gRPC to remote kernel), or KernelFsBackend (in-process syscalls). -- evidence: [README.md#L170-L171](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L170-L171), [README.md#L192-L195](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L192-L195), [README.md#L188-L190](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L188-L190)
- design-choices (1 claim(s)):
  - [observation/documented] The project commits to inline-only terminal output (no alternate-screen TUI, no ratatui), local-first operation with zero telemetry by default, and semver stability with no forced auto-updates. -- evidence: [README.md#L92-L104](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L92-L104), [README.md#L108-L119](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L108-L119)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] scode speaks the Agent Communication Protocol natively over two transports sharing one handler chain: `scode acp` over stdio and `scode acp serve --port N` over WebSocket. -- evidence: [docs/acp.md#L3-L4](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L3-L4), [docs/acp.md#L10-L10](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L10-L10), [docs/acp.md#L13-L14](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L13-L14)
  - [observation/documented] The WebSocket server exposes JSON-RPC at ws://localhost:8080/ws plus an embedded interactive Web UI at http://localhost:8080/; both transports share streaming, tool use, elicitation and permission prompting. -- evidence: [docs/acp.md#L21-L22](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L21-L22), [docs/acp.md#L18-L19](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L18-L19)
- memory-state (3 claim(s)):
  - [observation/documented] Sessions persist as JSONL under `<cwd>/.scode/sessions/<workspace-fingerprint>/`; session/load restores transcript, model, compaction state and fork lineage, but not permission-mode overrides, background commands, or MCP servers not passed in the request. -- evidence: [docs/acp.md#L274-L279](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L274-L279), [docs/acp.md#L267-L272](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L267-L272)
  - [observation/documented] Per-session memory is controlled via `_meta.sudocode.memory`; 'disabled' means the session neither reads nor writes the persistent memory directory, and disabling never deletes existing entries. -- evidence: [docs/acp.md#L135-L157](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L135-L157), [docs/acp.md#L110-L113](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L110-L113), [docs/acp.md#L127-L131](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/acp.md#L127-L131)
- orchestration (1 claim(s)):
  - [observation/documented] Sudo Code positions itself as an agent unit, not an orchestrator: it plugs into a nexus-VFS `chat-with-me` mailbox primitive so humans, orchestrators, or peer agents over ACP can drive it. -- evidence: [README.md#L125-L133](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L125-L133), [README.md#L165-L166](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/README.md#L165-L166)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Authentication supports three modes — subscription (CLAUDE_CODE_OAUTH_TOKEN), proxy (PROXY_AUTH_TOKEN + PROXY_BASE_URL), and api-key (Anthropic, OpenAI, xAI, Gemini, DashScope keys) — with auto-detection in that order. -- evidence: [docs/authentication.md#L6-L10](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/authentication.md#L6-L10), [docs/authentication.md#L3-L4](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/authentication.md#L3-L4), [docs/authentication.md#L14-L18](https://github.com/sudoprivacy/sudocode/blob/a67bb90f5c4b8de1b9b6aee32bc3c0df73c81408/docs/authentication.md#L14-L18)
More evidence: [full detail](sudocode.detail.md)

Metadata and full claim list: [full detail](sudocode.detail.md)
Human notes ([notes](sudocode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
