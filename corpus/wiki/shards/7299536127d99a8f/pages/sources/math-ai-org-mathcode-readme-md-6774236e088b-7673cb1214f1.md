---
access: public
aliases: []
claim_ids:
- clm_0df00fa8420a5dbe0c53b59cb2f3f3c2533fc98ce09e4aa0e4b4ca4da815cea9
- clm_11ded2815bfece942a0aa8dc86617c6dd9afcf7f4a983711aa1873547ce078e6
- clm_11e1298586aa4eaaef85a09fb9f9d4098bc5fea13889219c78d3c0faf996e212
- clm_16e7d6fb4507877f4412c1efd259fae7e97201c1e596d767ebc86b560698fb8b
- clm_34718f504afd90a75753dad2fa8bbe234702988f35874672f19c047645e9683a
- clm_3d2873a3483b172a13a3add20ab1c068cc6e764e85ca3df99c28e9597f952739
- clm_46580308d9ae466a6e655fae7be441ce9e7986a8b3a03a4a8fdb4ce41c17b68e
- clm_516dc6e5b7d7b2b47e9e3723b5a1cb7140c3911c54d4fe2c2752722c9d77f482
- clm_51bd3d3a8bfcb3323cef46408bc31d5cab69e5e1c75501a494fe2bc7c0f994e7
- clm_784106b7708c91951f16c013053caf22c28eca10ca38daf528f2f8849bbdc95a
- clm_7ebe23ce3e4bab7d3d661c56156b00aa02f0180008a91c515d0151b8c5ee006b
- clm_ae4567eea1d19515df83fa6163285c5ba8cb7c94d9dbe27a04f01306db303b30
- clm_b2a145acc942e6b35c9907456f3778bd10c91302fe3b8e867f93e3b1b0845fc4
- clm_b73a519f35e996af821dbb7bb25e81bd540debf5b51563f0f54a0be5b2dcc6ed
- clm_ca6467c88b1b25687d140bda5c2dee02e91be781a54c78f369ebcba5b185e75e
- clm_cc1043b8c6422269c9c4548cdad9e50f01878be35c292560641f23a159f0b3eb
- clm_d2a829af71bc42ac8a5faff887d67dad11f4a0c7fc7d71a66c48739fe2653f46
- clm_d6dc894a9a2535a4f7bad1be32259a86d1868320fe56165fd3e62f56033a5842
- clm_dee41b134af1e0ff4b389db3fa36e01305479dfb401d6cbbf007685d0ecaddea
- clm_df2bf30dee16dcd7910358e7942106b61e5061f6148a3e7191912a0e8c45489c
- clm_e00f2adf9881da73880712b6e5107c82617f8ee0660cee58b9beab456e8b628e
- clm_e569c24415f791f921d3226ca31f57e0ce32cb343f2d3f03a41a431ea46e80c2
- clm_f644fc95b618e71a0fd94de2159d1e7e5d0c056e632e90257e989ad8fcfb5cf4
maturity: draft
page_id: pg_06a3113e4dc35b419b7d7673cb1214f1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7cf590cf96925f8fadc2b742381d5170
title: math-ai-org/mathcode/README.md @ 6774236e088b
updated_at: '2026-09-14T02:16:43Z'
---

# math-ai-org/mathcode/README.md @ 6774236e088b

