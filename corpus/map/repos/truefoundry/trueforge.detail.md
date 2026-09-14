# truefoundry/trueforge -- full detail

[Back to orientation](trueforge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/truefoundry/trueforge/4bf9ce063019c29a0731a800cc81a2039b712572/3a164df5c5bd7b77.json](../../../wiki/dossiers/truefoundry/trueforge/4bf9ce063019c29a0731a800cc81a2039b712572/3a164df5c5bd7b77.json)

## specifications (1 claim(s))

- [observation/documented] TrueForge is an open-source agent harness that runs the agent execution loop (model calls, MCP tools, skills, sandboxing, approvals, context management, session state) and exposes it as a chat UI, an HTTP API with a TypeScript SDK, and an embeddable UI SDK. -- evidence: [README.md#L1-L10](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L1-L10), [README.md#L34-L34](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L34-L34) (`clm_20253b23d80da82a0ea8f881cc79829cbf1b3a0bd160debad7f942525bb80008`)

## components (1 claim(s))

- [observation/documented] The repo ships four npm packages: trueforge-core (library), trueforge (app + CLI, tarball includes dist/_frontend/), trueforge-sdk (Fern-generated, not hand-edited), and trueforge-ui (embeddable chat UI); packages/frontend is unpublished and its build is copied into the trueforge tarball. -- evidence: [RELEASING.md#L43-L44](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L43-L44), [RELEASING.md#L36-L41](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L36-L41) (`clm_e1b36f0681d3738e57f4fdf5ea5d6447d7685f1cadb715be60e239d409a24dbb`)

## design-choices (1 claim(s))

- [observation/documented] TrueForge adopts a 'sandbox as tool' pattern: the agent loop and credentials stay in the harness while the sandbox only runs code, file, and shell operations, is provisioned on demand, and never holds model or MCP credentials. -- evidence: [docs/sandbox.mdx#L24-L26](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L24-L26), [docs/sandbox.mdx#L15-L18](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L15-L18), [docs/sandbox.mdx#L20-L20](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L20-L20), [docs/sandbox.mdx#L72-L73](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L72-L73) (`clm_e18d3f2a282a09a65796cd0920ade1ac22a786c0da091bcc1af20e09b6a22071`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: fork PRs should change source only while maintainers regenerate the SDK after merge; releases use Changesets on main, npm trusted publishing via OIDC (no NPM_TOKEN), and a chart-release pipeline triggered after the trueforge npm publish. -- evidence: [README.md#L103-L103](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L103-L103), [RELEASING.md#L81-L81](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L81-L81), [RELEASING.md#L117-L122](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L117-L122), [RELEASING.md#L51-L63](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L51-L63), [RELEASING.md#L87-L88](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L87-L88) (`clm_093f811e18a7a7f0a85629e6a9f7dfe7f85aea0d18e7165abdfff6ff2958ce65`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are git-backed directories rooted at a SKILL.md with YAML frontmatter (name, description); only the description is visible upfront (progressive disclosure), and when chosen the repo is materialized under /opt/tfy/skills/{name} in the sandbox, which must be enabled. -- evidence: [docs/skills.mdx#L43-L46](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L43-L46), [docs/skills.mdx#L9-L9](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L9-L9), [docs/skills.mdx#L39-L39](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L39-L39), [docs/skills.mdx#L50-L52](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L50-L52) (`clm_a89dea5ff8fe2a79c96701733122f6784feeba26eeaba48ad1189b976bcd3890`)

## interfaces (2 claim(s))

- [observation/documented] The UI SDK offers three levels of control: using the TrueForgeUI component directly, supplying a custom layout, or mounting providers manually; it exports runtime-connected containers (ThreadContainer, ComposerContainer, ThreadListContainer) and presentational atoms replaceable via an overrides mechanism. -- evidence: [docs/ui-sdk/concepts/architecture.mdx#L28-L28](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L28-L28), [docs/ui-sdk/concepts/architecture.mdx#L8-L18](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L8-L18), [docs/ui-sdk/concepts/architecture.mdx#L6-L6](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L6-L6), [docs/ui-sdk/concepts/architecture.mdx#L26-L26](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L26-L26), [docs/ui-sdk/concepts/architecture.mdx#L24-L24](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L24-L24) (`clm_44b21d610b4018b6fae8bddca5dd0133d207f337af491549d90b463683bc0987`)
- [observation/documented] The UI SDK exposes stable styling hooks (.aui-root, .aui-markdown, .aui-monaco, data-slot attributes), though some slot values like avatar and tool-call-card lack the aui_ prefix, so users should inspect elements rather than assume the prefix. -- evidence: [docs/ui-sdk/concepts/architecture.mdx#L54-L54](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L54-L54) (`clm_7cd739cb3940f7caa6e602600f903871cc4e0e8d575b893474173211fe41fdc2`)

## memory-state (1 claim(s))

- [observation/documented] TrueForge runs in local mode (single process, SQLite, no login by default, intended for localhost only) or hosted mode (Postgres + Redis) deployable via Docker Compose, Helm, or Railway. -- evidence: [README.md#L80-L80](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L80-L80), [README.md#L75-L78](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L75-L78), [README.md#L51-L51](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L51-L51) (`clm_8bd2e81d588e3eca3a493ebabda623dc68d2b006af856c2a343748598d1772f6`)

## orchestration (1 claim(s))

- [observation/documented] The harness provides context-engineering features including subagents, deferred tool loading, Code Mode, large-result offloading, and compaction, plus human checkpoints such as tool approval, ask-user-questions, and Generative UI in chat. -- evidence: [README.md#L42-L49](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L42-L49) (`clm_6a0415fe45b851d4d066d9d809f8b1428afe6f9cb9252e534806fae6db2c95d4`)

## tools-permissions (1 claim(s))

- [observation/documented] MCP tool connectivity supports remote servers with header auth or OAuth, including in-chat authorization; sandbox provider configuration requires a Daytona API key with snapshot-create permission, and the sandbox is off by default per agent. -- evidence: [README.md#L42-L49](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L42-L49), [docs/sandbox.mdx#L32-L32](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L32-L32), [docs/sandbox.mdx#L34-L37](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L34-L37), [docs/sandbox.mdx#L58-L58](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L58-L58) (`clm_7b4d2344119d1b2a05de17c62ee1d9f80c5d801f6e2c39e7e3c00a1e43fab86c`)

## evaluation (1 claim(s))

- [observation/documented] The README reports benchmarks comparing TrueForge against Claude Managed Agents and deepagents on the same tasks, tools, and model, claiming equal accuracy at lower cost, with reproduction materials in the benchmark/ directory. -- evidence: [README.md#L99-L99](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L99-L99), [README.md#L84-L95](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L84-L95) (`clm_99f4b979158eba961984bec1d22ca7c98a82f33ec9ed483588a9a68f4eab5fd6`)

## dependencies (1 claim(s))

- [observation/documented] The project requires Node.js >= 22.14, is MIT-licensed, and its Helm chart bundles optional Bitnami Postgres and Redis subcharts that can be disabled via postgresql.enabled=false / redis.enabled=false. -- evidence: [README.md#L114-L114](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L114-L114), [README.md#L16-L30](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L16-L30), [RELEASING.md#L205-L206](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L205-L206) (`clm_78f9d7a12d59986c836ec66817d65ddd1827c03778fd1fc146ce118a18081657`)

## limitations (2 claim(s))

- [observation/documented] In hosted mode with login enabled, the agent library is not scoped per user or team: agents created by anyone are visible to all authenticated users on the deployment, though session history stays owner-scoped and settings remain admin-only. -- evidence: [docs/agent-library.mdx#L21-L21](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/agent-library.mdx#L21-L21), [docs/agent-library.mdx#L23-L27](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/agent-library.mdx#L23-L27), [docs/agent-library.mdx#L29-L29](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/agent-library.mdx#L29-L29) (`clm_e96706f5f9f4c895019cf7594376e62a1bf9d29617e70dfde421504ef0d4c98c`)
- [observation/documented] Daytona is documented as the only sandbox provider supported today, with support for additional providers planned. -- evidence: [docs/sandbox.mdx#L30-L30](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L30-L30) (`clm_71eb11687ed624c56a63f5257d4ea9dafd37e2ddd22d6a0a63ec72b619e9c768`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

