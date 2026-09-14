# storozhenko98/beehive -- full detail

[Back to orientation](beehive.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/storozhenko98/beehive/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/45e04241f2153fbd.json](../../../wiki/dossiers/storozhenko98/beehive/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/45e04241f2153fbd.json)

## specifications (1 claim(s))

- [observation/documented] Beehive manages multiple repos, creates isolated workspace clones on different branches, and runs terminals and AI agents side-by-side from one window, shipped as both a desktop GUI app and a terminal TUI. -- evidence: [README.md#L3-L3](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L3-L3), [README.md#L7-L7](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L7-L7) (`clm_8fbbcae4b3e7601e55a3fd4ff366aa3b9c5f9613880267d6767d494e21252bb8`)

## components (1 claim(s))

- [observation/documented] The stack comprises a React 19/TypeScript/Vite frontend with xterm.js, a Rust Tauri v2 backend using portable-pty, a Ratatui/Crossterm-based Rust TUI, and git operations performed by shelling out to git and gh CLIs. -- evidence: [README.md#L121-L128](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L121-L128) (`clm_af7a824e112bc52df5caa478cc7d9dc499f65ba88f954ba72d2e08dd80674eca`)

## design-choices (1 claim(s))

- [observation/documented] A configured comb startup command (e.g. a tmux session) runs once per comb the first time it opens after launch, after which the app returns to an interactive shell in the comb directory. -- evidence: [README.md#L175-L175](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L175-L175), [README.md#L177-L181](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L177-L181), [README.md#L183-L183](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L183-L183) (`clm_2beb77f7a345330d0bcacbcbce2460a0930e9d991b9c71bfd8560ae6ae296daf`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the GUI is built with npm install plus 'npm run tauri dev' for hot-reload development or 'npm run tauri build' for production, the TUI is built with cargo build --release from cli/, and CONTRIBUTING.md covers development setup and guidelines. -- evidence: [README.md#L112-L115](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L112-L115), [README.md#L94-L100](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L94-L100), [README.md#L196-L196](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L196-L196) (`clm_62c7798048e0abc4aebb8f99465867cc639cb0e5b09df9ed851b767195795cbc`)
- [observation/documented] Repository development practice: CLAUDE.md serves as AI-assistant context and documents contributor commands such as cargo check for Rust type-checking and npx tsc --noEmit for TypeScript type-checking. -- evidence: [CLAUDE.md#L64-L64](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/CLAUDE.md#L64-L64), [CLAUDE.md#L67-L67](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/CLAUDE.md#L67-L67), [README.md#L132-L159](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L132-L159) (`clm_c1adb2b1147ec6f84f148d0285e36afc14758bcc7f7345c75960af6fb064dfce`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The TUI installs via a curl-piped shell script, asks the user to choose 'bh' or 'beehive' as the command name, and auto-updates on startup. -- evidence: [README.md#L25-L25](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L25-L25), [README.md#L21-L23](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L21-L23) (`clm_2e576ab97c2e79a693a8e71847686f1e97e7775536c3939b38d7f38c43289996`)
- [observation/documented] The TUI binary can set the comb startup command programmatically via a --startup-cmd flag, and passing an empty string clears it, per the documented examples. -- evidence: [README.md#L33-L33](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L33-L33), [README.md#L35-L37](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L35-L37), [README.md#L27-L27](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L27-L27), [README.md#L29-L31](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L29-L31) (`clm_f7df7f857e532e480fce3e683a625b5e05bd9e18eee92dcd83d9af1669ab6b5b`)
- [observation/documented] Features include agent panes that launch Claude Code or any CLI agent alongside terminals, per-repo custom quick-launch buttons, comb copying including uncommitted work, live branch tracking in the sidebar, and persisted pane layouts. -- evidence: [README.md#L46-L56](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L46-L56) (`clm_01dad8755d56e23ff2114116f6ef9d2da514ffedd26f4e22f61f1dbbd5526a60`)

## memory-state (2 claim(s))

- [observation/documented] All config lives under ~/.beehive/: config.json for app settings, a beehive.json directory marker, and per-hive .hive/state.json holding repo info, nests, combs, pane layouts, and custom buttons; combs are full git clones on disk. -- evidence: [README.md#L163-L163](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L163-L163), [README.md#L171-L171](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L171-L171), [README.md#L165-L169](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L165-L169) (`clm_dd55c69d5005028b0dfed90135949124ae4014fc5c02d38f1e06c9ccd8e84e87`)
- [observation/documented] The GUI and TUI share the same config and data, so they can be used interchangeably. -- evidence: [README.md#L173-L173](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L173-L173) (`clm_8da932825b83edab2503cd1c5f3019f0ca5989f56da48e992e32ef5028100d00`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Beehive requires git and the GitHub CLI for all usage, and gh authentication is required because repo operations use gh. -- evidence: [README.md#L77-L82](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L77-L82), [README.md#L84-L86](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L84-L86) (`clm_9318896033ea98e9bd4a004a4e90ace8a2089539965fd310e76198cd7a871a78`)

## limitations (1 claim(s))

- [observation/documented] The desktop GUI is macOS-only for now; the standalone TUI supports macOS (Apple Silicon) and Linux x86_64 glibc, and Windows support is not yet available. Intel macOS is listed as untested for both. -- evidence: [README.md#L88-L88](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L88-L88), [README.md#L187-L192](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L187-L192) (`clm_a6fd43fa068e6a5bcea4ac2574521f21a5e5364b22166d97f840873f20475cbd`)

## relevance (1 claim(s))

- [inference/documented] The tool appears aimed at developers juggling several GitHub repositories who want parallel terminal and CLI coding-agent sessions in branch-isolated workspace clones. -- evidence: [README.md#L46-L56](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L46-L56), [README.md#L3-L3](https://github.com/storozhenko98/beehive/blob/42e6a36ead6da1e22004a46e5ed3b41589c2fac4/README.md#L3-L3) (`clm_577c573ac08f2c59f35c0caa230d4f25b408c0638717f52734e90eab30693f7a`)

