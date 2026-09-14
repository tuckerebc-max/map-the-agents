# awslabs/cli-agent-orchestrator -- full detail

[Back to orientation](cli-agent-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/awslabs/cli-agent-orchestrator/948c3d8004faa9f2f61b1c65dcde19291d7e072b/e8d798b8201b64d1.json](../../../wiki/dossiers/awslabs/cli-agent-orchestrator/948c3d8004faa9f2f61b1c65dcde19291d7e072b/e8d798b8201b64d1.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The project ships a cao-mcp-server that exposes orchestration tools such as assign, handoff, report_outcome, list_outcomes, and store_lesson to agents over MCP. -- evidence: [CHANGELOG.md#L131-L136](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L131-L136) (`clm_d189db69298b2c94bfcfbe1dfba26deb49145a48e92291fb4ab1784a3ef105f7`)
- [observation/documented] Multiple agent CLI providers are supported, including MiniMax Code (mcode), Oh My Pi (omp), xAI Grok Build CLI (grok_cli), Cursor CLI, and Antigravity CLI (agy). -- evidence: [CHANGELOG.md#L432-L432](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L432-L432), [CHANGELOG.md#L62-L69](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L62-L69), [CHANGELOG.md#L450-L450](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L450-L450) (`clm_50bae23659e17f11e1e05ab011e1a0b3211155a5fbdb692e6399da4e3b8d6341`)

## design-choices (1 claim(s))

- [observation/documented] Sessions run in tmux terminals with a conductor concept: a session's first (oldest surviving) terminal is normally its conductor, and five consumers depend on that ordering. -- evidence: [CHANGELOG.md#L129-L129](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L129-L129) (`clm_9661057684772b4e36c1d48a8e66bcf421f824910fc9a5314af36046298677a4`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] CLI commands cao agent assign|handoff|send-message|status|result|cancel exist as a fallback when a terminal's MCP connection is unavailable, sharing an orchestration module with the MCP tools. -- evidence: [CHANGELOG.md#L107-L112](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L107-L112) (`clm_85accfa3635dbc0d6bb6a30a9b7610cda1d1a48bedf3564256ac339a2bf44158`)
- [observation/documented] A Web UI provides a Profiles tab for browsing, creating, editing, cloning, and deleting agent profiles over profile management APIs, plus memory-system and fleet-panel views. -- evidence: [CHANGELOG.md#L12-L15](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L12-L15), [CHANGELOG.md#L476-L476](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L476-L476), [CHANGELOG.md#L428-L428](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L428-L428) (`clm_fc8d937d761bfacf4e1a4e1031788b4c4ebcd22d15c68c07d742252ea8a6b4bc`)

## memory-state (2 claim(s))

- [observation/documented] The system includes a memory layer with typed relationship storage, memory plugins for Claude Code, Kiro, and Codex, and a wiki with self-healing via 'cao memory heal'. -- evidence: [CHANGELOG.md#L288-L288](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L288-L288), [CHANGELOG.md#L426-L426](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L426-L426), [CHANGELOG.md#L452-L452](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L452-L452) (`clm_69523683b861008c7f526f19d0f8f59b04f5515ad335328c60394bee829316ae`)
- [observation/documented] An opt-in self-learning loop captures outcomes, performs retrospection, and promotes instructions; a skills/cao-learning skill instructs agents how to use it. -- evidence: [CHANGELOG.md#L25-L32](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L25-L32), [CHANGELOG.md#L280-L280](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L280-L280) (`clm_c578c9d5ca7ae4a8d504951834f86b58a5d60ded544d51d10977f80b89268576`)

## orchestration (1 claim(s))

- [observation/documented] Orchestration includes supervisor/worker flows, a run engine with durable run journal and playback, frozen execution manifests with plan approval, and a cross-node fleet coordinator. -- evidence: [CHANGELOG.md#L460-L460](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L460-L460), [CHANGELOG.md#L464-L464](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L464-L464), [CHANGELOG.md#L79-L79](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L79-L79), [CHANGELOG.md#L105-L105](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L105-L105) (`clm_d2fdee6cac98916e1c7ef790ca23600d607ced0aaea22ee8c2ad45213cf20ad7`)

## tools-permissions (1 claim(s))

- [observation/documented] The grok_cli provider offers native hard tool restrictions, and network egress is gated behind a web_fetch tool category; per-role tool-restriction examples are provided. -- evidence: [CHANGELOG.md#L85-L85](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L85-L85), [CHANGELOG.md#L62-L69](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L62-L69), [CHANGELOG.md#L436-L436](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L436-L436) (`clm_c33855e07578e7ef161b073222344ed2eec5cdecd8c3a8199c9ad05b46a0f011`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project floors at cryptography>=50.0.0 for two HIGH CVEs, pins nanoid >=3.3.17 via npm overrides for CVE-2026-67213, and bumped mcp to 1.28.1. -- evidence: [CHANGELOG.md#L408-L408](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L408-L408), [CHANGELOG.md#L210-L214](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L210-L214), [CHANGELOG.md#L152-L152](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L152-L152) (`clm_8d25ac339bc8aaca4df03f77e80eff23628a1b57aec6449aeb7abf6040f94ad2`)

## limitations (2 claim(s))

- [observation/documented] Windows is unsupported: the backend is tmux and four modules import fcntl at module scope, so the package refuses Windows at import with an explanation. -- evidence: [CHANGELOG.md#L206-L208](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L206-L208) (`clm_a80ea9bd8bd3a66107d0d5094eef74417946ee52ab145020187f3007b2f6dcfa`)
- [observation/documented] Intel macOS wheels are no longer published because cryptography 49.0.0+ ships no Intel-macOS wheel and CAO requires cryptography>=50.0.0, so Intel Macs cannot resolve dependencies. -- evidence: [CHANGELOG.md#L210-L214](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L210-L214) (`clm_42febe8e6d99ab2464dfd452a0620b84430fa96b0e2fc0a0ebaeb7fbda9fda4e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

