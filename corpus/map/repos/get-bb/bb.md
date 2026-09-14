# get-bb/bb

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d89160eb8c69 @ 3b3429692f6052ea

## Summary (orientation draft, not independently verified)

bb is an agentic IDE distributed as the bb-app npm package and a desktop app, with desktop/web/CLI/HTTP surfaces, threads, plugins, and a published plugin SDK. Evidence covers product interfaces, dependencies, telemetry, platform limits, and extensive release/build development workflows. Evidence coverage: 152 of 328 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 29 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Production runs send anonymous usage telemetry (app starts, thread and message counts, plugin installs) with a random per-install id; development/source runs never send, and BB_TELEMETRY=false opts out. -- evidence: [README.md#L85-L93](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L85-L93)
- design-choices (1 claim(s)):
  - [observation/documented] bb is described as an agentic IDE that builds itself, able to control, customize, and automate itself as groundwork for a user's own software factory. -- evidence: [README.md#L14-L15](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L14-L15)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: the dev loop uses pnpm dev (Vite with proxied API/WebSocket traffic and per-checkout data dirs under ~/.bb-dev) and pnpm start:worktree to test the production bundle without switching to production data or ports. -- evidence: [README.md#L103-L109](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L103-L109), [README.md#L99-L101](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L99-L101), [README.md#L114-L116](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L114-L116), [README.md#L111-L112](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L111-L112)
  - [observation/documented] Repository development practice: releases ship two outputs from one commit — the bb-app npm package via publish-bb-app.yml and the desktop app via build-desktop.yml — and a release is not complete until both are published at the same locked version. -- evidence: [docs/bb-release-process.md#L11-L16](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/docs/bb-release-process.md#L11-L16)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product exposes a desktop app, web app, CLI, and HTTP API as first-class ways to drive bb, with work running in threads that can be followed live, steered, or handed off to another agent. -- evidence: [README.md#L17-L19](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L17-L19)
  - [observation/documented] Running via npx serves a web interface at http://localhost:38886. -- evidence: [README.md#L55-L55](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L55-L55), [README.md#L51-L53](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L51-L53)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] bb depends on native add-ons including better-sqlite3, node-pty, and @parcel/watcher built by npm install scripts; npm 12+ blocks those scripts by default, requiring --allow-scripts. -- evidence: [README.md#L63-L65](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L63-L65), [README.md#L244-L247](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L244-L247), [README.md#L67-L69](https://github.com/get-bb/bb/blob/d89160eb8c69c1e3ebc2ba2514f1711af8d7c506/README.md#L67-L69)
- limitations (3 claim(s)):
More evidence: [full detail](bb.detail.md)

Metadata and full claim list: [full detail](bb.detail.md)
Human notes ([notes](bb.notes.md), never overwritten by build)

[Back to map index](../../index.md)
