# atomic (`atomic`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: bastani-inc
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: OpenAI, Anthropic, GitHub Copilot, OpenRouter, xAI, DeepSeek, Google Gemini, Google Vertex, Azure OpenAI, Bedrock, Mistral, Groq, Cerebras, Cloudflare, Ollama, llama.cpp, LM Studio, vLLM, SGLang
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [bastani-inc/atomic](../../repos/bastani-inc/atomic.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Verifiable coding agent runtime — build engineering processes as explicit, checkable execution graphs (workflows) with stages, checks, artifacts, and approval gates. Fork of Pi. Core differentiator is verification built into the execution model: explicit DAG execution graphs, executable checks & review gates (failures route into bounded repair loops), durability & resume (runs checkpoint to disk), human-in-the-loop approval gates anywhere in ...

(captured site page body (agents/atomic.md), not a verified repo-code finding)
Atomic, by bastani-inc, is a fork of Pi focused on making coding-agent behavior verifiable instead of hopeful. Engineering processes are defined as explicit execution graphs in TypeScript workflow files, with stages that can prompt agents, run tools, save artifacts, branch, run in parallel, retry within bounds, and checkpoint so runs survive interruption. Executable checks and fresh reviewers generate evidence, and failures route into bounded repair loops until gates pass, with human approval gates placeable anywhere in the graph. Nine specialist subagents cover workers, debugging, codebase analysis, and research, running in worktree-isolated parallel, and bundled workflows include fan-out-and-synthesize, adversarial-verification, loop-until-done, goal, and ralph loops. It stays Pi-compatible with providers, MCP servers, skills, and extensions, is installed via npm or a self-contained install script, and targets teams wanting deterministic, auditable agent pipelines.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/atomic.md)
