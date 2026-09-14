---
access: public
aliases: []
claim_ids:
- clm_01faf88b050a3d2b0c0242022942d26503004c107c7f306f5264b4f1509826f4
- clm_08ff060ee9a569accd2a6d45cb983231814d8a2524588a52571ac7f6d7d164b3
- clm_1f7bbd6ee1d170a4b81c8c3b1e3fde70a8500979f80a0109ba1c84eca654e566
- clm_3109c3ca64c4a93d8fd555ba21e0e8de5862549b0e9578eb71c28b07097935db
- clm_3fc1d190502cc98b3833c79e1e0f7664afec16b3415f6e2d55c99435c6b2cb44
- clm_4f8b31aca3635118f023e0608c75ad65127ab4e6c2f6f4a5aed2d0a5d891209d
- clm_552e8b273512f2b526a41c0e8e59e7b5a998e26680434966cfa398a82079ea1e
- clm_5556b9a585bed1aeb0f9bfd7e2fe94b2291a09f01567b61b11d4acda95d86c6f
- clm_568bd025fee07da25be82a6580745c4f3127ed434593d51406016b8c0647b1cc
- clm_655ec79d3a4400355f00bb82c67b0ecf8bfd93d4af195c47bf7d2e3dbcb48b57
- clm_6b938d252a89c0e7724b7d387006abe74a5c809ae22ec775666dab0412622d58
- clm_6e03e157fdbc6c013c0a3ee48aa43097945ec6a38b63ec958870d0c1dd449b38
- clm_7457678b021cf6a302a341ebdc5f63a89a2662cd3733d096f85ca9519b2f1513
- clm_7b04a9dda990acbafeabb1b09779a2d87ca4d2640caec14b27b4d7e6f020bca3
- clm_7b623d545e312f30a9140e283103929f349e8921b1f50c460a09b49aa9363e73
- clm_81a88d1b1245837f64db73ca7c9167bd388de896d3bff97986bb7b4967a6e951
- clm_85daeb1c3425a6e917ee6a7752919d8606cfcc239f83a143a414b5d087ba2c32
- clm_8fb71e1117d6e844a74b0e4725ae384ec7d00283985e50b12403b0e84be0df24
- clm_a5a30fe029976e32f74dd8d638366df32729aed4ed0e27a253bbec3abfa98e7e
- clm_ba8b7cc4faf92af58534650938aee715415889d820e3db07e44698f7504bf6c0
- clm_d65c795f0455f223c964bacc83efea63eb11ae5e86f7c96c8f3fd2f6f37e3ce3
- clm_df9499a52a05b86fa093a3b46141aeede7329907f49ed7402a9897a2a36354eb
- clm_f3e9c6df55d810327d9835759ba11e8bdfe1cc9cf1341c20ffca272abc5fd926
maturity: draft
page_id: pg_1733c72b81c05b26ae308f090115e04e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_537cc59157de59569296c20660b40a32
title: leonardcser/smelt/docs/docs/reference/configuration.md @ 9a7e6536df52
updated_at: '2026-09-14T02:12:19Z'
---

# leonardcser/smelt/docs/docs/reference/configuration.md @ 9a7e6536df52

