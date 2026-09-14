# xichan96/dinotty -- full detail

[Back to orientation](dinotty.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xichan96/dinotty/b8081196ed619e30ca758c7f763187d160e6ec93/4521443326693707.json](../../../wiki/dossiers/xichan96/dinotty/b8081196ed619e30ca758c7f763187d160e6ec93/4521443326693707.json)

## specifications (1 claim(s))

- [observation/documented] Dinotty is described as a terminal built for coding agents, letting users run Claude Code, opencode, Codex, or OpenClaw on any device with multi-device session continuity. -- evidence: [README.md#L24-L24](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L24-L24), [README.md#L26-L26](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L26-L26) (`clm_327828a440937367a150deb050e5ba08f9d713b5038c163d6163fcec99e96709`)

## components (4 claim(s))

- [observation/documented] The tech stack is Rust with Axum 0.7, Tokio, portable-pty, vte, russh, and russh-sftp on the backend; Vue 3, TypeScript, Vite, and xterm.js 5 on the frontend; Tauri for desktop. -- evidence: [README.md#L269-L273](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L269-L273) (`clm_ad5ff4d42ed18b2dcdbdc097107ab78881e9de0ab1529fd89e68dd9bd142be3b`)
- [observation/documented] The UI treats terminals, plugins, files, SSH sessions, and web previews as draggable panes, with split panes, multi-tab management, and cross-tab pane moves. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L34-L34](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L34-L34), [README.md#L86-L86](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L86-L86) (`clm_0ba3e8b1149572aea89407f5a496ca087ed3c790077661672e3868fff681339d`)
- [observation/documented] Dinotty includes a built-in SSH client supporting password and key auth, with SFTP file browsing, editing, upload, and download auto-enabled over SSH connections. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L68-L68](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L68-L68) (`clm_d19ce7efd39552779f364d828d9294a2f823fa5bd8901fd1cabbe34579ab64d8`)
- [observation/documented] A plugin system supports hot-reloadable JavaScript plugins with an API for custom commands, terminal interaction, event subscriptions, and CLI integration; built-ins include CC Switch and JSON Formatter. -- evidence: [README.md#L80-L80](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L80-L80), [README.md#L102-L102](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L102-L102) (`clm_866ed5a8d49dd5f4862de64277097f58b3f46fb18ca2d5b6ce9fd4f3bebcbf64`)

## design-choices (1 claim(s))

- [observation/documented] The product uses a server-side virtual terminal: a full VTE parser runs on the server so it knows exact screen state, enabling session recovery and screen snapshots rather than acting as a WebSocket-to-PTY pipe. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L153-L157](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L153-L157), [README.md#L275-L275](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L275-L275) (`clm_e961c520bbe8e278f7f24922b134f59a1c29e52a680b64db2d767a77bc657b79`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source involves a shallow clone of the dev branch, pnpm install and build in frontend/, then cargo run; debug logging uses RUST_LOG=debug and the frontend type-checks with npx vue-tsc --noEmit. -- evidence: [README.md#L226-L227](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L226-L227), [README.md#L223-L223](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L223-L223), [README.md#L245-L245](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L245-L245), [README.md#L219-L220](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L219-L220), [README.md#L248-L249](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L248-L249) (`clm_0f84b58cda54efe646e02dd7e19008779928e9b62f92e3b782a5df1e44365d7f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The server defaults to port 8999, accepts a -p flag for a custom port, and is accessed via browser at http://<ip>:8999. -- evidence: [README.md#L241-L241](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L241-L241), [README.md#L209-L209](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L209-L209), [README.md#L211-L213](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L211-L213) (`clm_4a52f411821b431f916e5ec025b42339d70e56b84a8e0e0971550e6cd87cfa59`)
- [observation/documented] On Windows the default shell is resolved in order DINOTTY_SHELL, pwsh.exe, powershell.exe, then %ComSpec%/cmd.exe, and DINOTTY_SHELL can override auto-detection. -- evidence: [README.md#L207-L207](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L207-L207), [README.md#L203-L205](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L203-L205) (`clm_2d4904ee0d9cd448f68a8e636c13d2e2678e9103316d5b18ba9c8cbe21d1ea57`)
- [observation/documented] A built-in MCP JSON-RPC server is documented, allowing AI assistants to operate terminal sessions. -- evidence: [README.md#L279-L291](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L279-L291) (`clm_5ddcbc6ca82ab604c7f4d80f3b52f7e2100bee9f42bf6f8ca9acd27d7dedfc03`)

## memory-state (1 claim(s))

- [observation/documented] PTY processes survive disconnection with auto-reconnect using exponential backoff; refreshing the page restores the session where it left off. -- evidence: [README.md#L130-L149](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L130-L149), [README.md#L30-L30](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L30-L30) (`clm_9e0eaa98a7875abc9ea0ead65b0c1b3b3356de85b27fdc35fdfc3c8518fdd5ce`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Access control includes a default token login plus a mutually exclusive 6-digit verification-code mode: codes are server-generated, pushed via a notifier plugin, valid 5 minutes, single-use, and invalidated after 5 wrong attempts. -- evidence: [README.md#L259-L259](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L259-L259) (`clm_e5e8eba659fa5cc0ed6a9da852dd166456e37e47faa1e5de7d32d8de78b76037`)
- [observation/documented] Verification-code login requires a notifier plugin subscribed to the auth.verification_code event; uninstalling such a plugin while that mode is active is rejected with HTTP 409 to prevent lockout. -- evidence: [README.md#L261-L261](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L261-L261) (`clm_b7b19fc28e6a895181ffd780e67090e25872687f745634b8f80260fd16c37b8f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The server is described as a single Rust binary with zero dependencies, self-hosted with no subscription or relay, keeping data on the user's machine. -- evidence: [README.md#L114-L114](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L114-L114), [README.md#L275-L275](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L275-L275) (`clm_e172be5daf7108b12c0f42d2bfc0608625abd8bc1b6b0f904b7f3171213b7b4a`)

## limitations (1 claim(s))

- [observation/documented] The macOS app is unsigned, so macOS may report it as damaged; the README instructs running 'xattr -cr /Applications/Dinotty.app' after installation to remove the restriction. -- evidence: [README.md#L173-L173](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L173-L173), [README.md#L175-L177](https://github.com/xichan96/dinotty/blob/b8081196ed619e30ca758c7f763187d160e6ec93/README.md#L175-L177) (`clm_2b582603b3caec7536325a359f622ce4cbb9bc577954b352c2a8869cb02fda0a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

