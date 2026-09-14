# choeng-rayu/rayu-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c16466f3b068 @ f8841530529d555b

## Summary (orientation draft, not independently verified)

Rayu CLI is a terminal AI coding agent distributed as @rayu-dev/rayu-cli, documented in a README and CHANGELOG describing a four-service monorepo (CLI, accounts API, Go gateway, website), multi-provider BYOK support, an external-agent orchestrator, a Telegram bridge, and an IPC layer; performance and comparison claims are unverified marketing text.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is a monorepo of four services plus a deploy stack: a TypeScript/Bun/Ink CLI, a NestJS/Prisma/MySQL accounts API, a Go/chi/Redis AI gateway, and a Next.js 15 website, with Docker Compose + Caddy for deployment. -- evidence: [README.md#L112-L112](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L112-L112), [README.md#L114-L120](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L114-L120)
- design-choices (1 claim(s)):
  - [observation/documented] The README claims a custom React/Ink terminal renderer with zero-GC cell buffers and a Go gateway with sub-millisecond routing overhead, with time-to-first-token under 500ms for cached sessions. -- evidence: [README.md#L57-L59](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L57-L59)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are directed to a Contributing Guide covering issues, code formatting, and pull requests, and the project adopts a Contributor Covenant 2.1 code of conduct with a correction/warning/ban enforcement ladder and GitHub-based reporting. -- evidence: [CODE_OF_CONDUCT.md#L57-L58](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L57-L58), [CODE_OF_CONDUCT.md#L78-L78](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L78-L78), [CODE_OF_CONDUCT.md#L72-L72](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L72-L72), [README.md#L137-L137](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L137-L137), [CODE_OF_CONDUCT.md#L90-L90](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L90-L90), [CODE_OF_CONDUCT.md#L100-L100](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L100-L100), [CODE_OF_CONDUCT.md#L84-L84](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L84-L84), [CODE_OF_CONDUCT.md#L96-L96](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CODE_OF_CONDUCT.md#L96-L96)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is distributed as the npm package @rayu-dev/rayu-cli, installable globally via npm, runnable via npx, or via curl/PowerShell install scripts that the README says require no Node, npm, or sudo. -- evidence: [README.md#L80-L81](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L80-L81), [README.md#L102-L104](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L102-L104), [README.md#L7-L11](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L7-L11), [README.md#L96-L98](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L96-L98), [README.md#L85-L86](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L85-L86), [README.md#L76-L76](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L76-L76)
  - [observation/documented] The CLI exposes slash commands including /model for mid-session model switching, /connect for provider setup, /sessions and /switch for Telegram bridge sessions, and /banner, /mascot, /brandmark for branding display. -- evidence: [CHANGELOG.md#L67-L74](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L67-L74), [README.md#L70-L70](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L70-L70), [README.md#L106-L106](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/README.md#L106-L106), [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20), [CHANGELOG.md#L142-L144](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L142-L144)
- memory-state (1 claim(s)):
  - [observation/documented] The changelog describes a secure IPC layer using a Unix socket protocol with per-session token auth, enabling cross-session routing and multi-session coordination. -- evidence: [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20)
- orchestration (2 claim(s)):
  - [observation/documented] The changelog documents an External Agent Orchestrator with an /agent command and ExternalAgent tool to launch and coordinate other agentic CLIs (Codex, Claude Code, OpenCode, ACP agents), with parallel/sequential/race/retry/fallback policies, git worktree isolation, and crash recovery. -- evidence: [CHANGELOG.md#L6-L20](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L6-L20)
  - [observation/documented] The changelog describes a planner subagent dispatching parallel Explore subagents, a collaborator swarm with persistent agent memory syncing, and /ultraplan and /ultrareview commands that run parallel planning/review subagents on the user's own provider. -- evidence: [CHANGELOG.md#L133-L136](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L133-L136), [CHANGELOG.md#L174-L180](https://github.com/Choeng-Rayu/rayu-cli/blob/c16466f3b068732e0be23698155c00a97cccf41c/CHANGELOG.md#L174-L180)
- tools-permissions (1 claim(s)):
More evidence: [full detail](rayu-cli.detail.md)

Metadata and full claim list: [full detail](rayu-cli.detail.md)
Human notes ([notes](rayu-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
