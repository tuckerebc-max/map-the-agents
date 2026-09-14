# codeany-ai/codeany -- full detail

[Back to orientation](codeany.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codeany-ai/codeany/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/c133a7afd77dd2c7.json](../../../wiki/dossiers/codeany-ai/codeany/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/c133a7afd77dd2c7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The internal package layout includes modules for config, permissions, memory, pipe mode, plugins, sessions, skills, slash command registry, team/mailbox, theme, TUI model/input/render, version, and git worktree isolation. -- evidence: [CODEANY.md#L16-L37](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L16-L37) (`clm_8d87254c007a6e75368aaa368883bf6a3ca167f742d6647f8238b3fda772ca95`)

## design-choices (2 claim(s))

- [observation/documented] Configuration lives in ~/.codeany/ with settings.json (model, permissions, MCP, hooks), an alternative config.yaml, persisted permissions.json, and directories for memory, sessions, skills, plugins, teams, and worktrees. -- evidence: [CODEANY.md#L41-L51](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L41-L51), [README.md#L112-L126](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L112-L126), [README.md#L110-L110](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L110-L110) (`clm_c080489a54e4ad673de5a8c7c7a47688a9842147cdaa4e02b886b266ce075fca`)
- [inference/documented] The project appears positioned as a feature-parity, fully open-source alternative to Claude Code, and even instructs contributors to compare against the original TypeScript codebase when adding features. -- evidence: [CODEANY.md#L5-L5](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L5-L5), [CODEANY.md#L78-L80](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L78-L80) (`clm_75dce6abfbee0b1567e3e9b0878d6a67b1c79b2eaff5cd7e63a1d58eed0d5b00`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors build with `make build` or `go build -o codeany ./cmd/codeany/`, run `make vet`, cross-compile six platforms with `make dist`, and test pipe mode via `go run ./cmd/codeany -p -y`. -- evidence: [CODEANY.md#L57-L60](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L57-L60), [CODEANY.md#L63-L65](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L63-L65) (`clm_d988da27935246e353da36ed956c4f392fe0a98a543ba4dda8cf14794b64718d`)
- [observation/documented] Repository development practice: slash commands must be registered in both AllCommands() for autocomplete and Handle() for routing, and go.work links the SDK locally while go.mod uses the published version for CI. -- evidence: [CODEANY.md#L69-L74](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L69-L74) (`clm_99b8774410b3ce7a4897fd45e8ce97d46db2396597f4a7f597f86c7584f53418`)

## skills-patterns (1 claim(s))

- [observation/documented] Custom skills are markdown files at .codeany/skills/<name>/SKILL.md with YAML frontmatter (name, description, argumentHint) whose body can reference $ARGUMENTS and be invoked as a slash command like /deploy staging. -- evidence: [README.md#L173-L178](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L173-L178), [README.md#L184-L184](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L184-L184), [README.md#L180-L182](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L180-L182), [README.md#L171-L171](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L171-L171) (`clm_947f3411ed4fc6c214d783682e66482243f522fd6f4091824bf42047dc85680a`)

## interfaces (4 claim(s))

- [observation/documented] The product is a terminal TUI agent written in Go using Bubble Tea, invoked as the `codeany` binary with interactive, initial-prompt, pipe (-p), and print (--print) modes. -- evidence: [README.md#L39-L39](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L39-L39), [README.md#L48-L48](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L48-L48), [README.md#L45-L45](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L45-L45), [README.md#L42-L42](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L42-L42), [README.md#L7-L7](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L7-L7) (`clm_132e5bcf861beba6a970a0552b42e15ce5aed5fa8475761d86032f6e4f975a71`)
- [observation/documented] The CLI supports flags including -p for pipe mode, -y to skip permission prompts, -m to select a model, and --output-format json for JSON output. -- evidence: [README.md#L57-L58](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L57-L58), [README.md#L48-L48](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L48-L48), [README.md#L45-L45](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L45-L45), [README.md#L51-L51](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L51-L51), [README.md#L54-L54](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L54-L54) (`clm_88b8f5e2f8c393f7d58ed141a6ef5e7012ba754772a28f5de94fbcdb692d6966`)
- [observation/documented] The TUI advertises 78 slash commands such as /model, /compact, /plan, /commit, /review, /mcp, /skills, /resume, and /permissions, plus keyboard shortcuts including Tab completion and `! cmd` shell execution. -- evidence: [README.md#L9-L9](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L9-L9), [README.md#L94-L106](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L94-L106), [README.md#L62-L90](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L62-L90) (`clm_e8e33caf985abce69dd7c7f834341e80e0b8a56f48832189078058838213420d`)
- [observation/documented] Project-level instructions are read from CODEANY.md or CLAUDE.md in the project root, with personal gitignored variants and modular rules under .codeany/rules/ or .claude/rules/. -- evidence: [README.md#L151-L151](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L151-L151), [README.md#L165-L167](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L165-L167) (`clm_47720c30a93db38a48640aec6eeceea2ac2350b8b0f55a06d6c4f9e2e0c6b9bf`)

## memory-state (1 claim(s))

- [observation/documented] The agent maintains memory files under ~/.codeany/memory/ (MEMORY.md plus files per the architecture doc), session history with save/restore/resume, and per-session context such as files accessed. -- evidence: [CODEANY.md#L16-L37](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L16-L37), [README.md#L112-L126](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L112-L126), [README.md#L62-L90](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L62-L90) (`clm_439e3f633817c52838301cc383057e473323fb20160a465d960e6f70c5c6e847`)

## orchestration (1 claim(s))

- [observation/documented] MCP servers are configured in settings.json (e.g. a stdio filesystem server launched via npx) and managed at runtime through /mcp subcommands to list servers and tools or reconnect a server. -- evidence: [README.md#L190-L194](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L190-L194), [README.md#L188-L188](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L188-L188), [README.md#L130-L147](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L130-L147) (`clm_1e6720e863efb3acffd93a7beebcba77f5ed74672e4e68127fb1716dfd8b9be3`)

## tools-permissions (1 claim(s))

- [observation/documented] The product has a permission model with a configurable permissionMode (e.g. "default") in settings.json, persisted permission rules in permissions.json, a /permissions command, and a -y flag to skip prompts. -- evidence: [README.md#L112-L126](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L112-L126), [README.md#L62-L90](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L62-L90), [README.md#L130-L147](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L130-L147), [README.md#L54-L54](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L54-L54) (`clm_a3c80879c56c5eb9ef0a309de19a70e1636729fe4be2d6c2e23ee6ad78cd3c1e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The agent depends on the open-agent-sdk-go SDK, which provides the agent loop, tools, MCP, permissions, hooks, and cost tracking; Codeany itself adds TUI, slash commands, skills, plugins, teams, sessions, and config management. -- evidence: [CODEANY.md#L69-L74](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/CODEANY.md#L69-L74) (`clm_bcc2ac089106d922c486721aee7f7b144af0ddcbbcc82de5e85a74214e3c3bea`)
- [observation/documented] Providers are configurable via environment variables: ANTHROPIC_API_KEY for Anthropic, or CODEANY_API_KEY, CODEANY_BASE_URL, and CODEANY_MODEL for OpenRouter or custom providers. -- evidence: [README.md#L30-L33](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L30-L33), [README.md#L27-L28](https://github.com/codeany-ai/codeany/blob/7e614dc436efb0b72f32d6de9e34a6f8a61886d9/README.md#L27-L28) (`clm_b1d6feebcd035605d5c3ba519d51f6bf2ff12d86eb7c487a3785f4ba2bf7814e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

