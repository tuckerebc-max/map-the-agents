# Omnigent (`omnigent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: omnigent-ai
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI, IDE, Web; install=pip
- Model providers: Anthropic, OpenAI, OpenRouter, LiteLLM, Ollama, vLLM, Azure, Databricks, Amazon Bedrock, Google Vertex AI
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [omnigent-ai/omnigent](../../repos/omnigent-ai/omnigent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source meta-harness providing harness-agnostic orchestration over multiple AI coding agents (Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, custom agents). Mix agents from different vendors in the same session -- ask one to review another's work. Any-device real-time sync across terminal, browser, phone, desktop app. Multi-user collaboration with shareable live sessions. Cloud sandbox execution (Modal, E2B, Daytona, Kubernetes, Databricks). Stackable policy/governance ...

(captured site page body (agents/omnigent.md), not a verified repo-code finding)
Omnigent provides a uniform orchestration layer over existing coding agents, letting one session supervise a Claude Code instance while an OpenCode agent reviews its output. Harnesses swap without rewriting work, and custom agents are declared in YAML with tools of type mcp, type agent, or plain Python functions. Policies stack at server, agent, or session level for approve-before-shell, tool-call caps, and spend budgets, with OS-level sandboxing via bwrap or seatbelt. Sessions sync across terminal, browser, and phone, with cloud sandboxes on Modal, E2B, Kubernetes, and others. Credentials can be API keys, coding-plan subscriptions, or gateway base URLs, switchable mid-session. The project is in alpha with a large contributor base and permissive Apache-2.0 licensing.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/omnigent.md)
