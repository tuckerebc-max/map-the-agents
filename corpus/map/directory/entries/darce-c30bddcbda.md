# Darce (`darce`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: AmerSarhan
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm install -g darce-cli
- Model providers: qwen, x-ai (Grok), anthropic (Claude), google (Gemini), deepseek, meta-llama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: no (no)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [amersarhan/darce-cli](../../repos/amersarhan/darce-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-based AI coding agent — 14 kB package, 3-second install, smart model routing/switching, works in any terminal, supports any model. Reads, writes, edits code, runs shell commands, and searches codebases. Free tier available.

(captured site page body (agents/darce.md), not a verified repo-code finding)
Darce exists to strip a terminal coding agent down to the smallest practical footprint: a 14 kB TypeScript package that installs in seconds and ships seven tools (Read, Write, Edit, Bash, Glob, Grep, WebFetch) rather than the sprawling feature sets of Claude Code-class harnesses. Requests route through a hosted API to models including Qwen3 Coder, Grok, Claude Sonnet, Gemini, DeepSeek, and Llama 4, with free and paid request quotas, and the CLI adds session resume, context compaction, and cost tracking on top. The target user is someone on constrained hardware or bandwidth who wants basic agentic editing without a large install. Development has stalled — 15 commits, no releases, and a comparison table whose 'open source' claim the repo does not clearly support — so it functions best as a minimalist reference.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/darce.md)
