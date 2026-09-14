# L2MAC (`l2mac`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: samholt
- License: MIT
- Language: Python
- Interface: install=pip install --upgrade l2mac
- Model providers: OpenAI (gpt-4o), Azure, others via ApiType config
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [samholt/l2mac](../../repos/samholt/l2mac.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First practical LLM-based von Neumann-architecture stored-program automatic computer; uses a self-bootstrapped prompt-program where each instruction step is loaded into a new LLM agent to execute, with persistent file-store memory, error correction, and unit test generation; 90.2% Pass@1 on HumanEval; accepted at ICLR 2024.

(captured site page body (agents/l2mac.md), not a verified repo-code finding)
L2MAC came out of research at the University of Cambridge on a recurring problem in 2024: a single LLM context window could not hold a whole codebase or book, so outputs degraded as they grew. Its control unit executes a stored prompt-program instruction by instruction, each step in a fresh agent context, with read/write tools against a persistent file store and self-generated unit tests to catch and fix errors. The code instantiation produced entire codebases (a playable Pygame game, a URL shortener) from one prompt, and the paper reported 90.2% Pass@1 on HumanEval. The project is cited for its architecture idea but has seen no meaningful development since mid-2024.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/l2mac.md)
