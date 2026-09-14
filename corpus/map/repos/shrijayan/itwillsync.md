# shrijayan/itwillsync

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f12b57bf7385 @ 49324d424dafa83f

## Summary (orientation draft, not independently verified)

itwillsync is an npm-distributed CLI that proxies terminal-based AI coding agents to a phone browser over the local network via QR-code-authenticated WebSocket sessions, with a multi-session hub dashboard. Evidence is mostly README product documentation plus contributor workflow files.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The architecture pairs a node-pty-backed agent process and HTTP/WebSocket server on the laptop with a browser terminal client on the phone, connected via WebSocket with token auth. -- evidence: [README.md#L60-L72](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L60-L72)
  - [observation/documented] The monorepo contains packages for the CLI (main npm package), a web-client browser terminal, a hub dashboard daemon, a landing page, and VitePress docs. -- evidence: [README.md#L199-L206](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L199-L206), [CONTRIBUTING.md#L32-L38](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L32-L38)
- design-choices (4 claim(s)):
  - [observation/documented] The product is agent-agnostic: it works with any terminal-based tool, citing Claude Code, Aider, Codex, Goose, Cline, and Copilot CLI, without vendor lock-in. -- evidence: [README.md#L120-L120](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L120-L120), [README.md#L130-L130](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L130-L130), [README.md#L44-L47](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L44-L47)
  - [observation/documented] Connections run over the local network (or Tailscale) with no cloud component, no accounts, and no telemetry; three connection modes are local WiFi (default), Tailscale, and localhost-only. -- evidence: [README.md#L134-L138](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L134-L138), [README.md#L49-L52](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L49-L52)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use Node 22+ via nvm and pnpm 10+, build packages in order (web-client, hub, CLI) with pnpm build, run pnpm test (optionally with --coverage), and open focused PRs against main with tests and passing CI. -- evidence: [CONTRIBUTING.md#L55-L57](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L55-L57), [CONTRIBUTING.md#L71-L71](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L71-L71), [CONTRIBUTING.md#L9-L11](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L9-L11), [CONTRIBUTING.md#L84-L88](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L84-L88), [CONTRIBUTING.md#L42-L46](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L42-L46), [CONTRIBUTING.md#L67-L69](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L67-L69), [CONTRIBUTING.md#L60-L61](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L60-L61)
  - [observation/documented] Repository development practice: code style is TypeScript with ESM modules, no linter is enforced yet (follow existing patterns), dependencies should stay minimal, and contributions are MIT-licensed. -- evidence: [CONTRIBUTING.md#L105-L107](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L105-L107), [CONTRIBUTING.md#L111-L111](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/CONTRIBUTING.md#L111-L111)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is invoked as npx itwillsync followed by an agent command (e.g. claude, aider, or any terminal command), with no install required but Node.js 20+ needed. -- evidence: [README.md#L30-L30](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L30-L30), [README.md#L24-L28](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L24-L28)
  - [observation/documented] Documented CLI flags include --port (default 7964), --localhost, --tailscale, --local, --no-qr, a setup subcommand, and -h/-v. -- evidence: [README.md#L156-L165](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L156-L165)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A hub daemon provides a multi-session dashboard showing each agent's name, working directory, status, and uptime, with real-time WebSocket updates and tap-to-open full terminal. -- evidence: [README.md#L90-L90](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L90-L90), [README.md#L112-L116](https://github.com/shrijayan/itwillsync/blob/f12b57bf7385cfaedc119a90d147d90e1437a7f2/README.md#L112-L116)
- tools-permissions (1 claim(s)):
More evidence: [full detail](itwillsync.detail.md)

Metadata and full claim list: [full detail](itwillsync.detail.md)
Human notes ([notes](itwillsync.notes.md), never overwritten by build)

[Back to map index](../../index.md)
