# oleksandrchekhovskyi/hax -- full detail

[Back to orientation](hax.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/oleksandrchekhovskyi/hax/7db349773eb70fa10e798d5b6662d4ee640dced5/bcb987170292241c.json](../../../wiki/dossiers/oleksandrchekhovskyi/hax/7db349773eb70fa10e798d5b6662d4ee640dced5/bcb987170292241c.json)

## specifications (2 claim(s))

- [observation/documented] hax is described as a minimalist, terminal-native coding agent implemented as a single native C binary with a small dependency set and low memory use. -- evidence: [README.md#L14-L27](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L14-L27), [README.md#L5-L5](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L5-L5) (`clm_97e1694f9ea8308f67ad197642023ca9026e25398050262352d0d71c1840b615`)
- [observation/documented] The product runs on Linux, macOS, FreeBSD, and OpenBSD; on Windows it is used under WSL, and the BSDs are build-from-source only. -- evidence: [README.md#L42-L43](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L42-L43) (`clm_63e789213d56068885577357f057d841d23bb86aa233dcce102425a6838d7f49`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The project deliberately omits MCP marketplaces, a plugin runtime, IDE panels, and per-command permission prompts, composing instead via subprocesses and documenting each omission in docs/philosophy.md. -- evidence: [README.md#L31-L35](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L31-L35), [README.md#L14-L27](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L14-L27) (`clm_defc6b4ab2f30fe75377dab8c4d6c2a1adfd56a0545a2f1f11d41873e00aa16f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI supports an interactive REPL, one-shot `-p` prompts (including stdin input), `-c` to continue the latest session, and `--resume`/`--resume=ID` session selection. -- evidence: [README.md#L100-L107](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L100-L107) (`clm_0f36525f32f17b453ee4879d1d93804220d1cbd4626418aa397337225ec83e72`)
- [observation/documented] In the REPL, slash commands such as `/provider`, `/model`, `/effort`, `/preset`, `/config`, and `/preset-save` select providers and settings; Ctrl-T opens a transcript view in $PAGER and Ctrl-O shows the conversation as displayed. -- evidence: [docs/configuration.md#L202-L205](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L202-L205), [docs/debugging.md#L47-L48](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L47-L48), [README.md#L82-L83](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L82-L83), [docs/configuration.md#L152-L153](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L152-L153), [docs/configuration.md#L49-L50](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L49-L50), [docs/debugging.md#L50-L52](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L50-L52) (`clm_30bcf644ee94d3af4f80a09281ab902a760de0c5d924057511c412a6f0240cb9`)
- [observation/documented] Provider support includes OpenAI and compatible endpoints, Anthropic and compatible endpoints, Codex via ChatGPT login, OpenRouter, OpenCode Zen/Go, llama.cpp, ollama, and custom endpoints configured through providers.<id> blocks. -- evidence: [docs/configuration.md#L324-L332](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L324-L332), [README.md#L85-L94](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L85-L94) (`clm_6b6385776d48222ef924641d5e9da65f1842e55b08ac8557f774829c385966c9`)
- [observation/documented] A wire-protocol trace can be collected via HAX_TRACE, capturing HTTP requests, statuses, and SSE events with credentials redacted; HAX_TRANSCRIPT mirrors the model-facing transcript to a file. -- evidence: [docs/debugging.md#L11-L13](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L11-L13), [docs/configuration.md#L255-L260](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L255-L260), [docs/debugging.md#L5-L5](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L5-L5), [docs/debugging.md#L21-L21](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/debugging.md#L21-L21) (`clm_643e2a0ab2ba1350b992425809e4d12e3230d8b478ae6c689b84a7e507d5b08c`)

## memory-state (3 claim(s))

- [observation/documented] hax follows the XDG Base Directory specification: config at ~/.config/hax/config.json, remembered interactive selections and sessions under ~/.local/state/hax/, and a model-metadata cache at ~/.cache/hax/catalog.json. -- evidence: [docs/configuration.md#L8-L9](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L8-L9), [docs/configuration.md#L11-L16](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L11-L16) (`clm_c9d5a1b88cdac4f985913f789a56f9a7e6ca46b6f036521f66d9ef710fe1bc11`)
- [observation/documented] Settings resolve in order: current-process override, resumed conversation, environment, state.json, config.json, then default; the resumed tier covers provider, model, effort, and preset. -- evidence: [docs/configuration.md#L26-L28](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L26-L28), [docs/configuration.md#L30-L32](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L30-L32) (`clm_bc9b23f179cc2547507574b6a9ac45cc57bb72cbc7b4a1e7c28673849daa812f`)
- [observation/documented] Automatic compaction summarizes history near the context limit, triggered by a configurable percentage threshold (default 85), with the context limit overridable per model. -- evidence: [docs/configuration.md#L234-L247](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L234-L247) (`clm_9b59f4f15688487fb745cb0a2d3d2ba62e878be4b35204e34833b791474440f9`)

## orchestration (2 claim(s))

- [observation/documented] Presets can act as roles with description, system-prompt additions, and a tint; only presets with a description are advertised to the model as subagent delegation targets. -- evidence: [docs/configuration.md#L184-L192](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L184-L192), [docs/configuration.md#L146-L150](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L146-L150) (`clm_5b48e394d74fd4fa22e8c34b1d56a86245e86f2f59566d205b05e13fb73bab0d`)
- [observation/documented] The agent manages background tasks with configurable wait timeout and a concurrency cap (default 32, up to 64), and bash commands detach after a default 2-minute timeout with a SIGTERM-to-SIGKILL grace period. -- evidence: [docs/configuration.md#L304-L317](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L304-L317) (`clm_0eb128f3673858b61ac29b3ec092b37a95ce3fb8ae2d00f54822e11cd41a6aef`)

## tools-permissions (1 claim(s))

- [observation/documented] The bash tool runs commands through a configurable shell with a default 2-minute timeout before detaching; the maximum timeout a model may request defaults to 30 minutes, and no per-command permission prompts exist by design. -- evidence: [README.md#L31-L35](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L31-L35), [docs/configuration.md#L304-L317](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L304-L317) (`clm_362da9659487f20a7268af2e770bc0e5fa0d6edf7fced28afd16b535c1ef1db2`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Building from source requires a C compiler, libcurl, jansson, meson, ninja, and pkg-config; fzf is additionally used for @file completion when available. -- evidence: [README.md#L70-L72](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L70-L72) (`clm_87b02669371e24fa28b69b6621de571692886c9c379d2e014c867058acb9e174`)
- [observation/documented] Model metadata (context limits, image capability, estimated spend) is fetched from models.dev and cached, refreshed in the background only when a catalog-identified provider needs it and the cache is stale; fetching can be disabled via catalog.url or catalog.refresh. -- evidence: [docs/configuration.md#L264-L267](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L264-L267), [docs/configuration.md#L269-L275](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/docs/configuration.md#L269-L275) (`clm_f236947bb815e2739c3fd0f79ebf9a5e98f648719e749328734746913f61a046`)

## limitations (1 claim(s))

- [observation/documented] By design hax lacks MCP marketplaces, a plugin runtime, IDE panels, and per-command permission prompts; the philosophy doc explains each omission and the pattern covering the need. -- evidence: [README.md#L31-L35](https://github.com/OleksandrChekhovskyi/hax/blob/7db349773eb70fa10e798d5b6662d4ee640dced5/README.md#L31-L35) (`clm_e89eb6ec1c02f1fa6269c0cd31c8271d35076382d550e55de55c8ba5876ede2a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

