# picocode (`picocode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: jondot
- License: MIT
- Language: Rust
- Interface: install=curl -sSfL https://raw.githubusercontent.com/jondot/picocode/main/install.sh | sh
- Model providers: Anthropic, OpenAI, DeepSeek, Google (Gemini), Ollama, and many more via Rig
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [jondot/picocode](../../repos/jondot/picocode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Tiny single-binary Rust agent; persona-driven (architect, security, zen, hacker, etc.); recipe-based automation for CI/CD; multi-LLM sovereignty; safety-first (destructive actions require confirmation); usable as CLI or Rust library.

(captured site page body (agents/picocode.md), not a verified repo-code finding)
picocode came out of the observation that most coding agents are heavy Node.js applications, and some jobs — CI codemods, unattended pipeline fixes — need something closer to a Unix tool. The Rust binary wraps a complete agent loop: file edits, shell commands, confirmation gates for destructive actions, and a --yolo flag for unattended runs, with a tool-call limit bounding runaway loops. Personas swap the agent's expertise and voice on a flag (architect, security, sre, tester, hacker), and recipes define named non-interactive tasks in picocode.yaml with prompt, persona, and model, invoked in pipelines. Model access spans Anthropic, OpenAI, DeepSeek, Gemini, and Ollama through the Rig library, and the same binary embeds as a Rust library. The project is early and small (14 commits, 60 stars, no releases yet), aimed at developers who want a minimal, auditable agent for CI rather than a full IDE companion.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/picocode.md)
