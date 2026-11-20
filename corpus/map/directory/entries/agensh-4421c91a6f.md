# Agensh (`agensh`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: microsoft
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=git clone + Docker Compose on Linux (Docker Engine, Compose v2, systemd, cgroup v2; passwordless sudo for Docker); launch a team with python3 -m agensh.project run against a project.toml, selecting the per-worker harness with --agent-harness copilot|pi|codex|claude
- Model providers: GitHub Copilot CLI (default), Pi, OpenAI Codex, or Claude Code as the per-worker harness — each brings its own model provider (gpt-5.6-sol default via the gateway, per-worker models configurable)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [microsoft/agensh](../../repos/microsoft/agensh.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A decentralized multi-agent harness that scales one GitHub repository's work across up to 1,024 agents with no central orchestrator: workers discover and claim sub-tasks through a Gitea workspace, Mattermost messaging, and shared context, and the accompanying paper reports ProgramBench pass rates improving ~49% from 1 agent to 128.

(captured site page body (agents/agensh.md), not a verified repo-code finding)
Agensh is Microsoft's answer to the question of how much of a software project a team of agents can finish when nobody coordinates them centrally: it scales to 1,024 workers that each gather context, claim sub-tasks, take action, verify results, and merge progress asynchronously, connected by a shared workspace (Gitea), a messaging interface (Mattermost), and a shared-context mechanism adapted from DeLM. A run is defined by a TOML project file that names the upstream repo, the goal, acceptance commands, worker count, token budget, and coordination rules (planning worker, peer-review paths), and a team launches as a set of Docker Compose projects on one Linux host; the arXiv paper (2609.26781, September 2026) reports the experiments behind the design, including Pandoc test-pass rates rising from 33.89% with one agent to 55.06% with 1,024 under a six-hour budget. Each worker runs a real coding harness inside its container — Copilot CLI by default, with Pi, Codex, and Claude Code selectable at launch through adapters — so the harnesses bring their own models and tools, and Agensh contributes the coordination loop rather than the coding. The release ships the harness, the experiment launch scripts, a reproduction guide, and a software-project pack that ...
Sources: [published index (sha256:dbc3ded38a45)](https://alltheagents.org/agents.json); [site page @ 59c63290fc63](https://github.com/prime-radiant-inc/alltheagents.org/blob/59c63290fc6391f18c769634a4982f7f5e63fe99/agents/agensh.md)
