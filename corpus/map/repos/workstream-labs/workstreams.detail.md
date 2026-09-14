# workstream-labs/workstreams -- full detail

[Back to orientation](workstreams.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/workstream-labs/workstreams/ef30f54b40fe58a556e100a95a0b745e842492e0/e276e1598c1de89e.json](../../../wiki/dossiers/workstream-labs/workstreams/ef30f54b40fe58a556e100a95a0b745e842492e0/e276e1598c1de89e.json)

## specifications (1 claim(s))

- [observation/documented] Workstreams is described as an IDE for orchestrating parallel AI coding agents, each running in an isolated git worktree. -- evidence: [README.md#L3-L3](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L3-L3) (`clm_225a7453cc4fbe74be088ceb941184b33e133b7ff7b58a2eb391c9834e2579c6`)

## components (2 claim(s))

- [observation/documented] The project ships as a macOS desktop app distributed via DMG installers for Apple Silicon (arm64) and Intel (x64), with built-in auto-update. -- evidence: [README.md#L24-L24](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L24-L24), [README.md#L11-L11](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L11-L11), [README.md#L9-L9](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L9-L9) (`clm_048a6eae2350834a948877ff5b4f0f3431d66b73e6785d9f53c969172ec35d99`)
- [observation/documented] An orchestrator sidebar manages multiple git worktrees per repository, showing real-time addition/deletion counts and preserving per-worktree terminals, editors, and state. -- evidence: [README.md#L30-L30](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L30-L30) (`clm_453f7343d96facf90ca6b6c523e32536b7d398b751f12370e6c3132c71bf03fc`)

## design-choices (1 claim(s))

- [observation/documented] Each workstream is defined with a natural-language prompt and an agent choice, and gets its own isolated git worktree. -- evidence: [README.md#L38-L38](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L38-L38) (`clm_213b19c0d2513292ea35d7c73c15da5f706ba1c68b51a702a9b2388535d65e09`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors clone, run bun install and bun link, run tests with bun test, and submit small PRs from main after adding tests. -- evidence: [CONTRIBUTING.md#L14-L18](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L14-L18), [CONTRIBUTING.md#L40-L40](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L40-L40), [CONTRIBUTING.md#L35-L38](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L35-L38), [CONTRIBUTING.md#L5-L10](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L5-L10) (`clm_49f53e40598741ec4399cc9660a585d71fac53097d4169cd5a51ed085219201b`)
- [observation/documented] Repository development practice: the codebase is organized as packages/core (shared engine), apps/cli (raw-ANSI TUI, one file per command), apps/desktop (WIP), and bun:test tests; runtime state lives in gitignored .workstreams/. -- evidence: [CONTRIBUTING.md#L22-L29](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L22-L29), [CONTRIBUTING.md#L31-L31](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L31-L31) (`clm_42996f6c0ef0ccdada72823ee04b1ec0344b3341a2d059d0532834ef13e7ec66`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product is agent-agnostic and reportedly works with Claude, Codex, Aider, and other agents. -- evidence: [README.md#L5-L5](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L5-L5) (`clm_1b3c529982c492b4553b00a69c106edd15de05b871a3d8136191bd39d4be1141`)
- [observation/documented] A CLI named `ws` (in apps/cli) supports commands such as init, create, run, and dashboard for terminal-driven workstream management. -- evidence: [README.md#L46-L46](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L46-L46), [README.md#L48-L54](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L48-L54) (`clm_7864cacbe35ca983fa3a01bd85fffa5ed6fd9bfd90f0e05c31a252523173821f`)
- [observation/documented] Users can leave inline comments on split-side diffs and send them to Claude as structured prompts containing file path, line number, and diff context. -- evidence: [README.md#L34-L34](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L34-L34) (`clm_3cb340164dbe4116e1235090f0b1e66fd8c273bdffb2247313f8b9b509bda963`)

## memory-state (1 claim(s))

- [observation/documented] Claude Code lifecycle events (idle, working, awaiting permission, ready for review) are tracked per worktree via hooks and shown as animated sidebar status indicators. -- evidence: [README.md#L42-L42](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L42-L42) (`clm_089206d0451d8d43c51a4557030254f40a5b5be51271b4cd43615de5fb537a71`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running the project requires macOS, Node.js 22, Git, and Bun for CLI installation. -- evidence: [README.md#L58-L58](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L58-L58), [README.md#L70-L72](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L70-L72) (`clm_db28710bcf2c03063fa5a081cde8afa3aeecff4c3aceac7498c2b175be4809c3`)

## limitations (1 claim(s))

- [observation/documented] The app is not yet signed with an Apple certificate, so users must strip the macOS quarantine flag with xattr to avoid a misleading 'damaged app' error. -- evidence: [README.md#L15-L22](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L15-L22) (`clm_040a80a5f2e20aa741c539c25213ff0864db55762df1eb1ccafe8aa6ef50c08b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

