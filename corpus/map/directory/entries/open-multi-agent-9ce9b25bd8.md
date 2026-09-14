# open-multi-agent (`open-multi-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: open-multi-agent
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: OpenAI, Anthropic, Google Gemini, DeepSeek, Ollama, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: partial (reported)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [open-multi-agent/open-multi-agent](../../repos/open-multi-agent/open-multi-agent.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): 'Describe the goal, not the graph' — the coordinator agent builds the task DAG at runtime from the goal rather than hand-wiring workflow graphs. Controlled execution lets users preview/approve/durably suspend plans, task dispatches, and tool calls; approved plans can be frozen for deterministic replay. Built-in offline Run Viewer, resume from checkpoints, append-only plan repair, and air-gapped/offline capability.

(captured site page body (agents/open-multi-agent.md), not a verified repo-code finding)
Multi-agent frameworks typically require developers to hand-wire workflow graphs before knowing what the work actually requires, which makes them brittle for open-ended goals. Open Multi-Agent (OMA), a TypeScript library for Node.js backends, replaces the fixed graph with a coordinator that plans a task DAG at runtime from a plain goal, then executes it with a deterministic scheduler. Every layer is inspectable: plans, task dispatches, and tool calls can be previewed and approved, runs durably suspend and resume, and approved plans freeze for replay through an offline Run Viewer with span waterfalls. Reliability features — checkpoint/resume, append-only plan repair, retries, loop detection, token and cost budgets, multi-agent consensus verification — target production use, and external agents like Claude Code, Gemini CLI, and Codex join the same DAG via process and ACP backends. It installs as @open-multi-agent/core or via a create-oma-app scaffold and suits backend teams building reliable multi-agent systems in TypeScript.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-multi-agent.md)
