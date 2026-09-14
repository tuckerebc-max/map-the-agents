---
access: public
aliases: []
claim_ids:
- clm_02757861e6bb828e8a86aef7a0aa71744bb668ab03c763274fcd1b55208479f3
- clm_16692059aaa17a7c3964ce2840fa0b2389dc48d817c6680aa38b22cea81db380
- clm_273ecf2e26657f36e9b4e1e39db069e89145da377309e5a78d35f8cf641b7377
- clm_2ef47e41acfb022f1ee4994e8ef68c52b78ef2b205f81448db759ee4898d4e94
- clm_488a8832d978b452e10467b08271331b7456bb02e9fbac74af5e4d3ccdf19d4b
- clm_ab2b9420a2497a7cebb8556c20256ceafc10fb51c929a8b8ac5e01becb986b48
- clm_be6b8b7162cd6dd706e6119385554312d22b94bb4b10c697b8160f3e37a26cbe
- clm_c557c737ac4d5c7a3ac50515bd4075576dd0318e0456fa23eca6d7c8572a6a28
- clm_c6a5e8b9e258e7546ca0f291a608380a3fb8d46115e82390ae30d42525044125
- clm_c8ea8456ee61f3d65b0718c09571cc313b30d3d416b1b9c84af419d7e69e5110
- clm_c92c27e17d99410b79ddf603180a2e429b34d19daca72a5a9854925a3c41c780
- clm_e0431ba3e449a8844be2faa0dc6f0ab1e20200d4061e717afec37fbab87fa9be
maturity: draft
page_id: pg_0f033bc75d925272beddb692ce484ee9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7665d5b4c720530e8b9a2ada40835f17
title: Big-Pony/pocketshell/README.md @ 8aa6474e8140
updated_at: '2026-09-14T01:37:58Z'
---

# Big-Pony/pocketshell/README.md @ 8aa6474e8140

<!-- rcw:begin owner=source:src_7665d5b4c720530e8b9a2ada40835f17 block=evidence -->
- Every connection performs a Noise IK handshake with mutual authentication and forward secrecy; unregistered devices cannot pass it, and keys live only in KEY_DIR. [@claim:clm_02757861e6bb828e8a86aef7a0aa71744bb668ab03c763274fcd1b55208479f3]
- Windows hosts are not supported yet; the auth boundary is the Agent process's own permissions with no extra sandbox, so access should be constrained via process permissions. [@claim:clm_16692059aaa17a7c3964ce2840fa0b2389dc48d817c6680aa38b22cea81db380]
- PocketShell is described as a self-hosted, mobile-first remote terminal that brings a dev machine's terminal sessions into a phone browser for CLI/TUI coding agents or plain shell use. [@claim:clm_273ecf2e26657f36e9b4e1e39db069e89145da377309e5a78d35f8cf641b7377]
- The Agent idempotently writes a notify hook into supported tools' configs (Claude Code, Codex, opencode, Kimi CLI), each toggleable in settings, and removes exactly that entry when disabled. [@claim:clm_2ef47e41acfb022f1ee4994e8ef68c52b78ef2b205f81448db759ee4898d4e94]
- Repository development practice: contributors fork, branch as feat/your-feature, and open PRs; protocol changes start in agent/src/protocol.ts with app/src/lib/protocol.ts as a verbatim mirror, and bun test plus bun run typecheck must pass on both sides. [@claim:clm_488a8832d978b452e10467b08271331b7456bb02e9fbac74af5e4d3ccdf19d4b]
- The Agent CLI includes install (requiring --advertise, default port 8722 bound to 127.0.0.1), pair, devices list/remove, uninstall, and tunnel setup subcommands. [@claim:clm_ab2b9420a2497a7cebb8556c20256ceafc10fb51c929a8b8ac5e01becb986b48]
- The host needs tmux and git; the binary is a single-file Bun compile with pure-JS crypto (sodium-javascript, noise-handshake) and no native addons. [@claim:clm_be6b8b7162cd6dd706e6119385554312d22b94bb4b10c697b8160f3e37a26cbe]
- Repository development practice: running from source uses Bun — backend via 'cd agent && bun install && bun run start', frontend via 'cd app && bun install && bun run dev' on port 5173; building requires Bun >= 1.3. [@claim:clm_c557c737ac4d5c7a3ac50515bd4075576dd0318e0456fa23eca6d7c8572a6a28]
- The phone UI offers three keyboard layouts (Classic default, Layered, Flick), an IME whole-segment input mode whose buffer survives disconnects, and a quick-actions panel. [@claim:clm_c6a5e8b9e258e7546ca0f291a608380a3fb8d46115e82390ae30d42525044125]
- Sessions are tmux-managed server-side so tasks keep running while the phone is offline; on reconnect, per-session lastSeq accounting replays only the missing output gap. [@claim:clm_c8ea8456ee61f3d65b0718c09571cc313b30d3d416b1b9c84af419d7e69e5110]
- The stack comprises a Svelte 5 + Vite + xterm.js + CodeMirror 6 frontend, a Bun/TypeScript backend serving the embedded frontend and WebSocket on one port, tmux-managed PTYs, and bun:sqlite storage. [@claim:clm_c92c27e17d99410b79ddf603180a2e429b34d19daca72a5a9854925a3c41c780]
- The Agent supports in-app auto-update via GitHub Releases with SHA256 verification and automatic binary swap and restart, disableable with POCKETSHELL_UPDATE=0. [@claim:clm_e0431ba3e449a8844be2faa0dc6f0ab1e20200d4061e717afec37fbab87fa9be]
<!-- rcw:end owner=source:src_7665d5b4c720530e8b9a2ada40835f17 block=evidence -->

## Researcher notes

