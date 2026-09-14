# Smol Developer (`smol-developer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: smol-ai
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: OpenAI (GPT-4-0613, GPT-3.5-turbo-0613)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [smol-ai/developer](../../repos/smol-ai/developer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Human-centric AI scaffolding agent that generates entire codebases from a product spec. Whole-program coherence via an intermediate shared_dependencies.md step where GPT maintains cross-file consistency. First embeddable developer agent library with importable functions (plan, specify_file_paths, generate_code). Markdown-is-all-you-need philosophy. Three usage modes: Git repo (CLI), library (Python import), API (Agent Protocol server).

(captured site page body (agents/smol-developer.md), not a verified repo-code finding)
Smol Developer addressed the failure mode of early code-generation agents, where independently generated files hallucinated incompatible interfaces. Its pipeline plans a shared dependencies document, uses OpenAI function calling to guarantee a valid file list, then generates each file with that document pinned into the prompt so the model effectively talks to itself across files. Humans stay in the loop by running the output, pasting errors back into the prompt, or using debugger.py to feed the whole codebase plus an error for fix suggestions. It shipped as a repo, an importable pip library, and an Agent Protocol API server, and at 12k stars it was one of the defining scaffolding agents of the 2023 GPT-4 era. Development stopped around 2024 and the code still targets the gpt-4-0613 era.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/smol-developer.md)
