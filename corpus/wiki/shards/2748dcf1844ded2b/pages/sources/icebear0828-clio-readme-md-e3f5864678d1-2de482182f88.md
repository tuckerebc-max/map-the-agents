---
access: public
aliases: []
claim_ids:
- clm_03c1b857b0e7d65ad731b02ba59df5e43765b8f0b706edb98383c1d9178e7d81
- clm_16bec364e7e037352e659ca34bc3aa2e5918d6cd68606fef919f5cb3274a7d7c
- clm_21032f2b4b2e959e961de0e5faebdc525db6258352775c4924aec217ca033a74
- clm_2c04da05f6c5df5e4fac3e4d21f828010b8f42bd8f6bc81cfb4ef87e135017bd
- clm_3cf1b6a36fa7c3e7d829af6daa5c5d69fad56f6ed450a72a3a1cb905ddd062e6
- clm_4207b564eeaf373f2cd8eaa82d0b75a00b0ef0b05aa47c204b60ca0c328c4b76
- clm_49f68e04d3bcf9bcd053b1ed6d0e6d371401c99cda1b5086db98b1cdb1b0dc4f
- clm_5deb774308069090023fb0d878f269bab66dbecb12040eaaea06511eb2ed9d3e
- clm_5ea6614f60246abb509e0b60c2f1fc822c18160183cc4623539cc4303cf01404
- clm_771d0f5f429c7524b6326d38784d8ca6426e1e8b74cd1137c6f9402e3a8aa8f6
- clm_8b6f93f49c114a273f30f2627ebfe11f893c80e1e067b8fc94f1eab70c8754b1
- clm_8e7468765b6b9829a0d5a2b53081fe43f3023950049b678848ace93682b95c1e
- clm_bd2df90e4b0bee877f3b4587fa36c417a1d09d6820a8d89023e9901a23092a4c
- clm_bfa9d1f55e6588b2fb0cc2cfde93d1e2db98493769e1e5d5d9f1825e1ea3c441
- clm_c4038043727826f38921c5c9d1a95897b36834567bd72e748d4bd32b816ed702
- clm_c46b75261ff414c073a34eb0cfb4253abec72733a41903b666434b02a175524e
- clm_d3aa84c2ebaf3b2507135a428f264b653642958c2b6f5a891e62e1b97ca29a7d
maturity: draft
page_id: pg_fa9a79fd346b57bd97f12de482182f88
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_065bc73fa81354318187ee3f451c7ec4
title: icebear0828/clio/README.md @ e3f5864678d1
updated_at: '2026-09-14T02:04:27Z'
---

# icebear0828/clio/README.md @ e3f5864678d1

