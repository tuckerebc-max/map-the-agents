# Webwright (`webwright`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: microsoft
- License: MIT
- Language: Python
- Interface: platforms=Web; install=pip
- Model providers: OpenAI, Anthropic, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [microsoft/webwright](../../repos/microsoft/webwright.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Code-as-action browser agent: instead of predicting one browser action at a time, the LLM writes and debugs Playwright scripts via a terminal, treating the browser as disposable and code+logs as the persistent workspace artifact. Ultra-minimal (~450-line core, no hidden frameworks — just httpx/pydantic/playwright/typer). Skill Factory distills solved scripts into reusable, verified, parameterized code skills that run standalone without a model. ...

(captured site page body (agents/webwright.md), not a verified repo-code finding)
Webwright, a Microsoft Research project, replaces the conventional web-agent loop of predicting one click or keystroke in a persistent browser with code-as-action: the model writes and debugs Python Playwright scripts in a terminal, treating each browser as disposable and the local workspace of code, logs, and screenshots as the durable state. The harness is deliberately minimal — a roughly 450-line core loop with httpx and pydantic as the only core dependencies — and it ships plugin manifests for Claude Code and OpenAI Codex plus skills for OpenClaw and Hermes Agent, all sharing one skills folder. On Online-Mind2Web it reaches 86.7% with GPT-5.4, and on the long-horizon Odysseys benchmark it set a reported SOTA of around 60% with GPT-5.4. Its Skill Factory distills solved tasks into parameterized CLI tools that rerun with zero tokens, lifting WebArena accuracy from 55% to 70%. It is aimed at researchers building browser agents on top of coding models.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/webwright.md)
