---
access: public
aliases: []
claim_ids:
- clm_01dad8755d56e23ff2114116f6ef9d2da514ffedd26f4e22f61f1dbbd5526a60
- clm_2beb77f7a345330d0bcacbcbce2460a0930e9d991b9c71bfd8560ae6ae296daf
- clm_2e576ab97c2e79a693a8e71847686f1e97e7775536c3939b38d7f38c43289996
- clm_577c573ac08f2c59f35c0caa230d4f25b408c0638717f52734e90eab30693f7a
- clm_62c7798048e0abc4aebb8f99465867cc639cb0e5b09df9ed851b767195795cbc
- clm_8da932825b83edab2503cd1c5f3019f0ca5989f56da48e992e32ef5028100d00
- clm_8fbbcae4b3e7601e55a3fd4ff366aa3b9c5f9613880267d6767d494e21252bb8
- clm_9318896033ea98e9bd4a004a4e90ace8a2089539965fd310e76198cd7a871a78
- clm_a6fd43fa068e6a5bcea4ac2574521f21a5e5364b22166d97f840873f20475cbd
- clm_af7a824e112bc52df5caa478cc7d9dc499f65ba88f954ba72d2e08dd80674eca
- clm_c1adb2b1147ec6f84f148d0285e36afc14758bcc7f7345c75960af6fb064dfce
- clm_dd55c69d5005028b0dfed90135949124ae4014fc5c02d38f1e06c9ccd8e84e87
- clm_f7df7f857e532e480fce3e683a625b5e05bd9e18eee92dcd83d9af1669ab6b5b
maturity: draft
page_id: pg_c2ba0f83d8d852658a1f82cad72ec6da
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_686f3df186985394a61f2568e44dec41
title: storozhenko98/beehive/README.md @ 42e6a36ead6d
updated_at: '2026-09-14T02:43:44Z'
---

# storozhenko98/beehive/README.md @ 42e6a36ead6d

<!-- rcw:begin owner=source:src_686f3df186985394a61f2568e44dec41 block=evidence -->
- Features include agent panes that launch Claude Code or any CLI agent alongside terminals, per-repo custom quick-launch buttons, comb copying including uncommitted work, live branch tracking in the sidebar, and persisted pane layouts. [@claim:clm_01dad8755d56e23ff2114116f6ef9d2da514ffedd26f4e22f61f1dbbd5526a60]
- A configured comb startup command (e.g. a tmux session) runs once per comb the first time it opens after launch, after which the app returns to an interactive shell in the comb directory. [@claim:clm_2beb77f7a345330d0bcacbcbce2460a0930e9d991b9c71bfd8560ae6ae296daf]
- The TUI installs via a curl-piped shell script, asks the user to choose 'bh' or 'beehive' as the command name, and auto-updates on startup. [@claim:clm_2e576ab97c2e79a693a8e71847686f1e97e7775536c3939b38d7f38c43289996]
- The tool appears aimed at developers juggling several GitHub repositories who want parallel terminal and CLI coding-agent sessions in branch-isolated workspace clones. [@claim:clm_577c573ac08f2c59f35c0caa230d4f25b408c0638717f52734e90eab30693f7a]
- Repository development practice: the GUI is built with npm install plus 'npm run tauri dev' for hot-reload development or 'npm run tauri build' for production, the TUI is built with cargo build --release from cli/, and CONTRIBUTING.md covers development setup and guidelines. [@claim:clm_62c7798048e0abc4aebb8f99465867cc639cb0e5b09df9ed851b767195795cbc]
- The GUI and TUI share the same config and data, so they can be used interchangeably. [@claim:clm_8da932825b83edab2503cd1c5f3019f0ca5989f56da48e992e32ef5028100d00]
- Beehive manages multiple repos, creates isolated workspace clones on different branches, and runs terminals and AI agents side-by-side from one window, shipped as both a desktop GUI app and a terminal TUI. [@claim:clm_8fbbcae4b3e7601e55a3fd4ff366aa3b9c5f9613880267d6767d494e21252bb8]
- Beehive requires git and the GitHub CLI for all usage, and gh authentication is required because repo operations use gh. [@claim:clm_9318896033ea98e9bd4a004a4e90ace8a2089539965fd310e76198cd7a871a78]
- The desktop GUI is macOS-only for now; the standalone TUI supports macOS (Apple Silicon) and Linux x86_64 glibc, and Windows support is not yet available. Intel macOS is listed as untested for both. [@claim:clm_a6fd43fa068e6a5bcea4ac2574521f21a5e5364b22166d97f840873f20475cbd]
- The stack comprises a React 19/TypeScript/Vite frontend with xterm.js, a Rust Tauri v2 backend using portable-pty, a Ratatui/Crossterm-based Rust TUI, and git operations performed by shelling out to git and gh CLIs. [@claim:clm_af7a824e112bc52df5caa478cc7d9dc499f65ba88f954ba72d2e08dd80674eca]
- Repository development practice: CLAUDE.md serves as AI-assistant context and documents contributor commands such as cargo check for Rust type-checking and npx tsc --noEmit for TypeScript type-checking. [@claim:clm_c1adb2b1147ec6f84f148d0285e36afc14758bcc7f7345c75960af6fb064dfce]
- All config lives under ~/.beehive/: config.json for app settings, a beehive.json directory marker, and per-hive .hive/state.json holding repo info, nests, combs, pane layouts, and custom buttons; combs are full git clones on disk. [@claim:clm_dd55c69d5005028b0dfed90135949124ae4014fc5c02d38f1e06c9ccd8e84e87]
- The TUI binary can set the comb startup command programmatically via a --startup-cmd flag, and passing an empty string clears it, per the documented examples. [@claim:clm_f7df7f857e532e480fce3e683a625b5e05bd9e18eee92dcd83d9af1669ab6b5b]
<!-- rcw:end owner=source:src_686f3df186985394a61f2568e44dec41 block=evidence -->

## Researcher notes

