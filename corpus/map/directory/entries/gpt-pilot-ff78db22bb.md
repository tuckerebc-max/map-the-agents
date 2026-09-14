# GPT Pilot (`gpt-pilot`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Pythagora-io
- License: Source Available
- Language: Python
- Interface: platforms=CLI; install=git clone, python3 -m venv venv, source venv/bin/activate, pip install -r requirements.txt, cp example-config.json config.json, python main.py. Also available as VS Code extension.
- Model providers: OpenAI, Anthropic, Groq (Azure & OpenRouter via OpenAI setting)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [pythagora-io/gpt-pilot](../../repos/pythagora-io/gpt-pilot.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Builds fully working, production-ready apps step-by-step using 11 specialized AI agents (Product Owner, Specification Writer, Architect, Tech Lead, Developer, Code Monkey, Reviewer, Troubleshooter, Debugger, Technical Writer). The repository is explicitly no longer maintained.

(captured site page body (agents/gpt-pilot.md), not a verified repo-code finding)
GPT Pilot set out to have AI write roughly 95% of an application while a human developer supervised, decomposing work through a pipeline of eleven role agents — specification writing, architecture, development, code review, debugging, documentation — so that each step stayed reviewable. It ran as a Python CLI (also packaged as the Pythagora VS Code extension) against OpenAI, Anthropic, or Groq keys, storing task state in SQLite or PostgreSQL. The repository is now explicitly unmaintained, and a security notice documents a supply-chain worm planted in core/telemetry/ between August 24, 2025 and June 11, 2026, with instructions to rotate credentials and check for indicators of compromise. Its successor is the commercial Pythagora extension, and running the old repo from source is discouraged.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gpt-pilot.md)
