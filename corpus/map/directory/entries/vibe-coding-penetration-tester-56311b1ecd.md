# vibe-coding-penetration-tester (`vibe-coding-penetration-tester`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: firetix
- License: Apache-2.0
- Language: Python
- Interface: platforms=Web; install=git clone, python -m venv .venv, source .venv/bin/activate, pip install -r requirements.txt, playwright install, cp .env.example .env
- Model providers: OpenAI, Anthropic, Ollama
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: False (reported)

Repository map entry: [firetix/vibe-coding-penetration-tester](../../repos/firetix/vibe-coding-penetration-tester.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): AI-assisted web application security testing tool (VibePenTester) with CLI and Flask web interfaces. Coordinates specialized security agents to discover and validate common web vulnerabilities. Features Playwright-powered browser automation, scope-aware scanning (url/domain/subdomain levels), dual output formats (Markdown + JSON reports), multi-agent scan workflow, and both CLI and web UI/API with session-based orchestration. Note: license discrepancy between README (GPL-3.0) and repo metadata ...

(captured site page body (agents/vibe-coding-penetration-tester.md), not a verified repo-code finding)
The tool exists because 'vibe-coded' applications reach production without security validation, and existing scanners miss logic-level vulnerabilities that require realistic interaction. Its workflow assigns specialized agents to a scan: discovery enumerates the target within a scope (url, domain, or subdomain), a planning agent prioritizes what to test, and vulnerability-testing agents probe common web vulnerability classes through a Playwright-driven browser that interacts with the application as a user would. Findings are validated and written into reproducible Markdown and JSON reports per target, with a Flask web UI and REST API available for session-based operation and sample reports plus a Juice Shop walkthrough included. Security-minded developers testing their own or authorized applications are the users; the project is Python-based, carries CI and a substantial test suite, and warns explicitly that it must only be used against owned or authorized targets.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibe-coding-penetration-tester.md)
