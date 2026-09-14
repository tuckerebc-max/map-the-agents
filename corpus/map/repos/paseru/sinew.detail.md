# paseru/sinew -- full detail

[Back to orientation](sinew.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/paseru/sinew/13b0a2187a078affc4089638db742a3d776795ba/8eac9848b44c0207.json](../../../wiki/dossiers/paseru/sinew/13b0a2187a078affc4089638db742a3d776795ba/8eac9848b44c0207.json)

## specifications (1 claim(s))

- [observation/documented] Sinew is a desktop AI coding harness built on Tauri 2, React, Rust, Monaco, xterm, and MCP, where every tool is toggleable, descriptions are editable, and providers are pluggable. -- evidence: [README.md#L19-L21](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L19-L21), [README.md#L13-L17](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L13-L17) (`clm_587cf0e6e55bf20beec41f13e0e9a714c7ed82f34585a61adfef17c9e6543972`)

## components (1 claim(s))

- [observation/documented] The codebase is organized as a React UI (src/), a Tauri 2 shell (src-tauri/), provider-agnostic core types (sinew-core), the agent loop and tools (sinew-app), and per-provider adapter crates. -- evidence: [README.md#L536-L540](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L536-L540) (`clm_b37c78a8766b5138350bc0aa7b06ac4b2019ec7e15aab7846933f215a8fba879`)

## design-choices (3 claim(s))

- [observation/documented] read, glob, and grep each require a mandatory limit parameter, forcing the model to declare how much output it wants to preserve context. -- evidence: [README.md#L256-L256](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L256-L256), [README.md#L208-L208](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L208-L208), [README.md#L233-L233](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L233-L233) (`clm_f7eb4d7b07d7e05825a646284fdfc924daa8c49db833ce69d49ae3df3a9958bb`)
- [observation/documented] The clean_context tool lets the model replace its own current-turn tool results with short placeholders, keeping the placeholder visible and avoiding retroactive purges so provider prompt caching is preserved. -- evidence: [README.md#L169-L169](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L169-L169), [README.md#L178-L178](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L178-L178), [README.md#L175-L176](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L175-L176) (`clm_289d9a45a935acc31f7ea62ef3ec1877634557a826d55c7c8d4b8e4603205e62`)
- [observation/documented] MCP tools are not exposed directly; only a compact server/tool catalog sits in the prompt, and load_mcp_tool lazily injects the full schema on first use, staying loaded for the conversation. -- evidence: [README.md#L386-L386](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L386-L386), [README.md#L382-L382](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L382-L382), [README.md#L371-L371](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L371-L371) (`clm_6e01732b68812becd1e6bb28f9e1bd9fbb46fd3e477aa680402e35f518182a7c`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are directories with a SKILL.md, discovered from four prioritized locations (.agents/skills and .sinew/skills in workspace and home), with the .agents format aligned to the Claude Agent Skills convention. -- evidence: [README.md#L415-L415](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L415-L415), [README.md#L396-L402](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L396-L402), [README.md#L408-L411](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L408-L411), [README.md#L413-L413](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L413-L413) (`clm_abd1d5587ab29595ba0913267d3f267f8c5ab7fb2ffc4299d2470a8982f50c61`)

## interfaces (3 claim(s))

- [observation/documented] The agent has three interaction modes: Act (single-turn loop), Goal (autonomous loop until the task finishes), and Plan (a question/answer session that only ends when the user clicks send-and-stop). -- evidence: [README.md#L68-L68](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L68-L68), [README.md#L72-L72](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L72-L72), [README.md#L76-L76](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L76-L76) (`clm_6c5763b2df9b4d35ca0c7048cecf05aa9ea3a69a31d73848498206f92bbc0506`)
- [observation/documented] The agent's toolset includes bash/bash_input, read, glob, grep, edit_file, write_file, web_search, web_fetch, create_image, question, todo_list, clean_context, load_mcp_tool, skill, subagent tools, and team tools. -- evidence: [README.md#L134-L155](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L134-L155) (`clm_da4ea9d8ba5ad2e4a5f680c6babf552b7db794af22e2d2e53c5fff0f66fd88b7`)
- [observation/documented] Rollback makes every past user message clickable, showing files changed since then and offering to revert workspace changes or keep them while undoing chat history, backed by per-turn checkpoints. -- evidence: [README.md#L517-L517](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L517-L517), [README.md#L526-L526](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L526-L526), [README.md#L521-L522](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L521-L522) (`clm_93d47e2b6d411086fb4cf06f4861501a94596e35ee188cecc732ad8975ef90af`)

## memory-state (1 claim(s))

- [observation/documented] The todo list's full state is re-injected into the system reminder every turn so the model always sees an up-to-date version, which the README says matters most in long Goal-mode runs. -- evidence: [README.md#L363-L363](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L363-L363) (`clm_dd474559cc1d15c08df413021d332cb343d0969decdbc7a4b075acdc105cc321`)

## orchestration (2 claim(s))

- [observation/documented] The main agent can launch a peer-to-peer team of 2 to 8 agents with no lead; teammates coordinate through a shared task board with dependencies and messages delivered via system reminders. -- evidence: [README.md#L440-L440](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L440-L440), [README.md#L497-L501](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L497-L501), [README.md#L493-L493](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L493-L493), [README.md#L456-L457](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L456-L457) (`clm_6fc00ef2327e15ebbfd48f04c498908366632ad35e2455ba89d95372be51d8fd`)
- [observation/documented] Configured sub-agents are exposed as subagent_<id> tools; calling one runs a full turn with that sub-agent's model and prompt while the whole harness (tools, MCP, skills) stays active. -- evidence: [README.md#L425-L425](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L425-L425), [README.md#L423-L423](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L423-L423) (`clm_8fd2b0c4e6bef439dfb5907a1f87ae3c35fead3253615990e27bcb938789fb75`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The glob and grep implementations sit on top of ripgrep, and web_search offers two configurable providers: paid LinkUp (API key) and free Exa via public MCP. -- evidence: [README.md#L258-L258](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L258-L258), [README.md#L331-L331](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L331-L331), [README.md#L235-L235](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L235-L235), [README.md#L327-L327](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L327-L327), [README.md#L329-L329](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L329-L329) (`clm_45962e30e2d834ed077cdaf03eeea9f64a159f35a8283dc5552f757a4659eda2`)
- [observation/documented] Sinew connects to five providers — Anthropic, OpenAI, Google, Kimi (subscription/OAuth) and OpenRouter (API key) — usable in parallel so models can be mixed per mode, sub-agent, or teammate. -- evidence: [README.md#L104-L110](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L104-L110), [README.md#L118-L118](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L118-L118), [README.md#L124-L126](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L124-L126) (`clm_8b59eadc5eec9a339be46583e3e4b9d8e1658a3ce18f67817c46b8e3d2d8a1b8`)

## limitations (1 claim(s))

- [observation/documented] The README warns that Claude Code and Antigravity OAuth flows are technically reserved for first-party clients, so third-party use could theoretically flag accounts, though no bans have been reported; API-key or OpenRouter paths are fully sanctioned. -- evidence: [README.md#L25-L35](https://github.com/Paseru/sinew/blob/13b0a2187a078affc4089638db742a3d776795ba/README.md#L25-L35) (`clm_19f6a1fe50e910915126c6e3e24154204181ea2e9ef6145d0c9aad92c6d21145`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

