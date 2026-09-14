# icebear0828/clio -- full detail

[Back to orientation](clio.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/icebear0828/clio/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/8da84aac3b00a168.json](../../../wiki/dossiers/icebear0828/clio/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/8da84aac3b00a168.json)

## specifications (1 claim(s))

- [observation/documented] Clio is a feature-rich terminal Claude Code clone connecting to the Anthropic API or compatible endpoints, providing an interactive agentic coding assistant with local tool execution. -- evidence: [README.md#L5-L5](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L5-L5) (`clm_4207b564eeaf373f2cd8eaa82d0b75a00b0ef0b05aa47c204b60ca0c328c4b76`)

## components (2 claim(s))

- [observation/documented] The tool set includes 21 tools spanning Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch, Agent, task tracking tools, Skill, ToolSearch, team tools, and SendMessage, categorized as safe, write, or dangerous. -- evidence: [README.md#L36-L66](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L36-L66), [README.md#L188-L210](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L188-L210) (`clm_2c04da05f6c5df5e4fac3e4d21f828010b8f42bd8f6bc81cfb4ef87e135017bd`)
- [inference/documented] The codebase appears organized into core engine modules (agent loop, streaming client, permissions, sandbox, session, settings) and a tools layer including checkpoint, hooks, MCP, LSP, subagent, tasks, teams, and worktree files. -- evidence: [README_zh.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README_zh.md#L313-L367), [README.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L313-L367) (`clm_16bec364e7e037352e659ca34bc3aa2e5918d6cd68606fef919f5cb3274a7d7c`)

## design-choices (3 claim(s))

- [observation/documented] Settings use a four-level hierarchy (global and project, each with committed and gitignored local files) where arrays concatenate across layers and scalars override. -- evidence: [README.md#L102-L102](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L102-L102), [README.md#L135-L135](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L135-L135), [README.md#L104-L109](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L104-L109) (`clm_bfa9d1f55e6588b2fb0cc2cfde93d1e2db98493769e1e5d5d9f1825e1ea3c441`)
- [observation/documented] Hooks run shell commands before or after tool execution; a non-zero pre-hook exit blocks the tool while post-hook failures only log a warning, with CLIO_TOOL_NAME, CLIO_TOOL_INPUT, and CLIO_HOOK_PHASE environment variables. -- evidence: [README.md#L273-L276](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L273-L276), [README.md#L258-L258](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L258-L258) (`clm_5deb774308069090023fb0d878f269bab66dbecb12040eaaea06511eb2ed9d3e`)
- [observation/documented] The system prompt auto-loads CLAUDE.md files via upward directory traversal plus git branch/status/commit context, and prompt caching via cache_control is claimed to save about 90% of input tokens. -- evidence: [README.md#L36-L66](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L36-L66) (`clm_49f68e04d3bcf9bcd053b1ed6d0e6d371401c99cda1b5086db98b1cdb1b0dc4f`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: CLAUDE.md instructs contributors to run npm run dev/build/test (vitest), keep TypeScript strict with no any, use ESM .js import extensions, and add tests per module. -- evidence: [CLAUDE.md#L148-L153](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L148-L153), [CLAUDE.md#L7-L13](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L7-L13), [CLAUDE.md#L138-L141](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L138-L141), [CLAUDE.md#L95-L99](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L95-L99) (`clm_f14ae4102753168e6be3ecb5af255f53bc439c3851cfa706783c60d7b1ee159b`)
- [observation/documented] Repository development practice: the project is intended for self-modification by Clio (dogfooding), with .clio/settings.json hooks running tsc and test gates after edits and writes, and a 3-strike rollback rule. -- evidence: [CLAUDE.md#L106-L107](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L106-L107), [CLAUDE.md#L117-L120](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L117-L120), [CLAUDE.md#L103-L103](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L103-L103) (`clm_6b52e39c7a437d1c026f0486fe732f30933c74b9d27a8085c26ac857e4962295`)
- [observation/documented] Repository development practice: autonomous git workflow requires feature branches and PRs (never pushing directly to master), conventional commits, and a self-review sub-agent that approves or requests changes via gh. -- evidence: [CLAUDE.md#L135-L135](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L135-L135), [CLAUDE.md#L123-L133](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/CLAUDE.md#L123-L133) (`clm_40269df1a87035cb15ce359a2152659fe937197ff90cb229dfbcb93506620f2e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes flags including --api-url, --api-key, --api-format (anthropic|openai), --model, --resume, --fork-session, --thinking, --permission-mode, --allow/--deny patterns, --allow-outside-cwd, and --dangerously-skip-permissions. -- evidence: [README.md#L72-L87](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L72-L87) (`clm_8e7468765b6b9829a0d5a2b53081fe43f3023950049b678848ace93682b95c1e`)
- [observation/documented] The REPL provides 17 slash commands such as /commit, /pr, /review, /compact, /context, /cost, /doctor, /init, /model, /sessions, /settings, and /theme. -- evidence: [README.md#L139-L157](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L139-L157), [README.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L313-L367) (`clm_03c1b857b0e7d65ad731b02ba59df5e43765b8f0b706edb98383c1d9178e7d81`)
- [observation/documented] The CLI supports OpenAI-compatible endpoints and custom gateways via --api-format openai and --api-url, in addition to the default direct Anthropic API connection. -- evidence: [README_zh.md#L286-L286](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README_zh.md#L286-L286), [README.md#L286-L286](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L286-L286), [README.md#L289-L289](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L289-L289) (`clm_c4038043727826f38921c5c9d1a95897b36834567bd72e748d4bd32b816ed702`)

## memory-state (1 claim(s))

- [observation/documented] Conversations auto-save to ~/.clio/sessions/{id}.json after each turn and can be resumed with --resume or forked with --fork-session. -- evidence: [README.md#L305-L305](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L305-L305), [README.md#L298-L298](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L298-L298), [README.md#L308-L309](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L308-L309) (`clm_21032f2b4b2e959e961de0e5faebdc525db6258352775c4924aec217ca033a74`)

## orchestration (3 claim(s))

- [observation/documented] Custom agents are defined in .clio/agents/*.md with front-matter specifying tools, model, and max_iterations, and are invoked via the Agent tool with a subagent_type parameter. -- evidence: [README.md#L224-L224](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L224-L224), [README.md#L226-L232](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L226-L232), [README.md#L237-L237](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L237-L237) (`clm_5ea6614f60246abb509e0b60c2f1fc822c18160183cc4623539cc4303cf01404`)
- [observation/documented] MCP servers are configured in settings.json, communicate over JSON-RPC 2.0 via stdio, and their tools are auto-discovered at startup with an mcp__<server>__<tool> prefix. -- evidence: [README.md#L243-L252](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L243-L252), [README.md#L241-L241](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L241-L241), [README.md#L254-L254](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L254-L254) (`clm_771d0f5f429c7524b6326d38784d8ca6426e1e8b74cd1137c6f9402e3a8aa8f6`)
- [observation/documented] Sub-agents support background execution via run_in_background with completion notifications, and can run in isolated git worktrees; agent teams enable messaging between agents. -- evidence: [README.md#L36-L66](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L36-L66), [README_zh.md#L36-L66](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README_zh.md#L36-L66) (`clm_8b6f93f49c114a273f30f2627ebfe11f893c80e1e067b8fc94f1eab70c8754b1`)

## tools-permissions (2 claim(s))

- [observation/documented] The runtime permission model has three modes: default (safe tools auto-allowed, dangerous/write prompt Y/n/a), auto (all allowed with deny rules), and plan (dangerous/write silently denied), cycled with Shift+Tab. -- evidence: [README.md#L212-L215](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L212-L215) (`clm_d3aa84c2ebaf3b2507135a428f264b653642958c2b6f5a891e62e1b97ca29a7d`)
- [observation/documented] Bash command allow/deny rules use glob patterns, configurable via --allow/--deny flags or settings allowRules/denyRules, and a two-stage auto classifier combines pattern matching with an LLM (Haiku). -- evidence: [README.md#L217-L220](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L217-L220), [README.md#L313-L367](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L313-L367), [README.md#L113-L133](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L113-L133) (`clm_c46b75261ff414c073a34eb0cfb4253abec72733a41903b666434b02a175524e`)

## evaluation (1 claim(s))

- [observation/documented] A benchmark report compares Clio against Claude Code on latency, token usage, cache efficiency, and correctness across five task types. -- evidence: [README.md#L371-L371](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L371-L371) (`clm_3cf1b6a36fa7c3e7d829af6daa5c5d69fad56f6ed450a72a3a1cb905ddd062e6`)

## dependencies (1 claim(s))

- [observation/documented] The project has 46 source files of roughly 9200 lines of TypeScript, with zero external runtime dependencies besides fast-glob. -- evidence: [README.md#L7-L7](https://github.com/icebear0828/clio/blob/e3f5864678d1f2e62283d8a459fd340f67dbdfe9/README.md#L7-L7) (`clm_bd2df90e4b0bee877f3b4587fa36c417a1d09d6820a8d89023e9901a23092a4c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

