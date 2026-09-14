# thesylvester/crispy -- full detail

[Back to orientation](crispy.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/thesylvester/crispy/a0abb0bac65bded06ae7209655cbf37aff627dbe/717deaf69b8a7ffb.json](../../../wiki/dossiers/thesylvester/crispy/a0abb0bac65bded06ae7209655cbf37aff627dbe/717deaf69b8a7ffb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (5 claim(s))

- [observation/documented] The codebase is organized into three layers: core (src/core/) owning state and logic, host (src/host/) as a thin RPC router, and webview (src/webview/) for UI. -- evidence: [CLAUDE.md#L14-L16](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L14-L16), [architecture.md#L3-L4](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L3-L4) (`clm_ea0709eb341359ebc0cabb856a5ecc98e85f082d2fb3f84f18a4333a37956516`)
- [observation/documented] Core includes vendor-agnostic transcript types, per-vendor adapters, a session-channel pub/sub multiplexer, session-manager orchestration, and an activity-index that owns all ~/.crispy/ disk I/O. -- evidence: [architecture.md#L8-L11](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L8-L11), [CLAUDE.md#L25-L34](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L25-L34) (`clm_1fe536f25a0b7092a6525ac18efa25a95d3e4d94476ba8d06bf0059dc35a3656`)
- [observation/documented] The webview uses React 19 with esbuild and vanilla CSS using VS Code theme variables, with a two-column layout of sidebar plus transcript viewer. -- evidence: [architecture.md#L46-L46](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L46-L46), [architecture.md#L48-L49](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L48-L49) (`clm_ac4a116f5472617a4e75f926cc71976339a62cb1945c37c1d8be3d922c5ad074`)
- [observation/documented] An approval system routes three approval types: standard tool-use option buttons, multi-question AskUser forms, and plan-review (ExitPlan) approvals resolved via transport.resolveApproval. -- evidence: [architecture.md#L92-L101](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L92-L101) (`clm_5369ae7e775d7b7c0fa58e4d30e417480f256a0f42cbce32193a58ebf821e162`)
- [observation/documented] The Windows desktop app auto-provisions WSL and the Crispy daemon; v0.3.4 fixed a WSL detection loop caused by reading an orphaned pre-rename node_modules/crispy/ directory. -- evidence: [README.md#L24-L24](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L24-L24), [README.md#L28-L28](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L28-L28), [README.md#L147-L152](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L147-L152) (`clm_9f1a326baced9df668784628df7d439c1222532ccfd7eb77d1f4b2e76d37633c`)

## design-choices (1 claim(s))

- [observation/documented] Core is written in a functional style: free functions with module-level state rather than classes, and the webview derives all state client-side from channel events with no direct file I/O. -- evidence: [CLAUDE.md#L57-L59](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L57-L59), [CLAUDE.md#L22-L23](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L22-L23), [architecture.md#L13-L14](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L13-L14) (`clm_8189e45d703dd865bbfce150d0a7e69c39a93e21427942b050bf84c69e1fbf8e`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run npm run typecheck, npm test (e2e pipeline test), npm run test:unit (vitest), and npm run dev for a dev server at localhost:3456, with visual checks via a browser-qa sub-agent. -- evidence: [CLAUDE.md#L170-L170](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L170-L170), [CLAUDE.md#L163-L166](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L163-L166), [CLAUDE.md#L172-L174](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L172-L174) (`clm_1d012dce7b71e72a2c9c3ff297644a7e25997f523bf240cb9ea98a87be49d04a`)
- [observation/documented] Repository development practice: CLAUDE.md forbids business logic in the host, vendor fields in transcript.ts, edits to generated Codex protocol files, and writes to ~/.crispy/ outside activity-index.ts. -- evidence: [CLAUDE.md#L75-L108](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L75-L108) (`clm_ceb8d78a9aba6ec7a67288a296fdf3b06ffcc5e0e4b6112f339c0b1668c1efa5`)
- [observation/documented] Repository development practice: user-facing skills belong in src/plugin/skills/ while dev-only tools go in .claude/skills/, and uncommitted .ai-reference/ specs must be read before changing transcript.ts or UI behavior. -- evidence: [CLAUDE.md#L178-L186](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L178-L186), [CLAUDE.md#L207-L208](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L207-L208), [CLAUDE.md#L199-L205](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L199-L205) (`clm_58f902c50383e01b70d304d2debc92a9d4c1fcd864db92fd72948cbf7b2c7102`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The webview talks to the host over a JSON-RPC protocol via a SessionService interface with dual transports: VS Code postMessage and WebSocket. -- evidence: [architecture.md#L34-L42](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L34-L42), [architecture.md#L66-L76](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L66-L76) (`clm_469016ba51996fb2c16681be17455b1021d7294a7af2cb5bcee7da2cf0f3d981`)
- [observation/documented] SessionService method groups cover session lifecycle (list/load/create/fork/close), agent control (send, interrupt, setModel, setPermissions), approvals, subscriptions, and file operations. -- evidence: [architecture.md#L66-L76](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L66-L76) (`clm_e2417184d61fc7c3e5646734dd3dac3b63c3739dd6de99fd231ffbd82090fd47`)
- [observation/documented] The standalone dev/standalone server listens on HTTP + WebSocket at port 3456 and serves the static webview bundle, auto-registering the Claude adapter at startup. -- evidence: [architecture.md#L34-L42](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L34-L42), [README.md#L206-L208](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L206-L208) (`clm_78a23726e10d5758a231084fe7e0a58db96d0a0bd355375d3be4185f3ab9152b`)
- [observation/documented] Crispy ships in three form factors: a VS Code/Cursor extension (also on OpenVSX), a standalone npm package (crispy-code) opening in the browser, and a Windows Tauri desktop installer with auto-update. -- evidence: [README.md#L5-L9](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L5-L9), [README.md#L181-L181](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L181-L181), [README.md#L167-L167](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L167-L167), [README.md#L187-L188](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L187-L188), [README.md#L147-L152](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L147-L152) (`clm_cdbcee30d34a2edf073e048143b5007994e69dc0733789bf3b89e0126e1b5fba`)

## memory-state (1 claim(s))

- [observation/documented] Agent memory indexes every session transcript locally with full-text and semantic search, backfills existing Claude Code and Codex transcripts, and recall results show match provenance with date/recency filters. -- evidence: [README.md#L75-L78](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L75-L78), [README.md#L57-L65](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L57-L65), [README.md#L13-L18](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L13-L18) (`clm_51e275040077a908f7f40b476e9491dfdc3697b12aa3feac6e1daa72f4ef6e74`)

## orchestration (1 claim(s))

- [observation/documented] /superthink pits Claude and Codex against each other on the same question and converges into a unified verdict, with sub-agents opening as live watchable tabs; /super-implement, /reflect, /handoff, and /spec-mode support planning workflows. -- evidence: [README.md#L13-L18](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L13-L18), [README.md#L93-L97](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L93-L97) (`clm_ae864fe566106b10b679583a1fa5acec78a9bc9e259563b7dc474cf5790d3ca0`)

## tools-permissions (2 claim(s))

- [observation/documented] Agency modes (plan, auto-accept, --dangerously-skip-permissions) are one-click toggles persisted per session, and a per-host Discord bot toggle lets multiple instances share one server with only one posting. -- evidence: [README.md#L57-L65](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L57-L65), [README.md#L13-L18](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L13-L18), [README.md#L103-L105](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L103-L105) (`clm_b752527e5b50a24c7c5b0ed3160935ebe3091c8b74d718479b2dfb74da3220c8`)
- [observation/documented] Tool use can be approved or denied remotely via inline Discord approval buttons, and the Discord integration uses fail-closed auth with an allowlist and a setup wizard. -- evidence: [README.md#L13-L18](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L13-L18), [README.md#L84-L87](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L84-L87) (`clm_d02e948032a95abfcfd04ce905af03614878ccf94d51637b68d165a32ad37334`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The Claude adapter depends on Anthropic's proprietary @anthropic-ai/claude-agent-sdk (required for Claude Code integration); Codex protocol types are generated from the Apache-2.0 OpenAI Codex CLI project. -- evidence: [README.md#L235-L239](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L235-L239), [README.md#L241-L243](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L241-L243) (`clm_a60400ef709db3506b802e53231cd9ead249c9b7297d388dee795827ca7c2e7a`)
- [observation/documented] Runtime requirements are Node.js 18+ for standalone use or VS Code 1.94+ for the extension, plus the Claude Code and/or Codex CLIs for whichever vendors are used. -- evidence: [README.md#L220-L222](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L220-L222) (`clm_2c0036dac8036e23e5ab46bc8b73f5ccf3c698a4572b6df12d9c29380f4c1b20`)

## limitations (1 claim(s))

- [observation/documented] Per the architecture doc, only the Claude adapter is wired up today, and the roadmap lists Gemini CLI and OpenCode support as coming soon. -- evidence: [CLAUDE.md#L10-L10](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/CLAUDE.md#L10-L10), [README.md#L158-L159](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/README.md#L158-L159), [architecture.md#L8-L11](https://github.com/TheSylvester/crispy/blob/a0abb0bac65bded06ae7209655cbf37aff627dbe/architecture.md#L8-L11) (`clm_7273e54032990d00833896455c0012f6bc36d00419dc74e6d846a0df9b98a497`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

