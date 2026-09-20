# caveman-code (`caveman-code`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: JuliusBrussee
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Anthropic, OpenAI, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, DeepSeek, Google Gemini, GitHub Copilot, Claude Pro/Max, ChatGPT Plus/Pro, and more (20+)
- Feature flags (directory-reported):
  - mcp_support: yes — full, Claude Code-compatible superset; transports: stdio, Streamable HTTP, in-process; OAuth 2.1 + PKCE (yes)
  - plugin_support: yes — plugin marketplace via caveman plugin command (yes)
  - claude_code_plugin: no (no)
  - subagents: yes — up to 7 parallel, worktree-isolated subagents; 5 ship by default; triggered via Task tool (yes)
  - hooks: yes — identical to Claude Code hooks; run as observers, never block (yes)
  - plan_mode: yes — /plan toggles read-only mode (model restricted to read/grep/find/ls); /act executes the saved plan (yes)

Repository map entry: [juliusbrussee/caveman-code](../../repos/juliusbrussee/caveman-code.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
caveman-code is a terminal coding agent forked from Mario Zechner's pi, modified so that every layer of the interaction pipeline compresses tokens: the model's own replies are constrained into terse '
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
