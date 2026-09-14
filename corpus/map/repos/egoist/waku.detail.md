# egoist/waku -- full detail

[Back to orientation](waku.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/egoist/waku/968d42dd38b78d28f46c36abb3d00410a4759957/623975403b923962.json](../../../wiki/dossiers/egoist/waku/968d42dd38b78d28f46c36abb3d00410a4759957/623975403b923962.json)

## specifications (1 claim(s))

- [observation/documented] Waku is a native desktop app for working with local coding agents, built in Rust with GPUI, keeping projects, sessions, and transcripts on the user's machine. -- evidence: [README.md#L3-L5](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L3-L5) (`clm_795605d98e326819d8e94b5cfb4f0aba6e3aed5806476995f9c15f1ea851eb32`)

## components (3 claim(s))

- [observation/documented] The desktop is an RPC client of a standalone waku-daemon; provider sessions run in waku-core behind the authenticated, versioned WebSocket contract in waku-protocol, and the desktop depends on waku-client rather than the daemon implementation. -- evidence: [README.md#L55-L63](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L55-L63) (`clm_085b07a612db2e07162708ae125cc129b2f19a5720035fda27264efdb9064bf6`)
- [observation/documented] The daemon owns task SQLite data, uploaded attachments, provider-native session forks, and all workspace filesystem and Git operations, while the desktop retains only presentation state and a disposable preview cache. -- evidence: [README.md#L55-L63](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L55-L63) (`clm_733a5bfff9a82b89ec02f46f4ca7aeae609e783eaa1da1b668053f0b27f814d8`)
- [observation/documented] A browser client lives at apps/web and uses a generated browser transport in packages/waku-client, with types generated from the Rust protocol and a WebSocket client implementing the same handshake, request IDs, subscriptions, deduplication, and replay cursors as the Rust client. -- evidence: [README.md#L65-L71](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L65-L71) (`clm_046516d0660add3425b55b7835541c16fe0b6f72128e9e8531aab9679b3f8615`)

## design-choices (2 claim(s))

- [observation/documented] App state is stored locally with no Waku account or remote service required; configuration is split between ~/.waku/app.json (release desktop), temp/app.json (debug), and ~/.waku/settings.json for daemon provider and Computer Use settings. -- evidence: [README.md#L77-L82](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L77-L82), [README.md#L47-L51](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L47-L51) (`clm_df56e4f993bd24a0f5564d2bde219886410cb90ed77ec2d51371c79e3e146636`)
- [observation/documented] The app supports queueing or steering follow-up messages while an agent works, switching models, reasoning effort, and access modes from a shared interface, and rewinding Git-backed tasks with conversation-aware checkpoints. -- evidence: [README.md#L47-L51](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L47-L51) (`clm_490f5b6ee1ee9bfacd9afba1f33d6809099828ec6fd0d995bd182f33e7e9394a`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: development requires Rust 1.96 or newer and Bun, uses `bun install` and `bun run dev`, and contributors should read CONTRIBUTING.md for the workflow and checks; release maintainers should also read RELEASING.md. -- evidence: [README.md#L96-L100](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L96-L100), [README.md#L111-L112](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L111-L112), [README.md#L102-L105](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L102-L105) (`clm_56b955c9ddec82b3784a6d0aa6a0842a33ba49d22ba7b3fb7db4aad578047550`)
- [observation/documented] Repository development practice: AGENTS.md instructs contributors to assume `bun ./scripts/dev.ts` is already running and owns the Waku Debug.app process, to avoid starting a second watcher or manually relaunching, and to validate the freshly rebuilt debug app after edits. -- evidence: [AGENTS.md#L5-L14](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/AGENTS.md#L5-L14) (`clm_3fda8856e9c9d3c0133d1e9827f44d4a9cdc82c09d2a1f37db15efc6ce3b6168`)

## skills-patterns (1 claim(s))

- [observation/documented] Waku discovers provider-native slash commands and skills from installed agent CLIs, including multiline YAML descriptions, and invokes Codex, Pi, and Oh My Pi skills with their native syntax. -- evidence: [CHANGELOG.md#L76-L83](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/CHANGELOG.md#L76-L83), [CHANGELOG.md#L49-L55](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/CHANGELOG.md#L49-L55) (`clm_c3fa5df1dd0ae9d920e62a6e7a013929d934a74d6c7cd67267064401f56057e4`)

## interfaces (2 claim(s))

- [observation/documented] The desktop's Settings → Daemon page can expose the child daemon on a fixed port, configure exact browser origins, and copy its stable authentication token; the daemon remains loopback-only by default. -- evidence: [README.md#L77-L82](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L77-L82) (`clm_403b5bd15160d4db108a59740d1c844418e7100cf38ac655c8f7bee21b37c44a`)
- [observation/documented] Waku detects installed agent CLIs automatically and uses each provider's native structured protocol and session continuity; supported agents include Amp, Claude Code, Codex CLI, Cursor CLI, Fx, Grok Build, Kimi Code, OpenCode, and Pi. -- evidence: [README.md#L31-L39](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L31-L39), [README.md#L41-L43](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L41-L43) (`clm_d9cd668c8a8268e7957bb00b6e5b01e94116a4b7362bbe6b7f212e228eaea534`)

## memory-state (1 claim(s))

- [observation/documented] Projectless task workspaces live on the daemon host under ~/.waku/projects/<date>/<slug>, and the daemon migrates workspaces from the older ~/.waku/<date>/<slug> layout on first load. -- evidence: [README.md#L73-L75](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L73-L75) (`clm_dee6181fcef070adbb566188d8cf6f6937b05a9f3ee6836a104e3ca4fa9f76f6`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation is documented per platform: a signed self-updating .dmg on macOS, a curl-piped install script placing files in ~/.local without root on Linux, and a per-user self-updating Setup.exe plus portable .zip on Windows. -- evidence: [README.md#L17-L19](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L17-L19), [README.md#L13-L15](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L13-L15), [README.md#L9-L9](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L9-L9), [README.md#L21-L25](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L21-L25) (`clm_16a73780e69fc98ea02150586325840d298e925cdbdc7d068a5a39ea14d633f6`)

## limitations (1 claim(s))

- [observation/documented] When connected to an externally managed daemon, the local folder picker and PTY are unavailable until the protocol gains daemon-host picker and terminal-stream endpoints; the embedded browser and experimental computer-use integration are currently macOS-only. -- evidence: [README.md#L107-L109](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L107-L109), [README.md#L84-L88](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L84-L88) (`clm_f9694f1930b71ce797e0d4c510a656d43de690afc22ddf864901b2eed36c4f55`)

## relevance (1 claim(s))

- [observation/documented] The project is licensed under GNU General Public License v3.0 only and accepts sponsorship via GitHub Sponsors. -- evidence: [README.md#L116-L116](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L116-L116), [README.md#L120-L120](https://github.com/egoist/waku/blob/968d42dd38b78d28f46c36abb3d00410a4759957/README.md#L120-L120) (`clm_4adc0dc14740729545bd27049a2c4ff2baf938bd741d8fc031f7ca66c6eef03e`)

