---
access: public
aliases: []
claim_ids:
- clm_06225f693747db933d7f3136a0f65b449f8d374b452d1e86ebd72186503c2520
- clm_0f116f8b5d9380e50baa0615aa1d61b658932cce2261651b1cb711c007107da5
- clm_299bcb4871abf4771455bd883ffbd2fc56e4118d300e1ca82c97dabb44a175dc
- clm_2a3c2c4b2f8c94a65c35ec5d90604f76d1f282c34cff9f412414967faebee801
- clm_2bf0de4578b961a7d9080147bebb0561775bdc1f45f6a3352b93678b555ade3b
- clm_2f711fbe0e5285214b5d14384f3dc2a0c4c3b5c9e3a221706edebbaa9d95db18
- clm_420a3d43d798aa7969f8186ffea262c5ab3bd41ee42e5e2a00cda3239737d957
- clm_6b2bbe199eda7e43e3192109650caa6134868244fe9a1875d3416af6a324589f
- clm_9556d28f055dbb68eb513c67ac54ecd299e619901ede627f5e45fa05d951b44a
- clm_c912fb44b30d2435db819d5d54c2e0adab406608ee85ac55888f4fcab53c2b1f
- clm_f124beb60ff6aae401d9d3922073e0ecaa34d8b4c177492d1ee4b36b0a82b757
maturity: draft
page_id: pg_90c47406b2cd54daaccb4f6cbf775b3e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_87dc71e2c99d5f76b6f90c47974a473b
title: Blushyes/coro-code/README.md @ 679c57af5376
updated_at: '2026-09-14T01:37:57Z'
---

# Blushyes/coro-code/README.md @ 679c57af5376

<!-- rcw:begin owner=source:src_87dc71e2c99d5f76b6f90c47974a473b block=evidence -->
- A tool-call permission system (tool/command/directory whitelists, interactive confirmation, sensitive-operation warnings) appears only as a planned roadmap item, not as a shipped capability. [@claim:clm_06225f693747db933d7f3136a0f65b449f8d374b452d1e86ebd72186503c2520]
- The core library supports exporting conversation and execution context to JSON (as a string, a file such as .coro/context.json, or a structured snapshot) and restoring it later via agent APIs like export_context_json and restore_context_from_file, exposed through coro_core::agent. [@claim:clm_0f116f8b5d9380e50baa0615aa1d61b658932cce2261651b1cb711c007107da5]
- Repository development practice: contributors are strongly recommended to install pre-commit hooks via platform-specific scripts; the hooks run cargo fmt --check, cargo clippy, and cargo test before each commit, and the contribution flow is fork, branch, change, test, PR. [@claim:clm_299bcb4871abf4771455bd883ffbd2fc56e4118d300e1ca82c97dabb44a175dc]
- Only OpenAI (gpt-4o, gpt-4o-mini) is listed as ready; Anthropic claude-3.5 and Google gemini-1.5 support are marked as coming, though env vars for those providers and Azure OpenAI are documented. [@claim:clm_2a3c2c4b2f8c94a65c35ec5d90604f76d1f282c34cff9f412414967faebee801]
- The CLI binary is named `coro`; it can run in interactive mode or accept a single task as a direct argument, and supports a `--config` flag pointing to a custom JSON config file. [@claim:clm_2bf0de4578b961a7d9080147bebb0561775bdc1f45f6a3352b93678b555ade3b]
- Installation is via `cargo install --git https://github.com/Blushyes/coro-code --bin coro`; prerequisites are Rust stable 1.70+ and an API key, with OpenAI recommended and Anthropic/Google noted as coming soon. [@claim:clm_2f711fbe0e5285214b5d14384f3dc2a0c4c3b5c9e3a221706edebbaa9d95db18]
- The persistence snapshot contains conversation_history, AgentExecutionContext, and optional AgentConfig; on restore the saved config is applied, unpaired tool results are handled automatically, and system prompts are re-injected by the agent as needed. [@claim:clm_420a3d43d798aa7969f8186ffea262c5ab3bd41ee42e5e2a00cda3239737d957]
- Coro Code is described as a high-performance AI coding agent written in Rust with a rich terminal UI, formerly named Trae Agent Rust and kept compatible with the original tool spec. [@claim:clm_6b2bbe199eda7e43e3192109650caa6134868244fe9a1875d3416af6a324589f]
- Configuration can be supplied via environment variables (OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL, and generic CORO_BASE_URL/CORO_MODEL overrides) or a `coro.json` file specifying protocol, base_url, api_key, model, and sampling params such as max_tokens, temperature, and top_p. [@claim:clm_9556d28f055dbb68eb513c67ac54ecd299e619901ede627f5e45fa05d951b44a]
- Config loading follows a unified priority of CLI arguments over environment variables over JSON file, marked completed in the roadmap; token compression (intelligent context compression with adaptive context windows) is also marked completed. [@claim:clm_c912fb44b30d2435db819d5d54c2e0adab406608ee85ac55888f4fcab53c2b1f]
- The project is dual licensed under MIT and Apache-2.0, and credits Trae Agent (original Python implementation and spec), the iocraft terminal UI framework, and model APIs from OpenAI, Anthropic, and Google. [@claim:clm_f124beb60ff6aae401d9d3922073e0ecaa34d8b4c177492d1ee4b36b0a82b757]
<!-- rcw:end owner=source:src_87dc71e2c99d5f76b6f90c47974a473b block=evidence -->

## Researcher notes

