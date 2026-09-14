# AutoStartup (`autostartup`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: jawerty
- License: unknown
- Language: Python
- Interface: platforms=IDE; install=pip3 install -r requirements.txt && python3 main.py (or Google Colab notebook)
- Model providers: Llama 2 (via HuggingFace)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [jawerty/autostartup](../../repos/jawerty/autostartup.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 100% Llama 2 inference with no OpenAI API keys needed; autonomously generates startup ideas, business plans, and React codebases from simple user intuition using lean startup methodologies (criticize loops, investor approval, pivoting).

(captured site page body (agents/autostartup.md), not a verified repo-code finding)
AutoStartup was a 2023 experiment by jawerty (Jared Vasquez) exploring whether a startup could be generated end-to-end from a one-line intuition using only locally hosted Llama 2 - no OpenAI keys. A criticize-revise-pitch loop (AutoGPT-style) iterates a business plan against an investor prompt until approval, then generates a React codebase via the author's 10x-React-Engineer project, with vector-search memory pairing past successes and criticisms into future pitches. Llama 2 13B inference runs locally or via a provided Colab notebook, making the whole pipeline local and key-free. The project was a demo built during a livestream, is admittedly buggy, and has seen only six commits. It is of historical interest as an early fully-local autonomous startup generator rather than a maintained tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/autostartup.md)