<!-- rcw:begin owner=source:src_7cf590cf96925f8fadc2b742381d5170 block=evidence -->
- When an external Kimina Lean Server is enabled, MathCode launches it loopback-only inside a fail-closed Lean sandbox with a random bearer key kept out of the Lean REPL environment, no provider credentials, and scratch-only writes. [@claim:clm_0df00fa8420a5dbe0c53b59cb2f3f3c2533fc98ce09e4aa0e4b4ca4da815cea9]
- The default backend path uses Codex/OpenAI (GPT-6 Astra at medium effort per .env.example); an Anthropic-compatible backend can be selected with MATHCODE_USE_OPENAI=0 plus Anthropic credentials. [@claim:clm_11ded2815bfece942a0aa8dc86617c6dd9afcf7f4a983711aa1873547ce078e6]
- Plugins are folders with a .mathcode-plugin/plugin.json manifest adding commands, skills, agents, MCP servers, and hooks, loaded via --plugin-dir or installed from Git repos via /plugin. [@claim:clm_11e1298586aa4eaaef85a09fb9f9d4098bc5fea13889219c78d3c0faf996e212]
- The optional /lean skill gives guidance without imposing a fixed phase, tactic order, retry budget, or planner; former fixed controllers were removed and are not release entrypoints or model-visible tools. [@claim:clm_16e7d6fb4507877f4412c1efd259fae7e97201c1e596d767ebc86b560698fb8b]
- Repository development practice: maintenance commands include setup.sh --install-lean, --status (health checks on binaries, bundled rg, and Lean readiness), --clean (preserving LeanFormalizations/ and vault data), and --help. [@claim:clm_34718f504afd90a75753dad2fa8bbe234702988f35874672f19c047645e9683a]
- The release binary bundles provider SDKs for Anthropic-compatible, Bedrock, Vertex, and Foundry routes plus the MCPB/DXT plugin package, so those routes need no source checkout's node_modules. [@claim:clm_3d2873a3483b172a13a3add20ab1c068cc6e764e85ca3df99c28e9597f952739]
- Project-local skills load from .mathcode/skills/<name>/SKILL.md, one directory per skill; standalone skills/*.md files are not loaded. [@claim:clm_46580308d9ae466a6e655fae7be441ce9e7986a8b3a03a4a8fdb4ce41c17b68e]
- In release bundles the /webui slash command's source-only --rebuild option is not available. [@claim:clm_516dc6e5b7d7b2b47e9e3723b5a1cb7140c3911c54d4fe2c2752722c9d77f482]
- WebUI provider-key rows are limited to anthropic and openrouter secrets; Codex/OpenAI routes use Codex OAuth rather than an OPENAI_API_KEY row. [@claim:clm_51bd3d3a8bfcb3323cef46408bc31d5cab69e5e1c75501a494fe2bc7c0f994e7]
- Python tools with YAML frontmatter dropped in tools/ are auto-discovered at startup; three analysis tools ship bundled (axiom-checker, lib-search, proof-stats), overridable by workspace-local tools of the same name. [@claim:clm_784106b7708c91951f16c013053caf22c28eca10ca38daf528f2f8849bbdc95a]
- The project targets mathematical proof formalization: it provides theorem and axiom libraries, an Obsidian theorem-dependency graph, and Lean/Mathlib toolchain integration, and asks research users to cite it. [@claim:clm_7ebe23ce3e4bab7d3d661c56156b00aa02f0180008a91c515d0151b8c5ee006b]
- MathCode is described as a terminal AI coding assistant with built-in Lean capabilities: it can inspect goals, check candidates, search declarations, and verify finished proofs interactively. [@claim:clm_ae4567eea1d19515df83fa6163285c5ba8cb7c94d9dbe27a04f01306db303b30]
- Repository development practice: setup.sh downloads or repairs the bundled runtime, verifies SHA256SUMS entries, creates .env from .env.example, installs a user-local launcher, and creates tools/, plugins/, and skills/ directories. [@claim:clm_b2a145acc942e6b35c9907456f3778bd10c91302fe3b8e867f93e3b1b0845fc4]
- For Lean work the agent chooses among four atomic tools: LeanGoal (inspect a source position), LeanCheck (compile a file or candidate with structured feedback), LeanSearch (query one provider), and LeanVerify (strict final check; only data.verified=true certifies completion). [@claim:clm_b73a519f35e996af821dbb7bb25e81bd540debf5b51563f0f54a0be5b2dcc6ed]
- A theorem library is managed via /theorem-store: storing one fully qualified declaration triggers fresh strict verification and a rollback-capable transaction with separate 300-second build budgets for private compilation and public Lake publication. [@claim:clm_ca6467c88b1b25687d140bda5c2dee02e91be781a54c78f369ebcba5b185e75e]
- Lean support ships a versioned lean-workspace/lake-manifest.json that setup materializes without running lake update, using a bundle-local .local/elan Lean/Lake pair by default. [@claim:clm_cc1043b8c6422269c9c4548cdad9e50f01878be35c292560641f23a159f0b3eb]
- The CLI accepts a prompt flag (e.g. mathcode -p "..."), piped stdin, and --help; a bundle-local ./run wrapper provides the same interface before the shell profile is reloaded. [@claim:clm_d2a829af71bc42ac8a5faff887d67dad11f4a0c7fc7d71a66c48739fe2653f46]
- A browser UI is launched via ./run webui, which sources the bundle .env, starts a local daemon, and prints an authentication URL; an interactive /webui slash command supports --no-browser, --port, --status, and --stop. [@claim:clm_d6dc894a9a2535a4f7bad1be32259a86d1868320fe56165fd3e62f56033a5842]
- Requirements include macOS arm64 or glibc Linux x86_64 with AVX2, curl, shasum or sha256sum, the codex CLI for the default backend, and optionally Python 3.12+ for bundled analysis tools. [@claim:clm_dee41b134af1e0ff4b389db3fa36e01305479dfb401d6cbbf007685d0ecaddea]
- Interactive sessions support a /goal command with positional or --budget token budgets, optional --max-continuations, and pause/resume/status/clear subcommands; it continues the same session rather than spawning a new agent. [@claim:clm_df2bf30dee16dcd7910358e7942106b61e5061f6148a3e7191912a0e8c45489c]
- The CLI ships with recurring prompt scheduling enabled by default; /loop commands create short-lived loops, and durable schedules that survive restarts can be created from interactive sessions. [@claim:clm_e00f2adf9881da73880712b6e5107c82617f8ee0660cee58b9beab456e8b628e]
- Conversational assumptions can be persisted as axioms per vault via /axiomatize (formalize, list, check consistency, remove); atomic Lean tool calls do not inject them implicitly. [@claim:clm_e569c24415f791f921d3226ca31f57e0ce32cb343f2d3f03a41a431ea46e80c2]
- Model effort is set via --effort or /effort with low, medium, high, max, or a positive integer; /effort auto and /effort unset return to the model default. [@claim:clm_f644fc95b618e71a0fd94de2159d1e7e5d0c056e632e90257e989ad8fcfb5cf4]
<!-- rcw:end owner=source:src_7cf590cf96925f8fadc2b742381d5170 block=evidence -->

## Researcher notes