<!-- rcw:begin owner=source:src_537cc59157de59569296c20660b40a32 block=evidence -->
- MCP servers run as child processes over stdio, registered via smelt.mcp.register with command, args, env, timeout (default 30000ms) and enabled fields; only the local server kind is supported. [@claim:clm_01faf88b050a3d2b0c0242022942d26503004c107c7f306f5264b4f1509826f4]
- Skills are on-demand knowledge packs loaded via the load_skill tool, scanned from global and project-local smelt, Claude-compatible (~/.claude, .claude), and Agent Skills-compatible (~/.agents, .agents) directories, with later entries overriding earlier ones. [@claim:clm_08ff060ee9a569accd2a6d45cb983231814d8a2524588a52571ac7f6d7d164b3]
- The reload guarantee covers only smelt-owned declarations; Lua config is trusted in-process code, not a sandbox, so arbitrary filesystem, process, or network side effects of a failing candidate are not rolled back. [@claim:clm_1f7bbd6ee1d170a4b81c8c3b1e3fde70a8500979f80a0109ba1c84eca654e566]
- Themes are ThemeSpec Lua tables with a required groups table keyed by highlight-group names; built-in colorschemes live in runtime/lua/smelt/colorschemes/ and custom ones drop into the user config directory, loaded via smelt.theme.use. [@claim:clm_3109c3ca64c4a93d8fd555ba21e0e8de5862549b0e9578eb71c28b07097935db]
- smelt uses four platform directories (config, state, data, cache) under XDG bases on Linux/macOS, storing sessions databases, OAuth credential files, recent.json picks, per-workspace permissions, prompt history, trust hashes, rotated logs, and a read-only mirror of the embedded Lua runtime. [@claim:clm_3fc1d190502cc98b3833c79e1e0f7664afec16b3415f6e2d55c99435c6b2cb44]
- smelt-managed configuration reloads transactionally: a fresh candidate is validated before replacing the running generation, and on failure existing commands, keymaps, tools, hooks, providers, settings, permissions, MCP/LSP declarations and watcher roots stay active. [@claim:clm_4f8b31aca3635118f023e0608c75ad65127ab4e6c2f6f4a5aed2d0a5d891209d]
- Model resolution on fresh launch follows CLI --model, then last explicitly chosen model from recent.json, then smelt.defaults.set in init.lua, then the first picker-visible model; /model switches at runtime and the choice is restored next launch. [@claim:clm_552e8b273512f2b526a41c0e8e59e7b5a998e26680434966cfa398a82079ea1e]
- Fast mode requests accelerated inference but requires the active model to resolve supports_fast_mode=true; /fast on|off|toggle changes the session and unsupported models reject the command. [@claim:clm_5556b9a585bed1aeb0f9bfd7e2fe94b2291a09f01567b61b11d4acda95d86c6f]
- Each skill is a directory containing a SKILL.md with YAML frontmatter (name, description) followed by agent instructions, and may include reference assets. [@claim:clm_568bd025fee07da25be82a6580745c4f3127ed434593d51406016b8c0647b1cc]
- Settings are written to smelt.settings in init.lua or via --set KEY=VALUE; unknown keys raise at access and type mismatches on assignment, and settings apply to the running session without writing to disk themselves. [@claim:clm_655ec79d3a4400355f00bb82c67b0ecf8bfd93d4af195c47bf7d2e3dbcb48b57]
- MCP tools appear in the agent's tool list with server-prefixed names (e.g. filesystem_read_file), default to ask permission, and are governed by a separate mcp ruleset matching qualified tool names. [@claim:clm_6b938d252a89c0e7724b7d387006abe74a5c809ae22ec775666dab0412622d58]
- Modes and reasoning effort are set via CLI flags or init.lua and toggled at runtime with Shift+Tab (modes) and Ctrl+T (reasoning); reasoning levels include off/low/medium/high/xhigh/max/ultra plus provider-defined labels. [@claim:clm_6e03e157fdbc6c013c0a3ee48aa43097945ec6a38b63ec958870d0c1dd449b38]
- Provider types map to specific endpoints, e.g. openai-compatible to /v1/chat/completions (Ollama, vLLM, llama.cpp, Gemini), openai to /v1/responses, anthropic to /v1/messages with thinking, and OAuth-backed codex/copilot/kimi-code endpoints. [@claim:clm_7457678b021cf6a302a341ebdc5f63a89a2662cd3733d096f85ca9519b2f1513]
- The request_audit setting controls provider-request records stored per session database: summary metadata by default, full reconstructable payloads, or off; SMELT_REQUEST_AUDIT pins the mode per process and overrides Lua config even after /reload. [@claim:clm_7b04a9dda990acbafeabb1b09779a2d87ca4d2640caec14b27b4d7e6f020bca3]
- Per-model overrides cover sampling (temperature, top_p, top_k, min_p, repeat_penalty), tool_calling toggle, context window, reasoning/fast-mode support, thinking budgets, and USD-per-1M-token cost fields. [@claim:clm_7b623d545e312f30a9140e283103929f349e8921b1f50c460a09b49aa9363e73]
- Cost tracking is built in for popular models like GPT, Claude, and DeepSeek; subscription-backed providers show zero cost, session cost appears in the status bar, totals in /stats, and unknown models default to zero cost. [@claim:clm_81a88d1b1245837f64db73ca7c9167bd388de896d3bff97986bb7b4967a6e951]
- OAuth credentials load from a provider-specific environment override, then a private JSON file in the state directory, then the OS keyring; smelt auth writes both file and keyring storage with 0600 files on Unix, and logout removes both copies. [@claim:clm_85daeb1c3425a6e917ee6a7752919d8606cfcc239f83a143a414b5d087ba2c32]
- On quota or rate-limit errors the conversation pauses with queued messages held; retries back off from 1 to 2, 4, then every 5 minutes, honoring provider reset times, and manual retry is done by pressing Enter with an empty prompt. [@claim:clm_8fb71e1117d6e844a74b0e4725ae384ec7d00283985e50b12403b0e84be0df24]
- Settings include vim keybindings, auto_compact with compact_threshold, auto_continue policy (off/goal/always), status-bar toggles for tokens/sec, tokens, cost, ghost-text prediction, tips, and file icons. [@claim:clm_a5a30fe029976e32f74dd8d638366df32729aed4ed0e27a253bbec3abfa98e7e]
- Lua API reference docs are auto-generated by `cargo xtask gen-lua-docs` and marked do-not-edit, suggesting a docs-generation step in the development workflow, though no contributor guide appears in the evidence. [@claim:clm_ba8b7cc4faf92af58534650938aee715415889d820e3db07e44698f7504bf6c0]
- Providers are registered via smelt.provider.register with types including openai-compatible, openai, codex, anthropic-compatible, anthropic, copilot, and kimi-code; unknown types fall back to openai-compatible and re-registering a name replaces the entry. [@claim:clm_d65c795f0455f223c964bacc83efea63eb11ae5e86f7c96c8f3fd2f6f37e3ce3]
- smelt.config.runtime_status() returns sanitized runtime and reload diagnostics including revisions, pending reload state, model selection, and controller convergence, and never includes credential values or Lua source contents. [@claim:clm_df9499a52a05b86fa093a3b46141aeede7329907f49ed7402a9897a2a36354eb]
- Configuration lives at ~/.config/smelt/init.lua (or %APPDATA%\smelt\init.lua on Windows, with $XDG_CONFIG_HOME overriding), can be pointed at another file with --config, and a first-launch wizard writes a starter init.lua when none exists. [@claim:clm_f3e9c6df55d810327d9835759ba11e8bdfe1cc9cf1341c20ffca272abc5fd926]
<!-- rcw:end owner=source:src_537cc59157de59569296c20660b40a32 block=evidence -->

## Researcher notes

