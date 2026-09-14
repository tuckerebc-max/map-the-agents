# LangGraph (`langgraph`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: unknown
- License: unknown
- Language: Python
- Interface: install=pip install -U langgraph  (or uv add langgraph)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Low-level orchestration framework and runtime for long-running, stateful agents; combines deterministic and agentic steps in one graph; durable execution, streaming, human-in-the-loop, persistence, comprehensive memory; inspired by Pregel and Apache Beam; fine-grained control focused on agent orchestration.

(captured site page body (agents/langgraph.md), not a verified repo-code finding)
LangGraph exists because prompt-loop agents fail at production concerns: they lose state across restarts, cannot pause for human approval, and interleave poorly with deterministic logic. It represents workflows as graphs where nodes share state, cycles are first-class, and every step checkpoints to durable storage, so long-running agents survive crashes and resume exactly. Human-in-the-loop interrupts, time-travel debugging, and persistence make it the substrate teams choose when building their own coding agents rather than adopting one. Klarna, Uber, LinkedIn, Elastic, Replit, and Cloudflare have publicly described using it, primarily from Python with a JavaScript port alongside.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/langgraph.md)
