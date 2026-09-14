# saadnvd1/agent-os -- full detail

[Back to orientation](agent-os.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/saadnvd1/agent-os/378069fed63708179ae4dd9ddad1a2ce64f37d5d/82000dd2a4b2ad99.json](../../../wiki/dossiers/saadnvd1/agent-os/378069fed63708179ae4dd9ddad1a2ce64f37d5d/82000dd2a4b2ad99.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The product supports multiple AI coding agents with a capability matrix: only Claude Code and Kilo Code support resume and fork, and each agent has a distinct auto-approve mechanism (flags or config files). -- evidence: [README.md#L66-L77](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L66-L77) (`clm_0681f31da857a9ea39263893c58884c5b5b9af300b99cc88151302ebf467c8f1`)
- [observation/documented] Documented features include voice-to-text prompting, up to four side-by-side session panes, code search, file picker with mobile upload, GitHub cloning, git integration, git worktrees, dev server control, and conductor/worker session orchestration via MCP. -- evidence: [README.md#L81-L90](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L81-L90) (`clm_c5b666dde13d0e6138365d56e1d94d625cbed07df5a1bc4d67f2ec7d7dd0e3cb`)
- [inference/documented] The fix saved WebSocket handlers immediately after definition so forceReconnect could attach them to the new socket, avoiding the bug where nulling handlers on the shared old socket object also cleared the live socket's handlers. -- evidence: [docs/issues/ios-safari-websocket-reconnect.md#L35-L35](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L35-L35), [docs/issues/ios-safari-websocket-reconnect.md#L16-L26](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L16-L26), [docs/issues/ios-safari-websocket-reconnect.md#L64-L69](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L64-L69), [docs/issues/ios-safari-websocket-reconnect.md#L56-L62](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L56-L62), [docs/issues/ios-safari-websocket-reconnect.md#L45-L45](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L45-L45) (`clm_b5dab3224d5a180145c83dd60b76e1c69a61394b622dcdcde1d9e1f5e9240a33`)
- [inference/documented] The terminal stack appears to consist of a React hook wrapping WebSocket management (websocket-connection.ts, useTerminalConnection.ts) and a server.ts that runs the WebSocket server and spawns PTYs, attaching to tmux sessions. -- evidence: [docs/issues/ios-safari-websocket-reconnect.md#L106-L108](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L106-L108), [docs/issues/ios-safari-websocket-reconnect.md#L39-L41](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L39-L41) (`clm_6e0492421513a7e2e049044f542b8250b93f81f8d3a9af479c93906b41d08551`)

## design-choices (1 claim(s))

- [observation/documented] The desktop app is a native wrapper around the web UI; the backend server must still be installed and run separately, with the wrapper only providing a native window instead of a browser. -- evidence: [README.md#L44-L44](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L44-L44) (`clm_d1d6de197adcf6e068e5cc7cf5379d55ef1789a29c2a7dbbf3a376ceed156bd8`)

## workflows (2 claim(s))

- [observation/documented] Installation paths: global npm install followed by 'agent-os install' and 'agent-os start' (recommended when Node.js 20+ exists), a curl-piped install script for fresh machines without Node.js, or manual git clone with npm install and npm run dev. -- evidence: [README.md#L19-L19](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L19-L19), [README.md#L22-L22](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L22-L22), [README.md#L30-L30](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L30-L30), [README.md#L32-L35](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L32-L35), [README.md#L15-L15](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L15-L15), [README.md#L25-L26](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L25-L26), [README.md#L50-L55](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L50-L55) (`clm_ad1633ee8999b0878559b6a2fc317ca654ec9ffcb0dd3fab5079d69915f44dea`)
- [observation/documented] Mobile access is documented via Tailscale: install on machine and phone, sign in with the same account, then reach the server at its 100.x.x.x address on port 3011. -- evidence: [README.md#L105-L105](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L105-L105), [README.md#L107-L109](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L107-L109) (`clm_dd4ea2fd77268a36a7a0f0e5f30f9dceab52199fadf3224b668a594df35502f6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] AgentOS provides a mobile-first web UI for managing AI coding sessions, served on port 3011 in the manual dev setup. -- evidence: [README.md#L3-L3](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L3-L3), [README.md#L50-L55](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L50-L55) (`clm_074570f800ca37c59c3f1e8a8ab70e4fcfbe28c8183387b6153498784be5d686`)
- [observation/documented] The CLI offers run, start, stop, status, logs, and update commands for controlling the server. -- evidence: [README.md#L94-L101](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L94-L101) (`clm_62384540f6289a02c1bec3e6a5436e0875b2c830881171ab86a7c03aa6bdaa91`)
- [observation/documented] Native desktop builds are distributed via GitHub Releases as macOS Apple Silicon .dmg and Linux .deb or .AppImage packages. -- evidence: [README.md#L39-L39](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L39-L39), [README.md#L41-L42](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L41-L42) (`clm_70c342477c833db2d49398738f29b174ce96b05f90821cdabcfa15e9bc613b44`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites are Node.js 20+, tmux, and ripgrep (auto-installed by the installer script per the README), plus at least one supported AI CLI such as Claude Code, Codex, Gemini CLI, Aider, or Cursor CLI. -- evidence: [README.md#L59-L62](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L59-L62) (`clm_90947ede32d15d9ab14a01ed7cef23e74920ec5253019f68262c20a599d66753`)
- [observation/documented] The project is MIT licensed and free and open source. -- evidence: [README.md#L124-L124](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L124-L124), [README.md#L122-L122](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/README.md#L122-L122) (`clm_7b5be1e0093745d7dcb68c6863a32a715a845a87365238a6518cda2317efafd9`)

## limitations (2 claim(s))

- [observation/documented] An iOS Safari issue where the terminal stayed stuck reconnecting after backgrounding was fixed (January 14, 2026, commit 12bae2e); Safari silently kills WebSockets and may not fire onclose while readyState still shows OPEN. -- evidence: [docs/issues/ios-safari-websocket-reconnect.md#L112-L116](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L112-L116), [docs/issues/ios-safari-websocket-reconnect.md#L3-L4](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L3-L4), [docs/issues/ios-safari-websocket-reconnect.md#L12-L12](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L12-L12), [docs/issues/ios-safari-websocket-reconnect.md#L8-L8](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/docs/issues/ios-safari-websocket-reconnect.md#L8-L8) (`clm_819fcfe871522be64fe354c87ce8b14a762fb5ab39eb0444547aa258e042cd5b`)
- [inference/documented] A roadmap file marks many ideas as unchecked, suggesting they are not yet implemented, including notifications, MCP server integration toggles, session templates/groups, conversation export, session snapshots, and WebSocket reconnection handling improvements. -- evidence: [ideas.md#L17-L24](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/ideas.md#L17-L24), [ideas.md#L5-L13](https://github.com/saadnvd1/agent-os/blob/378069fed63708179ae4dd9ddad1a2ce64f37d5d/ideas.md#L5-L13) (`clm_b98cce9d1191814a96170f2a5f714e0100de2d8259aa833a0779fa21a2131763`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

