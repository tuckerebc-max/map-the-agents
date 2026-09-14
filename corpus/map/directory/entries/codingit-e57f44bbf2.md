# CodingIT (`codingit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Gerome-Elassaad
- License: Apache-2.0
- Language: TypeScript
- Interface: install=git clone https://github.com/Gerome-Elassaad/CodingIT.git && npm install && npm run dev
- Model providers: OpenAI, Anthropic, Google Generative AI, Google Vertex AI, Mistral, Groq, Fireworks, Together AI, Ollama, xAI, DeepSeek
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [gerome-elassaad/codingit](../../repos/gerome-elassaad/codingit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI app builder prototype using E2B cloud sandboxes for secure code execution; supports multiple tech stacks (Python, Next.js, Vue, Streamlit, Gradio) and custom LLM personas; add custom LLM providers via JSON config.

(captured site page body (agents/codingit.md), not a verified repo-code finding)
Hosted prompt-to-app products keep their generation and execution machinery behind a hosted product, leaving developers who want to study or self-host the pattern without a reference implementation. CodingIT fills that role as an open Apache-2.0 prototype: a Next.js 14 application streams model output into E2B cloud sandboxes where the generated code actually runs, with npm and pip installation available inside the sandbox boundary. Target stacks - Next.js, Vue, Streamlit, Gradio, Python data analysis - are defined as E2B sandbox templates, so adding a stack means writing a Dockerfile rather than modifying application code. Eleven model providers from OpenAI and Anthropic to Groq and Ollama are configured through a single models file. Developers studying the app-builder pattern, or E2B's sandbox model, use it as a starting codebase; the author's newer desktop project, CodinIT.dev, continues the line.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codingit.md)
