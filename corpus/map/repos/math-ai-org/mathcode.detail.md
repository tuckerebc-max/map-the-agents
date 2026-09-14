# math-ai-org/mathcode -- full detail

[Back to orientation](mathcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/math-ai-org/mathcode/6774236e088bbe3bc857ce8138299addc67567b0/c2426028962b88f5.json](../../../wiki/dossiers/math-ai-org/mathcode/6774236e088bbe3bc857ce8138299addc67567b0/c2426028962b88f5.json)

## specifications (1 claim(s))

- [observation/documented] MathCode is described as a terminal AI coding assistant with built-in Lean capabilities: it can inspect goals, check candidates, search declarations, and verify finished proofs interactively. -- evidence: [README.md#L18-L20](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L18-L20) (`clm_ae4567eea1d19515df83fa6163285c5ba8cb7c94d9dbe27a04f01306db303b30`)

## components (1 claim(s))

- [observation/documented] For Lean work the agent chooses among four atomic tools: LeanGoal (inspect a source position), LeanCheck (compile a file or candidate with structured feedback), LeanSearch (query one provider), and LeanVerify (strict final check; only data.verified=true certifies completion). -- evidence: [README.md#L439-L442](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L439-L442) (`clm_b73a519f35e996af821dbb7bb25e81bd540debf5b51563f0f54a0be5b2dcc6ed`)

## design-choices (2 claim(s))

- [observation/documented] The optional /lean skill gives guidance without imposing a fixed phase, tactic order, retry budget, or planner; former fixed controllers were removed and are not release entrypoints or model-visible tools. -- evidence: [README.md#L444-L455](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L444-L455) (`clm_16e7d6fb4507877f4412c1efd259fae7e97201c1e596d767ebc86b560698fb8b`)
- [observation/documented] The default backend path uses Codex/OpenAI (GPT-6 Astra at medium effort per .env.example); an Anthropic-compatible backend can be selected with MATHCODE_USE_OPENAI=0 plus Anthropic credentials. -- evidence: [README.md#L505-L507](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L505-L507), [README.md#L516-L516](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L516-L516), [README.md#L518-L519](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L518-L519), [README.md#L509-L514](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L509-L514), [README.md#L521-L523](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L521-L523) (`clm_11ded2815bfece942a0aa8dc86617c6dd9afcf7f4a983711aa1873547ce078e6`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup.sh downloads or repairs the bundled runtime, verifies SHA256SUMS entries, creates .env from .env.example, installs a user-local launcher, and creates tools/, plugins/, and skills/ directories. -- evidence: [README.md#L66-L73](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L66-L73), [README.md#L52-L62](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L52-L62) (`clm_b2a145acc942e6b35c9907456f3778bd10c91302fe3b8e867f93e3b1b0845fc4`)
- [observation/documented] Repository development practice: maintenance commands include setup.sh --install-lean, --status (health checks on binaries, bundled rg, and Lean readiness), --clean (preserving LeanFormalizations/ and vault data), and --help. -- evidence: [README.md#L125-L130](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L125-L130), [README.md#L134-L138](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L134-L138), [README.md#L140-L142](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L140-L142) (`clm_34718f504afd90a75753dad2fa8bbe234702988f35874672f19c047645e9683a`)

## skills-patterns (3 claim(s))

- [observation/documented] Project-local skills load from .mathcode/skills/<name>/SKILL.md, one directory per skill; standalone skills/*.md files are not loaded. -- evidence: [README.md#L476-L477](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L476-L477) (`clm_46580308d9ae466a6e655fae7be441ce9e7986a8b3a03a4a8fdb4ce41c17b68e`)
- [observation/documented] Python tools with YAML frontmatter dropped in tools/ are auto-discovered at startup; three analysis tools ship bundled (axiom-checker, lib-search, proof-stats), overridable by workspace-local tools of the same name. -- evidence: [README.md#L483-L486](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L483-L486), [README.md#L481-L481](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L481-L481) (`clm_784106b7708c91951f16c013053caf22c28eca10ca38daf528f2f8849bbdc95a`)
- [observation/documented] Plugins are folders with a .mathcode-plugin/plugin.json manifest adding commands, skills, agents, MCP servers, and hooks, loaded via --plugin-dir or installed from Git repos via /plugin. -- evidence: [README.md#L490-L490](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L490-L490) (`clm_11e1298586aa4eaaef85a09fb9f9d4098bc5fea13889219c78d3c0faf996e212`)

## interfaces (4 claim(s))

- [observation/documented] The CLI accepts a prompt flag (e.g. mathcode -p "..."), piped stdin, and --help; a bundle-local ./run wrapper provides the same interface before the shell profile is reloaded. -- evidence: [README.md#L158-L162](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L158-L162), [README.md#L170-L174](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L170-L174) (`clm_d2a829af71bc42ac8a5faff887d67dad11f4a0c7fc7d71a66c48739fe2653f46`)
- [observation/documented] Interactive sessions support a /goal command with positional or --budget token budgets, optional --max-continuations, and pause/resume/status/clear subcommands; it continues the same session rather than spawning a new agent. -- evidence: [README.md#L222-L224](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L222-L224), [README.md#L215-L220](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L215-L220) (`clm_df2bf30dee16dcd7910358e7942106b61e5061f6148a3e7191912a0e8c45489c`)
- [observation/documented] A browser UI is launched via ./run webui, which sources the bundle .env, starts a local daemon, and prints an authentication URL; an interactive /webui slash command supports --no-browser, --port, --status, and --stop. -- evidence: [README.md#L185-L186](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L185-L186), [README.md#L193-L199](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L193-L199) (`clm_d6dc894a9a2535a4f7bad1be32259a86d1868320fe56165fd3e62f56033a5842`)
- [observation/documented] Model effort is set via --effort or /effort with low, medium, high, max, or a positive integer; /effort auto and /effort unset return to the model default. -- evidence: [README.md#L239-L243](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L239-L243) (`clm_f644fc95b618e71a0fd94de2159d1e7e5d0c056e632e90257e989ad8fcfb5cf4`)

## memory-state (2 claim(s))

- [observation/documented] A theorem library is managed via /theorem-store: storing one fully qualified declaration triggers fresh strict verification and a rollback-capable transaction with separate 300-second build budgets for private compilation and public Lake publication. -- evidence: [README.md#L384-L397](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L384-L397) (`clm_ca6467c88b1b25687d140bda5c2dee02e91be781a54c78f369ebcba5b185e75e`)
- [observation/documented] Conversational assumptions can be persisted as axioms per vault via /axiomatize (formalize, list, check consistency, remove); atomic Lean tool calls do not inject them implicitly. -- evidence: [README.md#L403-L408](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L403-L408), [README.md#L410-L412](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L410-L412) (`clm_e569c24415f791f921d3226ca31f57e0ce32cb343f2d3f03a41a431ea46e80c2`)

## orchestration (1 claim(s))

- [observation/documented] The CLI ships with recurring prompt scheduling enabled by default; /loop commands create short-lived loops, and durable schedules that survive restarts can be created from interactive sessions. -- evidence: [README.md#L463-L466](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L463-L466), [README.md#L459-L459](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L459-L459), [README.md#L468-L468](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L468-L468) (`clm_e00f2adf9881da73880712b6e5107c82617f8ee0660cee58b9beab456e8b628e`)

## tools-permissions (1 claim(s))

- [observation/documented] When an external Kimina Lean Server is enabled, MathCode launches it loopback-only inside a fail-closed Lean sandbox with a random bearer key kept out of the Lean REPL environment, no provider credentials, and scratch-only writes. -- evidence: [README.md#L338-L362](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L338-L362) (`clm_0df00fa8420a5dbe0c53b59cb2f3f3c2533fc98ce09e4aa0e4b4ca4da815cea9`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] Requirements include macOS arm64 or glibc Linux x86_64 with AVX2, curl, shasum or sha256sum, the codex CLI for the default backend, and optionally Python 3.12+ for bundled analysis tools. -- evidence: [README.md#L146-L152](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L146-L152) (`clm_dee41b134af1e0ff4b389db3fa36e01305479dfb401d6cbbf007685d0ecaddea`)
- [observation/documented] The release binary bundles provider SDKs for Anthropic-compatible, Bedrock, Vertex, and Foundry routes plus the MCPB/DXT plugin package, so those routes need no source checkout's node_modules. -- evidence: [README.md#L551-L555](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L551-L555) (`clm_3d2873a3483b172a13a3add20ab1c068cc6e764e85ca3df99c28e9597f952739`)
- [observation/documented] Lean support ships a versioned lean-workspace/lake-manifest.json that setup materializes without running lake update, using a bundle-local .local/elan Lean/Lake pair by default. -- evidence: [README.md#L77-L94](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L77-L94) (`clm_cc1043b8c6422269c9c4548cdad9e50f01878be35c292560641f23a159f0b3eb`)

## limitations (2 claim(s))

- [observation/documented] In release bundles the /webui slash command's source-only --rebuild option is not available. -- evidence: [README.md#L193-L199](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L193-L199) (`clm_516dc6e5b7d7b2b47e9e3723b5a1cb7140c3911c54d4fe2c2752722c9d77f482`)
- [observation/documented] WebUI provider-key rows are limited to anthropic and openrouter secrets; Codex/OpenAI routes use Codex OAuth rather than an OPENAI_API_KEY row. -- evidence: [README.md#L543-L547](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L543-L547) (`clm_51bd3d3a8bfcb3323cef46408bc31d5cab69e5e1c75501a494fe2bc7c0f994e7`)

## relevance (1 claim(s))

- [observation/documented] The project targets mathematical proof formalization: it provides theorem and axiom libraries, an Obsidian theorem-dependency graph, and Lean/Mathlib toolchain integration, and asks research users to cite it. -- evidence: [README.md#L604-L613](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L604-L613), [README.md#L77-L94](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L77-L94), [README.md#L416-L416](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L416-L416), [README.md#L375-L375](https://github.com/math-ai-org/mathcode/blob/6774236e088bbe3bc857ce8138299addc67567b0/README.md#L375-L375) (`clm_7ebe23ce3e4bab7d3d661c56156b00aa02f0180008a91c515d0151b8c5ee006b`)

