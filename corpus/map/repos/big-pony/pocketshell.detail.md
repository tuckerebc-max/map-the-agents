# big-pony/pocketshell -- full detail

[Back to orientation](pocketshell.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/big-pony/pocketshell/8aa6474e81400fa1896369f3920dbffaa6465585/ee6c89f3609269d6.json](../../../wiki/dossiers/big-pony/pocketshell/8aa6474e81400fa1896369f3920dbffaa6465585/ee6c89f3609269d6.json)

## specifications (1 claim(s))

- [observation/documented] PocketShell is described as a self-hosted, mobile-first remote terminal that brings a dev machine's terminal sessions into a phone browser for CLI/TUI coding agents or plain shell use. -- evidence: [README.md#L63-L63](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L63-L63) (`clm_273ecf2e26657f36e9b4e1e39db069e89145da377309e5a78d35f8cf641b7377`)

## components (1 claim(s))

- [observation/documented] The stack comprises a Svelte 5 + Vite + xterm.js + CodeMirror 6 frontend, a Bun/TypeScript backend serving the embedded frontend and WebSocket on one port, tmux-managed PTYs, and bun:sqlite storage. -- evidence: [README.md#L304-L312](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L304-L312) (`clm_c92c27e17d99410b79ddf603180a2e429b34d19daca72a5a9854925a3c41c780`)

## design-choices (2 claim(s))

- [observation/documented] Sessions are tmux-managed server-side so tasks keep running while the phone is offline; on reconnect, per-session lastSeq accounting replays only the missing output gap. -- evidence: [README.md#L78-L83](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L78-L83), [README.md#L65-L65](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L65-L65) (`clm_c8ea8456ee61f3d65b0718c09571cc313b30d3d416b1b9c84af419d7e69e5110`)
- [observation/documented] Every connection performs a Noise IK handshake with mutual authentication and forward secrecy; unregistered devices cannot pass it, and keys live only in KEY_DIR. -- evidence: [README.md#L254-L254](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L254-L254) (`clm_02757861e6bb828e8a86aef7a0aa71744bb668ab03c763274fcd1b55208479f3`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork, branch as feat/your-feature, and open PRs; protocol changes start in agent/src/protocol.ts with app/src/lib/protocol.ts as a verbatim mirror, and bun test plus bun run typecheck must pass on both sides. -- evidence: [README.md#L338-L338](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L338-L338), [README.md#L332-L336](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L332-L336) (`clm_488a8832d978b452e10467b08271331b7456bb02e9fbac74af5e4d3ccdf19d4b`)
- [observation/documented] Repository development practice: running from source uses Bun — backend via 'cd agent && bun install && bun run start', frontend via 'cd app && bun install && bun run dev' on port 5173; building requires Bun >= 1.3. -- evidence: [README.md#L199-L199](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L199-L199), [README.md#L227-L227](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L227-L227), [README.md#L202-L203](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L202-L203) (`clm_c557c737ac4d5c7a3ac50515bd4075576dd0318e0456fa23eca6d7c8572a6a28`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Agent CLI includes install (requiring --advertise, default port 8722 bound to 127.0.0.1), pair, devices list/remove, uninstall, and tunnel setup subcommands. -- evidence: [DEPLOYMENT-CN.md#L213-L216](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/DEPLOYMENT-CN.md#L213-L216), [README.md#L154-L157](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L154-L157), [README.md#L188-L188](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L188-L188), [README.md#L145-L145](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L145-L145), [README.md#L177-L177](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L177-L177), [README.md#L260-L264](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L260-L264), [README.md#L179-L184](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L179-L184) (`clm_ab2b9420a2497a7cebb8556c20256ceafc10fb51c929a8b8ac5e01becb986b48`)
- [observation/documented] The phone UI offers three keyboard layouts (Classic default, Layered, Flick), an IME whole-segment input mode whose buffer survives disconnects, and a quick-actions panel. -- evidence: [README.md#L87-L93](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L87-L93) (`clm_c6a5e8b9e258e7546ca0f291a608380a3fb8d46115e82390ae30d42525044125`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The Agent supports in-app auto-update via GitHub Releases with SHA256 verification and automatic binary swap and restart, disableable with POCKETSHELL_UPDATE=0. -- evidence: [README.md#L297-L297](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L297-L297), [README.md#L299-L300](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L299-L300) (`clm_e0431ba3e449a8844be2faa0dc6f0ab1e20200d4061e717afec37fbab87fa9be`)

## tools-permissions (1 claim(s))

- [observation/documented] The Agent idempotently writes a notify hook into supported tools' configs (Claude Code, Codex, opencode, Kimi CLI), each toggleable in settings, and removes exactly that entry when disabled. -- evidence: [README.md#L272-L272](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L272-L272), [README.md#L105-L110](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L105-L110) (`clm_2ef47e41acfb022f1ee4994e8ef68c52b78ef2b205f81448db759ee4898d4e94`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The host needs tmux and git; the binary is a single-file Bun compile with pure-JS crypto (sodium-javascript, noise-handshake) and no native addons. -- evidence: [README.md#L227-L227](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L227-L227), [README.md#L304-L312](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L304-L312), [README.md#L129-L129](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L129-L129) (`clm_be6b8b7162cd6dd706e6119385554312d22b94bb4b10c697b8160f3e37a26cbe`)

## limitations (1 claim(s))

- [observation/documented] Windows hosts are not supported yet; the auth boundary is the Agent process's own permissions with no extra sandbox, so access should be constrained via process permissions. -- evidence: [README.md#L256-L256](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L256-L256), [README.md#L69-L72](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L69-L72) (`clm_16692059aaa17a7c3964ce2840fa0b2389dc48d817c6680aa38b22cea81db380`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

