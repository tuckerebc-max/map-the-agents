# deep-swe (`deep-swe`)

[Back to directory index](../index.md)

Directory membership: backing-only.

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

(backing feed `description`, not a verified repo-code finding)
DeepSWE is a benchmark for measuring frontier coding agents on realistic, long-horizon software engineering work. Each of its 113 tasks comes from a live open-source repository — spanning TypeScript,
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
