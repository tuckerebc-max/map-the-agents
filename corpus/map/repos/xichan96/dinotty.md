# xichan96/dinotty

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b8081196ed61 @ 4521443326693707

## Summary (orientation draft, not independently verified)

Evidence consists of README files (English and German) describing Dinotty, a self-hosted Rust/Vue 3 web terminal for running coding agents across devices, with feature lists, install instructions, and tech-stack tables. No source code slices are present, so claims are documentation-based. Evidence coverage: 158 of 211 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 74 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Dinotty is described as a terminal built for coding agents, letting users run Claude Code, opencode, Codex, or OpenClaw on any device with multi-device session continuity. -- evidence: [README.md#L24-L24](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L24-L24), [README.md#L26-L26](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L26-L26)
- components (4 claim(s)):
  - [observation/documented] The tech stack is Rust with Axum 0.7, Tokio, portable-pty, vte, russh, and russh-sftp on the backend; Vue 3, TypeScript, Vite, and xterm.js 5 on the frontend; Tauri for desktop. -- evidence: [README.md#L269-L273](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L269-L273)
  - [observation/documented] The UI treats terminals, plugins, files, SSH sessions, and web previews as draggable panes, with split panes, multi-tab management, and cross-tab pane moves. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L34-L34](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L34-L34), [README.md#L86-L86](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L86-L86)
- design-choices (1 claim(s)):
  - [observation/documented] The product uses a server-side virtual terminal: a full VTE parser runs on the server so it knows exact screen state, enabling session recovery and screen snapshots rather than acting as a WebSocket-to-PTY pipe. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L153-L157](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L153-L157), [README.md#L275-L275](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L275-L275)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source involves a shallow clone of the dev branch, pnpm install and build in frontend/, then cargo run; debug logging uses RUST_LOG=debug and the frontend type-checks with npx vue-tsc --noEmit. -- evidence: [README.md#L226-L227](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L226-L227), [README.md#L223-L223](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L223-L223), [README.md#L245-L245](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L245-L245), [README.md#L219-L220](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L219-L220), [README.md#L248-L249](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L248-L249)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The server defaults to port 8999, accepts a -p flag for a custom port, and is accessed via browser at http://<ip>:8999. -- evidence: [README.md#L241-L241](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L241-L241), [README.md#L209-L209](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L209-L209), [README.md#L211-L213](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L211-L213)
  - [observation/documented] On Windows the default shell is resolved in order DINOTTY_SHELL, pwsh.exe, powershell.exe, then %ComSpec%/cmd.exe, and DINOTTY_SHELL can override auto-detection. -- evidence: [README.md#L207-L207](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L207-L207), [README.md#L203-L205](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L203-L205)
- memory-state (1 claim(s)):
  - [observation/documented] PTY processes survive disconnection with auto-reconnect using exponential backoff; refreshing the page restores the session where it left off. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L30-L30](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L30-L30)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Access control includes a default token login plus a mutually exclusive 6-digit verification-code mode: codes are server-generated, pushed via a notifier plugin, valid 5 minutes, single-use, and invalidated after 5 wrong attempts. -- evidence: [README.md#L259-L259](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L259-L259)
More evidence: [full detail](dinotty.detail.md)

Metadata and full claim list: [full detail](dinotty.detail.md)
Human notes ([notes](dinotty.notes.md), never overwritten by build)

[Back to map index](../../index.md)
