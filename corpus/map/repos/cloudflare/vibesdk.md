# cloudflare/vibesdk

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9da158d82c59 @ b32132cd1ca47fd1

## Summary (orientation draft, not independently verified)

VibeSDK is an open-source agentic platform for building and deploying full-stack applications on Cloudflare, built around a ThinkAgent Durable Object loop, SpaceDO workspaces, Cloudflare Artifacts version history, Worker Loader previews, and per-app SQLite Facets. Legacy phase-based architecture diagrams are explicitly marked retired and must not describe the current implementation. Evidence coverage: 135 of 342 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] VibeSDK is described as an open-source agentic platform for building and deploying full-stack applications on Cloudflare, with a hosted demo at build.cloudflare.dev. -- evidence: [README.md#L3-L3](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L3-L3), [README.md#L7-L7](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L7-L7)
  - [observation/documented] Users build apps by describing what they want and answering clarifying questions while the agent plans, edits files, deploys previews, inspects errors, and iterates with the human in the loop. -- evidence: [README.md#L15-L15](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L15-L15)
- components (1 claim(s)):
  - [observation/documented] The architecture comprises a ThinkAgent Durable Object running the model-and-tool loop, a SpaceDO workspace per project, Cloudflare Artifacts for git history and restore points, a Worker Loader for Dynamic Worker previews, and a generated App Durable Object Facet with SQLite. -- evidence: [README.md#L34-L41](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L34-L41)
- design-choices (1 claim(s)):
  - [observation/documented] Feature settings are dashboard-managed rather than committed in wrangler.jsonc, with keep_vars: true preserving production values across deploys; listed toggles default to off while ENABLE_EMAIL_AUTH defaults to on. -- evidence: [README.md#L116-L116](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L116-L116)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork and clone, run bun install and bun run setup, follow AGENTS.md, then run bun run typecheck, lint, and test before opening a pull request describing the change and its validation. -- evidence: [README.md#L151-L155](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L151-L155)
  - [observation/documented] Repository development practice: local development uses Node.js 18+, Bun, and commands such as bun run dev, build, typecheck, lint, and test, with bun run deploy building, migrating, and deploying via .prod.vars. -- evidence: [README.md#L120-L129](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L120-L129), [README.md#L96-L98](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L96-L98)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Previews are produced by bundling each committed deployment with @cloudflare/worker-bundler and loading it through the Worker Loader binding; SpaceDO serves static assets while backend requests and WebSockets are forwarded to the generated App Facet. -- evidence: [README.md#L60-L60](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L60-L60)
- memory-state (2 claim(s)):
  - [observation/documented] Each generated application gets isolated SQLite-backed storage via a Durable Object Facet, with database inspection and reset controls available to users. -- evidence: [README.md#L21-L30](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L21-L30), [README.md#L60-L60](https://github.com/cloudflare/vibesdk/blob/9da158d82c597a0e8f4bf033cdccd1053fb6fb15/README.md#L60-L60)
More evidence: [full detail](vibesdk.detail.md)

Metadata and full claim list: [full detail](vibesdk.detail.md)
Human notes ([notes](vibesdk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
