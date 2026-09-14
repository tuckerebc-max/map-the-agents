# intentlang (`intentlang`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: l3yx
- License: MIT
- Language: Python
- Interface: install=pip install intentlang | uv add intentlang
- Model providers: Any OpenAI-compatible (DeepSeek, Alibaba DashScope, Zhipu BigModel)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [l3yx/intentlang](../../repos/l3yx/intentlang.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): AI-Native, Intent-Oriented Programming Language built on Python; first framework to formally represent human intent as structured elements (Intent IR: Goal, Contexts, Tools, Input, Strategy, Constraints, Output); AI generates and executes Python code directly in the host runtime manipulating real objects without serialization (abandons function calling); data/instruction separation eliminates token limit/cost issues; embedded execution shares host process space (DB connections, browser ...

(captured site page body (agents/intentlang.md), not a verified repo-code finding)
Intentlang replaces the tool-call round trip with embedded code execution: the model receives an intent's metadata (never the data), generates Python, and that code manipulates real host objects — live database connections, browser sessions — through an embedded REPL with top-level await and error self-correction. The Intent IR (goal, contexts, tools, input, strategy, constraints, output) structures what the model sees, and data never enters the prompt, which sidesteps token costs on large inputs. Any Python object can serve as a tool, so frameworks integrate by injection rather than adapter. It targets developers building agents who find function-calling loops lossy, though executing model-written code demands sandboxing; the project remains a young solo experiment.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/intentlang.md)
