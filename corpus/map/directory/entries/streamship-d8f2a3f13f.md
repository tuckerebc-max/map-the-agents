# Streamship (`streamship`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: steamship-core
- License: MIT
- Language: Python
- Interface: platforms=CLI, Web; install=pip install steamship
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [steamship-core/python-client](../../repos/steamship-core/python-client.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Python SDK for the Steamship platform to build, scale, and monitor AI Agents, with a triad of deployable components (Agents, Packages, Plugins). LangChain-compatible via a separate library and supports multimodal agents.

(captured site page body (agents/streamship.md), not a verified repo-code finding)
The Steamship Python client was the entry point to a hosted platform that handled deployment, scaling, and monitoring for agents: developers wrote Agents with reasoning loops, Packages that exposed them as APIs, and Plugins for reusable capabilities, and the platform ran them as managed services. A separate compatibility library connected it to LangChain, and starter templates covered multimodal agents. The SDK is MIT-licensed, installs via pip, and documents itself at docs.steamship.com. No releases have appeared since early 2024 and the surrounding platform has gone quiet, so the project stands as a representative artifact of the 2021-2023 wave of hosted agent platforms rather than a current option.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/streamship.md)
