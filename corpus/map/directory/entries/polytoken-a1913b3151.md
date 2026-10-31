# polytoken (`polytoken`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: ed3d
- License: Proprietary
- Language: unknown
- Interface: platforms=CLI; install=curl -fsS https://get.polytoken.dev | bash
- Model providers: Anthropic, OpenAI, OpenAI Codex, Azure OpenAI, plus any Anthropic- or OpenAI-compatible endpoint; the built-in catalog also covers z.ai, DeepSeek, Mistral, Moonshot/Kimi, Ollama Cloud, OpenRouter, DeepInfra, Fireworks AI, QwenCloud, OpenCode Go, Umans, Neuralwatt, and Kagi
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): A proprietary local-first coding agent that runs as a background daemon, so the terminal UI and any protocol client are only front ends onto the same session. Prompts, facets, skills, hooks, and themes all ship as plain files you can read, copy, and replace.

(captured site page body (agents/polytoken.md), not a verified repo-code finding)
Polytoken exists because its author wanted a coding harness that no vendor can take away, and the homepage argues that case in the first person rather than with a feature list. The shape of the product follows: a long-running daemon owns conversations, permissions, and tool execution on your machine, while the terminal UI attaches to it as a client, which is why a session survives a front end that dies and can be reattached later. Almost everything the model sees is editable text. Facets are Markdown personas that swap the system prompt and the tool set; the shipped plan facet investigates with read-only shell access, writes a handoff plan, runs a plan-reviewer, and asks before work moves into the execute facet; skills use the Agent Skills SKILL.md format and load from project or global directories; hooks fire on lifecycle events such as post_clear. A zero-config first run walks you through creating a provider and configuring web search, and the provider list is broad by design — the author's own setup orchestrates GLM-5.2 through z.ai over a pile of GPT 5.6 and DeepSeek V4 Flash models, and custom Anthropic- or OpenAI-compatible endpoints are first-class. It installs as a checksum-verified binary for Linux and macOS on amd64 and arm64 and is free under a proprietary end-user license, which makes it a fit for ...
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/polytoken.md)
