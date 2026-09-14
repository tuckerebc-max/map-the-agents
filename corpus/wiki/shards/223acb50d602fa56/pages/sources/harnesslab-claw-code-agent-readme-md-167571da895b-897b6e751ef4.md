---
access: public
aliases: []
claim_ids:
- clm_09276ae26e1a9f6b2d425d0f21e265b2714005739d7c7b9445fa82fd1bd14ef0
- clm_1b8fd2aea85360a738384d01064ba470c340b1df8093e9d7a6ab025221652d2e
- clm_27df6666ccd0f7ebc90a4f0045db98cfa00fdfe72f60bd45da6584394ac1a0f7
- clm_3439f5afccb53b9741c278e9f1bdb7f9502888d179f34c36e4519aba28cd4445
- clm_49ed32724be8ced80e132fb169279f28b734da1360b23520722e1a067d0d9c43
- clm_5ed82571ba63f94477dfc56eae68522e232af11a454cecbd9ce985a1fd08a57c
- clm_7358ceb516d9aa7947f5561e45ab94d18041cc7739557d51cc448a20cdb28fbd
- clm_73abd09d3eae24df164486118329741a5528ebf7149116da8646032eeee4786d
- clm_7c848f1f5cfd100f5745b05a71118e1b0679739eb7b3f04b2088daa30a317b90
- clm_8fe274e968ca44742149f041559556a60c87fb6c0b0b9e87d290caed704527a3
- clm_962cc2f29218731e519f78452cdee8c4f3f3be860d05a27e87f0d95d75755310
- clm_9947e82547faea7814776546f9488279bda00d83903c189a86a8af787dfb9670
- clm_9a30e4f405acee7d4b67511af415b894718100738deb3caf02705a627adb8555
- clm_a8e0574876e0254f123f26ac2881dcc17bd6f5242d0fa0b2eb45ca7fe446f1ad
- clm_c22ee6215f0cb0c6400971b7b7c32809cfcc77d4b7e9ec8b6914905568f5449c
- clm_c500ca9edf6cdb55f280e288a1df0737c4a786b7eaa3f995694a973e39fc0592
- clm_dc501d1770064652a47c00c6461eae528180627b93237297fc124d8a9c8af849
- clm_e03b5e10507be0f910a566f32a3592499a9077984518300204f443a6abadffcf
- clm_f0d7e17aa6885eeab207b7f3d003c51102202f1a660ec26310bf6fa100c0ae40
maturity: draft
page_id: pg_3714658f6886563898d9897b6e751ef4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4d39afdf29635e9fbfa9f7b3eb7a2a1a
title: HarnessLab/claw-code-agent/README.md @ 167571da895b
updated_at: '2026-09-14T01:53:14Z'
---

# HarnessLab/claw-code-agent/README.md @ 167571da895b

