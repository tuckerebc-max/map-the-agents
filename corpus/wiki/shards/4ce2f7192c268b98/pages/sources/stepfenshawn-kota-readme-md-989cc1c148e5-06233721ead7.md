---
access: public
aliases: []
claim_ids:
- clm_11fe93fc33c7b436c1305dd05157e80c44a5633e77dbcb290fdd2f0fe1e1db72
- clm_1630eaae498c97a6c7708261ebceffb8ec82008cb128c7c3968acdd88364803e
- clm_4230db96680730defeb4f8931b1ac54d40e1a6f1deeab247a16e1a4f0bcf056a
- clm_49e950bdf450950a61df0e3277cc92caec88b4e9c6285aefcc7007af8a01a18c
- clm_6003c8fd78e6083ea8d7d223ed806e050145abcddd272ae9796027a6a6f68c83
- clm_62b23b92679ba310cd6b4bd5cece1fadd1cb3dc503f5e627a67c97c13282b8a0
- clm_763730c827adfc15443d33615ce4dd26e449073cc80b2ea5bc6ad8b6f97f60f7
- clm_8694bacaf87e14273fb029f82c2ab91ef00697db14b19365a447c56536fec49d
- clm_8e27209bec8f14e4efc155b152b3e274cda3016996eb1bf2809f52e70c6b93ab
- clm_ac673f54eaeb7aaa2d76975de274c1a484713a0077ba0d288cb9e271bc9b7fc5
- clm_e0dc788bb9a217eaaf82ca187e64a7b3dc8131bd5133fdd6dc9ca76af016d477
- clm_f9bfdbef1eb70cf3ce90243d453e6e32c8db7b06025aeba0daa6cef51908e97d
maturity: draft
page_id: pg_6eecaf31436c5fdd99c306233721ead7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_efa3acb387f4531a8bf7733bb3b25e57
title: StepfenShawn/kota/README.md @ 989cc1c148e5
updated_at: '2026-09-14T02:43:26Z'
---

# StepfenShawn/kota/README.md @ 989cc1c148e5

<!-- rcw:begin owner=source:src_efa3acb387f4531a8bf7733bb3b25e57 block=evidence -->
- The project states a vim-inspired philosophy: lightweight, highly extensible, simple plain-text configuration, and focus on practical development tasks. [@claim:clm_11fe93fc33c7b436c1305dd05157e80c44a5633e77dbcb290fdd2f0fe1e1db72]
- Built-in tools include read_file, write_file, edit_file, delete_file, make_dir, scan_codebase, grep_find, exec_cmd, and update_plan for structured task plans. [@claim:clm_1630eaae498c97a6c7708261ebceffb8ec82008cb128c7c3968acdd88364803e]
- Kota is described as a lightweight, highly extensible AI code agent written in Rust, usable both as a CLI tool and as a Rust library. [@claim:clm_4230db96680730defeb4f8931b1ac54d40e1a6f1deeab247a16e1a4f0bcf056a]
- A skills system offers built-in skills (code_review, refactor, debug, documentation), each restricting the agent to a listed set of tools, activated via /skill and deactivated via /skill-off. [@claim:clm_49e950bdf450950a61df0e3277cc92caec88b4e9c6285aefcc7007af8a01a18c]
- Users can define custom commands in Lua config as simple strings or functions taking named, positional, or mixed parameters, invoked like /test file=main.rs. [@claim:clm_6003c8fd78e6083ea8d7d223ed806e050145abcddd272ae9796027a6a6f68c83]
- The interactive CLI exposes commands such as /config, /history, /skills, /skill, /load, /sessions, /delete, and /quit, with tab completion for partial commands. [@claim:clm_62b23b92679ba310cd6b4bd5cece1fadd1cb3dc503f5e627a67c97c13282b8a0]
- ContextManager stores conversation history in sessions under a .chat_sessions directory, and context is maintained automatically across chat calls. [@claim:clm_763730c827adfc15443d33615ce4dd26e449073cc80b2ea5bc6ad8b6f97f60f7]
- Configuration is Lua-based, inspired by Neovim, via a .kota/config.lua file in the project root with a kota.setup call. [@claim:clm_8694bacaf87e14273fb029f82c2ab91ef00697db14b19365a447c56536fec49d]
- The library exposes AgentBuilder and ContextManager (from kota::kota_code) for building agents with persistent session-based conversation history. [@claim:clm_8e27209bec8f14e4efc155b152b3e274cda3016996eb1bf2809f52e70c6b93ab]
- Library usage requires adding kota 0.1.3, tokio with full features, and anyhow as Cargo dependencies. [@claim:clm_ac673f54eaeb7aaa2d76975de274c1a484713a0077ba0d288cb9e271bc9b7fc5]
- Kota supports OpenAI-compatible models, DeepSeek, and Anthropic Claude, plus any OpenAI-compatible endpoint and local models via Ollama or similar services. [@claim:clm_e0dc788bb9a217eaaf82ca187e64a7b3dc8131bd5133fdd6dc9ca76af016d477]
- Per the README, MCP server support, custom UI components, and workflow definitions are planned/future features, not yet shipped. [@claim:clm_f9bfdbef1eb70cf3ce90243d453e6e32c8db7b06025aeba0daa6cef51908e97d]
<!-- rcw:end owner=source:src_efa3acb387f4531a8bf7733bb3b25e57 block=evidence -->

## Researcher notes

