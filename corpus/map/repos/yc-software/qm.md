# yc-software/qm

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 361a6c0095dc @ da4f0a633de29ba8

## Summary (orientation draft, not independently verified)

QM is a multiplayer agent harness deployable to Slack and web, with per-scope workspaces, a headless TypeScript core on Node/Fastify backed by Postgres, and a versioned deployment-directory contract driven by the `qm` CLI. Evidence covers architecture, security postures, deployment tooling, and admin model verification; no eval harness or contributor test instructions appear in the slices. Evidence coverage: 96 of 108 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Contract v1 defines a committed, portable deployment directory whose sole interpreter is the qm CLI, which validates the same inputs it uses to render containers, task definitions, secret routing, and the agent-computer layer. -- evidence: [docs/deploy-directory.md#L3-L3](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L3-L3)
  - [observation/documented] The deployment config root requires contract: 1, orgId, publicUrl, target, and a services list including core; target is docker, fly, or aws, and unknown contract majors fail closed. -- evidence: [docs/deploy-directory.md#L24-L24](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L24-L24)
- components (2 claim(s)):
  - [observation/documented] A deployment runs three application workloads: core, web-ui (chat plus admin under /admin), and portal, which is the public entry point and hosts the optional built-in auth broker; Slack stays in core. -- evidence: [docs/combined-services.md#L3-L3](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/combined-services.md#L3-L3)
  - [observation/documented] The core runs TypeScript directly on Node with Fastify for HTTP; the Slack plugin uses Bolt, and the web UI builds with Vite and renders with Lit. -- evidence: [README.md#L87-L88](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L87-L88)
- design-choices (2 claim(s)):
  - [observation/documented] Each person and each room gets its own scoped memory, files, keychain view, permissions, crons, web apps, and durable sandbox, so employees work independently while collaborating in channels and projects. -- evidence: [README.md#L22-L23](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L22-L23), [README.md#L17-L20](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L17-L20)
  - [observation/documented] The core is generic: org-specific config, tools, skills, sandbox image, and infrastructure live in a deployment directory, and every substrate (harness, session store, sandbox, memory) sits behind an interface. -- evidence: [README.md#L90-L94](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L90-L94)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions are accepted as human-written text, not code — contributors describe changes informally in a .txt or .md file under adrs/, and maintainers handle implementation; vulnerabilities are reported privately. -- evidence: [README.md#L156-L160](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L156-L160)
  - [observation/documented] Repository development practice: the normal deployment gate order is check, doctor, plan, up --yes, then check --live, with infra build-image preceding plan on AWS MicroVM sandboxes. -- evidence: [docs/deploy-directory.md#L122-L122](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L122-L122)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
More evidence: [full detail](qm.detail.md)

Metadata and full claim list: [full detail](qm.detail.md)
Human notes ([notes](qm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
