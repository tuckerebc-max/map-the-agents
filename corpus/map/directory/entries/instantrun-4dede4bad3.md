# Instantrun (`instantrun`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Talha-Ali-5365
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=Ensure Python 3.10+, Docker, Alacritty installed; pip install -r requirements.txt; set OpenAI API key in instantrun.py; run python main.py
- Model providers: OpenAI (gpt-4o-mini)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [talha-ali-5365/instantrun](../../repos/talha-ali-5365/instantrun.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-powered agent that autonomously deploys any GitHub repository on a user's local machine. Uses LangGraph workflow to clone, set up, and run repos with intelligent error handling and Dockerized environment for isolated execution. Only 6 commits.

(captured site page body (agents/instantrun.md), not a verified repo-code finding)
InstantRun automates the 'clone it and get it running' chore that costs every developer time on unfamiliar repositories. A LangGraph workflow extracts key files and README setup instructions, drafts a Dockerized build-and-run plan, executes it, and loops failures back through an LLM that edits the Dockerfile or commands before retrying. Output streams through an Alacritty terminal, and execution stays isolated inside a container. It is a solo experiment — six commits, Arch Linux oriented, gpt-4o-mini only — and has been dormant since January 2025, but it documents a complete agentic deploy loop.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/instantrun.md)
