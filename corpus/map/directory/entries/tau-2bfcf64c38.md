# Tau (`tau`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: huggingface
- License: MIT
- Language: Python
- Interface: platforms=CLI, IDE; install=pip
- Model providers: OpenAI, Anthropic, OpenRouter, Hugging Face, local
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [huggingface/tau](../../repos/huggingface/tau.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Small, readable terminal coding agent — a Python port of Pi's minimalist coding agent — that reads, edits, and runs commands with durable JSONL sessions; also serves as a teaching project for how coding-agent systems are built.

(captured site page body (agents/tau.md), not a verified repo-code finding)
Tau is Hugging Face's Python port of the Pi minimalist coding agent, published both as a usable terminal agent and as a reference for how coding agents are constructed. The package splits into tau_ai (a provider-neutral event stream over OpenAI, Anthropic, Codex, OpenRouter, HF, and OpenAI-compatible endpoints), tau_agent (the harness loop, tools, and durable JSONL sessions with resume and branching), and tau_coding (the Textual TUI, one-shot print mode, file/shell tools, skills, and AGENTS.md project instructions). Context accounting with manual and automatic compaction keeps long sessions coherent, and providers are configured through a catalog file rather than code. Because the 'brain' is decoupled from the interface, the project doubles as teaching material — the docs site walks through the architecture — and the README states the goal of showing how coding agents work. Developers who want a small, inspectable agent they can read and modify, rather than a maximalist product, are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tau.md)
