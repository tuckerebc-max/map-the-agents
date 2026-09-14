# openchamber/openchamber

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1636fd2bf8e4 @ d00ddc4376c3a35c

## Summary (orientation draft, not independently verified)

OpenChamber uses OpenCode to run coding agents, calling official OpenCode APIs through @opencode-ai/sdk/v2; the CLI/Web and VS Code surfaces use the user's installed OpenCode CLI. The CLI exposes commands such as status, connect-url --qr, tunnel start, startup enable, logs, stop, and update, and binds to localhost by default with --lan and --ui-password options. Evidence coverage: 145 of 178 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (5 claim(s)):
  - [observation/documented] Session Goals let a user set a finish line; the system checks results after each turn and keeps the agent working until the goal completes, the agent is blocked, or a user-set limit is reached, continuing even after the app is closed. -- evidence: [README.md#L32-L32](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L32-L32)
  - [observation/documented] Multi-run assigns the same task to up to five models in separate sessions with optional worktrees, and Fusion can combine the strongest parts of those runs into a new session. -- evidence: [README.md#L36-L36](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L36-L36)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md mandates loading every matching project skill and nearest DOCUMENTATION.md before editing, treats skill loading as required rather than optional, and requires stopping to resolve conflicts between guidance sources. -- evidence: [AGENTS.md#L13-L17](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L13-L17), [AGENTS.md#L11-L11](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L11-L11), [AGENTS.md#L19-L21](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L19-L21), [AGENTS.md#L82-L87](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L82-L87)
  - [observation/documented] Repository development practice: contributors validate changes with package.json scripts, run 'bun run dead-code' after file/export changes, and run 'bunx oxlint' with a vendored anti-slop plugin on new or substantially rewritten TypeScript files. -- evidence: [AGENTS.md#L133-L140](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/AGENTS.md#L133-L140)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands such as status, connect-url --qr, tunnel start, startup enable, logs, stop, and update, and binds to localhost by default with --lan and --ui-password options. -- evidence: [README.md#L116-L116](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L116-L116), [README.md#L106-L114](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/README.md#L106-L114)
  - [observation/documented] The server exposes WebSocket routes (/api/event/ws, /api/global/event/ws, /api/terminal/ws) and SSE routes (/api/event, /api/global/event, /api/notifications/stream, /api/openchamber/events) that reverse proxies must pass through unbuffered. -- evidence: [docs/REVERSE_PROXY.md#L13-L23](https://github.com/openchamber/openchamber/blob/1636fd2bf8e4e29ee82fae3f4b2326195d9de825/docs/REVERSE_PROXY.md#L13-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](openchamber.detail.md)

Metadata and full claim list: [full detail](openchamber.detail.md)
Human notes ([notes](openchamber.notes.md), never overwritten by build)

[Back to map index](../../index.md)
