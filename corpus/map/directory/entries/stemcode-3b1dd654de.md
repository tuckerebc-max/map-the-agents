# StemCode (`stemcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: rizwan3d
- License: Apache-2.0
- Language: C# / .NET
- Interface: platforms=CLI, Desktop, IDE; install=Desktop app from GitHub Releases; CLI via install script (curl/PowerShell), npm/pnpm/bun, or NuGet
- Model providers: OpenAI, ChatGPT Plus/Pro sign-in, Anthropic Claude Pro/Max sign-in, GitHub Copilot sign-in, OpenRouter, OpenCode Zen, Kilo Code, Cerebras, Groq, DeepSeek, Google AI Studio, Ollama, LM Studio, Ollama Cloud, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [rizwan3d/stemcode](../../repos/rizwan3d/stemcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first AI coding agent for desktop, terminal, editor (VS Code, Visual Studio, JetBrains), and CI workflows. Works inside a real local repository (not a detached chat sandbox), keeps the human in control with approval prompts/permissions/profiles, stores reusable commands and team memory in versionable .stemcode/ files, reuses the same agent across desktop/CLI/IDE/CI. Profiles include planning, implementation, review, exploration, and delegated work ...

(captured site page body (agents/stemcode.md), not a verified repo-code finding)
StemCode is built around operating inside a real local repository rather than a detached chat sandbox: repository-aware search, LSP symbol intelligence, and graph-aware indexing feed surgical tracked edits (patches, insertions, search/replace) with undo/redo, while permission rules and approval prompts gate sensitive actions. The same engine ships as a desktop app, a CLI, editor extensions, and CI jobs, so the agent that plans locally can also run in GitHub Actions or GitLab CI. Profiles switch behavior between implementation, planning, review, and exploration postures, subagents take delegated tasks in independent contexts, and slash commands plus project memory persist in .stemcode. Model access is deliberately broad, from subscription sign-ins (ChatGPT, Claude, Copilot) to OpenRouter, Ollama, LM Studio, and any OpenAI-compatible endpoint. It is Apache-2.0 and free, positioned for developers who want agent assistance without their code leaving the machine.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/stemcode.md)
