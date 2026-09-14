# Explorer (`explorer`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: invariantlabs-ai
- License: Apache-2.0
- Language: Python
- Interface: install=pip install invariant-ai then run invariant explorer (Docker Compose required)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [invariantlabs-ai/explorer](../../repos/invariantlabs-ai/explorer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A tool for visualizing, exploring, testing, inspecting, and analyzing AI Agent traces.

(captured site page body (agents/explorer.md), not a verified repo-code finding)
Explorer grew out of Invariant Labs' agent-safety research as the local companion to their analysis stack: a Python API (pip install invariant-ai) plus a web UI that ingests agent traces, exposes tool calls and state for inspection, and supports structured comparison across runs. Teams used it to debug agents — locating the exact tool call where a run went wrong, comparing trajectories across model versions, and turning failures into regression test cases. Deployment ran locally via Docker Compose or the pip package with data stored in ./data, keeping traces on the developer's machine. Invariant Labs was absorbed into Snyk's AI security efforts, the hosted version was shut down in January 2026, and development on the repository has ceased.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/explorer.md)
