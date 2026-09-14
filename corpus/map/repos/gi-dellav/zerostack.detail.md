# gi-dellav/zerostack -- full detail

[Back to orientation](zerostack.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gi-dellav/zerostack/efd142b3ac46c9db79b1c318cad25bfd309acc5f/a1aca222966d5bd8.json](../../../wiki/dossiers/gi-dellav/zerostack/efd142b3ac46c9db79b1c318cad25bfd309acc5f/a1aca222966d5bd8.json)

## specifications (1 claim(s))

- [observation/documented] zerostack is a minimal coding agent written in Rust, inspired by pi and opencode. -- evidence: [README.md#L6-L6](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L6-L6) (`clm_2621f57e5e543ed6333145b2ac1421c16846c8bb4a02f5919691ed5acc9397b9`)

## components (1 claim(s))

- [observation/documented] The project is a single Rust crate with source under src/, including agent, session, permission, ui, context, and config modules; the TUI is custom on crossterm without ratatui. -- evidence: [ARCHITECTURE.md#L8-L24](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L8-L24), [ARCHITECTURE.md#L3-L4](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L3-L4), [ARCHITECTURE.md#L95-L101](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L95-L101) (`clm_086f898a17059924faa1d4771f665f96c4e2a3db45584d5cd2c852d64355e6bb`)

## design-choices (1 claim(s))

- [observation/documented] Provider abstraction uses type-erased enums (AnyClient/AnyModel/AnyAgent) instead of trait objects, and tokio runs single-threaded by default unless the multithread feature is enabled. -- evidence: [ARCHITECTURE.md#L28-L40](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L28-L40), [ARCHITECTURE.md#L95-L101](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L95-L101) (`clm_a87e4289fb44c49fd9feb8892a2c8f7a5123517cecd82802b2d23e074e6dfee9`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: unit tests live in src/tests/ and headless TUI-loop integration tests drive the real loop with a FakeBackend and mock agent models, without a terminal or network. -- evidence: [ARCHITECTURE.md#L44-L45](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L44-L45) (`clm_f5b1127ab69be0b28108aab81240fb1b93d4b9994be2eab2961f9e7d421f4238`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The agent supports multiple LLM providers: OpenRouter (default), OpenAI-compatible, Anthropic, Gemini, and Ollama, plus custom providers configured via config.yaml. -- evidence: [README.md#L536-L540](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L536-L540), [README.md#L542-L543](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L542-L543), [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32) (`clm_f224932fef0a847358ad28ff5b2ab417f26566b29c17c686ca2539a8541e2708`)
- [observation/documented] A prompts system lets users switch built-in system prompts (code, plan, review, debug, ask, etc.) at runtime via /prompt, and custom prompts can be added as markdown files under the config prompts directory. -- evidence: [README.md#L206-L208](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L206-L208), [README.md#L212-L227](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L212-L227), [README.md#L229-L230](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L229-L230) (`clm_7ae34aa3c592b144e7522469a29ee2ccd1ec4888ae939185cf8bff32600a937c`)
- [observation/documented] With the acp feature, zerostack acts as an ACP (JSON-RPC) agent server over stdio or TCP so editors like Zed can connect; ACP is not in the default build. -- evidence: [README.md#L502-L505](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L502-L505), [README.md#L517-L518](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L517-L518), [README.md#L514-L514](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L514-L514), [README.md#L507-L508](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L507-L508) (`clm_37b0a4f25d1aeaebaec119c597b8ef81651b754990e4e8ca0b8d516104bd262b`)
- [observation/documented] The agent automatically loads AGENTS.md or CLAUDE.md from the project root or ancestor directories into the system prompt, and optionally ARCHITECTURE.md under the archmd feature; -n disables context-file loading. -- evidence: [docs/ARCHITECTURE.md#L7-L8](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/docs/ARCHITECTURE.md#L7-L8), [README.md#L232-L236](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L232-L236), [docs/ARCHITECTURE.md#L12-L15](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/docs/ARCHITECTURE.md#L12-L15) (`clm_b6c32da7e15bddec977fc3a7741224fbfd94c968c01b9526dd2145d39c19ee2f`)

## memory-state (2 claim(s))

- [observation/documented] Sessions are saved as JSON under $XDG_DATA_HOME/zerostack/sessions/ and can be resumed with -c, -r, or --session <id>; auto-compaction summarizes old messages near the context-window limit. -- evidence: [README.md#L331-L333](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L331-L333), [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32), [ARCHITECTURE.md#L95-L101](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L95-L101), [ARCHITECTURE.md#L91-L91](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L91-L91) (`clm_99ae4ebf9a0c929a178f2b2f2ec7bc5c3d90e96c7c94d0b7aedbee71df455c15`)
- [observation/documented] The gated memory feature keeps plain-Markdown notes (global MEMORY.md plus per-project logs) injected into the system prompt each session; it is not in the default build. -- evidence: [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32), [README.md#L337-L338](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L337-L338), [README.md#L344-L344](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L344-L344), [README.md#L340-L342](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L340-L342) (`clm_306860977918cce409e21758b1b7a17340a36c7a785fcaf9875ad3835445592b`)

## orchestration (2 claim(s))

- [observation/documented] Git worktree integration offers /worktree, /wt-merge, and /wt-exit slash commands for a branch-per-task workflow, with optional auto-merge on exit; the feature is labeled experimental. -- evidence: [README.md#L442-L442](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L442-L442), [README.md#L463-L466](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L463-L466), [README.md#L448-L452](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L448-L452), [README.md#L440-L440](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L440-L440) (`clm_863568697c6018c7031fe8170fda8ad8cc16ec2284e1235912a0cd1487fce507`)
- [observation/documented] An iterative loop system (experimental) repeatedly works through a LOOP_PLAN.md plan with validation commands, usable via /loop in the TUI or headless flags like --loop-prompt and --loop-max. -- evidence: [README.md#L408-L408](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L408-L408), [README.md#L430-L436](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L430-L436), [README.md#L406-L406](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L406-L406), [README.md#L426-L428](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L426-L428), [README.md#L412-L416](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L412-L416) (`clm_a2b75a0e028c8e9f9f14e85445c1c8bf8269f291b6c5b0bc5a9af8127dd4a72d`)

## tools-permissions (3 claim(s))

- [observation/documented] There are five permission modes (restrictive, readonly, guarded, standard, yolo) with per-tool glob patterns, session allowlists, and doom-loop detection for repeated identical tool calls. -- evidence: [README.md#L266-L267](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L266-L267), [README.md#L250-L256](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L250-L256), [README.md#L262-L264](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L262-L264), [README.md#L14-L32](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L14-L32), [README.md#L269-L271](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L269-L271), [README.md#L248-L248](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L248-L248) (`clm_70e6634cb4583ca020b9a5ffbe32929409d6431e540997ec6a1bc8bc483d079b`)
- [observation/documented] A --dangerously-skip-permissions flag bypasses all permission checks entirely and is not a runtime-toggleable mode. -- evidence: [README.md#L258-L260](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L258-L260) (`clm_b016ef0a48afc385263a6b721486f701384c7e16606d662d3a5bb7e6acecc293`)
- [observation/documented] Optional --sandbox mode runs bash commands in bubblewrap (or zerobox on macOS), masks credential directories by default, and can require the backend via --sandbox-required; network stays on unless disabled. -- evidence: [README.md#L164-L173](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L164-L173), [README.md#L144-L146](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L144-L146), [README.md#L155-L162](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L155-L162), [README.md#L148-L153](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L148-L153), [README.md#L128-L131](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L128-L131) (`clm_3f72a61abe0f3a003d982e22d44f8b8b41ad0b184cd8aabb9ac65a137376ea4f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Core dependencies include rig 0.39, clap 4, crossterm 0.29, tokio, serde, pulldown-cmark, regex, reqwest, and mimalloc; optional features add rmcp (MCP) and agent-client-protocol (ACP). -- evidence: [ARCHITECTURE.md#L121-L121](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L121-L121), [ARCHITECTURE.md#L105-L119](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/ARCHITECTURE.md#L105-L119) (`clm_554651672dc1cb2fea8824f44ec80296b586c644f10a545663483beb814a18fd`)

## limitations (1 claim(s))

- [observation/documented] The README states Windows support is untested, and the loop and git-worktree features are explicitly marked experimental. -- evidence: [README.md#L442-L442](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L442-L442), [README.md#L408-L408](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L408-L408), [README.md#L34-L34](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L34-L34) (`clm_2e0f53730c6600e81363071e70dcfd9892eceae517417fa72b8b6f97c5ccbb39`)

## relevance (1 claim(s))

- [observation/documented] The project targets users wanting a lightweight terminal coding agent, citing ~30k LoC, a 26MB binary, and roughly 16MB average RAM versus much heavier JS-based agents. -- evidence: [README.md#L38-L38](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L38-L38), [README.md#L40-L43](https://github.com/gi-dellav/zerostack/blob/efd142b3ac46c9db79b1c318cad25bfd309acc5f/README.md#L40-L43) (`clm_4256c5f6432f8b6d742c10ed42857034047becc61bcd039200b6a0db939717d8`)

