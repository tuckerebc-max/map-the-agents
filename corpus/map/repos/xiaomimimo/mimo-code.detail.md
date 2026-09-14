# xiaomimimo/mimo-code -- full detail

[Back to orientation](mimo-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xiaomimimo/mimo-code/6fbb1732232c9d0ecefee209798a8586d78cb70d/d96a162cc3e28c0a.json](../../../wiki/dossiers/xiaomimimo/mimo-code/6fbb1732232c9d0ecefee209798a8586d78cb70d/d96a162cc3e28c0a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] For GPT/Codex models, a smaller tool ABI (bash, apply_patch, view_image, exec) is exposed; exec composes host tools inside QuickJS while permissions and side effects remain under host control. -- evidence: [docs/architecture/codex-microkernel-runtime.en.md#L7-L7](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L7-L7), [docs/architecture/codex-microkernel-runtime.en.md#L13-L15](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L13-L15) (`clm_2990f3cc22d78682a10f6967c7ffc961156bfc83574fed19cc0fb69812d369c9`)
- [observation/documented] The GPT profile is enabled when the model ID contains 'gpt-' (excluding 'oss' and 'gpt-4') and hides overlapping read/write/edit/grep/glob tools; prompt routing and tool profiles use separate string rules not yet unified. -- evidence: [docs/architecture/codex-microkernel-runtime.en.md#L35-L35](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L35-L35), [docs/architecture/codex-microkernel-runtime.en.md#L46-L46](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L46-L46), [docs/architecture/codex-microkernel-runtime.en.md#L44-L44](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/docs/architecture/codex-microkernel-runtime.en.md#L44-L44) (`clm_5f7e36ab93631df2b87a88ce376a949ffe84becb0522f1b166b26b0caff321cb`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: development uses bun (bun ci for frozen-lockfile install, bun run dev, bun turbo typecheck). -- evidence: [README.md#L535-L539](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L535-L539) (`clm_5c2f70f436c9fa63d9e3ae3b9cffd3f99adca62b60755283838e435c8eaa79b1`)

## skills-patterns (2 claim(s))

- [observation/documented] Builtin skills are matched by exact name, localized alias, or BM25 relevance; high-confidence matches auto-load, and users can override builtins with same-name skills in project or personal skill directories. -- evidence: [README.md#L270-L270](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L270-L270), [README.md#L238-L238](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L238-L238) (`clm_c6e1a3789e00d96753593140255b3969b9fe57f76e0218dc715db158caf2590c`)
- [observation/documented] Environment variables can disable builtin skills entirely, disable only office/media skills, or hide skills from TUI autocomplete while keeping them available to agents. -- evidence: [README.md#L275-L279](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L275-L279), [README.md#L281-L281](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L281-L281) (`clm_7f428ee8bfe61832784054a38a4c543e48f72ac63446599ec62c647e154d5a4d`)

## interfaces (3 claim(s))

- [observation/documented] MiMoCode is a terminal-native AI coding assistant that reads/writes code, runs commands, manages Git, and maintains persistent project memory across sessions. -- evidence: [README.md#L19-L19](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L19-L19) (`clm_a6020a5783bf3448215b073d5bff068ebc49ad23fd49d7a4445298d153c5b87b`)
- [observation/documented] Install options include a curl one-liner for macOS/Linux, a PowerShell script for Windows, and npm install -g @mimo-ai/cli; the CLI is launched with the `mimo` command. -- evidence: [README.md#L45-L45](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L45-L45), [README.md#L51-L51](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L51-L51), [README.md#L48-L48](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L48-L48), [README.md#L54-L55](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L54-L55) (`clm_b66d64704c64f6d5d8e8a603d2ce2e7ab446afa6ab568bc1001b6e1cd74888d6`)
- [observation/documented] First launch offers configuration via Xiaomi MiMo OAuth, Codex/ChatGPT OAuth, one-step import from Claude Code, catalog providers, or any custom OpenAI-compatible API. -- evidence: [README.md#L57-L62](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L57-L62) (`clm_d75a00647fb28292f69dfaa5a7934867c3dbd213e4b315e192ea0a2a7a8490a1`)

## memory-state (2 claim(s))

- [observation/documented] Cross-session memory uses SQLite FTS5 with files for project memory (MEMORY.md), session checkpoints, scratch notes, and per-task progress; memory is injected automatically on session resume. -- evidence: [README.md#L148-L151](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L148-L151), [README.md#L146-L146](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L146-L146), [README.md#L153-L153](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L153-L153) (`clm_34fa756b8b6e3b0863234103e432abd8f028ea360aea448417665ba6410f991a`)
- [observation/documented] Context management includes automatic checkpoints, context reconstruction near the window limit, budgeted injection with importance ranking, and a per-model adjustable compaction point via /context-limit or compaction.max_context. -- evidence: [README.md#L157-L160](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L157-L160), [README.md#L165-L167](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L165-L167) (`clm_50be779ee40350ac4133631be84aa6ba913f0ae16ea3b1330e2c856e01a743e2`)

## orchestration (3 claim(s))

- [observation/documented] Three primary agents exist: build (full permissions), plan (read-only analysis), and compose (specs-driven orchestration); Tab switches agents, and Compose is isolated once entered. -- evidence: [README.md#L140-L140](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L140-L140), [README.md#L134-L138](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L134-L138) (`clm_82691afaae0191369c8dd1789400850834a02aa9753aa0437663f423b5adc04e`)
- [observation/documented] The primary agent can spawn subagents that share session context, run in parallel, and support lifecycle tracking, cancellation, and background execution. -- evidence: [README.md#L205-L205](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L205-L205) (`clm_ad593f13fd32fd787e180bf3843be20f9fee51c21cd55ba0eda850dadaafbc0a`)
- [observation/documented] Workflows are deterministic JavaScript scripts orchestrating multiple agents with fixed phases, bounded retries, and automatic parallelization; four built-ins ship (compose, deep-research, fact-check, research-experiment), and custom ones go in .mimocode/workflows/. -- evidence: [README.md#L234-L234](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L234-L234), [README.md#L225-L230](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L225-L230), [README.md#L221-L221](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L221-L221) (`clm_2045fffbe584c14a0c4ac8123f674e87a3459fafa70a169f661d9c3dd9d6b935`)

## tools-permissions (1 claim(s))

- [observation/documented] File access outside the project directory triggers an external_directory permission prompt by default; /tmp can be allowlisted in config, and --dangerously-skip-permissions injects an allow-all base while explicit deny rules still block. -- evidence: [README.md#L514-L519](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L514-L519), [README.md#L477-L486](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L477-L486), [README.md#L468-L471](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L468-L471) (`clm_5bb0176e60f170b8b00bd0321b586e5178b37b447c1a16a0a04da0642accec96`)

## evaluation (1 claim(s))

- [inference/documented] The research-experiment workflow appears to provide an evaluation-style loop (baseline, iterate, audit against metric gaming) for mechanically verifiable metrics, though no benchmark results for the agent itself appear in the evidence. -- evidence: [README.md#L225-L230](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L225-L230) (`clm_6d2f9dc8fdb177e096afa178b202d7954a4ec4e5e3d59326b53dd323c927ec90`)

## dependencies (2 claim(s))

- [observation/documented] MiMoCode is built as a fork of OpenCode, retaining core capabilities (multiple providers, TUI, LSP, MCP, plugins) and adding memory, context management, subagents, goal loops, and dream/distill self-improvement. -- evidence: [README.md#L545-L545](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L545-L545) (`clm_9ec3c9d8c154fe705756b3126d4cc1c602d52c637b48deb43ba3b143e9817255`)
- [observation/documented] Voice input requires the sox dependency and is available to MiMo logged-in users; the ASR model mimo-v2.5-asr is only on MiMo's platform while voice control works via OpenRouter-compatible providers. -- evidence: [README.md#L287-L287](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L287-L287), [README.md#L317-L317](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L317-L317) (`clm_aed6f2a21a33d1228adcbb99fc28a99428e395453071a4559c24e6db87d443a4`)

## limitations (1 claim(s))

- [observation/documented] The README states MiMoCode does not support the built-in macOS Terminal.app, recommending iTerm2 or the VS Code integrated terminal for rendering issues. -- evidence: [README.md#L76-L76](https://github.com/XiaomiMiMo/MiMo-Code/blob/6fbb1732232c9d0ecefee209798a8586d78cb70d/README.md#L76-L76) (`clm_15240c53919e0e0e430d8728137c74f3bb4b04d4d00c7b9e6367afeb3b26045a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

