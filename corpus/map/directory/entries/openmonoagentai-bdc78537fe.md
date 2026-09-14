# OpenMonoAgent.ai (`openmonoagentai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: StartupHakk
- License: AGPL-3.0
- Language: C# / .NET 10
- Interface: platforms=CLI; install=binary - one-command curl install script
- Model providers: Local llama.cpp (default), OpenAI (WIP), Anthropic (WIP), Ollama (WIP)
- Feature flags (directory-reported):
  - mcp_support: yes - stdio; auto-detects code-review-graph MCP server, configurable in settings.json (yes)
  - plugin_support: yes - Playbooks (YAML workflows) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes - 5 specialist sub-agents (Explore, Plan, Coder, Verify, general-purpose) (yes)
  - hooks: yes - pre/post hooks in 12-step tool pipeline (yes)
  - plan_mode: yes - plan-mode guard + dedicated Plan sub-agent (yes)

Repository map entry: [startuphakk/openmonoagent.ai](../../repos/startuphakk/openmonoagent.ai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 100% local-first coding agent bundled with llama.cpp in Docker; zero per-token cost, zero data egress. Auto-detects hardware (NVIDIA/CPU/Apple Silicon), supports distributed inference (agent on laptop, inference on remote GPU box), 20 built-in tools with 12-step pipeline, Docker sandboxing, Roslyn + LSP deep code intelligence, self-hosted SearXNG private web search, vision support, and a VS Code/Cursor extension. Philosophy: 'AI as infrastructure ...

(captured site page body (agents/openmonoagentai.md), not a verified repo-code finding)
Local-first coding agents usually stop at supporting whatever inference server the user happens to run, leaving setup as the user's problem. OpenMono bundles the whole stack: a .NET 10 CLI paired with a llama.cpp server in Docker that auto-detects NVIDIA GPUs, Apple Silicon, or plain CPU and ships Qwen model defaults tuned per backend, so one install script yields a working agent with no API keys and no network egress. Around the core it layers 20 built-in tools, five sub-agents, Docker-sandboxed execution, and Roslyn-powered code intelligence, with OpenAI/Anthropic/Ollama providers marked work-in-progress. A free relay at app.openmonoagent.ai enables distributed inference — the agent on a laptop, compute elsewhere — and iOS, Android, and VS Code/Cursor clients exist alongside the CLI. The project is a public beta under AGPL-3.0 with hardware demands (64 GB RAM recommended on Apple Silicon, 24 GB NVIDIA on Linux). Privacy-sensitive developers and offline environments are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openmonoagentai.md)
