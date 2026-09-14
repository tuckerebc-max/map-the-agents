# stepfenshawn/kota -- full detail

[Back to orientation](kota.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stepfenshawn/kota/989cc1c148e521c4840054da7c02e6d8662ca04a/3c083603b8cbf1b6.json](../../../wiki/dossiers/stepfenshawn/kota/989cc1c148e521c4840054da7c02e6d8662ca04a/3c083603b8cbf1b6.json)

## specifications (1 claim(s))

- [observation/documented] Kota is described as a lightweight, highly extensible AI code agent written in Rust, usable both as a CLI tool and as a Rust library. -- evidence: [README.md#L19-L19](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L19-L19), [README.md#L4-L4](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L4-L4) (`clm_4230db96680730defeb4f8931b1ac54d40e1a6f1deeab247a16e1a4f0bcf056a`)

## components (1 claim(s))

- [observation/documented] The library exposes AgentBuilder and ContextManager (from kota::kota_code) for building agents with persistent session-based conversation history. -- evidence: [README.md#L136-L138](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L136-L138), [README.md#L141-L143](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L141-L143), [README.md#L145-L151](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L145-L151) (`clm_8e27209bec8f14e4efc155b152b3e274cda3016996eb1bf2809f52e70c6b93ab`)

## design-choices (1 claim(s))

- [observation/documented] The project states a vim-inspired philosophy: lightweight, highly extensible, simple plain-text configuration, and focus on practical development tasks. -- evidence: [README.md#L10-L10](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L10-L10), [README.md#L14-L17](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L14-L17) (`clm_11fe93fc33c7b436c1305dd05157e80c44a5633e77dbcb290fdd2f0fe1e1db72`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] A skills system offers built-in skills (code_review, refactor, debug, documentation), each restricting the agent to a listed set of tools, activated via /skill and deactivated via /skill-off. -- evidence: [README.md#L308-L309](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L308-L309), [README.md#L284-L284](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L284-L284), [README.md#L302-L302](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L302-L302), [README.md#L288-L293](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L288-L293) (`clm_49e950bdf450950a61df0e3277cc92caec88b4e9c6285aefcc7007af8a01a18c`)

## interfaces (3 claim(s))

- [observation/documented] Configuration is Lua-based, inspired by Neovim, via a .kota/config.lua file in the project root with a kota.setup call. -- evidence: [README.md#L40-L45](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L40-L45), [README.md#L38-L38](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L38-L38) (`clm_8694bacaf87e14273fb029f82c2ab91ef00697db14b19365a447c56536fec49d`)
- [observation/documented] The interactive CLI exposes commands such as /config, /history, /skills, /skill, /load, /sessions, /delete, and /quit, with tab completion for partial commands. -- evidence: [README.md#L196-L205](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L196-L205), [README.md#L251-L253](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L251-L253), [README.md#L249-L249](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L249-L249) (`clm_62b23b92679ba310cd6b4bd5cece1fadd1cb3dc503f5e627a67c97c13282b8a0`)
- [observation/documented] Users can define custom commands in Lua config as simple strings or functions taking named, positional, or mixed parameters, invoked like /test file=main.rs. -- evidence: [README.md#L223-L224](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L223-L224), [README.md#L47-L50](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L47-L50), [README.md#L216-L217](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L216-L217), [README.md#L52-L56](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L52-L56) (`clm_6003c8fd78e6083ea8d7d223ed806e050145abcddd272ae9796027a6a6f68c83`)

## memory-state (1 claim(s))

- [observation/documented] ContextManager stores conversation history in sessions under a .chat_sessions directory, and context is maintained automatically across chat calls. -- evidence: [README.md#L141-L143](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L141-L143), [README.md#L157-L159](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L157-L159) (`clm_763730c827adfc15443d33615ce4dd26e449073cc80b2ea5bc6ad8b6f97f60f7`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Built-in tools include read_file, write_file, edit_file, delete_file, make_dir, scan_codebase, grep_find, exec_cmd, and update_plan for structured task plans. -- evidence: [README.md#L268-L278](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L268-L278) (`clm_1630eaae498c97a6c7708261ebceffb8ec82008cb128c7c3968acdd88364803e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Kota supports OpenAI-compatible models, DeepSeek, and Anthropic Claude, plus any OpenAI-compatible endpoint and local models via Ollama or similar services. -- evidence: [README.md#L185-L186](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L185-L186), [README.md#L180-L182](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L180-L182) (`clm_e0dc788bb9a217eaaf82ca187e64a7b3dc8131bd5133fdd6dc9ca76af016d477`)
- [observation/documented] Library usage requires adding kota 0.1.3, tokio with full features, and anyhow as Cargo dependencies. -- evidence: [README.md#L124-L130](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L124-L130) (`clm_ac673f54eaeb7aaa2d76975de274c1a484713a0077ba0d288cb9e271bc9b7fc5`)

## limitations (1 claim(s))

- [observation/documented] Per the README, MCP server support, custom UI components, and workflow definitions are planned/future features, not yet shipped. -- evidence: [README.md#L104-L110](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L104-L110), [README.md#L83-L100](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L83-L100), [README.md#L315-L318](https://github.com/StepfenShawn/kota/blob/989cc1c148e521c4840054da7c02e6d8662ca04a/README.md#L315-L318) (`clm_f9bfdbef1eb70cf3ce90243d453e6e32c8db7b06025aeba0daa6cef51908e97d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

