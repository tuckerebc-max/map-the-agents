# OpenRath (`openrath`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: Rath-Team
- License: BSD-3-Clause
- Language: Python
- Interface: install=pip
- Model providers: OpenAI, Anthropic (OpenAI-compatible providers)
- Feature flags (directory-reported):
  - mcp_support: yes — stdio MCP tools adapted into the loop as FlowToolCall instances (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes — multi-agent collaboration; agents share session state; sessions can be forked/merged across agents with lineage tracking (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [rath-team/openrath](../../repos/rath-team/openrath.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): PyTorch-like runtime for dynamic multi-agent and multi-session workflows — Session as the central flowing value (like a Tensor); composable agents like nn.Linear; durable execution with checkpointing, leases, effect ledgers, and human-in-the-loop interrupts.

(captured site page body (agents/openrath.md), not a verified repo-code finding)
Multi-agent frameworks typically ask developers to express workflows in graphs or YAML, which hides control flow behind DSLs and makes state hard to inspect. OpenRath instead imports PyTorch's vocabulary: a Session is the value that flows between components the way a Tensor does, agents compose like nn.Linear layers, workflows nest like nn.Module, memories persist like Parameters, and tools are plain callables — while if/while remain ordinary Python, with an LLM-backed Selector handling only genuine routing decisions. Version 2.0 adds production machinery: checkpoints, leases, an effect ledger, human interrupts, and an Agent Server mode backed by PostgreSQL, Redis, and S3. It installs from PyPI (pip install openrath) with optional sandbox and server extras, documents itself at docs.openrath.com, and publishes an arXiv paper. Python engineers building durable multi-session agent applications, rather than terminal coding users, are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/openrath.md)
