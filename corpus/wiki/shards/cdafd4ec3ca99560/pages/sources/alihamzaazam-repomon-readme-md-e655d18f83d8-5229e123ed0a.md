---
access: public
aliases: []
claim_ids:
- clm_177b77535d127cf3546e9461131a733a6e2fa39035738e7c5ffbfcd8fa510a30
- clm_524e24a6a7b7d98405dabc6ab3a2d14fb0045269972a724e5472e6790557475e
- clm_751e7923e7d7a16bb7c90fcc6b8379a8f3727d3fc9858473ad04b462fbe64e49
- clm_78b2b6d9b8a8efa983299bf38d8bb084ae8a4e965e51d873644bb78627038d42
- clm_8903dba059f744044a80f0807bb1fb45139ed91524474b83883b5f644e2b322f
- clm_c1c2cde733d9b5b5d8c24084ed815352b39a5a007fc47e97f0b95cf0f5b3cdbe
- clm_dda6addfa466aaeaaf3f2016eac0db62456bb0267af458fbdc3a84f201acf740
- clm_dfe945c83df1f7dd6c9ad4a4764524f027fea138b908f0dc7cbb9c15afa9e326
maturity: draft
page_id: pg_aaf1875af7f25d9caeed5229e123ed0a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c8e1d0730b045399aef99596046a2af8
title: AliHamzaAzam/repomon/README.md @ e655d18f83d8
updated_at: '2026-09-14T01:59:20Z'
---

# AliHamzaAzam/repomon/README.md @ e655d18f83d8

<!-- rcw:begin owner=source:src_c8e1d0730b045399aef99596046a2af8 block=evidence -->
- The standalone CLI requires Git on every platform and tmux on macOS/Linux; Windows uses a bundled ConPTY host, and the desktop app bundles the daemon, CLI/TUI, and portable tmux so no separate installs are needed. [@claim:clm_177b77535d127cf3546e9461131a733a6e2fa39035738e7c5ffbfcd8fa510a30]
- A background daemon, repomond, owns SQLite, file watchers, the git layer, and the agent runtime, exposing a JSON-RPC API over a Unix socket or Windows named pipe; desktop, TUI, and iOS clients are thin clients over that API. [@claim:clm_524e24a6a7b7d98405dabc6ab3a2d14fb0045269972a724e5472e6790557475e]
- Repomon writes its own SQLite database in a platform data directory (overridable via REPOMON_DATA_DIR) and a Repomind home normally at ~/repomind when that feature is enabled. [@claim:clm_751e7923e7d7a16bb7c90fcc6b8379a8f3727d3fc9858473ad04b462fbe64e49]
- Repository development practice: the README's development section instructs contributors to run `cargo test --workspace` for Rust and `bun install && bun run test` in apps/desktop for the frontend. [@claim:clm_78b2b6d9b8a8efa983299bf38d8bb084ae8a4e965e51d873644bb78627038d42]
- Agents run in durable session windows: tmux windows on macOS/Linux, or a per-window detached repomon-agent-host.exe ConPTY process on Windows; because the session backend owns the process, agents survive daemon and TUI restarts. [@claim:clm_8903dba059f744044a80f0807bb1fb45139ed91524474b83883b5f644e2b322f]
- The daemon exposes a JSON-RPC API documented for writing custom clients, plus an MCP server (`repomond mcp`) that exposes the fleet to agents. [@claim:clm_c1c2cde733d9b5b5d8c24084ed815352b39a5a007fc47e97f0b95cf0f5b3cdbe]
- The workspace is split into crates: repomon-core (data model, gix git layer, SQLite store, watchers, usage ledger, agent runtime), repomon-daemon, repomon-tui, repomon-mcp, repomon-host, and a Tauri desktop app. [@claim:clm_dda6addfa466aaeaaf3f2016eac0db62456bb0267af458fbdc3a84f201acf740]
- Live agent processes survive app and daemon restarts but not an OS reboot; current desktop downloads lack an OS-level code signature, and the iOS companion is built but not yet released. [@claim:clm_dfe945c83df1f7dd6c9ad4a4764524f027fea138b908f0dc7cbb9c15afa9e326]
<!-- rcw:end owner=source:src_c8e1d0730b045399aef99596046a2af8 block=evidence -->

## Researcher notes

