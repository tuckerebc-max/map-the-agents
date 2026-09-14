# Translator (`translator`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: unknown
- Language: Python
- Interface: platforms=CLI; install=pip install
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/translator](../../repos/2389-research/translator.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM-powered document translation CLI that uses a multi-stage pipeline (translate, edit, critique/revise) with special handling for markdown + YAML frontmatter. Uses OpenAI's API with tiktoken for token management and pycountry for language codes.

(captured site page body (agents/translator.md), not a verified repo-code finding)
Translator is an LLM-powered document translation CLI, not a coding agent. It runs documents through a multi-stage pipeline — translate, edit, then critique and revise — so a draft is not the final output, and it has special handling for markdown with YAML frontmatter so structured metadata survives translation intact. It talks to OpenAI's API, uses tiktoken for token management, and pycountry for language codes. The audience is anyone who needs high-quality, pipeline-driven document translation from the command line with their own OpenAI key, and it is listed here because it is a 2389-research tool that is not an agent and should not be mistaken for one.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/translator.md)
