# Agents (`agents`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: aiwaves-cn
- License: Apache-2.0
- Language: Python
- Interface: platforms=Autonomous, IDE, Web; install=pip
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aiwaves-cn/agents](../../repos/aiwaves-cn/agents.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): A data-centric, self-evolving autonomous language agent framework (Agents 2.0) that applies the connectionist learning procedure to agent training. Makes an analogy where the agent pipeline is a computational graph, nodes are layers, and prompts/tools are weights — implementing back-propagation and gradient-based weight update using 'language loss', 'language gradients', and 'language weights'. Can optimize multi-agent systems by treating nodes as different ...

(captured site page body (agents/agents.md), not a verified repo-code finding)
Agent pipelines are usually hand-tuned, and the AIWaves team asked whether the training machinery of neural networks could be transplanted to prompts and tools. In Agents 2.0 the pipeline is treated as a computational graph: execution records trajectories per node, a prompt-based language loss scores outcomes, and backward propagation yields textual 'language gradients' used to rewrite each node's prompts and tools — and to add or remove nodes. Because nodes can themselves be agents, multi-agent systems are optimized as a unit. The framework is a Python library installed from source, accompanied by the arXiv paper 2406.18532. Activity has concentrated around the June 2024 Agents 2.0 release, with the codebase largely stable since.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agents.md)
