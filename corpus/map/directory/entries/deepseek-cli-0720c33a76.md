# deepseek-cli (`deepseek-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: holasoymalva
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g run-deepseek-cli
- Model providers: DeepSeek (Coder 1.3B, 6.7B, 33B) via local Ollama or DeepSeek cloud API
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [holasoymalva/deepseek-cli](../../repos/holasoymalva/deepseek-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Command-line AI coding assistant powered by DeepSeek Coder models; supports both local mode (via Ollama, free & private) and cloud mode (API key). Features code completion/generation across 100+ languages, repository-level code understanding, refactoring/migration, debugging/code review, project scaffolding, and an interactive REPL with syntax highlighting and session history.

(captured site page body (agents/deepseek-cli.md), not a verified repo-code finding)
deepseek-cli adapts the Gemini CLI codebase to DeepSeek Coder models, giving terminal users code generation, repository-level analysis, refactoring, debugging, and project scaffolding across roughly 100 languages. Its local mode runs DeepSeek Coder 1.3B/6.7B/33B through Ollama at no cost and entirely on-device, which the README recommends over the cloud mode that uses a DeepSeek platform API key. The interactive REPL supports session history, file-context inclusion, and model switching, and the project is MIT-licensed TypeScript installable via npm. With 14 commits and no releases since its initial push, it is best understood as a community fork demonstrating the Gemini CLI architecture on DeepSeek models rather than a product under active development.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepseek-cli.md)
