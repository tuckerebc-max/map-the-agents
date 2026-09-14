# HarnessRouter (`harnessrouter`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: harnessrouter
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI, Web; install=docker run harnessrouter/harnessrouter (console on port 3000, loopback-bound by default)
- Model providers: BYOK — delegates to the installed harnesses (Codex, Claude Code, Hermes, Pi, DeepSeek Harness, OpenCode)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [harnessrouter/harnessrouter](../../repos/harnessrouter/harnessrouter.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): The reference implementation of the Unified Harness Protocol (UHP), an open standard: it runs multiple agent harnesses through one OpenAI Responses-compatible API with sessions, streaming, cancellation, idempotency, and failure handling, so any harness is callable uniformly. Bring your own keys, no account, no cloud, no telemetry.

(captured site page body (agents/harnessrouter.md), not a verified repo-code finding)
HarnessRouter Community Edition is the self-hosted Apache-2.0 sibling of the hosted HarnessRouter Cloud, and its purpose is to make every agent CLI look identical to callers. The Docker container installs Codex, Claude Code, Hermes, Pi, DeepSeek Harness, and OpenCode on first run (each under its own upstream license — the CLIs are not redistributed), then exposes them through a single OpenAI Responses-compatible API at /v1/responses with harness CRUD, sessions, streaming, cancellation, idempotency, and failure handling, plus a thin web console over the same API. The project is also the reference implementation of the Unified Harness Protocol, an open standard (spec version 2026-08-11) that this repo passes at conformance class Full. Sessions run as real POSIX workspaces with bash and git, isolated per session, with state in SQLite on a Docker volume; it is built for teams that want to script or productize multiple harnesses behind one gateway on their own infrastructure.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/harnessrouter.md)
