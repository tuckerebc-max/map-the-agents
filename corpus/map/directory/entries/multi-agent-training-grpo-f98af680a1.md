# multi-agent-training-grpo (`multi-agent-training-grpo`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: FareedKhan-dev
- License: MIT
- Language: Python
- Interface: install=pip install dependencies (vllm, openai, pydantic, tenacity, beautifulsoup4, wikipedia, google-genai, transformers, peft, etc.)
- Model providers: vLLM (local), OpenAI API, Google Gemini API, Qwen models
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [fareedkhan-dev/multi-agent-training-grpo](../../repos/fareedkhan-dev/multi-agent-training-grpo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Implements GRPO (Generalized Reinforced Policy Optimization) algorithm to train multi-agent systems, improving planning and reducing hallucinations in long-horizon tasks through group-based trajectory evaluation and relative advantage learning.

(captured site page body (agents/multi-agent-training-grpo.md), not a verified repo-code finding)
The repository teaches a specific technique: reinforcement learning applied to the planning component of an agent system, using GRPO's group-relative advantage computation to improve long-horizon task performance. Three notebooks walk the full path — combining DeepMath-103K math problems with Natural Questions queries into training data, building a Planner/Executor/Verifier agent system over a vLLM-hosted Qwen model with sandboxed Python execution and search tools, and then training the planner with GRPO where GPT-4o scores trajectory outcomes and group-relative advantages drive policy updates through QLoRA on a single A100. The demo deliberately shows the untrained planner hallucinating — wrong tool order, wrong conclusions — before training. It is a blog-post companion from a prolific tutorial author, six commits and dormant, intended for readers learning how RL fits into agentic systems rather than for any production use.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/multi-agent-training-grpo.md)
