# AgentFlow (`agentflow`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: lupantech
- License: MIT
- Language: Python
- Interface: platforms=Web; install=pip
- Model providers: OpenAI, DashScope (Qwen), Gemini, DeepSeek, Together AI, vLLM (local)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [lupantech/agentflow](../../repos/lupantech/agentflow.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A trainable multi-agent framework with four specialized modules (Planner, Executor, Verifier, Generator) coordinated through in-the-flow online optimization via the Flow-GRPO algorithm. A 7B backbone model outperforms GPT-4o on 10 benchmarks. Accepted at ICLR 2026.

(captured site page body (agents/agentflow.md), not a verified repo-code finding)
AgentFlow approaches agentic systems as trainable rather than hand-prompted: four modules (Planner, Executor, Verifier, Generator) share an evolving memory and coordinate through tool calls — python execution, web and Wikipedia search — while the Flow-GRPO algorithm optimizes the planner online against sparse long-horizon rewards. The published results show a 7B backbone outperforming GPT-4o on 10 benchmarks spanning search, agentic, math, and science tasks, with gains of roughly 14-15% on the agentic suites. Models come from OpenAI, Google, DashScope, DeepSeek, Together, or local vLLM, and training configuration lives in train/config.yaml. Researchers in agentic RL and tool use are the users, and the paper was accepted at ICLR 2026.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agentflow.md)
