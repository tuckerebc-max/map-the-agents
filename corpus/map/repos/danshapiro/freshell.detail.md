# danshapiro/freshell -- full detail

[Back to orientation](freshell.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/danshapiro/freshell/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/101631a4d3dba4f6.json](../../../wiki/dossiers/danshapiro/freshell/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/101631a4d3dba4f6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The stack includes React 18, Redux Toolkit, xterm.js, Monaco, Express, node-pty, WebSocket, Vite, TypeScript, and Vitest-based testing tools. -- evidence: [AGENTS.md#L209-L211](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L209-L211), [README.md#L263-L267](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L263-L267) (`clm_53ee003035769becae444bfa5519e811aba7b091d1cb010c9cb260b07ad4c143`)
- [observation/documented] An extension system supports three pane-type categories: client (static HTML/JS), server (freshell-managed HTTP server with auto port allocation), and CLI (terminal tool wrapped as a pane), installed via a freshell.json manifest in ~/.freshell/extensions/. -- evidence: [README.md#L271-L271](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L271-L271), [README.md#L273-L275](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L273-L275), [README.md#L277-L277](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L277-L277) (`clm_c1582cb515a437647d1fab8673ea9be25f53143aa8270d2b2cf6b62e3b1a0abf`)

## design-choices (1 claim(s))

- [observation/documented] Desktop profiles let multiple independent clients run on one machine, each with its own settings, storage dir, and single-instance lock, configured via ~/.freshell/profiles.json. -- evidence: [README.md#L62-L65](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L62-L65), [README.md#L69-L75](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L69-L75), [README.md#L79-L79](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L79-L79) (`clm_8f22d190a21712bfee9dab2b91c6ae37b946eae95a9fea5eb3076cdb9b144a3a`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors must work in .worktrees worktrees, branch from origin/main, and land all behavior changes via PRs to main; direct pushes to main are forbidden. -- evidence: [AGENTS.md#L14-L27](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L14-L27), [AGENTS.md#L52-L57](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L52-L57) (`clm_53473b5b32ecde3693f71fc4f99e30615539c8a09a07293262019812d3388cf3`)
- [observation/documented] Repository development practice: the project mandates Red-Green-Refactor TDD for all but trivial changes, with both unit and e2e coverage required. -- evidence: [AGENTS.md#L6-L11](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L6-L11) (`clm_b4824d3371b0a5a9f8119543917b38277dde04a38a24275cf5a80c2f7cfbec0d`)
- [observation/documented] Repository development practice: broad test runs go through a shared coordinator gate, with scripts/base-gate.sh validating origin/main from a clean scratch worktree and npm run test:status showing holder info. -- evidence: [AGENTS.md#L30-L36](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L30-L36) (`clm_df259c60ecd967f0eea829a1dba3dbbfb93f4efea3f6b63673891ea4cec168a7`)
- [observation/documented] Repository development practice: destructive process-kill, config-corruption, and restart-storm test suites must run inside a disposable Docker sandbox via scripts/sandbox-test.sh, never on the host. -- evidence: [AGENTS.md#L39-L40](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L39-L40) (`clm_9e3182c806a2916c50ad987eb55d1f67bd414369b86b4c9f8996a27b56319119`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Freshell indexes local session history for Claude Code, Codex, OpenCode, and Amplifier, and can launch terminals for those plus Gemini and Kimi; OpenCode sessions are read directly from its local session database. -- evidence: [README.md#L245-L252](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L245-L252), [README.md#L243-L243](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L243-L243), [README.md#L254-L255](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L254-L255) (`clm_fd486503f8e9dac41768d24e4d42376482f6ec56dba0f1aec016de8f683cbf35`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] For OpenCode sessions, freshell does not set OPENCODE_PERMISSION or pass --dangerously-skip-permissions; OpenCode's own config and OS filesystem permissions govern access. -- evidence: [README.md#L257-L257](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L257-L257) (`clm_4eca9297b4b9fab0023d83f8c1b9ff016e5101a51dcf69d6e741c686d2425da3`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The app requires Node.js 18+ (20+ recommended) plus platform build tools for native modules, and runs on Windows, macOS, and Linux. -- evidence: [README.md#L56-L56](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L56-L56), [README.md#L1-L5](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L1-L5) (`clm_c9ec2b2a9cb6dacd4d75c13afa2a92fe23fa0296b70f49b76ccb8b52fbe9ffdf`)

## limitations (2 claim(s))

- [observation/documented] Stream Deck integration requires Chrome or Edge via WebHID and is not supported inside the freshell desktop app. -- evidence: [README.md#L175-L176](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L175-L176) (`clm_494c70ec6cd111ec4f34658a589406b38c1615c25c95e4edb72ecb4c6d4cddde`)
- [observation/documented] The host pressure dashboard pane is limited to Linux, WSL, and macOS and is not shown on Windows. -- evidence: [README.md#L23-L36](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L23-L36) (`clm_7f77b4ba6f55435a98353f7f92b16c625d66e5a1b96a4f68d5469c809ba1f4b6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

