---
access: public
aliases: []
claim_ids:
- clm_19f6a1fe50e910915126c6e3e24154204181ea2e9ef6145d0c9aad92c6d21145
- clm_289d9a45a935acc31f7ea62ef3ec1877634557a826d55c7c8d4b8e4603205e62
- clm_45962e30e2d834ed077cdaf03eeea9f64a159f35a8283dc5552f757a4659eda2
- clm_587cf0e6e55bf20beec41f13e0e9a714c7ed82f34585a61adfef17c9e6543972
- clm_6c5763b2df9b4d35ca0c7048cecf05aa9ea3a69a31d73848498206f92bbc0506
- clm_6e01732b68812becd1e6bb28f9e1bd9fbb46fd3e477aa680402e35f518182a7c
- clm_6fc00ef2327e15ebbfd48f04c498908366632ad35e2455ba89d95372be51d8fd
- clm_8b59eadc5eec9a339be46583e3e4b9d8e1658a3ce18f67817c46b8e3d2d8a1b8
- clm_8fd2b0c4e6bef439dfb5907a1f87ae3c35fead3253615990e27bcb938789fb75
- clm_93d47e2b6d411086fb4cf06f4861501a94596e35ee188cecc732ad8975ef90af
- clm_abd1d5587ab29595ba0913267d3f267f8c5ab7fb2ffc4299d2470a8982f50c61
- clm_b37c78a8766b5138350bc0aa7b06ac4b2019ec7e15aab7846933f215a8fba879
- clm_da4ea9d8ba5ad2e4a5f680c6babf552b7db794af22e2d2e53c5fff0f66fd88b7
- clm_dd474559cc1d15c08df413021d332cb343d0969decdbc7a4b075acdc105cc321
- clm_f7eb4d7b07d7e05825a646284fdfc924daa8c49db833ce69d49ae3df3a9958bb
maturity: draft
page_id: pg_665144806bba5191a12b109de19c355f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3c385797f21b5032b130c0b1abdfd33d
title: Paseru/sinew/README.md @ 13b0a2187a07
updated_at: '2026-09-14T02:29:58Z'
---

# Paseru/sinew/README.md @ 13b0a2187a07

<!-- rcw:begin owner=source:src_3c385797f21b5032b130c0b1abdfd33d block=evidence -->
- The README warns that Claude Code and Antigravity OAuth flows are technically reserved for first-party clients, so third-party use could theoretically flag accounts, though no bans have been reported; API-key or OpenRouter paths are fully sanctioned. [@claim:clm_19f6a1fe50e910915126c6e3e24154204181ea2e9ef6145d0c9aad92c6d21145]
- The clean_context tool lets the model replace its own current-turn tool results with short placeholders, keeping the placeholder visible and avoiding retroactive purges so provider prompt caching is preserved. [@claim:clm_289d9a45a935acc31f7ea62ef3ec1877634557a826d55c7c8d4b8e4603205e62]
- The glob and grep implementations sit on top of ripgrep, and web_search offers two configurable providers: paid LinkUp (API key) and free Exa via public MCP. [@claim:clm_45962e30e2d834ed077cdaf03eeea9f64a159f35a8283dc5552f757a4659eda2]
- Sinew is a desktop AI coding harness built on Tauri 2, React, Rust, Monaco, xterm, and MCP, where every tool is toggleable, descriptions are editable, and providers are pluggable. [@claim:clm_587cf0e6e55bf20beec41f13e0e9a714c7ed82f34585a61adfef17c9e6543972]
- The agent has three interaction modes: Act (single-turn loop), Goal (autonomous loop until the task finishes), and Plan (a question/answer session that only ends when the user clicks send-and-stop). [@claim:clm_6c5763b2df9b4d35ca0c7048cecf05aa9ea3a69a31d73848498206f92bbc0506]
- MCP tools are not exposed directly; only a compact server/tool catalog sits in the prompt, and load_mcp_tool lazily injects the full schema on first use, staying loaded for the conversation. [@claim:clm_6e01732b68812becd1e6bb28f9e1bd9fbb46fd3e477aa680402e35f518182a7c]
- The main agent can launch a peer-to-peer team of 2 to 8 agents with no lead; teammates coordinate through a shared task board with dependencies and messages delivered via system reminders. [@claim:clm_6fc00ef2327e15ebbfd48f04c498908366632ad35e2455ba89d95372be51d8fd]
- Sinew connects to five providers — Anthropic, OpenAI, Google, Kimi (subscription/OAuth) and OpenRouter (API key) — usable in parallel so models can be mixed per mode, sub-agent, or teammate. [@claim:clm_8b59eadc5eec9a339be46583e3e4b9d8e1658a3ce18f67817c46b8e3d2d8a1b8]
- Configured sub-agents are exposed as subagent_<id> tools; calling one runs a full turn with that sub-agent's model and prompt while the whole harness (tools, MCP, skills) stays active. [@claim:clm_8fd2b0c4e6bef439dfb5907a1f87ae3c35fead3253615990e27bcb938789fb75]
- Rollback makes every past user message clickable, showing files changed since then and offering to revert workspace changes or keep them while undoing chat history, backed by per-turn checkpoints. [@claim:clm_93d47e2b6d411086fb4cf06f4861501a94596e35ee188cecc732ad8975ef90af]
- Skills are directories with a SKILL.md, discovered from four prioritized locations (.agents/skills and .sinew/skills in workspace and home), with the .agents format aligned to the Claude Agent Skills convention. [@claim:clm_abd1d5587ab29595ba0913267d3f267f8c5ab7fb2ffc4299d2470a8982f50c61]
- The codebase is organized as a React UI (src/), a Tauri 2 shell (src-tauri/), provider-agnostic core types (sinew-core), the agent loop and tools (sinew-app), and per-provider adapter crates. [@claim:clm_b37c78a8766b5138350bc0aa7b06ac4b2019ec7e15aab7846933f215a8fba879]
- The agent's toolset includes bash/bash_input, read, glob, grep, edit_file, write_file, web_search, web_fetch, create_image, question, todo_list, clean_context, load_mcp_tool, skill, subagent tools, and team tools. [@claim:clm_da4ea9d8ba5ad2e4a5f680c6babf552b7db794af22e2d2e53c5fff0f66fd88b7]
- The todo list's full state is re-injected into the system reminder every turn so the model always sees an up-to-date version, which the README says matters most in long Goal-mode runs. [@claim:clm_dd474559cc1d15c08df413021d332cb343d0969decdbc7a4b075acdc105cc321]
- read, glob, and grep each require a mandatory limit parameter, forcing the model to declare how much output it wants to preserve context. [@claim:clm_f7eb4d7b07d7e05825a646284fdfc924daa8c49db833ce69d49ae3df3a9958bb]
<!-- rcw:end owner=source:src_3c385797f21b5032b130c0b1abdfd33d block=evidence -->

## Researcher notes

