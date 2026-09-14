<div align="center">

<picture>
  <img src="./resources/logo/vt_code_adaptive.svg" alt="VT Code" width="300" />
</picture>

**Secure, open, universal terminal coding agent in Rust.**

[![License](https://img.shields.io/badge/License-MIT_OR_Apache--2.0-30363D?style=flat-square)](#license)
[![MSRV](https://img.shields.io/badge/MSRV-1.93.0-30363D?style=flat-square)](./docs/development/DEVELOPMENT_SETUP.md)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-BFB38F?style=flat-square)](https://agentskills.io/)
[![Agent Client Protocol](https://img.shields.io/badge/Agent_Client_Protocol-383B73?style=flat-square&logo=zedindustries&logoColor=white)](./docs/guides/zed-acp.md)
[![Model Context Protocol](https://img.shields.io/badge/Model_Context_Protocol-A63333?style=flat-square&logo=modelcontextprotocol&logoColor=white)](./docs/guides/mcp-integration.md)
[![Agent Plugins](https://img.shields.io/badge/Agent_Plugins-5865F2?style=flat-square)](./docs/guides/agent-plugins.md)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/vinhnx/VTCode)

</div>

> [!TIP]
> New here? Start with [Installation](./docs/installation/README.md), then
> [Getting Started](./docs/user-guide/getting-started.md).

<details>
<summary><strong>Contents</strong></summary>

- [Overview](#overview)
- [Why VT Code](#why-vt-code)
- [Quick start](#quick-start)
  - [1. Install](#1-install)
  - [2. Configure](#2-configure)
  - [3. Run](#3-run)
  - [WebMCP browser bridge (opt-in)](#webmcp-browser-bridge-opt-in)
- [What's inside](#whats-inside)
  - [Commands](#commands)
  - [Four pillars](#four-pillars)
    - [Agent core](#agent-core)
    - [Safety](#safety)
    - [Extensibility](#extensibility)
    - [Interface \& quality](#interface--quality)
- [Documentation](#documentation)
- [Development](#development)
- [Contributing](#contributing)
  - [Ways to contribute](#ways-to-contribute)
  - [Getting started](#getting-started)
  - [Contributors](#contributors)
- [Support](#support)
  - [Sponsorship](#sponsorship)
- [License](#license)

</details>

## Overview

<div align="center">

<img src="./resources/gif/vtcode.gif" alt="VT Code demo" width="60%" />
<br />
<em>Secure, open, universal.</em>

</div>

VT Code is an open-source terminal coding agent written in Rust: one static binary for quick interactive sessions and long-running autonomous work alike. No IDE required, no context left behind.

It is a **harness, not just an LLM wrapper**. The model reasons; the runtime supplies everything else — tools, context, sandboxing, state, and **verification**. That separation is what turns raw model output into safe, reviewable progress, entirely in your terminal.

> [!NOTE]
> **Status:** Active development. Local inference and some automation flows
> are experimental and may change between releases.

> [!TIP]
> **Behind the build:** [Building VT Code, a year in](https://huggingface.co/blog/vinhnx90/building-vtcode-a-year-in)
> covers harness design, evals, security, and lessons from a year of
> building.
>
> **Video companions:** [Podcast](https://www.youtube.com/watch?v=XLoswcd5rH0) ·
> [Video](https://www.youtube.com/watch?v=PvL_kPjgU6o).

## Why VT Code

Most agents are a model plus a tool call. That gets you a demo, not a
teammate. Real work breaks them in predictable ways, and VT Code answers
each one with a structural default, not a prompt tweak:

| When agents fail at…              | VT Code's structural answer                                                                                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sessions drift**                | Dynamic context assembly and auto-compaction keep long sessions grounded: the model reasons over current state, not a stale transcript. [Runtime guidance](./docs/development/runtime-guidance.md)                                                    |
| **Tool output floods the window** | Results are spooled to disk and summarized into the model's view on demand: signal stays in context, noise stays out. [Runtime guidance](./docs/development/runtime-guidance.md)                                                                      |
| **One unreviewed command**        | Sandboxed execution and approvals fail closed, with adversarial regression coverage for the attacks that actually happen: command injection, path/symlink escape, environment leakage. [Security model](./docs/development/COMMAND_SECURITY_MODEL.md) |
| **"Done" is a claim**             | Built-in evals with pass@k / pass^k metrics and environment-based verification: the agent's own report never counts as success. [Eval guide](./docs/guides/eval.md)                                                                                   |

None of this is emergent.
[`ThreadEvent`](./crates/common/vtcode-exec-events) is the single source of
truth for what happened during a run: one event stream feeds replay,
checkpoints, memory, and trajectory export. The
[agent loop contract](./docs/guides/agent-loop-contract.md) specifies how
turns, tool results, and recovery behave. The behavior you rely on is
written down, not accidental.

If you have been burned by agents that look impressive until something goes wrong, these are the defaults you were missing — built in, not bolted on. The [four pillars](#four-pillars) below cover the full surface, or skip to [Quick start](#quick-start) and see it work.

## Quick start

### 1. Install

```bash
curl -fsSL https://raw.githubusercontent.com/vinhnx/vtcode/main/scripts/install.sh | bash
# or: brew install vinhnx/tap/vtcode
# or: cargo install vtcode
```

### 2. Configure

```bash
cd path/to/your/project
vtcode init         # scaffolds config + AGENTS.md; review before committing
```

Set your API key: the TUI's `/secret` command stores it in your OS keyring
(never in a workspace `.env` or shell history), which is the most secure
option:

```bash
vtcode secret add openai   # headless; or run /secret add openai inside the TUI
```

`vtcode login` covers OAuth providers (ChatGPT, GitHub Copilot). Plain env vars and workspace `.env` still work, useful for CI. See [Getting started](./docs/user-guide/getting-started.md) for the credential resolution order.

> [!CAUTION]
> Never commit API keys or put them in `vtcode.toml`.

### 3. Run

```bash
vtcode                  # interactive TUI
vtcode ask "…"          # one-shot question, no session, no tools
vtcode exec "…"         # headless task with the full tool loop
vtcode continue         # resume the last session
```

That is the whole loop: install, init, run. See [Commands](#commands) for the complete CLI surface, and [Getting Started](./docs/user-guide/getting-started.md) for the full tour.

### WebMCP browser bridge (opt-in)

```bash
# Inside the TUI:
/webmcp pair <origin>

# Or serve a bounded workspace:
vtcode webmcp serve --origin <origin> --allowed-root <dir>
```

| Host       | Link                                                      |
| ---------- | --------------------------------------------------------- |
| Hosted app | <https://vtcode.vinhnx.chatgpt.site/>                     |
| Fallback   | <https://vinhnx.github.io/VTCode/>                        |
| User guide | [WebMCP user guide](./docs/user-guide/webmcp.md)          |
| Deployment | [WebMCP deployment reference](./docs/reference/webmcp.md) |

## What's inside

One static Rust binary: no runtime dependencies, no plugins to install,
nothing to wire up. Everything below ships in the default build.

**At a glance:** durable sessions · sandboxed execution · every major model ·
MCP, Skills & plugins · terminal-native TUI · built-in evals

### Commands

Bare `vtcode` opens the interactive TUI. Four subcommands cover most of the
work:

```bash
vtcode ask "explain Rc vs Arc"    # one-shot answer, no session, no tools
vtcode exec "refactor main.rs"    # headless task with the full tool loop
vtcode review                     # agent review of uncommitted changes
vtcode eval --suite suite.json    # verify behavior with pass@k metrics
```

A second tier handles session lifecycle and day-to-day operations:

| Command                              | Purpose                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------- |
| `vtcode continue`                    | Resume the last session, or fork it into a new one with `--session-id`                |
| `vtcode schedule`                    | Durable recurring prompts, by cron or one-shot; `install-service` survives restarts   |
| `vtcode secret`                      | Store provider API keys in your OS keyring, never in shell history or workspace files |
| `vtcode models`                      | Inspect, test, and compare providers and models                                       |
| `vtcode snapshots` / `vtcode revert` | List and roll back to workspace snapshots                                             |
| `vtcode tool-policy`                 | Allow or deny specific tools per workspace                                            |
| `vtcode trajectory`                  | Pretty-print run logs for debugging and audits                                        |

`vtcode analyze`, `vtcode check`, `vtcode schema tools`, `vtcode man`, and
`vtcode update` round out the operator surface. See `vtcode --help` for the
full list.

### Four pillars

| Pillar                                         | In one line                                               |
| ---------------------------------------------- | --------------------------------------------------------- |
| **[Agent core](#agent-core)**                  | The loop that turns model output into reviewable progress |
| **[Safety](#safety)**                          | Fail-closed execution, from sandbox to policy             |
| **[Extensibility](#extensibility)**            | Every model and protocol, no fork                         |
| **[Interface & quality](#interface--quality)** | Terminal-native UX, verified by default                   |

#### Agent core

_The loop that turns model output into reviewable progress._

- **Durable sessions:** checkpoints, auto-compaction, and spooled tool
  output keep hour-long runs grounded. `continue` resumes; `revert` rolls
  back to a snapshot. ([Runtime
  guidance](./docs/development/runtime-guidance.md) · [Session
  persistence](./docs/development/session-persistence.md))
- **One event contract:** a single `ThreadEvent` stream drives replay, the
  session store, memory, and trajectory export. One history, never divergent
  copies. ([Agent loop contract](./docs/guides/agent-loop-contract.md))
- **Planning & autonomy:** planning gates, propose/verify sub-agents,
  isolated worktrees, and cost guardrails. Autonomy is earned with evidence,
  not granted up front.
  ([Planning workflow](./docs/guides/planning-workflow.md) ·
  [Full automation](./docs/guides/full-automation.md))
- **Persistent memory:** gotchas, decisions, and library notes survive across
  runs, so the agent stops re-learning your project every session.
  ([Memory management](./docs/guides/memory-management.md))

#### Safety

_Fail closed by default, with coverage for the attacks that actually happen._

- **Sandboxed execution:** command policies and workspace approvals fail
  closed: injection, path/symlink escape, and environment leakage are blocked
  before anything runs. ([Security
  model](./docs/development/COMMAND_SECURITY_MODEL.md) ·
  [Permissions](./docs/guides/permissions.md))
- **Syntax-aware command parsing:** tree-sitter decomposes shell pipelines
  into sub-commands, so every piece is validated against policy, not just
  the first word. ([Tree-sitter
  integration](./docs/user-guide/tree-sitter-integration.md))
- **Hooks & tool policies:** lifecycle hooks gate tool calls before they
  run; per-tool allow/deny rules run common dev tools automatically and
  require confirmation for dangerous operations. ([Hooks
  guide](./docs/guides/hooks-guide.md) · [Execution
  policy](./docs/development/EXECUTION_POLICY.md))

#### Extensibility

_Plug in without forking; your setup survives upgrades._

- **Every model, one abstraction:** first-party APIs (OpenAI, Anthropic,
  Gemini, DeepSeek, Qwen, Mistral, xAI, …), gateways (OpenRouter, Vercel AI
  Gateway), OpenAI-compatible endpoints, and local inference (Ollama, LM
  Studio, llama.cpp) behind one streaming interface. Switching models never
  changes your workflow. ([Provider
  guides](./docs/providers/PROVIDER_GUIDES.md) · [Local
  models](./docs/guides/local-models.md))
- **Integrations:** MCP servers, Agent Skills, Agent Plugins, ACP (Zed),
  A2A, and the WebMCP browser bridge all attach to the core without patching
  it. ([MCP](./docs/guides/mcp-integration.md) ·
  [Skills](./docs/skills/SKILLS_GUIDE.md) ·
  [Plugins](./docs/guides/agent-plugins.md) ·
  [ACP](./docs/guides/zed-acp.md) · [A2A](./docs/a2a/a2a-protocol.md) ·
  [WebMCP](./docs/user-guide/webmcp.md))
- **Embed VT Code:** serve the agent over ACP for editors, expose an
  Anthropic-compatible API with `vtcode anthropic-api`, or proxy to the Codex
  app-server. VT Code works as a backend, not just a CLI.
  ([ACP](./docs/guides/zed-acp.md) ·
  [Protocols](./docs/protocols/OPEN_RESPONSES.md))

> [!TIP]
> Manage models with `vtcode models list|config|test|compare|info`, restrict
> providers per workspace via `providers_whitelist` in `vtcode.toml`, and
> control local inference with `/local` in the TUI.
> [Provider guides](./docs/providers/PROVIDER_GUIDES.md) are the source of
> truth for credentials and model defaults.

#### Interface & quality

_Native to the terminal, verified by default._

- **Terminal-native TUI:** WCAG AA-validated themes, markdown rendering,
  diff previews, and customizable output styles and status line. Built for
  the terminal, not ported to it. ([Interactive
  mode](./docs/user-guide/interactive-mode.md) · [Output
  styles](./docs/guides/output_styles.md))
- **Headless & automation:** `exec` mode, scheduled tasks, and sub-agents
  cover scripted, parallel, and unattended work.
  ([Exec mode](./docs/user-guide/exec-mode.md) ·
  [Scheduled tasks](./docs/user-guide/scheduled-tasks.md) ·
  [Sub-agents](./docs/user-guide/subagents.md))
- **Evals:** pass@k / pass^k metrics with environment-based verification.
  The agent's own report never counts as success.
  ([Eval guide](./docs/guides/eval.md))

> [!TIP]
> Optional search accelerators (ripgrep, ast-grep) install with
> `vtcode dependencies install search-tools`.

## Documentation

| Area    | Guides                                                                                                                                                                                                                                                                                   |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Start   | [Installation](./docs/installation/README.md) · [Getting started](./docs/user-guide/getting-started.md) · [Wiki](https://github.com/vinhnx/VTCode/wiki)                                                                                                                                  |
| Use     | [TUI](./docs/user-guide/interactive-mode.md) · [CLI](./docs/user-guide/commands.md) · [WebMCP](./docs/user-guide/webmcp.md) · [Automation](./docs/guides/full-automation.md) · [Planning](./docs/guides/planning-workflow.md) · [Configuration](./docs/config/CONFIG_FIELD_REFERENCE.md) |
| Extend  | [Skills](./docs/skills/SKILLS_GUIDE.md) · [Plugins](./docs/guides/agent-plugins.md) · [MCP](./docs/guides/mcp-integration.md) · [Editors (ACP)](./docs/guides/zed-acp.md)                                                                                                                |
| Operate | [Safety](./docs/security/SECURITY_MODEL.md) · [Protocols](./docs/protocols/OPEN_RESPONSES.md) · [Loop engineering](./docs/project/PLAN-loop-engineering.md) · [Architecture](./docs/ARCHITECTURE.md)                                                                                     |

The full catalog lives in the [Documentation Index](./docs/INDEX.md).

## Development

```mermaid
graph LR
    types --> config --> core --> tools --> agent --> TUI
```

Clone and run the fast gate:

```bash
git clone https://github.com/vinhnx/vtcode.git
cd vtcode
./scripts/run-debug.sh
./scripts/check-dev.sh   # fast gate: clippy, fmt, check
cargo nextest run        # tests (never `cargo test`)
```

Rust stable, edition 2024, MSRV 1.93. ~30 crates layered as
`types → config → core → tools → agent → TUI`, with `ThreadEvent` as the
authoritative runtime contract.

See [Development setup](./docs/development/DEVELOPMENT_SETUP.md) and
[Testing](./docs/development/testing.md).

## Contributing

### Ways to contribute

- **Security**: Found a vulnerability? Follow the [Security
  Policy](https://github.com/vinhnx/VTCode/security/policy).
- **Bug fixes and patches**: Small or large, every fix counts.
- **Documentation**: Guides, examples, and corrections help everyone.
- **Features and ideas**: Open an issue or start a discussion.
- **Code reviews and testing**: Trying things out and reporting breakage keeps the project healthy.

### Getting started

- Browse [good first issues](https://github.com/vinhnx/vtcode/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)
- Read [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for humans
- Check [AGENTS.md](./AGENTS.md) for AI agents

> [!NOTE]
> Small, focused PRs merge fastest. If you get stuck, open an issue for help.

### Contributors

Thank you to everyone who shaped VT Code.

<details>
<summary><strong>Show all contributors</strong></summary>

<div align="center">
  <a href="https://github.com/kernitus"><img src="https://avatars.githubusercontent.com/u/2789734?s=60" width="40" height="40" alt="@kernitus" title="@kernitus Main Contributor (52 commits)" style="border-radius: 50%; border: 2px solid #FFD700;" /></a>&nbsp;
  <a href="https://github.com/7jrxt42BxFZo4iAnN4CX"><img src="https://avatars.githubusercontent.com/u/72938937?s=60" width="40" height="40" alt="@7jrxt42BxFZo4iAnN4CX" title="@7jrxt42BxFZo4iAnN4CX Core contributor (44 commits) - subagents, hooks, config & TUI fixes (#737, #738, #740-#742+)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/oiwn"><img src="https://avatars.githubusercontent.com/u/398035?s=60" width="40" height="40" alt="@oiwn" title="@oiwn Core contributor (6 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/Sachin-Bhat"><img src="https://avatars.githubusercontent.com/u/25080916?s=60" width="40" height="40" alt="@Sachin-Bhat" title="@Sachin-Bhat Core contributor (3 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/chenrui333"><img src="https://avatars.githubusercontent.com/u/1580956?s=60" width="40" height="40" alt="@chenrui333" title="@chenrui333 Core contributor (3 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/gzsombor"><img src="https://avatars.githubusercontent.com/u/66230?s=60" width="40" height="40" alt="@gzsombor" title="@gzsombor Core contributor (2 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/leonj1"><img src="https://avatars.githubusercontent.com/u/5171829?s=60" width="40" height="40" alt="@leonj1" title="@leonj1 Core contributor (2 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/netbrah"><img src="https://avatars.githubusercontent.com/u/162479981?s=60" width="40" height="40" alt="@netbrah" title="@netbrah Core contributor (2 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/xcrong"><img src="https://avatars.githubusercontent.com/u/46434477?s=60" width="40" height="40" alt="@xcrong" title="@xcrong Core contributor (2 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/mouse-value-add"><img src="https://avatars.githubusercontent.com/u/263469348?v=4&s=60" width="40" height="40" alt="@mouse-value-add" title="@mouse-value-add Core contributor (2 commits)" style="border-radius: 50%; border: 2px solid #50C878;" /></a>&nbsp;
  <a href="https://github.com/raphamorim"><img src="https://avatars.githubusercontent.com/u/3630346?s=60" width="40" height="40" alt="@raphamorim" title="@raphamorim PR #708, rio-vt migration (1 commit)" style="border-radius: 50%; border: 2px solid #4A90D9;" /></a>&nbsp;
  <a href="https://github.com/nnfrog"><img src="https://avatars.githubusercontent.com/u/142202920?s=60" width="40" height="40" alt="@nnfrog" title="@nnfrog GHSA-r249-hpfx-x2w7 (security advisory)" style="border-radius: 50%; border: 2px solid #FF6B6B;" /></a>&nbsp;
  <a href="https://github.com/glmgbj233"><img src="https://avatars.githubusercontent.com/u/115564047?s=60" width="40" height="40" alt="@glmgbj233" title="@glmgbj233 GHSA-wqgw-crr5-cr2p (security advisory)" style="border-radius: 50%; border: 2px solid #FF6B6B;" /></a>&nbsp;
  <a href="https://github.com/EvoLinkAI"><img src="https://avatars.githubusercontent.com/u/253253881?s=60" width="40" height="40" alt="@EvoLinkAI" title="@EvoLinkAI Contributor (1 commit) - Evolink provider (#664)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/diegosouzapw"><img src="https://avatars.githubusercontent.com/u/8016841?s=60" width="40" height="40" alt="@diegosouzapw" title="@diegosouzapw Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/ericcurtin"><img src="https://avatars.githubusercontent.com/u/1694275?v=4&s=60" width="40" height="40" alt="@ericcurtin" title="@ericcurtin Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/ForrestThump"><img src="https://avatars.githubusercontent.com/u/44280834?s=60" width="40" height="40" alt="@ForrestThump" title="@ForrestThump Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/morler"><img src="https://avatars.githubusercontent.com/u/478444?s=60" width="40" height="40" alt="@morler" title="@morler Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/poelzi"><img src="https://avatars.githubusercontent.com/u/66107?s=60" width="40" height="40" alt="@poelzi" title="@poelzi Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/RobertBorg"><img src="https://avatars.githubusercontent.com/u/1288566?s=60" width="40" height="40" alt="@RobertBorg" title="@RobertBorg Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/Sanjays2402"><img src="https://avatars.githubusercontent.com/u/51058514?s=60" width="40" height="40" alt="@Sanjays2402" title="@Sanjays2402 Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/TuanLe-bk18"><img src="https://avatars.githubusercontent.com/u/222461688?s=60" width="40" height="40" alt="@TuanLe-bk18" title="@TuanLe-bk18 Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>&nbsp;
  <a href="https://github.com/uiYzzi"><img src="https://avatars.githubusercontent.com/u/40852301?s=60" width="40" height="40" alt="@uiYzzi" title="@uiYzzi Contributor (1 commit)" style="border-radius: 50%; border: 2px solid #B19CD9;" /></a>
</div>

</details>

## Support

### Sponsorship

VT Code is built and maintained in spare time. If it helped you ship or learn something, a [sponsorship](https://github.com/sponsors/vinhnx) keeps the project independent.

<div align="center">
  <a href="https://github.com/dnhn"><img src="https://avatars.githubusercontent.com/u/2561973" width="80" height="80" alt="@dnhn" style="border-radius: 50%" /></a>
  <a href="https://github.com/codemod"><img src="https://avatars.githubusercontent.com/u/78830094" width="80" height="80" alt="@codemod" style="border-radius: 50%" /></a>
  <a href="https://github.com/coderabbitai"><img src="https://avatars.githubusercontent.com/u/132028505" width="80" height="80" alt="@coderabbitai" style="border-radius: 50%" /></a>
  <a href="https://github.com/KhaiRyth"><img src="https://avatars.githubusercontent.com/u/273723951" width="80" height="80" alt="@KhaiRyth" style="border-radius: 50%" /></a>
</div>

<div align="center">

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-30363D?style=for-the-badge&logo=github-sponsors&logoColor=%23EA4AAA)](https://github.com/sponsors/vinhnx)
<a href="https://buymeacoffee.com/vinhnx"><img src="./resources/screenshots/qr_donate.png" alt="Buy Me a Coffee" width="100" /></a>

</div>

## License

First-party code is **MIT OR Apache-2.0**. See [LICENSE](LICENSE).
Third-party code keeps its original licenses: see[THIRD-PARTY-NOTICES](THIRD-PARTY-NOTICES).

<div align="right">

[Back to top](#readme)

</div>
