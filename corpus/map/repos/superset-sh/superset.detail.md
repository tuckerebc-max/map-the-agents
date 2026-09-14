# superset-sh/superset -- full detail

[Back to orientation](superset.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/superset-sh/superset/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/3abdd6e4e089dfca.json](../../../wiki/dossiers/superset-sh/superset/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/3abdd6e4e089dfca.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Superset runs CLI-based coding agents in parallel, each isolated in its own git worktree with its own branch, terminal, and environment. -- evidence: [README.md#L37-L37](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L37-L37), [README.md#L56-L56](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L56-L56) (`clm_608904044747fbcba50a6a2aed5c8482f182a23dab479c18ed4a13708e305639`)
- [observation/documented] The desktop app includes a built-in terminal (splits, persistent sessions, rich prompt editor), a diff viewer for reviewing and committing agent changes, and an in-app browser with per-workspace port detection. -- evidence: [README.md#L112-L112](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L112-L112), [README.md#L84-L84](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L84-L84), [README.md#L98-L98](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L98-L98) (`clm_cdf7a99d30c1a333a06c24bfb3f0122d0d213cfd3946fe1f6b499d201b2988bf`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run `./.superset/setup.local.sh` then `bun run dev`; the setup script brings up local Postgres plus Electric via Docker and seeds a dev account, requiring Bun 1.3.14+, docker, jq, and caddy. -- evidence: [README.md#L287-L287](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L287-L287), [README.md#L279-L281](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L279-L281), [README.md#L283-L285](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L283-L285), [README.md#L274-L277](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L274-L277) (`clm_9e4d34f44a781e92dc045a706f7eca8409b2b1c61bdb3d22625e550b8b3916a4`)
- [observation/documented] Repository development practice: AGENTS.md prescribes a component folder layout (one folder per component, co-located tests, barrel exports), Lingui-based i18n with `bun run check:i18n` enforced in CI, and a rule against hand-editing generated Drizzle migration files. -- evidence: [AGENTS.md#L72-L75](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L72-L75), [AGENTS.md#L83-L85](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L83-L85), [AGENTS.md#L140-L154](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L140-L154) (`clm_1ef29b0721e24c4eee120122512fe24a90917bc06f83c3ad641258f8d8ab9232`)
- [observation/documented] Repository development practice: plugin releases are git tags `<name>@<version>`; publishing rewrites `.agent-marketplace.json` and generated manifests, and `bun run check:plugins` runs in CI to catch skipped publish steps. -- evidence: [AGENTS.md#L95-L101](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L95-L101) (`clm_95ea37020f92407860938d24ec99da935c1134eb7fee751a3d5d241a4c41579a`)

## skills-patterns (1 claim(s))

- [observation/documented] Agents come pre-loaded with `superset:*` skills (orchestrating parallel agents, scheduling automations, filing feedback, diagnosing issues) provisioned automatically at launch. -- evidence: [README.md#L181-L190](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L181-L190) (`clm_ae6e5ee6b9906fa9329629d30e11d3b9ae9c9dd14665bc76aba7745ed47d102b`)

## interfaces (1 claim(s))

- [observation/documented] The product ships multiple surfaces: a desktop app, a single `superset` CLI binary, a TypeScript SDK (@superset_sh/sdk), and an MCP server that lets agents create and manage workspaces. -- evidence: [README.md#L235-L240](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L235-L240) (`clm_fef957afcc1973e2e0465fccfd8a15789b7e043672202ba71ae9dd628253dae2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Agent sessions can be scheduled as automations, e.g. overnight issue triage, changelog drafting, or dependency freshness tasks. -- evidence: [README.md#L126-L126](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L126-L126) (`clm_4d48112cee747b6ee534dd7c5468f10c4887892f9163c2e1c1aa230789ffcc98`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The only hard runtime prerequisite stated is Git; the GitHub CLI (gh) is optional and unlocks PR workflows, with Superset offering to install it. -- evidence: [README.md#L261-L261](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L261-L261) (`clm_ce8f3063791b3e38c027cd9d4087fa6f0e412debc4840830d93f4afa6c2b8bc1`)
- [observation/documented] The tech stack is described as Electron, React, Tailwind, Bun, Turborepo, Vite, Biome, Drizzle ORM, Neon, and tRPC. -- evidence: [README.md#L307-L318](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L307-L318), [AGENTS.md#L3-L3](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/AGENTS.md#L3-L3) (`clm_6ca490113567e120064980146f89d49054a87981caa05a987ed0fc0db32d3dcc`)

## limitations (1 claim(s))

- [observation/documented] Per the README, Windows builds are not yet available; Linux x64 AppImage is experimental, with macOS the primary target. -- evidence: [README.md#L256-L259](https://github.com/superset-sh/superset/blob/ed42524ed1d4d33cdfa4bf201871cfc8ffa51637/README.md#L256-L259) (`clm_412ef1f667382f3ef812c8498ab5b40ba4f85182f41f8b31298e14a44cd8eec4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

