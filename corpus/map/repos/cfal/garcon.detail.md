# cfal/garcon -- full detail

[Back to orientation](garcon.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cfal/garcon/42a5322794a9a755a9eee34f707aeb7e72ee6331/76fa39f541038aba.json](../../../wiki/dossiers/cfal/garcon/42a5322794a9a755a9eee34f707aeb7e72ee6331/76fa39f541038aba.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is organized into a SvelteKit/Svelte 5 frontend (web/), a Bun server handling chat lifecycle, providers, Git, auth, and notifications (server/), agent-specific runtimes (server-agents/), shared contracts (common/), and black-box integration tests. -- evidence: [README.md#L190-L194](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L190-L194) (`clm_e84ccf9c333cc2fd9e51fd973c59808460c778a86ea5c652c65a1f9f9d0081fe`)

## design-choices (1 claim(s))

- [observation/documented] Model names may carry a `[Nk]` suffix (100-1000, thousands of tokens) that sets a per-chat Claude auto-compaction window; the annotation overrides CLAUDE_CODE_AUTO_COMPACT_WINDOW for that child process only and requires Claude Code 2.1.238+. -- evidence: [README.md#L117-L117](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L117-L117), [README.md#L119-L119](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L119-L119) (`clm_82abca4e5a09be83ec4f3a4e34c315073c324ad2d1cb545e7908398138ab7318`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: AGENTS.md directs contributors to use bun instead of npm, run `bun run test` to validate changes, start new servers on different ports rather than killing running ones, and treat the git tree as read-only unless instructed. -- evidence: [AGENTS.md#L7-L37](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L7-L37) (`clm_c7ec9f7aee411fe82f84ae67049157813defb12b06b4478849a051a175ca4285`)
- [observation/documented] Repository development practice: every WebSocket/API contract change requires updated type definitions, sender and receiver logic, tests, and a migration note in the PR description when behavior changes. -- evidence: [AGENTS.md#L56-L60](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L56-L60), [AGENTS.md#L50-L52](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L50-L52), [AGENTS.md#L54-L54](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L54-L54) (`clm_1b63d0f83240485fa164f987a9fa4d1fadac8469dd1500f42e2c2317a222e4da`)
- [observation/documented] Repository development practice: integration coverage is mandatory when correctness crosses server, transport, persistence, provider, or SPA boundaries, with black-box server tests under integration-tests/tests/server and live-agent suites kept under test:live:* gated by PR CI. -- evidence: [AGENTS.md#L406-L409](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L406-L409), [AGENTS.md#L402-L402](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L402-L402) (`clm_3df0c98e0533218c819df3ddc92e8f3d89a964db4f3f9b9546fd63c0e3f9683a`)
- [observation/documented] Repository development practice: the frontend must follow canonical Svelte 5 patterns, including $state/$derived/$effect rune usage, callback props instead of createEventDispatcher, and typed context helpers rather than string-keyed context. -- evidence: [AGENTS.md#L306-L307](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L306-L307), [AGENTS.md#L311-L312](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L311-L312), [AGENTS.md#L289-L293](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L289-L293), [AGENTS.md#L321-L322](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L321-L322) (`clm_0021cf51c63bd3e36b565e6987acf9faddc9d7814c113f8c4c95e0ebbeb952c0`)

## skills-patterns (1 claim(s))

- [observation/documented] A companion garcon-skills package exposes the control plane to skill-aware agents via skills like garcon-captain, garcon-agent, garcon-task, garcon-message, garcon-schedule, and garcon-amp, installed with a link.sh script. -- evidence: [README.md#L145-L147](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L145-L147), [README.md#L155-L155](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L155-L155), [README.md#L143-L143](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L143-L143), [README.md#L149-L153](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L149-L153) (`clm_33b52fd12413901b72a930d99ec0b3a6fb790c9f23501134f7fb474d98d3f506`)

## interfaces (3 claim(s))

- [observation/documented] A CLI drives visible Garcon chats through a running server, supporting catalog discovery, sync/detached starts and resumes, steering, status, transcript search and reads, export, handoff, and stop controls. -- evidence: [README.md#L123-L123](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L123-L123) (`clm_2ad387874998c477d65e534b082df5c31930a6f284ae3fa473681a04188e59af`)
- [observation/documented] The web UI is served at http://127.0.0.1:8080 by default; first launch requires creating an account at /setup, and authentication is enabled by default. -- evidence: [README.md#L38-L38](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L38-L38) (`clm_432a5f146be6dfa7357a70ab0968d76a9d30e955e7d1a768ac4eae3b442bfa4e`)
- [observation/documented] The CLI is invoked as `bun cli/main.ts --workspace <name>` with subcommands such as start-async, search, read, status, and resume-async, including flags like --parent, --agent, --model, and --permissions. -- evidence: [README.md#L132-L133](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L132-L133), [README.md#L127-L129](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L127-L129), [README.md#L136-L139](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L136-L139) (`clm_658acd5967d19269261de486795c819c53fbd3ce86521543847477224059ec5b`)

## memory-state (1 claim(s))

- [observation/documented] Tickets persist in the workspace's tickets.sqlite, independent of chats and transcripts; a damaged or unknown-schema store is left unavailable for explicit recovery rather than rebuilt from transcripts. -- evidence: [README.md#L165-L165](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L165-L165) (`clm_75ea4fe2e40dac035fe3fb43623545ee8ca4d97c38e4839f6114275d94f1e545`)

## orchestration (1 claim(s))

- [observation/documented] Chats can exchange provenance-labeled messages, launch delegated child chats, and receive their final results while keeping parentage auditable; the workspace tiles up to four resizable windows and tracks lineage in Chat Map. -- evidence: [README.md#L54-L60](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L54-L60) (`clm_f1bde8ef6a719c03ac9426124604535b8752b557e99fda47e06b319acc6d4e02`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Running Garcon requires Bun, git, and a modern browser, plus at least one coding agent or API provider; optional pull-request support needs an authenticated GitHub CLI on the host. -- evidence: [README.md#L42-L44](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L42-L44) (`clm_1153a4567aec63fd56e8be5a7dd02c17e75fd2e75c08868e4254c1b62812af99`)
- [observation/documented] Garcon supports Claude Code, Codex, Cursor Agent, OpenCode, Amp, Factory Droid, and Pi as coding agents, plus direct Anthropic Messages and OpenAI Responses/Chat Completions compatible endpoints and provider presets like Ollama and OpenRouter. -- evidence: [README.md#L111-L111](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L111-L111), [README.md#L113-L113](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L113-L113), [README.md#L109-L109](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L109-L109) (`clm_20d068f8e1cc00d3c29622ac36ed14acbac868546f854d3defa14d68c512b99a`)

## limitations (1 claim(s))

- [observation/documented] Garcon does not sandbox agents or their commands, which run on the host under the user's account; the README warns against exposing an unauthenticated instance to an untrusted network. -- evidence: [README.md#L27-L27](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L27-L27), [README.md#L179-L179](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L179-L179) (`clm_721a26cbe454ea51cd3886d428dd9aa26b99ebcd449bae9258ea426ec338d9e8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

