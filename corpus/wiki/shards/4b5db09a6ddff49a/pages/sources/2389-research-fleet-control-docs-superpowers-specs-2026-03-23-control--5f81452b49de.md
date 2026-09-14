---
access: public
aliases: []
claim_ids:
- clm_101c21d32aa374b9d6fd1efc4891ff0f4a86b4896682c5ff5d594aa07a0b560d
- clm_1262a776ef0c77b153bafac67d8249c28b942f2128b61836a753178b3926eaa2
- clm_3b00d59dec249dcc84975206f9165510ac33cda8d07f33be14aee427cd893989
- clm_41d50af997e98ff064758c1d6a60c61f9e57430e1958486ce41f324ae5be1272
- clm_4710e0ea7da04c5390633f588e7967aaccdd469c76f085280b214dc5504121ef
- clm_5b02b3aca20bfd8d5a546d4345363a8e83da9a8d4a039fa55e1fa6e19b7f176a
- clm_6310a43d48c89d8978f5d98b9625d09a4daa97fb66d62eb5f22d01c437b9156d
- clm_6fcf964319deb6a492a20b2b5b40d61e8b627802d76876554abcc0a3e6b2f746
- clm_788e0bc7d226446d7dc839688fd1d292784e4d744504d7ee2e7a3159d299718a
- clm_987efabd4222cb78734fb62c1687185171090c087cf0e296942ba33c5769fd18
- clm_a50e53a41d3d1cf309220dcdc2c194ad184b148f160f1464cac9d82546ceaa84
- clm_ad94268eb125d83e752a986fae95c635ca830dbe0363ac86745fec53dfc1fc55
- clm_c063ea1083b0ac93069907b7695b83817bb59034697a6ab94536a323f777cc93
- clm_c1d779ed02d99285fcd0e14e4fc4d53ea6758469cfa2f7a85a52c285420a5640
- clm_ce2cca6205064568a74c3b9c781ee67bf1b1df2ccb0f1aa43d3ba414a92319f8
- clm_da651159fec9ccd2eecf3aef0bf91424bca37ffbfa805c82bc0bc7935797b9b3
- clm_e051b41e70da86e4d6f065d67a7a5d8846c46a33c92623d5495ac6d3a23f3bc0
- clm_e4161f92de2ed2adf3b7c52f706c700a52bb128cfef5cc02b2eb1f1c2e3da42d
- clm_fad476195077eb2ab6b45f9ba809406efb1900d3feceee0d1715ce566fd6b558
maturity: draft
page_id: pg_140769cd8c5c5bdbb47a5f81452b49de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4b8c3616b6125cb48740031cc4bde733
title: 2389-research/fleet-control/docs/superpowers/specs/2026-03-23-control-plane-design.md
  @ efe2657f5465
updated_at: '2026-09-14T01:26:04Z'
---

# 2389-research/fleet-control/docs/superpowers/specs/2026-03-23-control-plane-design.md @ efe2657f5465

