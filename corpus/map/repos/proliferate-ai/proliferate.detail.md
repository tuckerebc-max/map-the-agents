# proliferate-ai/proliferate -- full detail

[Back to orientation](proliferate.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/proliferate-ai/proliferate/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/48727c705a63ed65.json](../../../wiki/dossiers/proliferate-ai/proliferate/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/48727c705a63ed65.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product supports subagents that delegate scoped work to child agents, plus integrations including MCPs, skills, Computer Use, Browser Use, and custom tools shared across agents. -- evidence: [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49) (`clm_71e9505bff09d8c05b54d1647db971f35521595d861603fff6254abb2f10d467`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: running from source requires Rust stable, Node.js 22+, and pnpm, with 'make install' and 'make dev-local' to launch the desktop app with the bundled local AnyHarness runtime. -- evidence: [README.md#L121-L124](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L121-L124), [README.md#L119-L119](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L119-L119), [README.md#L115-L117](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L115-L117) (`clm_96a22697aa3f93d1d23d10c2481806e4737e36f6f05a15e0c72863573b48c793`)
- [observation/documented] Repository development practice: local full-stack development additionally needs Python 3.12+, uv, and Docker, using named dev profiles when multiple worktrees run concurrently. -- evidence: [README.md#L126-L128](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L126-L128), [README.md#L138-L139](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L138-L139), [README.md#L130-L136](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L130-L136) (`clm_54ee03fd46a4d5c4b24f81c15a7d667ea0f7c2c946c83b136489901f38453b8f`)
- [observation/documented] Repository development practice: AGENTS.md routes contributors to per-area and per-system spec docs, and contributors must run 'python3 scripts/check_docs.py' after changing repository documentation. -- evidence: [AGENTS.md#L18-L25](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L18-L25), [AGENTS.md#L56-L58](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L56-L58), [AGENTS.md#L60-L79](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L60-L79), [AGENTS.md#L13-L14](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L13-L14), [AGENTS.md#L145-L145](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L145-L145) (`clm_760fa0954dd8833539139405c2c530e70cf73b242e01e893ab21e64a5770374e`)
- [observation/documented] Repository development practice: repository rules forbid weakening lints or deleting pinning tests without founder review, discourage destructive git commands, and require PRs to consider testing and observability standards. -- evidence: [AGENTS.md#L106-L111](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L106-L111), [AGENTS.md#L115-L143](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L115-L143) (`clm_2b6b846767e639a20a7f71a6b2c62c319e4fc887988c8732556447696e9650b6`)
- [observation/documented] Repository development practice: server tests are run with 'uv run pytest -q' from the server directory, and the anyharness SDK is built via pnpm generate and build steps. -- evidence: [AGENTS.md#L35-L37](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/AGENTS.md#L35-L37) (`clm_3bf5e99d8fe82ae402811bab8743cdd85053c554093326181211623fd15ed60e`)
- [observation/documented] Repository development practice: CLAUDE.md instructs Claude Code to read and follow AGENTS.md before working and to follow assigned documentation lifecycles rather than re-deriving settled architecture. -- evidence: [CLAUDE.md#L5-L9](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/CLAUDE.md#L5-L9), [CLAUDE.md#L3-L3](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/CLAUDE.md#L3-L3) (`clm_de68bedfdd7f6f86b48da08af05400aa723612d0e3a60c4ad7a7589bf5f194f8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Proliferate runs coding agents such as Claude Code, Codex, OpenCode, Cursor, and Grok through each agent's native harness. -- evidence: [README.md#L53-L53](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L53-L53), [README.md#L23-L24](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L23-L24), [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49), [README.md#L55-L87](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L55-L87) (`clm_1f00b19537f6de34a749521d8ed2f818035f6f3f3795eb069f4c307a33b4d3aa`)
- [observation/documented] The desktop app can be pointed at a self-hosted control plane via a documented configuration procedure. -- evidence: [README.md#L102-L106](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L102-L106) (`clm_fb5b041378797d93948cb5e82e19cd47ee45e5fea8e6fe1619120bd278ff7c23`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Multiple coding agents can run in parallel in one workspace, and each task gets an isolated git worktree with its own branch, terminal, conversation, and review state. -- evidence: [README.md#L23-L24](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L23-L24), [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49) (`clm_9fd1c5cbdbfb144a212faa2119164de0f12ac8835137f8fb81df4bd087e07515`)
- [observation/documented] The product advertises recurring and event-driven agent workflows, such as nightly review passes, alert triage, and dependency bumps. -- evidence: [README.md#L44-L49](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L44-L49) (`clm_61f086cb72c79561e1f76cadccefc1f2acf6b6bc323fcf9b3d3571bdd7bf14d9`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The control plane is self-hostable; the Docker Compose guide runs Caddy, Postgres, and the API with bootstrap and update scripts, and an AWS option uses a CloudFormation wrapper on EC2. -- evidence: [README.md#L95-L100](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L95-L100), [README.md#L91-L93](https://github.com/proliferate-ai/proliferate/blob/74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f/README.md#L91-L93) (`clm_0a5daf5425c05a5d90c20acd36298fc82f5385990338bed296d039f46c0b45f6`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

