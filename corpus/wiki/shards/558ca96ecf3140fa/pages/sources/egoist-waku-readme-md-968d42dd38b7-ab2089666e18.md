---
access: public
aliases: []
claim_ids:
- clm_046516d0660add3425b55b7835541c16fe0b6f72128e9e8531aab9679b3f8615
- clm_085b07a612db2e07162708ae125cc129b2f19a5720035fda27264efdb9064bf6
- clm_16a73780e69fc98ea02150586325840d298e925cdbdc7d068a5a39ea14d633f6
- clm_403b5bd15160d4db108a59740d1c844418e7100cf38ac655c8f7bee21b37c44a
- clm_490f5b6ee1ee9bfacd9afba1f33d6809099828ec6fd0d995bd182f33e7e9394a
- clm_4adc0dc14740729545bd27049a2c4ff2baf938bd741d8fc031f7ca66c6eef03e
- clm_56b955c9ddec82b3784a6d0aa6a0842a33ba49d22ba7b3fb7db4aad578047550
- clm_733a5bfff9a82b89ec02f46f4ca7aeae609e783eaa1da1b668053f0b27f814d8
- clm_795605d98e326819d8e94b5cfb4f0aba6e3aed5806476995f9c15f1ea851eb32
- clm_d9cd668c8a8268e7957bb00b6e5b01e94116a4b7362bbe6b7f212e228eaea534
- clm_dee6181fcef070adbb566188d8cf6f6937b05a9f3ee6836a104e3ca4fa9f76f6
- clm_df56e4f993bd24a0f5564d2bde219886410cb90ed77ec2d51371c79e3e146636
- clm_f9694f1930b71ce797e0d4c510a656d43de690afc22ddf864901b2eed36c4f55
maturity: draft
page_id: pg_66300620a16c54658ab3ab2089666e18
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d76612cdd51155da99fc20dd87a3646e
title: egoist/waku/README.md @ 968d42dd38b7
updated_at: '2026-09-14T01:47:10Z'
---

# egoist/waku/README.md @ 968d42dd38b7

<!-- rcw:begin owner=source:src_d76612cdd51155da99fc20dd87a3646e block=evidence -->
- A browser client lives at apps/web and uses a generated browser transport in packages/waku-client, with types generated from the Rust protocol and a WebSocket client implementing the same handshake, request IDs, subscriptions, deduplication, and replay cursors as the Rust client. [@claim:clm_046516d0660add3425b55b7835541c16fe0b6f72128e9e8531aab9679b3f8615]
- The desktop is an RPC client of a standalone waku-daemon; provider sessions run in waku-core behind the authenticated, versioned WebSocket contract in waku-protocol, and the desktop depends on waku-client rather than the daemon implementation. [@claim:clm_085b07a612db2e07162708ae125cc129b2f19a5720035fda27264efdb9064bf6]
- Installation is documented per platform: a signed self-updating .dmg on macOS, a curl-piped install script placing files in ~/.local without root on Linux, and a per-user self-updating Setup.exe plus portable .zip on Windows. [@claim:clm_16a73780e69fc98ea02150586325840d298e925cdbdc7d068a5a39ea14d633f6]
- The desktop's Settings → Daemon page can expose the child daemon on a fixed port, configure exact browser origins, and copy its stable authentication token; the daemon remains loopback-only by default. [@claim:clm_403b5bd15160d4db108a59740d1c844418e7100cf38ac655c8f7bee21b37c44a]
- The app supports queueing or steering follow-up messages while an agent works, switching models, reasoning effort, and access modes from a shared interface, and rewinding Git-backed tasks with conversation-aware checkpoints. [@claim:clm_490f5b6ee1ee9bfacd9afba1f33d6809099828ec6fd0d995bd182f33e7e9394a]
- The project is licensed under GNU General Public License v3.0 only and accepts sponsorship via GitHub Sponsors. [@claim:clm_4adc0dc14740729545bd27049a2c4ff2baf938bd741d8fc031f7ca66c6eef03e]
- Repository development practice: development requires Rust 1.96 or newer and Bun, uses `bun install` and `bun run dev`, and contributors should read CONTRIBUTING.md for the workflow and checks; release maintainers should also read RELEASING.md. [@claim:clm_56b955c9ddec82b3784a6d0aa6a0842a33ba49d22ba7b3fb7db4aad578047550]
- The daemon owns task SQLite data, uploaded attachments, provider-native session forks, and all workspace filesystem and Git operations, while the desktop retains only presentation state and a disposable preview cache. [@claim:clm_733a5bfff9a82b89ec02f46f4ca7aeae609e783eaa1da1b668053f0b27f814d8]
- Waku is a native desktop app for working with local coding agents, built in Rust with GPUI, keeping projects, sessions, and transcripts on the user's machine. [@claim:clm_795605d98e326819d8e94b5cfb4f0aba6e3aed5806476995f9c15f1ea851eb32]
- Waku detects installed agent CLIs automatically and uses each provider's native structured protocol and session continuity; supported agents include Amp, Claude Code, Codex CLI, Cursor CLI, Fx, Grok Build, Kimi Code, OpenCode, and Pi. [@claim:clm_d9cd668c8a8268e7957bb00b6e5b01e94116a4b7362bbe6b7f212e228eaea534]
- Projectless task workspaces live on the daemon host under ~/.waku/projects/<date>/<slug>, and the daemon migrates workspaces from the older ~/.waku/<date>/<slug> layout on first load. [@claim:clm_dee6181fcef070adbb566188d8cf6f6937b05a9f3ee6836a104e3ca4fa9f76f6]
- App state is stored locally with no Waku account or remote service required; configuration is split between ~/.waku/app.json (release desktop), temp/app.json (debug), and ~/.waku/settings.json for daemon provider and Computer Use settings. [@claim:clm_df56e4f993bd24a0f5564d2bde219886410cb90ed77ec2d51371c79e3e146636]
- When connected to an externally managed daemon, the local folder picker and PTY are unavailable until the protocol gains daemon-host picker and terminal-stream endpoints; the embedded browser and experimental computer-use integration are currently macOS-only. [@claim:clm_f9694f1930b71ce797e0d4c510a656d43de690afc22ddf864901b2eed36c4f55]
<!-- rcw:end owner=source:src_d76612cdd51155da99fc20dd87a3646e block=evidence -->

## Researcher notes

