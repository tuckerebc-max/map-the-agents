# big-pony/pocketshell

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8aa6474e8140 @ ee6c89f3609269d6

## Summary (orientation draft, not independently verified)

PocketShell is a self-hosted, mobile-first remote terminal that proxies tmux-backed terminal sessions to a phone browser, with server-side task continuation, gap-only replay on reconnect, push/webhook notifications, and Noise IK end-to-end encryption, shipped as a single-file Bun binary. Evidence is documentation-only (README and deployment guide); no runtime source code appears in the slices. Evidence coverage: 162 of 318 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] PocketShell is described as a self-hosted, mobile-first remote terminal that brings a dev machine's terminal sessions into a phone browser for CLI/TUI coding agents or plain shell use. -- evidence: [README.md#L63-L63](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L63-L63)
- components (1 claim(s)):
  - [observation/documented] The stack comprises a Svelte 5 + Vite + xterm.js + CodeMirror 6 frontend, a Bun/TypeScript backend serving the embedded frontend and WebSocket on one port, tmux-managed PTYs, and bun:sqlite storage. -- evidence: [README.md#L304-L312](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L304-L312)
- design-choices (2 claim(s)):
  - [observation/documented] Sessions are tmux-managed server-side so tasks keep running while the phone is offline; on reconnect, per-session lastSeq accounting replays only the missing output gap. -- evidence: [README.md#L78-L83](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L78-L83), [README.md#L65-L65](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L65-L65)
  - [observation/documented] Every connection performs a Noise IK handshake with mutual authentication and forward secrecy; unregistered devices cannot pass it, and keys live only in KEY_DIR. -- evidence: [README.md#L254-L254](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L254-L254)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, branch as feat/your-feature, and open PRs; protocol changes start in agent/src/protocol.ts with app/src/lib/protocol.ts as a verbatim mirror, and bun test plus bun run typecheck must pass on both sides. -- evidence: [README.md#L338-L338](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L338-L338), [README.md#L332-L336](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L332-L336)
  - [observation/documented] Repository development practice: running from source uses Bun — backend via 'cd agent && bun install && bun run start', frontend via 'cd app && bun install && bun run dev' on port 5173; building requires Bun >= 1.3. -- evidence: [README.md#L199-L199](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L199-L199), [README.md#L227-L227](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L227-L227), [README.md#L202-L203](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L202-L203)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Agent CLI includes install (requiring --advertise, default port 8722 bound to 127.0.0.1), pair, devices list/remove, uninstall, and tunnel setup subcommands. -- evidence: [DEPLOYMENT-CN.md#L213-L216](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/DEPLOYMENT-CN.md#L213-L216), [README.md#L154-L157](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L154-L157), [README.md#L188-L188](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L188-L188), [README.md#L145-L145](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L145-L145), [README.md#L177-L177](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L177-L177), [README.md#L260-L264](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L260-L264), [README.md#L179-L184](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L179-L184)
  - [observation/documented] The phone UI offers three keyboard layouts (Classic default, Layered, Flick), an IME whole-segment input mode whose buffer survives disconnects, and a quick-actions panel. -- evidence: [README.md#L87-L93](https://github.com/Big-Pony/pocketshell/blob/8aa6474e81400fa1896369f3920dbffaa6465585/README.md#L87-L93)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
More evidence: [full detail](pocketshell.detail.md)

Metadata and full claim list: [full detail](pocketshell.detail.md)
Human notes ([notes](pocketshell.notes.md), never overwritten by build)

[Back to map index](../../index.md)
