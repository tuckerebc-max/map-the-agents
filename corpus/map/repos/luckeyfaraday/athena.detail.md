# luckeyfaraday/athena -- full detail

[Back to orientation](athena.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/luckeyfaraday/athena/47ec8132d51d7911f17c539beb9ba12a9324866a/4ac2ac908f6c4b73.json](../../../wiki/dossiers/luckeyfaraday/athena/47ec8132d51d7911f17c539beb9ba12a9324866a/4ac2ac908f6c4b73.json)

## specifications (1 claim(s))

- [observation/documented] Athena is a local desktop workspace for orchestrating AI coding agents, described as version 0.1.7 and targeting Linux, Windows, and macOS. -- evidence: [README.md#L34-L34](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L34-L34), [README.md#L9-L18](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L9-L18), [README.md#L5-L7](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L5-L7) (`clm_8a8d93ae81838f58d2835505b1928347848b99dcde449908687c0e35e46cb2e4`)

## components (2 claim(s))

- [observation/documented] The app is an Electron + React frontend with a FastAPI Python backend launched by Electron, plus an MCP server under mcp_server/ exposing Athena tools to Hermes. -- evidence: [README.md#L55-L55](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L55-L55), [README.md#L72-L81](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L72-L81), [README.md#L120-L130](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L120-L130) (`clm_dc3958e785e69b4ad1e7f693c7434d6f9f9bfc2b9be926015f3ff6026eb028c1`)
- [observation/documented] Embedded terminals are implemented with node-pty in the Electron main process and rendered in the React UI with xterm.js. -- evidence: [README.md#L55-L55](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L55-L55), [README.md#L300-L300](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L300-L300), [README.md#L335-L335](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L335-L335) (`clm_2e86ca3b4194498bb51ed79361a3773d15c7299128abfce9e0c42765fd1f717f`)

## design-choices (3 claim(s))

- [observation/documented] Fresh agent panes start without project context by default; memory, recall, and instruction bundles attach only when an explicit immersive context mode is selected, creating an immutable workspace-scoped bundle and a bootstrap prompt pointing at it. -- evidence: [README.md#L302-L304](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L302-L304), [README.md#L306-L309](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L306-L309), [README.md#L595-L597](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L595-L597) (`clm_aa1fb4e0df274d617ee195e2a7bac2f2772c710679f5516cee4e114fec7f1aef`)
- [observation/documented] Terminal streaming is bounded and sequence-aware: output goes only to subscribed visible views, is retained until xterm acknowledges, replays from an atomic snapshot after remount, and sends an explicit reset/truncation marker when a consumer falls behind. -- evidence: [README.md#L337-L343](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L337-L343) (`clm_75d94a0b446fa97942df4e6b75b227eb0b1250b5fccd6366042438a5a4e26dd3`)
- [observation/documented] Session handoffs are bounded markdown summaries that filter terminal UI noise and reject or clearly mark metadata-only sessions and buffers lacking usable task evidence rather than merging full transcripts. -- evidence: [README.md#L315-L315](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L315-L315), [README.md#L319-L323](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L319-L323), [README.md#L325-L325](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L325-L325) (`clm_9ec493001227dc9dade9350ebc8f60001757043a089653a534c5d1637bd12914`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run pytest plus scripts/run_regression_checks.py and client test/build suites before PRs; PRs run the same suites in .github/workflows/pr-checks.yml, and changes to terminal streaming, session discovery, or pane layout must add a regression case. -- evidence: [README.md#L291-L293](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L291-L293), [README.md#L270-L273](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L270-L273), [README.md#L277-L283](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L277-L283), [README.md#L680-L684](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L680-L684), [README.md#L267-L268](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L267-L268) (`clm_e3d548dd41d1c383849da1fdb3c5a99c4dc1ce9008b7fe59f54c63c99a832a4b`)
- [observation/documented] Repository development practice: contributor notes say to keep run artifacts under .context-workspace/runs/<run-id>/, avoid overwriting user-owned AGENTS.md/CLAUDE.md without opt-in, and prefer adapter-specific behavior. -- evidence: [README.md#L680-L684](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L680-L684) (`clm_81565d7f3e5fbc0363d2c541857738e3ac17ef227c85264086f582d4a2a8b590`)

## skills-patterns (2 claim(s))

- [observation/documented] On every launch the app installs an agent skill named athena-context-workspace into Codex, Claude, and OpenCode skill directories, tracking installs in ~/.context-workspace/agent-skills.json so user-edited directories are not overwritten. -- evidence: [README.md#L379-L383](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L379-L383), [README.md#L385-L388](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L385-L388), [README.md#L375-L377](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L375-L377) (`clm_1e1af23e6bc6fc87153dc76d2cf4a448577cdd5c0d7fe4c82ff0aeec1efb57a0`)
- [observation/documented] A bundled Hermes skill (docs/hermes-recall-skill/SKILL.md) defines a required pattern: run session_search, summarize native sessions, write the recall cache, verify by reading it back, and report before continuing. -- evidence: [docs/hermes-recall-skill/SKILL.md#L26-L26](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/docs/hermes-recall-skill/SKILL.md#L26-L26), [docs/hermes-recall-skill/SKILL.md#L1-L4](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/docs/hermes-recall-skill/SKILL.md#L1-L4), [docs/hermes-recall-skill/SKILL.md#L28-L33](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/docs/hermes-recall-skill/SKILL.md#L28-L33) (`clm_9905ccb6d2f680fd3ae071b6fac8686f545fe303cfb9f82c128eadde530155fa`)

## interfaces (2 claim(s))

- [observation/documented] The FastAPI backend exposes endpoints including /health, /hermes/recall/*, /memory/*, /agents/adapters, /agents/sessions, /agents/spawn, and run status/artifact/cancel routes. -- evidence: [README.md#L244-L263](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L244-L263) (`clm_da6a7003124b1fd8d7238b2fc73332d6afdb2015f86092ca3d62508d77b0c2fa`)
- [observation/documented] The MCP bridge exposes context_workspace_* tools such as list/summarize agent sessions, spawn_agent, spawn_terminal, kill_terminal, close_workspace, and recall cache read/write/clear. -- evidence: [README.md#L557-L557](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L557-L557), [README.md#L543-L555](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L543-L555), [README.md#L559-L559](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L559-L559) (`clm_fdf479f880ced03bd2ca66592d269bb60449fa48d8cbe3ca8130c9aab1a53ece`)

## memory-state (2 claim(s))

- [observation/documented] Project-local recall is written to .context-workspace/hermes/session-recall.md, with audit metadata tracking source, source count, titles, byte size, refresh time, and whether recall was used by a launch. -- evidence: [README.md#L96-L101](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L96-L101) (`clm_875debc05873b500151271c6f74e9e8e3e5661d62d7892020c8002c98dbfa39f`)
- [observation/documented] The backend uses HermesManager and HermesMemoryStore for Hermes status and memory read/write; GET /memory/hermes returns plain text so CLI agents can consume it with curl. -- evidence: [README.md#L367-L369](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L367-L369), [README.md#L363-L363](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L363-L363), [README.md#L371-L371](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L371-L371) (`clm_dd881fa8ae278fb112690163ee27feca59ca72ee43aded91acd8d886ea9fd76f`)

## orchestration (1 claim(s))

- [observation/documented] The Command Room launches embedded panes for shell, Hermes, Codex, OpenCode, Claude, and Athena Code, including grid launches for parallel work, and tracks live PTYs plus historical native sessions grouped by provider. -- evidence: [README.md#L61-L66](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L61-L66), [README.md#L347-L356](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L347-L356), [README.md#L87-L92](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L87-L92) (`clm_22add2cae4cd326a730653dfa5e4a512e149e9060e6a094a02c01d133ae25cc3`)

## tools-permissions (1 claim(s))

- [observation/documented] The Electron control server requires a per-launch Bearer token for every endpoint except /health, writes the token to a 0600-permission discovery file, and enforces loopback-only Host plus cross-origin rejection to block other local processes and web pages. -- evidence: [README.md#L509-L518](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L509-L518) (`clm_3c19db0e2423c75ed87b51fa066a811e164d2f01465c4a806606b27c2e7fc9ef`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requirements are Node.js/npm and Python 3.11+ (recommended); agent CLIs (codex, opencode, claude, athena-code, grok, hermes) are optional, and the app opens without them, showing missing adapters as unavailable. -- evidence: [README.md#L146-L146](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L146-L146), [README.md#L134-L144](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L134-L144) (`clm_5f1f9be172e460e2d2883a472b426afb0b55debc34fc846f14e7d8cd270c736e`)
- [observation/documented] Packaged desktop releases bundle a self-contained backend runtime, so FastAPI, Uvicorn, and Python need not be installed on the host; setting CONTEXT_WORKSPACE_PYTHON overrides the bundled runtime. -- evidence: [README.md#L439-L443](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L439-L443), [README.md#L188-L191](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L188-L191) (`clm_96d2e7803345d6cdd24052b5c4855c6a60bc6a9872ce8f0b4af00bf904c77c64`)

## limitations (2 claim(s))

- [observation/documented] Without an agent CLI installed, related launch commands may fail inside the terminal until the CLI is on PATH; visible terminal spawning via MCP requires the Electron app itself, not just the FastAPI backend. -- evidence: [README.md#L146-L146](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L146-L146), [README.md#L499-L499](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L499-L499), [README.md#L561-L561](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L561-L561) (`clm_500aff3f4f87f0a8dde7a9793ae348e2647ba33a1b887a0f3cb3213b191a7731`)
- [observation/documented] Documented Windows quirks: launching the backend by file path fails with ModuleNotFoundError (must run as a module), and system proxies can route localhost MCP traffic through them causing 502s unless NO_PROXY excludes loopback. -- evidence: [README.md#L491-L495](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L491-L495), [README.md#L488-L489](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L488-L489) (`clm_9090636398d340dbdef4a136baa63ef330797828b1dcaa2d11a3505ab66c46b8`)

## relevance (1 claim(s))

- [observation/documented] Athena targets developers running multiple AI coding agents against one local project who need session resume, curated handoffs instead of noisy transcripts, and Hermes-driven terminal control via MCP. -- evidence: [README.md#L567-L572](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L567-L572), [README.md#L59-L59](https://github.com/luckeyfaraday/Athena/blob/47ec8132d51d7911f17c539beb9ba12a9324866a/README.md#L59-L59) (`clm_9cf242a2d3b297e6e63b36548f68cb9ca84c72ebf6e35933a0edfd759db19eee`)

