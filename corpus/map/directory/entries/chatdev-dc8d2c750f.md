# ChatDev (`chatdev`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: OpenBMB
- License: Apache-2.0
- Language: Python
- Interface: platforms=IDE; install=pip (uv sync), npm (frontend), docker
- Model providers: BYOK (any LLM provider via configurable API_KEY and BASE_URL)
- Feature flags (directory-reported):
  - mcp_support: yes (mcp_example directory, Blender MCP integration) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [openbmb/chatdev](../../repos/openbmb/chatdev.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A zero-code multi-agent orchestration platform with visual workflow canvas and drag-and-drop agent orchestration; evolved from a 'Virtual Software Company' into a general-purpose platform for data visualization, 3D generation, game development, and deep research.

(captured site page body (agents/chatdev.md), not a verified repo-code finding)
ChatDev began as a research project from Tsinghua NLP and ModelBest simulating a virtual software company: LLM agents take on roles like CEO, CTO, and programmer, collaborating through a chain-shaped 'ChatChain' topology to move a one-line idea through design, coding, testing, and documentation. The project has since broadened beyond software into a general multi-agent platform, releasing ChatDev 2.0 with a drag-and-drop visual workflow canvas where agents are configured via YAML and composed through a web UI, targeting applications from 3D generation and game development to deep research. Under the hood it evolved from chain topologies to DAG-based multi-agent collaboration networks (MacNet) that scale to thousands of agents, backed by a series of research papers and an active OpenBMB community. Researchers in multi-agent collaboration and developers exploring agent-based software automation are its primary users; it is open source under Apache-2.0, installable via pip or Docker, with an MCP example directory included.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/chatdev.md)
