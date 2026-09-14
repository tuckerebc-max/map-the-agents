# podiom/podiom

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 78025f740077 @ a58c745d296cbf3b

## Summary (orientation draft, not independently verified)

Selected evidence records: The repository points to docs/requirements/foundation.md as the authoritative foundation specification, at version v1.6. The podiomd daemon embeds the web SPA and uses pure-Go SQLite, so it needs no external web assets or cgo at runtime.

## Source coverage

Source coverage (partial): 3 of 39 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository points to docs/requirements/foundation.md as the authoritative foundation specification, at version v1.6. -- evidence: [README.md#L216-L235](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L216-L235)
- components (2 claim(s)):
  - [observation/documented] The podiomd daemon embeds the web SPA and uses pure-Go SQLite, so it needs no external web assets or cgo at runtime. -- evidence: [README.md#L182-L183](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L182-L183)
  - [observation/documented] The layout includes a thin CLI client (cmd/podiom), a daemon combining web server, scheduler, and core (cmd/podiomd), internal packages, and a Svelte/Vite/TypeScript/Tailwind web UI built into podiomd. -- evidence: [README.md#L204-L210](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L204-L210)
- design-choices (1 claim(s)):
  - [observation/documented] Podiom is local-first: all runtime state lives under one overridable root ($PODIOM_HOME, defaulting to ~/.podiom/), and provider CLIs keep their native authentication and policy controls. -- evidence: [README.md#L212-L212](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L212-L212), [README.md#L190-L192](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L190-L192), [README.md#L110-L115](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L110-L115)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md gives coding-agent guidelines—state assumptions before implementing, keep changes minimal and surgical, and turn tasks into verifiable, test-driven goals. -- evidence: [AGENTS.md#L21-L25](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L21-L25), [AGENTS.md#L49-L52](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L49-L52), [AGENTS.md#L11-L15](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L11-L15)
  - [observation/documented] Repository development practice: provider-specific logic must stay in registries and per-layer tables rather than branching on provider names, with a drift test (TestProviderKnowledgeStaysInRegistry) enforcing this boundary. -- evidence: [AGENTS.md#L67-L67](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L67-L67), [AGENTS.md#L71-L77](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L71-L77), [AGENTS.md#L91-L95](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/AGENTS.md#L91-L95)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Podiom does not replace the provider runtime; it shells out to the native claude and codex CLIs and reuses their models, MCP servers, tools, skills, and authentication. -- evidence: [README.md#L41-L43](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L41-L43)
  - [observation/documented] The web UI defaults to 127.0.0.1:8787, with bind address and port configurable via server.bind and server.port in config.yaml; a browser-native WebSocket endpoint at /api/ws is also documented. -- evidence: [README.md#L198-L200](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L198-L200), [README.md#L216-L235](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L216-L235)
- memory-state (1 claim(s)):
  - [observation/documented] Podiom stores a canonical history for every session and can replay that history onto a fresh backing CLI session when the provider or profile changes. -- evidence: [README.md#L83-L86](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L83-L86)
- orchestration (1 claim(s)):
  - [observation/documented] A goal gives one lead agent an outcome to own over days or weeks; the agent turns it into roadmap tasks and schedules, delegates work, and records periodic reviews with progress, evidence, and next steps. -- evidence: [README.md#L52-L59](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L52-L59), [README.md#L47-L50](https://github.com/Podiom/Podiom/blob/78025f74007775e4e161ab5632ee6a19f616fbc1/README.md#L47-L50)
- tools-permissions (1 claim(s)):
More evidence: [full detail](podiom.detail.md)

Metadata and full claim list: [full detail](podiom.detail.md)
Human notes ([notes](podiom.notes.md), never overwritten by build)

[Back to map index](../../index.md)
