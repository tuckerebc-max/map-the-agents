# madarco/agentbox

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 138c1f585fdb @ a04bee36c7612b6b

## Summary (orientation draft, not independently verified)

AgentBox is an npm CLI that runs coding agents in isolated sandbox boxes on local Docker or cloud providers, with commands for lifecycle, access, sync, and checkpoints. Evidence is mostly README product documentation plus CLAUDE.md contributor guidance.

## Source coverage

Source coverage (partial): 3 of 35 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Multiple sandbox backends are supported: local Docker, remote Docker, Hetzner, Vercel, and E2B fully supported, with Daytona marked partial; each differs in base image source, snapshot support, and preview URL mechanism. -- evidence: [README.md#L88-L93](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L88-L93)
- design-choices (1 claim(s)):
  - [observation/documented] Git credentials stay on the local machine, and pushing to the remote repository requires permission requests, as a safety design. -- evidence: [README.md#L24-L28](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L24-L28)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: build from source by cloning the repo, running `pnpm install && pnpm build`, then invoking `node apps/cli/dist/index.js --help`; the full dev workflow and smoke tests live in docs/development.md. -- evidence: [README.md#L174-L174](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L174-L174), [README.md#L168-L172](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L168-L172)
  - [observation/documented] Repository development practice: tests use vitest with default discovery and must stay pure (no docker, no network); integration testing is currently manual, and linting uses eslint plus prettier via `pnpm lint`/`pnpm format`. -- evidence: [CLAUDE.md#L62-L71](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/CLAUDE.md#L62-L71)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI exposes commands grouped as create/run (create, claude), access (url, screen, code, shell, open, logs, dashboard), inspect (list, status, top), lifecycle (start, stop, destroy, pause/unpause), sync (download, cp, checkpoint), and advanced (wait, prune, self-update, config, relay, app). -- evidence: [README.md#L118-L124](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L118-L124), [README.md#L147-L152](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L147-L152), [README.md#L128-L130](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L128-L130), [README.md#L141-L143](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L141-L143), [README.md#L134-L137](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L134-L137), [README.md#L113-L114](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L113-L114)
  - [observation/documented] `agentbox claude` creates a sandboxed box and launches Claude Code in a detachable tmux session, and `agentbox attach 1` reconnects to a box later. -- evidence: [README.md#L48-L48](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L48-L48), [README.md#L113-L114](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L113-L114)
- memory-state (1 claim(s)):
  - [observation/documented] Boxes support checkpoints: new boxes can start from a previous checkpoint in under a second, boxes auto-pause when idle to save resources, and `agentbox checkpoint` lists/creates project checkpoints. -- evidence: [README.md#L24-L28](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L24-L28), [README.md#L141-L143](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L141-L143)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Requirements are macOS (arm64 or Intel) or Linux, Docker Desktop or OrbStack, and Node >=20.10; the first create/claude builds a ~1 GB agentbox/box:dev image once, and portless gives box web apps consistent URLs. -- evidence: [README.md#L83-L84](https://github.com/madarco/agentbox/blob/138c1f585fdbeddff392bbf76086b1d8382a998e/README.md#L83-L84)
More evidence: [full detail](agentbox.detail.md)

Metadata and full claim list: [full detail](agentbox.detail.md)
Human notes ([notes](agentbox.notes.md), never overwritten by build)

[Back to map index](../../index.md)
