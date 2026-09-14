# CodeLlama (`codellama`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Meta AI
- License: Llama 2 Community License
- Language: Python
- Interface: platforms=API, CLI; install=Clone repo, pip install -e . in conda env; download weights via download.sh with signed URL from Meta
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [meta-ai/codellama](../../repos/meta-ai/codellama.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A family of Llama-2-based code models (7B/13B/34B/70B) with code infilling (7B & 13B), up to 100k token input context, and three flavors: foundation, Python-specialized, and instruction-following. State-of-the-art among open code models at release. GitHub repo archived by owner on Jul 1, 2025. A model, not an agent harness.

(captured site page body (agents/codellama.md), not a verified repo-code finding)
Code Llama was Meta's family of code-specialized large language models built on Llama 2, released in sizes from 7B to 70B in three variants: foundation, Python-specialized, and instruction-following. The 7B and 13B variants support infilling for editor-style fill-in-the-middle completion, and all sizes accept input contexts up to 100,000 tokens, which was unusually long for code models at the August 2023 release. The repository provides inference code and a download script for the gated weights rather than any agent tooling; applications consumed the models through their own harnesses. Meta archived the repository on July 1, 2025 as the model line aged out.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codellama.md)
