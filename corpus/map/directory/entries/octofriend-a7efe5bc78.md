# Octofriend (`octofriend`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: synthetic-lab
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install --global octofriend
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [synthetic-lab/octofriend](../../repos/synthetic-lab/octofriend.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Ships open-sourced, custom-trained autofix models (diff-apply and fix-json on Hugging Face) that repair mangled JSON tool calls and bad diffs from any coding model — plus zero telemetry and mid-conversation model switching.

(captured site page body (agents/octofriend.md), not a verified repo-code finding)
Octofriend is a terminal coding assistant built around tolerating weak or eccentric models rather than assuming a frontier provider. Two fine-tuned open-source models automatically repair the broken tool calls and malformed diffs that smaller models produce, so users can run cheaper or local models without the loop collapsing. It works with any OpenAI- or Anthropic-compatible API plus local runtimes, and models can be swapped mid-conversation when one gets stuck. Rules files, session resume, image attachments, Docker sandboxing, MCP servers, and automatic LSP integration round out the feature set. The project is MIT-licensed with a zero-telemetry privacy stance and recommends its own zero-data-retention Synthetic provider.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/octofriend.md)
