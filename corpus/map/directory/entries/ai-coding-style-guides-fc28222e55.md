# AI-Coding-Style-Guides (`ai-coding-style-guides`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: lidangzzz
- License: Apache-2.0
- Language: TOML, JavaScript, Markdown
- Interface: platforms=IDE; install=Copy AI_Coding_Style_Guide_prompts.toml into your prompt management system, or load via Python toml.load()
- Model providers: Any (model-agnostic style guide)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [lidangzzz/ai-coding-style-guides](../../repos/lidangzzz/ai-coding-style-guides.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 'The First AI Coding Style Guide' — coding style guidelines designed specifically for AI-assisted coding (vibe coding/SWE agents) to maximize code compression and reduce token usage. Defines 8 compression levels from basic whitespace removal to advanced refactoring. Demonstrates compressing the KMP algorithm from 1,216 to 283 characters (23.3% of original) while maintaining functionality.

(captured site page body (agents/ai-coding-style-guides.md), not a verified repo-code finding)
Context windows fill up fast, and this project argues the fix is to write code compressed in the first place rather than to compress it after the fact. The guide supplies a TOML prompt file with eight levels, from whitespace removal through identifier shortening and comment stripping to aggressive refactoring, always preserving exported names so public APIs stay readable. Correctness is delegated to unit tests rather than human review, on the premise that LLMs read compressed code fine and can re-expand it for humans on demand. Worked examples show a KMP implementation at 23.3% of its original size (outperforming JSCompress) and a C++ JSON parser nearly halved, with the LLM successfully explaining the compressed output. Teams using vibe-coding or SWE-agent workflows apply it to fit more code into context at lower token cost.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/ai-coding-style-guides.md)
