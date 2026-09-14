---
access: public
aliases: []
claim_ids:
- clm_1e1af23e6bc6fc87153dc76d2cf4a448577cdd5c0d7fe4c82ff0aeec1efb57a0
- clm_22add2cae4cd326a730653dfa5e4a512e149e9060e6a094a02c01d133ae25cc3
- clm_2e86ca3b4194498bb51ed79361a3773d15c7299128abfce9e0c42765fd1f717f
- clm_3c19db0e2423c75ed87b51fa066a811e164d2f01465c4a806606b27c2e7fc9ef
- clm_500aff3f4f87f0a8dde7a9793ae348e2647ba33a1b887a0f3cb3213b191a7731
- clm_5f1f9be172e460e2d2883a472b426afb0b55debc34fc846f14e7d8cd270c736e
- clm_75d94a0b446fa97942df4e6b75b227eb0b1250b5fccd6366042438a5a4e26dd3
- clm_81565d7f3e5fbc0363d2c541857738e3ac17ef227c85264086f582d4a2a8b590
- clm_875debc05873b500151271c6f74e9e8e3e5661d62d7892020c8002c98dbfa39f
- clm_8a8d93ae81838f58d2835505b1928347848b99dcde449908687c0e35e46cb2e4
- clm_9090636398d340dbdef4a136baa63ef330797828b1dcaa2d11a3505ab66c46b8
- clm_96d2e7803345d6cdd24052b5c4855c6a60bc6a9872ce8f0b4af00bf904c77c64
- clm_9cf242a2d3b297e6e63b36548f68cb9ca84c72ebf6e35933a0edfd759db19eee
- clm_9ec493001227dc9dade9350ebc8f60001757043a089653a534c5d1637bd12914
- clm_aa1fb4e0df274d617ee195e2a7bac2f2772c710679f5516cee4e114fec7f1aef
- clm_da6a7003124b1fd8d7238b2fc73332d6afdb2015f86092ca3d62508d77b0c2fa
- clm_dc3958e785e69b4ad1e7f693c7434d6f9f9bfc2b9be926015f3ff6026eb028c1
- clm_dd881fa8ae278fb112690163ee27feca59ca72ee43aded91acd8d886ea9fd76f
- clm_e3d548dd41d1c383849da1fdb3c5a99c4dc1ce9008b7fe59f54c63c99a832a4b
- clm_fdf479f880ced03bd2ca66592d269bb60449fa48d8cbe3ca8130c9aab1a53ece
maturity: draft
page_id: pg_663b4cf6e35b5b39bcc6d4a39d7ee196
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5076850d3be151088791f5acba56f63f
title: luckeyfaraday/Athena/README.md @ 47ec8132d51d
updated_at: '2026-09-14T02:14:53Z'
---

# luckeyfaraday/Athena/README.md @ 47ec8132d51d

