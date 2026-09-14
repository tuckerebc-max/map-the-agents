# Multi-Agent-AI-System (`multi-agent-ai-system`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: FareedKhan-dev
- License: MIT
- Language: Python
- Interface: install=git clone, pip install -r requirements.txt
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [fareedkhan-dev/multi-agent-ai-system](../../repos/fareedkhan-dev/multi-agent-ai-system.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent AI customer support system using LangGraph + LangSmith supervisor-based orchestration with two subagents (music catalog, invoice/billing), human-in-the-loop verification, persistent short/long-term memory, and structured agent evaluation. (Not a coding agent — it's a customer support system tutorial.)

(captured site page body (agents/multi-agent-ai-system.md), not a verified repo-code finding)
This is a tutorial artifact, not a tool: Fareed Khan's repository accompanies a Medium walkthrough of building supervisor-based multi-agent systems with LangGraph and LangSmith, using the Chinook digital-music sample database as its domain. A supervisor routes queries between two ReAct subagents — one for the music catalog, one for invoice and billing — with human-in-the-loop verification interrupting the flow until a customer's identity is confirmed before invoice access, and memory split between short-term checkpointing and a long-term store that persists user music preferences between sessions. LangSmith datasets and evaluators grade final responses, and the write-up compares supervisor versus swarm architectures. The code lives in one notebook plus a utility file, last touched in 2025, and exists to be read alongside the blog post rather than deployed. It entered the census through keyword matching on 'multi-agent system' and is neither a coding agent nor a harness.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/multi-agent-ai-system.md)
