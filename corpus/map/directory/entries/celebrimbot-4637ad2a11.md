# Celebrimbot (`celebrimbot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: GiacomoSaccaggi
- License: unknown
- Language: Kotlin
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: Local model with cloud escalation (LazyModelManager loads on demand, unloads after 60s idle)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Full multi-agent AI system that reads, writes, executes

(captured site page body (agents/celebrimbot.md), not a verified repo-code finding)
Celebrimbot is an IntelliJ plugin that embeds a multi-agent AI coding system directly in JetBrains IDEs. From a single chat panel the system reads project files, writes and modifies code, executes terminal commands, searches the web, and inspects git history, with an agentic loop that routes requests, executes tasks locally where possible, and escalates to cloud planning only when the task requires it, retrying failures automatically. Its architecture splits into three modules — a pure-Kotlin core, the IntelliJ plugin layer, and a standalone CLI/HTTP server — with a lazy model manager that loads the model on first use and unloads it after 60 seconds of inactivity to avoid taxing IDE memory. This targets JetBrains developers who want an agentic, tool-using assistant inside their IDE without the per-token subscription model of cloud-bound competitors. It is distributed free on the JetBrains Marketplace (created July 2026) under an Apache-2.0 license, with source available on GitHub.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/celebrimbot.md)