<!-- rcw:begin owner=source:src_5076850d3be151088791f5acba56f63f block=evidence -->
- On every launch the app installs an agent skill named athena-context-workspace into Codex, Claude, and OpenCode skill directories, tracking installs in ~/.context-workspace/agent-skills.json so user-edited directories are not overwritten. [@claim:clm_1e1af23e6bc6fc87153dc76d2cf4a448577cdd5c0d7fe4c82ff0aeec1efb57a0]
- The Command Room launches embedded panes for shell, Hermes, Codex, OpenCode, Claude, and Athena Code, including grid launches for parallel work, and tracks live PTYs plus historical native sessions grouped by provider. [@claim:clm_22add2cae4cd326a730653dfa5e4a512e149e9060e6a094a02c01d133ae25cc3]
- Embedded terminals are implemented with node-pty in the Electron main process and rendered in the React UI with xterm.js. [@claim:clm_2e86ca3b4194498bb51ed79361a3773d15c7299128abfce9e0c42765fd1f717f]
- The Electron control server requires a per-launch Bearer token for every endpoint except /health, writes the token to a 0600-permission discovery file, and enforces loopback-only Host plus cross-origin rejection to block other local processes and web pages. [@claim:clm_3c19db0e2423c75ed87b51fa066a811e164d2f01465c4a806606b27c2e7fc9ef]
- Without an agent CLI installed, related launch commands may fail inside the terminal until the CLI is on PATH; visible terminal spawning via MCP requires the Electron app itself, not just the FastAPI backend. [@claim:clm_500aff3f4f87f0a8dde7a9793ae348e2647ba33a1b887a0f3cb3213b191a7731]
- Requirements are Node.js/npm and Python 3.11+ (recommended); agent CLIs (codex, opencode, claude, athena-code, grok, hermes) are optional, and the app opens without them, showing missing adapters as unavailable. [@claim:clm_5f1f9be172e460e2d2883a472b426afb0b55debc34fc846f14e7d8cd270c736e]
- Terminal streaming is bounded and sequence-aware: output goes only to subscribed visible views, is retained until xterm acknowledges, replays from an atomic snapshot after remount, and sends an explicit reset/truncation marker when a consumer falls behind. [@claim:clm_75d94a0b446fa97942df4e6b75b227eb0b1250b5fccd6366042438a5a4e26dd3]
- Repository development practice: contributor notes say to keep run artifacts under .context-workspace/runs/<run-id>/, avoid overwriting user-owned AGENTS.md/CLAUDE.md without opt-in, and prefer adapter-specific behavior. [@claim:clm_81565d7f3e5fbc0363d2c541857738e3ac17ef227c85264086f582d4a2a8b590]
- Project-local recall is written to .context-workspace/hermes/session-recall.md, with audit metadata tracking source, source count, titles, byte size, refresh time, and whether recall was used by a launch. [@claim:clm_875debc05873b500151271c6f74e9e8e3e5661d62d7892020c8002c98dbfa39f]
- Athena is a local desktop workspace for orchestrating AI coding agents, described as version 0.1.7 and targeting Linux, Windows, and macOS. [@claim:clm_8a8d93ae81838f58d2835505b1928347848b99dcde449908687c0e35e46cb2e4]
- Documented Windows quirks: launching the backend by file path fails with ModuleNotFoundError (must run as a module), and system proxies can route localhost MCP traffic through them causing 502s unless NO_PROXY excludes loopback. [@claim:clm_9090636398d340dbdef4a136baa63ef330797828b1dcaa2d11a3505ab66c46b8]
- Packaged desktop releases bundle a self-contained backend runtime, so FastAPI, Uvicorn, and Python need not be installed on the host; setting CONTEXT_WORKSPACE_PYTHON overrides the bundled runtime. [@claim:clm_96d2e7803345d6cdd24052b5c4855c6a60bc6a9872ce8f0b4af00bf904c77c64]
- Athena targets developers running multiple AI coding agents against one local project who need session resume, curated handoffs instead of noisy transcripts, and Hermes-driven terminal control via MCP. [@claim:clm_9cf242a2d3b297e6e63b36548f68cb9ca84c72ebf6e35933a0edfd759db19eee]
- Session handoffs are bounded markdown summaries that filter terminal UI noise and reject or clearly mark metadata-only sessions and buffers lacking usable task evidence rather than merging full transcripts. [@claim:clm_9ec493001227dc9dade9350ebc8f60001757043a089653a534c5d1637bd12914]
- Fresh agent panes start without project context by default; memory, recall, and instruction bundles attach only when an explicit immersive context mode is selected, creating an immutable workspace-scoped bundle and a bootstrap prompt pointing at it. [@claim:clm_aa1fb4e0df274d617ee195e2a7bac2f2772c710679f5516cee4e114fec7f1aef]
- The FastAPI backend exposes endpoints including /health, /hermes/recall/*, /memory/*, /agents/adapters, /agents/sessions, /agents/spawn, and run status/artifact/cancel routes. [@claim:clm_da6a7003124b1fd8d7238b2fc73332d6afdb2015f86092ca3d62508d77b0c2fa]
- The app is an Electron + React frontend with a FastAPI Python backend launched by Electron, plus an MCP server under mcp_server/ exposing Athena tools to Hermes. [@claim:clm_dc3958e785e69b4ad1e7f693c7434d6f9f9bfc2b9be926015f3ff6026eb028c1]
- The backend uses HermesManager and HermesMemoryStore for Hermes status and memory read/write; GET /memory/hermes returns plain text so CLI agents can consume it with curl. [@claim:clm_dd881fa8ae278fb112690163ee27feca59ca72ee43aded91acd8d886ea9fd76f]
- Repository development practice: contributors run pytest plus scripts/run_regression_checks.py and client test/build suites before PRs; PRs run the same suites in .github/workflows/pr-checks.yml, and changes to terminal streaming, session discovery, or pane layout must add a regression case. [@claim:clm_e3d548dd41d1c383849da1fdb3c5a99c4dc1ce9008b7fe59f54c63c99a832a4b]
- The MCP bridge exposes context_workspace_* tools such as list/summarize agent sessions, spawn_agent, spawn_terminal, kill_terminal, close_workspace, and recall cache read/write/clear. [@claim:clm_fdf479f880ced03bd2ca66592d269bb60449fa48d8cbe3ca8130c9aab1a53ece]
<!-- rcw:end owner=source:src_5076850d3be151088791f5acba56f63f block=evidence -->

## Researcher notes

