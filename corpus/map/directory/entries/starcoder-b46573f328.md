# StarCoder (`starcoder`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: BigCode
- License: Apache-2.0 (code); BigCode OpenRAIL-M (model weights)
- Language: Python
- Interface: platforms=API, CLI; install=pip install -r requirements.txt
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [bigcode-project/starcoder](../../repos/bigcode-project/starcoder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A code language model trained on 80+ programming languages plus GitHub issues, commits, and notebooks. Supports 8-bit loading under 20GB RAM and has a C++ implementation (starcoder.cpp). Superseded by StarCoder2; repo inactive since May 2023. A model, not an agent harness.

(captured site page body (agents/starcoder.md), not a verified repo-code finding)
StarCoder was the BigCode community's flagship code model, trained on The Stack v1.2 plus GitHub issues, commits, and notebooks with fill-in-the-middle and an 8,192-token context, and it could be quantized to 8-bit to run under 20GB of RAM. It is a base model, not an instruction follower — the model card warns that direct 'write a function' prompts underperform — and it seeded an ecosystem that included starcoder.cpp for CPU inference. The model is governed by the BigCode OpenRAIL-M license with gated access, and the training corpus and code were released openly to enable audit and repurposing. The lineage continued with StarCoder2 in 2024, and the original repository has been inactive since mid-2023. It is a model, not a harness, and belongs in this census only as a categorization reference.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/starcoder.md)
