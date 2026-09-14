# getpaseo/paseo

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d1b705a0cd91 @ 412941229c6b93c1

## Summary (orientation draft, not independently verified)

Paseo is a self-hosted interface for running coding agents (Claude Code, Codex, Copilot, OpenCode, Pi) via a local daemon with desktop, mobile, web, and CLI clients, plus a TypeScript SDK and plugin system. Evidence: 3 of 52 candidate files stored (README.md, AGENTS.md, CLAUDE.md); 49 omitted by file/byte budget, including SECURITY.md, CONTRIBUTING.md and all of docs/; selection incomplete.

## Source coverage

Source coverage (partial): 3 of 52 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The monorepo includes packages/server (daemon with agent orchestration, WebSocket API, MCP server), packages/app (Expo client), packages/cli, packages/desktop (Electron), packages/relay, and packages/website. -- evidence: [README.md#L171-L176](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L171-L176), [CLAUDE.md#L11-L16](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/CLAUDE.md#L11-L16)
- design-choices (2 claim(s)):
  - [observation/documented] Paseo is self-hosted: agents run on the user's own machine with their existing dev environment, tools, configs, and skills. -- evidence: [README.md#L44-L48](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L44-L48)
  - [observation/documented] The README states Paseo has no telemetry, tracking, or forced log-ins, describing a privacy-first stance. -- evidence: [README.md#L44-L48](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L44-L48)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors must run typecheck and lint after every change, run only the specific vitest file they changed (never the full suite locally), and push to CI for full-suite verification. -- evidence: [CLAUDE.md#L118-L141](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/CLAUDE.md#L118-L141), [CLAUDE.md#L93-L103](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/CLAUDE.md#L93-L103)
- skills-patterns (1 claim(s)):
  - [observation/documented] Paseo ships skills installable via `npx skills add getpaseo/paseo`, including /paseo-handoff, /paseo-advisor, and /paseo-committee for agent-to-agent delegation and review patterns. -- evidence: [README.md#L163-L165](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L163-L165), [README.md#L157-L159](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L157-L159), [README.md#L155-L155](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L155-L155)
- interfaces (4 claim(s)):
  - [observation/documented] Paseo exposes a CLI with commands like `paseo run --provider`, `paseo ls`, `paseo attach`, and `paseo send` for launching and interacting with agents from the terminal. -- evidence: [README.md#L113-L113](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L113-L113), [README.md#L119-L121](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L119-L121), [README.md#L115-L117](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L115-L117)
  - [observation/documented] The CLI can target a remote daemon with `--host`, where `--cwd` is interpreted as a path on that host. -- evidence: [README.md#L124-L125](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L124-L125)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] A local daemon manages the coding agents, and clients (desktop, mobile, web, CLI) connect to it; agents can also run in parallel on the user's machines. -- evidence: [README.md#L61-L61](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L61-L61), [README.md#L42-L42](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L42-L42)
- tools-permissions (1 claim(s)):
  - [observation/documented] Plugins run with access to the daemon machine and connected clients, so users are warned to install only code they trust. -- evidence: [README.md#L55-L57](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L55-L57)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Paseo requires at least one external agent CLI (Claude Code, Codex, GitHub Copilot, OpenCode, or Pi) installed and configured with credentials. -- evidence: [README.md#L67-L71](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L67-L71), [README.md#L65-L65](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L65-L65)
More evidence: [full detail](paseo.detail.md)

Metadata and full claim list: [full detail](paseo.detail.md)
Human notes ([notes](paseo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
