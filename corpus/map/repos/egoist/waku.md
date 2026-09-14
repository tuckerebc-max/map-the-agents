# egoist/waku

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 968d42dd38b7 @ 623975403b923962

## Summary (orientation draft, not independently verified)

Waku is a Rust/GPUI native desktop app for working with local coding-agent CLIs, built around a standalone waku-daemon and a versioned WebSocket protocol, with a browser client sharing the same wire contract. Evidence covers product architecture, supported agents, install paths, changelog features, and contributor workflow rules.

## Source coverage

Source coverage (partial): 3 of 16 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Waku is a native desktop app for working with local coding agents, built in Rust with GPUI, keeping projects, sessions, and transcripts on the user's machine. -- evidence: [README.md#L3-L5](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L3-L5)
- components (3 claim(s)):
  - [observation/documented] The desktop is an RPC client of a standalone waku-daemon; provider sessions run in waku-core behind the authenticated, versioned WebSocket contract in waku-protocol, and the desktop depends on waku-client rather than the daemon implementation. -- evidence: [README.md#L55-L63](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L55-L63)
  - [observation/documented] The daemon owns task SQLite data, uploaded attachments, provider-native session forks, and all workspace filesystem and Git operations, while the desktop retains only presentation state and a disposable preview cache. -- evidence: [README.md#L55-L63](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L55-L63)
- design-choices (2 claim(s)):
  - [observation/documented] App state is stored locally with no Waku account or remote service required; configuration is split between ~/.waku/app.json (release desktop), temp/app.json (debug), and ~/.waku/settings.json for daemon provider and Computer Use settings. -- evidence: [README.md#L77-L82](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L77-L82), [README.md#L47-L51](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L47-L51)
  - [observation/documented] The app supports queueing or steering follow-up messages while an agent works, switching models, reasoning effort, and access modes from a shared interface, and rewinding Git-backed tasks with conversation-aware checkpoints. -- evidence: [README.md#L47-L51](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L47-L51)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: development requires Rust 1.96 or newer and Bun, uses `bun install` and `bun run dev`, and contributors should read CONTRIBUTING.md for the workflow and checks; release maintainers should also read RELEASING.md. -- evidence: [README.md#L96-L100](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L96-L100), [README.md#L111-L112](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L111-L112), [README.md#L102-L105](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L102-L105)
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to assume `bun ./scripts/dev.ts` is already running and owns the Waku Debug.app process, to avoid starting a second watcher or manually relaunching, and to validate the freshly rebuilt debug app after edits. -- evidence: [AGENTS.md#L5-L14](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/AGENTS.md#L5-L14)
- skills-patterns (1 claim(s)):
  - [observation/documented] Waku discovers provider-native slash commands and skills from installed agent CLIs, including multiline YAML descriptions, and invokes Codex, Pi, and Oh My Pi skills with their native syntax. -- evidence: [CHANGELOG.md#L76-L83](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/CHANGELOG.md#L76-L83), [CHANGELOG.md#L49-L55](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/CHANGELOG.md#L49-L55)
- interfaces (2 claim(s)):
  - [observation/documented] The desktop's Settings → Daemon page can expose the child daemon on a fixed port, configure exact browser origins, and copy its stable authentication token; the daemon remains loopback-only by default. -- evidence: [README.md#L77-L82](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L77-L82)
- memory-state (1 claim(s)):
More evidence: [full detail](waku.detail.md)

Metadata and full claim list: [full detail](waku.detail.md)
Human notes ([notes](waku.notes.md), never overwritten by build)

[Back to map index](../../index.md)
