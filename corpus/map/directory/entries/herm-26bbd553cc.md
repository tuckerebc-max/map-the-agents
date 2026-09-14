# herm (`herm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aduermael
- License: MIT
- Language: Go (CLI), Swift (iOS/macOS app), Rust (sandbox backend)
- Interface: platforms=CLI; install=curl -fsSL https://hermagent.com/install.sh | sh
- Model providers: Anthropic,OpenAI,Gemini,Grok,OpenRouter,Ollama,Azure OpenAI,Vertex AI,Bedrock
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aduermael/herm](../../repos/aduermael/herm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Model-agnostic, general-purpose AI coding agent that runs in containers by default; terminal-native, supports multiple isolation methods (Docker containers, in-process Unix-like sandboxes, host sandboxes like sandbox_exec/bubblewrap). Self-building dev environments scoped per project.

(captured site page body (agents/herm.md), not a verified repo-code finding)
herm is a coding agent built around the idea that isolation removes the need for constant permission prompts. The CLI runs on the host, but the agent's file edits and shell commands execute inside a Docker container scoped to the current working directory, with alternative isolation backends (in-process sandboxes, macOS sandbox-exec, Linux bubblewrap) for environments without Docker. When a project needs tooling that is not installed, herm writes a per-project Dockerfile itself and rebuilds the environment, so setup happens inside the agent loop rather than as a manual prerequisite. Models are provider-agnostic and can be mixed per role — one model for main coding, a cheaper one for exploration, another for vision — across Anthropic, OpenAI, Gemini, Grok, OpenRouter, and cloud endpoints. System prompts, skills, and tool implementations are all public in the repository, and a native iOS/macOS companion app with an on-device sandbox is in development.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/herm.md)
