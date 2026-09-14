# winfunc/opcode

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 70c16d8a4910 @ 1501a42f650f8975

## Summary (orientation draft, not independently verified)

Selected evidence records: opcode is a desktop GUI application and toolkit for Claude Code, supporting custom agent creation, interactive session management, and background agent execution. The stack comprises a React 18 + TypeScript + Vite 6 frontend, a Rust backend using Tauri 2, Tailwind CSS v4 with shadcn/ui, and SQLite via rusqlite, with Bun as package manager.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] opcode is a desktop GUI application and toolkit for Claude Code, supporting custom agent creation, interactive session management, and background agent execution. -- evidence: [README.md#L39-L39](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L39-L39), [README.md#L7-L12](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L7-L12)
- components (2 claim(s)):
  - [observation/documented] The stack comprises a React 18 + TypeScript + Vite 6 frontend, a Rust backend using Tauri 2, Tailwind CSS v4 with shadcn/ui, and SQLite via rusqlite, with Bun as package manager. -- evidence: [README.md#L337-L341](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L337-L341)
  - [observation/documented] The Rust backend is organized into Tauri command handlers, a checkpoint module for timeline management, and a process module for process management, with a Rust test suite under src-tauri/tests. -- evidence: [README.md#L345-L358](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L345-L358)
- design-choices (1 claim(s)):
  - [observation/documented] In web mode the frontend falls back from Tauri event listening to browser DOM events, handling both string payloads (Tauri) and object payloads (web) for compatibility. -- evidence: [web_server.design.md#L51-L54](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L51-L54), [web_server.design.md#L39-L49](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L39-L49)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should fork, branch, ensure tests pass, and open PRs with title prefixes like Feature:, Fix:, Docs:, Refactor:, Improve:, or Other:, or risk closure without merging. -- evidence: [CONTRIBUTING.md#L36-L36](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L36-L36), [CONTRIBUTING.md#L9-L12](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L9-L12), [CONTRIBUTING.md#L18-L24](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L18-L24)
  - [observation/documented] Repository development practice: frontend code should use TypeScript, functional components with hooks, and Tailwind CSS; Rust code should follow standard conventions with cargo fmt, clippy, explicit Result handling, and cargo test. -- evidence: [CONTRIBUTING.md#L49-L53](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L49-L53), [CONTRIBUTING.md#L62-L65](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L62-L65), [CONTRIBUTING.md#L43-L46](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L43-L46)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Web server mode exposes a REST API and WebSocket interface mirroring the desktop app, with request fields for command type (execute/continue/resume), project path, prompt, model, and session id. -- evidence: [web_server.design.md#L58-L67](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L58-L67), [web_server.design.md#L7-L7](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L7-L7)
  - [observation/documented] The web server provides cancel and output endpoints at /api/sessions/{sessionId}/cancel and /api/sessions/{sessionId}/output, added because the frontend expected them. -- evidence: [web_server.design.md#L165-L166](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L165-L166)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] When creating a custom agent, users can configure permissions for file read/write and network access per agent, and agents run in separate processes. -- evidence: [README.md#L133-L136](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L133-L136), [README.md#L383-L387](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L383-L387)
More evidence: [full detail](opcode.detail.md)

Metadata and full claim list: [full detail](opcode.detail.md)
Human notes ([notes](opcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
