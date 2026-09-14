---
access: public
aliases: []
claim_ids:
- clm_0ba3e8b1149572aea89407f5a496ca087ed3c790077661672e3868fff681339d
- clm_0f84b58cda54efe646e02dd7e19008779928e9b62f92e3b782a5df1e44365d7f
- clm_2b582603b3caec7536325a359f622ce4cbb9bc577954b352c2a8869cb02fda0a
- clm_2d4904ee0d9cd448f68a8e636c13d2e2678e9103316d5b18ba9c8cbe21d1ea57
- clm_327828a440937367a150deb050e5ba08f9d713b5038c163d6163fcec99e96709
- clm_4a52f411821b431f916e5ec025b42339d70e56b84a8e0e0971550e6cd87cfa59
- clm_5ddcbc6ca82ab604c7f4d80f3b52f7e2100bee9f42bf6f8ca9acd27d7dedfc03
- clm_866ed5a8d49dd5f4862de64277097f58b3f46fb18ca2d5b6ce9fd4f3bebcbf64
- clm_9e0eaa98a7875abc9ea0ead65b0c1b3b3356de85b27fdc35fdfc3c8518fdd5ce
- clm_ad5ff4d42ed18b2dcdbdc097107ab78881e9de0ab1529fd89e68dd9bd142be3b
- clm_b7b19fc28e6a895181ffd780e67090e25872687f745634b8f80260fd16c37b8f
- clm_d19ce7efd39552779f364d828d9294a2f823fa5bd8901fd1cabbe34579ab64d8
- clm_e172be5daf7108b12c0f42d2bfc0608625abd8bc1b6b0f904b7f3171213b7b4a
- clm_e5e8eba659fa5cc0ed6a9da852dd166456e37e47faa1e5de7d32d8de78b76037
- clm_e961c520bbe8e278f7f24922b134f59a1c29e52a680b64db2d767a77bc657b79
maturity: draft
page_id: pg_f0cbdca48bc05753abe5ac27e2a770c2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1b0d30a9c5a1523e89703c91ef5375fc
title: xichan96/dinotty/README.md @ b8081196ed61
updated_at: '2026-09-14T03:24:52Z'
---

# xichan96/dinotty/README.md @ b8081196ed61

<!-- rcw:begin owner=source:src_1b0d30a9c5a1523e89703c91ef5375fc block=evidence -->
- The UI treats terminals, plugins, files, SSH sessions, and web previews as draggable panes, with split panes, multi-tab management, and cross-tab pane moves. [@claim:clm_0ba3e8b1149572aea89407f5a496ca087ed3c790077661672e3868fff681339d]
- Repository development practice: building from source involves a shallow clone of the dev branch, pnpm install and build in frontend/, then cargo run; debug logging uses RUST_LOG=debug and the frontend type-checks with npx vue-tsc --noEmit. [@claim:clm_0f84b58cda54efe646e02dd7e19008779928e9b62f92e3b782a5df1e44365d7f]
- The macOS app is unsigned, so macOS may report it as damaged; the README instructs running 'xattr -cr /Applications/Dinotty.app' after installation to remove the restriction. [@claim:clm_2b582603b3caec7536325a359f622ce4cbb9bc577954b352c2a8869cb02fda0a]
- On Windows the default shell is resolved in order DINOTTY_SHELL, pwsh.exe, powershell.exe, then %ComSpec%/cmd.exe, and DINOTTY_SHELL can override auto-detection. [@claim:clm_2d4904ee0d9cd448f68a8e636c13d2e2678e9103316d5b18ba9c8cbe21d1ea57]
- Dinotty is described as a terminal built for coding agents, letting users run Claude Code, opencode, Codex, or OpenClaw on any device with multi-device session continuity. [@claim:clm_327828a440937367a150deb050e5ba08f9d713b5038c163d6163fcec99e96709]
- The server defaults to port 8999, accepts a -p flag for a custom port, and is accessed via browser at http://<ip>:8999. [@claim:clm_4a52f411821b431f916e5ec025b42339d70e56b84a8e0e0971550e6cd87cfa59]
- A built-in MCP JSON-RPC server is documented, allowing AI assistants to operate terminal sessions. [@claim:clm_5ddcbc6ca82ab604c7f4d80f3b52f7e2100bee9f42bf6f8ca9acd27d7dedfc03]
- A plugin system supports hot-reloadable JavaScript plugins with an API for custom commands, terminal interaction, event subscriptions, and CLI integration; built-ins include CC Switch and JSON Formatter. [@claim:clm_866ed5a8d49dd5f4862de64277097f58b3f46fb18ca2d5b6ce9fd4f3bebcbf64]
- PTY processes survive disconnection with auto-reconnect using exponential backoff; refreshing the page restores the session where it left off. [@claim:clm_9e0eaa98a7875abc9ea0ead65b0c1b3b3356de85b27fdc35fdfc3c8518fdd5ce]
- The tech stack is Rust with Axum 0.7, Tokio, portable-pty, vte, russh, and russh-sftp on the backend; Vue 3, TypeScript, Vite, and xterm.js 5 on the frontend; Tauri for desktop. [@claim:clm_ad5ff4d42ed18b2dcdbdc097107ab78881e9de0ab1529fd89e68dd9bd142be3b]
- Verification-code login requires a notifier plugin subscribed to the auth.verification_code event; uninstalling such a plugin while that mode is active is rejected with HTTP 409 to prevent lockout. [@claim:clm_b7b19fc28e6a895181ffd780e67090e25872687f745634b8f80260fd16c37b8f]
- Dinotty includes a built-in SSH client supporting password and key auth, with SFTP file browsing, editing, upload, and download auto-enabled over SSH connections. [@claim:clm_d19ce7efd39552779f364d828d9294a2f823fa5bd8901fd1cabbe34579ab64d8]
- The server is described as a single Rust binary with zero dependencies, self-hosted with no subscription or relay, keeping data on the user's machine. [@claim:clm_e172be5daf7108b12c0f42d2bfc0608625abd8bc1b6b0f904b7f3171213b7b4a]
- Access control includes a default token login plus a mutually exclusive 6-digit verification-code mode: codes are server-generated, pushed via a notifier plugin, valid 5 minutes, single-use, and invalidated after 5 wrong attempts. [@claim:clm_e5e8eba659fa5cc0ed6a9da852dd166456e37e47faa1e5de7d32d8de78b76037]
- The product uses a server-side virtual terminal: a full VTE parser runs on the server so it knows exact screen state, enabling session recovery and screen snapshots rather than acting as a WebSocket-to-PTY pipe. [@claim:clm_e961c520bbe8e278f7f24922b134f59a1c29e52a680b64db2d767a77bc657b79]
<!-- rcw:end owner=source:src_1b0d30a9c5a1523e89703c91ef5375fc block=evidence -->

## Researcher notes

