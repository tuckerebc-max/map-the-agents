# Syncode (`syncode`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: structuredllm
- License: MIT
- Language: Python
- Interface: install=pip install syncode (or pip install git+https://github.com/structuredllm/syncode.git)
- Model providers: HuggingFace models (code, chat, instruct)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry (renamed): original lead [uiuc-focal-lab/syncode](https://github.com/uiuc-focal-lab/syncode) (source: backing, field: `source_code_url`) now resolves to [structuredllm/syncode](../../repos/structuredllm/syncode.md) (github id 687211074, verified [https://github.com/structuredllm/syncode](https://github.com/structuredllm/syncode)).

## Description

Highlight (site page `what_makes_it_special`): Grammar-guided generation framework for LLMs ensuring outputs are syntactically valid per Context-Free Grammars (CFG) and Regex. Pre-computes masks for speed (~10% overhead), handles general-purpose languages including non-context-free fragments (Python indentation, Go end-of-scope), and reports 99% JSON accuracy with Gemma-2b.

(captured site page body (agents/syncode.md), not a verified repo-code finding)
SynCode is a constrained-decoding library from UIUC that forces LLM output to conform to a Context-Free Grammar, with soundness and completeness guarantees — every produced token sequence satisfies the grammar. It works as a logit processor over HuggingFace models: an incremental LR(1)/LALR(1) parser tracks grammar state, and a pre-computed DFA mask store hides invalid tokens at each step, adding roughly 10% generation overhead while reporting 99% JSON validity with small models. Built-in grammars cover Python, Go, Java, SQL, and JSON, and the framework handles constructs beyond plain CFGs, such as Python's indentation-sensitivity and Go's brace-scoping. It ships as a pip package aimed at researchers generating structured or syntactically valid code, with the design published in an arXiv paper (2403.01632). It is not an agent: there is no tool loop, only constrained decoding.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/syncode.md)