<!-- rcw:begin owner=source:src_4b8c3616b6125cb48740031cc4bde733 block=evidence -->
- Post-build implementation notes state the terminology was renamed from agent to pane: endpoints use /panes/ and MCP tools include list_panes, get_pane, stop_pane, send_to_pane, and get_pane_conversation. [@claim:clm_101c21d32aa374b9d6fd1efc4891ff0f4a86b4896682c5ff5d594aa07a0b560d]
- Core principles include observer-not-launcher, zero agent instrumentation, CLI/MCP parity over one internal API, a single binary, CGO-free builds, and no elevated privileges. [@claim:clm_1262a776ef0c77b153bafac67d8249c28b942f2128b61836a753178b3926eaa2]
- The design spec describes a Go binary `control` that observes and manages running AI agents via tmux introspection, offering visibility, stopping, and session history. [@claim:clm_3b00d59dec249dcc84975206f9165510ac33cda8d07f33be14aee427cd893989]
- The architecture has three layers in one Go module: a `controld` daemon, a `control` CLI, and an MCP server, with the CLI and MCP as thin clients over the daemon's HTTP API. [@claim:clm_41d50af997e98ff064758c1d6a60c61f9e57430e1958486ce41f324ae5be1272]
- A redaction pass strips secret patterns (API keys, KEY/SECRET/TOKEN/PASSWORD env assignments, connection strings) before storage, replacing them with [REDACTED]; raw scrollback is never persisted or served. [@claim:clm_4710e0ea7da04c5390633f588e7967aaccdd469c76f085280b214dc5504121ef]
- Stopping an agent resolves the pane's process tree, verifies PID identity, then escalates SIGINT to SIGTERM after 5s and optionally SIGKILL with --force, exiting code 4 on failure. [@claim:clm_5b02b3aca20bfd8d5a546d4345363a8e83da9a8d4a039fa55e1fa6e19b7f176a]
- Socket security relies on file permissions (0700 directory, 0600 socket/db/pid); the trust boundary is same-user access, and socket paths over 104 bytes fall back to /tmp/control-<uid>. [@claim:clm_6310a43d48c89d8978f5d98b9625d09a4daa97fb66d62eb5f22d01c437b9156d]
- Live state is held in memory under an RWMutex with per-agent fields such as pane ID, type, PID, process start time, and a scrollback high-water mark; only parsed summaries are kept, not raw scrollback. [@claim:clm_6fcf964319deb6a492a20b2b5b40d61e8b627802d76876554abcc0a3e6b2f746]
- Stated non-goals: no agent launching, no cost/token tracking, no centralized agent configuration, no remote monitoring (local Unix socket only), and no detection of agents outside tmux. [@claim:clm_788e0bc7d226446d7dc839688fd1d292784e4d744504d7ee2e7a3159d299718a]
- The daemon exposes HTTP endpoints over the Unix socket: /agents, /agents/:id, /agents/:id/stop, /history, /history/:id/actions, and /ping, all returning JSON. [@claim:clm_987efabd4222cb78734fb62c1687185171090c087cf0e296942ba33c5769fd18]
- The daemon handles lifecycle signals: SIGTERM/SIGINT drain requests, finalize sessions, and clean up socket and PID files; SIGHUP reloads config such as poll interval and session names. [@claim:clm_a50e53a41d3d1cf309220dcdc2c194ad184b148f160f1464cac9d82546ceaa84]
- CLI commands include daemon start/stop/status, ls, show, stop, history, tui, and mcp, with global flags --json, --socket, and --help, and filter flags like --project, --type, --since, --until, --limit. [@claim:clm_ad94268eb125d83e752a986fae95c635ca830dbe0363ac86745fec53dfc1fc55]
- On startup the daemon performs crash recovery, marking sessions whose PIDs or panes no longer exist as status 'crashed' with an ended timestamp. [@claim:clm_c063ea1083b0ac93069907b7695b83817bb59034697a6ab94536a323f777cc93]
- The design requires tmux version 2.6 or newer; the daemon checks the version at startup and warns if older. [@claim:clm_c1d779ed02d99285fcd0e14e4fc4d53ea6758469cfa2f7a85a52c285420a5640]
- The daemon polls tmux roughly every 5 seconds, keeps an in-memory agent registry guarded by sync.RWMutex, persists history to SQLite in WAL mode, and serves HTTP/1.1 over a Unix socket. [@claim:clm_ce2cca6205064568a74c3b9c781ee67bf1b1df2ccb0f1aa43d3ba414a92319f8]
- The tech stack specifies Go, modernc.org/sqlite as the only acceptable SQLite driver (mattn/go-sqlite3 forbidden), bubbletea/lipgloss for the TUI, and net/http over a Unix socket. [@claim:clm_da651159fec9ccd2eecf3aef0bf91424bca37ffbfa805c82bc0bc7935797b9b3]
- All tmux and process interactions are specified to use exec.Command with discrete argument lists, avoiding shell interpolation to prevent injection from tmux-controlled values. [@claim:clm_e051b41e70da86e4d6f065d67a7a5d8846c46a33c92623d5495ac6d3a23f3bc0]
- History persists to ~/.control/history.db (0600) with WAL and foreign_keys pragmas, sessions and actions tables, SHA-256 content-hash deduplication, and schema versioning via PRAGMA user_version. [@claim:clm_e4161f92de2ed2adf3b7c52f706c700a52bb128cfef5cc02b2eb1f1c2e3da42d]
- The MCP server uses stdio transport with JSON-RPC 2.0, protocol version 2024-11-05, and tools including list_agents, get_agent, stop_agent, get_history, get_actions, and ping. [@claim:clm_fad476195077eb2ab6b45f9ba809406efb1900d3feceee0d1715ce566fd6b558]
<!-- rcw:end owner=source:src_4b8c3616b6125cb48740031cc4bde733 block=evidence -->

## Researcher notes

