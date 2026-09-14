# tokenjuice (`tokenjuice`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: vincentkoc
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g tokenjuice  (or brew tap vincentkoc/tap && brew install tokenjuice)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [vincentkoc/tokenjuice](../../repos/vincentkoc/tokenjuice.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Deterministic, rule-driven output compactor (JSON rules, not LLM vibes) for terminal-heavy agent workflows. Runs commands, observes output, and returns a smaller payload — reducing transcript waste across 80+ agent/IDE integrations via thin host adapters. Raw output bypass via --raw/--full. Most host integrations install a hook/rule/guidance file (Claude Code, Codex, Cursor).

(captured site page body (agents/tokenjuice.md), not a verified repo-code finding)
TokenJuice attacks the token waste produced when agents run noisy commands — git status dumps, test suites, docker builds — by intercepting command output and returning a compacted version before it reaches the model's context. Compression is deterministic: rule files written in JSON describe what to keep, elide, or summarize per command, so behavior is auditable and reproducible rather than an LLM paraphrase, and raw output remains reachable via explicit --raw/--full flags or stored artifacts. Distribution is the distinctive part: tokenjuice install writes host-native integration files — a Claude Code hook in settings.json, Codex/Cursor rules, plugin entries for OpenCode and others — covering roughly 100 hosts, so the same rules apply across editors, CLIs, and CI. The project is MIT-licensed TypeScript, installable via npm or Homebrew, with docs covering the adapter spec and rule format. Teams running terminal-heavy agent workflows who want lower token spend without behavioral unpredictability are the target users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tokenjuice.md)
