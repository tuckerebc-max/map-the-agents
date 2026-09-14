# minghinmatthewlam/pi-gui -- full detail

[Back to orientation](pi-gui.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/minghinmatthewlam/pi-gui/eb9a7380705dffad36db3efa771ee825aafbef6f/337c0a03359906f9.json](../../../wiki/dossiers/minghinmatthewlam/pi-gui/eb9a7380705dffad36db3efa771ee825aafbef6f/337c0a03359906f9.json)

## specifications (1 claim(s))

- [observation/documented] pi-gui is a Codex-style desktop app for the pi coding agent, in public beta for macOS (Apple Silicon) and Linux (AppImage). -- evidence: [README.md#L52-L52](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L52-L52), [README.md#L3-L3](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L3-L3) (`clm_74c52ebfcfd9961d38e015505f601039c0bfb086441c160503a39b0025e2a896`)

## components (2 claim(s))

- [observation/documented] The Electron app is split into a React renderer, a narrow preload IPC bridge, and a Node main process handling windowing, session supervision, worktrees, PTYs, notifications, and persistence. -- evidence: [README.md#L90-L91](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L90-L91), [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104) (`clm_f55da37270386608e70c36267407f18c52354ebe18533e886ad85a2ec067a2cd`)
- [observation/documented] Supporting packages include pi-sdk-driver (a thin adapter to the pi coding agent), session-driver (shared session driver types), and catalogs (workspace/session catalog state). -- evidence: [README.md#L145-L149](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L145-L149), [README.md#L106-L107](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L106-L107), [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104) (`clm_e6e3569065d57049a44c6ea05da0a4d19a33844dc507a599ba5687207a2c6d0b`)

## design-choices (1 claim(s))

- [observation/documented] The app is a UI shell around @earendil-works/pi-coding-agent rather than a separate agent runtime; session management, auth setup, and agent execution run through upstream pi. -- evidence: [README.md#L9-L14](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L9-L14) (`clm_7e006a36f54d73716fb27c29ffb551414f644b139bc7568daa3f4cd500536dc4`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors use Node 20+ with pnpm via corepack, and run pnpm dev/build/typecheck/lint/test from the repo root; desktop E2E tests use a Playwright+Electron harness split into lanes, with the core lane run by default. -- evidence: [README.md#L132-L134](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L132-L134), [README.md#L111-L112](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L111-L112), [README.md#L129-L130](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L129-L130), [README.md#L121-L127](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L121-L127) (`clm_832d90395d1481406e81d3762fe90137ef7f65d0b498c11b5daae173fc003fad`)
- [observation/documented] Repository development practice: AGENTS.md instructs defining success criteria before coding, planning verification with the self-test skill, committing in small focused checkpoints, and running simplify before closing non-trivial work. -- evidence: [AGENTS.md#L6-L10](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/AGENTS.md#L6-L10) (`clm_02f77ecb9c52d53c09ae1eff8c1019cf677d7ce9b70abfd6fe2ff5762bac12c5`)
- [observation/documented] Repository development practice: desktop changes are expected to be verified on the real Electron surface, not only by unit tests, and contributors must not delete session history or artifacts without approval. -- evidence: [AGENTS.md#L13-L16](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/AGENTS.md#L13-L16), [README.md#L153-L155](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L153-L155), [AGENTS.md#L19-L21](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/AGENTS.md#L19-L21) (`clm_5c4cc40242278bcef3764eedbe513954a656a1b914a99a5120a08df94e31649a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The renderer communicates with the main process only through a typed IPC surface exposed by the preload bridge, with no broad Node access granted to the renderer. -- evidence: [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104) (`clm_4f71d3eaf14a8b67b90842ea2abbd1536f6dd003919b1adeb9ba65afd87b733e`)
- [observation/documented] Features include a threaded timeline with collapsible tool calls, an integrated node-pty terminal, an inline diff viewer toggled with Cmd/Ctrl+D, @-file mentions, image attachments, themes, and OS notifications when runs finish. -- evidence: [README.md#L32-L48](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L32-L48) (`clm_3a6ffe09b53ab3335f02eb53ea0fca967a1b611290503c2cfa3f9e796656c7ce`)

## memory-state (1 claim(s))

- [observation/documented] pi persists each session as a JSONL transcript on disk, and pi-gui reads those files as the authoritative record for closed sessions instead of keeping a divergent copy. -- evidence: [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104) (`clm_6032897e5cc7d98bab7e9b8e9a6b4363cb29ea9c47b00757f704d0d1f4f58389`)

## orchestration (1 claim(s))

- [observation/documented] An orchestrator thread can spin up and supervise child worker threads, and each thread can run locally or in an isolated git worktree so parallel work does not collide. -- evidence: [README.md#L32-L48](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L32-L48) (`clm_44331079c376013a27d99f61294eb18f19d9e5fe267ae56a734c9953a481a540`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The app depends on @earendil-works/pi-coding-agent as its upstream runtime and uses node-pty for the integrated terminal. -- evidence: [README.md#L32-L48](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L32-L48), [README.md#L9-L14](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L9-L14), [README.md#L166-L167](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L166-L167) (`clm_06e0dbd46664ed1d9c79c3e8fc24b8ddf772541e7de6da62154429f95110b5fc`)
- [observation/documented] pi-gui reuses pi's auth and session state, so provider credentials configured with the pi CLI carry over; providers connect via OAuth or API key in Settings. -- evidence: [README.md#L32-L48](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L32-L48), [README.md#L84-L86](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L84-L86) (`clm_718f2d0f03822247d92fce2429792f8fda244d9219df1824c11684a8e8719e00`)

## limitations (1 claim(s))

- [observation/documented] Native computer use is not built into pi-gui; desktop/browser control is offered separately via the author's standalone computer-use-mcp server. -- evidence: [README.md#L159-L162](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L159-L162) (`clm_3fc46f19495864502d04abb40d85a862cf3726ee243aff195f62973f5954d721`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

