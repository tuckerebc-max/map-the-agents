# alpbahadur/49-ide -- full detail

[Back to orientation](49-ide.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/alpbahadur/49-ide/c8bfb5c0a3552264412e39cd9c12ced75627d735/9e8ea4ce68281998.json](../../../wiki/dossiers/alpbahadur/49-ide/c8bfb5c0a3552264412e39cd9c12ced75627d735/9e8ea4ce68281998.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Terminals are real tmux sessions served via ttyd with ANSI color, scrollback, and the user's shell config, plus broadcast input to multiple terminals at once. -- evidence: [README.md#L94-L95](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L94-L95), [README.md#L111-L114](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L111-L114) (`clm_1d42606b8ffd4f0b0c0b23c4ae7703992276ae63d6d521c278a6156347ca14dd`)
- [observation/documented] A macOS desktop app is distributed as a .dmg on GitHub Releases, runs as a tray icon, is not notarized (requiring an xattr workaround), and offers in-app update checks. -- evidence: [README.md#L79-L79](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L79-L79), [README.md#L71-L71](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L71-L71), [README.md#L69-L69](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L69-L69), [README.md#L77-L77](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L77-L77) (`clm_adce38f8c4c45e63c70ee2600e9c4efad06013da4f50f15a251e4f9b2e36679e`)
- [observation/documented] A HUD overlay shows live CPU, RAM, and Claude API usage across all connected machines, and agents from any machine join one canvas without SSH. -- evidence: [README.md#L99-L100](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L99-L100) (`clm_12589f1cdcf149c44a218ecc39d1017f52618bd386ce02c3d1ac06839f672028`)

## design-choices (1 claim(s))

- [observation/documented] The relay stores no terminal data server-side; terminal I/O is relayed, never persisted, and self-hosting keeps terminals and files on the user's machine. -- evidence: [README.md#L59-L62](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L59-L62), [README.md#L148-L151](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L148-L151), [README.md#L104-L107](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L104-L107) (`clm_d62ea3cac180e8b555e0a3d2954944c69ab0bb192504144cffba0684d5fa340d`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: contributors must sign a CLA on their first PR by commenting a fixed statement, granting the organization copyright, patent, and relicensing rights, because the project is BSL 1.1 licensed. -- evidence: [CONTRIBUTING.md#L8-L11](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CONTRIBUTING.md#L8-L11), [CLA.md#L22-L26](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L22-L26), [CLA.md#L40-L48](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L40-L48), [CLA.md#L76-L77](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L76-L77), [CONTRIBUTING.md#L18-L19](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CONTRIBUTING.md#L18-L19), [CLA.md#L30-L36](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L30-L36) (`clm_2cba7901fd90f6ac21d6bcaba4e912418eb3b71789d24be6fc9372dd57b4c054`)
- [observation/documented] Repository development practice: AGENTS.md mandates using the bd (beads) CLI for all issue tracking (bd ready/claim/close, --json flags, discovered-from links) and forbids markdown TODO lists or external trackers. -- evidence: [AGENTS.md#L166-L171](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L166-L171), [AGENTS.md#L183-L189](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L183-L189), [AGENTS.md#L111-L111](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L111-L111) (`clm_84f50bcfa158291569bb36ecc49a79c45a363138c7f4c0be527e1a6b45424978`)
- [observation/documented] Repository development practice: CLAUDE.md instructs coding agents to never work in master, use worktrees/branches named with beads issue IDs, never push or merge without explicit user consent, and rebuild minified client JS and the agent tarball after changes. -- evidence: [CLAUDE.md#L17-L22](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L17-L22), [CLAUDE.md#L1-L2](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L1-L2), [CLAUDE.md#L24-L26](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L24-L26), [CLAUDE.md#L12-L12](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L12-L12), [CLAUDE.md#L8-L8](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L8-L8) (`clm_5a51678584c3267c7fde2b387461fed4610e33c57e609f0027c750b717f2af25`)
- [observation/documented] Repository development practice: CLAUDE.md imposes context-mode MCP routing rules for contributor agents — curl/wget, WebFetch, and inline HTTP in Bash are blocked in favor of ctx_* tools, with Bash limited to short-output commands. -- evidence: [CLAUDE.md#L46-L48](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L46-L48), [CLAUDE.md#L30-L30](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L30-L30), [CLAUDE.md#L35-L38](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L35-L38), [CLAUDE.md#L41-L43](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L41-L43), [CLAUDE.md#L53-L56](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLAUDE.md#L53-L56) (`clm_996a8df9dba4eca51a84d4acdb4a028df67ac4192cd7f8159215debc9adeeceb`)
- [observation/documented] Repository development practice: AGENTS.md documents a development-only multi-instance mode where each worktree runs its own stack, keyed by cloud URL, with per-instance database, config dir, ttyd port block, and tmux socket. -- evidence: [AGENTS.md#L46-L47](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L46-L47), [AGENTS.md#L41-L44](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L41-L44), [AGENTS.md#L49-L54](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L49-L54) (`clm_56c607444c13efd343b0bad148f8bc59a3b2d415ff33771ad4336ba85174f0fb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is described as a 2D agentic IDE whose workspace is an infinite zoomable canvas of draggable, resizable panes with persistent layout, replacing terminal tabs. -- evidence: [README.md#L87-L90](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L87-L90), [README.md#L7-L7](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L7-L7) (`clm_15cbb01876bc042379bc22299e72ca3b8d527372054afe0e4ef400db21cdbdd5`)
- [observation/documented] Setup uses a 49ctl CLI: './49ctl setup' for one-time interactive setup and './49ctl start' to launch the cloud server and agent, then the UI is served at localhost:1071 with no account or login. -- evidence: [README.md#L50-L55](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L50-L55), [README.md#L57-L57](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L57-L57) (`clm_e7460fadefa1a461847867265734c0c775383e41c9c47b15c4d00e09a0c33413`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Architecture: 49-agent processes on machines connect over WSS to a relay (self-hosted or 49agents.com), which browsers on phones, laptops, and tablets also connect to; each agent connects independently via WebSocket. -- evidence: [README.md#L132-L146](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L132-L146), [README.md#L120-L127](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L120-L127), [README.md#L148-L151](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L148-L151) (`clm_e316b82e2913f340a8fc17fec64f75097672defc524870fe4a685b1214e04050`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product integrates Beads (steveyegge/beads) for interactive issue tables on the canvas; the agent runs via node agent/bin/49-agent.js and the cloud server via node cloud/src/index.js. -- evidence: [README.md#L34-L44](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L34-L44), [AGENTS.md#L64-L64](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L64-L64), [AGENTS.md#L67-L68](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L67-L68) (`clm_a6a5efcc5808fe6a36c25c6229123d0476708f62ab97bbaed7456427b64c46ee`)

## limitations (1 claim(s))

- [observation/documented] The macOS app is not notarized, so macOS blocks it on first launch until the user runs 'xattr -cr' on the app bundle. -- evidence: [README.md#L71-L71](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L71-L71), [README.md#L73-L75](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L73-L75) (`clm_679c79dabf272228f6ba85837afe8147c227eef3d4b115a0fdec715766d6b1f0`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

