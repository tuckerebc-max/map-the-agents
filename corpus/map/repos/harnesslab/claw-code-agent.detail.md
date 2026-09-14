# harnesslab/claw-code-agent -- full detail

[Back to orientation](claw-code-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/harnesslab/claw-code-agent/167571da895b2a1a9e36ecfae2876984cef65e0d/76b0b0a684f15cec.json](../../../wiki/dossiers/harnesslab/claw-code-agent/167571da895b2a1a9e36ecfae2876984cef65e0d/76b0b0a684f15cec.json)

## specifications (1 claim(s))

- [observation/documented] The project is a Python reimplementation of the Claude Code npm agent architecture, intended to run with local open-source models via an OpenAI-compatible API server, and is marked alpha status. -- evidence: [README.md#L91-L91](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L91-L91), [README.md#L11-L19](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L11-L19), [README.md#L7-L9](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L7-L9) (`clm_49ed32724be8ced80e132fb169279f28b734da1360b23520722e1a067d0d9c43`)

## components (1 claim(s))

- [observation/documented] The src/ tree includes modules for the agent loop (agent_runtime.py), tool execution (agent_tools.py), prompt assembly (agent_prompting.py), context building, session state, slash commands, nested-agent management, an OpenAI-compatible streaming client, and plugin runtime. -- evidence: [README.md#L223-L287](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L223-L287) (`clm_e03b5e10507be0f910a566f32a3592499a9077984518300204f443a6abadffcf`)

## design-choices (2 claim(s))

- [observation/documented] Custom agent profiles are markdown files discovered from ./.claude/agents and ~/./.claude/agents, with project agents overriding user agents and user agents overriding built-ins on matching agent_type. -- evidence: [README.md#L607-L607](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L607-L607), [README.md#L602-L602](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L602-L602), [README.md#L604-L605](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L604-L605) (`clm_c22ee6215f0cb0c6400971b7b7c32809cfcc77d4b7e9ec8b6914905568f5449c`)
- [observation/documented] The runtime targets OpenAI-compatible chat-completions endpoints, so it can run against vLLM, Ollama, LiteLLM Proxy, or OpenRouter, configured via OPENAI_BASE_URL, OPENAI_API_KEY, and OPENAI_MODEL environment variables. -- evidence: [README.md#L402-L406](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L402-L406), [README.md#L381-L381](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L381-L381), [README.md#L327-L327](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L327-L327), [README.md#L354-L354](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L354-L354) (`clm_1b8fd2aea85360a738384d01064ba470c340b1df8093e9d7a6ab025221652d2e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README instructs running the full test suite with 'python3 -m unittest discover -s tests -v', and points to TESTING_GUIDE.md for step-by-step feature verification commands. -- evidence: [README.md#L857-L859](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L857-L859), [README.md#L855-L855](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L855-L855), [README.md#L871-L871](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L871-L871) (`clm_09276ae26e1a9f6b2d425d0f21e265b2714005739d7c7b9445fa82fd1bd14ef0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI exposes commands such as agent, agent-chat, agent-bg/agent-ps/agent-logs/agent-kill for background sessions, agent-resume, agent-prompt, token-budget, and agents-create/update/delete, plus utility commands like summary, manifest, commands, and tools. -- evidence: [README.md#L469-L487](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L469-L487), [README.md#L660-L665](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L660-L665) (`clm_dc501d1770064652a47c00c6461eae528180627b93237297fc124d8a9c8af849`)
- [observation/documented] Slash commands are handled locally before the model loop and include /help, /context, /token-budget, /mcp, /search, /remote, /account, /config, /plan, and /tasks, some with aliases. -- evidence: [README.md#L553-L553](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L553-L553), [README.md#L555-L589](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L555-L589) (`clm_73abd09d3eae24df164486118329741a5528ebf7149116da8646032eeee4786d`)
- [observation/documented] CLI flags include --cwd, --model, --base-url, --allow-write, --allow-shell, --unsafe, --stream, --show-transcript, system-prompt override/append flags, and --add-dir for extra context directories. -- evidence: [README.md#L502-L516](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L502-L516) (`clm_7358ceb516d9aa7947f5561e45ab94d18041cc7739557d51cc448a20cdb28fbd`)
- [observation/documented] A local browser GUI launched via python -m src.gui serves a dark-themed chat UI at 127.0.0.1:8765 by default, with sessions sidebar, slash-command palette, live settings, budget editing, and a Tasks tab backed by .port_sessions/task_runtime.json. -- evidence: [README.md#L752-L752](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L752-L752), [README.md#L791-L791](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L791-L791), [README.md#L748-L750](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L748-L750), [README.md#L795-L802](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L795-L802) (`clm_9947e82547faea7814776546f9488279bda00d83903c189a86a8af787dfb9670`)

## memory-state (2 claim(s))

- [observation/documented] Each agent run automatically saves a resumable session under .port_sessions/agent, and agent-resume or agent-chat --resume-session-id continues from the saved transcript when run from the same directory. -- evidence: [README.md#L837-L841](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L837-L841), [README.md#L820-L820](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L820-L820), [README.md#L829-L833](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L829-L833), [README.md#L849-L849](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L849-L849) (`clm_962cc2f29218731e519f78452cdee8c4f3f3be860d05a27e87f0d95d75755310`)
- [observation/documented] The runtime journals file edits with snapshot IDs and replays summaries on session resume, and performs context reduction via auto-snip, auto-compact, and reactive compaction on prompt-too-long errors. -- evidence: [README.md#L156-L205](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L156-L205), [README.md#L27-L85](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L27-L85) (`clm_3439f5afccb53b9741c278e9f1bdb7f9502888d179f34c36e4519aba28cd4445`)

## orchestration (1 claim(s))

- [observation/documented] The agent supports nested delegation of subtasks to child agents with sequential and parallel execution, dependency-aware topological batching, child-session save/resume, and lineage tracking via an agent manager. -- evidence: [README.md#L734-L738](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L734-L738), [README.md#L726-L726](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L726-L726) (`clm_9a30e4f405acee7d4b67511af415b894718100738deb3caf02705a627adb8555`)

## tools-permissions (2 claim(s))

- [observation/documented] The runtime uses a tiered permission system: read-only tools run by default, file writes require --allow-write, shell execution requires --allow-shell, and destructive shell operations require --unsafe. -- evidence: [README.md#L879-L884](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L879-L884), [README.md#L877-L877](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L877-L877) (`clm_5ed82571ba63f94477dfc56eae68522e232af11a454cecbd9ce985a1fd08a57c`)
- [observation/documented] Built-in tools include list_dir, read_file, write_file, edit_file, glob_search, grep_search, bash, web_fetch, web_search, tool_search, sleep, config/account/remote/MCP tools, and plan tools, each with a documented permission level. -- evidence: [README.md#L671-L671](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L671-L671), [README.md#L673-L692](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L673-L692) (`clm_f0d7e17aa6885eeab207b7f3d003c51102202f1a660ec26310bf6fa100c0ae40`)

## evaluation (1 claim(s))

- [inference/documented] No evidence in the provided slices describes benchmark or success-rate evaluation of the agent's task performance; the testing material shown covers manual verification commands and a unit-test suite, so evaluation capability appears undocumented here. -- evidence: [README.md#L149-L152](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L149-L152), [README.md#L855-L855](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L855-L855), [README.md#L871-L871](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L871-L871) (`clm_27df6666ccd0f7ebc90a4f0045db98cfa00fdfe72f60bd45da6584394ac1a0f7`)

## dependencies (2 claim(s))

- [observation/documented] The core agent runtime claims zero external dependencies, using only Python's standard library, and requires Python 3.10 or higher. -- evidence: [README.md#L95-L97](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L95-L97), [README.md#L293-L298](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L293-L298) (`clm_7c848f1f5cfd100f5745b05a71118e1b0679739eb7b3f04b2088daa30a317b90`)
- [observation/documented] The bundled web GUI uses FastAPI and Uvicorn, which are installed automatically when the package is installed via pip; the core runtime itself remains dependency-free. -- evidence: [README.md#L814-L814](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L814-L814) (`clm_c500ca9edf6cdb55f280e288a1df0737c4a786b7eaa3f995694a973e39fc0592`)

## limitations (3 claim(s))

- [observation/documented] The README lists in-progress work including full MCP parity beyond stdio transport, full slash-command and REPL/TUI parity, hooks parity, real remote transport, voice/VIM modes, and editor integrations. -- evidence: [README.md#L209-L217](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L209-L217) (`clm_a8e0574876e0254f123f26ac2881dcc17bd6f5242d0fa0b2eb45ca7fe446f1ad`)
- [observation/documented] The parity checklist states that large parts of the mirrored Python workspace still act as inventory or scaffolding, with the working runtime concentrated in a subset of src modules. -- evidence: [PARITY_CHECKLIST.md#L5-L5](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/PARITY_CHECKLIST.md#L5-L5) (`clm_98b5a747dba0c757eab9a49ce7d7835ad715ef45cedfef9f4c8d0aed8419f91b`)
- [observation/documented] Using the OpenRouter backend sends conversation content, including file contents and shell output, to OpenRouter and upstream providers, so the docs warn against using it with repos containing secrets. -- evidence: [README.md#L393-L396](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L393-L396) (`clm_8fe274e968ca44742149f041559556a60c87fb6c0b0b9e87d290caed704527a3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

