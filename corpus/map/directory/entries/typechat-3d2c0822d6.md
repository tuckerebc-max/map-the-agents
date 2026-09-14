# TypeChat (`typechat`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: microsoft
- License: MIT
- Language: TypeScript, Python, C#
- Interface: install=npm
- Model providers: OpenAI, Azure OpenAI, and OpenAI-compatible endpoints
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [microsoft/typechat](../../repos/microsoft/typechat.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Library (not a coding agent) that replaces prompt engineering with schema engineering. Developers define TypeScript types representing application intents; TypeChat constructs prompts using these types, validates LLM responses against the schema, repairs non-conforming outputs, and summarizes results. Eliminates complex decision trees and fragility of traditional prompt engineering. Available in TypeScript, Python, and C#/.NET.

(captured site page body (agents/typechat.md), not a verified repo-code finding)
TypeChat exists because wiring natural-language input to application actions through prompt engineering grows fragile as intents multiply. The library inverts the approach: the developer declares intents as TypeScript types (discriminated unions, meta-schemas), and TypeChat constructs prompts from those types, validates each model response against the schema, and drives repair loops with the model when validation fails before returning a typed instance the application can dispatch on. A final programmatic summarization step confirms the parsed intent matches what the user asked, without another model call. Teams building chat interfaces over existing APIs use it for intent routing and command parsing rather than autonomous agent loops; it is MIT-licensed, installable via npm, and maintained at a reduced pace by Microsoft.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/typechat.md)
