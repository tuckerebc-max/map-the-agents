# truefoundry/trueforge

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4bf9ce063019 @ 3a164df5c5bd7b77

## Summary (orientation draft, not independently verified)

TrueForge is an open-source (MIT) TypeScript agent harness that runs the agent loop and exposes it via chat UI, HTTP API/SDK, and an embeddable UI SDK, with SQLite local mode and Postgres+Redis hosted mode. Evidence covers its architecture, sandbox-as-tool design, skills system, UI SDK composition, benchmarking claims, release workflows, and a documented multi-tenancy limitation.

## Source coverage

Source coverage (partial): 6 of 50 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] TrueForge is an open-source agent harness that runs the agent execution loop (model calls, MCP tools, skills, sandboxing, approvals, context management, session state) and exposes it as a chat UI, an HTTP API with a TypeScript SDK, and an embeddable UI SDK. -- evidence: [README.md#L1-L10](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L1-L10), [README.md#L34-L34](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L34-L34)
- components (1 claim(s)):
  - [observation/documented] The repo ships four npm packages: trueforge-core (library), trueforge (app + CLI, tarball includes dist/_frontend/), trueforge-sdk (Fern-generated, not hand-edited), and trueforge-ui (embeddable chat UI); packages/frontend is unpublished and its build is copied into the trueforge tarball. -- evidence: [RELEASING.md#L43-L44](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L43-L44), [RELEASING.md#L36-L41](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L36-L41)
- design-choices (1 claim(s)):
  - [observation/documented] TrueForge adopts a 'sandbox as tool' pattern: the agent loop and credentials stay in the harness while the sandbox only runs code, file, and shell operations, is provisioned on demand, and never holds model or MCP credentials. -- evidence: [docs/sandbox.mdx#L24-L26](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L24-L26), [docs/sandbox.mdx#L15-L18](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L15-L18), [docs/sandbox.mdx#L20-L20](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L20-L20), [docs/sandbox.mdx#L72-L73](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/sandbox.mdx#L72-L73)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: fork PRs should change source only while maintainers regenerate the SDK after merge; releases use Changesets on main, npm trusted publishing via OIDC (no NPM_TOKEN), and a chart-release pipeline triggered after the trueforge npm publish. -- evidence: [README.md#L103-L103](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/README.md#L103-L103), [RELEASING.md#L81-L81](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L81-L81), [RELEASING.md#L117-L122](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L117-L122), [RELEASING.md#L51-L63](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L51-L63), [RELEASING.md#L87-L88](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/RELEASING.md#L87-L88)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are git-backed directories rooted at a SKILL.md with YAML frontmatter (name, description); only the description is visible upfront (progressive disclosure), and when chosen the repo is materialized under /opt/tfy/skills/{name} in the sandbox, which must be enabled. -- evidence: [docs/skills.mdx#L43-L46](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L43-L46), [docs/skills.mdx#L9-L9](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L9-L9), [docs/skills.mdx#L39-L39](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L39-L39), [docs/skills.mdx#L50-L52](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/skills.mdx#L50-L52)
- interfaces (2 claim(s)):
  - [observation/documented] The UI SDK offers three levels of control: using the TrueForgeUI component directly, supplying a custom layout, or mounting providers manually; it exports runtime-connected containers (ThreadContainer, ComposerContainer, ThreadListContainer) and presentational atoms replaceable via an overrides mechanism. -- evidence: [docs/ui-sdk/concepts/architecture.mdx#L28-L28](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L28-L28), [docs/ui-sdk/concepts/architecture.mdx#L8-L18](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L8-L18), [docs/ui-sdk/concepts/architecture.mdx#L6-L6](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L6-L6), [docs/ui-sdk/concepts/architecture.mdx#L26-L26](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L26-L26), [docs/ui-sdk/concepts/architecture.mdx#L24-L24](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L24-L24)
  - [observation/documented] The UI SDK exposes stable styling hooks (.aui-root, .aui-markdown, .aui-monaco, data-slot attributes), though some slot values like avatar and tool-call-card lack the aui_ prefix, so users should inspect elements rather than assume the prefix. -- evidence: [docs/ui-sdk/concepts/architecture.mdx#L54-L54](https://github.com/truefoundry/trueforge/blob/4bf9ce063019c29a0731a800cc81a2039b712572/docs/ui-sdk/concepts/architecture.mdx#L54-L54)
- memory-state (1 claim(s)):
More evidence: [full detail](trueforge.detail.md)

Metadata and full claim list: [full detail](trueforge.detail.md)
Human notes ([notes](trueforge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
