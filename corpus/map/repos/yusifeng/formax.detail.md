# yusifeng/formax -- full detail

[Back to orientation](formax.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yusifeng/formax/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/d2824f0bf33bfc75.json](../../../wiki/dossiers/yusifeng/formax/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/d2824f0bf33bfc75.json)

## specifications (2 claim(s))

- [observation/documented] Formax is an open-source implementation of a Claude Code-style AI assistant for software engineering tasks, offering both TUI and GUI workflows. -- evidence: [README.md#L5-L5](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L5-L5) (`clm_78387d22ebf55ebcddfe5bde6533ae6cdf03ffa18bb081894f450f4ab705f7ce`)
- [observation/documented] The project is in Beta and is positioned as better suited for learning, experimentation, and architecture study than for stable production daily use. -- evidence: [README.md#L116-L116](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L116-L116), [README.md#L9-L9](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L9-L9) (`clm_7d3f3bbb38fb44ca01152792aea227f19d5d381c3b2a4b91aac84bdd0d7fff52`)

## components (1 claim(s))

- [observation/documented] The codebase includes a hooks system (PreToolUse, PermissionRequest, PostToolUse) configured via `.formax/settings.local.json` with scripts under `.formax/hooks/*`, plus audit fields and a debug env flag. -- evidence: [CODEMAP.md#L179-L197](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/CODEMAP.md#L179-L197) (`clm_ed683449e8d0df4a65abcc2b2db7d895e48f44cc2d280aca5d2a104cd53b22c6`)

## design-choices (2 claim(s))

- [observation/documented] The architecture follows a single shared semantic core (packages/core semantics) consumed by three entry points — TUI, app-server, and Web — with renderers forbidden from forking semantic state. -- evidence: [ARCHITECTURE.md#L12-L12](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L12-L12), [ARCHITECTURE.md#L7-L10](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L7-L10), [ARCHITECTURE.md#L94-L95](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L94-L95) (`clm_eda160accb8e372065199d6a12c3dd5e94a6018276819f4488040d0f9f712eaf`)
- [observation/documented] Architectural invariants include transcript truth from semantics projection, single-writer discipline, replay parity, `replaySeq` as ordering authority, and input lifecycle closure. -- evidence: [ARCHITECTURE.md#L111-L115](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L111-L115) (`clm_fdbed5c714abe7de13d4cd1926db43328a0c1cc8c568163fefc94aab7c1c6bc4`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the project is built 100% with Codex, keeping `.codex/skills`, `docs/`, and `plans/` as traces of AI-assisted development, and semantic changes follow a contract-first change workflow. -- evidence: [README.md#L108-L110](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L108-L110), [ARCHITECTURE.md#L126-L130](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L126-L130) (`clm_d1ae779c5821a002ca883b7805e586d448a0ce5b93da7590669ac9b1898de270`)
- [observation/documented] Repository development practice: a review-findings log records code-review rounds (e.g. `codex review --uncommitted`) with P1–P3 findings, fixes verified by targeted test runs and type-checks. -- evidence: [docs/anthropic-thinking-effort-review-findings-log.md#L5-L7](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/docs/anthropic-thinking-effort-review-findings-log.md#L5-L7), [docs/anthropic-thinking-effort-review-findings-log.md#L13-L19](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/docs/anthropic-thinking-effort-review-findings-log.md#L13-L19) (`clm_f98e8bbb0a2456f0f2bba89f79051234fa48d58bc0b12048bca499a73e826acb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes commands including bare `formax` (REPL in a project directory), `formax setup`, `formax web`, `formax app-server`, and `formax serve`. -- evidence: [README.md#L70-L72](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L70-L72), [README.md#L89-L91](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L89-L91), [README.md#L62-L64](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L62-L64), [README.md#L83-L85](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L83-L85), [README.md#L46-L48](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L46-L48), [README.md#L54-L57](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L54-L57) (`clm_62d4e197ca0260a7c7725bfc4927cb52562edbf2664c51a77b19df0e809d2cc7`)
- [observation/documented] `formax app-server` provides a JSON-RPC backend over stdio for GUI/IDE clients, and `formax serve` starts only the WebSocket bridge for advanced debugging or split deployments. -- evidence: [ARCHITECTURE.md#L7-L10](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L7-L10), [README.md#L87-L87](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L87-L87), [README.md#L93-L93](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L93-L93) (`clm_d7f55ec8a4496a4ea4b97386c4ea2e623b55cde5467fcddeac95f3fbb40b6e19`)

## memory-state (1 claim(s))

- [observation/documented] Session save/replay is supported with writer/reader modules and durable transcript turn snapshots; session saving is enabled by default and can be disabled via `FORMAX_SESSION_SAVE`. -- evidence: [docs/environment-variables.md#L33-L36](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/docs/environment-variables.md#L33-L36), [CODEMAP.md#L49-L62](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/CODEMAP.md#L49-L62) (`clm_cc8cb60de48d7c35b4add6729d9b0720dcea386713ff74bc9e7a412dbef17bb5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Permissions use a deny/ask/allow rule matcher, a policy engine with preflight enforcement before tool execution, and an approval service with user prompts and remember behavior. -- evidence: [CODEMAP.md#L163-L176](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/CODEMAP.md#L163-L176), [ARCHITECTURE.md#L99-L100](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L99-L100) (`clm_a2b72fe6c9159f1cc7ca9e7411e9c792349829a39505fa5b21ecf28608fed28a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is published to npm as `@yusifeng/formax` (installed via `npm i -g @yusifeng/formax@beta`) and requires Node.js >= 20 per the README badge. -- evidence: [README.md#L11-L15](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L11-L15), [README.md#L46-L48](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L46-L48) (`clm_a0074d620198de57396be460aaa841b5c8891ac4fe8d46cc4f7e05f1bf41f9bd`)

## limitations (2 claim(s))

- [observation/documented] Documented gaps: hooks support is incomplete, WebFetch/WebSearch have known stability and behavior gaps, MCP is not supported in this version, and the Web UI is minimal. -- evidence: [README.md#L102-L104](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L102-L104) (`clm_3a1f0e62659b41600126be7b4c6929462af4abbb92205d9f0971f3be959e20b4`)
- [observation/documented] Anthropic and OpenAI-compatible providers work in setup/runtime flows, while Gemini appears in config surfaces but is not fully supported in runtime execution yet. -- evidence: [README.md#L120-L120](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L120-L120) (`clm_8531910071aaa72815c09764c3809ff19e50d1d3fd0c3b76400c8b0afa1f4100`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

