# mistralai/mistral-vibe -- full detail

[Back to orientation](mistral-vibe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mistralai/mistral-vibe/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/da3e2ef6099117de.json](../../../wiki/dossiers/mistralai/mistral-vibe/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/da3e2ef6099117de.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Built-in tools include read, write_file, edit, grep (with ripgrep support), todo list management, ask_user_question, and task delegation; shell tools exist in a legacy one-shot bash variant and a managed variant with session, stdin, and log-file tools. -- evidence: [README.md#L95-L111](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L95-L111), [README.md#L590-L593](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L590-L593), [README.md#L579-L588](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L579-L588) (`clm_ce6cca88bfe85ad6d7aae3b72071a79425efeaac588c26030a6e2a350cb3d892`)

## design-choices (1 claim(s))

- [observation/documented] Vibe includes a trust folder system: directories containing a .vibe subfolder may prompt for trust confirmation, trusted folders are remembered in ~/.vibe/trusted_folders.toml, and AGENTS.md instructions and project-local skills load only for trusted folders. -- evidence: [README.md#L260-L260](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L260-L260), [README.md#L514-L514](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L514-L514), [README.md#L258-L258](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L258-L258), [README.md#L400-L403](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L400-L403) (`clm_c376a6061f915170f92704e0d1cd4c4cf9393e7f176f62c579ffc94110f4e3a6`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are directories with a SKILL.md using YAML frontmatter, following the Agent Skills specification; they can add tools, slash commands, and behaviors, and are discovered from config skill_paths, .agents/skills/, .vibe/skills/, and ~/.vibe/skills/. -- evidence: [README.md#L370-L370](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L370-L370), [README.md#L372-L372](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L372-L372), [README.md#L376-L376](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L376-L376), [README.md#L400-L403](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L400-L403) (`clm_c4b898a11cae93255c053cc1b6a8477d57be6ae57904ff2f217c58b61979b3b6`)

## interfaces (4 claim(s))

- [observation/documented] Mistral Vibe is a command-line coding assistant powered by Mistral's models, providing a conversational interface to explore, modify, and interact with codebases using natural language. -- evidence: [README.md#L22-L22](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L22-L22), [README.md#L20-L20](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L20-L20) (`clm_3479157b9b2836b228dd7bf7d6e30d649b1eb009c98b4a1ee1eecdd17327de27`)
- [observation/documented] The CLI offers interactive chat via `vibe`, a one-shot prompt argument, and non-interactive programmatic mode through `--prompt` or piped input for scripting. -- evidence: [README.md#L252-L254](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L252-L254), [README.md#L268-L270](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L268-L270), [README.md#L232-L232](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L232-L232), [README.md#L266-L266](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L266-L266) (`clm_d8c413536c4feff1e58772c45df404da851ca2798c164c60f450eae9b1455fb8`)
- [observation/documented] Programmatic mode accepts options including --max-turns, --max-price, --max-tokens, --agent, --auto-approve/--yolo, --enabled-tools/--disabled-tools, and --output with text, json, or streaming formats. -- evidence: [README.md#L284-L294](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L284-L294) (`clm_839eb591feec058d5b3ce4c0633c38ea5c10159e6cd492489eb6b1116be63b31`)
- [observation/documented] Vibe supports MCP server configuration under mcp_servers, with a `vibe mcp add` command supporting streamable-http transport, static auth via --api-key-env or --header, and OAuth browser login by default otherwise. -- evidence: [README.md#L648-L652](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L648-L652), [README.md#L644-L646](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L644-L646), [README.md#L642-L642](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L642-L642) (`clm_be58a10711a10a10e3225be11b34fd73012a878ca04c7c179deae9327a320f11`)

## memory-state (1 claim(s))

- [observation/documented] Compaction uses a built-in prompt at prompts/compact.md by default, keeps the same session and visible conversation, and later model requests use the compacted context followed by newer messages; custom compaction prompts are supported. -- evidence: [README.md#L531-L531](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L531-L531), [README.md#L542-L543](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L542-L543) (`clm_c65253ae44b97c2ebbf5f644461470016f5fdb54061efa16444e40a9e85ca89e`)

## orchestration (1 claim(s))

- [observation/documented] A `task` tool delegates work to subagents that run independently without user interaction; a built-in read-only `explore` subagent exists, and custom subagents are defined with agent_type = "subagent". -- evidence: [README.md#L146-L146](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L146-L146), [README.md#L158-L158](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L158-L158), [README.md#L148-L148](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L148-L148) (`clm_1963e688c519f838ccd8b9345dd33cb6bb414d3d1a2c5fc42dc5da8390f78a5e`)

## tools-permissions (2 claim(s))

- [observation/documented] Vibe ships built-in agent profiles governing tool approval: ask (approval required), plan (read-only, auto-approves safe tools), accept-edits (default, auto-approves file edits), and auto-approve (approves all tool executions). -- evidence: [README.md#L117-L120](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L117-L120) (`clm_b260c0ae2c87d6ed6699f8d67ad4bd780c857f156edacc1c832de0e4ba5749f8`)
- [observation/documented] Tool availability is configurable via enabled_tools and disabled_tools, supporting exact names, glob patterns, and regex (re: prefix); enabled_tools narrows the set first, then disabled_tools removes matching tools. -- evidence: [README.md#L637-L638](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L637-L638), [README.md#L617-L620](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L617-L620), [README.md#L629-L629](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L629-L629) (`clm_7136e8f77fcbfe620394b78fd3dd98b77d9aee993a6ee5973b10105280f810ba`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is published on PyPI as mistral-vibe and targets Python 3.12+; installation is via a curl install script, `uv tool install mistral-vibe`, or pip. -- evidence: [README.md#L53-L55](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L53-L55), [README.md#L47-L49](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L47-L49), [README.md#L31-L33](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L31-L33), [README.md#L3-L6](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L3-L6) (`clm_c829feb7add145ddefa07733195838ef9a32c93d5391eee4c95f2cd79ac6785c`)

## limitations (1 claim(s))

- [observation/documented] Voice mode is documented as experimental and may change in future releases; it is toggled with the /voice slash command and recording starts via Ctrl+R. -- evidence: [README.md#L319-L324](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L319-L324), [README.md#L304-L305](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L304-L305), [README.md#L311-L311](https://github.com/mistralai/mistral-vibe/blob/d4b3223bbd74f83cbc08da4b9c3776c8ad196955/README.md#L311-L311) (`clm_9b4c72e1fbce1338457beebcbcf0686cf10c4a41199a1f7bdfe2d019976334d6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

