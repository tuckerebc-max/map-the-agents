# deep-swe (`deep-swe`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: datacurve-ai
- License: Apache-2.0
- Language: TypeScript, Go, Python, JavaScript, Rust (task corpus); Python (harness)
- Interface: install=pip
- Model providers: Anthropic (Claude Opus 4.8), OpenAI (GPT-5.5); supports multiple CLI agents
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a - Pier drives Claude Code directly as one of several supported agents (reported)
  - subagents: no (no)
  - hooks: yes - \[\[verifier.collect\]\] hook in each task.toml extracts agent commits as a patch for grading (yes)
  - plan_mode: no (no)

Repository map entry: [datacurve-ai/deep-swe](../../repos/datacurve-ai/deep-swe.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Benchmark for frontier coding agents on original, long-horizon software engineering tasks drawn from active open-source repos (113 tasks across 5 languages). Real-world tasks rather than synthetic/curated examples, designed for multi-step sustained engineering. Behavior-based verification: accepts any solution with correct observable behavior regardless of internal structure/symbol names - reference patches held out and never used at grading time. Uses a fork ...

(captured site page body (agents/deep-swe.md), not a verified repo-code finding)
DeepSWE is a benchmark for measuring frontier coding agents on realistic, long-horizon software engineering work. Each of its 113 tasks comes from a live open-source repository — spanning TypeScript, Go, Python, JavaScript, and Rust — and ships as a Harbor-format package with an isolated Docker environment and a programmatic verifier, so scores reflect whether real tests pass rather than model self-assessment. The companion Pier harness executes candidate agents (mini-swe-agent, Claude Code, Codex, Gemini CLI, opencode) with per-agent network allowlists, optionally on Modal sandboxes. Datacurve publishes the leaderboard from Pier runs of mini-swe-agent; benchmark consumers are AI labs and teams comparing agents under identical, reproducible conditions.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/deep-swe.md)