<!-- rcw:begin owner=source:src_065bc73fa81354318187ee3f451c7ec4 block=evidence -->
- The REPL provides 17 slash commands such as /commit, /pr, /review, /compact, /context, /cost, /doctor, /init, /model, /sessions, /settings, and /theme. [@claim:clm_03c1b857b0e7d65ad731b02ba59df5e43765b8f0b706edb98383c1d9178e7d81]
- The codebase appears organized into core engine modules (agent loop, streaming client, permissions, sandbox, session, settings) and a tools layer including checkpoint, hooks, MCP, LSP, subagent, tasks, teams, and worktree files. [@claim:clm_16bec364e7e037352e659ca34bc3aa2e5918d6cd68606fef919f5cb3274a7d7c]
- Conversations auto-save to ~/.clio/sessions/{id}.json after each turn and can be resumed with --resume or forked with --fork-session. [@claim:clm_21032f2b4b2e959e961de0e5faebdc525db6258352775c4924aec217ca033a74]
- The tool set includes 21 tools spanning Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, Agent, task tracking tools, Skill, ToolSearch, team tools, and SendMessage, categorized as safe, write, or dangerous. [@claim:clm_2c04da05f6c5df5e4fac3e4d21f828010b8f42bd8f6bc81cfb4ef87e135017bd]
- A benchmark report compares Clio against Claude Code on latency, token usage, cache efficiency, and correctness across five task types. [@claim:clm_3cf1b6a36fa7c3e7d829af6daa5c5d69fad56f6ed450a72a3a1cb905ddd062e6]
- Clio is a feature-rich terminal Claude Code clone connecting to the Anthropic API or compatible endpoints, providing an interactive agentic coding assistant with local tool execution. [@claim:clm_4207b564eeaf373f2cd8eaa82d0b75a00b0ef0b05aa47c204b60ca0c328c4b76]
- The system prompt auto-loads CLAUDE.md files via upward directory traversal plus git branch/status/commit context, and prompt caching via cache_control is claimed to save about 90% of input tokens. [@claim:clm_49f68e04d3bcf9bcd053b1ed6d0e6d371401c99cda1b5086db98b1cdb1b0dc4f]
- Hooks run shell commands before or after tool execution; a non-zero pre-hook exit blocks the tool while post-hook failures only log a warning, with CLIO_TOOL_NAME, CLIO_TOOL_INPUT, and CLIO_HOOK_PHASE environment variables. [@claim:clm_5deb774308069090023fb0d878f269bab66dbecb12040eaaea06511eb2ed9d3e]
- Custom agents are defined in .clio/agents/*.md with front-matter specifying tools, model, and max_iterations, and are invoked via the Agent tool with a subagent_type parameter. [@claim:clm_5ea6614f60246abb509e0b60c2f1fc822c18160183cc4623539cc4303cf01404]
- MCP servers are configured in settings.json, communicate over JSON-RPC 2.0 via stdio, and their tools are auto-discovered at startup with an mcp__<server>__<tool> prefix. [@claim:clm_771d0f5f429c7524b6326d38784d8ca6426e1e8b74cd1137c6f9402e3a8aa8f6]
- Sub-agents support background execution via run_in_background with completion notifications, and can run in isolated git worktrees; agent teams enable messaging between agents. [@claim:clm_8b6f93f49c114a273f30f2627ebfe11f893c80e1e067b8fc94f1eab70c8754b1]
- The CLI exposes flags including --api-url, --api-key, --api-format (anthropic|openai), --model, --resume, --fork-session, --thinking, --permission-mode, --allow/--deny patterns, --allow-outside-cwd, and --dangerously-skip-permissions. [@claim:clm_8e7468765b6b9829a0d5a2b53081fe43f3023950049b678848ace93682b95c1e]
- The project has 46 source files of roughly 9200 lines of TypeScript, with zero external runtime dependencies besides fast-glob. [@claim:clm_bd2df90e4b0bee877f3b4587fa36c417a1d09d6820a8d89023e9901a23092a4c]
- Settings use a four-level hierarchy (global and project, each with committed and gitignored local files) where arrays concatenate across layers and scalars override. [@claim:clm_bfa9d1f55e6588b2fb0cc2cfde93d1e2db98493769e1e5d5d9f1825e1ea3c441]
- The CLI supports OpenAI-compatible endpoints and custom gateways via --api-format openai and --api-url, in addition to the default direct Anthropic API connection. [@claim:clm_c4038043727826f38921c5c9d1a95897b36834567bd72e748d4bd32b816ed702]
- Bash command allow/deny rules use glob patterns, configurable via --allow/--deny flags or settings allowRules/denyRules, and a two-stage auto classifier combines pattern matching with an LLM (Haiku). [@claim:clm_c46b75261ff414c073a34eb0cfb4253abec72733a41903b666434b02a175524e]
- The runtime permission model has three modes: default (safe tools auto-allowed, dangerous/write prompt Y/n/a), auto (all allowed with deny rules), and plan (dangerous/write silently denied), cycled with Shift+Tab. [@claim:clm_d3aa84c2ebaf3b2507135a428f264b653642958c2b6f5a891e62e1b97ca29a7d]
<!-- rcw:end owner=source:src_065bc73fa81354318187ee3f451c7ec4 block=evidence -->

## Researcher notes

