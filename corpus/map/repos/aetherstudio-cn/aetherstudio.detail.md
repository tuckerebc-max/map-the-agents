# aetherstudio-cn/aetherstudio -- full detail

[Back to orientation](aetherstudio.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aetherstudio-cn/aetherstudio/f7fcd26149f22f88c90354ef297aac400d8c20d4/9dbf470b8b2608bc.json](../../../wiki/dossiers/aetherstudio-cn/aetherstudio/f7fcd26149f22f88c90354ef297aac400d8c20d4/9dbf470b8b2608bc.json)

## specifications (3 claim(s))

- [observation/documented] AGENT_SPEC.md sets goals of production-grade Git support, SSH remote connections, Acrylic/glass UI, 60fps rendering with sub-16ms input latency, and configurable LLM API keys (OpenAI, Claude, Kimi). -- evidence: [AGENT_SPEC.md#L5-L11](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L5-L11) (`clm_f6f3af944d23d376866c241ba1daf64e9b58315403c9d90eabd1f47c3c05de1b`)
- [observation/documented] AGENT_SPEC.md lists non-goals: no new LSP/DAP features, no new plugin-system features, no additional localization, and no cloud sync or collaborative editing. -- evidence: [AGENT_SPEC.md#L14-L17](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L14-L17) (`clm_43366760b3184d893c2923802d1e949bb19867412af520144e55020e081102fc`)
- [observation/documented] AGENT_SPEC.md records that aether-ai, aether-shared, and aether-terminal crates were missing (directories present but empty) at spec time, and plans an AiClient with a complete(prompt) async method plus an AppSettings struct covering AI, UI, and remote settings. -- evidence: [AGENT_SPEC.md#L21-L36](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L21-L36), [AGENT_SPEC.md#L65-L72](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L65-L72), [AGENT_SPEC.md#L48-L54](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L48-L54) (`clm_41018fc6304a989dcee919a9cb64b0045cfb80858b43d3f097c3a7dd71f52338`)

## components (1 claim(s))

- [observation/documented] The project is a Cargo workspace split by responsibility into crates including aether-core (text buffer, lexer, search), aether-render (Direct2D rendering/themes), aether-win32 (native UI layer), aether-lsp, aether-dap, aether-remote, aether-ai, aether-tree-sitter, aether-plugin, aether-shared, and aether-cli. -- evidence: [README.md#L166-L178](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L166-L178), [README.md#L339-L351](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L339-L351) (`clm_400b79043bcfea23abe44a308a3ebc957910fd32a1a2083d4346b8402ee0a593`)

## design-choices (3 claim(s))

- [observation/documented] The editor uses a Piece Table text buffer with multi-cursor support, undo/redo history, syntax highlighting, find/replace, and auto-indentation. -- evidence: [README.md#L50-L65](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L50-L65), [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238) (`clm_d2c46354b04eeaf6b5ee9790071705c34ef7881be0a1311269792fabdd8d7417`)
- [observation/documented] The UI is self-rendered via a Direct2D/DirectWrite pipeline with themes, translucent backgrounds, shadows, animations, and dirty-rectangle optimization, on a Win32 window with DWM immersive dark mode and high-DPI support. -- evidence: [README.md#L50-L65](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L50-L65), [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238) (`clm_1df5d36482c628b390891f91bd2c4e42dfacfd1e5b2f3e1cf62d05ae8a7df3e8`)
- [observation/documented] AI integration is HTTP-based LLM interaction with DeepSeek and Kimi presets, offering code explanation, rewrite, inline suggestions, agent tool-result feedback, and an API configuration panel. -- evidence: [README.md#L50-L65](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L50-L65), [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238) (`clm_36335f66754aa7540421f29eb5f9a920fb55979496c35d3e9503177854992ac9`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: CONTRIBUTING.md requires external contributors to use a fork workflow, branch from dev (temp/ or fix/ prefixes), target PRs at dev rather than main, and follow a <type>(<scope>): <description> commit format with types like feat, fix, perf, and refactor. -- evidence: [CONTRIBUTING.md#L9-L9](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L9-L9), [CONTRIBUTING.md#L94-L95](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L94-L95), [CONTRIBUTING.md#L134-L143](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L134-L143), [CONTRIBUTING.md#L115-L115](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L115-L115), [CONTRIBUTING.md#L86-L91](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L86-L91) (`clm_efc3db0ad90748a6fc14286ab0201f689380daf83b294216402cae9af2185a3c`)
- [observation/documented] Repository development practice: a pre-push checklist mandates cargo fmt --check, cargo check -p aether-win32, and cargo test --workspace --lib --no-fail-fast; the README also documents workspace tests run with CARGO_INCREMENTAL=0 to avoid an ICE, clippy with -D warnings, a GUI smoke test script, and a coverage script. -- evidence: [README.md#L141-L142](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L141-L142), [README.md#L131-L132](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L131-L132), [README.md#L145-L146](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L145-L146), [README.md#L135-L135](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L135-L135), [CONTRIBUTING.md#L103-L107](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L103-L107) (`clm_a6d18f4ce77c2fa6edf69eb5426a5fe440bf8fc20586030948f1c4233057af85`)
- [observation/documented] Repository development practice: the README reports a test snapshot (dated 2026-07-06) of 793 passing unit tests, coverage of about 47.8% regions / 43.7% lines, a successful GUI smoke test, ~67MB memory, and a lexer benchmark of roughly 500-650 MiB/s. -- evidence: [README.md#L148-L148](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L148-L148), [README.md#L323-L331](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L323-L331), [README.md#L150-L158](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L150-L158) (`clm_9e9f67a36b6e3a57a448d175052b56300bef5811d39f79bbd4d5bffe22704637`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The aether CLI can launch the GUI, open a file path, and navigate to a line:column position such as file.txt:10:5. -- evidence: [README.md#L287-L287](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L287-L287), [README.md#L290-L291](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L290-L291), [README.md#L117-L118](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L117-L118), [README.md#L114-L114](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L114-L114) (`clm_a2b19b57ba367a9da947395975c931a256bee6881a1685017fa611aa91f89965`)
- [observation/documented] Per the Chinese feature list, the aether CLI supports --wait and --new-window flags in addition to opening paths and locating line/column positions. -- evidence: [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238) (`clm_d9479f40a9a351c7e75764f50ed2accd83361ff9eefe7c41f2c0486c05a5967b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building requires Windows 10 1809+ (Windows 11 recommended), a Rust stable toolchain pinned via rust-toolchain.toml, Visual Studio 2022 or Windows SDK build tools, and the x86_64-pc-windows-msvc target. -- evidence: [README.md#L89-L92](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L89-L92), [README.md#L262-L265](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L262-L265) (`clm_d40631a4abd79ccd20a4e57fa1415db23824a3cb9f38a55814c4ec5bb84a9f38`)

## limitations (1 claim(s))

- [observation/documented] The product currently targets only Windows 10 1809+ and Windows 11; AGENT_SPEC.md also notes the build environment lacked a Rust toolchain, so code correctness had to be ensured without compile verification. -- evidence: [README.md#L219-L219](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L219-L219), [README.md#L46-L46](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L46-L46), [AGENT_SPEC.md#L21-L36](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L21-L36) (`clm_e566c9e832b219f65dc74af7cf2cd5281569e30f38e2a488a3b9d42023ad8bd7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

