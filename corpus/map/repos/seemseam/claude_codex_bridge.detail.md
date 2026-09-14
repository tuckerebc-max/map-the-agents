# seemseam/claude_codex_bridge -- full detail

[Back to orientation](claude_codex_bridge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/seemseam/claude_codex_bridge/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/ac7d55089d5c9a56.json](../../../wiki/dossiers/seemseam/claude_codex_bridge/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/ac7d55089d5c9a56.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A background daemon keeps project state alive even after the foreground UI is closed, per the README's feature list. -- evidence: [README.md#L47-L53](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L47-L53) (`clm_6dcd2c09f9c1eb2009aedb09c19ecdfeec2b0d2e90b02e1ad27b300f61f9acd1`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Supported managed agents receive built-in ask, ccb-clear, ccb-compact, and ccb-diagnose control skills even when optional skill inheritance is disabled. -- evidence: [README.md#L305-L305](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L305-L305) (`clm_f4b7670ca95cce1abe3efa3233b723ea86ce31bfd36fb29070e79caac5e0f4c5`)

## interfaces (4 claim(s))

- [observation/documented] CCB is described as a lightweight multi-agent TUI that coordinates CLI agents such as Codex, Claude, and Gemini in visible, controllable workflows. -- evidence: [README.md#L5-L6](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L5-L6) (`clm_f8eec5c95f482c380c95364d0f3cf607f2cc23fe37990d718d3cd206b8f6d34e`)
- [observation/documented] The README badges list version 8.6.13, platforms Linux/macOS/WSL/Windows beta, and 16 CLI provider families. -- evidence: [README.md#L8-L12](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L8-L12) (`clm_ae5e5b6893353475db1f3081cdcb2499787b570194f2521bdec857567c7809f1`)
- [observation/documented] The Config UI binds to loopback only; a token source is configured in .ccb/ccb.config, and the CLI prints the URL and token source but never the token value. -- evidence: [README.md#L178-L178](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L178-L178), [README.md#L168-L168](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L168-L168) (`clm_cc436b4776af489152359ab539d738eeea1f043809d93d9df8a352bb742f9397`)
- [observation/documented] Version-2 config uses [windows] entries where commas and semicolons denote vertical stacking and horizontal splits, e.g. A,B;C,D as a four-pane layout. -- evidence: [README.md#L186-L186](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L186-L186) (`clm_2f2773f26d08e34e262f0d3434ecbec45f9935d7062db3db2d26352c4c952617`)

## memory-state (1 claim(s))

- [observation/documented] .ccb/ccb_memory.md serves as the project-wide shared memory document for collaboration rules, constraints, and agent handoff conventions. -- evidence: [README.md#L307-L307](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L307-L307) (`clm_0da90645688a2c6f8504c2e70291f396a64f27611b8ef244ca39fad98edd45e8`)

## orchestration (1 claim(s))

- [observation/documented] Agents can invoke /ask during workflow orchestration to delegate and hand off work, and users can type directly in any agent pane. -- evidence: [README.md#L221-L221](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L221-L221), [README.md#L215-L215](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L215-L215) (`clm_3c10d6eaaee86fbbda28baaa1681eba4d70f346116c3c7a158fdd55d20d18704`)

## tools-permissions (2 claim(s))

- [observation/documented] Project configuration executing tool-window commands or custom provider command templates requires exact external approval via ccb config approve-commands. -- evidence: [README.md#L406-L409](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L406-L409) (`clm_82c87afa9521263bb3701c48ee167b8b5dfc3e5c011e9e0ffed63ba21c83b78f`)
- [observation/documented] The mobile gateway binds to loopback by default; LAN binding requires a specific private interface address, and remote access uses Tailscale Serve rather than Funnel. -- evidence: [README.md#L255-L259](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L255-L259) (`clm_1e74c304ac2110b700908e69626b45591ca5c1a006512933036848e27edb3089`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The native Windows x64 beta requires Python 3.10+, WezTerm, Git Bash, and Herdr 0.8.0 or newer, with an install-local managed Python runtime. -- evidence: [README.md#L86-L90](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L86-L90) (`clm_85803b6453668e8b195ef7066087fc45c7b6214dbf206533cc85434269d31cae`)

## limitations (1 claim(s))

- [observation/documented] Release notes state that DeepSeek CLI, Z.ai, and DeepSeek Harness remain implemented but are no longer presented as current headline provider support. -- evidence: [README.md#L338-L341](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L338-L341) (`clm_6b3f9b46ef5566b57d4377427437e04fae0ad0d94d7f583d46718e31fd918972`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