<!-- rcw:begin owner=source:src_4d39afdf29635e9fbfa9f7b3eb7a2a1a block=evidence -->
- Repository development practice: the README instructs running the full test suite with 'python3 -m unittest discover -s tests -v', and points to TESTING_GUIDE.md for step-by-step feature verification commands. [@claim:clm_09276ae26e1a9f6b2d425d0f21e265b2714005739d7c7b9445fa82fd1bd14ef0]
- The runtime targets OpenAI-compatible chat-completions endpoints, so it can run against vLLM, Ollama, LiteLLM Proxy, or OpenRouter, configured via OPENAI_BASE_URL, OPENAI_API_KEY, and OPENAI_MODEL environment variables. [@claim:clm_1b8fd2aea85360a738384d01064ba470c340b1df8093e9d7a6ab025221652d2e]
- No evidence in the provided slices describes benchmark or success-rate evaluation of the agent's task performance; the testing material shown covers manual verification commands and a unit-test suite, so evaluation capability appears undocumented here. [@claim:clm_27df6666ccd0f7ebc90a4f0045db98cfa00fdfe72f60bd45da6584394ac1a0f7]
- The runtime journals file edits with snapshot IDs and replays summaries on session resume, and performs context reduction via auto-snip, auto-compact, and reactive compaction on prompt-too-long errors. [@claim:clm_3439f5afccb53b9741c278e9f1bdb7f9502888d179f34c36e4519aba28cd4445]
- The project is a Python reimplementation of the Claude Code npm agent architecture, intended to run with local open-source models via an OpenAI-compatible API server, and is marked alpha status. [@claim:clm_49ed32724be8ced80e132fb169279f28b734da1360b23520722e1a067d0d9c43]
- The runtime uses a tiered permission system: read-only tools run by default, file writes require --allow-write, shell execution requires --allow-shell, and destructive shell operations require --unsafe. [@claim:clm_5ed82571ba63f94477dfc56eae68522e232af11a454cecbd9ce985a1fd08a57c]
- CLI flags include --cwd, --model, --base-url, --allow-write, --allow-shell, --unsafe, --stream, --show-transcript, system-prompt override/append flags, and --add-dir for extra context directories. [@claim:clm_7358ceb516d9aa7947f5561e45ab94d18041cc7739557d51cc448a20cdb28fbd]
- Slash commands are handled locally before the model loop and include /help, /context, /token-budget, /mcp, /search, /remote, /account, /config, /plan, and /tasks, some with aliases. [@claim:clm_73abd09d3eae24df164486118329741a5528ebf7149116da8646032eeee4786d]
- The core agent runtime claims zero external dependencies, using only Python's standard library, and requires Python 3.10 or higher. [@claim:clm_7c848f1f5cfd100f5745b05a71118e1b0679739eb7b3f04b2088daa30a317b90]
- Using the OpenRouter backend sends conversation content, including file contents and shell output, to OpenRouter and upstream providers, so the docs warn against using it with repos containing secrets. [@claim:clm_8fe274e968ca44742149f041559556a60c87fb6c0b0b9e87d290caed704527a3]
- Each agent run automatically saves a resumable session under .port_sessions/agent, and agent-resume or agent-chat --resume-session-id continues from the saved transcript when run from the same directory. [@claim:clm_962cc2f29218731e519f78452cdee8c4f3f3be860d05a27e87f0d95d75755310]
- A local browser GUI launched via python -m src.gui serves a dark-themed chat UI at 127.0.0.1:8765 by default, with sessions sidebar, slash-command palette, live settings, budget editing, and a Tasks tab backed by .port_sessions/task_runtime.json. [@claim:clm_9947e82547faea7814776546f9488279bda00d83903c189a86a8af787dfb9670]
- The agent supports nested delegation of subtasks to child agents with sequential and parallel execution, dependency-aware topological batching, child-session save/resume, and lineage tracking via an agent manager. [@claim:clm_9a30e4f405acee7d4b67511af415b894718100738deb3caf02705a627adb8555]
- The README lists in-progress work including full MCP parity beyond stdio transport, full slash-command and REPL/TUI parity, hooks parity, real remote transport, voice/VIM modes, and editor integrations. [@claim:clm_a8e0574876e0254f123f26ac2881dcc17bd6f5242d0fa0b2eb45ca7fe446f1ad]
- Custom agent profiles are markdown files discovered from ./.claude/agents and ~/./.claude/agents, with project agents overriding user agents and user agents overriding built-ins on matching agent_type. [@claim:clm_c22ee6215f0cb0c6400971b7b7c32809cfcc77d4b7e9ec8b6914905568f5449c]
- The bundled web GUI uses FastAPI and Uvicorn, which are installed automatically when the package is installed via pip; the core runtime itself remains dependency-free. [@claim:clm_c500ca9edf6cdb55f280e288a1df0737c4a786b7eaa3f995694a973e39fc0592]
- The CLI exposes commands such as agent, agent-chat, agent-bg/agent-ps/agent-logs/agent-kill for background sessions, agent-resume, agent-prompt, token-budget, and agents-create/update/delete, plus utility commands like summary, manifest, commands, and tools. [@claim:clm_dc501d1770064652a47c00c6461eae528180627b93237297fc124d8a9c8af849]
- The src/ tree includes modules for the agent loop (agent_runtime.py), tool execution (agent_tools.py), prompt assembly (agent_prompting.py), context building, session state, slash commands, nested-agent management, an OpenAI-compatible streaming client, and plugin runtime. [@claim:clm_e03b5e10507be0f910a566f32a3592499a9077984518300204f443a6abadffcf]
- Built-in tools include list_dir, read_file, write_file, edit_file, glob_search, grep_search, bash, web_fetch, web_search, tool_search, sleep, config/account/remote/MCP tools, and plan tools, each with a documented permission level. [@claim:clm_f0d7e17aa6885eeab207b7f3d003c51102202f1a660ec26310bf6fa100c0ae40]
<!-- rcw:end owner=source:src_4d39afdf29635e9fbfa9f7b3eb7a2a1a block=evidence -->

## Researcher notes

