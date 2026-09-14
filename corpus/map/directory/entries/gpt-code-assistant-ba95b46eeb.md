# Gpt-Code-Assistant (`gpt-code-assistant`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: narenmanoharan
- License: Apache-2.0
- Language: Python
- Interface: install=pip install gpt-code-assistant
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: False (reported)

Repository map entry: [narenmanoharan/gpt-code-assistant](../../repos/narenmanoharan/gpt-code-assistant.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Privacy-centric CLI for exploring/querying codebases via LLMs and vector embeddings; only sends code snippets to OpenAI when a query requires them. Uses GPT-4 to autonomously retrieve the most relevant local code snippets; terminal-only with no UI; language-agnostic.

(captured site page body (agents/gpt-code-assistant.md), not a verified repo-code finding)
The tool indexes a local codebase into vector embeddings and lets developers ask natural-language questions in the terminal, with GPT-4 retrieving the most relevant snippets and sending only those snippets to OpenAI, minimizing code exposure. It is terminal-only and language-agnostic, aimed at developers exploring unfamiliar or large codebases, generating documentation, or asking debugging questions without uploading their whole repository. Indexing happens locally, and only query-dependent snippets leave the machine, a deliberate design for proprietary codebases. The project saw 86 commits through August 2023 and then went quiet; it stands as an early example of retrieval-grounded code assistants, pre-dating the current agent wave.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gpt-code-assistant.md)
