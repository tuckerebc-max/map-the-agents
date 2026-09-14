# ramarlina/agx -- full detail

[Back to orientation](agx.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ramarlina/agx/e674cec110883774508aee1ee1ca355827563725/14a96526364b8134.json](../../../wiki/dossiers/ramarlina/agx/e674cec110883774508aee1ee1ca355827563725/14a96526364b8134.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture comprises a SQLite (WAL mode) state layer with durable checkpoints, a CLI plus daemon handling provider tool calls, filesystem edits, and worktree isolation, and a decision layer for human gate transitions and review flow. -- evidence: [README.md#L131-L133](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L131-L133) (`clm_be95bf4204416c7310220ba674091f41d401029d0aa7d121f6550e2c70bf5d6c`)

## design-choices (3 claim(s))

- [observation/documented] Work is checkpointed at every step so restarts resume where the user left off, and resuming is described as constant-cost regardless of thread age. -- evidence: [README.md#L127-L127](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L127-L127) (`clm_8f43a2c17da823b86637cfe0997ec782476659fdd467e501576b100917d2c3dc`)
- [observation/documented] Agents pause for explicit human approve/reject before anything irreversible, and PR review begins with a first pass from a reviewer agent. -- evidence: [README.md#L112-L119](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L112-L119) (`clm_4dfe9c7a7357fadb0e55e2af544c1074fcb80ba3fdf4394ec3865a5d4e56f005`)
- [inference/documented] The planned GitHub integration would store PRs, comments, links, and sync state in a dedicated SQLite database at ~/.agx/github/prs.sqlite (env-overridable), mirroring the existing Linear adapter pattern; this is planned, not verified as shipped. -- evidence: [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L7-L7](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L7-L7), [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L146-L146](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L146-L146), [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L159-L164](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L159-L164), [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L166-L166](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L166-L166) (`clm_012fc4f7c4358bb86baffaa6b8f41684c2192a294d503728854f43555a4575e1`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the repo is an npm workspace with apps/local (Next.js dashboard), apps/desktop (Electron), lib, commands, and cloud-runtime; dev commands include `npm run local:dev`, `local:build`, `board:bundle`, and Electron `build:mac`. -- evidence: [README.md#L205-L213](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L205-L213), [README.md#L217-L220](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L217-L220), [README.md#L203-L203](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L203-L203), [README.md#L231-L235](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L231-L235), [README.md#L224-L227](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L224-L227) (`clm_2fc2b97348c1555c5ba81b888cf8c5e7b45f4e70bf58fb5075e95baa03253843`)
- [observation/documented] Repository development practice: contributions are welcomed via GitHub Discussions and Issues, with PRs made by forking main, adding tests, and submitting. -- evidence: [README.md#L250-L250](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L250-L250), [README.md#L252-L254](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L252-L254) (`clm_1d310568b677a06c7fe23d8cfd7116f1c0b0b4e07758110f19a7993dc80db8f7`)
- [observation/documented] Repository development practice: a GitHub-integration Phase 1 plan instructs agentic workers to use superpowers subagent-driven-development or executing-plans, building schema, stores, OAuth stubs, a link resolver, and sync orchestrator behind an AGX_GITHUB_ENABLED feature flag, TDD-style with Jest and mocked HTTP. -- evidence: [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L37-L37](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L37-L37), [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L3-L3](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L3-L3), [docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L5-L5](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/docs/superpowers/plans/2026-04-17-github-integration-phase1.md#L5-L5) (`clm_6bbcbe2232fc08a532ad3efc1fa8801fb598de1dd55862feb0c927439a7e1c4f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] AGX ships as a CLI, a local web dashboard, and a macOS desktop app from one repository. -- evidence: [README.md#L57-L57](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L57-L57) (`clm_79d0bb44e32584ddb4b06b655ce953583e9282baee7342d263a455a6000b56da`)
- [observation/documented] The CLI exposes provider chat commands such as `agx claude -p`, `agx codex -p`, `agx gemini -p`, and `agx ollama -p`, with single-letter aliases c, x, g, o. -- evidence: [README.md#L147-L152](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L147-L152) (`clm_2e847a2d1ace253497f63d58e46dbadc556e402b8ea7e09041811b43c9d26f35`)
- [observation/documented] CLI commands include `agx init` for first-time setup, `agx board start` to open the ticket-agent-PR board, plus project, repo, workspace, and vars subcommands. -- evidence: [README.md#L159-L166](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L159-L166), [README.md#L170-L174](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L170-L174), [README.md#L75-L80](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L75-L80) (`clm_0baa37ce201822a478a776f7daba1b74abc4ce0f2026dee83d0a4685038640fb`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product claims fully local operation with an activity log, signed actions, and destructive-command safeguards. -- evidence: [README.md#L135-L135](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L135-L135), [README.md#L112-L119](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L112-L119) (`clm_96c4ae598502f6bb42b0056b703d31bc5c276cbf27c518d42cd3a3b7c097e8a4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requires Node.js >= 22.16.0 for CLI install and at least one provider CLI (Claude Code, Codex CLI, Gemini CLI, or Ollama); no external database is needed since SQLite is used locally. -- evidence: [README.md#L196-L196](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L196-L196), [README.md#L189-L194](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L189-L194) (`clm_51026b6e21cca3154de9adb1ae9ccc6e5c97616437ba0732128e603166460e40`)
- [observation/documented] Telemetry is enabled by default, collecting anonymous usage data such as OS, Node and AGX versions, commands run, provider used, task outcomes, and timing; it can be disabled via `agx telemetry off` or config. -- evidence: [README.md#L279-L280](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L279-L280), [README.md#L265-L273](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L265-L273), [README.md#L261-L261](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L261-L261) (`clm_69a04ac3a23bf342b9db88c4a08b8fde46a182bea213842d8223a7979d8d1f1b`)

## limitations (1 claim(s))

- [observation/documented] The telemetry documentation states prompts, code, API keys, file paths, and PII are not collected. -- evidence: [README.md#L275-L275](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L275-L275) (`clm_3c14424bc4334b88070601ba6dc1305cdcf6292afc9d07318511261da4d86950`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

