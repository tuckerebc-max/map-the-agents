# choiyounggi/cliclaw

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6a5e048a5abf @ 16445cc7ff31dba2

## Summary (orientation draft, not independently verified)

cliclaw is a macOS Bun daemon that turns a Telegram chat into a remote control for local coding CLIs (Claude Code, Codex, Pi, Gemini), with per-chat sessions, a confirm-gate safety mode, launchd auto-start, and streaming responses. Evidence is README/DEVELOPMENT/CONTRIBUTING documentation only; no source code slices are present.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The codebase is organized as a bot.ts daemon entry point, a cli.ts entry point, and lib/ modules for audit logging, confirm IPC, danger patterns, launchd, streaming, rate limiting, and agent path resolution. -- evidence: [DEVELOPMENT.md#L26-L53](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/DEVELOPMENT.md#L26-L53)
- design-choices (2 claim(s)):
  - [observation/documented] Agent paths are auto-discovered at startup in three passes (well-known dirs, newest nvm node's bin, login-shell PATH) with no absolute paths in config.json; undetected agents are skipped. -- evidence: [README.md#L181-L181](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L181-L181), [README.md#L176-L179](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L176-L179)
  - [observation/documented] Secrets written to bot.log/bot.err are pre-redacted, covering Telegram bot tokens, npm tokens, GitHub PATs, and exact matches of the live config token. -- evidence: [README.md#L221-L225](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L221-L225)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors must pass bun test (222+ cases) and tsc --noEmit, add unit tests for new features, discuss changes over 30 lines via issue/RFC first, and PRs are validated by a GitHub Actions Test workflow on macOS-latest. -- evidence: [CONTRIBUTING.md#L20-L25](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/CONTRIBUTING.md#L20-L25), [CONTRIBUTING.md#L7-L14](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/CONTRIBUTING.md#L7-L14)
  - [observation/documented] Repository development practice: coding conventions require Bun 1.x runtime with zero runtime dependencies (devDeps only), strict TypeScript, lib/<feature>.ts module separation, vitest-API tests in __tests__/, and no direct console.log. -- evidence: [CONTRIBUTING.md#L29-L35](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/CONTRIBUTING.md#L29-L35)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes CLI commands including init, start, install-launchd, uninstall-launchd, upgrade, version, logs (--audit/--err), doctor, and help. -- evidence: [README.md#L113-L123](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L113-L123)
  - [observation/documented] In Telegram, slash commands switch the active agent, show status/health, stop jobs, reset sessions, toggle safety, set model overrides, and toggle Claude plan mode; other text or photos are sent as prompts. -- evidence: [README.md#L127-L140](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L127-L140)
- memory-state (1 claim(s)):
  - [observation/documented] All state lives under ~/.cliclaw/ (relocatable via CLICLAW_HOME): config.json, a bot.pid single-instance lock, safety.json, per-chat session metadata and per-agent session directories, logs, and a .sock confirm-gate IPC socket. -- evidence: [README.md#L167-L167](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L167-L167), [README.md#L147-L147](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L147-L147), [README.md#L149-L165](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L149-L165)
- orchestration (1 claim(s)):
  - [observation/documented] The daemon is built for unattended operation: single-instance lock, dormant retry every 60s on broken config instead of crash looping, graceful shutdown notifying chats, process-group kills on /stop, and retention sweeps of stale uploads/sessions (default 30 days). -- evidence: [README.md#L236-L245](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L236-L245)
More evidence: [full detail](cliclaw.detail.md)

Metadata and full claim list: [full detail](cliclaw.detail.md)
Human notes ([notes](cliclaw.notes.md), never overwritten by build)

[Back to map index](../../index.md)
