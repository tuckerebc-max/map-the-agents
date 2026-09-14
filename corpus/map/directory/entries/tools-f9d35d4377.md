# Tools (`tools`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: buildownai
- License: NOASSERTION
- Language: TypeScript
- Interface: platforms=IDE; install=Uses Bun as package manager (bun.lockb present); no explicit install instructions
- Model providers: Ollama
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [buildownai/tools](../../repos/buildownai/tools.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): NOTE: Not a coding agent harness. Monorepository of simple LLM-based AI tools serving as companion code/examples for the BuildOwn.AI book. Includes a chapter_summarizer tool. Very early stage (3 commits, 1 star).

(captured site page body (agents/tools.md), not a verified repo-code finding)
The repository supports the BuildOwn.AI book by making its examples runnable: the book teaches building with LLMs, and this repo holds the corresponding simple tool implementations, organized by chapter for readers to follow along. Its only substantive tool, chapter_summarizer, sits alongside a shared utilities directory in a small TypeScript project managed with Bun and linted with Biome, with a purchase link back to the book itself. Readers of the book are the intended users; nobody installs it as software. With three commits, one star, and no releases, it is effectively a static companion artifact.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tools.md)
