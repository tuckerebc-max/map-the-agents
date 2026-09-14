# paean-ai/deeptide -- full detail

[Back to orientation](deeptide.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/paean-ai/deeptide/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/b47b4daf011a3fc2.json](../../../wiki/dossiers/paean-ai/deeptide/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/b47b4daf011a3fc2.json)

## specifications (1 claim(s))

- [observation/documented] DeepTide is an agentic coding assistant in which the model plans, calls tools, observes results, and adapts; it ships as a macOS native app, a cross-platform Bun CLI, and a Rust CLI with an optional desktop GUI. -- evidence: [README.md#L23-L31](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L23-L31), [README.md#L204-L205](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L204-L205) (`clm_12194fbe820b2259db492dff0cda5274c345046a191e1856f1c72fd122ae9cf3`)

## components (2 claim(s))

- [observation/documented] The repo hosts two npm packages: `deeptide`, a thin redirect to @paean-ai/zero-cli, and `deeptide-rs`, which ships a native Rust binary via GitHub Releases postinstall; the Rust port lives under crates/. -- evidence: [README.md#L45-L48](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L45-L48), [README.md#L320-L326](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L320-L326), [README.md#L36-L39](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L36-L39) (`clm_857bfcda8b534e951d3bd382dba190f8be110c8190368fa36037245476f53e94`)
- [observation/documented] The repository also contains a native local inference runtime under native/: a hard-forked ds4 DeepSeek V4 Flash Metal engine and dsgo, an OpenAI/Anthropic-compatible local gateway, built via npm run build:native on macOS. -- evidence: [README.md#L279-L279](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L279-L279), [README.md#L50-L53](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L50-L53), [README.md#L287-L290](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L287-L290) (`clm_7755b96dec60b4b49e49995c580fe658e22ab47a352fddafd92f12cda2e81bc4`)

## design-choices (1 claim(s))

- [observation/documented] The local V4 Flash Q2 profile caps context at 64k, disables subagents, and forces serial tool execution, because Q2's attention quality degrades on long contexts and parallel tool calls compound state too quickly. -- evidence: [docs/deepseek-v4-flash-q2.md#L36-L36](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L36-L36), [docs/deepseek-v4-flash-q2.md#L38-L38](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L38-L38) (`clm_8e8afd0d0185b227560829480e5fd38d291249765313e1a7270d018b7791701b`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors build the Rust GUI from the crates/ workspace with cargo run/build -p deeptide-gui, build native components with npm run build:ds4 / build:dsgo, and report security vulnerabilities via private vulnerability reporting, redacting sensitive data from logs. -- evidence: [README.md#L310-L314](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L310-L314), [README.md#L190-L192](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L190-L192), [README.md#L287-L290](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L287-L290), [README.md#L302-L308](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L302-L308) (`clm_27f327dd6ad63736d4f211e373dc56b9262582e4f758a197116465eb937f0994`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI installs `deeptide` and `tide` commands supporting an interactive REPL, one-shot mode via `-p`, `--base-url`/`--api-key` for BYOK providers, `tide auth login`, and `tide doctor` diagnostics. -- evidence: [README.md#L141-L141](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L141-L141), [README.md#L69-L74](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L69-L74), [README.md#L105-L110](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L105-L110) (`clm_79dc8dd248488e7e39470c24db26e8b3275730bed49b959ebc07f3762c2c0ffe`)
- [observation/documented] The Rust GUI shares the CLI's configuration (~/.config/tide/settings.json and project .deeptide/settings.json), on-disk session store resumable via `--resume`, and full tool set; it is launched with `deeptide-rs --gui` or the `deeptide-gui` binary. -- evidence: [README.md#L180-L180](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L180-L180), [README.md#L156-L159](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L156-L159), [README.md#L161-L168](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L161-L168), [README.md#L183-L184](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L183-L184) (`clm_aa2f60178a1f2bd60e3f20d90c41b240a59054fac10e3a737aa0bee7a8fa7e16`)

## memory-state (1 claim(s))

- [observation/documented] DeepTide includes a persistent project memory system across sessions, and GUI and CLI conversations share the same on-disk session store so chats started in either can be resumed in the other. -- evidence: [README.md#L207-L224](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L207-L224), [README.md#L161-L168](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L161-L168) (`clm_95bc9a895857b64e8407fb3617264079e97ace343941401fb16e001dd3ca7e22`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product offers 30+ built-in tools (file I/O, shell, web, tasks, MCP, scheduling, sub-agents), 25+ slash commands, and four permission modes: default, accept-edits, plan, and bypass. -- evidence: [README.md#L207-L224](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L207-L224) (`clm_7bb767a79497261e7693acccbdb0945fa970c7d4369ee76b1af5b27a8de53732`)

## evaluation (1 claim(s))

- [observation/documented] The repo references a local-agent benchmark suite under benchmarks/local-agent/ used to check long-context regressions (32k/64k/96k prompts) before raising the V4 Flash context window, and the quant doc prescribes four workload checks including long-context recall and expert-diversity testing. -- evidence: [docs/deepseek-v4-flash-iq2-asymmetric.md#L137-L140](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-iq2-asymmetric.md#L137-L140), [docs/deepseek-v4-flash-q2.md#L53-L53](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L53-L53) (`clm_c1c0a93c5ea8622c05d806f9a81c33113ed5f92d4aae11eb9b8102aabdb4efd3`)

## dependencies (1 claim(s))

- [observation/documented] The cross-platform CLI requires Bun installed and on PATH at runtime (even when installed via npm), matching its underlying Zero CLI engine; Bun sits alongside Node rather than replacing it. -- evidence: [README.md#L82-L85](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L82-L85), [README.md#L97-L97](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/README.md#L97-L97) (`clm_f14462c48b03ff756a5d8f9f3b761451c8cea55dc97931676973ed9b8f104857`)

## limitations (1 claim(s))

- [observation/documented] The shipped local DeepSeek V4 Flash Q2 build is documented as a technology-feasibility preview, not a production coding model, and is not a faithful approximation of cloud V4 behavior. -- evidence: [docs/deepseek-v4-flash-q2.md#L5-L5](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L5-L5), [docs/deepseek-v4-flash-q2.md#L13-L13](https://github.com/paean-ai/deeptide/blob/b48688d56c3eb61d0c028de2fa73dd674be2f3e8/docs/deepseek-v4-flash-q2.md#L13-L13) (`clm_192e39c4bf5178738fe73ddd1dcce0ae70694c825890fa2d490404e01ad6ce25`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

