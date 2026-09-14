# superset-sh/superset

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ed42524ed1d4 @ 3abdd6e4e089dfca

## Summary (orientation draft, not independently verified)

The product ships multiple surfaces: a desktop app, a single `superset` CLI binary, a TypeScript SDK (@superset_sh/sdk), and an MCP server that lets agents create and manage workspaces. Superset runs CLI-based coding agents in parallel, each isolated in its own git worktree with its own branch, terminal, and environment.

## Source coverage

Source coverage (partial): 3 of 28 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Superset runs CLI-based coding agents in parallel, each isolated in its own git worktree with its own branch, terminal, and environment. -- evidence: [README.md#L37-L37](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L37-L37), [README.md#L56-L56](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L56-L56)
  - [observation/documented] The desktop app includes a built-in terminal (splits, persistent sessions, rich prompt editor), a diff viewer for reviewing and committing agent changes, and an in-app browser with per-workspace port detection. -- evidence: [README.md#L112-L112](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L112-L112), [README.md#L84-L84](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L84-L84), [README.md#L98-L98](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L98-L98)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run `./.superset/setup.local.sh` then `bun run dev`; the setup script brings up local Postgres plus Electric via Docker and seeds a dev account, requiring Bun 1.3.14+, docker, jq, and caddy. -- evidence: [README.md#L287-L287](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L287-L287), [README.md#L279-L281](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L279-L281), [README.md#L283-L285](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L283-L285), [README.md#L274-L277](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L274-L277)
  - [observation/documented] Repository development practice: AGENTS.md prescribes a component folder layout (one folder per component, co-located tests, barrel exports), Lingui-based i18n with `bun run check:i18n` enforced in CI, and a rule against hand-editing generated Drizzle migration files. -- evidence: [AGENTS.md#L72-L75](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L72-L75), [AGENTS.md#L83-L85](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L83-L85), [AGENTS.md#L140-L154](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L140-L154)
- skills-patterns (1 claim(s)):
  - [observation/documented] Agents come pre-loaded with `superset:*` skills (orchestrating parallel agents, scheduling automations, filing feedback, diagnosing issues) provisioned automatically at launch. -- evidence: [README.md#L181-L190](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L181-L190)
- interfaces (1 claim(s)):
  - [observation/documented] The product ships multiple surfaces: a desktop app, a single `superset` CLI binary, a TypeScript SDK (@superset_sh/sdk), and an MCP server that lets agents create and manage workspaces. -- evidence: [README.md#L235-L240](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L235-L240)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Agent sessions can be scheduled as automations, e.g. overnight issue triage, changelog drafting, or dependency freshness tasks. -- evidence: [README.md#L126-L126](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L126-L126)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The only hard runtime prerequisite stated is Git; the GitHub CLI (gh) is optional and unlocks PR workflows, with Superset offering to install it. -- evidence: [README.md#L261-L261](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L261-L261)
  - [observation/documented] The tech stack is described as Electron, React, Tailwind, Bun, Turborepo, Vite, Biome, Drizzle ORM, Neon, and tRPC. -- evidence: [README.md#L307-L318](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L307-L318), [AGENTS.md#L3-L3](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L3-L3)
More evidence: [full detail](superset.detail.md)

Metadata and full claim list: [full detail](superset.detail.md)
Human notes ([notes](superset.notes.md), never overwritten by build)

[Back to map index](../../index.md)
