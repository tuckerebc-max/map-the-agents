# Koder Feature Guide

This guide is the topic map for the `koder` CLI. Start here when you want to know which part of the product to use, then follow the deeper guide for the exact commands and setup.

## Main Guides

| Topic | Guide | Use It For |
|---|---|---|
| First run | [Getting Started](getting-started.md) | Install Koder, configure a model, start a session, and run a safe first task. |
| Terminal usage | [Interactive TUI](interactive-tui.md) | Prompt controls, slash commands, mentions, shell mode, history, status output, and voice input. |
| Models and config | [Configuration Guide](configuration.md) | API keys, OAuth providers, base URLs, reasoning effort, settings bundles, MCP config, and provider examples. |
| Sessions and memory | [Sessions and Memory](sessions-and-memory.md) | Named sessions, goals, scheduled loops, resume, clear, compact, rewind, memory files, thinkback, and AutoDream. |
| Agents and teams | [Agents and Teams](agents-and-teams.md) | Project agents, background subagents, `task_delegate`, `/fork`, `/peers`, teammate modes, and shared team memory. |
| Engineering workflows | [Workflows](workflows.md) | Reviews, security review, planning, Git readiness, PR comments, GitHub Actions setup, and release notes. |
| Extension system | [Skills, Plugins, and MCP](extensions.md) | Skills, verifier skills, plugins, MCP servers, channels, and Magic Docs. |
| Permissions and data | [Permissions and Privacy](permissions-and-privacy.md) | Tool approvals, sandbox policy, managed settings, workspace directories, local paths, and privacy boundaries. |
| Event hooks | [Hooks](hooks.md) | Run your own commands on session, tool, permission, compaction, and agent lifecycle events. |
| Shell sandboxing | [Sandbox Guide](sandbox.md) | Backend selection, real backend status, shell isolation boundaries, backend setup, and troubleshooting. |
| Voice input | [Voice Mode](voice-mode.md) | Dictation controls and provider-specific speech-to-text configuration. |
| Full command list | [Command Reference](commands.md) | Complete slash-command catalog with examples. |

## Runtime Modes

| Mode | Command | When To Use It |
|---|---|---|
| Interactive | `koder` | Daily coding work with live output, slash completion, file mentions, shell mode, and persistent context. |
| Single prompt | `koder "fix this test"` | One task from your shell while still recording the turn in the selected session. |
| Print mode | `koder --print "summarize"` | Script-friendly output. Pair with `--output-format json` or `stream-json` for automation. |
| Named session | `koder -s my-project` | Keep a project or topic in a durable conversation thread. |
| Resume | `koder --resume` or `koder --continue` | Continue a previous local session. |
| Bare mode | `koder --bare` | Start without hooks, skills, plugins, MCP, memory, or project `AGENTS.md` context. |

## Capability Map

Koder is organized around a few everyday jobs:

- Talk to models from OpenAI, Anthropic, Google, GitHub Copilot, OAuth-backed subscriptions, Azure, OpenRouter, and other LiteLLM providers.
- Work in a terminal TUI with streaming output, command completion, shell mode, reverse search, file mentions, status output, usage tracking, and optional voice dictation.
- Keep durable local context through SQLite-backed sessions, named sessions, session goals, exports, summaries, memory files, compaction, rewind, and thinkback.
- Track long-running work with `/goal` and run recurring local prompts with `/loop` and `/schedule`.
- Edit and inspect repositories with file tools, search tools, shell tools, Git helpers, review commands, and project instructions from `AGENTS.md`.
- Delegate work to local background agents and teams while keeping teammate state, task records, and memory under Koder-owned local paths.
- Extend the runtime with project skills, user skills, plugins, MCP servers, session channels, and Magic Docs.
- Control risk with explicit permission rules, sandbox policy, managed settings, allowed workspace roots, and local privacy diagnostics.

## Choosing Your Path

| I want to... | Start with |
|---|---|
| Try Koder safely in a new repository | [Getting Started](getting-started.md), then `/onboarding`, `/status`, `/permissions`, and a read-only prompt. |
| Understand the terminal UI | [Interactive TUI](interactive-tui.md), then `/help`, `/keybindings`, `/theme`, `/voice status`, and shell mode. |
| Configure a model or endpoint | [Configuration Guide](configuration.md), then `/model`, `/effort`, `/reasoning`, and `koder config show`. |
| Keep project context across sessions | [Sessions and Memory](sessions-and-memory.md), then `/session`, `/goal`, `/resume`, `/compact`, `/memory`, and `/thinkback`. |
| Review or prepare a branch | [Workflows](workflows.md), then `/diff`, `/review`, `/security-review`, and `/commit`. |
| Run recurring checks | [Sessions and Memory](sessions-and-memory.md), then `/loop`, `/schedule`, and `/tasks`. |
| Add local domain knowledge | [Skills, Plugins, and MCP](extensions.md), then `/skills`, `/init-verifiers`, `/plugin`, and `/mcp`. |
| Run parallel investigations | [Agents and Teams](agents-and-teams.md), then `/fork`, `/agents`, `/peers`, and `/tasks`. |
| Audit data access and command risk | [Permissions and Privacy](permissions-and-privacy.md) and [Sandbox Guide](sandbox.md). |
| Automate actions on session or tool events | [Hooks](hooks.md), then `/hooks` to inspect the loaded configuration. |

## Common Starting Points

Use these commands when you are exploring a new workspace:

```bash
koder /onboarding
koder /status
koder /model
koder /files
koder /permissions
koder /skills
koder /agents
koder /goal
```

Use these commands when you are already in a coding flow:

```bash
koder /diff
koder /review
koder /security-review
koder /commit
koder /usage
koder /memory
koder /peers
koder /loop
```

Use these commands when you are setting up the runtime:

```bash
koder config show
koder auth login google
koder auth login claude
koder mcp list
koder plugin list
koder /voice status
```
