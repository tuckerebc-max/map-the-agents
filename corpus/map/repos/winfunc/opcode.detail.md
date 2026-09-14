# winfunc/opcode -- full detail

[Back to orientation](opcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/winfunc/opcode/70c16d8a4910db48cd9684aeacdd431caefd7d71/1501a42f650f8975.json](../../../wiki/dossiers/winfunc/opcode/70c16d8a4910db48cd9684aeacdd431caefd7d71/1501a42f650f8975.json)

## specifications (1 claim(s))

- [observation/documented] opcode is a desktop GUI application and toolkit for Claude Code, supporting custom agent creation, interactive session management, and background agent execution. -- evidence: [README.md#L39-L39](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L39-L39), [README.md#L7-L12](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L7-L12) (`clm_5610ba2c29b2cf8fecd5ca977b8420b90a94d0370c1614b1ac5d85a0da92fac0`)

## components (2 claim(s))

- [observation/documented] The stack comprises a React 18 + TypeScript + Vite 6 frontend, a Rust backend using Tauri 2, Tailwind CSS v4 with shadcn/ui, and SQLite via rusqlite, with Bun as package manager. -- evidence: [README.md#L337-L341](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L337-L341) (`clm_1cc5dc55902f1f28c0346ae05858dad6d4e21663ed4e47e2a72e20a47b38df1b`)
- [observation/documented] The Rust backend is organized into Tauri command handlers, a checkpoint module for timeline management, and a process module for process management, with a Rust test suite under src-tauri/tests. -- evidence: [README.md#L345-L358](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L345-L358) (`clm_d785052957aaa61010b4e5deccb7f1ddfc93327cdb01e806ab44c95f5dcfa164`)

## design-choices (1 claim(s))

- [observation/documented] In web mode the frontend falls back from Tauri event listening to browser DOM events, handling both string payloads (Tauri) and object payloads (web) for compatibility. -- evidence: [web_server.design.md#L51-L54](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L51-L54), [web_server.design.md#L39-L49](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L39-L49) (`clm_5a35f847e31f8410e3d1bfd8c5973ce175872b7443703bc7d40f8427ac434a60`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should fork, branch, ensure tests pass, and open PRs with title prefixes like Feature:, Fix:, Docs:, Refactor:, Improve:, or Other:, or risk closure without merging. -- evidence: [CONTRIBUTING.md#L36-L36](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L36-L36), [CONTRIBUTING.md#L9-L12](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L9-L12), [CONTRIBUTING.md#L18-L24](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L18-L24) (`clm_567e8a2284636d696fd1f3032ead04439f194cc29a920f7c8541a4a27c1d545b`)
- [observation/documented] Repository development practice: frontend code should use TypeScript, functional components with hooks, and Tailwind CSS; Rust code should follow standard conventions with cargo fmt, clippy, explicit Result handling, and cargo test. -- evidence: [CONTRIBUTING.md#L49-L53](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L49-L53), [CONTRIBUTING.md#L62-L65](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L62-L65), [CONTRIBUTING.md#L43-L46](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/CONTRIBUTING.md#L43-L46) (`clm_e95ade364d257124b117f70b6de2e344360fe67361d0013b2ea985414f632862`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Web server mode exposes a REST API and WebSocket interface mirroring the desktop app, with request fields for command type (execute/continue/resume), project path, prompt, model, and session id. -- evidence: [web_server.design.md#L58-L67](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L58-L67), [web_server.design.md#L7-L7](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L7-L7) (`clm_0f66fce9ca8aa3aaf49c04ffdb4faf67fee473b700000068f054a789347731ea`)
- [observation/documented] The web server provides cancel and output endpoints at /api/sessions/{sessionId}/cancel and /api/sessions/{sessionId}/output, added because the frontend expected them. -- evidence: [web_server.design.md#L165-L166](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L165-L166) (`clm_14bc4b6623b50c593bc851763570f455b28534bb5cb15d1fc676e9075e1b9869`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] When creating a custom agent, users can configure permissions for file read/write and network access per agent, and agents run in separate processes. -- evidence: [README.md#L133-L136](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L133-L136), [README.md#L383-L387](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L383-L387) (`clm_c1fd597dd809c3e5e2e51e5993826bfbf52ad2c82951888c1442286f9e1efc90`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building from source requires Rust 1.70.0+, Bun, Git, and the Claude Code CLI available on PATH, plus platform-specific system libraries such as webkit2gtk on Linux. -- evidence: [README.md#L200-L202](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L200-L202), [README.md#L186-L190](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L186-L190), [README.md#L209-L224](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L209-L224), [README.md#L180-L184](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L180-L184), [README.md#L192-L198](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/README.md#L192-L198) (`clm_35d7c29340e9b13035ec3e61307c80be70cf44cab79619229b08e571cd3ccafe`)

## limitations (2 claim(s))

- [observation/documented] The web server mode has documented critical issues: sessions interfere via generic events, the cancel endpoint is a stub that does not terminate processes, stderr is not captured, and claude-cancelled events are missing. -- evidence: [web_server.design.md#L373-L373](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L373-L373), [web_server.design.md#L367-L370](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L367-L370) (`clm_169b44fc7dbb7f45478526becf90046d58ab90685c1a9abe27eac80e16f1390b`)
- [observation/documented] Web server mode is described as functional for single-session use but not production-suitable, and web mode runs Claude with the --dangerously-skip-permissions flag with CORS allowing all origins. -- evidence: [web_server.design.md#L373-L373](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L373-L373), [web_server.design.md#L296-L299](https://github.com/winfunc/opcode/blob/70c16d8a4910db48cd9684aeacdd431caefd7d71/web_server.design.md#L296-L299) (`clm_8a42e354eaf7eb9184fee6e07ede8381e4ec1028b71b9864664090430b74aab2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

