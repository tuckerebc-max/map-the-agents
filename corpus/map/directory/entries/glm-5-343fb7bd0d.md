# GLM-5 (`glm-5`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: zai-org
- License: Apache-2.0
- Language: Python
- Interface: install=binary
- Model providers: Z.ai API platform, z.ai chat, open weights on Hugging Face/ModelScope
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [zai-org/glm-5](../../repos/zai-org/glm-5.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Series of large language models (GLM-5/5.1/5.2) targeting complex systems engineering and long-horizon agentic tasks. GLM-5.2 delivers a solid 1M-token context, 744B params (40B active), IndexShare architecture reducing per-token FLOPs 2.9x at 1M context, and DeepSeek Sparse Attention. Best-in-class open-source coding/agentic performance.

(captured site page body (agents/glm-5.md), not a verified repo-code finding)
The GLM-5 series (GLM-5, 5.1, 5.2, 5.3, 5.3-Flash) is Z.ai's open-weight model line aimed squarely at coding and long-horizon agentic workloads, with 28.5T pre-training tokens, DeepSeek Sparse Attention, and an IndexShare architecture that cuts per-token FLOPs 2.9x at million-token context. The repository ships weights (BF16 and FP8 variants on Hugging Face and ModelScope) plus serving and fine-tuning recipes for SGLang, vLLM, Transformers, and KTransformers, with hosted access via the Z.ai API platform. Benchmarks position it as the leading open-source model for coding and long-horizon agent tasks. In this census it is a model, not a harness: the agentic loops live in downstream tools that consume these weights.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/glm-5.md)
